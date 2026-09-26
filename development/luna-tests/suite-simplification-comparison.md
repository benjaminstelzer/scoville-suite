# Gezielte Vergleiche für PLAN-0011

Verwende run_codex_cli_case.py und sein bestehendes Ergebnisformat. Rohdaten und
Ausgangskopien bleiben unter workspace temp/2026-09-25-suite-simplification/.
Kein vollständiger Suite-Lauf ist Voraussetzung dieser Vergleiche.

Vergleiche je Fall Ausgangsstand, Kandidat und einen einfachen Zielprompt.
Gleiche Aufgabe, Eingaben, Modell, Effort, Host und Laufgrenzen verwenden.
Fallauswahl und erwartetes Verhalten vor der Ausgangsmessung festhalten.
Schlussfälle getrennt zurückhalten; nicht zur Formulierungsoptimierung nutzen.

| Umbau | Fälle vor der jeweiligen Änderung festlegen |
| --- | --- |
| W-008 | Einfügen, Next action, Evidence, Abschluss; Wiederaufnahme als Schlussfall |
| W-010 | Normaler Mehr-Einheiten-Lauf und belegter Fehler; Reparaturgrenze und Wiederaufnahme als Schlussfälle |
| W-011 | Mehrdeutige Routingfälle und korrekte Bestandsfälle; anders formulierter gleichartiger Fall als Schlussfall |

Pro Variante und Fall eine Ergebniszeile speichern:

| Variante | Fall | Modell / Effort / Host | Ergebnis und Begründung | Geladene Referenzen | Tokens | Aufrufe | Dauer |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Ausgang / Kandidat / Zielprompt | Fall-ID | beobachtete Metadaten | bestanden / Fehler / nicht geprüft | Pfade | beobachtete Werte oder nicht verfügbar | beobachtet | gemessen oder nicht verfügbar |

manifest.json enthält angefragtes Modell/Effort und den CLI-Pfad. summary.json
enthält Fall, turns, served_files, Ergebnis und native Identitätsprüfung.
Tokenwerte stehen je Turn unter usage; fehlende Felder sind nicht verfügbar,
nicht null Kosten. Keine ungeprüfte Summe über kumulative Werte bilden.
Dauer bei Bedarf außen mit einer monotonen Uhr messen; der Runner speichert sie
bisher nicht. Lokale CLI-Ausführung belegt keine Desktop-Hostausführung.
Das semantische Urteil bleibt getrennt vom Protokollergebnis.

Die vorhandenen EventContractTests und TurnBudgetTests liefern eine kleine
kontrollierte Probe des Ergebnisformats. Sie belegen keine Modellleistung.
Echte Ausgangs- und Kandidatenmessungen gehören zu W-008, W-010 und W-011.

## Plan-Zwischenstand am 25. September 2026

Drei begrenzte hypothetische Vier-Fälle-Läufe mit gpt-6-luna und medium
über dieselbe Codex-CLI: Einfügen, Next action, Evidence und Abschluss.
Alle drei Läufe bestehen das Runnerprotokoll. Ausgang und Kandidat erhalten
in den Antworten die geforderten Zustände und behaupten keine ausgeführten
Tests. Der Kandidat verlangt keinen Schreibprofil-Helper mehr. Der einfache
Prompt trifft die grundlegenden Zustände, nennt beim Abschluss aber nicht
ausdrücklich das Entfernen von Next action und das Leeren der Blocker.
Das ist kein Nachweis tatsächlicher Dateiedits.

| Variante | Turns | Referenzen | Sekunden | Inputtokens je Turn | Outputtokens je Turn |
| --- | --- | --- | --- | --- | --- |
| baseline | 3 | 7 | 37.7 | 26796 / 52064 / 78572 | 324 / 333 / 1228 |
| candidate | 3 | 7 | 56.9 | 26833 / 75445 / 101103 | 472 / 690 / 2110 |
| simple | 1 | 0 | 26.8 | 34380 | 1021 |

Die Tokenfelder werden unverändert je Turn berichtet und nicht summiert.
Der Kandidat belegt hier keine Token- oder Zeitersparnis. Alle sieben
Referenzen G/P/L/E/W/V/R wurden auch beim Kandidaten geladen.
Zwei verbliebene Schreibprofilformulierungen in P und D wurden erst nach
dieser Kandidatenmessung entfernt; die Messung gilt für den gesicherten Stand.

Unabhängiger lokaler Ausführungsnachweis: Im gebauten General-Paket wurde
Next action einer isolierten gültigen Fixture geändert. Python 3.10.20
validierte danach alle drei Records ohne Fehler. Das Paket enthält weder
Schreibprofilresolver noch prompting.toml. Ein erster Versuch schrieb
versehentlich CRLF und wurde korrekt vom derzeitigen Validator abgelehnt;
LF bestand. CRLF-Unterstützung bleibt W-009. Die 78 Plan-Tests bestanden
vor der abschließenden Bereinigung der beiden Profilformulierungen.

