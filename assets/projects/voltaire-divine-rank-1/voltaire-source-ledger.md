# Voltaire — Divine Rank 1: Source Ledger

This ledger records the evidence used to construct the sixteen-folio sourcebook dossier. It is an audit document, not an additional layer of canon. Repository-relative paths refer to the Voltaire repository as it stood on 2026-07-25.

## Canon policy

### Evidence classifications

- **Explicit canon** — directly recorded in a played-session account, a user-authored primary note, or the current character-sheet snapshot. The original knowledge-boundary tag still applies.
- **Strong inference** — supported by several independent events or by a very close reading of one unambiguous event, but not formally named or ruled by the table.
- **Weak inference** — plausible and thematically supported, but other explanations remain equally viable.
- **Artistic framing** — editorial language, reconstructed testimony, visual metaphor, encounter packaging, or connective prose created for this dossier. It may illuminate canon but does not add facts to it.
- **Unresolved contradiction** — sources conflict, an item or power has an unexplained state, or the table has explicitly left the question open.

“Explicit canon” may describe an explicitly recorded **plan**, theory, belief, or private experience without making its intended outcome true. For example, Voltaire’s summit rite is explicit canon as declared intent; a functioning beacon network is not.

### Knowledge boundaries

The repository’s root `AGENTS.md` defines four in-world boundaries:

- **[Party]** — reasonably available to the adventuring party.
- **[Voltaire-only]** — experienced or known by Voltaire but not necessarily by the party.
- **[DM-private]** — table/DM material; no player character is presumed to know it.
- **[To verify]** — unresolved continuity, mechanism, or adjudication.

The dossier may juxtapose these records for the real-world reader, but it must not imply that every in-world narrator knows them. “Scholars believe” and similar phrases are artistic framing unless a scholar actually appears in the cited source.

### Source hierarchy and limitations

1. Dated files in `Adventures/` are the best evidence for played events and preserve the repository’s knowledge tags.
2. `Adventures/Voltaire's Notes/Character Sheet D&D Beyond/Dicfuc_131028470_2026-07-25.md` is authoritative for the current adventuring-character statistics.
3. User-authored portions of the two JSON note archives and photographed paper notes are primary character/player evidence, but can be fragmentary. Assistant/model replies inside the JSON archives are brainstorming, not canon.
4. `Codex/` is the maintained reference layer. It is useful and usually well tagged, but it occasionally retains stale summaries; where it differs from a dated session or current sheet, the latter wins.
5. `Overview.md` is a valuable synthesis of earlier material, not an infallible chronology.
6. `Module/` is DM preparation and planned mindscape material. It is not evidence that those scenes, powers, creatures, rules, or outcomes occurred in the campaign.
7. Images document the repository’s visual continuity, not independent factual evidence. A pictured intended scene is not proof that the scene occurred.

## Folio-by-folio evidence map

## Folio 1 — Cover

| Dossier element | Classification | Evidence and editorial boundary |
|---|---|---|
| **Voltaire** | Explicit canon | The character is consistently named throughout the repository; current sheet: `Adventures/Voltaire's Notes/Character Sheet D&D Beyond/Dicfuc_131028470_2026-07-25.md:11-18`. |
| **Divine Rank 1** | Explicit canon, [Voltaire-only] origin | Current sheet, line 208; advancement event in `Adventures/2026-06-06.md:55-68`; maintained summary in `Codex/Lore/Divine Rank 1.md:7-21`. |
| **Prince of the Swamp** | Explicit self-title | Voltaire’s retrospective declaration in `Overview.md:50-52`, supported by the swamp-prince origin in `Codex/Characters/Party/Voltaire.md:26-33`. It is not proof that a current court recognises the title. |
| **Scribe of Unbeing** | Artistic title based on an explicit associated role | The Scribe and the Ink of Unbeing are established in `Codex/Powers/The Ink of Unbeing.md:5-25`; this exact compound is editorial rather than table-bestowed. |
| **The V in the Margin** and “a god newly written, in a hand not wholly his own” | Artistic framing | Created from the repeated V, marginalia, authored-belief, and identity-transfer motifs. These are dossier epithets, not canon titles. |
| “The book does not store; it remembers. The Scribe decides.” | Artistic condensation of explicit source text | Adapted from the longer Ink passage in `Codex/Powers/The Ink of Unbeing.md:10-16`; the wording is shortened and the pronoun clarified for the cover. |
| Seal arrangement and “forbidden archive” presentation | Artistic framing | Created to establish sourcebook tone. |

## Folio 2 — Contents, Editorial Method, and Current Status

| Claim or use | Classification | Evidence and notes |
|---|---|---|
| Voltaire is a Variant Human, formerly a Fey prince; Rogue 5 (Thief) / Warlock 8 (Archfey); Hermit; Chaotic Neutral; level 13 | Explicit canon | `Codex/Characters/Party/Voltaire.md:17-24`; current sheet `.../Dicfuc_131028470_2026-07-25.md:15-25`. |
| His current divine state is Rank 1 | Explicit canon | `Codex/Lore/Divine Rank 1.md:13-21`; current sheet line 208. |
| His present recorded location is the exterior of the Shadar-kai tower, climbing toward its summit anti-light in giant-spider form | Explicit canon, [Voltaire-only] | `Adventures/2026-07-25.md:93-98,168-173`; `Codex/Characters/Party/Voltaire.md:198-212`. |
| Roughly twelve subjective months have passed across two Feywild/tower distortions | Explicit record with temporal uncertainty | `Codex/Characters/Party/Voltaire.md:184-211`; the exact outside interval remains [To verify]. |
| The dossier distinguishes fact, theology, rumour, and encounter interpretation | Artistic framing grounded in repository policy | Root `AGENTS.md`, “Knowledge Boundaries”; this ledger’s canon policy. |

## Folio 3 — The Being Known as Voltaire; Names, Titles, and Viewpoints

