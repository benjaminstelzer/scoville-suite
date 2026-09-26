# Vergleich: veröffentlichte Suite gegen Ursprungsvariante

Stand: 2026-09-26, nur lesend.

- **Ursprung:** Commit `84b0468` (25.09., 13:24), der Stand meines ersten Reviews. Workflow v0.5 mit Launcher, Guard, Hash-Belegen und Warteschleife.
- **Veröffentlicht:** Commit `ff592a3` (HEAD), die Quellen der v2-Suite samt Koordinations-Patch. Stichprobe: `SKILL.md` und `references/operations.md` von Workflow auf GitHub (`scoville-suite-for-codex`, `main`) stimmen inhaltlich mit HEAD überein.
- **Messung:** Der ursprüngliche Stand wird durch die DIVI5-Läufe `01a0d499…` (ALT1, v0.5) und `01a0d3ae…` (ALT2) abgebildet. Der veröffentlichte Stand durch den DIVI5-Lauf vom 26.09. ab 11:40 (Coordinator `S-MNGR-#3/#4/#5-PLAN-0012`, 9 Tasks).

## Ergebnis in einem Satz

Die veröffentlichte Suite erfüllt das Ziel deutlich. Der Coordinator verbraucht pro Einheit rund 3–5× weniger, Polling ist praktisch weg, und die Kernregeln aller Skills sind erhalten. Beim Worker hält die 75-%-Schwelle aber nicht zuverlässig: Ein Worker lief in eine Auto-Compaction.

## Umfang je Skill (Laufzeitpaket: Dateien / Bytes)

| Skill | Ursprung | Veröffentlicht | Kommentar |
| --- | ---: | ---: | --- |
| Code | 6 / 34.360 | 6 / 33.939 | umbenannt in `scoville-code`, Inhalt praktisch gleich |
| Handoff | 3 / 6.952 | 3 / 7.416 | Codeblock mit vier Backticks, Regel zum Arbeitsverzeichnis präzisiert |
| Plan | 18 / 216.585 | 11 / 156.649 | SKILL 10,6 → 5,7 KB, Referenzen 76,2 → 33,0 KB, keine Hash-Guards und keine Writing-Profile |
| UI | 18 / 122.924 | 19 / 125.002 | strukturierte Klassifikation ausgelagert, Router präzisiert |
| Workflow | 29 / 259.901 | 16 / 72.151 | Referenzen 120,2 → 15,2 KB, Skripte 127 → 44 KB |
| Ask | 12 / 60.504 | 14 / 59.818 | native Chats statt `prepare`/`creation_result`/`match_delivery` |
| Setup | – | 7 / 17.194 | neu: verwaltet `.scoville/config.json` |

## Messwerte im echten DIVI5-Einsatz

| Messwert | ALT1 (Ursprung) | ALT2 (Ursprung) | Veröffentlicht |
| --- | ---: | ---: | ---: |
| Worker-Einheiten | 9 | 3 | 3 |
| Coordinator-Aufrufe pro Einheit | 109 | 85 | 32 |
| Coordinator-Input pro Einheit | 13,7 Mio. | 10,1 Mio. | 2,9 Mio. |
| Warte-/Poll-Aufrufe insgesamt | 286 | 54 | 2 |
| Scoville-Helper-Fehler | 14 | 5 | 0 |
| Auto-Compactions Coordinator / Worker | 0 / 0 | 0 / 0 | 0 / 1 |
| Höchste Kontextbelegung Worker | – | – | 86 % |

## Kernregeln: erhalten oder verloren

**Workflow, erhalten:** explizite Aktivierung, Plan- und Commit-Hoheit des Coordinators, frischer und schreibgeschützter Reviewer, Review-Pflicht bei Code und kritischer Doku, höchstens drei Reparaturen, Schwellen 25/75 %, Ergebnis vor Archivierung sichern, IDs statt Titel, ganzer aktiver Plan als Standardumfang, Stopp an den aktiven Worker, kein persistentes Goal, kein Worktree ohne Auftrag, fünf Routen mit Step-Overrides, Hooks und Backups werden nicht umgangen, `needs_user_decision` und `context_handoff`.