Abschließend bestanden: 78 Plan-Tests erneut nach der Textbereinigung;
General-Paket mit 20 Dateien und Codex-Suite-Mitglied mit 18 Dateien samt
Linkprüfung und ohne entfernte Profilabhängigkeiten. Eine isolierte Fixture
wurde pausiert, mit dem Selector wiedergefunden und auf in_progress gesetzt.
Selector und Validator bestanden vor und nach Wiederaufnahme unter Python 3.10.
Die abschließende Suche nach Hash-/Profilanweisungen fand nur drei ausdrückliche
Aussagen zum Wegfall der Belegpflicht und zur historischen Lesbarkeit.
W-008 ist abgeschlossen. Eine Kostenverbesserung ist nicht belegt.

Task-IDs: Ausgang 01a0d872-91b7-7961-9358-8582582013ba;
Kandidat 01a0d87f-23e2-7bf3-a58d-5c0904040696;
Zielprompt 01a0d87f-9db9-7c60-93b9-52f74b13b0a7.

## Code- und UI-Sprachprüfung am 25. September 2026

Je vier hypothetische Routingfälle, gpt-6-luna / medium, gleiche CLI und
Leseprotokoll. Die erfolgreichen Ausgangs- und Kandidatenläufe erhielten
dieselben Fälle. Keine Projektaktionen oder gerenderten UI-Tests.

| Bereich / Variante | Turns | Referenzen | Sekunden | Inputtokens je Turn | Outputtokens je Turn |
| --- | --- | --- | --- | --- | --- |
| scoville-code-anti-ai-slop / baseline-v3 | 2 | 1 | 18.5 | 27063 / 42242 | 191 / 429 |
| scoville-code-anti-ai-slop / candidate | 2 | 2 | 33.3 | 27152 / 43831 | 413 / 1291 |
| scoville-ui / baseline-v2 | 2 | 4 | 21.8 | 40294 / 63528 | 228 / 543 |
| scoville-ui / candidate | 2 | 4 | 22.9 | 26763 / 48855 | 203 / 466 |

Code: Beide Fassungen erkennen Structural beim geänderten serialisierten
Cachefeld, Normal beim Kommentar und die weiter geltende Develop-Aufgabe trotz
fehlender Produktentscheidung. Der Kandidat trennt Klassifikation von
Ausführungsrecht und lädt beim angefragten Migrations-Dry-run Change und
Validation. Der Ausgang nennt dort nur Change und beschränkt sich auf
Klassifikation. Die neue Formulierung ergänzt keine Ausführungsbefugnis.

UI: Beide Vier-Fälle-Läufe erhalten Ownership-only, Evidence-only, die
begrenzte Source-only-Ausnahme und den Ausschluss von SlotFill. Der Kandidat
lädt für gewöhnliche Prosa keine strukturierten Ausgabeidentifier. Die
Greenfield-Zuständigkeit bleibt unverändert. Ein gesonderter Schlussfall prüft
das bedarfsweise Nachladen des exakten Ausgabeformats.

Die ersten Ausgangsläufe mischten READ-Zeilen und Antworten und scheiterten
am Protokoll. Nach Präzisierung desselben Protokolls für beide Varianten
scheiterte ein Code-Lauf zusätzlich mit leerer Antwort und code-mode-host-Fehler.
Diese Läufe sind keine fachlichen Bestehensnachweise. Die einfachen
Kontrollprompts verlangten nicht vorhandene bzw. nicht manifestierte Skillpfade.
Damit fehlt ein auswertbarer semantischer Vergleich mit dem einfachen Prompt.

Die Tokenwerte bleiben getrennt je Turn. Weder diese Einzelmessungen noch
die kürzere bedingte Referenz belegen geringere Laufzeit oder Tokenkosten.
Anthropic und reale UI-Ausführung wurden hier nicht geprüft.

Beobachtete Task-IDs:
- scoville-code-anti-ai-slop-wording-baseline: 01a0d8a6-3b40-7833-ace2-665b11bb2aaa (FAIL im Protokoll).
- scoville-code-anti-ai-slop-wording-baseline-v3: 01a0d8ac-1c46-7591-adf2-914324549fb2 (PASS im Protokoll).
- scoville-code-anti-ai-slop-wording-candidate: 01a0d8ac-1d1c-7462-8d64-d2495a7db76e (PASS im Protokoll).
- scoville-code-anti-ai-slop-wording-simple: 01a0d8ad-21c3-72b1-a020-4d0f6d5869c0 (FAIL im Protokoll).
- scoville-ui-wording-baseline: 01a0d8a6-3c40-7252-91de-880b8cce72d8 (FAIL im Protokoll).
- scoville-ui-wording-baseline-v2: 01a0d8a9-e556-7d63-9d33-a1115c4cdc36 (PASS im Protokoll).
- scoville-ui-wording-candidate: 01a0d8ac-1e2c-7053-99fe-d7a3639f07aa (PASS im Protokoll).
- scoville-ui-wording-simple: 01a0d8ad-22b1-7303-9145-66026613cefc (FAIL im Protokoll).
- scoville-ui-wording-structured: 01a0d8b1-330f-76c1-abe9-5be7f21bcbd6 (PASS im Protokoll).
- scoville-ui-wording-structured-final: 01a0d8b3-7468-7951-b651-b9c4ac5fb243 (PASS im Protokoll).
- scoville-ui-wording-structured-fixed: 01a0d8b2-4660-74b1-8c3f-fd741b48e7a5 (PASS im Protokoll).

