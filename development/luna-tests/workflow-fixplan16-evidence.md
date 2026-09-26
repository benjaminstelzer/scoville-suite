# PLAN-0016: gezielte Verhaltensprüfung

Stand: 2026-09-26. Ausgangsrevision: `34a01ab1aa80a80933f4dd0bd688f61c46f936f3`.
Kandidat aus dem kanonischen Suite-Builder, keine reguläre Installation.
Testartefakte: `temp/2026-09-26-workflow-fixplan16/` relativ zum AI-Workspace.

## Prüfstatus und Zeilenenden

Modellanforderung: gpt-6-sol, medium. Native Subagent-ID:
`/root/sol16_checks`. Modelltelemetrie über diese Anforderung hinaus nicht verfügbar.

SOL führte die zwei vorhandenen Prüfungen separat aus: zuerst Exit 7 und 0,
nach dem beauftragten Edit jeweils 0. Der erste Fehler wurde ausdrücklich
als Fehler berichtet. Ein unabhängiger Bytevergleich bestätigt ausschließlich
`retries=2` zu `retries=3`; alle gemischten Zeilenenden und übrigen Bytes blieben
erhalten. Checkskripte und lokale Git-Konfiguration blieben unverändert.
Das Fixture nutzt `core.autocrlf=true`. Keine manuelle Helper-Reparatur.

## Struktur und vorhandene Tests

- 17 Workflow-Tests bestanden, einschließlich tatsächlicher Selector-/Builder-
  Übergabe, Rolleninputs und frischer Kontextmessung.
- README-Projektionen unverändert und gültig.
- Gebaute Laufzeitdateien entsprechen dem kanonischen Payload: Code 7, Plan 10,
  Workflow 16 Dateien. Distributions-README-Dateien sind kein Testgegenstand.
- Zwei zunächst unvollständige Build-Prüfaufrufe scheiterten am fehlenden
  `--output`; sie zählen nicht als bestandene Prüfungen. Danach wurde der
  tatsächlich konsumierte Laufzeit-Payload direkt verglichen.

## Koordinatorprobe

SOL 6 Medium (`/root/sol16_coordinator_probe`) erhielt einen widersprüchlichen
Cursor und ein Worker-Ergebnis mit fehlgeschlagenem Diff-Check. Er korrigierte
den Executor-Zähler auf 3, ersetzte den veralteten Startzustand durch erledigt
aber unakzeptiert, setzte das aktive Kind auf keines und wählte den bestehenden
Reviewer als nächsten Schritt. `app.txt` blieb unverändert. Er behauptete keine
Zustellung oder Abnahme. Das Fixture hat bewusst simulierte Handles; diese Probe
belegt nur Rollenentscheidung und Cursorpflege, keine native Koordination.

## Native Prüfung und Korrektur der Ausgangsanalyse

Korrektur der Ausgangsanalyse: Die Roh-Rollouts der DIVI-Manager #6/#7 zeigen
bereits Build und create_thread in derselben functions.exec-Zelle mit direkter
Weitergabe und ausschließlich ausgegebener Erstellung. read_thread stellt die
verschachtelten Tool-Ausgaben separat dar; das belegt keine zusätzliche Ausgabe
an das aufrufende Modell. Der behauptete Doppel-Ausgabefehler wird zurückgezogen.
Die vorübergehend verstärkte Anweisung wurde wieder auf den vorherigen Text
reduziert. Der native Test bestätigt den vorhandenen direkten Übergabepfad.

Der native Erstauftrag und die Fortsetzung sind geprüft.
Separate native Test-Chats und interne Nachrichten sind jetzt ausdrücklich genehmigt.
Manager: 01a0de0d-1506-7b71-b8c1-f7d01f1cad8f, angefordert gpt-6-sol / medium.
Fixture: temp/2026-09-26-workflow-fixplan16/native-run im gespeicherten Projekt
AI Projects. Der Test verwendet ausdrücklich nur diesen Unterordner als Arbeits-
und Planwurzel. Worker-Schwelle 1 Prozent erzwingt günstig einen echten
telemetriebasierten Übergang; die produktive 75-Prozent-Grenze wird hier nicht
neu gemessen. Kein Produktionsprojekt oder regulär installiertes Skill verändert.
Keine vergleichende Tokenersparnis behauptet.


## Beobachtete native Ergebnisse

Alle sechs Chats wurden mit gpt-6-sol / medium erstellt. Der native Versuch
verwendete echte Erstellung, Nachrichten, Rollenprüfung und Fortsetzung.

