# Aktuelle Vorgabe

ADR-0092 ersetzt die unten historisch dokumentierte Bestätigungspflicht. Archivierung bleibt eine einmalige Aktion; keine Bestätigungsnachricht, Nachprüfung oder externe Wiederholung. Fehlende Bestätigung ist kein Abnahmefehler.

## Historischer Prüfstand vor Nutzerkorrektur

# Archivierungsstellen: Prüfung nach Nutzerkorrektur

| Fall | Route | Voraussetzung und Grenze |
| --- | --- | --- |
| Coordinator-Rollover | Nachfolger meldet Übernahme; Vorgänger archiviert sich und bestätigt | Alle Vorgänger-Projektwrites vor create_thread; Absender muss erzeugter Nachfolger sein. Reale neue Route noch zu testen. |
| Worker/Reviewer/Repair abgeschlossen | Direkt bei bereits belegtem Turn-Ende; sonst eine Selbstarchivierungsaufforderung | Originalresultat zuerst sichern. Keine zusätzliche Warteabfrage nur zur Archivierung. Bestätigung erforderlich. |
| Worker/Reviewer/Repair-Rollover | Nachfolger meldet Übernahme an Coordinator; danach obige Archivierungsregel | Tatsächlicher Absender muss gesicherter Nachfolger sein. Keine Übernahme-Pollschleife. |
| Stopp oder Nutzerentscheidung | Offen halten bis tatsächlicher Zustand geklärt beziehungsweise Entscheidung beantwortet | Archivierung ist kein Abbruchwerkzeug. |
| Ask erfolgreich | Offen für Follow-ups; Selbstarchivierung bei explizitem Ja im Adviserchat | Bestehende Rechte bleiben; autorisierte Testbereinigung darf beendete Adviser direkt archivieren. |
| Ask Fehler/autorisierte Bereinigung | Bestehende direkte Route nach gesichertem Fehler/Ergebnis und bekanntem Ende | Kein neuer automatischer Archivierungsgrund. Fehlende Rechte werden nicht umgangen. |
| Abschließender Coordinator | Sichtbar lassen | Kein automatisches Selbstarchivieren bei Planabschluss. |

Owner: Workflow operations.md, operations-rollover.md und der durch build_dispatch_prompt.py
gebaute Rollenauftrag. Ask: native.md und native-delivery.md. Die übrigen kanonischen
Suite-Skills besitzen keine eigene native Chat-Archivierungsroute. Nicht mehr exportierte
task_lifecycle-Kopien sind kein Runtime-Owner. Abnahme bleibt offen, solange eine
vorgeschriebene Archivierung nicht mit passender ID und archived:true bestätigt ist.

## Beobachtete Hostgrenze: Selbstarchivierung

SOL-6-Medium-Probe `01a0dca2-1e73-7cc2-926f-391705ea1c15`: Der eigene Archivierungsaufruf führte zur Ablage unter archived_sessions und zum Abbruch des laufenden Turns. Das äußere Toolresultat lautet `aborted by user after 0.1s`; anschließend folgt `turn_aborted` mit reason `interrupted`. Eine nachgelagerte Bestätigung kam nicht an. Quelle: lokaler archivierter Rollout derselben ID vom 2026-09-26T09-33-27.

Die oben verlangte Bestätigung nach Selbstarchivierung ist damit nicht abgenommen. Aktuelle Runtime-Anweisungen dazu sind vorläufig und benötigen eine Korrektur samt realem Nachtest. Keine erfolgreiche Abschlussbestätigung vor dem Archivierungsaufruf senden. Die Variante mit Archivierung und Versand innerhalb derselben Code-Zelle ist ungetestet.

Ein anschließender einmaliger externer `set_thread_archived`-Aufruf mit derselben ID und `archived:true` lieferte erfolgreich genau diese ID und `archived:true`. Der bereits archivierte Probechat blieb archiviert. Damit ist eine idempotente externe Abschlussbestätigung für diesen Fall belegt, ohne wait. Ein realer Nachfolgerlauf mit dieser Bestätigung und der Selbstarchivierungsnachricht ist weiterhin offen.
