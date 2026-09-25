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
Modell gpt-6-sol/medium, Workspace Z:/Projekts/AI/temp/2026-09-25-workflow-live.
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
