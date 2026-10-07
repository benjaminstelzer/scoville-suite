# Bestätigte Fixes und vorhandene gezielte Nachtests

Prüfung der bestehenden Nachweise am 05.10.2026, keine neuen Testläufe oder Modellversuche. Reviewurteile ersetzen die angegebenen Tests nicht.

| Fix | Beobachteter Nachtest | Verantwortlicher Nachweis |
| --- | --- | --- |
| W-001: stdout.write/flush nach Reportwrite und ValueError bei geschlossenem Stream | 14 fokussierte Feedback-Tests PASS, Rücknahme eigener Änderungen und Erhalt konkurrierender Writes | 0035-w001-result.md |
| W-002: fehlerhafte Extraktion automatischer Temp-Pfade im lokalen Test | 23 fokussierte Tests PASS mit vollständigem Sonderzeichenpfad | 0035-w002-result.md |
| W-002: Vergleich aufgelöster Assignment-Pfade mit unaufgelöstem Temp-Alias | 23 Windows-Tests PASS, tatsächlicher TMPDIR-Symlink unter WSL 1/1 PASS | 0035-w002-result.md |
| W-003: PowerShell 5.1 verliert Quotes/ändert Progress-Key | Drei gezielte Tests PASS, reale native unveränderte Korrekturaufrufe und kompletter JSON-Vergleich PASS | 0035-w003-result.md; Actions-Modusnachweis noch offen |
| W-006: escaped Backticks, Absatzgrenzen, ATX-Headings und verbleibender Backtick-Run | Vier fokussierte CLI-Tests PASS und 118 Plan-Tests PASS nach allen Fixes; unveränderter Korpus | 0035-w006-result.md |
| W-006: Harness erwartete exit0 trotz unzulässigem Extra-H2 | Korrigierte Erwartung prüft SECTION_H2_ORDER plus Warnung/exit1; Gesamtcheck 118 PASS | 0035-w006-result.md |
| W-008: fehlende, leere oder mehrfache Proposal-Titel | Alle vier ungültigen Fälle mit korrigierten CLI-Folgeaufrufen; fünf fokussierte und 114 Plan-Tests PASS | 0035-w008-result.md |
| W-016: Source-Metadaten erlaubten implizite Workflow-Aktivierung | Tatsächliche Codex-Payloadprojektion mit false und unverändertem explizitem Start geprüft | 0035-w016-result.md; keine installierte Host-Triggerwirkung behauptet |
| W-009-Vorbereitung: doppelte Outputziele und Windows-Case-Aliase im Register | Sieben Budgettests PASS einschließlich Alias-/Duplicate-/Atomic-Failure-Fällen | 0035-w009-harness-result.md |
| Runtime-CI-Ergänzung: Budget-Fixture und WSL-Umgebung | Gezielter Budgettest 1/1, vollständige Windows/WSL-Suite jeweils 16/16 PASS | 0035-runtime-ci-gap.md |
| Nachweistext: Paket-/Gesamtdateizahl verwechselt | Neu gezählt, alle Paket-Hashes verglichen: 291 Paketdateien, insgesamt 295; PASS | 0035-runtime-ci-count-retest.json |
| Parent-Capture: altes channel-Feld statt aktueller phase | Beide gesicherten Finals stimmen exakt mit task_complete überein | 0035-w003-review-4.json; 0035-w005-review-3.json |

W-004s fehlende unmittelbare Dateibaum-Beobachtung nach Fehler wurde durch einen tatsächlichen modellfreien Fehler-/Korrektur-Consumer ergänzt; kein Produktfix. Sonstige Fixture-/Capture-Fehler und ihre erfolgreichen korrigierten Folgeaufrufe bleiben in den jeweiligen Rohspuren erhalten.

Offen bleiben die finale W-001-Luna-Probe in W-007, neue Actions-Ausführung für W-003/W-005, übertragene W-009-Fälle und W-015. Aus vorhandenen Nachtests folgt keine Gesamtplan-Abnahme.
