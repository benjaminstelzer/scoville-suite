---
format_version: 1
id: PLAN-0063
status: completed
created: 2026-10-30
updated: 2026-10-30
---

# Antworterhalt und gezielte Capture-/Diagnosekorrekturen

## Goal

Die zwei P2- und sieben P3-Befunde der Nachprüfung von PLAN-0062 an den aktuellen kanonischen Quellen bestätigen und ausschließlich bestätigte Fehler korrigieren. Verantwortliche Quellen sind members/ und ../shared/; abgeleitete Dateien entstehen über den vorhandenen Buildweg. Jeder bestätigte Helperfehler erhält eine Regression im bestehenden Harness. Der [Bericht](../testing/0063-antworterhalt-und-capture-restkorrekturen.md) hält je Punkt Beobachtung, Änderung, Ergebnis und Grenzen fest.

Der Nutzer hat den vollständigen GitHub-Push und lokale Skillupdates freigegeben. Auslieferung umfasst die private CI und tatsächlich geänderte öffentliche main-Ziele. Lokal werden vorhandene Codex-Suitekopien vollständig und bei Claude Code ausschließlich Scoville Plan aktualisiert. Übrige Claude-Skills bleiben unverändert. Keine neuen Tags oder Releases. Für geändertes Python ist eine passende neue Matrix erforderlich. Bei Modelltests gilt gpt-6.1-sol/low; ohne Modelllauf keine Wirkungsbehauptung.

## Non-goals

- Keine Umsetzung der bewusst offenen Berichtspunkte aus PLAN-0062, insbesondere Ladeumfang, UTF-8-Stoppregel, Layoutkopplung oder Rundengrenze.
- Keine zusätzlichen Absicherungsframeworks, bezahlten Claude-Aufrufe oder Änderungen außerhalb der neun Befunde.
- PLAN-0062 bleibt abgeschlossen.

## Work items

### W-001 Erhaltene Ask-Antworten bei Speicherfehler weiterverwenden
Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: Ein Rohspeicherfehler verwirft keine bereits erhaltene Claude-Antwort; Ask nutzt private nutzereigene temporäre Ablage.
Acceptance: Blockierte Ablage und testbare Rechtefehler erhalten Antwort und Sitzungszuordnung mit raw_file null und knapper Ursache. Normalfall liefert die Rohdatei. Große Aufträge scheitern vor Adviserstart verständlich. Kein bezahlter Wiederholungslauf und kein doppelter Speicherversuch durch den Consumer.
Instructions: P2-1 an ask_claude.py, ask.py und build_adviser_prompt.py prüfen. Vorhandenen Publikationsmechanismus und bestehende Tests nutzen; keine neue Speicherinfrastruktur.
Steps:
1. [status: done] Fehler mit lokalem CLI-Platzhalter und blockierter Ablage nachstellen, am Ask-Owner korrigieren und im vorhandenen Ask-Harness prüfen; fertig bei erhaltenem Ergebnis, expliziter Speicherdiagnose und intaktem Normal-/Großauftragsweg.
Evidence: Blockierte gemeinsame Ablage und vier injizierte Speicherfehler erhalten die Antwort ohne erneuten Aufruf; gezielte Ask-Regressionsfälle bestanden. Große Speicherfehler liefern keine Spawnargumente.

### W-002 Vollständigen Capture ohne Tokenbudget ermöglichen
Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: Der Checker sichert unbekannt begrenzte Ausgabe vollständig und erhält Signal- und Doppelfehlerdiagnosen.
Acceptance: P2-2 erlaubt --run --publish-full --project-root ohne Limit mit vollständiger Datei und kompakter Statusausgabe ohne Inline-/Fitbehauptung. Erfolg, Kindfehler, ungültiges UTF-8 und Timeout behalten ihre bestehenden Exit-/Vollständigkeitsverträge. Begrenzter Modus bleibt erhalten. P3-1 ergänzt SIGHUP auf POSIX; P3-2 bewahrt ursprünglichen Capturefehler und gegebenenfalls process_id bei zusätzlichem Speicherfehler. General-/Codex-Texte widersprechen sich nicht; schreibgesperrte Rollen erhalten keine neue Befugnis.
Instructions: ../shared/runtime/check_text_size.py und ../shared/prompting/output-delivery.md sind Owner. POSIX-Signalnachweise nur behaupten, wenn tatsächlich ausgeführt.
Steps:
1. [status: done] Die drei Fehler reproduzieren oder vollständig im Code belegen; Lauf ohne Budget, Signalbehandlung und zusammengesetzte Fehlermetadaten korrigieren. Fertig nach vorhandenen Runtime-Harnesstests einschließlich Originalbytes und fehlender Wiederholung.
2. [status: done] Den erlaubten limitlosen Aufruf und SIGHUP im bestehenden Ausgabetext knapp ergänzen; fertig bei Quellenvergleich mit unveränderten Rollen-, Signal-, UTF-8- und begrenzten Captureverträgen.
Evidence: Limitloser 431-KB-Capture, Kind-Exit 0/7/125, UTF-8 und Timeout technisch geprüft. SIGHUP ergänzt; POSIX-Signaltests unter Windows ausgelassen. Doppelfehlerprüfung erweitert.