| Claim or use | Classification | Evidence and notes |
|---|---|---|
| Once a prince of a dim Fey swamp kingdom ruled by his father | Explicit core canon | `Overview.md:46-52`; `Codex/Characters/Party/Voltaire.md:26-33`. Court structure beyond father, kingdom, throne, and swamp is not established. |
| Voltaire Marius | Explicit historical name | Historical paper-sheet extract, `Adventures/Voltaire's Notes/Character Sheet D&D Beyond/Imports/Voltaire Paper Character Sheet (extract).md:15-24`. |
| Voltaire the Black | Explicit current sheet name | Current sheet, lines 11-12. |
| Prince of the Swamp | Explicit self-title with unresolved present authority | `Overview.md:50-52`; origin evidence above. |
| The Scribe | Explicit associated role / interpretive title | `Codex/Powers/The Ink of Unbeing.md:5-25`. The dossier uses it descriptively, not as proof of a formal office. |
| God of Unbecoming | Explicit claim or proposal; unratified | `Adventures/2026-06-06.md:77-82`; no domain mechanic answered. |
| Faux-Human | Explicit historical description | `Overview.md:46-52`; `Codex/Characters/Party/Voltaire.md:26-33`. |
| The V in the Margin | Artistic framing | Editorial title for the V left where concepts, memories, and identities have been altered. |
| He treats gods, demons, bets, and cosmic law as systems in a game | Strong inference | Repeated character framing in `Overview.md:40-42,134-138`; Shar trial in `Codex/Lore/Shar.md:23-40`; visitor-book and archive behaviour in `Adventures/2026-02-21.md:338-384`. |
| Mortals may see an adventurer, Fey may see a dispossessed prince, Shar may see an anomaly, and followers may see an author of belief | Artistic framing based on strong evidence | The individual perspectives are reconstructed from the sources above, the follower conversions in `Adventures/2025-08-16.md:9-31`, and Shar’s recorded engagement in `Codex/Lore/Shar.md:23-50`; these are not verbatim institutional positions. |
| His defining contradiction is brilliant system-perception paired with hazardous judgment | Explicit character framing / strong inference | INT 19, WIS 9 on `Codex/Characters/Party/Voltaire.md:58-65`; behavioural summary, lines 158-180; repeated module tone guide is planning only and not needed as proof. |

## Folio 4 — Appearance, Manifestations, Signs, and Omens

| Claim or use | Classification | Evidence and notes |
|---|---|---|
| Age 30; 185 cm / 6'1"; 185 lb; dark hair; brown, perpetually open eyes | Explicit canon | `Codex/Characters/Party/Voltaire.md:42-54`; current sheet records age, eyes, and weight at `.../Dicfuc_131028470_2026-07-25.md:208-223,420-424,864-870`. |
| Intricate tattoos; fixed smile; frowning physically hurts; donkey tail merged with the crab-book | Explicit canon / historical continuity | `Codex/Characters/Party/Voltaire.md:49-54`; paper-sheet extract lines 66-81. |
| Red eyelids and overlapping angelic/abyssal writing on his arms | Explicit historical appearance | Paper-sheet extract, lines 66-81. Whether every mark remains unchanged is not recorded. |
| V scars on chest and forehead | Explicit canon, [Voltaire-only] | `Adventures/2026-06-06.md:55-73`. |
| Robe of Eyes and later Mask rubble carried on it | Explicit event; effect unresolved | `Adventures/2026-07-25.md:72-90,168-180`; `Codex/Items/Robe of Eyes.md:15-25`. |
| Giant-spider divine ascent | Explicit class transformation, not a unique divine form | `Adventures/2026-07-25.md:93-98`; Feral Transformation is a sheet feature. |
| Numerous eyes appearing on walls and coalescing into V; voice saying “Machinations”; oppressive atmosphere diminishing | Explicit observed manifestation, mechanism unresolved | `Adventures/2026-07-25.md:127-141`; `Codex/Places/Temple of Blood.md:11-24`. |
| Umbral sunflowers, deepening shadow, contained solar glow, ageing sigil, many eyes, and V function as Voltaire-specific omens | Strong inference | Aspen events: `Adventures/2026-01-25.md:56-74`; Feywild darkening: `Adventures/2026-06-06.md:36-54`; temple manifestation: `Adventures/2026-07-25.md:127-141`. Causation varies and must not be presented as a fixed omen table. |
| Witnesses cannot consistently remember or depict him | Weak inference / artistic framing only | Memory alteration is established, but no source says Voltaire is intrinsically unmemorable or visually indescribable. Any such line must be phrased as archival unease, not a power. |

## Folio 5 — Origin, Exile, and the Later Drawing of the Sun

| Claim or use | Classification | Evidence and notes |
|---|---|---|
| Visiting bards brought a Deck of Many Things into a card game at the swamp court | Explicit core canon | `Overview.md:46-52`; `Codex/Characters/Party/Voltaire.md:28-33`; `Codex/Items/Deck of Many Things.md:10-16`. |
| The draw displaced him to a desert, stripped or transformed his Fey nature into humanity, and erased much of his past | Explicit core canon | Same sources. |
| The cards were King of Spades and Ace of Clubs, and the desert was Michaca | Unresolved contradiction / detail only in later synthesis | `Overview.md:50-52` and `Codex/Characters/Party/Voltaire.md:30-33` name them; the raw user account in `Adventures/Voltaire's Notes/Voltaire's D&D Notes.json`, user chunk `[0]`, describes an unidentified Deck draw. Retain the Deck displacement; qualify the card identities and place-name. |
| “Exile” | Artistic framing for a canonical displacement | No court, god, or named exiler is recorded as sentencing him. “Exile” describes the condition and loss, not a proven judicial act. |
| Greg used haste so Voltaire could read/transcribe the Book of Vile Darkness and Book of Exalted Deeds | Explicit player account / strong canon | `Overview.md:54-58`; `Codex/Characters/Greg.md:8-18`; raw user account in `Adventures/Voltaire's Notes/Voltaire's D&D Notes.json`, user chunk `[0]`. “Compelled” is stated in the Greg Codex but the exact degree of consent is not independently detailed. |
| Universal comprehension and indwelling knowledge of cosmic good and evil resulted | Explicit recorded consequence | `Overview.md:54-58`; `Codex/Characters/Party/Voltaire.md:34-40`; `Codex/Characters/Greg.md:14-18`. |
| The Sun was a later, second Deck draw granting advancement and a radiant blast | Explicit canon | `Codex/Items/Deck of Many Things.md:17-24`; `Codex/Items/Sun Card.md:7-15`. |
| The Sun Card was fed to a frog/toad and merged on a natural 20 into Robin | Explicit canon | `Adventures/2025-08-16.md:38-50`; `Codex/Characters/Robin.md:7-20`. |
| The Sun caused the original exile | Contradicted; do not state | The repository separates the original unnamed/two-card displacement from the later Sun draw. The dossier title “the Later Drawing of the Sun” is a deliberate chronology guardrail. |
| The current sheet still lists the Sun Card after Robin’s creation | Unresolved contradiction | `.../Dicfuc_131028470_2026-07-25.md:286-307`; `Codex/Items/Sun Card.md:17-20`. It may reflect sheet lag, spiritual retention, reconstitution, or another table ruling; none is confirmed. |

## Folio 6 — Apotheosis and Divine Rank 1

