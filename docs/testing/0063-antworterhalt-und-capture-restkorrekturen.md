# PLAN-0063: Antworterhalt und Capture-/Diagnosekorrekturen

## Ausgang und Befugnis

Suite-Baseline a54ebe77ec12b8e63bd8ee8c0bb3feaf882d1030, Shared-Baseline 9bd6639b1e1839a611f248b4d04078782c375510. Öffentliche Ausgangsstände entsprechen der Nachprüfung von PLAN-0062. Umsetzung lokal freigegeben, Pushs einschließlich privater CI, Quell-Exporte und Installation gesperrt. PLAN-0062 bleibt abgeschlossen.

## Befunde und Ergebnisse

| Punkt | Bestätigung | Änderung | Prüfung und Grenze |
| --- | --- | --- | --- |
| P2-1 Ask-Rohspeicher | Vor Fix: reguläre .scoville-Datei im temporären Root und injizierte Speicherfehler werfen die empfangene Antwort weg. | Bestehender Ask-Owner legt exklusiv private nutzereigene Tempverzeichnisse an. Speicherfehler liefern raw_file null und raw_file_error; ein vorhandener vollständiger Recoverypfad bleibt nutzbar. Consumer versucht das Speichern nicht nochmals. Große Aufträge nutzen dieselbe Funktion. | Echter lokaler CLI-Platzhalter liefert Antwort und Sitzung trotz Publisher-/Verzeichnisfehler, Wirkung genau einmal. Gemeinsame Pfadkollision, Normal-/Recoveryweg und misslungener Großauftrag geprüft. Kein bezahlter Claude- oder Modelllauf. Private POSIX-Modusbits hier nicht ausgeführt. |
| P2-2 Capture ohne Tokenlimit | Originalaufruf ohne Limit endet vor dem Kind mit 125. | --run mit --publish-full und Projektroot erlaubt ohne Zahlenlimit, immer Datei und kompakter Status statt Inlineinhalt/Fitbehauptung. | 431-KB-Originalbytes vollständig nachgelesen, Erfolg, Kind-Exit 7/125, ungültiges UTF-8 und Timeout im bestehenden Runtime-Harness. UTF-8-/Timeoutfehler bleiben Checker-Exit 125 mit tatsächlichem Kindstatus in Metadaten. Begrenzter Modus bleibt über dessen vorhandene Fälle geprüft. |
| P3-1 SIGHUP | collect_output registriert zuvor nur SIGINT/SIGTERM. | SIGHUP auf POSIX im selben begrenzten Cleanupweg, Ausgabetext entsprechend ergänzt. | Vorhandener Signaltest prüft SIGINT/SIGTERM/SIGHUP jeweils mit eigener Bereitschaftsdatei und tatsächlicher Prozessfamilie. Unter Windows übersprungen, kein POSIX-Erfolg behauptet. Neue Matrix erforderlich. |
| P3-2 Doppelfehler | Originalregression: publication_failed verliert capture_error und process_id. | Zusätzlicher Speicherfehler erhält ursprüngliche Fehlerart, Exit, Vollständigkeit und bei unsicherem Cleanup die PID. Vollständige Recoverydatei oder explizit fehlende Kopie unterscheiden sich. | Echter Timeout plus injizierte Cleanupunsicherheit und Link-/Schreibfehler prüfen Metadatenkomposition. Recoverybytes bleiben erhalten; ohne Datei keine unbenutzbare Leseanweisung. Das beweist keine reale fehlgeschlagene Prozessbereinigung. |
| P3-3 Empfehlungsladeweg | Qualitätsowner gilt für Empfehlungen, Einstieg lädt ihn vorher nur bei Implementierung/Review. | Ein bestehender Ladesatz vereint Implementierung, konkrete Empfehlungen und Reviews. Redundanter Reviewsatz entfällt. | Quellenvergleich und erzeugte General-/Codex-Varianten: Konzeptausnahme und weitere Routenbedingungen erhalten. Keine neue Checkliste und kein Modell-Wirkungsnachweis. |
| P3-4 fehlerhafte Steps | Vor Fix: führende Nullen erzeugen zusätzlich einen falschen Legacy-Next-Action-Vorschlag. | Nachgelagerte Legacyprüfung unterbleibt bei Stepdiagnosen desselben Items. | Fehlerhafte 01/02-Statussteps liefern Stepfehler ohne falschen Reparaturweg. Echte Legacyarbeit ohne Steps verlangt weiterhin Next action. Keine neue Grammatik. |
| P3-5 Step-Leerzeichen | Vor Fix nur allgemeine Statusdiagnose bei trailing whitespace. | Bestehender Code und seine Korrektur benennen das nachgestellte Leerzeichen. | Fehler und korrigierte Eingabe geprüft, keine Änderung an Selector oder zulässigen Steps. |
| P3-6 Setup show | Vor Fix meldet Schema 2 mit pin_threads fälschlich ein Legacyproblem mit main. | Bekannte Altfelder bei validierten Schema-2-Kernpaaren als cleanup_required mit legacy_fields zeigen. Rein lesende Sammeldiagnose behauptet keinen Speicherfehler. | Show erhält Dateibytes, nennt pin_threads, explizites Cleanup funktioniert. Fehlerhafter Workflowabschnitt bleibt Fehler ohne partielle effective-Erfolgspayload. |
| P3-7 Batchdatum | Kalenderdatum wird schon abgewiesen, Diagnose nennt bisher nur das Format. | Meldung und Korrektur nennen gültiges Kalenderdatum, bestehender DECISION_BATCH_HASH_INVALID-Code bleibt. | Ungültiger Februar und gültiges korrigiertes Datum geprüft. Historischer 64-Hex-Vertrag bleibt erhalten. |