### W-003 Falsche Reparaturhinweise des Planvalidators berichtigen
Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: Step- und Batchdiagnosen benennen den Primärfehler und einen passenden Reparaturweg.
Acceptance: P3-4 erzeugt bei fehlerhaften vorhandenen Steps keinen zusätzlichen Legacy-Next-Action-Hinweis; echte Legacy-Items bleiben geprüft. P3-5 benennt nachgestellte Step-Leerzeichen. P3-7 nennt ungültige Kalenderdaten in Meldung und Korrektur, ohne Diagnosecodes entgegen dem Vertrag zu ändern. Grammatik und Selectorsemantik bleiben erhalten.
Instructions: validate_profile.py und bestehende Planregressionen bearbeiten; bestätigte und korrigierte Eingaben prüfen.
Steps:
1. [status: done] Alle drei Fälle am aktuellen Validator nachstellen, eng korrigieren und mit positiven Gegenfällen prüfen; fertig bei richtigen Diagnosen, unveränderten Codes und bestandenem Plan-Harness.
Evidence: 15 Formatregressionen bestanden: führende Null ohne Legacy-Fehlhinweis, präziser Leerzeichen-/Kalenderhinweis und korrigierte Gegenfälle; Codes und Grammatik unverändert.

### W-004 Qualitätskriterien auch vor Codeempfehlungen laden
Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: Codeempfehlungen erreichen dieselben Qualitätskriterien wie Implementierung und Review.
Acceptance: P3-3 ist an Code SKILL.md und dem Qualitätsowner belegt und mit einem knappen Ladehinweis korrigiert. Rein konzeptionelle Antworten bleiben ohne neue Referenzpflicht; bestehende Change-/Validationbedingungen bleiben erhalten.
Instructions: Nur die belegte Routinglücke ändern, keine neue Reviewphase oder Checkliste.
Steps:
1. [status: done] Den aktuellen Ladeweg prüfen und an Code SKILL.md präzisieren; fertig bei geprüftem Quellenvergleich und gültigen erzeugten Varianten ohne pauschale Advise-Aktivierung.
Evidence: Quelle und Qualitätsowner belegen die Routinglücke. Gemeinsamer Ladesatz deckt Empfehlungen ab; Konzeptausnahme bleibt. Gebaute Varianten geprüft, keine Modellwirkung behauptet.

### W-005 Setup zeigt Schema-2-Cleanupbedarf korrekt an
Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: Setup show unterscheidet Schema-2-Altfelder von Schema-1-Routentabellen und beschreibt lesende Fehler korrekt.
Acceptance: P3-6 meldet für gültige Schema-2-Paare mit bekannten Altfeldern cleanup_required samt betroffenen Feldern. Show bleibt lesend, Cleanup und normale gültige/ungültige Konfigurationen behalten ihre Verträge. Lesende Fehler behaupten keinen gescheiterten Speichervorgang.
Instructions: setup.py und bestehende Setup-Tests bearbeiten; unbekannte Felder nicht still verwerfen.
Steps:
1. [status: done] show mit pin_threads nachstellen und die Schemaunterscheidung samt lesenden Diagnosen korrigieren; fertig nach gespeichert unverändertem Eingangsprofil, verständlicher Fehlermeldung und funktionierendem ausdrücklichem Cleanup.
Evidence: Elf Cleanup-/Migrationstests bestanden, einschließlich Schema-2-Altfeldanzeige, unveränderter Show-Datei, explizitem Cleanup und lesendem Fehlertext.