| Claim or use | Classification | Evidence and notes |
|---|---|---|
| Rank 0 followed replacement of two Fey creatures’ divine memories with memories of Voltaire | Explicit Voltaire-authored session account | `Adventures/2025-08-16.md:9-16`. The morally coercive method should not be euphemised. |
| Shrek became a follower through useful knowledge carrying hidden belief “fine print” | Explicit Voltaire-authored session account | `Adventures/2025-08-16.md:17-31`. “Willing” applies to accepting the note, not informed consent to the clause. |
| Robin became the fourth recorded follower/disciple | Explicit canon | `Adventures/2025-08-16.md:38-50`. |
| Six subjective Feywild months, Bloodweb acceptance, darkening territory, concept-memory experiments, and encounter with the Shadar-kai preceded Rank 1 | Explicit canon, [Voltaire-only] | `Adventures/2026-06-06.md:20-24,36-58`. The spiders are not confirmed worshippers. |
| Roughly twenty Shadar-kai revealed themselves, whipped him, carved V into chest and forehead with his offered Shadow Dagger, admitted him, licked away blood, dedicated themselves, and became initiates | Explicit canon, [Voltaire-only] | `Adventures/2026-06-06.md:48-59`; `Codex/Lore/Divine Rank 1.md:13-21`. |
| Voltaire advanced to Divine Rank 1, gained 300 XP and Inspiration | Explicit canon | `Adventures/2026-06-06.md:59-69`. |
| The Mask-statue rite, six-month vigil, Robin’s summons, and Blessing of V are later Rank 1 events | Explicit events; mechanics unresolved | `Adventures/2026-07-25.md:72-98`; `Codex/Lore/Divine Rank 1.md:32-47`. |
| Rank 1 has a standard package of resistances, immunities, salient actions, senses, or worship thresholds | Unsupported | `Codex/Lore/Divine Rank 1.md:36-48` explicitly lists these mechanics as unestablished. Imported 3.x divine-rank rules are not canon unless the table adopts them. |
| Theological explanation of the ascent as “recognition made ontological” | Strong inference / artistic framing | Rank 0 and Rank 1 both coincide with follower recognition, but the table has not defined the metaphysical equation. |

## Folio 7 — Emerging Divine Portfolio

| Proposed sphere | Classification | Evidence and boundary |
|---|---|---|
| **Domain of Unbecoming** | Explicit canon as player intent; not mechanically confirmed | `Adventures/2026-06-06.md:77-82`; `Codex/Lore/Divine Rank 1.md:23-31`; `Codex/Factions/Voltaire's Followers.md:34-42`. |
| Memory, identity, forgetting, and forced or chosen re-inscription | Strong inference | Ink mechanism and known uses: `Codex/Powers/The Ink of Unbeing.md:10-32,52-67`; follower conversions: `Adventures/2025-08-16.md:9-31`. |
| Authored belief, recognition, and self-made divinity | Strong inference | Self Worship on current sheet, lines 21-25 and 420-424; “Voltaire is divine” visitor book, `Adventures/2026-02-21.md:360-384`; Rank 0 and Rank 1 follower events. |
| Thresholds, exile, and passage between conditions or realms | Strong inference, not a named domain | Fey-to-human displacement; repeated planar crossings in `Adventures/2025-03-29.md:28-38`; aspen gateway and planned tower realm in `Codex/Places/Shadar-kai Tower of Bright Darkness.md:24-37`. |
| Light/darkness, sun/moon, and duality | Emerging/disputed inference | Concept extraction in `Adventures/2026-06-06.md:49-54`; Robin/Voltaire sun-and-moon exchange in `Adventures/2026-07-25.md:88-95`; planning notes in `Codex/Lore/Voltaire's Divine Blueprint.md:7-32`. The older proposed **Domain of Duality** is not simultaneously a ratified domain. |
| Stories, marginalia, rules, and machination | Strong thematic inference | Crab-book title and purpose: `Codex/Items/Crab Book/Machinations & Actions - Player's Handbook.md:3-25`; author-sense and visitor book: `Adventures/2026-02-21.md:338-384`; “Machinations” manifestation: `Adventures/2026-07-25.md:134-141`. |
| Loss, secrets, and Shar’s portfolio | Weak inference as Voltaire’s own portfolio | Shar is involved with the Ink and interrupts the life experiment, but similarity and proximity do not transfer her portfolio: `Codex/Powers/The Ink of Unbeing.md:34-42`; `Codex/Lore/Shar.md:42-57`. |
| What worshippers ask, what the portfolio obliges, and how each sphere could corrupt him | Artistic framing | These are prospective theological readings, not established commandments or divine rules. They should be presented as disputed doctrine or consequence design. |

## Folio 8 — The V, the Follower Sigil, and the Proposed Beacon Network

| Claim or use | Classification | Evidence and notes |
|---|---|---|
| **V** is Voltaire’s divine symbol | Explicit canon | `Codex/Characters/Party/Voltaire.md:76-84`; `Codex/Lore/Divine Rank 1.md:13-21`. |
| V was left as a calling card or essence in concept-stripped creatures’ minds | Explicit canon, [Voltaire-only] | `Adventures/2026-06-06.md:49-54`; `Codex/Powers/The Ink of Unbeing.md:62-67`. |
| V was carved into Voltaire’s chest and forehead during the Shadar-kai initiation | Explicit canon, [Voltaire-only] | `Adventures/2026-06-06.md:55-73`. |
| The **follower sigil** is a separate ornate design: square and outward-growing triangle forming seven points, framed by eye motifs and made with light and dark inks | Explicit Codex description | `Codex/Factions/Voltaire's Followers.md:16-24`. |
| The sigil was carved into the Shadowfell aspen and aged into the bark as if always present | Explicit canon, [Voltaire-only] | `Adventures/2026-01-25.md:56-74`. |
| The sigil was drawn into the Warlock Knights archive grid’s presumed missing Lead position, followed by haze and dimming | Explicit event, interpretation unresolved | `Adventures/2026-02-21.md:338-343`; `Codex/Lore/Warlock Knights Archive Ward Grid.md:7-22`. |
| Selûne’s seven stars explain the follower sigil | DM-private possibility only | `Adventures/2026-01-25.md:68-74` marks this as [DM-private]. It must not be written as Voltaire’s knowledge or settled symbolism. |
| Voltaire plans to place V through a blood-rendered follower sigil around the summit anti-light and call connected marks | Explicit declared intent, not an accomplished act | `Adventures/2026-07-25.md:100-127`; `Codex/Places/Shadar-kai Tower of Bright Darkness.md:24-37`. |
| Aspen mark, archive mark, flesh scars, altered minds, visitor book, and Blood Temple V are possible nodes | Strong/weak inference depending on node | Each mark exists, but membership in one network is unknown. Visitor book and Blood Temple connection are [To verify]: `Codex/Powers/The Ink of Unbeing.md:57-67`; `Codex/Places/Temple of Blood.md:20-24`. |
| A teleportation or beacon network is operational | Unsupported; do not state | The summit rite has not happened. `Adventures/2026-07-25.md:121-127` is an explicit continuity correction. “Beacon network” is an editorial descriptor, not an established in-world name. |
| The Blood Temple manifestation proves the network worked | Contradicted; do not state | It occurred before the summit rite and has several possible conduits: `Adventures/2026-07-25.md:127-141`. |
| Network diagram, lines between nodes, and the question “what could answer from the other side?” | Artistic framing | The diagram visualises hypotheses. It is not a map of proven connections or ranges. |

