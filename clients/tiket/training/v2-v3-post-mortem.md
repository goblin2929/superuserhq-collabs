# Post-Mortem: How Deterministic Validation Gates Fixed a Production AI Audit Pipeline

**Date:** April 2026
**Author:** Novastacks AI (internal engineering review)
**Audience:** Engineers and technical marketers building agentic workflows with Claude Code

---

## Executive Summary

Novastacks produces AEO/SEO prospect audit reports using Claude Code skills — structured markdown procedures that orchestrate data collection, scoring, and HTML report generation. Between February and April 2026, multiple client-facing reports shipped with fabricated or inflated numbers. This post-mortem documents the failure classes, the v2→v3 architecture change that fixed them, and the engineering principles behind deterministic validation gates.

The core lesson: **LLMs will fabricate plausible-looking numbers when given ambiguous data sources. The only reliable fix is deterministic Python validation between each pipeline phase.** No amount of prompt engineering prevents a model from picking the wrong field from a JSON file — but `if report_number != file_number: sys.exit(1)` does.

---

## 1. The Problem: What Shipped Wrong in v2

### Gap 1 — Keyword Count Inflation (systemic)

Two DataForSEO endpoints return keyword counts for a domain:

| Endpoint | Field | What it counts | Typical value |
|---|---|---|---|
| `domain_rank_overview` | `metrics.organic.count` | Keywords where domain ranks in top 100 | 2,941 |
| `ranked_keywords` | `total_count` | All keywords including positions 101-200+ | 5,179 |

The v2 Sonnet subagent had both files in its context. No rule specified which to use. It consistently picked the larger number — or worse, blended them into a third number that matched neither source.

**Real examples from production audits:**

| Prospect | v2 reported | Canonical (DRO) | ranked_keywords total_count | v2 error |
|---|---|---|---|---|
| Leica Biosystems | 7,599 | 2,941 | 5,179 | Matches neither source — LLM fabricated |
| Blue Buffalo (historical) | 27,659 | 15,164 | ~27K | Used inflated endpoint |
| Brady Morris | 68 | 24 | — | 2.8x inflated |

The Leica case is the most telling: v2 reported 7,599 keywords, which doesn't match the DRO count (2,941) OR the ranked_keywords count (5,179). The LLM generated a number that looked plausible but was pure fabrication — it split the difference or estimated from partial context.

### Gap 1b — ETV Inflation (same root cause)

| Prospect | v2 ETV | v3 ETV (canonical) | Inflation |
|---|---|---|---|
| Leica Biosystems | $114,202 | $30,826 | 3.7x |
| Kong Dental (historical) | $9,997 | $3,624 | 2.8x |

### Gap 2 — CWV Attribution Swap

The Kong Dental audit reported "Kong Dental's homepage has FCP 2.8 seconds." The actual value was 3.2 seconds. Where did 2.8 come from? It was FDC's (a competitor) FCP value. The report subagent read the wrong lighthouse file.

**Root cause:** The subagent had lighthouse JSON files for all 3 domains in its context. When writing "prospect FCP is X," it grabbed the number from a competitor file without verifying the filename matched the domain being described.

### Gap 3 — Missing CWV

Kong Dental's CLS was 0.473 — **4.7x above Google's 0.1 threshold** — the single most damaging metric in the dataset. The v2 report omitted it entirely. The report mentioned FCP and LCP but skipped CLS with no explanation.

### Gap 5 — Unverified Negative Existence Claims

The Blue Buffalo audit stated "zero defensive content." The brand had a 50-question FAQ page at `/why-choose-blue/frequently-asked-questions/`. The subagent never crawled the sitemap — it assumed absence from the data it had in context meant absence from the site.

### Gap 6 — Content Length Fabrication (discovered this session)

The Brady Morris v3 report (before the fix) claimed the homepage contained "56,525 characters of text content." Tina visited bradymorris.in manually — it's a thin Elementor page with a hero, nav, some product images, and a footer.

**Investigation revealed:**
- Raw HTML: 112,412 chars (includes all markup)
- Body minus `<script>/<style>` tags but WITH HTML tags still included: 42,964 chars
- **Actual visible text (tags stripped): 3,526 chars / 534 words**

The `analyze-pages.py` script used Python's `HTMLParser.handle_data()` which fires for ALL text nodes — including text inside `<script>`, `<style>`, `<noscript>`, and `<svg>` tags. Elementor injects massive framework markup into the body. The script counted JavaScript variable names as "page content."