## Quellenreview und lokale Pakete

- Maßstab: Git-Baselines oben. Geänderte Quellen, echte Consumer und Regressionen geprüft. Erforderliche Rollenrechte, vollständige Inhalte, bestehende UTF-8-Grenze, Kind-/Checkerstatus, atomarer No-Replace-/Recoveryvertrag und übrige Lesebedingungen bleiben erhalten. Die Erweiterungen gehören ausschließlich zu den neun Befunden. Keine neue dauerhafte Helper-Infrastruktur.
- Shared-Snapshot über den vorhandenen Generator synchronisiert. Vier lokale Entwicklungsansichten über den bestehenden Builder erzeugt und mit --check-packages geprüft. Ihr Runtimebeleg ist ausdrücklich pending, nicht bestanden. Keine Quell-Exporte oder Synchronisierung öffentlicher Checkouts.
- README-Quellen benötigen keine inhaltliche Änderung: Die vorhandenen allgemeinen Darstellungen enthalten keine entgegenstehende Zusage. Root und acht tatsächlich betroffene Member erhalten Changelogs; Skillwriter bleibt unverändert.
- Skill-Creator-Validator lehnt das unverändert zulässige compatibility-Feld ab. Das Feld bleibt erhalten; YAML-, Feld- und Paketprüfungen erfolgen separat. Dies ist eine Validatorgrenze, kein behaupteter Formatpass.
- Keine Modellläufe und keine Aussage über geänderte Modellwirkung. Ablauf- und Ergebnisbelege stammen aus Python-/Prozess-/Dateiprüfungen mit aufgezeichneten CLI-Platzhaltern.

## Noch gesperrter Auslieferungsumfang