## Folio 9 — Powers and Divine Phenomena

| Power or phenomenon | Classification | Evidence and boundary |
|---|---|---|
| Universal language comprehension | Explicit recorded consequence | `Codex/Characters/Party/Voltaire.md:34-40,76-84`; `Codex/Characters/Greg.md:10-18`. The ability is described as unconscious. |
| Ink of Unbeing: memory extraction, inscription, transference, forgetfulness, and eternal recall | Explicit DM-provided power text; individual mechanics partly untested | `Codex/Powers/The Ink of Unbeing.md:10-32`. |
| Demonstrated Ink uses: Fey conversion, fine-print belief, aspen inscription, visitor-book writing, and concept-memory experiment | Explicit events with varying unresolved mechanisms | `Codex/Powers/The Ink of Unbeing.md:52-67`; corresponding dated sessions. |
| Book-scent / author-sense | Explicit recorded ability | `Codex/Characters/Party/Voltaire.md:76-90`; demonstrated in the archive at `Adventures/2026-02-21.md:338-354,418-425`. |
| Sun radiant blast | Explicit recorded homebrew boon | `Codex/Items/Sun Card.md:7-15`; `Codex/Items/Deck of Many Things.md:17-24`. |
| Fey Presence, Misty Escape, Feral Transformation, Eldritch Blast, Sneak Attack, Cunning Action, Steady Aim, Uncanny Dodge, pact magic | Explicit current character mechanics | `Codex/Characters/Party/Voltaire.md:92-101`; current sheet `.../Dicfuc_131028470_2026-07-25.md:35-60,200-208,869-881`. |
| No food or drink required to recover exhaustion; long rest suffices | Explicit observed change, exact scope uncertain | `Adventures/2025-08-16.md:5-9`; `Adventures/2026-06-06.md:36-43`; `Codex/Characters/Party/Voltaire.md:84-90`. |
| Darkening Fey territory, umbral flora, Blood Temple remote sight/voice/eyes/V, and Blessing of V | Explicit phenomena; repeatability and cause unresolved | `Adventures/2026-01-25.md:56-74`; `Adventures/2026-06-06.md:36-54`; `Adventures/2026-07-25.md:88-98,127-141`. |
| Voltaire can reliably create life, command darkness, consecrate temples, see through signatories, grant spells, or teleport between V marks | Unsupported | Each is prevented, singular, merely intended, or explicitly [To verify]. |
| “Blessings,” “curses,” “divine senses,” and intervention categories in the dossier | Artistic organisation | Category names arrange observed material. They do not establish a complete Rank 1 rules package. |

## Folio 10 — Soul Coins, Worship, and Divine Economy

| Claim or use | Classification | Evidence and notes |
|---|---|---|
| Voltaire wagered for sixteen soul coins; the refusing demon was destroyed with the Sun power | Explicit player account / strong canon | `Overview.md:123-132`; `Codex/Items/Soul Coins.md:7-15`; raw user account in `Adventures/Voltaire's Notes/Voltaire's D&D Notes.json`, user chunk `[0]`. The demon’s exact identity is [To verify]. |
| The coins were imbued into the crab-book and appeared as sketches | Explicit Voltaire-only report | `Codex/Items/Soul Coins.md:17-25`; `Overview.md:96-104`. |
| One soul coin was later accepted as 500 gp and produced 450 gp change | Explicit played event | `Adventures/2026-02-21.md:147-165`. Whether this is a standard exchange rate is [To verify]. |
| A supposedly book-embedded coin later became spendable | Unresolved contradiction | No source explains whether the coin was removed, copied, manifested, or merely represented in the book. |
| Voltaire can consume, redeem, free, store, transform, judge, or mint souls | Unsupported; do not state as an ability | The sources establish possession/currency and a soul-imbued crab-book, not general soul mastery. |
| Worship by independent beings increases divine leverage or rank | Explicit character doctrine / unconfirmed metaphysics | `Codex/Factions/Voltaire's Followers.md:7-15`. Rank changes correlate with followers, but no formula or causal threshold is established. |
| Confirmed follower cases: two converted Fey, Shrek, Robin, a fine-print blink dog, and roughly twenty Shadar-kai initiates | Explicit Codex record with ethical/status qualifications | `Codex/Factions/Voltaire's Followers.md:26-39`; primary events in `Adventures/2025-08-16.md:9-50` and `Adventures/2026-06-06.md:55-74`. |
| Bloodweb spiders and the unclaimed slave are worshippers | Unsupported | Spiders accepted him but are explicitly not confirmed worshippers: `Codex/Factions/Voltaire's Followers.md:34-39`. The slave follows under local custom after collecting gold, not as a recorded devotee: `Adventures/2026-02-21.md:158-165`. |
| Names, stories, promises, memories, symbols, and acts may function as devotion | Strong theological inference | The conversions, visitor-book phrase, sigils, Sun disciple, and Shadar-kai rite support the question, but the table has not established a universal divine economy. |
| Rites, taboos, offerings, sects, accidental worship, heresies, and political consequences | Artistic framing built from documented methods | Any proposed practice must be labelled “likely,” “emerging,” or “disputed,” not described as an established church. |

## Folio 11 — Relationships

