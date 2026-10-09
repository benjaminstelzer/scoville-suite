# PLAN-0049: Verständlichkeit und Umsetzungskontrolle

Gezielte Prüfung der Änderungen aus PLAN-0048. Angefordert waren Luna 6/Medium sowie die ursprünglichen Konsensreviewer Sol 6.1/Xhigh und Opus 5.5/High. Die Modelleinstellungen wurden beim Dispatch gewählt; separate Modelltelemetrie liegt nicht vor.

## Luna-Proben

Sechs frische Agenten erhielten je drei Szenarien mit vorab getrennt festgelegten Kriterien. Zwei weitere frische Gruppen prüften mögliche Einflüsse des Testauftrags; vier prüften korrigierte Reader, tatsächliche Worker-Aufträge, Prozessregeln und Input-/Output-Routen. Insgesamt zwölf Agenten mit 36 Szenarien. Ein Szenario ist eine Verständnisantwort, kein ausgeführter Workflow. Vollständige Antworten wurden ausgewertet; Rohantworten bleiben ausschließlich im temporären Arbeitsverzeichnis.

| Bereich | Erstprüfung | Gezielte Nachprüfung |
| --- | --- | --- |
| Dokumentreader | Falsches kleinstes Budget; falsche Fortsetzung nach Budgetwechsel; Wiederholung eines fehlgeschlagenen Aufrufs ohne benannte Korrektur | Neutraler Auftrag beseitigt nur die erste Abweichung. Nach Textkorrektur: alle drei Fälle richtig; bei Budgetwechsel Neustart mit Teil 1, nach Fehler nur sichtbare Korrektur oder ungelesen/Stop |
| Manager | Alle drei Fälle richtig: READY/START, vollständiger Auftrag und erforderliche Dokumente, Übernahmegrenzen | Keine Wiederholung unveränderter Fälle |
| Hash | Alle drei Fälle richtig: Originalbytes, Vergleich und getrenntes vollständiges Lesen, Fehler-/Fallbackgrenzen | Kein zusätzlicher Verständnislauf; technische Diagnosefälle erweitert |
| Shell | Ein Fall ersetzt den fiktiv vorgegebenen Interpreter durch den Hostpfad aus dem Testauftrag; zwei Fälle richtig | Ohne Hostpfad im Auftrag alle drei richtig. Kein zusätzlicher Discovery-Fix daraus abgeleitet |
| Prozess | Alle drei Fälle richtig: Erfolg setzt die Shell fort, Kindstatus bleibt erhalten, Startfehler/POSIX | Nach UTF-8-Fix alle drei neuen Fälle richtig, einschließlich CP437 und Unicodepfad |
| Planfelder | Alle drei Fälle richtig: Aktionen/Ergebnisse/Bedingungen, ausstehende Abnahme, Schutzregeln | Keine Wiederholung unveränderter Fälle |
| Tatsächlicher Worker-Auftrag | Direkter Pythonaufruf und rg-Filter richtig; C2 vermischt bei empfangenem Dokument Lesen und Veröffentlichung: teilweise FAIL | Readerroute ausdrücklich abgegrenzt. Frische T1–T3 unterscheiden empfangenen Input, eigenes großes Ergebnis und ungelesenen Input bei zu kleinem Limit richtig |

Die ursprünglichen Abweichungen bleiben erhalten. Neutrales Framing und spätere richtige Antworten machen sie nicht rückwirkend zu bestandenen Fällen. Mehrere Antworten ignorierten die gewünschte deutsche Ausgabesprache; daraus wurde kein Suite-Codefehler abgeleitet.

## Korrekturen

