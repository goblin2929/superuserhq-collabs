# Novastacks AI and Superuser HQ Collabs — Repository Setup Design

## Purpose

A multi-client collaboration workspace for Novastacks AI and Superuser HQ. Used to create training content (guides, code examples, presentations, video scripts) and manage project plans/proposals for clients.

## Repository Structure

```
superuserhq-collabs/
├── CLAUDE.md                  # Project description & folder conventions
├── .gitignore                 # Standard ignores
├── README.md                  # Repo overview
├── clients/
│   └── tiket/
│       ├── training/          # Training content for Tiket
│       └── docs/              # Client-specific docs for Tiket
├── shared/
│   ├── templates/             # Reusable templates across clients
│   └── resources/             # Shared resources (images, common assets)
└── docs/
    └── plans/                 # Project plans & proposals for clients
```

## Organization Approach

**Hybrid (client-first with shared resources):**
- Top-level `clients/` directory with a subfolder per client
- Each client folder contains `training/` and `docs/` subfolders
- `shared/` folder for cross-client templates and resources
- `docs/plans/` for project plans and proposals

## Adding a New Client

Create a new folder under `clients/<client-name>/` with `training/` and `docs/` subfolders.

## Key Files

### CLAUDE.md
Minimal — project description, folder conventions, and how to add a new client.

### .gitignore
Covers OS files, editor files, temp files, dependency artifacts, and environment files.

### README.md
Brief repo overview with folder structure and purpose.

### .gitkeep
Empty directories include `.gitkeep` files so Git tracks the folder structure.

## First Client

**Tiket** — content types TBD, general structure set up for now.

## Design Decisions

- **Option B (Structured Client Folders)** chosen over flat or heavily structured alternatives
- Enough structure to stay organized without over-committing to content type subfolders
- Easy to evolve as client needs become clearer
