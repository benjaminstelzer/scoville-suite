# Befundabgleich zu PLAN-0058

Prüfmaßstab ist der Nutzerauftrag zum unabhängigen Review der veröffentlichten
PLAN-0057-Lieferung. Die Reviewbehauptungen werden an kanonischen Quellen geprüft;
Zeilenangaben aufgelöster Exporte sind keine identischen Quellenpositionen.
Quellenkorrektur, tatsächliche Modellwirkung und Veröffentlichung bleiben getrennt.
Dieser Bericht und der Folgeplan sind öffentlich.
Der Nutzer hat den geprüften Stand am 2026-10-29 mit „alles pushen“ zur Veröffentlichung freigegeben. Technische Abnahmen bleiben Voraussetzung.

| ID | Soll / zuständiger Quellenbereich | Stand |
| --- | --- | --- |
| A1 | Plan/UI/Cleanup/Setup/Ask laden Datenregeln vor Anforderung oder Lesen von Maschinendaten. | Umgesetzt: fünf SKILL-Einstiege; Paket-/Linktests bestanden; gezielte Wirkungsprobe bestanden, Grenzen siehe unten. |
| A2 | Bestehender Writing-Auslöser erreicht strittige sachliche/technische Schlussfolgerungen; konzeptionelle Ausnahme widerspricht ihm nicht. | Umgesetzt: fünf Writing-Auslöser plus Setup; Ask war bereits abgedeckt. Gezielte Wirkungsprobe bestanden, Grenzen siehe unten. |
| A3 | Code begrenzt zusätzliche Absicherung mit only auf Anforderungen oder glaubwürdige ungedeckte Fehler. | Umgesetzt: Code SKILL.md enthält only; scoped Quellenreview bestanden. |
| A4 | Reviewer prüft unabhängig Fehler/Regressionen im gesamten zuständigen Diff; Rollenrechte und Umfang mit schmalem Vertragstest erhalten. Explorer behält seinen Frageauftrag. | Umgesetzt: build_dispatch_prompt.py nennt Fehler/Regressionen; Dispatch 12 und native Creation 12 bestanden. Voll-Diff-Pflicht für Explorer verworfen: Frageauftrag bleibt. |
| A5 | Code-Change/Validation verlinken die bei ihrer Operation nötigen Shell-, Daten- und Ausgaberegeln. | Umgesetzt: Code Change/Validation verlinken Shell, Daten- und Ausgaberegeln. Paket-/Linktests bestanden; gezielte Routenproben bestanden, keine isolierte Linkkausalität. |
| A6 | Historischen Instruction-/Luna-Harness samt exklusiven Tests nach Consumerabgleich nicht exportieren; keine irreführenden aktuellen Testlinks. | Umgesetzt: suite.json verweist auf aktuelle Buildtests; export_suite.py schließt alte Harnesspfade, drei exklusive Tests und unbenutzte capabilities.md aus. Consumerabgleich und 3 Exporttests bestanden; kanonische Historie unverändert. |
| A7 | Skillwriter-Standardprompt lädt Creator nicht durch unbedingte Mention; Strukturprüfung nur für Skillpakete. | Umgesetzt: default_prompt ohne Creator-Mention; Strukturprüfung nur für Skillpakete. Native Mention-Doku geprüft; Ursache des früheren Modellverhaltens bleibt unbewiesen. |
| A8 | Profilzahlen, technische Kompatibilität, Dokumentationsindex und öffentliche Planlinks sind zutreffend. | Umgesetzt: sechs General-/neun Codex-Skills, tatsächliches Testprofil und Claude-Grenze in README-Ownern; irreführender Zusatz auch aus Code/Handoff/UI-Metadaten entfernt. 12 README-Tests bestanden; beide Exportprofile valide. |
| A9 | Shared-Ausgabetest prüft seinen tatsächlichen Owner; vollständig übersprungene Testpfade sind EMPTY. | Umgesetzt: Shared-Test prüft acht tatsächliche Codex-Output-Consumer; check_all.py trennt ausgeführt/übersprungen und EMPTY. 6 Shared- und 9 Gate-Tests bestanden. |
| A10 | Shell-Owner erinnert an ausreichende PowerShell-JSON-Serialisierungstiefe. | Umgesetzt: shared/prompting/shell-commands.md nennt ausreichende ConvertTo-Json-Tiefe und Standardtiefe 2. |
| A11 | UI-Konsistenzaudit verwendet Nachweisarten statt entfallener Stufen. | Umgesetzt: ui-consistency-audit.md verlangt die Nachweisarten aus Validation. |
| A12 | WordPress-Validation und reine Interaktionsnachweise folgen bedingtem Router ohne unnötige Quality-Lektüre. | Umgesetzt: WordPress-Validation bedingt; ui-interactions.md bewahrt eigenständige Mindestregel ohne unbedingten Quality-Load. |
| A13 | Ask-Claude-Auftrag besitzt einen auflösbaren Ausgaberegelpfad. | Umgesetzt: ask.py liefert absoluten output_delivery_rules-Pfad; relocatable Vertragsprüfung in 55 bestandenen Ask-Tests. |
| A14 | Ausgaberegeln nennen assigning agent; Fallbacks verlinken tatsächliche Owner. | Umgesetzt: output-delivery.md nennt assigning agent; check_text_size-Fallback verlinkt die installierten Owner. |
| A15 | Unbenutzte Templateflags und zwei verwaiste Workflow-README-Fragmente entfernen. | Umgesetzt: ungenutztes template-Flag und zwei verwaiste README-Fragmente nach Consumerabgleich entfernt; Paket-, Runtime-, Lifecycle- und README-Tests bestanden. |
| A16 | Rohhashes und normalisierte Belege anhand ihrer tatsächlichen Verträge bei CRLF prüfen; nur reproduzierte Fehler korrigieren. | Umgesetzt nach CRLF-Reproduktion: Shared-Textprovenienz und zwei CI-Textassets normalisiert; Python-LF-Attribute ergänzt. Rohe Manifestidentität und Binär-/Remote-Artefaktbytes bleiben unverändert. LF/CRLF-Gegenfälle bestanden. |
| A17 | Gemeinsam kopierter Planvalidator verweist eindeutig auf Scoville Plan statt eine fehlende Workflow-Datei. | Umgesetzt: Planvalidator nennt Scoville Plan; 124 Tests ausgeführt und bestanden, 1 bestehender Skip. |
| A18 | Reviewscope auch ohne Diff; umliegende Idiome und ausdrückliche Autorisierung erhalten. | Umgesetzt: shared/code-review.md umfasst Audits ohne Diff; Code bewahrt umliegende Idiome und ausdrücklich autorisierten Entscheidungsraum. |
| A19 | Autorenroute verlinkt Goal-Lifecycle; ADR-Bereinigung schützt andere nichtterminale Pläne. | Umgesetzt: authoring.md verlinkt Goal-Lifecycle; beide Pflegequellen schützen nichtterminale Pläne; Plan-Tests bestanden. |
| B1 | Nur betroffene erhaltene ADRs mit datiertem Revisionsvermerk, Inhalt und historische Bereinigung bleiben. | Umgesetzt: Revisionsnotiz nur in zwölf erhaltenen, im Cleanup geänderten ADRs; keine gelöschten Records gelesen. Recordvalidierung bestanden. |
| B2 | Neutraler menschlicher manueller Weg für Sonderstufen; Agenten bleiben beim Helper. | Umgesetzt: menschlicher manueller Sonderstufenweg in Setup/Ask; 20 Setup-Tests bestanden. Agenten verwenden weiter Helper. |
| B3 | Gelöschte ADRs weder wiederherstellen noch erneut prüfen. | Bindende Ausschlussgrenze. |
| B4 | Folgeplan und verlinkte Records öffentlich, sensible Inhalte vorlegen, bestehender Validator, neue Pushfreigabe. | Umgesetzt in ADR-0225 und Suite-AGENTS.md; Export/Planvalidator und Fundprüfung bestanden; Freigabe „alles pushen“ erhalten und Veröffentlichung verifiziert. |
| B5 | Unveränderten Code-Testkatalog als historische PLAN-0034-Evidenz kennzeichnen. | Umgesetzt: members/scoville-code/development/README.md kennzeichnet den bytegleich erhaltenen PLAN-0034-Katalog als historisch. |