| Figure or group | Classification | Evidence and relationship boundary |
|---|---|---|
| **Shar** — witness, limiter, facilitator, possible rival or theological creditor | Explicit relationship; motives partly inferred | Trial/game terms: `Codex/Lore/Shar.md:23-40`; Ink and interest: lines 42-50; prevented life-creation and pale manifestation: lines 52-57; statue chamber and planned thanks: lines 59-70. She is not confirmed as Voltaire’s warlock patron. |
| **Robin** — Sun-born disciple, guiding sun, recipient of the Blessing of V | Explicit canon | `Codex/Characters/Robin.md:7-35`; `Adventures/2026-07-25.md:88-95`. Her nature and blessing mechanics remain unresolved. |
| **Cornholio** — party ally, Shar’s consort/chosen, possible remote conduit | Explicit relationship; conduit mechanism unresolved | `Codex/Characters/Party/Cornholio.md:36-44`; `Adventures/2026-07-25.md:127-141`. |
| **Greg** — catalyst who exposed Voltaire to the two cosmic books | Explicit backstory; present motives/status unknown | `Codex/Characters/Greg.md:8-31`. |
| **Glasya / Glasher** — archdevil fascination and current affiliation | Explicit relationship | `Overview.md:123-138`; current sheet affiliation at `.../Dicfuc_131028470_2026-07-25.md:21-25,212-215`. “Glasya” and “Glasher” are repository variants; do not silently choose one as proof of separate beings. |
| **Shadar-kai initiates** — willing or deliberate recognisers at Rank 1 | Explicit followers; terms unknown | `Adventures/2026-06-06.md:48-74`; `Codex/Factions/Voltaire's Followers.md:26-39`. Their name, hierarchy, agenda, and expectations are [To verify]. |
| **Bloodweb spiders** — hosts, ritual audience, ecological influence | Explicit contact; worship/pact not established | `Adventures/2026-06-06.md:36-45`; `Codex/Factions/Voltaire's Followers.md:34-39`. |
| **Mask** — destroyed hollow image and possible vacant office | Explicit event; relationship and succession inferred | `Codex/Lore/Mask.md:7-25`; `Adventures/2026-07-25.md:72-90`. |
| **Celsus / the crab-book** — body-bound companion and archive | Explicit core, name [To verify] | `Codex/Items/Crab Book/Crab Book.md:7-32`; historical sheet extract lines 58-64. |
| **Corellon** — intended future confrontation over an “ancient divine fracture” | Explicit declared plan, not an existing encounter | `Adventures/2026-07-25.md:93-95,168-171`. The precise fracture and Voltaire’s claim about it remain unadjudicated. |
| **Titania and Oberon** — Fey-political touchstones | Explicit mentions; family or dynastic tie unsupported | Titania/cyclic Faerealm account: `Adventures/2026-01-25.md:118-140`; Oberon mention: `Adventures/2026-06-06.md:28-35`. They are not proven relatives or former lieges. |

## Folio 12 — Relics and Possessions

| Relic | Classification | Evidence and unresolved cost |
|---|---|---|
| **Crab-book / Celsus / _Machinations & Actions: 5e — Player’s Handbook_** | Explicit canon | `Codex/Items/Crab Book/Crab Book.md:7-32`; `Codex/Items/Crab Book/Machinations & Actions - Player's Handbook.md:3-31`; `Overview.md:94-104`. Its capacity to alter reality is an open question, not a fact. |
| **Ink of Unbeing / Book of Hollow Binding** | Explicit DM-provided power; identification partly inferred | `Codex/Powers/The Ink of Unbeing.md:10-42`. The crab-book is “almost certainly” the named book in the Codex, not formally proven identical. |
| **Voidbone pen** | Explicitly used, persistent-item status unresolved | `Adventures/2026-06-06.md:49-54,63-75`; `Codex/Powers/The Ink of Unbeing.md:44-50`. |
| **Sun Card** | Explicit artifact/power source; post-Robin state contradictory | `Codex/Items/Sun Card.md:7-20`; current sheet lines 286-307. |
| **Two Shadow Daggers +2** | Explicit current inventory and mechanics | Current sheet lines 286-307, 869-881; `Codex/Items/Shadow Dagger+2.md:7-29`. One was offered for the V carving; whether it returned is [To verify]. |
| **Onyx Hit Dagger of Returning +2** | Explicit historical notation; identity overlap unresolved | Paper-sheet extract lines 98-107; `Codex/Items/Shadow Dagger+2.md:22-29`. |
| **Sharite ceremonial dagger** | Explicitly recorded separate mystery | `Codex/Items/Sharite Ceremonial Dagger.md:7-24`. Do not conflate it with either Shadow Dagger without a ruling. |
| **Robe of Eyes with Mask rubble** | Explicit possession and event; effect unresolved | `Codex/Items/Robe of Eyes.md:7-25`; `Adventures/2026-07-25.md:75-90`. |
| **Soul coins** | Explicit currency/record; physical state unresolved | `Codex/Items/Soul Coins.md:7-26`; `Adventures/2026-02-21.md:147-165`. |
| **_Glimpse within the Abyss_, two volumes** | Explicitly stolen/pocketed | `Adventures/2026-02-21.md:423-450`. Exact contents and risks are [To verify]. |
| **_Dark Moon Heresy_** | Explicitly absorbed; its claims are unverified heresy | `Adventures/2026-02-21.md:492-505`. “Shar and Selûne are the same being” must not be promoted to fact. |
| Visitor book | Explicit altered external object, not a confirmed possession | `Adventures/2026-02-21.md:360-390`. Its contractual or conduit function is [To verify]. |

## Folio 13 — Historical Chronology and Testimonies

### Chronology anchors

| Era or date | Classification | Evidence |
|---|---|---|
| Fey prince before displacement | Explicit core canon | `Overview.md:46-52`; `Codex/Characters/Party/Voltaire.md:26-33`. |
| Deck displacement and desert wandering | Explicit core; card/place details disputed | Same sources and raw JSON user chunk `[0]`. |
| Greg’s transcription | Explicit player account / strong canon | `Overview.md:54-58`; `Codex/Characters/Greg.md:10-18`. |
| Historical human thief / registered prince / body alterations | Explicit historical state | Paper-sheet extract, lines 15-107. |
| 2025-03-29 — seals the Tiamat-shrine rupture with Hellhound Ink and “Fall,” enters the closing event horizon, reaches Shar | Explicit played event | `Adventures/2025-03-29.md:28-38`. |
| 2025-08-16 — Ink conversions, fine-print faith, Rank 0, Robin’s creation | Explicit Voltaire-authored account | `Adventures/2025-08-16.md:9-50`. |
| 2026-01-03 — found beneath the Shadowfell aspen preaching godhood to anthropomorphic shadows | Explicit party record, circumstances unusual | `Adventures/2026-01-03.md:47-50`. |
| 2026-01-25 — umbral sunflowers and the aspen sigil | Explicit [Voltaire-only] | `Adventures/2026-01-25.md:56-74`. |
| 2026-02-21 — archive sigil, author-sense thefts, visitor book, soul-coin payment | Explicit events with mechanisms [To verify] | `Adventures/2026-02-21.md:147-165,338-390,423-505`. |
| 2026-06-06 — Feywild months, concept experiment, Shadar-kai initiation, Rank 1 | Explicit [Voltaire-only] | `Adventures/2026-06-06.md:20-24,36-74`. |
| 2026-07-25 — Mask-statue rite, Blessing of V, ascent, remote Blood Temple manifestation | Explicit events with meaning [To verify] | `Adventures/2026-07-25.md:72-141,168-185`. |
| “Before Exile,” “The Exiled Prince,” “The Warlock and the Thief,” “The Beacon Age,” or similar era labels | Artistic framing | Editorial era names organise evidence; they are not recorded historical period names. “Beacon Age” must be prospective because no network is active. |

