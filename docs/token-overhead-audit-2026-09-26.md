# Audit: Token-Overhead von Workflow und Ask in Codex

Stand: 2026-09-26. Geprüft wurden drei Workflow-Läufe im Projekt DIVI5 (NEU: Suite v2, ALT1, ALT2), ein Ask-Lauf, die installierten Skills unter `<codex-home>/skills` und die privaten Entwicklungsquellen (HEAD `d792a25`). Nur lesend; keine Session, keine Installation und keine Quelle wurde verändert. Messwerte und Methode: [Analyse](token-overhead-analyse-2026-09-26.md). Korrekturplan: [PLAN-0014](plans/0014-token-overhead-codex.md).

Maßstab: die einfachste native Codex-Lösung ohne eigene Overlays. Einzige Ausnahme ist Claude über die Claude-CLI. Nötig sind nur: nie mehr als ein schreibender Task, Ergebniszustellung und sichere Wiederaufnahme.

## Gesamturteil

**Nicht releasefähig.** Das Kommunikationskonstrukt um die nativen Aufgabenwerkzeuge verursacht im aktuellen Lauf 63 % des Coordinator-Inputs: 41 % durch Helper-/Encoding-Schichten und 22 % durch eine Warteschleife. Die Regeln zum Arbeitsverhalten sind überwiegend brauchbar; mehrere Schutzregeln gegen Polling und Kommentare sind mit e5fe414 verloren gegangen.

## Befunde

| ID | Schwere | Befund | Beleg | Auswirkung | Maßnahme |
| --- | --- | --- | --- | --- | --- |
| A1 | hoch | Lifecycle und Ergebnisprüfung laufen über `task_lifecycle.py`, `parse_role_result.py`, JSON per PowerShell-Here-String und JS-Kodierer statt über native Aufrufe | HEAD `operations-dispatch.md` Z. 52, `operations.md` Z. 29, 82–83; NEU 26 Lifecycle- und 51 Encoding-Aufrufe; NEU#1 Z. 292/298 | 7,2 Mio. Tokens (41 %) Coordinator-Input im Lauf NEU | W-003 |
| A2 | hoch | Coordinator pollt mit `wait_threads` (60 s) und Code-`wait` (30 s), Median-Abstand 34 s | HEAD `operations.md` Z. 20; NEU#2 Z. 208–345; 33 Aufrufe NEU, 286 ALT1 | 3,8 Mio. (22 %) NEU, 43,4 Mio. (35 %) ALT1 | W-002 |
| A3 | hoch | Worker-Auftrag enthält vollständige Decision-Records und Plan-Header | HEAD `build_dispatch_prompt.py` Z. 93; Auftrag 24.725 Zeichen, davon 15.934 Decisions, 2.174 Plan, 1.531 Step | Jeder Worker-Modellaufruf trägt rund 18k Zeichen ohne Bezug zum Step | W-004 |
| A4 | hoch | Ask läuft über `prepare`, `creation_result`, `match_delivery`, Warteschleife und Encoding-Schicht | Ask `SKILL.md` Z. 50–58, `references/native.md` Z. 11–22; Ask-Lauf `01a0d834…`: 62 `wait_threads`, 14 Encoding-Aufrufe | Wie A1/A2 für jede Konsultation | W-006 |
| A5 | mittel | Generierter Prompt und Leseausgaben landen mehrfach im Coordinator-Kontext | NEU#2 Z. 130/137/151/170 (31,6k/40,1k/25,0k/25,9k); NEU 23 Ausgaben > 10k, 14 doppelt gelesene Dateien | 3,2 Mio. (18 %) NEU für Skill-/Plan-Lesen | W-003, W-004 |
| A6 | mittel | Übergabe liest den Vorgänger-Thread und die Taskliste | NEU#2 Z. 77 (`read_thread`, `turnLimit:3`, `includeOutputs:true`, 40,1k), Z. 54 (`list_threads`, 13,8k); HEAD `operations-rollover.md` Z. 37 | 53,9k Zeichen pro Übergabe | W-005 |
| A7 | mittel | Schutzregeln gegen Polling und Kommentare entfernt | e5fe414; Fundstellen in `e5fe414~1`: `operations-accepted.md:37`, `operations-results.md:11`, `operations-activation.md:81`, `operations-wait.md:19/35/61`, `operations-rollover.md:156` | Coordinator 38, Worker 5,5 Kommentare pro Task (NEU) | W-002 |
| A8 | mittel | Worker-Erstellung ist langsam | Median 7 Tool-Aufrufe, 1,5 min, 0,97 Mio. Input pro Dispatch (NEU); `build_dispatch_prompt.py` mit 7 Pflichtargumenten | Verzögert jeden Step | W-004 |
| A9 | mittel | Helper werden falsch aufgerufen oder per `--help` erkundet | `observed_status` statt `status` (NEU#1 Z. 385, NEU#2 Z. 93); Altformat an Parser (NEU#1 Z. 234); `select_context.py` ohne `--format` (`01a0d834…` Z. 4088); 30 `--help`-Aufrufe über alle Läufe | Zusatzaufrufe mit je ~120k Kontext | W-003, W-007 |
| A10 | niedrig | Veraltete Legacy-Guard-Regel | HEAD Workflow-`SKILL.md` Z. 83; DIVI5-`AGENTS.md` Block `scoville-workflow-contract:v2`; Datei existiert nicht (NEU#1 Z. 84) | 3 Leseaufrufe pro Start | W-007 |
| A11 | niedrig | Installierte Skills weichen vom HEAD-Paket ab | Plan (SKILL, edit.md, read-only.md), Defaults von Workflow/Setup/Ask; Installation 25.09. 23:41, spätere Commits `c16a89c`, `d792a25` | Läufe nutzen nicht den geprüften Stand | W-010 |
| A12 | niedrig | Zeit bis zum ersten Worker unverändert | NEU 4,5 min, ALT1 3,5 min, ALT2 5,2 min | Start dauert Minuten | W-004 |
| A13 | Info | Unkommittierter Entwurf einer anderen Sitzung adressiert Teile von A2, A3, A5, A6, A7 | Arbeitsbaum, ADR-0083, Stand 00:33; ungetestet, nicht installiert | Gefahr doppelter Arbeit | W-001 |
| A14 | Info, außerhalb der Suite | Projektregeln werden in jeden Task injiziert und groß gelesen | DIVI5-`AGENTS.md` 8,5k Zeichen pro Task; `project-workflow-contract.md` 32,8k Zeichen, Coordinator 13×, Worker 5×, Reviewer 3× | Fester Grundaufwand je Task | Projekt separat |

## Was funktioniert und bleibt

- Ein Step pro Worker hält den Worker-Kontext klein (Worker-Input pro Aufruf im Median 52–131k gegenüber 121–145k beim Coordinator).
- Review mit Reparaturgrenze und automatischer Rollover sind durch frühere native Läufe belegt (PLAN-0011 W-026).
- Das Ergebnisformat `SCOVILLE_RESULT_V1` ist kurz und genügt für die Zustellung.
- Alle 13 dokumentierten Helper-Aufrufstellen in den aktuellen Quellen stimmen mit den argparse-Signaturen überein; die Fehler entstehen bei unklaren Feldnamen und fehlenden kopierbaren Aufrufen.

## Nicht geprüft

- Geldkosten; die Tokens sind überwiegend gecachter Input.
- Ob `send_message_to_thread` einen idle Coordinator in jeder Host-Konfiguration zuverlässig weckt; das belegt erst PLAN-0014 W-009.
- `skills/public` (Build-Ausgabe, auf Wunsch nicht gelesen).