- Gemeinsamer, an Workflow-Kinder übertragener Text enthält wieder die direkte PowerShell-`&`-Regel. Die Discovery-Regel bleibt für ihren eigenen Einstieg erhalten.
- Readertexte verlangen vollständiges Kopieren des erzeugten Befehls. Nur die vorgesehenen Datei-/Teilparameter wechseln; Programm, Launcher und Quotierung bleiben erhalten.
- Budgetierte Eingabereader werden weder zusätzlich in `--run` eingepackt noch veröffentlicht oder als Quellerfassung gespeichert. Die zulässige Lieferung eigener großer Ergebnisse bleibt erhalten.
- Bei geändertem Ausgabelimit beginnt das vollständige Lesen mit Teil 1 unter der neuen kleinsten Grenze. Eine bindende Grenze darf nicht zur Fortsetzung der alten Teilfolge erhöht werden.
- Ein fehlgeschlagener Reader darf erst nach Korrektur einer sichtbaren Ursache erneut beginnen; andernfalls bleibt der Input ungelesen und abhängige Arbeit stoppt.
- Windows-Startdiagnosen werden ausdrücklich als UTF-8-Bytes auf stderr geschrieben. Vorher erzeugte ein fehlender Unicodepfad unter CP437 tatsächlich einen `UnicodeDecodeError`; der fokussierte Regressionstest besteht nach dem Fix.
- Hashdiagnosen nennen bei fehlendem Limit den richtigen `--sha256`-Aufruf. Unlesbare empfangene Artefakte bleiben unverifiziert und unverändert.

Kanonische Eigentümer: `../shared/runtime/native_task_arguments.py`, `document_reader.md`, `check_text_size.py`, `../shared/prompting/common.md` und der betroffene gemeinsame Runtime-Test. Suite-Snapshots wurden daraus erzeugt. Die Planfeldregel und Interpreterdiscovery erhielten hier keine weitere Änderung.

## Technische Prüfung

Sechs betroffene unittest-Fälle bestehen jeweils unter Windows und Linux: Hashmodi und Diagnosen, Argumente/Prozessstart, generierte Teilreader und Kommando-Capture, sieben tatsächliche Managerreader, UTF-8-Teilrekonstruktion sowie exakte Paket-/Helperinventare. Nach der reinen Routenpräzisierung wurden nur Managerreader und Inventar erneut auf beiden Systemen geprüft: jeweils 2/2 PASS. Der Unicode-Startfehler wird mit CP437 unter PowerShell 5.1 und 7 geprüft. Windows: Python 3.14.3; Linux: WSL Ubuntu-24.04/Python 3.12.3 und sh. Die zwei unveränderten technischen Ergebnisse aus [PLAN-0048](0048-scoville-aufruf-fixes.md) wurden wiederverwendet.

## Ursprüngliche Reviewer

Sol: ursprünglicher Agent `ask_sol0047_consensus`, angefordert gpt-6.1-sol/Xhigh. Opus: fortgesetzte Session `b89b0e56-0d55-45ba-9df2-2bbe6ce859fe`, angefordert claude-opus-5-5/High. Beide prüften tatsächliche Quellen, Diffs, vollständige relevante Luna-Antworten und Kriterien. Ihre Findings führten zu den oben genannten Korrekturen. Beide nehmen den Endstand einschließlich Routenpräzisierung und T1–T3 im geprüften Umfang ab; kein verpflichtendes Finding bleibt offen. Opus meldete fortgesetzten Kontext ohne Permission-Denials; tatsächliche Modell-/Efforttelemetrie war nicht verfügbar.

Nicht blockierend bleibt „unchanged“ im Readertext auf das Beibehalten der erzeugten Aufrufform bezogen: vorgeschriebene Datei-, Teil- und Limitwechsel gelten weiterhin. Die konkreten Proben verstanden dies. Bei neuer Fehlinterpretation gezielt erneut prüfen.

## Grenzen

Stichproben beweisen keine universelle Verständlichkeit. Windows-/Linux-Verständnisszenarien ersetzen keine reale Modellausführung auf beiden Systemen; diese ist von den tatsächlichen Runtime-Tests getrennt. Keine komplette historische Testmatrix, Installation, Veröffentlichung oder EMPCO-Aktion. Das unveränderte Skill-Creator-Problem mit `compatibility` wurde nicht erneut geprüft oder durch Entfernen der Metadaten verdeckt.
