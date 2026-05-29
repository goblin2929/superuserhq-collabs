# Presenter View for HTML Decks — Design

**Date:** 2026-05-29
**Status:** Approved
**Scope:** `clients/tiket/docs/` — new `presenter.html`, additive change to shared `deck-stage.js`

## Problem

The deck (`beyond-cowork.html`) embeds per-slide speaker notes as a positional JSON
array in `<script type="application/json" id="speaker-notes">`. `deck-stage.js`
parses them into `this._notes` but **never renders them** — it only broadcasts the
slide index via `postMessage({slideIndexChanged})` and a `slidechange` event, for an
external notes renderer that does not exist. There is no way to see the notes while
presenting.

## Goal

A true two-window presenter mode:

- **Projector window** — the existing deck, clean and full-screen.
- **Laptop window** (`presenter.html`) — current slide's notes, next-slide preview,
  slide counter, and a timer.
- **Either window drives** — arrow keys / clicks in either window advance both, in sync.
- **Notes stay single-sourced** in the deck HTML; the presenter receives them, never
  duplicates them.

## Architecture

### Transport: `window.open` + `postMessage`

`presenter.html` is opened first (on the laptop). A button runs
`window.open('beyond-cowork.html')` and keeps the handle. The two windows message
each other directly via `postMessage`. Chosen over `BroadcastChannel` /
`localStorage` storage-events because those are **unreliable across separate
`file://` windows**, and the deck is built to run from `file://`.

When the presenter opens the deck, the deck's `window.opener` is the presenter —
same-origin, so messaging works on both `file://` and `http://`.

### Message protocol

| Direction | Message | Meaning |
|---|---|---|
| presenter → deck | `{type:'presenter-hello'}` | "I'm here, send me everything" (handshake, handles races) |
| deck → presenter | `{type:'deck-payload', notes, labels, total, index}` | Full notes + slide labels + state |
| deck → presenter | `{type:'deck-slide', index, total}` | Slide changed (sent on every nav) |
| presenter → deck | `{type:'deck-nav', action:'next'\|'prev'\|'goto'\|'reset', index?}` | Drive the deck |

Handshake is two-way idempotent: the deck sends `deck-payload` on init (if
`window.opener` exists) **and** in response to any `presenter-hello`, so it doesn't
matter which window finishes loading first.

### Changes to `deck-stage.js` (additive, backward-compatible)

All new behavior is guarded on `window.opener` existing or on receiving a known
message type, so every other deck using the shared component is unaffected.

1. Constructor: bind `_onPresenterMessage`.
2. `connectedCallback`: `window.addEventListener('message', this._onPresenterMessage)`;
   remove it in `disconnectedCallback`.
3. New `_sendToPresenter(msg)` — posts to `window.opener` if present and not self.
4. New `_presenterPayload()` — builds `{notes, labels, total, index}`; `labels`
   derived from each slide's `data-screen-label`.
5. On init (end of mount, after slides collected): if `window.opener`, send payload.
6. In `_applyIndex` broadcast block: also `_sendToPresenter({type:'deck-slide', ...})`.
7. `_onPresenterMessage`: `presenter-hello` → send payload; `deck-nav` → call existing
   `next()` / `prev()` / `goTo()` / `reset()`.

### `presenter.html` (new, self-contained)

Single file, no build step, matches the deck's dark aesthetic.

- **Layout:** "NOW" panel (large, current notes) · "NEXT" strip (next slide label +
  first note line) · footer with `N / total` counter and timer.
- **Notes rendering:** each note string is `"[Both · ~1 min]\n• …\n• …"`. Render the
  leading `[…]` as a cue header (speaker + timing); render `• ` lines as a list.
- **Controls:** ←/→ / PgUp/PgDn / Space / Home drive the deck via `deck-nav` messages;
  on-screen Prev/Next buttons too. An "Open slides ↗" button launches the deck window;
  re-launches if the handle is closed.
- **Timer:** counts up; starts on first advance; click to pause; long-press / dedicated
  button to reset. Presenter-side only.
- **State:** holds `notes`, `labels`, `total`, `index` from the payload; re-renders on
  each `deck-slide`. No notes hardcoded here.

## Out of scope (YAGNI)

- Rendered thumbnail of the next slide (text preview only).
- Editing notes from the presenter.
- Syncing via server / multi-device-over-network (same-machine two-window only).

## Testing / verification

Open `presenter.html`, click "Open slides", confirm:
- notes for slide 1 show immediately;
- advancing in the deck window updates the presenter;
- advancing in the presenter window updates the deck;
- counter and next-preview track correctly across the full 48 slides;
- closing and reopening the deck window re-syncs via handshake.
