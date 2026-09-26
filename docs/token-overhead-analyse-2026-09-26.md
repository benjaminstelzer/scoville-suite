# Token-Overhead der Scoville Suite in Codex – Analyse zu PLAN-0014

Die Abschnitte 1–5 bewahren die Ausgangsanalyse und ihre damaligen Vorschläge.
Für aktuelle Anforderungen gelten PLAN-0014 und seine akzeptierten Decisions,
insbesondere ADR-0089, ADR-0092 und ADR-0093. Aktuelle Nachweise folgen unten.

Stand: 2026-09-26. Nur Analyse; keine Skill-, Code- oder Sessionänderung. Grundlage: Rollouts unter `<codex-home>/sessions` und `archived_sessions` (JSONL zeilenweise per Skript), installierte Skills unter `<codex-home>/skills`, private Entwicklungsquellen unter `skills/private/scoville-suite` (HEAD `d792a25`) und `skills/private/shared`. `skills/public` wurde nicht gelesen; die Pakete dort entstehen durch den Build.

Hinweis: Der Arbeitsbaum enthält einen unkommittierten Entwurf einer anderen Sitzung (ADR-0083, Stand 00:33) mit Änderungen an Workflow-`SKILL.md`, `operations*.md` und `build_dispatch_prompt.py`. Er ist weder getestet noch installiert. Befunde unten beziehen sich auf HEAD und die installierten Skills; wo der Entwurf einen Befund bereits adressiert, steht das unter „Status“.

## 1. Kurzfazit

Der größte Hebel ist nicht der Anleitungstext, sondern das Kommunikationskonstrukt um native Codex-Mittel. Im aktuellen DIVI-5-Lauf entfallen 41 % des Coordinator-Inputs (7,2 von 17,5 Mio. Tokens) auf Modellaufrufe nach Helper-, JSON- und Encoding-Schichten (`task_lifecycle.py`, `parse_role_result.py` über PowerShell-Here-Strings), weitere 22 % (3,8 Mio.) auf eine 30-Sekunden-Warteschleife. Codex bietet `create_thread`, `send_message_to_thread` und `set_thread_archived` direkt; ein Ende des Coordinator-Turns mit Aufwecken durch die Nachricht des Workers ersetzt die Schleife.

Kosten des aktuellen Laufs (2 Worker-Steps, 2 Reviews): 26,5 Mio. Input-Tokens insgesamt, davon 17,5 Mio. Coordinator. Pro Worker-Step 8,8 Mio. Coordinator-Input und 76 Coordinator-Modellaufrufe. Pro Worker-Erstellung im Median 7 Tool-Aufrufe, 1,5 Minuten und 0,97 Mio. Input-Tokens.

Drei größte Hebel:
1. Native Kommunikation ohne Helper-/Encoding-Schichten (P7, P3, P8): 7,2 Mio. + 0,76 Mio. (read_thread) im aktuellen Lauf.
2. Idle statt Warteschleife (P1): 3,8 Mio. im aktuellen Lauf, 43,4 Mio. im Lauf ALT1.
3. Worker erhält nur seinen Step (P5): Auftrag 24,7k Zeichen, davon 15,9k vollständige Decision-Records und 2,2k Plan-Header; der eigentliche Step hat 1,5k.

## 2. Messwerte

Läufe im Projekt `<project-root>`:

- **NEU**: Suite v2 (installiert 25.09. 23:41), DIVI-PLAN-0012, Coordinator `01a0da85…`, `01a0da9d…`, Worker `01a0da92…`, `01a0daa1…`, Reviewer `01a0da96…`, `01a0da99…`.
- **ALT1**: Workflow v0.5, Lauf `01a0d499…`, 24./25.09., 10 Coordinator-Generationen, 9 Worker, 3 Reviewer.
- **ALT2**: Lauf `01a0d3ae…`, 24.09., 3 Coordinator-Generationen, 3 Worker.