### Testimony policy

- **Verbatim source-backed quotations:**
  - “I’M PRINCE OF THE SWAMP NOT THE FUCKING DESERT!” — `Overview.md:50-52`.
  - “The Scribe does not steal; he transfers … he decides.” — DM-provided excerpt, `Codex/Powers/The Ink of Unbeing.md:10-16`.
  - “Lead me to the books with the best smell.” — `Adventures/2026-02-21.md:338-346`.
  - “Voltaire is divine.” and “sign here.” — `Adventures/2026-02-21.md:360-384`.
  - “Begin.”, “Rise.”, and “As above, so below.” — `Adventures/2026-07-25.md:72-90`.
  - Robin as “his sun” and Voltaire as “her moonlight” — `Adventures/2026-07-25.md:93-95`.
  - “Machinations.” — `Adventures/2026-07-25.md:134-137`.
- **Handwritten fragments:** `Adventures/Voltaire's Notes/Session Notes aka Voltaires Diary of Insanity/IMG_2610.jpeg`, `IMG_2617.jpeg`, `IMG_2623.jpeg`, `IMG_2624.jpeg`, and `IMG_2642.jpeg` are visual primary sources. Transcriptions should be labelled as such where spelling or handwriting is uncertain.
- **Scholar, hostile theologian, Fey court, cult, and witness excerpts not present verbatim in the repository:** **Artistic framing.** They should be described in this ledger or an editorial note as reconstructed from cited events, not attributed to a real canonical speaker.

## Folio 14 — Confirmed Adventuring Aspect

| Statistic or feature | Classification | Evidence |
|---|---|---|
| Variant Human; Rogue 5 / Warlock 8; Hermit; Chaotic Neutral; level 13 | Explicit current mechanics | Current sheet `.../Dicfuc_131028470_2026-07-25.md:11-25`; `Codex/Characters/Party/Voltaire.md:17-24`. |
| AC 19; HP 100; speed 30 ft.; proficiency +5 | Explicit current mechanics | Current sheet lines 27-34; Codex lines 67-74. |
| STR 7, DEX 19, CON 16, INT 19, WIS 9, CHA 20 | Explicit current mechanics | `Codex/Characters/Party/Voltaire.md:58-65`; current sheet field extract. |
| Darkvision 120 ft.; spell save DC 18; spell attack +10 | Explicit current mechanics | Current sheet lines 43-55, 208-209; Codex lines 67-74, 98-101. |
| Two Shadow Daggers +2 at +11, 1d4+6; Eldritch Blast +10, 1d10+5 per beam | Explicit current sheet | Current sheet lines 869-881. |
| Sneak Attack 3d6, Cunning Action, Steady Aim, Uncanny Dodge, two 4th-level pact slots, listed invocations, Fey Presence, Misty Escape | Explicit current mechanics | `Codex/Characters/Party/Voltaire.md:92-101`; current sheet feature fields. |
| Divine Rank 1 | Explicit note, not a completed rules package | Current sheet line 208; `Codex/Lore/Divine Rank 1.md:36-48`. |
| Rogue 4 / Warlock 8 and Chaotic Good | Stale/contradictory historical summaries | `Codex/Items/Deck of Many Things.md:17-24` and `Codex/Characters/Party/Voltaire.md:158-165` retain older statements. Use the dated 2026-07-25 sheet: Rogue 5 / Warlock 8, Chaotic Neutral. |
| Historical AC 18, HP 72, different ability distribution | Explicit former state only | Paper-sheet extract lines 15-43. It may inform chronology, not the current stat panel. |

## Folio 15 — Interpretive Divine Rank 1 Encounter Profile, Regional Effects, and Encounter Modes

The entire divine encounter profile is **interpretive**, except where a feature reproduces the confirmed adventuring aspect or clearly cites an observed phenomenon. It must be headed “Interpretive Divine Rank 1 Encounter Profile,” not “official stat block.”

| Design element | Classification | Evidence and constraint |
|---|---|---|
| Base AC, HP, saves, attacks, spell DC, and class actions | Explicit current mechanics | Folio 14 sources. Do not inflate them silently. |
| Ink actions involving extraction, transfer, forgetfulness, or recall | Interpretive mechanics derived from explicit power text | `Codex/Powers/The Ink of Unbeing.md:10-32,52-67`. Any save, range, duration, recharge, or damage value is artistic balancing. |
| Feral giant-spider manifestation, Misty Escape, Fey Presence, daggers, Eldritch Blast, and thief reactions | Explicit capabilities with sourcebook-style packaging | Current sheet and `Codex/Characters/Party/Voltaire.md:92-101`. Packaging as legendary or mythic actions is artistic. |
| Many Eyes to V / remote “Machinations” intervention | Interpretive repeatable effect based on one explicit event | `Adventures/2026-07-25.md:127-141`. Range, consent, conduit, cost, and repeatability are unknown. |
| Blessing of V | Name and act explicit; mechanical effect wholly interpretive | `Adventures/2026-07-25.md:88-95`; `Codex/Lore/Divine Rank 1.md:32-47`. |
| Legendary resistance, legendary actions, mythic phase, lair actions, regional effects, and divine interventions | Artistic framing unless directly tied to a cited event | Rank 1 grants no confirmed generic package: `Codex/Lore/Divine Rank 1.md:36-48`. |
| Sustained presence darkens a region and changes inhabitants | Explicit observation; Voltaire’s exact agency is a strong inference | `Adventures/2026-06-06.md:36-45`. |
| A marked aspen widens its aura, houses lesser shades, produces umbral sunflowers, and bears an aged sigil | Explicit local phenomenon, [Voltaire-only] | `Adventures/2026-01-25.md:56-74`. |
| A remote temple blackens, manifests eyes/V, and loses some oppressive atmosphere | Explicit one-time phenomenon | `Codex/Places/Temple of Blood.md:11-24`. |
| Divine injury, death, disappearance, true-title speech, or promise-breaking changes a region | Artistic encounter design | No such causal rules are established. Use conditional language (“might,” “in an interpretive encounter”) and avoid adding them to the historical voice. |
| Ally, patron, rival, dangerous unknown, object of worship, indirect glimpse, and mythic encounter modes | Artistic guidance grounded in relationships | The modes are GM-facing narrative applications, not historical claims. |