**Before fix:**
```python
def handle_data(self, data):
    if self.in_script:  # only catches JSON-LD scripts
        self.script_content += data
    else:
        self.current_data += data
        self.all_text += data  # BUG: includes regular <script> and <style> content
```

**After fix:**
```python
def handle_data(self, data):
    if self.in_script:
        self.script_content += data
    elif self._skip_depth > 0:  # inside script/style/noscript/svg
        pass
    else:
        self.current_data += data
        self.visible_text += data  # only human-visible text
```

Impact on Brady Morris homepage: **56,525 → 3,526 chars (16x deflation)**. The report's Section 05 finding title changed from "56,000 Characters of Homepage Text That AI Cannot Read" to "534-Word Homepage in a Market Where AI Needs Depth to Cite." The entire narrative flipped from "content exists but is badly structured" to "barely any content at all."

---

## 2. Architecture: v2 vs v3

### v2 — Single Monolithic Skill

```
prospect-audit-v2.md (~800 lines)
├── Data collection instructions (Phases 0-5)
├── Scoring rubrics
├── Report writing instructions
├── JSON schema
└── HTML rendering call
```

One file. One LLM context window. Data collection → scoring → report → render with no checkpoints between phases. The LLM that collected the data is the same one that writes the report about it. No external verification.

**Analogy:** A single analyst who gathers data, writes the report, and publishes it with no peer review, no fact-check, and no editor.

### v3 — Decomposed Orchestrator with Gates

```
prospect-audit-v3/
├── SKILL.md                              ← Orchestrator (wires phases + gates)
├── skills/
│   ├── prospect-audit-collect.md         ← Data collection only (Phases 0-5)
│   └── prospect-audit-report.md          ← Scoring + report only
├── scripts/
│   ├── analyze-pages.py                  ← Page feature extractor (deterministic)
│   ├── validate_raw_data.py              ← Gate 1: file existence
│   ├── validate_json_output.py           ← Gate 2: schema + self-consistency
│   └── validate_claims_vs_raw.py         ← Gate 3: numbers vs source files
└── references/
    ├── api-patterns.md                   ← Canonical Source Fields table
    ├── report-anti-patterns.md           ← Quality rules from past failures
    ├── market-defaults.md                ← Per-market config
    └── json-schema-full.md               ← Output schema
```

**Pipeline flow:**
```
Collect subagent → Gate 1 → Report subagent → Gate 2 → Gate 3 → HTML renderer
```

Each arrow is a **hard boundary**. The collect subagent cannot influence the report subagent's context. Gate 1 cannot be skipped — it's a Python script with an exit code. If Gate 3 says the keyword count doesn't match the raw file, the render is blocked regardless of how convincing the report prose sounds.

---

## 3. The Validation Gates (Technical Detail)

### Gate 1 — Raw Data Presence (`validate_raw_data.py`)

**What it checks:** Do all expected files exist? Are they non-empty? Do they parse as valid JSON?

**Hard failures:** Lighthouse files (3 required — one per domain). Without these, CWV analysis is impossible.

**Soft warnings:** Sentiment, tech-stack (nice to have but not blocking).

**What it catches:** Incomplete data collection — API failures, rate limits, timeouts.

**What it cannot catch:** Data files that exist and parse correctly but contain wrong values.

```
Exit 0 = all critical files present
Exit 1 = missing critical files (lists which ones)
Exit 2 = usage error
```

### Gate 2 — JSON Schema + Self-Consistency (`validate_json_output.py`)

**Structural checks:**
- 16 required top-level fields present
- Scores in 0-10 range (not 0-100)
- `executive_summary_html` contains `<p>` tags
- `domain_comparison` has exactly 3 entries
- Gated sections have `section_title`, `overlay_title`, `overlay_desc`
- `section_04` has max 3 findings, `section_05` has max 2
- `section_07` has exactly 3 horizons
- No placeholder strings (TBD, TODO, PLACEHOLDER, FILL IN)

**Gap 3 — CWV completeness:**
If ANY section_04 finding mentions FCP or LCP, ALL THREE core metrics (FCP, LCP, CLS) must appear. This catches the Kong Dental bug where CLS 0.473 was silently omitted.

**Gap 5 — Negative existence claims:**
Scans ALL prose for patterns like "no FAQ page", "zero defensive content", "does not exist." Flags for human review.