| Rolle | Task-ID |
| --- | --- |
| Manager | 01a0de0d-1506-7b71-b8c1-f7d01f1cad8f |
| Erster Worker | 01a0de0e-02a3-7783-a07d-ecdcca26c59d |
| Erster Reviewer | 01a0de0f-ee5e-74b1-952c-7a76deb69613 |
| Handoff-Worker | 01a0de12-1134-7ea0-9bd5-297256fa42ad |
| Nachfolger | 01a0de13-0807-79b0-abae-3d5801f22bac |
| Zweiter Reviewer | 01a0de14-5650-7733-a06f-69f4ab9c8666 |

- Erster Worker: Ausgangsprüfung Exit 7, danach settings/mode/report erfolgreich.
  Ein unabhängiger Bytevergleich bestätigt den begrenzten Edit und einmalige
  Marker step-1 und step-2 in der richtigen Reihenfolge. Reviewer pass.
- Fixture-Fehler: coordinator_percent=100 war ungültig. Worker blockierte korrekt.
  Manager korrigierte nur die Testkonfiguration auf 99 und setzte denselben
  Worker fort. Der Folge-Checkpoint lieferte unavailable wegen veralteter
  Telemetrie und damit vertragsgemäß continue. Keine erfundene Übergabe.
- Zweiter Fall: kontrollierte Übergabe nach Schritt 1 vorgesehen. Zusätzlich
  lag tatsächlich fresh-Telemetrie vor: 35.790 / 258.400 bei Testschwelle 1 Prozent,
  action=context_handoff. Der Auslöser war durch Fixture und niedrige Schwelle
  vorgegeben; kein unabhängiger Nachweis der produktiven 75-Prozent-Grenze.
- Der native Nachfolger sendete seine Übernahme und schrieb nur Schritt 2.
  Unabhängige Endprüfung: continuation.txt exakt first\nsecond\n. Reviewer pass.
- Der Manager bearbeitete nur Koordinations-/Planunterlagen und die ungültige
  Testkonfiguration, keine Produktdateien. Alle Schritte blieben seriell.
- Abschlusscursor zunächst mit überholtem role=executor: Operations-Regel um
  den klaren fertigen Zustand ergänzt. Gezielte SOL-Nachprüfung korrigierte nur
  den Cursor auf fertig, Rolle/Kind/Next action keine. Keine erneute Ausführung.
- Beide Fixture-Pläne abgeschlossen und Index idle; Profilvalidator ohne Fehler.

## Übergaben und Kosten

Roh-Rollout response_item/custom_tool_call und zurückgegebene Zellausgabe wurden
getrennt vom erweiterten read_thread-Protokoll ausgewertet. Alle fünf Dispatches
übergaben built.output unverändert in derselben Zelle. Zusätzliche ausgegebene
Auftragskopien: 0. Auftragslängen in Reihenfolge: 8.041, 7.795, 7.991, 8.387 und
6.862 Zeichen. Der Nachfolger erhält den vollständigen Work Item-Kontext und
kurzen Hand-off statt Vorgängerhistorie. Zusatzkontext enthält Projektfakten und
Autorisierung; keine erneute allgemeine Checkpoint-/Zustellanleitung.

Manager-Regeln wurden nicht mehrfach geladen. Identische Plan-/Index-Leseaufrufe
traten zur Abschlussbearbeitung auf; die zwei identischen Selector-Befehle bezogen
sich auf verschiedene aktive Pläne. Ein gezielter read_thread-Aufruf betraf die
Wiederaufnahme nach dem Konfigurationsfehler, keine Vorgängerhistorie bei Rollover.

Zeit vom context_handoff-Aufruf bis zur Takeover-Nachricht: 33,4 Sekunden.
Gesamter erster und zweiter Lauf bis zum Bericht: ungefähr 9 Minuten.

Summe einmaliger response_id/token_usage_record über die sechs Chats bis zum
Abschlussbericht, vor der gezielten Cursor-Nachprüfung: 3.857.495 Input-Tokens,
inklusive 3.572.992 gecachter Input-Tokens, sowie 22.005 Output-Tokens.
Ungecachter Input: 284.503. Das sind kumulierte Aufrufwerte, keine Kontextgröße,
keine Eurokosten und kein kontrollierter Vorher-Nachher-Vergleich. Die Zahlen
enthalten Testaufbau, Fixture-Recovery und zwei Reviews. Rohzählung liegt in
native-metrics.json im Testbereich. Subagentenproben und Cursor-Nachprüfung sind
nicht in dieser abgegrenzten Summe enthalten.

## Grenzen

Die produktive Kontextschwelle wurde nicht erneut getestet. Ein Modelllauf
beweist keine allgemeine Befolgungsgarantie oder Kostenverbesserung. Eine echte
Manager-Rollover-Kette ist nicht Teil dieses Versuchs; Cursor-Wiederaufnahme
wurde separat geprüft. Archivierung wurde nicht nachgeprüft. Kein Release oder
reguläre Installation wurde durchgeführt.