| Messwert | ALT1 | ALT2 | NEU |
| --- | ---: | ---: | ---: |
| Worker-Steps (Executor-Tasks) | 9 | 3 | 2 |
| Coordinator-Modellaufrufe | 983 | 256 | 152 |
| … pro Worker-Step | 109 | 85 | 76 |
| Coordinator-Input Summe | 122,9 Mio. | 30,4 Mio. | 17,5 Mio. |
| … pro Worker-Step | 13,7 Mio. | 10,1 Mio. | 8,8 Mio. |
| Coordinator-Input pro Aufruf Median / Max | 137,9k / 214,1k | 125,5k / 173,9k | 120,7k / 177,8k |
| Warte-/Poll-Aufrufe (`wait_threads` + Code-`wait`) | 286 | 54 | 33 |
| … pro Kind-Task | 23,8 | 18,0 | 5,5 |
| Abstand zwischen Warteaufrufen, Median | 34,3 s | 34,9 s | 34,4 s |
| Coordinator-Kommentare / Final-Meldungen | 103 / 35 | 36 / 13 | 38 / 5 |
| Worker-Kommentare pro Worker | 8,2 | 4,0 | 5,5 |
| Coordinator-Ausgaben > 10k Zeichen | 144 | 44 | 23 |
| Doppelt gelesene Dateien (Coordinator) | 26 | 8 | 14 |
| Helper-Aufrufe mit Fehler-/Usage-Signal (Coordinator) | 14 | 5 | 2 |
| Worker-Erstellung: Tool-Aufrufe / Minuten / Input (Median) | 11 / 2,2 / 1,60 Mio. | 11 / 2,6 / 1,26 Mio. | 7 / 1,5 / 0,97 Mio. |
| Zeit bis zum ersten Worker nach Workflow-Aufruf | 3,5 min | 5,2 min | 4,5 min |
| Worker-Auftrag (Zeichen) | 236–300 + Nachricht | 300 + Nachricht | 24.725 |

Anteil des Coordinator-Inputs nach auslösendem Tool (der Modellaufruf nach einer Tool-Ausgabe wird dieser Ursache zugeordnet):

| Ursache | ALT1 | ALT2 | NEU |
| --- | ---: | ---: | ---: |
| P7 Helper/Encoding (`task_lifecycle`, `parse_role_result`, Guard, Here-Strings) | 33,5 % | 41,5 % | 41,2 % |
| P1 Warten/Poll | 35,3 % | 27,3 % | 21,9 % |
| P3/P5 Skill-, Plan- und Recordlesen | 8,9 % | 12,1 % | 18,2 % |
| read_thread | 0,5 % | 0,5 % | 4,3 % |
| Dispatch (Selector, Modellpaar, Builder, create) | 4,9 % | 4,6 % | 1,8 % |