## Folio 16 — Secrets, Unresolved Mysteries, and Ten Adventure Hooks

### Unresolved record

| Mystery | Classification | Evidence |
|---|---|---|
| What exactly was lost in the first Deck draw, and can Fey nature or memory return? | Explicit open question | `Codex/Characters/Party/Voltaire.md:215-222`; origin contradictions above. |
| Is the voidbone pen a persistent object or temporary manifestation? | Explicit open question | `Codex/Powers/The Ink of Unbeing.md:44-50`; `Adventures/2026-06-06.md:63-75`. |
| What remains in creatures after their concepts were removed and V inserted? | Explicit open question | `Adventures/2026-06-06.md:49-54,77-85`. |
| What do the Shadar-kai expect, and what did their initiation grant? | Explicit open question | `Adventures/2026-06-06.md:77-85`. |
| What is the summit anti-light, and what will answer a completed rite? | Explicit open question | `Codex/Places/Shadar-kai Tower of Bright Darkness.md:24-37`. |
| Did the visitor book create Cornholio’s conduit? | Explicit open question | `Codex/Powers/The Ink of Unbeing.md:57-61`; `Adventures/2026-07-25.md:127-141`. |
| Did destroying Mask’s hollow statue expose or transfer an office? | Weak inference / explicit open question | `Codex/Lore/Mask.md:7-25`; `Adventures/2026-07-25.md:72-90,175-180`. |
| What did the Blessing of V do? | Explicit open question | `Codex/Characters/Robin.md:26-35`. |
| What is the actual Rank 1 portfolio and mechanical package? | Explicit open question | `Codex/Lore/Divine Rank 1.md:23-48`. |
| What would Divine Rank 2 require or cost? | Artistic future question | The repository does not state a threshold or consequence. |

### Adventure-hook derivations

All ten hooks are **artistic framing** anchored to unresolved canon. Their premises may be used without treating their proposed culprit, solution, or outcome as already true.

1. **The Signer Who Never Signed** — a visitor-book signature manufactures or reveals a memory of service. Basis: the repeated claim and invitation in `Adventures/2026-02-21.md:360-384`, plus the Ink’s demonstrated ability to alter memory in `Adventures/2025-08-16.md:9-16`.
2. **Sixteen Minus One** — the soul behind the spent coin returns with an impossible receipt and a claim against Celsus. Basis: `Codex/Items/Soul Coins.md:13-25`; `Adventures/2026-02-21.md:147-165`. The receipt and life-debt are artistic inventions.
3. **The False V** — a Fey faction weaponises crude Vs and Voltaire’s coercive origin against him. Basis: the ethical breach in `Adventures/2025-08-16.md:9-31` and the V/sigil distinction in `Codex/Factions/Voltaire's Followers.md:16-24`.
4. **What the Aspen Remembers** — the aged sigil reveals a memory of the swamp kingdom and an accusation of betrayal. Basis: `Adventures/2026-01-25.md:56-74` and the disputed origin record; the remembered accuser is artistic.
5. **Robin’s Second Sun** — a second Sun Card forces Robin and Voltaire to test whether her origin is unique. Basis: Robin’s creation in `Adventures/2025-08-16.md:38-50` and the current sheet’s unexplained retained Sun Card at line 306.
6. **The Empty Mask Speaks** — Mask rubble on the Robe of Eyes gives useful warnings while eroding Voltaire’s history. Basis: `Adventures/2026-07-25.md:72-90,175-180`; the speaking rubble and memory cost are artistic.
7. **Twenty Different Rites** — the Shadar-kai initiates remember incompatible, magically enforceable promises. Basis: the obscure initiation and unresolved obligations in `Adventures/2026-06-06.md:55-74`; the twenty promises are artistic.
8. **The Beacon That Answers First** — a distant V calls before the summit rite, threatening to complete the proposed network on another power’s terms. Basis: `Adventures/2026-07-25.md:100-141`; the caller and terms are artistic.
9. **Greg’s Missing Sentence** — a line from the Vile/Exalted transcription belongs to neither source and destabilises authorship. Basis: Greg’s accelerated transcription in `Overview.md:54-58`; the missing sentence is artistic.
10. **Unbecoming, Ratified** — the proposed domain offers Rank 2 at the cost of the last proof of Voltaire’s princely identity. Basis: the unratified proposal in `Adventures/2026-06-06.md:77-82` and the still-unresolved Rank 2 future; the offer and cost are artistic.

## Mandatory continuity guardrails

### Sun and exile

- The first Deck event caused the desert displacement, loss of Fey nature, and damaged memory.
- The Sun was a later draw that granted advancement/radiant power and was later merged with a frog/toad to create Robin.
- Do not say the Sun exiled Voltaire.
- “Exile” is a mythic/editorial description; no sentencing authority or exiler is established.
- King of Spades, Ace of Clubs, and Michaca are later-synthesis details that conflict with a less specific raw account.

### V, follower sigil, and network

- **V** and the ornate **seven-point follower sigil** are distinct.
- Confirmed marks do not automatically constitute a connected system.
- The summit rite and teleportation network are explicit intent but have not happened.
- The two summit-rite images in `Adventures/2026-07-25/` are explicitly visualisations of intent.
- The Blood Temple event occurred before the rite and cannot prove network activation.
- “Beacon network” is an editorial name unless the table later adopts it.

### Patronage, Shar, and self-worship

- The current mechanical subclass lists **The Archfey** as Otherworldly Patron: current sheet lines 43-49.
- The current faith field says **Self Worship**: lines 21-25 and 420-424.
- The Codex phrase “acts as his own Warlock patron” (`Codex/Characters/Party/Voltaire.md:76-84`) is character posture/theological shorthand, not a replacement for the current mechanical field.
- Shar is a witness, limiter, facilitator, and possible creditor/rival. She is not confirmed as Voltaire’s warlock patron.
- Voltaire’s planned prayer of thanks does not establish worship, subordination, or transfer of the tower to Shar.

### Soul coins

- Possessing, sketching/imbuing, wagering, and spending soul coins does not establish general power over souls.
- No source grants Voltaire the ability to consume, redeem, free, judge, transform, or mint souls.
- The book-embedded versus later-spendable state is unresolved.

### Mask

- The destruction of a hollow statue and occupation of its place are explicit.
- Succession, theft of office, inheritance of portfolio, and divine vacancy are interpretations or open questions.
- Mask’s rubble on the Robe of Eyes has no confirmed mechanical effect.

### Module and mindscape

