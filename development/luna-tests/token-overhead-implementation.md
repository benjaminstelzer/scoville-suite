# PLAN-0014: Ausgangsstand und native Probe

## Ausgangsstand

Der unkommittierte Stand vor dieser Umsetzung ist unter
`temp/2026-09-26-token-overhead-implementation/baseline/` im Workspace gesichert.
Die folgenden Pfade liegen unter
`members/scoville-workflow-for-codex/scoville-workflow-for-codex/`.

| Datei | Bereits adressiert | Noch offen |
| --- | --- | --- |
| SKILL.md | P6: vorhandene eigene Task-ID verwenden; direkte Rollenzähler | P8: Legacy-Guard-Regel; kompakter Laufdatensatz |
| references/operations.md | P1: Turn-Ende; P2/P4: kurze Meldungen; P7: direkte Archivierung | P1/P3/P7: Statusabfrage plus read_thread und Parser nach jeder Nachricht |
| references/operations-dispatch.md | P3: Prompt nur einmal bauen; P7: direkte Erstellung | P5: Abnahmekriterien fehlen im Auftrag; P8: umfangreiche Builder-Signatur |
| references/operations-rollover.md | P6: kurze Übergabe ohne gesamten Vorgängerchat | P1: Abfrage für Ende bleibt; tatsächliche Nachfolger-ID erst nach create_thread bekannt |
| scripts/build_dispatch_prompt.py | P4: kurze Meldungen; P5: nur Step; P1: direkte Nachricht | P5: Outcome und Acceptance fehlen; P7: Parserimport; P8: sieben Pflichtargumente |

Begleitende Änderungen vorgefunden: Workflow-Test und drei README-Fragmente
bilden Teile dieses Entwurfs ab; Ask-Konfigurationsreferenz enthält eine
Aufrufklarstellung. PLAN-0012 W-017 und ADR-0083 halten den Release-Stopp fest.
P8 bleibt suiteweit offen; P9 ist nur teilweise wiederhergestellt.
Keine laufende DIVI-Session wurde verändert.

## Reproduzierbare Messung

```text
py -3 development/luna-tests/analyze_workflow_rollouts.py --manifest development/luna-tests/workflow-rollout-baseline.json --output development/luna-tests/workflow-rollout-baseline-results.json
```

Das Manifest enthält vollständige IDs und konkrete Rollout-Pfade. ALT1/ALT2
schließen ihren Launcher aus, NEU schließt seinen initialen Coordinator ein.
Input stammt aus token_usage_record, je response_id einmal; keine Summierung
kumulativer Tokenzähler. Aufrufe stammen nur aus response_item, nicht zusätzlich
aus den gespiegelten item_completed-Ereignissen.

| Messwert | ALT1 | ALT2 | NEU |
| --- | ---: | ---: | ---: |
| Coordinator-Tasks | 10 | 3 | 2 |
| Executor-Tasks | 9 | 3 | 2 |
| Coordinator-Modellaufrufe | 983 | 256 | 152 |
| Coordinator-Input | 122906902 | 30391889 | 17530567 |
| Coordinator-Kommentare / Finals | 103 / 35 | 36 / 13 | 38 / 5 |
| wait_threads + Code-wait | 278 | 54 | 33 |

Die Kernwerte stimmen mit Abschnitt 2 der historischen Analyse überein.
ALT1 hat zusätzlich acht wait_agent-Aufrufe: Die historische Summe 286 enthält
diese trotz engerer Spaltenbezeichnung. Große Ausgaben, Fehlerausgaben,
Warteabstände und doppelte Lesezugriffe weichen bei expliziter neuer Zählregel
teilweise ab. Diese Nebenwerte sind noch keine vollständige Reproduktion der
historischen Tabelle; insbesondere ist eine Dispatch-Dauer nicht aus einer
beliebigen Zeitspanne vor create_thread abzuleiten.

## Native Zustellprobe am 2026-09-26

- Coordinator: `01a0dc63-95fa-71e2-ad78-1ef36363546d`.
- Worker: `01a0dc63-cdb4-73d3-a14a-bd716aabe996`.
- Erster Coordinator-Turn `01a0dc63-96ff-7702-a672-7009b4516f3a`
  endete bei Unix-Zeit 1790403930 mit IDLE und Worker-ID.
- Worker-Nachricht eröffnete Turn `01a0dc64-0143-7e70-8d25-dddfd1df6131`
  bei 1790403936, also nach dem Turn-Ende.
- Der Coordinator verwendete keine Warte- oder Leseabfrage. Seine native
  Abschlussnachricht erreichte den aufrufenden Chat.