Der erste strukturierte Schlussfall lud die neue Referenz, ließ aber zwei
zusätzliche Verbote für den unbekannten React-Eigentümer aus. Die Matrix
verlangt jetzt ausdrücklich die Kombination mit den Runtime-Regeln. Ein
weiterer Lauf wich auf Framework aus und erfand Ausgabeidentifier. Der
Einstieg unterscheidet deshalb jetzt das Lesen zur Admin-Klassifikation von
der Anwendung der Implementierungsregeln auf unterstützte Seiten.
Der abschließende Lauf 01a0d8b3-7468-7951-b651-b9c4ac5fb243 lud Adapter,
Routing und classification-output.md. Alle sechs Felder und die fünf
hier erforderlichen Verbote stimmen. Drei Turns, 19.3 Sekunden. Dies ist ein
nachgebesserter Regressionstest, kein weiterhin unabhängiger Schlussfall.
Die Ausgabeextraktion bewahrt die bisherigen Identifier und ihre Semantik.
Beide Paketprofile bestehen die Linkprüfung (Code 11, UI 24 Dateien).
Der bekannte quick_validate-Konflikt beim optionalen compatibility-Feld
bleibt der unter W-007 dokumentierte Unterschied, kein neues Bestehen.

## Workflow-Ausgang für W-010

Nach W-005/W-017 wurden vollständige Quelltexte, Shared-Imports und das
gebaute Codex-Paket vor dem Orchestrierungsumbau gesichert. Drei hypothetische
Fälle: zwei Einheiten mit und ohne Review, Worker-/Koordinator-Rollover,
Archivierungsfehler und Reparaturgrenze. gpt-6-luna / medium, vorhandene CLI.

Task 01a0d8c5-2833-7ae3-a4e4-4ecb191ee3a1: 4 Turns, 64.7 Sekunden, Protokoll bestanden.
Inputtokens je Turn: 16298 / 39687 / 75466 / 115052.
Outputtokens je Turn: 226 / 329 / 507 / 1913.
Geladene Referenzen: references/operations.md, references/operations-dispatch.md, references/operations-checkpoint.md, references/operations-compaction.md, references/operations-review.md, references/operations-activation.md, references/operations-wait.md, references/operations-selection.md, references/operations-results.md, references/operations-accepted.md, references/operations-scope.md, references/operations-rollover.md.

Die Antwort beschreibt Parken/Aktivieren und die blockierende Archivprüfung.
Sie erhält Review bei Code und die Grenze von drei Reparaturen. Der anfängliche
separate Launcher-/Koordinatorstart wird nicht vollständig beschrieben und die
konfigurierten Schwellen werden nicht aus dem Asset nachgeladen. Daher kein
vollständiges semantisches Bestehen. Das ist eine Erklärungssimulation, kein
realer Mehr-Einheiten-Lauf und kein Nachweis tatsächlich erstellter Nachfolger.

Separater read-only Test am realen aktuellen Desktop-Rollout: Der gebaute
Checkpoint erkennt die eigene Task-ID, frische Telemetrie mit 203319 Inputtokens
bei 258400 Fenstergröße und liefert context_handoff für die Workergrenze 75.
Der Test löste keinen Taskwechsel aus. Seine Aufgabe ist der Nachweis des
verfügbaren tatsächlichen Kontextsignals, nicht die Rolloverabnahme.

### W-010: erster Kandidatenlauf

Task 01a0d8d9-00d0-79e2-a764-e9188fd4e9ec, gpt-6-luna / medium:
Ein Turn, 9.7 Sekunden, 32089 Inputtokens und 180 Outputtokens. Das Protokoll
scheiterte an angeforderten, nicht vorhandenen Phasenreferenzen. Neben den drei
verlinkten aktuellen Referenzen erfand die Antwort checkpoint-, compaction-
und review-Dateien. Keine Szenarioantwort und kein semantisches Bestehen.
Die Kernanweisung benennt nun ausdrücklich, dass die drei Laufzeitreferenzen
auch diese Abläufe vollständig enthalten. Ausgangslauf und Fehlversuch bleiben
erhalten; aus dem frühen Abbruch wird keine Aufwandsersparnis abgeleitet.

Der zweite Kandidatenversuch (Task 01a0d8db-68d6-75e1-b56a-eb6e62450488,
ID aus dem tatsächlichen thread.started-Ereignis) endete mit CLI-Code 1 und
empty_agent_response. Davor forderte die Teilantwort erneut nicht vorhandene
Phasenreferenzen an. Keine abgeschlossene Antwort, keine neue semantische
Abnahme und keine erneute unveränderte Wiederholung. Der nächste Vergleich
muss die Ursache dieser Referenzanforderungen und den Testkontext klären.