### W-006 Geprüften lokalen Kandidaten und Freigabeumfang vorlegen
Status: done
Depends on: [W-001, W-002, W-003, W-004, W-005]
Blocked by: []
Decisions: []
Outcome: Der begrenzte Folgefix ist lokal geprüft und sein noch gesperrter Auslieferungsumfang konkret benannt.
Acceptance: Bestehende betroffene Tests und check_all.py bestehen. Gemeinsame Dateien und variantengerechte Texte sind über den vorhandenen Builder vollständig erzeugt, Paketstruktur und Markdown-Links geprüft, unbeabsichtigte Regelverluste gegen die Baseline ausgeschlossen. Neue Matrix und dadurch abhängige Releasegates werden ohne Pushfreigabe nicht als bestanden ausgegeben. Bericht unterscheidet jeden erledigten, widerlegten oder offenen Punkt und nennt alle betroffenen Distributionen.
Instructions: Die frühere CI-/Export-/Pushsperre wurde für diesen Kandidaten ausdrücklich aufgehoben. Die Auslieferung und begrenzte lokale Installation gehören zu W-007. Modellwirkung bleibt ohne Lauf unbewiesen.
Steps:
1. [status: done] Shared-Snapshot und tatsächlich betroffene Changelog-/README-Quellen aktualisieren, technische und Paket-/Linkprüfungen ausführen; fertig bei eindeutig dem Quellstand zugeordneten Ergebnissen und dokumentierten Grenzen.
2. [status: done] Quellen und erzeugte Consumer gegen die Baseline reviewen, Bericht abschließen und konkreten CI-/Export-/Publikationsumfang vorlegen; fertig bei überprüfbarem Kandidaten ohne gesperrte Aktion. Fehlender erforderlicher CI-/Releasebeleg bleibt als Blocker sichtbar.
Evidence: Gesamtcheck zwölf Gruppen, 530 ausgeführte Tests, acht Skips. Neue Matrix 41068939874 auf 194ea71: sechs Jobs bestanden, einschließlich POSIX-Signalfällen auf Linux/macOS.


### W-007 Freigegebene Distributionen und lokale Skills ausliefern
Status: done
Depends on: [W-006]
Blocked by: []
Decisions: []
Outcome: Der geprüfte Folgefix ist auf GitHub und im freigegebenen lokalen Installationsumfang verfügbar.
Acceptance: Beide Suite-Exporte und alle tatsächlich geänderten Einzelrepo-Distributionen stammen aus einem sauberen, geprüften Quellcommit mit passender erfolgreicher Matrix. Paket-, Link-, Exportprofil- und Privatschutzprüfungen bestehen; Remote-main entspricht vollständig den verifizierten Kandidaten. Vorhandene Codex-Kopien enthalten ihre Mainloop-Variante, bei Claude Code wird nur Plan aus der General-Variante aktualisiert. Übrige Claude-Skills, Projekteinstellungen und fremde Skills bleiben erhalten. Keine neuen Tags oder Releases.
Instructions: Aktuelle Nutzerfreigabe umfasst privaten CI-Push, Exporte, öffentliche main-Pushs und lokale Updates. Die spätere Präzisierung begrenzt Claude Code auf Plan. Veraltete ersetzte Paketdateien aus den freigegebenen Installationen entfernen; keine neue Installation fehlender Geschwister oder automatische Sessionfortsetzung.
Steps:
1. [status: done] Vier Paketansichten mit Matrix 41068939874 über den bestehenden CLI-Build verifizieren, beide Quellprofile exportieren und vorgegebene öffentliche Checkouts synchronisieren; fertig bei geprüften Paketen, Exportprofilen, Links und vollständiger Kandidatenzuordnung.
2. [status: done] Nur geänderte main-Ziele pushen und vollständig remote abgleichen; vorhandene Codex-Skills sowie ausschließlich Claude-Plan aktualisieren und gegen die verifizierten Pakete prüfen. Fertig bei übereinstimmenden Remote-/Installationsinhalten und unverändertem nicht freigegebenem Umfang.
3. [status: done] Auslieferungsbelege in diesem Plan und im Bericht festhalten, Profil korrekt abschließen und die Abschlussrecords in beiden Suites nachliefern; fertig bei validiertem Endzustand, sauberem Quellstand und remote geprüftem Abschluss.
Evidence: Sieben öffentliche main-Pushs mit vollständigem Remote-Abgleich; Skillwriter unverändert. Codex und ausschließlich Claude-Plan aktualisiert, übriges Claude unverändert. Matrix 6/6 bestanden.