Bewusste General-/Codex-/Standalone-Unterschiede, dokumentierte Modelltestgrenzen
und die freigegebene private GitHub-Publikationsprüfung sind keine neuen Defekte.
Historische Evidenz darf alte Links behalten; falls nötig genügt eine Kennzeichnung
an ihrer bestehenden Dokumentation, ohne die Evidenz umzuschreiben.

Die Revisionen betreffen ADR-0047, 0061, 0089, 0118, 0120, 0136, 0142, 0148, 0153, 0199, 0211 und 0224. Die Auswahl folgt ausschließlich dem Diff der heute erhaltenen Dateien; inhaltliche Entscheidungen bleiben unverändert.

## Beobachtete Wirkung und Grenzen

14 frische native Empfänger mit nachgewiesenem `gpt-6.1-sol` / `low` prüften ausschließlich die geänderten A1/A2/A5-Auslöser und A4. Die 81 angeforderten Datei-Lektüren waren vollständig enthalten. Kein Claude-Lauf.

| Gruppe | Beobachtung | Grenze |
| --- | --- | --- |
| A1, fünf Skills | Writing und Datenregeln vor dem angeforderten Producer/Helper; vollständige Auswertung, kein Rohberichtsdump. | Plan/UI/Cleanup forderten vorher kleine Dateiinventare an. Plan rief den wiederholbaren Producer zweimal auf. |
| A2, sechs Skills inklusive Setup | Writing geladen; unbelegte Korrektur anhand des Fixturevertrags zurückgewiesen. | Keine Probe für berechtigte Nutzerkorrekturen; Plan las unnötig Dateilänge. |
| A5, zwei Code-Fälle | Exit 7 trotz späterer Fortschrittsausgabe erhalten; alle 1200 Checks ausgewertet, Fehler 701 gefunden. | Kleine Inventare vor Datenregel; Writing lud mit, daher kein isolierter Kausalitätsnachweis der Links. Change-Link nur strukturell geprüft. |
| A4, ein Reviewer | Echtes unverändertes Helper-Assignment; unabhängige Versandregression trotz voreingenommenem Fokus im vollständigen Step-Diff erkannt; changes_requested, keine Tests gestartet. | Kleine isolierte Regression; keine allgemeine Trefferquote oder Explorer-Laufabnahme. |