**Workflow, bewusst entfallen:** Launcher und Parken, Guard mit Revisionen und Generationen (vorher 90 Fundstellen, jetzt 1 Hinweis), Hash- und Beleg-Pflichten (41 → 3 Erwähnungen, jeweils „nicht nötig“), die `wait_threads`-Schleife, der Lifecycle-Helper im Laufzeitpfad und der Parser-Zwang für Ergebnisse.

**Workflow, bewusst neu:** Die Worker-Nachricht weckt den ruhenden Coordinator. Step-Gruppen (ADR-0093/0094). Takeover- und Selbstarchivierungsnachrichten beim Rollover.

**Plan:** Alle Autoritäts- und Lebenszyklusregeln sind erhalten: nichts erfinden, `done` erst nach Acceptance und Evidence, Decisions als `proposed` oder `accepted`, Nachfrage vor Aktivierung und Abbruch, Einordnung von Nachrichten während laufender Arbeit, Pre-flight, unveränderliche gestartete Historie, ID-Vergabe, Validator. Die Warteschlange ist auf Ankunftsreihenfolge vereinfacht (ADR-0076).

**Ask:** Unabhängigkeit, Review- und Consultation-Modus, keine stille Modellersetzung, getrennte Angabe von angefordertem und gemeldetem Modell, sichtbare Fehlschläge und Follow-ups sind erhalten. Die Claude-CLI hat standardmäßig nur Read, Grep und Glob.

**Code, UI, Handoff:** Die Kernregeln sind unverändert. Die Änderungen präzisieren nur Formulierungen.

## Befunde

| ID | Schwere | Befund | Beleg | Empfehlung |
| --- | --- | --- | --- | --- |
| V1 | hoch | Die 75-%-Schwelle beim Worker greift nicht zuverlässig. Ein Worker lief bis 86 % und in eine native Compaction, das widerspricht dem Kernprinzip. | `S-WORK-#5-W-028/STEP-2`: 140 Modellaufrufe, 1 Checkpoint-Aufruf, 1 Compaction, Maximum 223.025 von 258.400 Tokens | Den Auslöser in `operations-rollover.md` („After a coherent change and its immediate checks …“) und im Worker-Prompt konkretisieren: Checkpoint nach jedem abgeschlossenen Step und nach jedem Build-/Test-Zyklus. |
| V2 | mittel | Der Coordinator prüft die Schwelle nur an akzeptierten Einheiten. In einer Einheit mit Review- und Reparaturschleife stieg er bis 69 %. | `S-MNGR-#3-PLAN-0012`: Maximum 179.118 Tokens, 7 Turns | Zusätzlich nach jedem übernommenen Kind-Ergebnis prüfen; ein Rollover weiterhin nur an sicheren Punkten. |
| V3 | mittel | Das lokale `packages/` im privaten Repo ist veraltet (Stand `c52980b`, 25.09. 20:09). Es enthält noch Legacy-Guard-Regel, Lifecycle-Helper und `wait_threads`-Schleife. | `packages/scoville-workflow-for-codex/.../references/operations.md` Z. 20 und 83 gegenüber HEAD-Quelle und GitHub | Neu bauen oder aus dem Repo entfernen, damit niemand daraus installiert. |
| V4 | niedrig | Worker-Kommentare in langen Einheiten sind zu zahlreich. | `S-WORK-#5-W-028/STEP-2`: 18 Kommentare | Die Meldungsregel des Worker-Prompts auf „eine Meldung pro Phase“ schärfen. |
| V5 | Info | Step-Gruppen sind wieder erlaubt. Das ist eine bewusste Entscheidung, erhöht aber das Risiko aus V1. | ADR-0093, ADR-0094; `operations-dispatch.md` Z. 8–16 | Bei V1 mitprüfen. Grund für die Überschreitung in V1 war ein einzelner großer Step. |
| V6 | Info | Keine Scoville-Helper-Fehler im Einsatz. Die 7 Fehlersignale stammen aus PowerShell- und Playwright-Aufrufen des Projekts. | Analyse der 9 Tasks | – |
