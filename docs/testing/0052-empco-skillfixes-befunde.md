# Aktuelle Befunde zur Skillfix-Beobachtung

## Beobachteter Umfang

Ab Wiederaufnahmeturn `01a1205e-4bdb-74a1-b1a1-905470d5e3a6`: Runner, Manager3/4, Executor14, Reviewer14, Ganzcode-Reviewer15 und acht ergänzende Reviewer. Geprüft wurden relevante Aufrufe, Rückgaben, geladene Regeln, Auftragsgrenzen, Ergebnisse und Planänderungen bis zu den in state.json genannten Itemgrenzen. Kein eigener Produkttest oder semantischer Produktreview. Laufende Teilreviews sind noch nicht abgenommen.

Manager3 `01a12062-a6f3-7f82-88be-76912ac78b1b` schloss nur W370/Schritt3 nach der unabhängigen Harnessreview ab. Manager4 `01a12078-6d15-71a3-be47-debffa817cc7` übernahm Schritt4. Neue Produktfindings wurden als offene W371–W374 erfasst; ergänzende frische Reviews prüfen die fehlende Abdeckung. Keine Gesamtfreigabe aus dem begrenzten ersten Codebericht.

## Bestätigte neue Anwendungsfehler

Scoville Ask mit angefordertem Sol 6.1/high, Referenz `PLAN-0052-W001-FIRST`, hat die neuen Befunde gegen die installierten Regeln und betroffenen Helper geprüft. Tatsächliche Modelltelemetrie wurde nicht offengelegt. Kein Helperdefekt nachgewiesen; die Schutzprüfungen verwarfen die falschen Aufrufe korrekt. Die wiederholten Anwendungsfehler bleiben trotzdem Verbesserungsbedarf.

| Fehler und Quelle | Wirkung und Recovery | Zuständiger Skill und kleinster Fixvorschlag |
| --- | --- | --- |
| Zweimal Code/SKILL.md direkt als Python bei Teil3: Engineering `01a12095-6e1e-7db3-ac67-52034349debb`, exec-5fc9061a; Admin `01a12098-388a-7150-8c63-3c839e0fd77e`, exec-bd758ce5. | Identischer SyntaxError in Prosezeile10. Beide lasen danach korrekt neu ab Teil1 bis last. Keine Projektänderung aus dem Fehlaufruf. | Shared Writing/Workflow-Reader: vorhandene Fortsetzungsregel direkt neben das erzeugte, als Readerkommando bezeichnete Kommando setzen: gesamtes Kommando kopieren, nur --part ändern. Entfernte Wiederholung dafür kürzen. Wirksamkeit dieses Vorschlags noch ungetestet. |
| Successor mit verbotenem --project-root: Runner, exec-fcb6f7a4. | Helper Exit2 vor Spawn; nach Entfernen des Arguments genau ein Manager4 gestartet. | Workflow: CLI-Hilfe zu --project-root auf initial start only präzisieren; richtiges Successor-Beispiel bereits vorhanden. |
| Reviewer mit coordinator-only --boundary: Ganzcode-Reviewer `01a1207d-d317-7e43-a468-5857deb65d7e`, exec-d87e64e5. | Exit2; ohne Parameter continue. Manager-Herkunft des Beispiels durch BLOCKED-Meldung berichtet, natives vollständiges Spawnargument im Retrieval nicht separat sichtbar. | Workflow: --boundary-Hilfe mit coordinator only beginnen; erzeugte Reviewerkommandos vollständig rollenrichtig liefern. |
| Mehrfach gequotetes python -c mit eingebettetem exec: derselbe Reviewer, exec-e0de6f1b. | SyntaxError; Inventar später erfolgreich ermittelt. Welche Quotierungsschicht den Text änderte, ist nicht eindeutig belegt. | Shared Writing/Code: einfache vorhandene Inventar-/Zählbefehle statt unnötiger verschachtelter Python-Schleifen verwenden; kein pauschales neues Verbot. |
| Wildcard als wörtlicher rg-Pfad unter --run: derselbe Reviewer, exec-2c6afe23; zusätzlich Admin exec-846efd04. | Exit2 mit Teiltreffern und Pfadfehler, kein erfolgreicher Gesamtlauf. Danach gezielte Quellen gelesen. | Shared Writing: vorhandenes Verzeichnis plus -g-Muster verwenden; bestehende Regel deckt den Fall ab. Kompaktes korrektes Beispiel statt weiterer Regel. |
| Nicht vorhandene reviewer.md bzw. reviewer* gesucht: Admin exec-740127a0, Writer exec-6d5dc8d9, PHP exec-25472107. | Fehlende Referenz bzw. wörtlicher Globpfad. Installiertes Inventar enthält keine reviewer.md; kein kanonischer Verweis darauf nachgewiesen. | Workflow-Aufträge: vorhandene Referenzen und Readerkommandos direkt benennen; unbekannte Namen aus dem tatsächlichen Inventar ermitteln. Kein Installationsdefekt behaupten. |

## Belegte Fixwirkung und offene Grenzen

Executor14 `01a1206a-4a99-7722-81f6-db162ac97756` beschränkte die Korrektur auf zwei Promise-Verbindungen. Ein fokussierter Erfolgslauf und zwei erwartete injizierte Fehlerläufe belegten Cleanup; frühere Matrizen wurden nicht wiederholt. Reviewer14 `01a12073-6c0d-77e3-b746-7941c877fe0a` prüfte read-only genau die Korrektur und verbleibende Schritt3-Grenze und gab pass. Erwartetes Exit1 wurde nicht nachträglich als Erfolg umgedeutet.

Manager4s Kontextabruf meldete `output_complete=false`, obwohl der Kindprozess Exit0 lieferte. Umsetzung und Dispatch blieben bis zur vollständigen Quellenübernahme gesperrt: korrekte Ausgabesperre, kein zusätzlicher Helperbefund. Zuvor gemeldete Reader-Serialisierung und Positionscapture sind mangels vollständiger Originaldetails nicht als gesicherte Hostursache bewertet. Gekürzte Retrievals beweisen keine ursprüngliche Trunkierung. Historische Abnahmen bleiben in PLAN-0048 bis PLAN-0051; reine Produktfindings werden hier nicht gesammelt. Keine unmittelbare Skilländerung beauftragt oder ausgeführt.