### W-010: Vergleich mit sichtbarem Paketverzeichnis

Alle drei Varianten erhielten dasselbe neutrale Verzeichnisformat und das
bisherige Szenario. Der READ-Platzhalter erlaubt nun auch scripts und assets.
Das beseitigt die künstliche Unkenntnis vorhandener Dateinamen, erzwingt aber
keine bestimmte Lektüre. Ergebnisse:

- Baseline: Task 01a0d8de-73dd-7bd0-9b59-880788df63db, Abbruch nach 120.6 Sekunden am Testlimit, keine abgeschlossene Antwort und keine Tokenmessung.
- Kandidat: Task 01a0d8de-73d2-76d0-9ec9-69d35caada76, zwei Turns, 16.1 Sekunden. Inputtokens 16155/35190, Outputtokens 77/167. Erst richtige Referenzen, danach erneut die nicht vorhandene operations-checkpoint.md. Protokoll fehlgeschlagen.
- Einfacher Prompt: Task 01a0d8de-7496-7770-87b0-58e9a3ebdf71, ein Turn, 6.7 Sekunden. Inputtokens 11581, Outputtokens 87. Verlangt task_lifecycle.md unter references statt scripts. Protokoll fehlgeschlagen.

Keine Variante dieses Vergleichs erreichte eine Szenarioantwort. Keine
Kostenverbesserung und kein Modellverständnisnachweis. Der Baseline-Timeout
ist eine Grenze dieses kurzen Erklärungstests, nicht der produktive
Reviewtimeout. Keine weitere unveränderte Wiederholung. Tatsächliche
Dateiauflösung und Ablaufausführung werden im nativen Fixturelauf geprüft.

Nativer Fixturelauf gestartet: Koordinator 01a0d8e2-673d-71c1-bf6a-803bf31e6749,
Modell gpt-6-sol/medium.
Zwei Einheiten, absichtliche Konfigurationswerte 1/1 Prozent, tatsächliche
Telemetrie, keine Änderungen außerhalb des Fixtures. Start ist noch kein
Abnahmeergebnis. Defaultgrenzen 25/75 wurden unabhängig deterministisch geprüft.

### W-010: vollständige Texte ohne READ-Protokoll

Ein zusätzlicher kontrollierter Vergleich lieferte die jeweils vollständigen
Laufzeitreferenzen samt Defaults und Lifecycle-Vertrag im Startprompt. Der
Kontrollprompt erhielt nur seine kurze Anweisung. Derselbe Dreifallauftrag,
gpt-6-luna/medium und 3600 Sekunden Testlimit. Dies prüft die Erklärung des
Ablaufs bei verfügbarer Quelle, nicht bedarfsgerechtes Dateiladen.

| Variante | Task | Sekunden | Input / Output | Ergebnis |
| --- | --- | --- | --- | --- |
| Ausgangsfassung | 01a0d8e6-29f2-7272-91a3-fc5d508b0af2 | 24.1 | 42772 / 1095 | Protokoll bestanden; beschreibt alte Guard-/Archivblockade; separaten anfänglichen Launcherstart ausgelassen |
| Kandidat | 01a0d8e6-2916-7df1-afc7-53d16184b181 | 27.7 | 20524 / 1201 | Alle drei Fälle gemäß neuem Vertrag erklärt |
| Einfacher Prompt | 01a0d8e6-2a87-7cd3-9eea-dde64662e8c0 | 21.6 | 11462 / 977 | Protokoll bestanden; Worker erzeugt fälschlich selbst Nachfolger und Koordinator rollt auch nach letzter Einheit ohne Restarbeit über |

Der Kandidat erhält eine Einheit pro Worker, Code-Review, Plan-/Commithoheit,
drei Reparaturen, echte Nachfolger bei 80/30 Prozent, gleiche Rolle/Einheit/
Modellpaar/Run, beendeten Vorgänger vor Weiterarbeit und nichtblockierende
Archivfehler. Das ist ein bestandenes erklärendes Szenario, keine reale
Ausführung. Die Kandidatenquelle benötigt in diesem Volltextversuch weniger
Inputtokens als die Ausgangsfassung, läuft aber nicht schneller. Verschiedene
Cacheanteile und eine einzelne Probe erlauben keine allgemeine Kostenprognose.
Die früheren Fehler bei selbst angeforderten Referenzen bleiben bestehen und
werden durch diesen Test nicht nachträglich zu Erfolgen.


## PLAN-0013: Ausgangsmessung am 25. September 2026

Vier getrennte hypothetische Verständnis- und Lesevergleiche ohne Projektaktionen.
Quellen und gebautes General-Paket vor Änderung gesichert unter
`<workspace-root>/temp/2026-09-25-plan-0013/`. Das vorhandene Paket bestand
`build_suite.py --check-packages`. Fälle, Schlüssel, Befehle und Rohdaten liegen
in `cases.json`, `expected.md`, `baseline-commands.json` und `baseline-*`.

