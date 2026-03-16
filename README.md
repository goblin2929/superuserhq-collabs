# Novastacks AI and Superuser HQ — Collabs

Multi-client collaboration workspace for creating training content and managing project plans.

## Structure

```
clients/          # One folder per client (lowercase-kebab-case)
  <client>/
    training/     # Training content (guides, code examples, presentations, video scripts)
    docs/         # Active engagement deliverables
shared/
  templates/      # Reusable templates across clients
  resources/      # Shared resources (images, common assets)
docs/
  plans/          # Project plans & proposals (pre-engagement or cross-client)
```

## Adding a New Client

Create a folder under `clients/<client-name>/` with `training/` and `docs/` subfolders:

```bash
mkdir -p clients/<client-name>/training clients/<client-name>/docs
touch clients/<client-name>/training/.gitkeep clients/<client-name>/docs/.gitkeep
```

## Conventions

- Client folder names: lowercase-kebab-case (e.g., `tiket`, `acme-corp`)
- Only text-based content is committed to git
- Large binaries (slide decks, videos) are managed externally