1. Privates Repository scoville-runtime-ci: genau den lokal vorbereiteten neuen Python-/Testkandidaten auf main committen/pushen und die sechs Plattform-/Python-Jobs auswerten. Alte Matrix 41056288278 darf die geänderten Eingaben nicht freigeben.
2. Erst nach gültiger Matrix freigabefähige Paketbelege und beide Quell-Exporte erzeugen. Exportierte Profile und Links prüfen. Geänderte öffentliche Ziele sind scoville-suite, scoville-suite-for-codex-mainloop sowie scoville-code, scoville-handoff, scoville-plan, scoville-ui und scoville-ask-for-codex. Skillwriter bleibt unverändert. Cleanup, Workflow und Setup werden nur in ihren vorgesehenen Suitepaketen verteilt.
3. Nur diese geprüften main-Stände synchronisieren/pushen und remote prüfen. Keine neuen Tags, Releases oder Installation. Diese Liste ist eine Freigabevorlage und führt keine dieser gesperrten Handlungen aus.

## Abschließende lokale Ergebnisse

- check_all.py: exit 0, zwölf Prüfgruppen bestanden, 530 Python-Tests ausgeführt und acht ausgelassen. Zwei Pfade enthalten keine Python-Tests (Code/Handoff); sie sind keine bestandenen Modelltests. Aktuelle Gruppen: Shared 101, Entwicklung 73, Plan 142, Workflow 87, Ask 63, Setup 31 und Runtime 33 ausgeführte Tests.
- Vier lokale Paketansichten mit --check-packages bestanden. YAML/Frontmatter aller 22 Pakete geprüft, 19 Checker-Kopien bytegleich zum gemeinsamen Owner, Ausgabetexte innerhalb jeder Hostvariante bytegleich, Code quality an allen vorgesehenen Zielen bytegleich. Paketlinks werden im vorhandenen Builder, aktuelle Planlinks im Profilvalidator geprüft. Quell-Exportprofile sind mangels Exportfreigabe noch ungeprüft.
- Privater Runtime-CI-Kandidat vorbereitet, Eingangskennung e70eff5bc4b31506122f7fcce26dbac8ce25393b30c085af5719234caa06a824. Kein neuer Matrixlauf und keine Freigabe durch den alten Lauf. Der lokale Paketbuild belegt Struktur und Vollständigkeit, keinen freigegebenen Releasebuild.
- Source-/Textvergleich gegen die Baselines bestätigt die neun gezielten Änderungen ohne weitere Regel-, Rechte- oder Schnittstellenabschwächung. Keine Wirkungsaussage für ein Modell. Insbesondere POSIX-Signalverhalten bleibt bis zur Plattformprüfung offen.
- Temporäre Checkeingaben waren beim Aufräumen gesperrt und wurden durch den bestehenden Cleanupweg erfolgreich nach Desktop/_delete verschoben. Kein verbleibender Cleanupfehler.

Geprüfter Shared-Quellcommit: 7e199a7356f640000f0eec6a35deb29c7661417b. Suite-Zuordnung folgt dem Commit dieses Berichts nach dem bestandenen Gesamtcheck.

## Freigegebene Auslieferung

Die spätere Nutzerfreigabe hebt die vorherige Push-/Export-/Installationssperre für diesen Kandidaten auf. Lokale Updates gelten vollständig für vorhandene Codex-Suitekopien und bei Claude Code ausschließlich für Scoville Plan. Übrige Claude-Skills bleiben unberührt. Keine neuen Tags oder Releases.