Identische Bedingungen für die Nachmessung: gpt-5.6-luna / medium, Windows CLI,
8 Turns höchstens, 90 Sekunden pro Turn. Aktuelle CLI SHA256
`0122378c15dc0c3c0af0d6addf2dd278125c19676b41fadaa520f89d2c9e0079`,
Katalog `40613815a90ec48dd1ccef6cdf9ef3e0c94c8594812eccc1bd69afadea02ef14`.
Die alte festgeschriebene CLI fehlt. Die aktuelle bestand vor Backend-Aufrufen
mit dem bestehenden lokalen Preflight-Verfahren: genau Luna/medium, keine
Tools und kein Auth-Header, beendeter Prozessbaum. Das ist neue lokale
Qualifikation, keine übernommene Host- oder Backend-Garantie.

Bytes zählen einmal SKILL.md und jede tatsächlich gelieferte Referenz als
UTF-8/LF. Wiederholte Lieferungen würden erneut zählen; der unveränderte Runner
lehnt doppelte READ-Anfragen ab. Read-Anfragen sind angeforderte Zeilen, keine
Tool-Aufrufe. Alle beobachteten Eventströme enthalten null Modell-Tool-Aufrufe.
CLI-Turns stehen getrennt. Tokenwerte bleiben unverändert je Turn in Rohdaten;
Gesamtkosten und vergleichbare Gesamtdauer sind nicht verfügbar.

| Fall | Gelieferte Dateien nach SKILL.md | Bytes | READ-Anfragen | Tools | Turns | Ergebnis |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| Einfügen | G / P / W / E / V | 44844 | 5 | 0 | 3 | Protokoll PASS; separate Aufgabe und unveränderter aktueller Punkt; Position gegenüber W-002 nicht eindeutig erklärt |
| Fortschreiben | keine | 7376 | 4 | 0 | 1 | FAIL unmanifested_request; Leerzeichen am READ-Pfad |
| Abschluss | keine | 7376 | 6 | 0 | 1 | FAIL unmanifested_request; Leerzeichen am READ-Pfad |
| Wiederaufnahme | R / P / L / W / E | 44392 | 5 | 0 | 2 | Protokoll PASS; Rückkehr und historische Priorität erhalten; vorgeschriebener Selector und abschließender Validator nicht genannt |

R=`references/read-only.md`, G=`references/planning-granularity.md`,
P=`references/native-plan-format.md`, L=`references/native-project-lifecycle.md`,
W=`references/native-work-items.md`, E=`references/native-editing.md`,
V=`references/profile-validation.md`. Keine Variante belegt tatsächliche Edits.
Die früh abgebrochenen Fälle belegen keine geringere erforderliche Lesemenge.

Task-IDs in Fallreihenfolge: `01a0da4f-0ae2-78f0-82f5-239cd16267a3`,
`01a0da50-4e7d-75b0-9605-bf33e4983623`,
`01a0da50-b607-77a0-8045-38332b8a7af2`,
`01a0da50-cf43-7690-8a8b-682513d153a9`.


### PLAN-0013: Verhaltensregressionen vor dem Review

73 Python-Tests bestehen auf Windows unter Python 3.11.15 und 3.14.3.
`valid-profile` und `record-writing/before` sowie `record-writing/after` liefern
jeweils valid:true. Negative historische Batch-Tests bleiben unverändert.
Validator und Selector sind bytegleich zum gesicherten Ausgang.

Ein frischer Luna-Medium-Subagent führte fünf isolierte Fälle mit tatsächlichen
Edits aus. Rohbericht: `<workspace-root>/temp/2026-09-25-plan-0013/model-edits/results.md`;
unabhängige Endzustandsvergleiche: `model-edit-observer.json`. Angefragtes Modell:
gpt-6-luna / medium; Subagent `/root/plan_model_edits`. Diese Ausführung ist vom
CLI-Lesevergleich mit gpt-5.6-luna getrennt und kein vergleichbarer Kostenlauf.

- Reihenfolge: W-003 und W-004 am Ende; ausdrücklich priorisiertes W-005 nach W-001. Keine neuen Präfixe, alte W-001/W-002-Blöcke unverändert.
- Rückkehr: tatsächliches `python check.py` meldet PASS; W-003 done und W-001 wieder aktiv. Historisches W-002-Prioritätspräfix erhalten. Ein Zwischenzustand ließ current_item noch auf done W-003 stehen; der Validator erkannte ihn. Nach Korrektur war der Endzustand gültig. Kein fehlerfreier Erstlauf behauptet.
- Decisions: Zwei einzelne akzeptierte Übergänge ohne neue Batch-Felder, jeweils validiert. Der bestehende Batch blieb bytegleich.
- General ohne Python: Nur die beauftragte Next action geändert, manuell geprüft, kein Python-Aufruf im Modellfall.
- Codex ohne Python: Die verlangte Änderung blieb aus; das Modell meldete die erforderliche Runtime als fehlend. Unveränderte Dateien unabhängig bestätigt.