Grenzen: Tokens sind überwiegend gecachter Input; Kosten in Geld sind nicht bestimmt. NEU enthält Nutzer-Zwischenfragen zur Modelltabelle (Coordinator #1 Z. 417–604); diese Turns sind in den Summen enthalten.

## 3. Befunde P1–P9

Belegformat: `NEU#1` = `archived_sessions/rollout-2026-09-25T23-43-03-01a0da85-96be-7173-acf9-d8cd1da1e4e3.jsonl`, `NEU#2` = `…-01a0da9d-4b5b-7703-8a7f-0d95a7ec9229.jsonl`, Zeilennummern der JSONL-Datei.

| # | Befund | Beleg | Ursache | Status |
| --- | --- | --- | --- | --- |
| P1 | Coordinator pollt: 11 Paare `wait_threads` (60 s) + Code-`wait` (30 s) während eines 13-min-Workers | NEU#2 Z. 208–345; Summe 33 Warteaufrufe NEU, 286 ALT1 | HEAD `operations.md` Z. 20: „Wait for that exact task with `wait_threads` … A timeout means it is still being observed.“ Kein Idle/Wake-Weg; Worker darf laut `build_dispatch_prompt.py` Z. 92 keine Nachricht senden | offen; Entwurf `operations.md` Z. 24–30 beendet den Turn und erwartet Benachrichtigung |
| P2 | Coordinator kommentiert zwischen deterministischen Schritten | NEU 38 Kommentare, ALT1 103 | Regel „do not insert narration turns between successful deterministic operations“ in e5fe414 entfernt (P9) | teilweise; Entwurf `operations.md` Z. 14 |
| P3 | Große Leseausgaben, Prompt mehrfach ausgegeben | NEU#2 Z. 130/137/151/170: `build_dispatch_prompt` via PowerShell mit 31,6k/40,1k/25,0k/25,9k Zeichen Ausgabe; NEU#1 Z. 173/183: SKILL + References 40,1k/28,0k, dreimal gelesen | Builder-Ausgabe wird als Tool-Ergebnis in den Kontext geholt statt in derselben Code-Zelle an `create_thread` übergeben | teilweise; Entwurf `operations-dispatch.md` Z. 37–39 |
| P4 | Worker kommentiert laufend | NEU 5,5, ALT1 8,2 Kommentare pro Worker | Regel „Host-required progress commentary is at most one short factual sentence“ in e5fe414 entfernt | teilweise; Entwurf `build_dispatch_prompt.py` (Autonomie-Satz) |
| P5 | Worker bekommt und lädt mehr als seinen Step | Auftrag 24.725 Zeichen (Delegationseingang von NEU-Worker `01a0da92…`): `plan_context` 19.731, davon `decisions` 15.934 (ganze ADR-Records), `plan` 2.174, `work_item` 1.531; Worker lesen `.scoville/workflow.md` (NEU `01a0daa1…` Z. 48, 40,2k Ausgabe), Reviewer ruft `select_context.py` auf (`01a0da96…` Z. 40, 30,3k) | HEAD `build_dispatch_prompt.py` Z. 93 serialisiert die volle Selector-Projektion | teilweise; Entwurf verbietet Plan/Workflow-Laden, sendet nur Punkt |
| P6 | Übergabe liest den Vorgänger | NEU#2 Z. 77: `read_thread` des Vorgängers, `turnLimit:3`, `includeOutputs:true`, 40,1k; Z. 54: `list_threads` 13,8k | HEAD `operations-rollover.md` Z. 37 „four sections …“ und Handle-/Archivierungsschritte | teilweise; Entwurf `operations-rollover.md` Schritt 2–4 |
| P7 | Kommunikation und Lifecycle über Encoding-/Shell-Schichten | NEU: 51 Aufrufe mit `$OutputEncoding`/Here-String/`TextEncoder`/`b64`; 26 `task_lifecycle.py`-Aufrufe (create, creation_result, archive, verify_archive); NEU#1 Z. 292/298 JS-Base64-/UTF-8-Kodierer; Ask: 62 `wait_threads` im Ask-Lauf `01a0d834…` | HEAD `operations-dispatch.md` Z. 52 (create über Helper), `operations.md` Z. 82–83 (archive/verify_archive über Helper), Ask `references/native.md` Z. 11–22, Ask `SKILL.md` Z. 50–58 | Workflow teilweise im Entwurf; Ask offen |
| P8 | Helper mit falschen Argumenten bzw. per `--help` erkundet | siehe Abschnitt 5 | unklare Vertragsangaben, zu viele Pflichtargumente | offen |
| P9 | Verlorene Regeln | siehe Tabelle unten | e5fe414 „Prepare simplified Scoville Suite v2 candidates“ | offen |

Verlorene Regeln (alle in e5fe414 entfernt, Fundstelle im Vorgängerstand `e5fe414~1`):

| Regel | Datei:Zeile in `e5fe414~1` |
| --- | --- |
| „do not insert narration turns between successful deterministic operations.“ | `members/scoville-workflow-for-codex/scoville-workflow-for-codex/references/operations-accepted.md:37` |
| „Host-required progress commentary is at most one short factual sentence“ | `…/references/operations-results.md:11` |
| „after a meaningful state change or user status request, not in a polling loop.“ | `…/references/operations-activation.md:81` |
| „Do not add status polling.“ | `…/references/operations-wait.md:19` |
| „do not authorize polling, periodic progress chatter, or messages while a child is active“ | `…/references/operations-wait.md:35` |
| „emit no commentary and call `wait_threads` again …“ (Schweigepflicht in der Wartephase) | `…/references/operations-wait.md:61` |
| „Never poll for visibility.“ | `…/references/operations-rollover.md:156` |

Weitere veraltete Regeln:

- HEAD Workflow-`SKILL.md` Z. 83 und DIVI5-`AGENTS.md` (Block `scoville-workflow-contract:v2`) verlangen die Prüfung eines Legacy-`.scoville-workflow/guard.json`. Im Lauf NEU dreimal gelesen (NEU#1), die Datei existiert nicht mehr (NEU#1 Z. 84).
- Installierte Skills weichen vom HEAD-Paket ab: `scoville-plan` (SKILL.md, edit.md, read-only.md), Workflow/Setup/Ask-Defaults (`workflow.toml`, `config.default.json`) – Installation 25.09. 23:41, spätere Commits `c16a89c`, `d792a25`.
- Projektseitig (nicht Suite): DIVI5-`AGENTS.md` wird mit 8,5k Zeichen in jeden Task injiziert; `docs/general-rules/project-workflow-contract.md` (32,8k Zeichen) lesen Coordinator 13×, Worker 5×, Reviewer 3×. Separat im Projekt zu entscheiden.

## 4. Fixes (nach Einsparung, Details in PLAN-0014)

| Fix | Ersatz in 1–2 Sätzen | Bewusst bleibt | Beleg der Einsparung |
| --- | --- | --- | --- |
| F1 Native Kommunikation | `create_thread`, `set_thread_archived` und `send_message_to_thread` direkt aufrufen; Prompt bauen und Task erzeugen in einer Code-Zelle, nur IDs ausgeben. Kein `task_lifecycle.py`, keine PowerShell-Here-Strings oder JS-Kodierer im Laufzeitpfad. | Ergebnisformat `SCOVILLE_RESULT_V1`, Ergebnis vor Archivierung sichern | 41 % Coordinator-Input NEU |
| F2 Idle statt Warten | Nach `create_thread` endet der Coordinator-Turn; der Worker schickt sein Ergebnis mit einer `send_message_to_thread`-Nachricht an den Coordinator und weckt ihn so. | Genau ein schreibender Task; Stopp über Nachricht an den aktiven Task | 22 % NEU, 35 % ALT1 |
| F3 Worker bekommt nur seinen Step | Auftrag = Step-Text, Status direkter Abhängigkeiten, ID und Entscheidungssatz relevanter Decisions, kurzer Zusatz. Kein Plan-Header, keine ganzen ADRs, kein Laden von Plan/Workflow/Handoff oder `.scoville/workflow.md`. | Ein Worker pro Step; Code-Skill und Projektregeln bleiben Sache des Workers | 15,9k + 2,2k Zeichen pro Auftrag |
| F4 Einmal lesen | Jede Skill-/Referenzdatei einmal pro Coordinator-Task; Ergebnis direkt aus der Benachrichtigung statt `read_thread`; Legacy-Guard-Prüfung streichen. | Validator nach Plan-Schreiben | 18 % + 4 % NEU |
| F5 Schlanke Übergabe | Nachfolger bekommt: Skill-Aufruf, Pfad des Laufdatensatzes, Vorgänger-ID. Kein `read_thread`/`list_threads` des Vorgängers; der Vorgänger schreibt nach `create_thread` nichts mehr. | Automatischer Rollover, Laufdatensatz | 53,9k Zeichen in NEU#2 Z. 54/77 |
| F6 Verlorene Meldungsregeln zurück | Die sieben Regeln aus e5fe414 als drei Sätze im Coordinator- und Worker-Teil wiederherstellen. | Eine kurze Meldung bei Dispatch, Ergebnis, Blocker | 38 Kommentare NEU |
| F7 Schneller Dispatch | `build_dispatch_prompt.py` liefert Prompt, Titel, Modell und Reasoning in einem Aufruf; Pflichtargumente auf Einheit, Rolle und Projektwurzel senken. | Ein Step = ein Worker | 7 Aufrufe/1,5 min/0,97 Mio. pro Dispatch |
| F8 Ask nativ | Ask erstellt Advisers direkt mit `create_thread`; Advisers antworten per `send_message_to_thread`; kein `prepare`/`creation_result`/`match_delivery`, keine Warteschleife. `ask.py` nur für Konfiguration und die Claude-CLI. | Claude über Claude-CLI; keine stille Modellersetzung | 62 Warteaufrufe im Ask-Lauf |

## 5. Helper-Korrekturen

Statischer Abgleich: alle 13 dokumentierten Aufrufstellen in den aktuellen Quellen passen zu den argparse-Signaturen. Die Fehler entstehen im Lauf:

| Helper | Aufrufstelle | Falsch | Korrekt / Fix |
| --- | --- | --- | --- |
| `task_lifecycle.py` `archive` | NEU#1 Z. 385, NEU#2 Z. 93 | `"observed_status":"completed"` → `unrecognized terminal status` | Feld heißt `status`; Doku `task_lifecycle.md` Z. 89 „observed `status`“ missverständlich. Fix F1: Aufruf entfällt, `set_thread_archived` direkt |
| `parse_role_result.py` | NEU#1 Z. 234 | Altes JSON-Ergebnis statt Zeilenformat → `MAGIC_INVALID` | Nur `SCOVILLE_RESULT_V1`-Text; mit F2 kommt das Ergebnis direkt aus der Worker-Nachricht |
| `parse_role_result.py` | NEU#1 Z. 226 | `--help` zur Vertragssuche | Kopierbarer Aufruf in Doku; nach F1 kein Shell-Pipe nötig |
| `build_dispatch_prompt.py` | NEU#1 Z. 283; ALT 4× | `--help` zur Vertragssuche (7 Pflichtargumente) | Pflichtargumente auf `--unit --role --project-root` senken; Selector-Pfad und Plan-Wurzel ableiten |
| `select_context.py` | Session `01a0d834…` Z. 4088 | ohne `--format` → `the following arguments are required: --format` | `--format` default `json` wie `validate_profile.py` |
| `task_lifecycle.py` `match_delivery` | ALT1 Coordinator `01a0d49a-b05b…` Z. 376 | `wrong delivery reference` | Fix F1/F8: Referenzabgleich entfällt, Absender-Task-ID genügt |
| `manage_workflow_guard.py` | ALT: 11× `--help` | Vertragssuche | bereits entfernt (v2) |
| `ask.py` | Session `01a0d834…`: 14 Aufrufe mit Encoding-Schicht | JSON per PowerShell-Here-String | F8: `resolve` nur bei Konfigurationsbedarf, sonst native Aufrufe |

`--help`-Aufrufe über alle ausgewerteten Läufe: 30 (Guard 11, Builder 5, Lifecycle 5, Selector 4, Kontext 2, Validator 2, Parser 1).

## 6. Testgrenzen

Verbindlich sind PLAN-0014 W-008, W-009 und W-012 samt späteren Nutzerentscheidungen.
Normaler Workflow verwendet Nachrichten statt Polling; gezielte Wiederaufnahme-
abfragen bleiben erlaubt. Hostpflichten für Fortschrittsmeldungen bleiben bestehen.
Helper-Ausgaben müssen beim tatsächlichen Verbraucher ohne Reparatur funktionieren.
Luna Medium prüft Helper, SOL 6 Medium die geänderten Skills. Ask Claude behält
seine CLI-Route. Zusammenhängende Steps dürfen in Reihenfolge gruppiert werden;
der Worker erhält den vollständigen Work Item als Kontext und einen klaren Auftrag.
Archivierung wird ausgeführt, aber weder bestätigt noch nachgeprüft.

## 7. Release-Gate

Veröffentlichung erst, wenn W-008 und W-009 ihre Grenzen einhalten und die Messwerte gegen Abschnitt 2 dokumentiert sind (PLAN-0014 W-010).

## 8. Umsetzungsnachweise und verbleibender Vergleich

Kanonische Änderungen und Verbraucherbelege stehen unter
development/luna-tests/token-overhead-implementation.md,
suite-simplification-comparison.md und private-helper-inventory.md.
Das historische Vergleichsskript und seine Auswahl sind dort reproduzierbar
gesichert; ADR-0086 hält die genehmigte Korrektur uneinheitlicher Zählweisen fest.

Der native SOL-6-Medium-Gruppenlauf PLAN-0003 ist abgeschlossen. Er umfasst
Steps 1–4 als Bibliotheksgruppe und danach Steps 5–6 als CLI-Gruppe, zwei Reviews,
einen tatsächlichen Worker- und einen Coordinator-Rollover. Acht fokussierte
Tests bestanden; CLI-Beispiel words=4 lines=2 und Fehlerfall Exit 1 sind ausgeführt.
Planvalidierung meldet null Fehler/Warnungen. Rohereignisse belegen direkte
Builder-stdout-Verwendung in create_thread ohne doppelte Promptausgabe, einmaligen
Work-Item-Kontext und Fortsetzung nach Rollover ohne erneute erledigte Arbeit.

| PLAN-0003 Coordinator-Messung | Wert |
| --- | ---: |
| Coordinatoren / Worker / Reviewer | 2 / 3 / 2 |
| Modellaufrufe | 78 |
| Inputtokens | 5.596.543 |
| Warteaufrufe | 0 |
| Erkannte Helper-Usage-Fehler | 0 |
| Worker-Promptgrößen, Zeichen | 8.603 / 9.885 / 8.662 |

Quelle: temp/2026-09-26-private-helper-tests/native-run-3-audit im Workspace,
mit manifest.json, gesicherten Rolloutausschnitten und metrics.json.
Die 1%-Schwellen erzwingen Rollover für die Funktionsprüfung; diese Zahlen
belegen keine repräsentative Einsparung und sind nicht direkt mit DIVI vergleichbar.
Inputtokens enthalten Cacheinput und sind keine Geldkosten.

Der kontrollierte Vorher-/Nachherlauf verwendet dasselbe neue Drei-Step-Fixture,
SOL 6 Medium in allen Rollen, 75%-Schwellen und frische Coordinatoren. Protokoll:
temp/2026-09-26-private-helper-tests/controlled-comparison/protocol.md.
Beide Läufe sind abgeschlossen. Reguläre Installation und Veröffentlichung
bleiben ausschließlich in PLAN-0012.

## 9. Kontrollierter Vergleich: PLAN-0004 gegen PLAN-0005

Gleiches Drei-Step-Fixture und gpt-6-sol/medium in allen Rollen; beide mit
75%-Kontextschwellen, ohne künstliche Unterbrechung oder Nutzersteuerung.
Ausgang: drei Worker und drei Reviewer. Kandidat: eine zusammenhängende
Step-Gruppe, zwei Reviewer und eine echte Reparatur eines Testimports.
Beide Endstände bestehen acht fokussierte Tests und die Planvalidierung.

| Messwert | Ausgang | Kandidat | Änderung |
| --- | ---: | ---: | ---: |
| Coordinator-Modellaufrufe | 84 | 41 | −51,2 % |
| Coordinator-Inputtokens | 4.672.761 | 1.944.090 | −58,4 % |
| Coordinator-Outputtokens | 18.804 | 9.663 | −48,6 % |
| Modellaufrufe aller Rollen | 143 | 75 | −47,6 % |
| Inputtokens aller Rollen | 6.670.228 | 3.075.684 | −53,9 % |
| Outputtokens aller Rollen | 28.512 | 15.608 | −45,3 % |
| Davon Cacheinput aller Rollen | 6.380.160 | 2.840.576 | enthalten im Input |
| Ungecachter Input aller Rollen | 290.068 | 235.108 | −18,9 % |
| Erstauftrag ab Startnachricht | 100,893 s | 62,606 s | −37,9 % |
| Coordinator-Warteaufrufe | 6 | 0 | −6 |
| Erkannte Helper-Usage-Fehler | 0 | 0 | unverändert |

Die Zahlen enthalten die gesamte Kandidaten-Reparatur samt erneutem Review.
Es wurde keine günstigere hypothetische Variante ohne Reparatur angesetzt.
Einzelne Worker-Aufträge sind größer: 7.351 Zeichen für die Dreiergruppe
gegenüber 5.435/5.404/5.403 für drei Einzelaufträge. Die Gruppierung spart
wiederholten Rollen-/Kontextaufwand, nicht jeden einzelnen Prompt-Charakter.

Quellen und Zählung: controlled-comparison/baseline-manifest.json und
candidate-manifest.json im Testbereich, unveränderte lokale Rolloutkopien,
baseline-analysis.json und candidate-analysis.json. Unique response IDs werden
einmal gezählt. Die detaillierten Token-/Übergabewerte stehen in comparison.md.
Dies ist ein beobachtetes Vergleichspaar, keine allgemeine Verteilung oder
Geldkostenrechnung. Cacheinput ist Teil des Inputs, kein zusätzliches Volumen.

Die Startmeldung nennt Plan, Gruppierung und Grund in zwei Sätzen. Tatsächlich
erzeugte Worker-/Reviewer-/Repair-Titel enthalten STEPS-1-3. Native Probe und
Grenzen: grouping-title-test.md. Der frühere PLAN-0001-Stopptest belegt getrennt
die gezielte Wiederaufnahme; dessen Recovery-Abfragen zählen nicht in dieses
Vergleichspaar. PLAN-0003 belegt getrennt die tatsächlichen Rollover.

### Tatsächliche Übergaben

Kandidatenaufträge: 7.351 Zeichen Worker, 7.187 erster Reviewer, 8.592 Repair,
7.441 zweiter Reviewer. Zusammen 30.571 statt 30.966 Zeichen für sechs
Ausgangsaufträge (−1,3 %). Allein die Worker-Aufträge sinken durch Gruppierung
von insgesamt 16.242 auf 7.351 Zeichen (−54,7 %). Die vier tatsächlichen
Rollenrückgaben umfassen 284/491/257/195 Zeichen, zusammen 1.227 statt 1.898.

Der vollständige Work Item steht pro Auftrag einmal. Zusatzkontext enthält
nötige Ziele/Grenzen und bei Review/Repair die wirklichen Befunde. Kein ganzer
Plan, kein Vorgängerchat, keine doppelte Promptausgabe. Die Builder-Ausgabe
geht direkt in derselben Code-Zelle an create_thread. Kein erfolgreicher
Helpertext wurde korrigiert oder als JSON von Hand rekonstruiert.
Coordinator-read_thread-Aufrufe sinken von sieben auf null; Rückgaben kommen
direkt per Nachricht. Beide Läufe hatten je eine lokale Patchkorrektur,
die als solche dokumentiert bleibt und kein Helperfehler ist.

### Rückgabe an PLAN-0012

PLAN-0012 W-017 erhält diese Auswertung und
development/luna-tests/suite-simplification-comparison.md mit der finalen
SOL-Paketzuordnung, privaten Helperinventar und ausdrücklich benannten Grenzen.
candidate-grouping-titles entsprach den 104 damaligen Stagingdateien.
Der anschließende Titelstand candidate-ask-titles verändert ausschließlich
Ask README.md und references/native.md; alle 104 Dateien entsprechen dem
danach erzeugten Staging. ask-final-package-match.json sichert den Vergleich.
development/luna-tests/ask-title-final.md belegt den zusätzlichen nativen
SOL-Medium-Titeltest mit Rückzustellung. Der abschließende candidate-astra-final
enthält nur zwei weitere geänderte Paketdateien: Workflow README.md und
references/operations-dispatch.md. Alle 104 Dateien entsprechen dem Staging
(astra-final-package-match.json). development/luna-tests/astra-final-review.md
sichert zwei behobene Findings, Astras Nachreview ohne materiellen Restbefund
und den erfolgreichen SOL-Medium-Verbrauchertest der Kürzungssperre.
Coordinatoren des Vergleichs: 01a0dcde-72d2-70f3-a13b-dd08b4452ee5 (Ausgang)
und 01a0dced-78b1-7040-a790-463fdb4ed22f (Kandidat).

Offen im Releaseplan bleiben der sichere reguläre Installationsabgleich,
saubere committete Veröffentlichungsquelle und die bestehenden Remotegates.
Live-Familien-/source-only-Audits melden noch die früheren veröffentlichten
Namen/Reihenfolgen. Der Release-Verifier selbst bestand mit einem echten,
sauberen und lokal committeten Testquellbaum und unverändertem Buildreceipt.
Diese Tests erteilen keine Veröffentlichungsgenehmigung. Der DIVI-Stopp bleibt.