Private CI: Commit 194ea7125c3961a2c550daa4aa163f2ed03e8915, [Runtime helpers 41068939874](https://github.com/benjaminstelzer/scoville-runtime-ci/actions/runs/41068939874). Alle sechs Jobs auf Windows/macOS/Linux mit Python 3.11/aktuell erfolgreich. Damit ist der zuvor fehlende POSIX-Nachweis der SIGINT-/SIGTERM-/SIGHUP-Regressionsfälle auf Linux/macOS erbracht. Modellwirkung bleibt ungeprüft.

Geänderte öffentliche Ziele: scoville-suite, scoville-suite-for-codex-mainloop, scoville-code, scoville-handoff, scoville-plan, scoville-ui und scoville-ask-for-codex. Skillwriter wird mitverglichen und ohne Änderung übersprungen. Alle bestehenden Ziele wurden auf main, ursprüngliche Sichtbarkeit, saubere Checkouts und fehlende Divergenz geprüft.

## Verifizierte Auslieferung und Installation

- Funktionaler Kandidat aus Quellcommit fb0aefc nach erfolgreicher neuer Matrix mit vier freigabefähigen CLI-Builds erzeugt. Publikationsgates, beide Quell-Exportprofile samt Links und Privatausschlüssen bestanden. README-Gesamttexte sind bytegleich zum bereits gelesenen vorherigen Stand und wurden nicht erneut als neue Texte geprüft. Unveränderte Paketstrukturnachweise wiederverwendet.
- Sieben geänderte öffentliche Ziele auf main veröffentlicht. Vollständiger Gitbaum jedes Remote gegen den verifizierten Kandidaten abgeglichen, Sichtbarkeit erhalten. Skillwriter mitverglichen und ohne Änderung übersprungen. GitHub wies mehrere erste Pushs mit Internal Server Error beziehungsweise commit_refs-Fehler ab. Nach Beobachtung unveränderter Remote-Referenzen gelangen normale Fast-Forward-Pushs, ohne Force oder neue Commits zur Umgehung.

| Repository | Funktionaler Auslieferungscommit | Ergebnis |
| --- | --- | --- |
| scoville-suite | b602954e8c114140d4191d98a07a221b698a4498 | veröffentlicht und vollständiger Remote-Baum geprüft |
| scoville-ui | def0a67550044a802bc755c2a494da25e49a04d7 | veröffentlicht und vollständiger Remote-Baum geprüft |
| scoville-skillwriter | dfd021137f828512ac3ccaab38fae129af057bc6 | unverändert, kein Push |
| scoville-ask-for-codex | 5527258e9d074186f8355cc4b52f9ddce3e60ea6 | veröffentlicht und vollständiger Remote-Baum geprüft |
| scoville-suite-for-codex-mainloop | 004d0b5b67f13aa5e1a42ffd9b53fcebcbbff2a9 | veröffentlicht und vollständiger Remote-Baum geprüft |
| scoville-code | 8e27c902c0b7980be0701780c49054e2d886ec4c | veröffentlicht und vollständiger Remote-Baum geprüft |
| scoville-handoff | be4c25d2b1b58f14d87867277c3324fd53699768 | veröffentlicht und vollständiger Remote-Baum geprüft |
| scoville-plan | a7e7aeecc22dc4b16b0113be8213100fbc965818 | veröffentlicht und vollständiger Remote-Baum geprüft |

- Lokale Installation aus exakt benannten veröffentlichten Suitecommits über den Host-Skill-Installer geladen. 16 geänderte Codex-Installationskopien und ausschließlich Scoville Plan bei Claude aktualisiert. Eine vorhandene Codex-Skillwriter-Kopie war bereits aktuell. Zwölf ersetzte alte Referenzdateien aus den freigegebenen Codex-Paketen entfernt. Fünf übrige Claude-Pakete blieben unverändert, keine fehlenden Geschwister neu installiert.
- Installationsinventar, aktuelle Einstiegstexte und gemeinsame Checker geprüft. Echte kleine Aufrufe des neuen limitlosen Captures aus installiertem Codex-Code und Claude-Plan sowie des installierten Claude-Planvalidators bestanden. Keine Behauptung, dass laufende Agenten ihren bereits geladenen Kontext neu gelesen haben.
- Abschließender vorgeschriebener Gesamtcheck lief parallel zur Auslieferung auf unveränderten Implementierungsquellen und bestand erneut mit zwölf Prüfgruppen. Die danach geschriebenen Abschlussfelder werden gezielt mit dem Planvalidator geprüft. Nachlieferung dieser Abschlussrecords verändert keine Skill-/Helperbytes.
- Keine neuen Tags, Releases oder Änderungen an Projekteinstellungen. Keine Modellläufe oder General-Claude-Modellwirkung behauptet. Native POSIX-Codex-Ausführung bleibt von den nun belegten POSIX-Python-Signaltests getrennt.