Der allgemeine Skill-Creator-Check scheitert am vorhandenen `compatibility`-Feld;
der Repository-Builder akzeptiert es. Das ist keine erfolgreiche zusätzliche
Paketkonformitätsprüfung. Der Nutzer hat Viewer-Tests ausdrücklich ausgenommen
(ADR-0078); Rust wurde nicht installiert und Viewer-Kompatibilität nicht als
geprüft ausgegeben.


### PLAN-0013: Reviewkorrekturen und Ende ohne W-007

Astra-Review `01a0da62-677e-74b0-9641-f493f836d259`, angefragt gpt-6-astra/medium,
frischer Kontext. Das Ergebnis traf unmittelbar vor dem bestätigten Stop ein.
Tatsächliches Modell/Effort war dem Reviewer nicht bestätigt. Er meldete eine
verlorene draft-Aktivierungsgrenze, beschädigte Unicode-Zeichen und fehlenden
entscheidungswirksamen Nachweis historischer Priorität. Der Nutzer beauftragte
die Berücksichtigung trotz Abbruch von W-007; W-008/W-009 bewahren die Korrekturen.

- Aktivierung verlangt wieder einen draft Plan. Completed/cancelled bleiben terminal; die enge ungestartete Ausnahme erlaubt keine Reaktivierung.
- Der Windows-Standard cp1252 hatte bei Python-Textreads UTF-8-Zeichen fehlkonvertiert. Die Planquelle war beschädigt, nicht die UTF-8-Leselogik des Viewers. Goal/Non-goals sowie ursprüngliche Titel, Abhängigkeiten, Outcome, Acceptance und Steps von W-001 bis W-006 stimmen nach Reparatur mit activation-before überein. edit.md verlangt explizites UTF-8 und korrekt gekoppelte PowerShell-/Python-Streams. Umlaut-Roundtrip, LF und fehlendes BOM wurden tatsächlich geprüft.
- Frischer Luna-Medium-Fall unter `priority-edits`: W-003 mit historischer Priorität wird vor dem im Dokument früher stehenden W-002 ausgewählt. Fremder W-002-Block blieb unverändert; finaler Validator und Selector bestehen. Modellseitige Patch-/Pfadfehler wurden erkannt und korrigiert; kein fehlerfreier Erstlauf behauptet.
- Derselbe Lauf löste den separaten Rückkehr-/Prioritätskonflikt zunächst falsch durch Rückkehr auf. Das Ergebnis bleibt als Fehllauf erhalten. Die Lifecycle-Regel verlangt jetzt vor Abschluss den Vergleich aller einschlägigen Rückkehr- und Prioritätsziele.
- Frischer Nachtest `conflict-recheck`: Check meldet PASS; W-003 bleibt in_progress/current und fragt zwischen W-001 und W-004. Beide Ziele und der unbeteiligte W-002-Block bleiben unverändert. Validator, Selector und unabhängiger Endzustandsvergleich bestehen.

Rohdaten unter `<workspace-root>/temp/2026-09-25-plan-0013/`: `astra-review-result.md`,
`priority-edits/results.md`, `priority-observer.json`, `conflict-recheck/results.md`,
`conflict-observer.json`. Die Modellfälle verwenden angefragt gpt-6-luna/medium
als frische Subagents `/root/historical_priority` und `/root/successor_recheck`.
Nach Aktivierungs- und Encodingkorrektur bestanden 74 Tests unter Windows mit
Python 3.11.15 und 3.14.3; nach der letzten Konfliktpräzisierung wurden die fünf
betroffenen Routing-/Quellverträge unter beiden Versionen erneut geprüft.

W-007 wurde auf Nutzeranweisung abgebrochen. Keine Nachmessung, kein abschließender
Releasepaketbau und kein echter Workflow-Lauf. Entsprechend keine Abnahme einer
Token-/Kosten-/Laufzeitverbesserung oder abschließender Paketgleichheit. Viewer-
Tests bleiben gemäß ADR-0078 ausgenommen. Keine Veröffentlichung oder Installation.

## PLAN-0014: Verbraucherstand vom 26. September 2026

Testartefakte: workspace/temp/2026-09-26-private-helper-tests. Die älteren PLAN-0011-Messungen oben bleiben historische Ergebnisse.