Excludes (after session patches):
- `readiness_table`, `table_html`, `domain_comparison` paths (these are structured comparison data, not prose claims)
- Findings with positive titles ("First-Mover", "Bright Spot", "Advantage") where negative phrasing refers to competitors

### Gate 3 — Claims vs Raw Data (`validate_claims_vs_raw.py`)

This is the gate that catches fabricated numbers. Added after the Blue Buffalo and Kong Dental audits shipped with hallucinated data that passed Gates 1 and 2.

**Gap 1 — Domain comparison cross-validation:**
```python
for each domain in domain_comparison:
    open {slug}-domain-rank-overview.json
    compare report.ranked_keywords vs raw.metrics.organic.count
    compare report.etv vs raw.metrics.organic.etv (5% tolerance)
    compare report.pos_1 vs raw.metrics.organic.pos_1 (exact match)
```

**Gap 2 — CWV attribution check:**
```python
for each CWV mention in section_04 prose:
    extract the FIRST value after "FCP"/"LCP"/"CLS"
    compare against prospect's lighthouse file
    if it matches a COMPETITOR's lighthouse value instead → attribution error
```

Key design decision: only checks the **first** CWV mention per metric. Later mentions in the same finding are competitor comparisons ("our LCP 5.4s vs their 1.9s") — flagging those would be a false positive.

**Tolerances:**
- ETV: 5% relative tolerance (rounding), absolute $5 tolerance for near-zero values
- CWV: 100ms absolute tolerance for FCP/LCP, 0.01 for CLS
- Keywords: exact match (no tolerance — this is a count, not a measurement)

---

## 4. v2 vs v3 Results (All 5 Prospects)

| Prospect | v2 AEO | v3 AEO | v2 KW (prospect) | v3 KW | v2 ETV | v3 ETV | Key correction |
|---|---|---|---|---|---|---|---|
| Brady Morris | 3.6 | 3.2 | 68 | 24 | $986 | $986 | Keywords from DRO canonical; content_length 56K→534 words |
| Leica Biosystems | 5.6 | 5.8 | 7,599 | 2,941 | $114,202 | $30,826 | Keywords 2.6x deflated; ETV 3.7x deflated |
| Succession Strength | 4.8 | 4.7 | 12 | 7 | $33 | $33 | Keywords corrected; CWV comparison prose validated |
| Supercool Studio Bali | 4.9 | 4.2 | 0 | 0 | $0 | $0 | Content_length fixed; table false positives resolved |
| Findbliss.ai | 1.8 | 1.0 | — | 1 | — | $0 | Full collection from scratch; brand collision found |

**Leica is the proof case.** The v2 report told Benoit Helary his site has 7,599 keywords generating $114K in traffic value. The real numbers: 2,941 keywords, $31K. If he'd cross-checked against Ahrefs or SEMrush, our credibility would be destroyed.

---

## 5. Model Impact: Sonnet vs Opus

The v3 SKILL.md was changed from `model: claude-sonnet-4-6` to `model: claude-opus-4-6` during this session.

| Prospect | Sonnet v3 score | Opus v3 score | Delta |
|---|---|---|---|
| Brady Morris | 5.0 | 3.2 | -1.8 |
| Succession Strength | 6.3 | 4.7 | -1.6 |
| Supercool Studio Bali | 4.4 | 4.2 | -0.2 |

Opus scored consistently stricter. The biggest driver: **Core Keyword Visibility** (35% of LLM Visibility score). Sonnet treated "mentioned at position #7 in a boutique options subsection" as a meaningful citation (~6/10). Opus treated it as barely visible (~3/10).

**Key insight:** Model choice affects analytical judgment (scoring, narrative framing). It does NOT affect data accuracy — that's the pipeline + gates. Use Opus for report generation (better judgment), Sonnet for data collection (cost-efficient, less judgment needed).

---

## 6. Why Decomposed Skills Beat One Big File

### 1. Isolated Context Windows

The collect agent has ~200K tokens for API calls and page crawling. The report agent has ~200K tokens for scoring and writing. A monolithic skill splits that budget across both. When context overflows, the LLM drops instructions silently — and the instructions it drops are usually the boring-but-critical ones ("use `metrics.organic.count`, not `total_count`").

### 2. Deterministic Gates