Belegt: Native Nachricht weckt in diesem Desktop-Host einen idle Chat.
Noch nicht belegt: vollständige SCOVILLE_RESULT_V1-Annahme, sichere Wiederaufnahme,
Archivierung, Rollover und Verhalten anderer Hosts. Die Probe verwendet einen
festen Marker; sie ist kein vollständiger Workflow-Abnahmetest.

## Testharness-Grenze

run_codex_cli_case.py fordert hypothetische Antworten ohne Tools an und begrenzt
Modelle auf gpt-5.6-luna/terra. Dieser Runner allein erfüllt die geplanten realen
gpt-6-luna-Helpertests nicht. Der temporäre helper_luna_tests.py-Entwurf führt
Helper mit modellgewählten Argumenten aus, ersetzt Provider aber durch Fixtures.
Reale Provider- und Rückgabeverwendung darf daraus nicht abgeleitet werden.

## Vollständiges Rollenresultat

Die zweite native Probe verwendet Worker `01a0dc66-3327-76e3-a0b7-dccda4da351a`.
Der Coordinator meldete nach beendeter Idle-Phase direkte erfolgreiche Prüfung
von SCOVILLE_RESULT_V1 mit role=executor und status=completed einschließlich
Review-Feldern. Er verwendete weder Parser noch read_thread oder wait_threads.
Die Meldung PROBE_RESULT_V1 wurde im aufrufenden Chat empfangen.

## Erweiterte Helper-Abnahme und Build

Nutzerpriorität: Suite fertigstellen; übrige private Helper parallel prüfen.
Reine Helpertests dürfen Luna 6 Medium nutzen. Geänderte Skills behalten SOL 6 Medium.
Inventar: private-helper-inventory.md. GitHub-Testagent: /root/github_helper_sol
mit explizit gpt-6-sol medium; Evidenz im Workspace unter
`temp/2026-09-26-private-helper-tests/github/evidence.md`. Drei Hauptpfade bestanden
mit realen Verbrauchern; positive Release- und Familienprüfung sowie weitere
optionale Audit-Modi bleiben offen.

Codex-Kandidat: `skills/temp/release/codex`, Manifest SHA256
`b5652ff7d2b900c20569ceedab951bd409866ee4e502c284ef796a97c4cce4f8`.
Isolierte Installation: `temp/2026-09-26-private-helper-tests/installed`.
31 Suite-Entwicklungstests bestanden. Shared-Tests fanden zwei veraltete
Lifecycle-Exportannahmen nach dessen autorisierter Entfernung. Die Tests prüfen
jetzt den verbleibenden gemeinsamen Konfigurationshelper isoliert und die
Abwesenheit des Lifecycle-Exports; beide betroffenen Tests bestanden danach.
Setup erklärt automatische JSON-Serialisierung; seine zwei bestehenden Tests bestanden.

## Modelltests: Zwischenstand

- /root/luna_helpers: gpt-6-luna medium; echte Claude-Prepare-Rückgabe unverändert
  an Provider weitergegeben. Native Modellstarts und weitere Builder-Optionen offen.
- /root/sol_plan_setup: gpt-6-sol medium; Plan/Setup mit tatsächlichem Builder und
  Modellresolver als Verbraucher bestanden. Beide Berichte liegen unter
  `temp/2026-09-26-private-helper-tests/<luna|sol-plan-setup>/evidence.md`.
- /root/sol_workflow_ask: gpt-6-sol medium. Native Adviser-ID
  `01a0dc7f-8aeb-7e72-bfc7-e097ad34baf0`; Antwort an Subagent vom Host abgewiesen:
  direct app-server input is not allowed for multi-agent v2 sub-agents.
  native.md verhindert jetzt den Start aus diesem ungeeigneten Caller.
- Wiederholung aus Root: `01a0dc82-6a34-76f0-a011-418b8610ca95`, SOL6 medium,
  Referenz PLAN0014-SOL-ASK-ROOT-A. Helferrückgabe direkt für model/thinking verwendet;
  Nachricht mit richtigem Sender und Referenz empfangen. Der Root hatte zuvor
  irrtümlich ein nicht dokumentiertes CLI-Argument resolve eingesetzt: Usage-Fehler,
  kein Helperdefekt und kein fehlerfreier Erstaufruf in diesem Root-Versuch.
- Zwei parallele Ask-Chats: `01a0dc84-3a5f-7e92-90ba-b9853b8d4473` und
  `01a0dc84-3dd0-7532-9ff1-4a542cf1619c`; zweiter Fall fordert bewusst eine fehlende
  Evidenzdatei an. Beide Antworten müssen einzeln gesichert werden.