- The proposal to host a game/trial in Head-Space is explicit: `Codex/Places/Head-Space.md:7-20`; `Overview.md:134-138`.
- The gladiatorial capture, pop-up-book void, colosseum, Head-Space monsters, favour system, rules changes, dialogue, and ending choices are DM preparation, not played history: `Module/Scribes-Folly/00 - Canon Primer.md:1-38`; `Module/Scribes-Folly/01 - The Scribe's Folly.md:1-18,26-87,91-120`; `Module/Voltaire's D&D Module.md:1-38`.
- Module material may inform mood or an explicitly labelled future hook. It must not be cited as proof of a current divine power, a past event, or party knowledge.

### Additional guardrails

- Use current Rogue 5 / Warlock 8 and Chaotic Neutral statistics; older Rogue 4 and Chaotic Good references are stale.
- Do not conflate the two current Shadow Daggers +2, the historical Onyx Returning Dagger, and the Sharite ceremonial dagger.
- Bloodweb spiders are not confirmed worshippers.
- The visitor-book conduit is not confirmed.
- Robin’s Blessing of V has no confirmed effect.
- The Domain of Unbecoming is claimed intent; the older Domain of Duality is a conceptual blueprint; neither is a ratified rules package.
- The Warlock Knights’ buried metal god is **Telos**, not Talos: `Codex/Lore/Telos.md:7-18`; `Codex/Lore/Talos.md:7-13`.
- “Lux,” appearing in assistant/model material in the JSON note archive, is not canonical. The disciple’s canonical name is Robin.

## Image provenance

All artwork was sourced from the listed in-repository files on 2026-07-25. For a practical local HTML and repository-safe PDF, the opaque PNG presentation copies were re-encoded once as JPEG at quality 92 (quality 94 for the cover), without resizing, cropping, retouching, or content changes. The two handwritten JPEG photographs remain byte-identical copies. These images support presentation and continuity only. The repository records that its imagery was created through its OpenAI image workflow, but individual prompt, generation, artist-credit, and licensing metadata was not retained with these files. This ledger therefore makes no claim beyond their presence in the user-controlled repository and the mechanical delivery conversion just described.

| Dossier asset | In-repository source | Status |
|---|---|---|
| `assets/voltaire-portrait.jpg` | `Codex/Characters/Party/Voltaire_portrait.png` | Repository reference art; delivery re-encode |
| `assets/robin-dialogue.jpg` | `Adventures/2026-01-25/2026-01-25_robin-shoulder-dialogue_wide.png` | Played-scene illustration; delivery re-encode |
| `assets/followers-sigil.jpg` | `Codex/Factions/Voltaire_followers_sigil.png` | Repository symbolic reference; delivery re-encode |
| `assets/aspen-sigil.jpg` | `Adventures/2026-01-25/2026-01-25_aspen-sigil-carving_wide.png` | Played-scene illustration; delivery re-encode |
| `assets/tower-ascent.jpg` | `Codex/Places/Shadar-kai_Tower_of_Bright_Darkness_establishing.png`; also identical to `Adventures/2026-07-25/2026-07-25_giant-spider-ascent.png` | Played-scene illustration; delivery re-encode |
| `assets/blood-temple-v.jpg` | `Codex/Places/Temple_of_Blood_ref.png`; also identical to `Adventures/2026-07-25/2026-07-25_blood-temple_many-eyes-to-v.png` | Played-scene illustration; delivery re-encode |
| `assets/mask-ritual.jpg` | `Adventures/2026-07-25/2026-07-25_mask-statue-ritual.png` | Played-scene illustration; delivery re-encode |
| `assets/visitor-book.jpg` | `Adventures/2026-02-21/2026-02-21_visitor-book_floating-quill_ink-of-unbeing_wide.png` | Played-scene illustration; delivery re-encode |
| `assets/ink-unbeing.jpg` | `Codex/Powers/The_Ink_of_Unbeing_ref.png` | Repository reference art; delivery re-encode |
| `assets/sun-card.jpg` | `Codex/Items/Sun_Card_ref.png` | Repository reference art; delivery re-encode |
| `assets/soul-coins.jpg` | `Codex/Items/Soul_Coins_ref.png` | Repository reference art; delivery re-encode |
| `assets/crab-book.jpg` | `Codex/Items/Crab Book/Crab_Book_ref.png` | Repository reference art; delivery re-encode |
| `assets/robe-eyes.jpg` | `Codex/Items/Robe_of_Eyes_ref.png` | Repository reference art; delivery re-encode |
| `assets/shadow-dagger.jpg` | `Codex/Items/Shadow_Daggerplus2_ref.png` | Repository reference art; delivery re-encode |
| `assets/divine-blueprint.jpg` | `Codex/Lore/Voltaire_Divine_Blueprint_motif.png` | Conceptual/planning illustration; not proof of a ratified domain; delivery re-encode |
| `assets/robin.jpg` | `Codex/Characters/Robin_portrait.png` | Repository reference art; delivery re-encode |
| `assets/cornholio.jpg` | `Codex/Characters/Party/Cornholio_portrait.png` | Repository reference art; delivery re-encode |
| `assets/greg.jpg` | `Codex/Characters/Greg_portrait.png` | Repository reference art; delivery re-encode |
| `assets/glasya.jpg` | `Codex/Lore/Glasya_motif.png` | Repository reference art; delivery re-encode |
| `assets/shar.jpg` | `Codex/Lore/Shar_motif.png` | Repository reference art; delivery re-encode |
| `assets/diary-flesh-cage.jpeg` | `Adventures/Voltaire's Notes/Session Notes aka Voltaires Diary of Insanity/IMG_2617.jpeg` | Primary handwritten note photograph |
| `assets/diary-marginalia.jpeg` | `Adventures/Voltaire's Notes/Session Notes aka Voltaires Diary of Insanity/IMG_2642.jpeg` | Primary handwritten cosmology-note photograph |
| `assets/cover.jpg` | `assets/output/pdf/plates/voltaire_divine_dossier_plate.png` | Reused repository artwork / artistic reconstruction from the prior local dossier; quality-94 delivery re-encode |

Artwork showing the proposed summit rite or network activation must not be captioned as accomplished history. Low-resolution drafts, `_draft` images, `*_prev*` files, and the meme image `Codex/Lore/norhan_frog_fucker.png` were excluded from the dossier’s evidentiary visual set.

## Audit conclusion

The strongest defensible portrait is of a former Fey prince whose identity was forcibly rewritten by a Deck event, then repeatedly re-authored through cosmic texts, a body-bound memory archive, bargains, symbols, and the beliefs of others. His Rank 1 status and several unprecedented phenomena are explicit. His formal portfolio, divine mechanics, church, beacon network, succession to Mask, general authority over souls, and eventual Rank 2 trajectory remain open. The dossier’s mythology should make those absences feel intentional without converting them into false certainty.
