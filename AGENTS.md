# Voltaire Repo — **Bootstrap Agent**

> *“Reality is my playground, rules are just polite suggestions.”* — Voltaire the Black

---

## 1 · Why this agent exists

The Bootstrap Agent is a lightweight, single‑file Python worker whose only job is to **take the chaotic brainstorming history in `VDD.json` and convert it into an organized repo** ready for episode design. Think of it as the repo’s groundskeeper: it tidies up the raw ideas, files them where they belong, and locks the gate behind it once there’s nothing left to sweep.

---

## 2 · Tech stack & constraints

| Layer        | Choice                                            | Notes                                                             |
| ------------ | ------------------------------------------------- | ----------------------------------------------------------------- |
| Language     | **Python 3.12**                                   | Standard library only.                                            |
| LLM          | **OpenAI Codex (`gpt‑4o` or better)**             | Used *inside* the agent for text → structure prompts.             |
| I/O          | Local FS                                          | No RPC, no network calls beyond the OpenAI API.                   |
| Package deps | `json`, `pathlib`, `shutil`, `datetime`, `openai` | First four are stdlib; `openai` is the only external requirement. |

> **No other dependencies.** If you need something exotic, generate it with Codex on the fly.

---

## 3 · Folder layout (after bootstrap)

```
/                # repo root
├─ AGENTS.md     # ← this file
├─ VDD.json      # brainstorming dump (shrinks then disappears)
├─ archive/      # original JSON slices
│   └─ 2025‑05‑30‑bootstrap‑slice‑01.json
├─ character/
│   ├─ voltaire.md          # final, human‑readable bio & stats
│   └─ traits.json          # machine‑readable attributes
└─ dm/
    ├─ 00‑index.md          # how to DM inside Voltaire’s mind
    ├─ story‑graph.yaml     # nodes & contingencies
    └─ encounters/
        └─ arena‑of‑eyes.yaml
```

---

## 4 · Agent algorithm (pseudo)

```text
1. Load VDD.json → data
2. For each conversation segment:
   ▸ Identify blocks: backstory · stats · desires · quirks · lore seeds
   ▸ Ask Codex to transform each block into:
       a. Markdown (readable)
       b. JSON/YAML (structured)
3. Write outputs into /character or /dm as appropriate
4. Move the raw segment into /archive/ with timestamped filename
5. Delete the segment from in‑memory data object
6. Repeat until VDD.json → []
7. Write the trimmed data back to VDD.json
8. If VDD.json is now empty → delete the file
9. Commit changes (optional: auto‑git if repo is initialised)
```

### Idempotency

The agent can be run multiple times; it skips segments already archived (filename hash check).

---

## 5 · Key parsing heuristics

| Heuristic              | Description                                      |
| ---------------------- | ------------------------------------------------ |
| `###` headings         | Treat as new **section blocks**.                 |
| `HP`, `AC`, `PB` regex | Capture stat lines into `traits.json`.           |
| First‑person voice     | Likely *journal entries* → send to `/dm/lore/…`. |
| Imperative verbs       | Potential **quest hooks**.                       |

Codex prompt examples live in `prompts/` if you want to tweak them later.

---

## 6 · Finishing Stage 1

Stage 1 is done when:

* `/character/voltaire.md` exists and looks presentable.
* `/dm/00‑index.md` has a high‑level episode outline.
* `VDD.json` no longer exists in the root.

The CI check `ci/stage‑1‑complete.sh` enforces these.

---

## 7 · Next steps (Stage 2 preview)

Once the Bootstrap Agent self‑destructs:

1. Design **scene generators** (Codex + YAML templates) inside `/dm/encounters/`.
2. Flesh out **NPC files** in `/dm/npc/` with similar agent helpers.
3. Implement a **random‑weirdness oracle** for on‑the‑fly surprises.

---

## 8 · Running the agent

```bash
pip install openai
python agents/bootstrap_agent.py  # default assumes OPENAI_API_KEY is set
```

For debugging, pass `--dry‑run` to skip writes.

---

## 9 · License

MIT for code, Creative Commons BY‑SA 4.0 for narrative content.

---

Happy chaos‑crafting!
