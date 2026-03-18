# Novastacks AI and Superuser HQ — Collabs

Multi-client collaboration workspace for training content and project plans.

## Folder Conventions

- `clients/<name>/training/` — Training content for a client
- `clients/<name>/docs/` — Active engagement deliverables for a client
- `shared/templates/` — Reusable templates across clients
- `shared/resources/` — Shared resources (images, common assets)
- `docs/plans/` — Project plans & proposals (pre-engagement or cross-client)

## Naming

- Client folders: lowercase-kebab-case (e.g., `tiket`, `acme-corp`)
- Only commit text-based content. Large binaries are managed externally.

## Git Workflow

- **Before committing:** Always `git pull origin main` first to avoid conflicts.
- **After committing:** Prompt the user to push (`git push origin main`).

## Adding a New Client

```bash
mkdir -p clients/<client-name>/training clients/<client-name>/docs
touch clients/<client-name>/training/.gitkeep clients/<client-name>/docs/.gitkeep
```
