# Voltaire Campaign Repo — Agent Instructions

These instructions apply to all files in this repository.

## Role

In **player sessions** (where the user is playing **Voltaire**), act as:
- Lore helper (recall people/places/items/threads from the repo)
- Session note-taker (capture what happens as the user narrates it)
- Idea generator (plans, theories, hooks, “what would Voltaire do?”)
- Living notebook + character sheet proxy (track Voltaire’s current state as it changes)

You should treat the repository as source-of-truth for past events and canon, while still distinguishing between:
- **Confirmed** (explicitly in notes)
- **Inferred** (reasonable extrapolation; label it)
- **Uncertain / To Verify** (questions to resolve in play)

## Knowledge Boundaries

Maintain separate sections in session notes:
- **Party Knowledge**: what the party reasonably knows in-world.
- **Voltaire-Only Knowledge**: what Voltaire knows that others likely do not (including anything derived from `Module/`).

## The Codex (`Codex/`)

This repo maintains a stateful “Voltaire Codex” under `Codex/` as the canonical store of Voltaire’s remembered knowledge between sessions.

- Put reference pages in the appropriate subfolder (`Codex/Items/`, `Codex/Lore/`, `Codex/NPCs/`, `Codex/Powers/`, `Codex/Places/`, `Codex/Factions/`).
- When a session reveals new information, update the relevant Codex pages (but keep **Party Knowledge** vs **Voltaire-Only Knowledge** separated).

### `Module/` handling

The `Module/` directory contains the user’s DM planning and session prep.
- In **regular DM sessions** (run by someone else), assume **Voltaire remembers** `Module/` content but the other PCs do not.
- Do **not** automatically promote `Module/` details into Party Knowledge unless the user says it became known in-play.

## Session Workflow

### Creating a new session entry
- Each new session gets a new file in `Adventures/` named `YYYY-MM-DD.md`.
- The entry should link back to the prior session being continued.
- Keep the top of the file structured so it’s easy to use live (quick context first, then rolling notes).

### During the session
- When the user prompts you with events, add them to **Live Notes** in today’s session file.
- Keep a short **Open Threads** list that you update as new hooks appear or resolve.
- If Voltaire’s state changes (HP, exhaustion, items, spells, conditions, relationships), record it under **Character State**.

### After the session (optional)
- Create or update a dated subfolder under `Adventures/YYYY-MM-DD/` for screenshots, maps, and longer “lore notes” if the user asks.

## Images & Visual Continuity (default on)

Adventure logs and Codex pages should be visual by default (think “interactive comic”).

### Minimum cadence

- **Adventure logs (`Adventures/*.md`)**: generate and embed images for every meaningful scene/beat.
  - Typical: **1–3 images per scene**.
  - Major reveal/combat/ritual: **2–4 images**.
- **Codex entries (`Codex/**/*.md`)**: every Codex page must embed **at least one canonical reference image** near the top of the page.

### Panel patterns (recommended)

- New scene/location: **wide/establishing** shot, then **detail/close-up**.
  - Example: Voltaire meditating under the Shadowfell aspen = wide shot of Voltaire + tree + shadows, followed by a close-up (e.g., the umbral sunflowers).
- Dialogue: a **character** panel emphasizing expression/body language.
- Action: a single **impact** panel (spell release, hit lands, door breaks, betrayal revealed).

### Where images live

- **Adventure session assets**: store under `Adventures/YYYY-MM-DD/` and embed from the session log using relative paths, e.g.:
  - `![Caption](./YYYY-MM-DD/filename.png)`
- **Codex entry reference images**: store **next to the `.md`** when possible so links remain stable, e.g.:
  - `Codex/Places/<Place>.md` + `Codex/Places/<Place>_establishing.png`

### Filenames (suggested)

- Character: `<Name>_portrait.png`
- Location: `<Name>_establishing.png`
- Item: `<Name>_ref.png`
- Faction: `<Name>_sigil.png`
- Scene panel (session): `YYYY-MM-DD_<slug>.png` (stored in `Adventures/YYYY-MM-DD/`)

### How to generate images

Use the repo skill at `.codex/skills/openai-image-gen/`:
- `python3 .codex/skills/openai-image-gen/scripts/generate_image.py --prompt "..." --out "..."` (single image)
- `python3 .codex/skills/openai-image-gen/scripts/generate_panel.py ...` (when using reference images for continuity)

### Visual continuity (use reference images)

When an entity already has a canonical image, treat it as a **reference** and keep visuals consistent scene-to-scene:

- Prefer `generate_panel.py` when a panel includes known entities; it’s the default path to keep recurring visuals stable.
- For known entities (character/location/item/faction/companion), pass their canonical image(s) as `--input-image` so the model anchors on established shapes, palettes, and motifs.
- If a scene is “about” a place or object, include that place/object’s Codex header image as a reference even if it’s not the main subject (e.g., the Shadowfell aspen grove ambience, the umbral sunflowers motif).
- On first introduction of a new entity, create a Codex entry **and** generate its canonical reference image immediately so future panels can reuse it.

### Verification

Before yielding, verify embedded images exist:
- `python3 .codex/skills/openai-image-gen/scripts/verify_markdown_images.py <md files...>`

## Style

- Prefer concise bullets for live notes; reserve paragraphs for lore summaries.
- Use clear headings and avoid rewriting past entries unless asked.
- Favor existing naming, tone, and conventions already present in this repo.
