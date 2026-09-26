# PLAN-0014: Abnahmestand

Geprüfter Ablaufkandidat: candidate-grouping-titles im isolierten Testbereich.
Die damaligen 104 Paketdateien waren bytegleich zum damaligen Staging.
Die anschließende Ask-Titeländerung liegt in candidate-ask-titles und ist in
ask-title-final.md geprüft. Der abschließende Stand candidate-astra-final
enthält zusätzlich die geprüfte Kürzungssperre und korrigierte Workflow-README;
104/104 Dateien stimmen mit Staging überein. check-packages besteht. Keine reguläre Installation,
Quellcommits oder Veröffentlichung. PLAN-0015 wurde nicht verändert.

Frühere Regeln in abgeschlossenen Punkten bleiben historische Aufträge.
Aktuell gelten ADR-0089 (JSON lesen/automatisch erzeugen), ADR-0092
(Archivierung ohne Nachprüfung), ADR-0093 (geordnete Gruppen) und ADR-0094
(kurze Gruppenmeldung und vollständiger Bereich im Titel).

| Punkte | Beobachteter Nachweis |
| --- | --- |
| W-001 | Reproduzierbare historische Rolloutauswahl und genehmigte Zählkorrektur in token-overhead-implementation.md und Analyse. |
| W-002, W-003 | Native Ergebnisnachrichten wecken Coordinatoren; keine Lifecycle-/Parser-Zwischenschicht. Raw Calls aus PLAN-0003/0005 übergeben Builder-output unmittelbar an create_thread. |
| W-004, W-005 | Ein Work Item pro Auftrag als Kontext, expliziter Step-Bereich und relevante Fakten. PLAN-0003 setzt nach Step 1 nur Restarbeit fort; Coordinator übernimmt aus kleinem Laufdatensatz. |
| W-006 | Eigene native Ask-Chats, eindeutige Sender/Referenzen, tatsächliche Rückzustellung; Fehlerfall fehlender Datei. Ask Claude bleibt echter CLI-Verbraucher. |
| W-007, W-008, W-011 | Dokumentierte Helper-Aufrufe und tatsächliche Verbraucher mit Luna/SOL. Erfolgreiche Texte werden nicht repariert; Klartext-Dispatch, erlaubte technische JSON-Daten und Serialisierung. |
| W-009 | Gleicher SOL-Medium-Fall: Coordinator 84 auf 41 Modellaufrufe; Gesamtinput 6.670.228 auf 3.075.684 einschließlich realer Code-Reparatur. Stop/resume separat im ersten nativen Lauf. |
| W-010 | PLAN-0012 W-017 erhält Analyse, Paketzuordnung und Testbelege. Installation/saubere Releasequelle/Remotegates bleiben dort offen. |
| W-012 | Workflow, Ask, Plan und Setup mit SOL 6 Medium; finale Paketzuordnung in suite-simplification-comparison.md. |
| W-013 | Zehn kanonische private Skills inventarisiert; Laufzeithelper mit Verbrauchern geprüft. GitHub-release-Modus mit ehrlichem sauberem Testbuild. Live-Familienabweichungen bleiben externe Releasegrenze. |
| W-014 | PLAN-0003: letzter Vorgängerwrite vor Erstellung, Übernahmenachricht und einmalige Selbstarchivierung; keine waits oder Archivierungsnachprüfung. |
| W-016 | Findings mitgeteilt, Nutzerfreigabe eingeholt, kleinste Korrekturen und Nachtests dokumentiert in project-rules-review.md. |
| W-017 | PLAN-0005: zwei Sätze zu Plan/Gruppierung/Grund; native Worker-, Reviewer- und Repair-Titel tragen STEPS-1-3. |
| W-015 | Unter ADR-0095 umgesetzt; ask-title-final.md belegt tatsächlichen SOL-Titel und native Antwortzustellung. |
| W-018 | Beide Astra-Findings behoben; Astra-Nachreview ohne materiellen Restbefund. SOL testet vollständige, tatsächlich gekürzte und fehlgeschlagene Ausgabe erfolgreich; siehe astra-final-review.md. |

Hauptbelege: docs/token-overhead-analyse-2026-09-26.md,
suite-simplification-comparison.md, private-helper-inventory.md sowie
temp/2026-09-26-private-helper-tests/{native-run-3-audit,controlled-comparison,
grouping-title-test.md,final-package-match.json} im Workspace.

Grenzen: ein kontrolliertes Vergleichspaar, keine allgemeine Kostengarantie.
Cacheinput ist in Inputtokens enthalten. Die native Code-Reparatur zählt mit.
Frühere Fehlversuche und der anfänglich dreisätzige Formulierungstest bleiben
dokumentiert. Ein nicht bestandenes Live-Release-Audit ist kein Helper-Erfolg
und wird nicht zu einer Veröffentlichungsfreigabe umgedeutet.

Die Abnahmematrix deckt alle 18 Punkte ab. Der Astra-Schlussreview und seine
gezielten Nachprüfungen sind abgeschlossen. Installation und Veröffentlichung
bleiben wie beauftragt außerhalb dieses Plans bei PLAN-0012.