- Native SOL-Workflow-Prüfung gestartet: `01a0dc83-ccb4-7d62-b15f-71f8ddc72ed9`.
  Vom Nutzer gespeichertes Fixture-Projekt: `projects/temp/2026-09-26-private-helper-tests/workflow-e2e`,
  Projekt-ID `fa0d6440-62b3-466d-8e44-722770ff9d71`. Kein E2E-Pass vor Ergebnis.

Alle 55 Shared-Tests bestanden nach der fokussierten Korrektur; 21 Ask-Tests
nach Ergänzung der Callergrenze ebenfalls bestanden.

Parallel-Ask-Ergebnis: Beide Originalnachrichten sind direkt im Hauptchat angekommen.
ROUND2-A vom bekannten Sender 01a0dc84-3a5f-7e92-90ba-b9853b8d4473 bestätigt
automatische JSON-Erzeugung und eigenen Adviser-Chat. ROUND2-B von
01a0dc84-3dd0-7532-9ff1-4a542cf1619c meldet die tatsächlich fehlende Datei und
keine erfundenen Befunde. Beide scope-Werte stimmen; keine Ersatzchats oder
Antwortreparaturen. Die Antworten kamen A dann B, also kein Beleg umgekehrter Reihenfolge.

Der native SOL-Workflow meldet echte Worker-Kontextübergabe nach implementierter
Zählfunktion, vor CLI-Einstieg. Ein gezielter Stopptest wurde am 2026-09-26 an
den bekannten Coordinator gesendet; Stillstand und Wiederaufnahme bleiben bis
zur beobachteten Rückgabe offen.

Korrektur der vorläufigen Doppel-Ausgabe-Vermutung: read_thread zeigt auch
verschachtelte Toolereignisse. Die echten response_item-Aufrufe von functions.exec
für Worker 1/2/3 und Reviewer 1 enthalten built=await exec_command,
create_thread(prompt:built.output) und ausschließlich text(created). Damit
wurde kein vollständiger Builderprompt ans Coordinator-Modell ausgegeben.
Der frühere Verdacht aufgrund interner Command-Ausgaben ist verworfen; keine
Transportänderung ist dadurch begründet.

## Rollover-Befund und Korrektur

Coordinator 1 akzeptierte Step1 nach Review und frischer Rollover-Telemetrie.
Nachfolger 01a0dc8c-e50f-7e83-83f1-cfbc8eff85c2 verwendete jedoch timeoutMs:0
vor Laden der Rollover-Referenz, sah den Vorgänger noch aktiv und beendete
seinen Turn ohne Übernahme/Archivierung. Dies ist ein echter negativer E2E-Befund.
operations-rollover.md verlangt jetzt explizit einmal timeoutMs:60000 und das
Laden der Referenz vor der Prüfung, auch im erzeugten Nachfolgerauftrag.
Die Korrektur wurde gebaut und an einer inaktiven Grenze isoliert übernommen;
der identische Nachfolger wurde gezielt wiederaufgenommen. Keine Neuerstellung.
Automatischer Erfolg bleibt bis zum nächsten tatsächlichen Rollover offen.

operations.md enthält nun die vollständigen knappen Resultatgrenzen für den
Coordinator. Im ersten Lauf musste dieser sie per Quellensuche nachladen, weil
die alte Referenz nur auf nicht mitgelieferte Größenlimits verwies. Diese
Dokumentationskorrektur ist noch nicht in den laufenden Test eingewechselt.

## Geprüfte Übergaben und Testchat-Aufräumen

Luna-Snapshot: `temp/2026-09-26-private-helper-tests/luna/native-handoff-audit.md`.
Worker1-Auftrag 5846 Zeichen; Worker2-Auftrag 6204 Zeichen. Planprojektion in
beiden: Assigned point 328 Zeichen und Outcome/Acceptance 327 Zeichen. Nur
Worker2 ergänzt die notwendige Original-Kontextübergabe. Kein ganzer Plan/Chat.
Rest ist der gemeinsame Rollen- und Ergebnisvertrag. Beide Worker wurden nach
beendetem Turn und übernommener Fortsetzung mit exakter ID/archived:true archiviert.