| Bereich | Tatsächlicher Nachweis | Grenze |
| --- | --- | --- |
| Plan/Setup | sol-plan-setup/evidence.md: SOL 6 Medium; Validator/Selector und Setup-Konfiguration vom Workflow-Resolver verwendet | Kein nativer Worker in dieser Einzelprobe |
| Luna-Helper | luna/evidence.md: Resolver, Builder, Selector, Validator, Setup und echter Claude-CLI-Verbrauch | Astra-Korrekturen zu Skillquelle, Toolprotokoll und internem Selector berücksichtigt |
| Reviewer/Repair | sol-repair-consumer/evidence.md: unabhängige SOL-6-Medium-Rollen verwenden Builder-Aufträge; echter changes_requested-Befund führt zur Reparatur; 2 Tests bestanden | Subagenten statt nativer Chats; Zustellung separat |
| Native Workflow/Ask | token-overhead-implementation.md und sol-native/evidence.md trennen ersten vollständigen Lauf, erfolgreiche Ask-Chats und fehlgeschlagenen Subagenten-Caller | Finaler Workflow läuft noch |
| Private GitHub-Helper | github/evidence.md und github-remaining/evidence.md: Hauptpfade sowie pre-cleanup und skill-package erfolgreich | source-only am Live-Familienzustand gescheitert; positiver release-Test setzt Receipt-Metadaten synthetisch und belegt keine reale saubere Releaseherkunft |

candidate-native-final ist eine unveränderliche Kopie des geprüften codex/suite-Builds aus skills/temp/release/codex. Plan und Setup wurden dateiweise gegen installed verglichen: keine Unterschiede in Paketdateien, Python-Caches ausgenommen. Bestehende SOL-Nachweise gelten für diese unveränderten Dateien. Der Repair-Test verwendet candidate-no-archive-check; die spätere Ask-native-delivery-Korrektur betrifft seinen Workflow nicht.

workflow-rollout-baseline-results.json enthält reproduzierte historische Werte, keinen kontrollierten Vorher-Nachher-Vergleich desselben Fixtures. baseline-installed liegt vorbereitet vor; der native Vergleichslauf steht noch aus. Keine gemessene Einsparung des finalen Fixtures und kein vollständiger W-009-Pass behauptet.

Archivierung wird gemäß ADR-0092 im normalen Ablauf ausgeführt, aber nicht nachgeprüft. Seltene harmlose Restfehler rechtfertigen keine zusätzliche Kontrollschicht. Keine reguläre Installation oder Veröffentlichung.

### Finale Gruppen- und Setup-Prüfung

SOL 6 Medium prüfte die native Gruppe W-001/steps-1-4 in PLAN-0003 anhand
der Rohereignisse: native-run-3-audit/evidence.md im Testbereich. Drei Dispatches
geben Builder-stdout unmittelbar an create_thread weiter, ohne vorherige
Promptausgabe. Der vollständige Work Item steht einmal als Kontext im Auftrag.
Worker 1 übergab nach Step 1; Worker 2 setzte Steps 2-4 fort, ohne Step 1 neu
zu implementieren. Fünf Bibliothekstests und Review bestanden, keine CLI-Tests
wurden vorgezogen. CLI-Gruppe und Coordinator-Nachfolger bleiben in Arbeit.

candidate-grouping-criterion enthält zusätzlich die kurze Prüffrage zur
Gruppierung und die gleiche lokale Interpreterwahl für Setup wie für Ask und
Workflow. Paketprüfung gültig. sol-setup-final/evidence.md belegt SOL 6 Medium:
show, serialisiertes set, erneutes show und tatsächliche Verwendung durch
Workflow-Resolver für executor/reviewer. Keine Helper-Ausgabe repariert.
Die gesonderte Gruppierungsprobe ist eine Anwendungsprüfung der Formulierung,
kein neuer nativer Lauf. Keine gemessene Einsparung wird daraus abgeleitet.

controlled-comparison/protocol.md legt den noch ausstehenden gleichen
Drei-Step-Fall für Ausgang und Kandidat fest: SOL 6 Medium in allen Rollen,
75%-Schwellen, frische Coordinatoren und keine künstliche Unterbrechung.

PLAN-0003 ist inzwischen abgeschlossen: beide Gruppen reviewt, acht fokussierte
Tests bestanden, CLI-Beispiel words=4 lines=2, fehlende Datei Exit 1. Plan/index
completed/idle, Validator ohne Fehler/Warnungen. Der Rohereignis-Audit belegt
auch Coordinator-Übernahme: letzter Projektwrite vor create_thread, Nachfolger
sichert eigene ID und sendet Übernahme, Vorgänger ruft Selbstarchivierung einmal
als letzte Aktion auf. Kein Rollover-wait und keine Archivierungs-Nachprüfung.
Auch CLI-Worker/Reviewer konsumierten Builder-Ausgaben direkt; nur die
benötigten akzeptierten Bibliotheksfakten wurden ergänzt.

Die ausführlichen nativen Belege und tatsächlichen Modell-/Effort-Einträge
stehen in native-run-3-audit/evidence.md, manifest.json und metrics.json im
Testbereich. Der kontrollierte Ausgangslauf PLAN-0004 läuft als frischer
Coordinator 01a0dcde-72d2-70f3-a13b-dd08b4452ee5; der Kandidatenlauf folgt.

### Wiederaufnahme und finale Paketzuordnung