Python scripts with exit codes cannot be hallucinated past. An LLM can convince itself "I already verified that number." A `sys.exit(1)` cannot be reasoned with. The gate doesn't care how compelling the prose is — if `report_keywords != raw_file_keywords`, the render is blocked.

### 3. Canonical Reference Docs

`api-patterns.md` has a "Canonical Source Fields" table:

| Report claim | Canonical raw file | Canonical field | Common mistake |
|---|---|---|---|
| Total ranked keywords | `{slug}-domain-rank-overview.json` | `items[0].metrics.organic.count` | Using `ranked_keywords.total_count` (inflates 1.5-3x) |
| ETV | `{slug}-domain-rank-overview.json` | `items[0].metrics.organic.etv` | Reading the wrong domain's file |
| FCP / LCP / CLS | `lighthouse-{slug}.json` | `tasks[0].result[0].audits.{metric}.numericValue` | Attributing competitor's value to prospect |

Both sub-skills reference this table. In v2, the canonical mapping was implicit — the LLM decided which field to use each run. In v3, the table makes it explicit and Gate 3 enforces it.

### 4. Failure Isolation

When Gate 3 says "keyword count mismatch for leica," you know the report subagent used the wrong field. You re-run just the report subagent with a FIX MODE prompt pointing at the specific error. In v2, you'd get a finished report with no indication anything was wrong — until a client fact-checked it.

### 5. Retry Semantics

"Re-run the report subagent with corrected page-analysis data" takes 10 minutes and touches nothing else. In v2, re-running means re-collecting all API data (~30 minutes, ~$0.50 in API costs) and hoping the LLM produces a different report.

### 6. Accumulated Learning

`report-anti-patterns.md` grows with each audit failure:
- Blue Buffalo (April 2026): Added "negative existence claims need sitemap verification"
- Kong Dental (April 2026): Added "CWV values must be read from PROSPECT's lighthouse file"
- Brady Morris (April 2026): Added "content_length must come from tag-stripped visible text"

Every bug becomes a documented rule. In v2, learnings lived in conversation context and vanished between sessions.

### 7. Parallel Execution

v3 spawned 3 audit orchestrators in parallel (one per prospect) because each is self-contained with its own data directory and temp files. v2 is serial by nature — one monolithic skill, one execution at a time.

---

## 7. The Proof Chain: How to Verify Any Number

For any numeric claim in a v3 report, the audit trail is:

```
Report JSON (what the client sees)
  ↓ Gate 3 verified against
Raw data file on disk (what the API returned)
  ↓ saved by
Collect subagent (which called the API)
  ↓ validated by
Gate 1 (file exists, parses, non-empty)
```

Example: "Leica Biosystems ranks for 2,941 keywords."

1. Report JSON: `domain_comparison[0].ranked_keywords = "2,941"`
2. Gate 3 opened: `www-leicabiosystems-com-domain-rank-overview.json`
3. Read: `items[0].metrics.organic.count = 2941`
4. Match confirmed: 2,941 == 2,941 → PASS
5. Cross-check: position buckets (pos_1 + pos_2_3 + ... + pos_91_100) sum to 2,941 → self-consistent

No step in this chain involves LLM judgment. Every link is either a file read or an integer comparison.

---

## 8. What's Still Missing (Future Gates)

| Gap | What it would catch | Status |
|---|---|---|
| Gap 4 — Headline SERP verification | "We rank #1 for X" claims that don't match live SERP data | Deferred (discipline rule in anti-patterns.md, not automated) |
| Gap 6 — Content length cross-validation | Section 05 word count claims vs page-analysis-comparison.json | Pipeline fix done, gate not yet built |
| LLM response text archival | Full ChatGPT response text for post-hoc verification | Collect skill saves metadata but not full text |
| Multi-run consistency | Same prospect audited twice should produce similar scores | No regression test framework yet |

---

## Summary

The v2→v3 migration is not about making the LLM smarter. Opus is a better model than Sonnet, but the model upgrade is secondary to the architecture change. The real fix is structural:

1. **Decompose** the monolithic skill into isolated phases
2. **Gate** each phase transition with deterministic Python
3. **Document** canonical data sources so the LLM cannot choose wrong
4. **Accumulate** failure patterns as enforceable rules

An LLM that reads the right file and uses the right field produces accurate reports regardless of model size. An LLM that has ambiguous instructions and no validation will fabricate numbers regardless of how capable it is. The gates make the difference.