Nach gesicherter Evidenz sind die vier beendeten Ask-Testchats 01a0dc7f-8aeb-7e72-bfc7-e097ad34baf0,
01a0dc82-6a34-76f0-a011-418b8610ca95, 01a0dc84-3a5f-7e92-90ba-b9853b8d4473 und
01a0dc84-3dd0-7532-9ff1-4a542cf1619c archiviert; jeweilige native Antwort bestätigt archived:true.
Auch die drei abgeschlossenen frühen Zustellprobe-Chats 01a0dc63-95fa-71e2-ad78-1ef36363546d,
01a0dc63-cdb4-73d3-a14a-bd716aabe996 und 01a0dc66-3327-76e3-a0b7-dccda4da351a
wurden nach gezielter Endzustandsprüfung mit matching ID/archived:true archiviert.
Der noch laufende vollständige Workflowtest verwaltet seine Rollen selbst.

## Fortsetzung nach ADR-0092

Die kanonischen Workflow- und Ask-Anweisungen verlangen keine Archivierungsbestätigung oder Nachprüfung mehr. Auch native-delivery.md ist angepasst. Builder-Ergebnisbeispiele zeigen nur Pflichtfelder; finding wird ausschließlich für tatsächliche offene Fehler ergänzt. Anlass war das echte worker-5-result mit finding=none.

Workflow: 16 Tests bestanden. Ask: 21 Tests bestanden. Kandidat mit suite/codex-Layout gebaut und check-packages gültig. Ein erster Refresh mit falschem standalone-Layout wurde vom Builder abgewiesen; anschließend wurde das vorhandene suite-Layout verwendet. Keine Installation oder Veröffentlichung. Die unveränderliche Testkopie candidate-no-archive-check enthält den Workflow für die laufende SOL-6-Medium-Repair-Verbraucherprobe, aber noch nicht die spätere native-delivery.md-Korrektur. Reale neue Workflow-Rollover-Abnahme bleibt offen.

## Finale native Ask-Zustellung

SOL-6-Medium-Adviser 01a0dcbe-6058-72d2-8778-62dfaf766565 antwortete als eigener nativer Chat auf PLAN0014-FINAL-ASK-SOL an den tatsächlichen Hauptchat. Settings kamen unverändert aus ask.py des Pakets candidate-assigned-point. Der Adviser bestätigte read-only die Klartext-Evidence-Kompatibilität mit dem Validator und fand einen fehlenden Artefaktverweis im Dokumentationsbeispiel. Das Beispiel wurde um tests/results.txt ergänzt; keine Parseränderung. Die unabhängige Antwort benannte ihre Grenze ohne ausgeführte Schreibtests.

## Native Run 2 abgeschlossen

Finaler Coordinator: 01a0dcbe-fbd7-77d1-9b8c-e2254ade849d. Meldung und Fixture belegen abgeschlossenen PLAN-0002, Idle-Index und vier bestandene fokussierte Tests. Der Lauf nutzte candidate-native-final, also die Nachrichtenarchivierung, aber noch nicht die späteren Scope-/Kontextkorrekturen. Keine Archivierungs-Nachprüfung vorgenommen.

Offline-Auswertung: temp/2026-09-26-private-helper-tests/native-run-2-audit/manifest.json und metrics.json. Drei Coordinatoren, fünf Worker, zwei Reviewer. Coordinatoren: 109 Modellaufrufe, 6658725 Inputtokens, null waits, null vom Analyseskript erkannte Helper-Usage-Fehler. Coordinator 1 wurde ab dem genauen Run-2-Startzeitpunkt ausgewertet, seine frühere Arbeit ausgeschlossen. Worker-Prompts: 6461/8009/8052/6065/6073 Zeichen. Diese Werte enthalten die dokumentierte Teststeuerung von 1% auf 75% Worker-Kontext; sie sind kein kontrollierter Vergleich und keine repräsentative Standardkonfiguration.

Die Reviewer-Beanstandung fehlender Tests in Step 1 war eine Scope-Abweichung; der Coordinator ordnete sie dem vorgesehenen Step 2 zu. Die spätere SOL-Einzelprobe unter sol-rule-fixes prüft die genehmigten Scope- und Formatkorrekturen. Ihre Grenzen (zusätzlicher Index-Read und manuelle Auslassung einer Finding-Formatphrase im Reviewerprompt) sind keine vollständig unveränderte Übergabe-Abnahme.

Aktuell genehmigt und in Quellen: vollständiger Work Item als Kontext mit eindeutig benanntem Step; Coordinator wählt relevante Goals/Non-goals und weitere Vorgaben über supplemental-context. Neu diskutiert, noch nicht genehmigt: ein Worker für den ganzen Work Item. Bis zur Entscheidung keine weiteren Dispatch-Vergleichsläufe auf einer womöglich überholten Einteilung.