Der SOL-Abschlussaudit final-acceptance-audit.md prüfte den ersten nativen
Stopptest anhand der Rohereignisse erneut: Worker 2 erstellt (Record 155),
Stopp vor Ergebniszustellung (161), Stopp weitergeleitet (174), blockiertes
Ergebnis erhalten (186), Worker-Ende beobachtet (190), Ergebnis gesichert (197),
Fortsetzung beauftragt (226), Worker 3 nur für Restarbeit erstellt (263).
resume-step-1.txt und run-1-completed.md bewahren den vorhandenen Funktionsstand.
Keine doppelte Ergebnisannahme und kein paralleler ungeklärter Worker. Das
erfüllt W-009; ein künstlicher Transport-Race-Test ist nicht gefordert.

Dateivergleich: Ask in candidate-grouping-criterion ist bytegleich zum nativ
geprüften candidate-assigned-point. Plan und Workflow unterscheiden sich vom
erfolgreichen candidate-grouped nur durch die geprüfte Gruppierungs-Prüffrage.
Setup hat seinen eigenen finalen SOL-Verbrauchertest. Danach angefordert:
kurze Plan-/Gruppenmeldung und vollständiger Bereich im Titel (ADR-0094).
Diese Ergänzung liegt in candidate-grouping-titles; deren nativer Test erfolgt
im Kandidatenvergleich. Die SOL-Formulierungsprobe steht unter
grouping-title-test.md: zunächst drei statt höchstens zwei Sätze im erweiterten
Szenario, im fokussierten Drei-Step-Szenario ein Satz und korrekte Bereichstitel.
Die erste Probe wird nicht als fehlerfrei gewertet.

### Finaler Kandidat mit Gruppierungsansage und Titeln

candidate-grouping-titles enthält die geprüften Workflow-Runtime-Anweisungen.
final-package-match.json im Testbereich belegt 104/104 Paketdateien bytegleich
zum damaligen Staging; Caches sind ausgeschlossen. check-packages ist gültig.
Reguläre Installationen wurden nicht geändert.

| Geänderter Skill | Finaler SOL-6-Medium-Nachweis |
| --- | --- |
| Workflow | Native PLAN-0005 mit Gruppierung, Ergebnisübernahme, echtem Reviewbefund, Repair und erneutem Review. PLAN-0003 belegt unveränderte Rollover-Verträge. |
| Plan | Selector/Validator und Evidence-Verbraucher in sol-plan-setup/sol-rule-fixes; finaler Gruppen-Selector und Planabschluss in PLAN-0005. Gruppierungserklärung zusätzlich mit SOL angewandt. |
| Ask | Eigener SOL-Adviser 01a0dcbe-6058-72d2-8778-62dfaf766565 mit tatsächlicher Nachricht; parallele Antworten und fehlende Datei separat belegt. Anschließende Titeländerung separat unter ask-title-final.md geprüft. |
| Setup | sol-setup-final: show, serialisiertes set, show und beide tatsächlichen Workflow-Resolver; Paket seit dieser Probe unverändert. |

PLAN-0005 ist abgeschlossen: acht Tests aus Projektroot und Modulverzeichnis,
abschließender Reviewer pass, Validator null Fehler/Warnungen. Eine echte
Testimport-Reparatur war nötig. Sie ist keine Helper-Rückgabekorrektur und bleibt
in Aufwand und Tokenvergleich enthalten. Der Builder-Repairpfad hat damit
zusätzlich einen tatsächlichen nativen Verbraucher.

grouping-title-test.md belegt die native Startmeldung in zwei Sätzen und die
unverändert erzeugten Titel S-WORK-#1-W-001/STEPS-1-3,
S-REVW-#1-W-001/STEPS-1-3 und S-FIXR-#1-W-001/STEPS-1-3. Der native Testauftrag
hat weder Gruppe noch Titel vorgegeben. Diese Abnahme betrifft Workflow-Titel;
die anschließend freigegebene Ask-Titeländerung W-015 ist separat geprüft.

### Ergänzung: Ask-Titel unter ADR-0095

candidate-ask-titles stimmt mit allen 104 Paketdateien des danach erzeugten
Stagings überein. ask-final-package-match.json im Testbereich weist gegenüber
candidate-grouping-titles genau zwei Änderungen aus: Ask README.md und
references/native.md. Helpercode und alle anderen Skill-Dateien sind unverändert.
ask-title-final.md belegt den echten SOL-Medium-Chattitel und die Rückzustellung.
Paketprüfung und 18 Ask-Tests bestehen.

### Abschluss nach Astra-Medium-Review

candidate-astra-final enthält zusätzlich nur Workflow README.md und
references/operations-dispatch.md als geänderte Paketdateien. Alle 104 Dateien
sind bytegleich zum finalen Staging; astra-final-package-match.json sichert dies.
astra-final-review.md belegt beide behobenen Findings und Astras Nachreview
ohne materiellen Restbefund. SOL 6 Medium führt das echte Dispatch-Beispiel mit
vollständiger, tatsächlich gekürzter und fehlgeschlagener Toolausgabe aus:
Nur die vollständige Ausgabe erreicht den abgefangenen create_thread-Aufruf.
Diese Prüfung ergänzt die früheren nativen E2E-Belege. Paketprüfung besteht.