Die gezielten Proben bestehen; vollständige Regelbefolgung aller Läufe ist ausdrücklich nicht belegt. Daraus werden keine zusätzlichen Verbote oder neue Infrastruktur abgeleitet. Originalaufträge, vollständige Traces und Modellnachweise bleiben private Laufprotokolle.

Ein unabhängiger Sol/high-Quellenreview prüfte die geänderten Owner und Consumer auf Autorisierung, Aktivierung, Widersprüche, Rollenrechte, vollständige Übergaben und Buildverträge. Drei verbliebene General-Kompatibilitätsangaben wurden korrigiert und eng nachgeprüft; keine offenen belastbaren Quellenbefunde.

Der vorbereitete Runtime-Kandidat besteht lokal mit 23 Tests unter Windows/Python 3.14.3. Die neue private Actions-Matrix 40910346436 besteht 6/6 auf Windows, Linux und macOS mit Python 3.11/3.x. check_all.py besteht mit 12 Prüfgruppen, 0 Fehlern und 2 explizit leeren Python-Testpfaden; 7 bestehende optionale Skips bleiben ausgewiesen. Alle vier Paketvarianten bestehen Struktur- und Veröffentlichungsgate; beide Quellprofile bestehen den Planvalidator mit 0 Fehlern/0 Warnungen.

## Öffentlicher Umfang

Neu öffentlich sind dieser Befundabgleich, PLAN-0058 und ADR-0225. Die zwölf Revisionsnotizen ergänzen bereits veröffentlichte ADRs. PLAN-0057, seine Audits, nicht verlinkte private Audits und Modellrollouts bleiben ausgeschlossen. Die neuen Texte wurden vollständig auf Zugangsdaten, persönliche Pfade und Drittnamen gelesen; keine solchen Funde. Eine ergänzende Pfad-/Secretmustersuche ergab ebenfalls keine Treffer.

Online bleiben aufgelöste Paketblöcke, private Testdaten und die fehlende Shared-Geschwisterstruktur Grenzen. Der öffentliche Plan samt verlinkten Records ermöglicht Fortsetzung innerhalb dieser Grenzen, keine vollständige Gleichheit aller Entwicklungsprüfungen.

## Veröffentlichung

Freigabe: ausdrückliches „alles pushen“ am 2026-10-29 nach der Rückfrage zur privaten CI-Matrix. Veröffentlicht wurden ausschließlich main-Stände von scoville-suite, scoville-suite-for-codex-mainloop, scoville-code, scoville-handoff, scoville-plan, scoville-ui, scoville-skillwriter und scoville-ask-for-codex. Acht Remote-Commits, Dateiinventare und Git-Blobinhalte stimmen mit den geprüften Distributionen überein; alle acht Repos bleiben öffentlich. Die kanonischen Quellen wurden nicht direkt auf ihren öffentlichen Origin gepusht; veröffentlicht wurden ausschließlich gefilterte Exporte. Keine lokale Installation, Tags oder Releases.

Alle A1–A19 wurden im bestätigten Umfang umgesetzt. Verworfen wurden ausschließlich die weitergehende Voll-Diff-Pflicht für Explorer und eine Normalisierung der exakten Manifest-/Binäridentität. B1, B2, B4 und B5 umgesetzt; B3 als Ausschlussgrenze eingehalten. Die beschriebenen Modell- und Online-Grenzen bleiben offen ausgewiesen, ohne zusätzliche Nutzerentscheidung.
