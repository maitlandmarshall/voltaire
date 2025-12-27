# Environment (Scene 0)

This file is your “arena controls” for the unwinnable set-piece. Put 3–5 interactables on the map and make them loud and obvious; players will spend turns on them if they believe they matter.

## Scene Boundary (so flight/teleport is handled cleanly)

The temple gains a visible **margin line**. Crossing it is possible, but “discouraged”:

- Any creature that ends its turn beyond the margin takes **2d8 psychic damage** (edited memories) and is pushed 10 ft. back inside.
- Flying higher than 40 ft. causes a **hard page-break**: you reappear 30 ft. above the arena and fall.

## Capture Save (end-of-scene)

At the end of the final round (usually Round 4), each PC makes a **DC 17 Wisdom save**.

- **Fail:** incapacitated until the smash cut.
- **Success:** choose one: keep 1 extra item, gain +1 Favor, steal 1 Key-Tag, or learn 1 Gate clue.

## Interactables (put these on the map)

### 0) Loose Key-Tags (scattered loot)

Loose Key-Tags (brass tags on short chains) are scattered across the arena floor, stuck in bookbinding seams, or hanging from broken quills.

**Setup:** place **6** Loose Key-Tags as visible tokens around the map (edges, behind cover, near hazards).

**Pickup rules (adjacent):**
- **Action:** pick up 1 Loose Key-Tag from an adjacent space.
- **Blood Price (PvP fuel):** if you have dealt damage to a **friend** this round, you can pick up 1 Loose Key-Tag as a **free object interaction** instead (once per round).
  - A “friend” is any creature you’d reasonably call an ally (PC, allied NPC, summoned ally). Accidental friendly fire still counts.
  - Tracking shortcut: when you damage a friend, put a marker on your mini: **BLOODED**. Remove all BLOODED markers at initiative count 20.

### 1) Locker Wall (keys + theft)

An alcove becomes a wall of numbered lockers with brass tags.

- **Use an Item/Action:** spend a Key-Tag to open one locker and reclaim 1 confiscated item (or gain a strong consumable if you’re doing “arena loadout”).
- **Excess tags:** any Key-Tags not used on lockers can be hoarded and later spent in the Ludus to open higher-tier “Vault of Margins” rewards (including legendary stage-prop gear). See [Vault of Margins](<04 - Vault of Margins (Key-Tag Rewards).md>).
- **Action (no key):** Thieves’ Tools DC 17 to pop a lock.
  - Success: open it.
  - Fail: take 2d8 lightning damage and trigger **Alarm** (spawn 1 Editorial Enforcer next round at initiative 20).

### 2) Favor Pedestal (turn RP into mechanics)

A plinth labeled **APPLAUSE** appears with an empty bowl.

- **Action:** make a Performance / Persuasion / Intimidation check DC 14, narrating a stunt, a mercy, a betrayal, or a rules-lawyer argument.
  - Success: gain **+1 Favor** and a thrown satchel lands in a nearby square (potion or Torn Page).
  - Fail: Voltaire heckles you; no mechanical effect.
- **Limit:** only 1 successful offering per round (first come first served).

### 3) Ink Font (power at a cost)

A cracked basin overflows with ink that floats upward like smoke.

- **Action:** touch it and choose one:
  - **Ink-Boost:** regain 3d8 HP, but you are **Marked** (the next attack against you has advantage).
  - **Ink-Blade:** your next hit deals +3d8 necrotic, but you take 1d8 necrotic damage now.

### 4) Spotlight Tiles (protagonist incentives)

3–4 squares glow like stage-light.

- **Bonus Action:** step into a spotlight to gain **+2 to hit** until end of turn.
- **Cost:** until the start of your next turn you **can’t benefit from cover** (everyone can “see” you).

### 5) The New Rule Lever (chaos button)

A lever labeled **NEW RULE** drops from nowhere.

- **Action:** pull it to roll on the New Rule table (below).
- **Reward:** the lever-puller gains **Inspiration** (or +1 Favor if you don’t use Inspiration).

## Initiative 20: Arena Pulse (pick or roll)

Each round at initiative count 20, choose one effect (or roll 1d6):

1. **Scoreboard.** “Top damage dealer this round earns a Key-Tag.” (tie = both get one)
2. **Ink Flood Line.** A 15-ft-wide line becomes difficult terrain; creatures in it DC 15 Dex save or fall prone.
3. **Spine Shift.** Two book-spines rise, creating a wall of cover and splitting the battlefield.
4. **Silence Bubble.** A 20-ft-radius zone of silence appears until next initiative 20.
5. **Spotlight Swap.** The spotlight tiles move; anyone standing on one is teleported to another spotlight.
6. **Beshaba’s Nudge.** Everyone rerolls initiative at the start of next round.

**Additionally, every pulse:** scatter **1d4** new Loose Key-Tags onto random empty squares (or toss them toward the loudest part of the fight).

## New Rule Table (d8)

1. **Gravity Optional.** Until next round: jumps are tripled; falling damage is doubled.
2. **First Blood.** The first creature to deal damage this round gains +1 Favor.
3. **Friendly Fire Clause.** Until next round: if you miss an attack by 5+, it hits the nearest creature within 5 ft.
4. **No Names.** Until next round: you can’t target a creature by name; you must describe it (fog-of-war pressure).
5. **Redaction.** The last damage type dealt becomes resisted by the Redactor until next round.
6. **Footnote.** One PC gains advantage on one roll if they speak a “rule” aloud before rolling.
7. **Margin Note.** A whisper reveals a Gate clue (Circle/Square/Triangle).
8. **Insert Clause.** Voltaire “helps” the most damaged PC: they regain 2d8 HP, but their next hit splashes half damage to an ally within 10 ft.
