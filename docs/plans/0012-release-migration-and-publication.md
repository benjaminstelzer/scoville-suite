---
format_version: 1
id: PLAN-0012
status: active
created: 2026-09-25
updated: 2026-09-26
current_item: W-009
---

# Scoville und private Skills konsistent migrieren und veröffentlichen

## Goal

Die finalen Scoville-Pakete und privaten `benjaminstelzer-*`-Skills werden ohne Namens-, Rollen-, Build-, Dokumentations- oder GitHub-Drift migriert und veröffentlicht. Allgemeine und Codex-Ausgabe behalten ihre unterschiedlichen Installations- und Python-Verträge.

## Non-goals

- Keine Veröffentlichung vor vollständiger Abnahme von PLAN-0011 und den Releasegates. Lokale Vorbereitung ist gemäß ADR-0069 vorgezogen.
- Keine Wiederholung abgeschlossener Skillimplementierungen oder Modellprüfungen ohne geänderte relevante Bytes.
- Keine Veröffentlichung fremder privater Quellen oder Änderung unbeteiligter Repositories.
- Keine Teilinstallation als unterstützter Suite-Modus.

## Work items

### W-001 Finalen Quellen- und Veröffentlichungsumfang festlegen

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0069]
Outcome: Ein belegter Abgleich benennt den finalen Quellenstand, alle Veröffentlichungsziele sowie aktuelle, umbenannte und abgelöste Skill-IDs ohne Doppelbesitz.
Acceptance: Die offenen Punkte von PLAN-0011 sind als Veröffentlichungssperren dokumentiert. Kanonische Quellen, lokale Installationen, Suite-Manifeste, Release-Staging, GitHub-Repositories und das Audit `docs/release-preflight-audit-2026-09-25.md` sind gegen denselben Stand geprüft. Die Zuordnung nennt für jedes Ziel Quelle, Profil, Paket-ID, Repository, Sichtbarkeit, Version, Nachfolger und wiederverwendbare oder veraltete Evidenz. Ungeklärte Abweichungen blockieren abhängige Arbeit.
Steps:
1. Prüfe `PROJECT_INDEX.md`, PLAN-0011 und seine vorhandenen Nachweise; bewahre die offenen Punkte W-001 und W-002 und erfasse ihre Abnahmen als Veröffentlichungssperren.
2. Inventarisiere `suite.json`, `packages/`, `<workspace-root>/skills/private/`, lokale Skillinstallationen und die Live-Repositories von `benjaminstelzer` und ordne jeden aktuellen oder historischen Skill genau einem Ziel zu.
3. Gleiche frühere Evidenz aus PLAN-0002 und PLAN-0006 bis PLAN-0011 mit den finalen relevanten Bytes ab; übernimm nur weiterhin gültige Nachweise und halte offene Releasegates fest.
Evidence: [2026-09-25: Quellen und Live-Ziele in docs/release-inventar-2026-09-25.md erfasst; offene Abnahmen bleiben Releasegates., 2026-09-25: Nutzer nimmt ADR-0070 an; vier Altmitglieder ersatzlos ausmustern und erst beim Release privat setzen., General und Codex check-packages gegen plan-0011-w025-final bestanden; Quellenzuordnung und Nachweisgrenzen im Releaseinventar., 2026-09-25: Fünf Ask-Alt-IDs gelten nur für lokale Upgrade-Bereinigung; frühere skills/public-Kopien sind weder Releasequelle noch Ziel.]

### W-002 Aktivierung, Zuständigkeiten und Familienbeziehungen stimmen überein

Status: done
Depends on: [W-001]
Blocked by: []
Decisions: [ADR-0069]
Outcome: Jeder aktuelle Skill hat eindeutige Auslöser, Zuständigkeiten und Übergaben; Familienverweise entsprechen dem gewählten Distributionsprofil.
Acceptance: Standalone-Pakete behandeln fehlende oder inaktive optionale Geschwister korrekt und simulieren keinen fremden Skill. General- und Codex-Suite verlangen alle Mitglieder ihres jeweiligen Profils und enthalten keine Logik für optionale Familienmitglieder. Explizite Aktivierungen, Nutzer-Ausschlüsse, Workflow- und Ask-Grenzen sowie selektives Laden bleiben erhalten. Manifestprojektionen und vollständige Skillquellen widersprechen sich nicht.
Steps:
1. Prüfe alle aktuellen `members/*/*/SKILL.md`, ihre geladenen Referenzen und die Familienmetadaten in `suite.json` auf Aktivierung, Ausschluss, Besitzer, Übergabe und Nachbarschaft.
2. Prüfe drei eindeutige Projektionen gegen ihren Familienvertrag: Standalone-Pakete mit optionalen Familienmitgliedern sowie General- und Codex-Suite mit vollständiger Pflichtmitgliedschaft ihres jeweiligen Profils; entferne nur veraltete Beziehungen und ergänze fehlende eindeutige Übergaben an ihren kanonischen Besitzern.
3. Ergänze gezielte Vertragsfälle für mehrdeutige Auslöser, fehlende Standalone-Geschwister und unvollständige Suite-Installationen; prüfe die finalen Projektionen.
Evidence: [2026-09-25: Familienverträge geprüft; acht Suite- und vier Profiltests unter Windows/Python 3.14 bestanden; Grenzen in docs/release-inventar-2026-09-25.md.]

### W-003 Scoville-Namen und abgelöste Pakete sind lokal driftfrei vorbereitet

Status: done
Depends on: [W-001, W-002]
Blocked by: []
Decisions: [ADR-0069, ADR-0070]
Outcome: Aktuelle Scoville-Skills verwenden das freigegebene Namensschema ohne `anti-ai-slop`; abgelöste Pakete haben eindeutige Nachfolger und keine aktive Quelle mehr.
Acceptance: Skill-IDs, Quell- und Paketverzeichnisse, Manifestwerte, interne Links, Installationspfade, Changelogs und GitHub-Zielnamen stimmen überein. `scoville-ui` ersetzt die beiden alten UI-Pakete. `scoville-ask-for-codex` ersetzt die fünf Ask-Varianten. Die endgültige Deprecated-Liste ist belegt und trennt Umbenennung, Zusammenführung und ersatzlose Stilllegung. Historische Plan- und Evidenzdateien bleiben unverändert lesbar.
Steps:
1. Erstelle aus W-001 die verbindliche Altname-zu-Ziel-Zuordnung und prüfe Zielkollisionen auf lokalen Pfaden und GitHub.
2. Benenne nur aktuelle kanonische Quellen und ihre Manifest-, Paket-, README-, Link- und Testverbraucher um; erhalte historische Aufzeichnungen und Git-Historie.
3. Prüfe den vollständigen aktiven Quellenbaum auf veraltete IDs und klassifiziere jeden verbleibenden Treffer als aktive Migration, historische Evidenz oder Fehler.
Evidence: [2026-09-25: Code lokal umbenannt; Profile gebaut und Paketkopien abgeglichen; acht Suite- und fünf Familientests grün; Nachweise und Validatorgrenze im Releaseinventar.]

### W-004 Private Benjamin-Skills haben einen gemeinsamen lokalen und privaten GitHub-Vertrag

Status: done
Depends on: [W-001]
Blocked by: []
Decisions: [ADR-0069]
Outcome: Die privaten `benjaminstelzer-*`-Quellen liegen unter einem gemeinsamen Elternordner und entsprechen ihren privaten GitHub-Repositories.
Acceptance: `benjaminstelzer-github-skill`, `benjaminstelzer-imitate-me-skill` und `benjaminstelzer-skillwriter-skill` liegen mit erhaltener vorhandener Git-Historie unter `<workspace-root>/skills/private/benjaminstelzer/`. Git-Roots, lokale Änderungen, Historie und Verbraucherpfade bleiben erhalten. Paket- und Repository-Namen folgen dem freigegebenen Schema. Fehlende private Repositories sind als konkrete Veröffentlichungsziele vorbereitet; keine private Quelle wird öffentlich.
Steps:
1. Prüfe die zwei bestehenden Git-Roots sowie den bisher nicht versionierten Skillwriter-Quellordner und alle Verbraucher ihrer bisherigen Pfade; bewahre Arbeitsstände und vorhandene Historie.
2. Verschiebe die vollständigen Quellverzeichnisse nach `<workspace-root>/skills/private/benjaminstelzer/` und aktualisiere ausschließlich belegte Workspace-, Build-, Test- und Dokumentationsverweise.
3. Vergleiche jedes kanonische Paket vollständig mit seinem privaten GitHub-Ziel und bereite fehlende oder abweichend benannte Ziele unter Erhalt der Sichtbarkeit und Historie vor.
Evidence: [2026-09-25: Drei Quellen verschoben; 275 Dateien einschließlich Git bytegleich erhalten; Remote-Paketdifferenzen und private Ziele im Releaseinventar dokumentiert.]

### W-005 Buildprofile und Python-Verträge gelten für die finalen Namen und Pakete

Status: done
Depends on: [W-003]
Blocked by: []
Decisions: [ADR-0069]
Outcome: Der Builder erzeugt aus den finalen Quellen reproduzierbare Standalone-, General- und Codex-Pakete mit korrekter Mitgliedschaft und Laufzeitlogik.
Acceptance: Manifest, gemeinsame Helper, Fragmente, Paketinventare, Quellenhashes und isolierte Exporte stimmen je Profil überein. General enthält nur die vorgesehenen bedingt geladenen Python-Ersatzrouten. Codex verlangt Python und die vorgesehenen Helper und enthält keine manuellen Python-Ersatzwege. Ein vorhandener fehlerhafter Helper fällt nicht still auf manuelle Ausführung zurück. Ask behält seine Modellabfrage und den festgelegten Claude-CLI-Weg. Reproduzierbarkeit, Links, LF-Textausgabe und vollständige Profilinstallation sind geprüft.
Steps:
1. Prüfe `suite.json`, `development/build_suite.py`, `development/shared/build/build_suite.py` und die kanonischen Profilfragmente gegen die finalen Namen und Mitgliedschaften.
2. Baue alle vorgesehenen Layouts im einzigen Release-Staging unter `<workspace-root>/skills/temp/release/`; prüfe Receipt, Inventar, Quellenhashes, Links und isolierten Wiederaufbau.
3. Führe die relevanten General-ohne-Python-, Codex-Helperfehler- und Vollinstallationsfälle auf den finalen Paketbytes aus; trenne fachliche Fallbacks von Python-Ersatzrouten.
Evidence: [2026-09-25: Vier Layouts und LF geprüft; 53 Shared-Tests grün; gebaute Helfer melden Fehler korrekt; Prüfgrenzen und Profilverträge im Releaseinventar.]

### W-006 Suite-Installation entfernt alte Skillvarianten kontrolliert

Status: done
Depends on: [W-005]
Blocked by: []
Decisions: [ADR-0069, ADR-0070]
Outcome: General- und Codex-Installation entfernen eindeutig abgelöste Skillverzeichnisse vor der vollständigen Installation und verhindern Doppelaktivierungen.
Acceptance: Die Migration gleicht die exakten Alt-IDs aus `docs/release-preflight-audit-2026-09-25.md` erneut mit finalen Manifesten und veröffentlichten Altanleitungen ab. General entfernt nur seine früher installierbaren Scoville-Mitglieder. Codex behandelt zusätzlich `scoville-workflow-for-codex`, den bedingten Altnamen `scoville-workflow-codex` und alle fünf Ask-Varianten. Nur vorhandene eindeutig zugeordnete Verzeichnisse werden entfernt. Persönliche Anpassungen werden vorab erkannt und erhalten oder als notwendige Migration gemeldet. Danach werden alle Mitglieder des gewählten Profils installiert und ihre Erkennung geprüft.
Steps:
1. Erzeuge aus der belegten W-001-Zuordnung profilbezogene Altlisten und gleiche jeden Eintrag mit der GitHub-Momentaufnahme sowie dem finalen Nachfolger ab.
2. Ergänze die kanonischen Installationsfragmente um einen kopierbaren Migrationsprompt mit Bestandsprüfung, Anpassungsschutz, genauer Entfernung und vollständiger Neuinstallation.
3. Prüfe General- und Codex-Migration in isolierten Skill-Verzeichnissen mit alten, gemischten, angepassten und bereits aktuellen Zuständen; belege fehlende Doppelinstallationen und vollständige Discovery.
Evidence: [2026-09-25: Nutzer verlangt einfache Deinstallationsliste mit Überspringen fehlender Skills; Prompt entsprechend gekürzt., Acht isolierte Dateimigrations- und echte Discoveryfälle bestanden am vorherigen Entwurf; finaler Kurzprompt noch profilbezogen zu prüfen., Nutzerkorrektur: Auch persönliche Einstellungen der entfernten Installationen löschen; keine Sicherung oder Migration oder Fallback-Kopie., Endprojektionen bestanden; isolierte Löschprüfung vor Prozessstart automatisch mit blocked by policy abgewiesen., Nutzerkorrektur: W-006 liefert den Auftrag an den später installierenden Agenten; keine manuelle Deinstallation der aktuellen Installation und kein Host-Blocker daraus., Frische General- und Codex-Projektionen geprüft: neun gemeinsame und sieben zusätzliche Codex-Alt-IDs sowie vollständige Deinstallation ohne Sicherung und frische Installation; LF-only., Prompt auf zwei Anweisungen plus Listen reduziert; General nennt Python 3.10+ optional und Codex Python 3.11+ samt Paketmanager oder offiziellem Installer., Abschließende Nutzerkorrektur: Codex verwendet sein integriertes Python 3.11+ ohne manuellen Installationsweg; Projektionen stimmen.]

### W-007 READMEs sprechen mit einer Stimme und erklären den finalen Stand

Status: done
Depends on: [W-003, W-004, W-005]
Blocked by: []
Decisions: [ADR-0069]
Outcome: Private Skills, Scoville-Mitglieder und Suite-READMEs sind innerhalb ihrer Gruppe konsistent und erklären Namen, Voraussetzungen, Installation und Grenzen in Benjamins Stimme.
Acceptance: Kanonische Fragmente und private README-Quellen sind mit `benjaminstelzer-imitate-me` geprüft. Eingefügte Textbausteine passen zum umgebenden Dokument und widersprechen keinem Paketprofil. Namen, Links, Beispiele, Python- und Hostvoraussetzungen, Migrationsprompt, Familienrollen und Ask-Einzelinstallation sind sachlich korrekt. Generierte READMEs stimmen mit ihren Quellen überein. Historische Release-Texte werden nicht umgeschrieben.
Steps:
1. Prüfe die finalen kanonischen README-Fragmente aller Scoville-Mitglieder und Suites sowie die READMEs unter `<workspace-root>/skills/private/benjaminstelzer/` auf Fakten, Gruppenkonsistenz und Einbettung gemeinsamer Bausteine.
2. Überarbeite nur die betroffenen Quellen mit `benjaminstelzer-imitate-me`; erhalte Anforderungen, Grenzen, Installation und technische Identifikatoren.
3. Erzeuge alle Projektionen über den Builder und prüfe vollständige Dokumente, Links, Beispiele, Gruppenterminologie und Abwesenheit veralteter aktiver Namen.
Evidence: [README-Arbeit unabhängig von der gesperrten Löschprüfung vorgezogen; W-006 bleibt direkte Voraussetzung von W-008., Sieben Mitglieds- und drei private READMEs geprüft; vierzehn README-Tests grün; beide Profile gebaut; Generatorkopien synchronisiert.]

### W-008 Releasekandidaten und Executables sind aus demselben finalen Stand belegt

Status: done
Depends on: [W-006, W-007]
Blocked by: []
Decisions: [ADR-0069]
Outcome: Alle Releasepakete, Plan-Viewer-Executables, Installer und Checksummen stammen aus dem finalen freigegebenen Quellenstand und sind ihren Zielreleases eindeutig zugeordnet.
Acceptance: Finale Versionen, Changelogs, Tags, Pakete und Releaseziele sind widerspruchsfrei. Der Plan Viewer wird für alle vorgesehenen Plattformvarianten neu gebaut. Scoville Plan und Scoville Suite erhalten die nach ihrem Assetvertrag erforderlichen Executables, Installer und Checksummen. Verifizierte Builds sind in alle von W-001 inventarisierten regulären lokalen Ausgabeziele synchronisiert; Inventare und Hashes stimmen überein. Nur obsolete generierte Dateien sind entfernt, während Quellen, persönliche Anpassungen und Git-Historie erhalten bleiben. Artefakttests und lokale Prüfsummen bestehen. Kein Asset einer älteren Quelle wird als neuer Build ausgegeben.
Steps:
1. Friere nach W-007 den finalen Quellenstand und die Zielversionen ein; prüfe Changelogs, Releasegates und Assetzuordnung je Repository.
2. Baue die vorgesehenen Plan-Viewer-Plattformartefakte aus `members/scoville-plan/development/viewer/` über den kanonischen Buildweg neu und erzeuge die zugehörigen Checksummen.
3. Synchronisiere die verifizierten Builds in alle von W-001 inventarisierten regulären lokalen Ausgabeziele; vergleiche Inventare und Hashes, entferne ausschließlich obsolete generierte Dateien und erhalte Quellen, persönliche Anpassungen und Git-Historie.
4. Prüfe Releasepakete und Executables lokal auf Version, Plattform, Startbarkeit soweit vorgesehen, Paketinhalt und Prüfsumme; stelle den vollständigen Uploadsatz je Zielrelease bereit.
Evidence: [2026-09-25: Viewer v1.3.3 und vier Plattformziele samt gemeinsamem SHA256SUMS.txt statisch geprüft; npm ci sowie npm run check und npm run build grün., 2026-09-25: Kandidatenversionen und direkte profilbezogene GitHub-Installationslinks im Releaseinventar festgelegt; native Rust- und GitHub-Matrix-Builds stehen aus., 2026-09-25: General mit 4 Mitgliedern und 63 Dateien sowie Codex mit 7 Mitgliedern und 111 Dateien frisch gebaut; Receipt- Quellen- Helper- und LF-Prüfungen grün., 2026-09-25: 187 fokussierte Tests grün; git diff --check sowie native Planprüfung mit 0 Fehlern und 0 Warnungen bestanden., 2026-09-25: Vier Buildlayouts samt Standalone-Zielen receipt-genau und LF-only; Builder normalisiert nun auch Receipts und alle sieben `packages/`-Projektionen sind bytegleich., 2026-09-25: Alle vier Kandidaten nennen Commit 10cd737b62c12536310124bc243248fd98b15285 und source_dirty false; Paket- Release- und Helperprüfungen bestanden., 2026-09-25: Nach portabler Pfadkorrektur nennen alle vier neu gebauten Kandidaten eba97cbccfc580394ebbe1b1390b45893833cb28 und source_dirty false; alle drei Prüfungen je Ziel grün., 2026-09-25: Origin main ist 15 Commits zurück und enthält keinen Plan-Viewer-Workflow; die GitHub-Matrix erfordert den vor PLAN-0011 gesperrten öffentlichen Push., 2026-09-25: Viewer-Lauf 36175688109 auf 08bf750 bestand alle vier Plattformjobs und den Checksummenjob; elf heruntergeladene Artefakte stimmen mit SHA256SUMS.txt überein., 2026-09-25: Portabilitätslauf 36178096054 auf d6096a4 bestand alle sechs Windows- Ubuntu- und macOS-Jobs mit Python 3.11 und aktuell., 2026-09-25: Vier Kandidaten aus 19a91cb mit source_dirty false gebaut; Paket- und Helperprüfungen bestanden., 2026-09-25: Suite-Exporte mit 547 und 705 Dateien stimmen vollständig mit ihren Export-Receipts überein., 2026-09-25: Windows-Viewer 1.3.3 startete lokal; Linux und macOS sind durch die erfolgreichen nativen Buildjobs belegt., 2026-09-25: Nutzer korrigiert den Installationsvertrag; W-012 trennt Neuinstallation und vollständige Bereinigung früherer Scoville- oder Ask-Suites., 2026-09-25: Gelöschtes Release-Staging wird aus dem finalen sauberen Quellenstand vollständig neu erzeugt., 2026-09-25: ADR-0073 hält docs und development öffentlich; 30 Quelltexte nutzen neutrale Pfade und der Quellbaumtest ist grün., 2026-09-25: Aktive Ask-Texte verwenden konsistent Ask; ASK bleibt nur als markierter Legacy-Titel oder historisches Literal erhalten., 2026-09-25: Vier Kandidaten aus 234ea1b melden source_dirty false; Paket- und Helperprüfungen sind grün., 2026-09-25: Exporte mit 550 und 708 Dateien sind receipt-genau und die Public-Ziele stimmen exakt; maschinenspezifische Pfade fehlen., 2026-09-25: Elf Viewer-Artefakte stimmen mit SHA256SUMS.txt überein; beide Exportprofile bestehen die Planprüfung mit 0 Fehlern und 0 Warnungen.]

### W-012 Bereinigung früherer Suites und Neuinstallation sind getrennt erklärt

Status: done
Depends on: [W-006, W-007]
Blocked by: []
Decisions: [ADR-0071]
Outcome: Nutzer erhalten zuerst eine kurze Neuinstallationsanleitung und danach einen getrennten Upgrade-Auftrag für frühere Scoville- oder Ask-Suites.
Acceptance: Beide Profil-READMEs zeigen die Neuinstallation vor dem Upgrade. Der Upgrade-Auftrag entfernt alle bekannten früheren Scoville-Suite-IDs und die fünf Ask-IDs samt Einstellungen sofern vorhanden; fehlende Einträge werden übersprungen und fremde Skills bleiben erhalten. Danach installiert er das gewählte vollständige Profil direkt aus dessen GitHub-Repository. Isolierte Prüfungen belegen die vollständige Liste und verhindern profilabhängiges Auslassen der Ask-IDs.
Steps:
1. Überarbeite `development/readme/suite-install.md` und `docs/release-preflight-audit-2026-09-25.md` gemäß ADR-0071 zu getrennten Anleitungen mit einer gemeinsamen vollständigen Alt-ID-Liste.
2. Ergänze `development/tests/test_build_suite.py` um General- und Codex-Prüfungen für Reihenfolge vollständige Alt-ID-Liste Einstellungen fehlende Einträge und direkte Repository-Installation.
3. Erzeuge alle README-Projektionen neu und prüfe beide Profile sowie die Abwesenheit rechnerbezogener Pfade in ausgelieferten Nutzertexten.
Evidence: [2026-09-25: General- und Codex-README trennen Neuinstallation und Upgrade; beide enthalten exakt 16 Alt-IDs samt fünf Ask-IDs und die direkte Profil-URL., 2026-09-25: Neun Suite- und vier kanonische Profiltests grün; README-Projektionen aktuell und Hostpfadprüfung grün.]

### W-013 Prioritized after W-012: Suite-Übersicht erklärt die Nutzung jedes Skills

Status: cancelled
Depends on: [W-012]
Blocked by: []
Decisions: []
Outcome: Jede Suite-Übersicht zeigt für jedes enthaltene Mitglied einen konkreten kurzen `How to use`-Abschnitt; die Codex-Ausgabe erklärt auch den expliziten Workflow-Aufruf.
Acceptance: Die General-README enthält vier und die Codex-README sieben memberbezogene `How to use`-Abschnitte. Jeder Abschnitt stammt aus der kanonischen Nutzungsquelle des Mitglieds und enthält mindestens einen konkreten Aufruf oder eine konkrete Bedienanweisung. Vollständige Konfigurations- und Spezialhinweise bleiben in der verlinkten Einzel-README. Tests prüfen Anzahl Reihenfolge Profilmitgliedschaft und den Workflow-Aufruf.
Steps:
1. Prüfe die vorhandenen Nutzungsfragmente und `suite.descriptions` in `suite.json` sowie `development/shared/build/build_suite.py`; bestimme den kurzen kanonischen Teil vor dem ersten Nutzungs-Unterabschnitt.
2. Erweitere die Suite-Komposition um diesen kurzen `How to use`-Teil ohne eine zweite Textquelle und erhalte die vollständigen Einzel-READMEs.
3. Ergänze gezielte General- und Codex-README-Tests und erzeuge alle Projektionen neu.
Evidence: [2026-09-25: Nutzer ersetzt eingebettete Nutzungstexte durch direkte Links zur vollständigen README; der begonnene Einbettungsentwurf wurde nicht übernommen.]

### W-014 Prioritized after W-013: Suite-Übersicht verlinkt die Nutzung jedes Skills

Status: done
Depends on: [W-012]
Blocked by: []
Decisions: []
Outcome: Jede Skillbeschreibung der Suite-Übersicht führt kompakt zum `How to use`-Abschnitt ihrer vollständigen README.
Acceptance: Die General-README enthält vier und die Codex-README sieben eindeutige memberbezogene Links auf vorhandene `README.md#how-to-use`-Ziele. Der Workflow-Link steht in der Codex-Suite bei Scoville Workflow for Codex. Keine Nutzungsanleitung wird in der Übersicht dupliziert. Link- und Profiltests bestehen.
Steps:
1. Ergänze `suite.descriptions` in `development/shared/build/build_suite.py` um genau einen profilabhängigen relativen Link je Mitglied und prüfe das vorhandene `How to use`-Ziel der Mitglieds-README.
2. Ergänze `development/shared/tests/test_readme_templates.py` und `development/tests/test_build_suite.py` um Anzahl Zielauflösung Profilmitgliedschaft und Workflow-Link.
3. Synchronisiere die Shared-Projektion und erzeuge alle README-Projektionen neu.
Evidence: [2026-09-25: General enthält vier und Codex sieben direkte README.md#how-to-use-Links; Workflow steht in Codex an erster Stelle., 2026-09-25: Kanonischer Shared-Test gezielter Suite-Linktest und README-Projektionsprüfung grün.]

### W-015 Deferred after W-014: Workflow wird nicht mehr als Beta bezeichnet

Status: done
Depends on: [W-014]
Blocked by: []
Decisions: []
Outcome: Aktuelle Nutzertexte beschreiben Scoville Workflow for Codex ohne Beta-Kennzeichnung.
Acceptance: Suite-Einleitung Workflow-Beschreibung Manifestprojektionen und generierte General- oder Codex-READMEs enthalten keine aktuelle Beta-Kennzeichnung für Workflow. Historische Changelog-Einträge bleiben unverändert. Betroffene README- und Pakettests bestehen.
Steps:
1. Entferne die aktuelle Beta-Kennzeichnung aus `development/readme/suite-intro.md` und den kanonischen Workflow-README-Quellen sowie die zugehörige Manifestvariable in `suite.json`.
2. Passe ausschließlich Tests an die die aktuelle Beta-Projektion prüfen; erhalte historische Changelog-Texte.
3. Erzeuge README- und Paketprojektionen neu und prüfe aktive Nutzertexte auf verbleibende Workflow-Beta-Aussagen.
Evidence: [2026-09-25: Aktive Nutzertexte enthalten keine Workflow-Beta-Kennzeichnung; generierte Workflow-READMEs sind bytegleich und 14 Shared- sowie 10 Suite-Tests sind grün.]

### W-011 Prioritized after W-008: Gesamten finalen Release unabhängig prüfen

Status: done
Depends on: [W-008]
Blocked by: []
Decisions: [ADR-0069, ADR-0071, ADR-0073]
Outcome: Eine unabhängige Astra-Medium-Prüfung bestätigt den vollständigen finalen Releasekandidaten vor jeder GitHub-Veröffentlichung oder benennt konkrete Korrekturen.
Acceptance: Eine frische Astra-Aufgabe prüft Quellenstand, Releasepakete, Viewer-Artefakte, Checksummen, Releaseinventar und geplante GitHub-Mutationen read-only. Jeder Befund mit Auswirkung auf Korrektheit oder Veröffentlichung ist vor W-009 behoben und nachgeprüft; Ergebnis und Grenzen sind belegt.
Steps:
1. [execute: model=gpt-6-astra; reasoning=medium] Prüfe den vollständigen finalen Releasekandidaten und die geplanten GitHub-Mutationen unabhängig gegen PLAN-0012 und die weiterhin geltenden Releasegates.
Evidence: [2026-09-25: Nutzer bestätigt Übernahme von PLAN-0013 sowie Neubau und frische Astra-Medium-Prüfung., 2026-09-25: Vier Vorbereitungsbuilds und sieben Paketkopien geprüft; 74 Plan- und 55 Shared-Tests grün; Grenzen in docs/release-inventar-2026-09-25.md., Astra 01a0da87-3b50-7d13-862a-18aa35776db3 meldet zwei Befunde; 4162f42 korrigiert beide mit lokal geprüften Builds., Nutzer verzichtet gemäß ADR-0080 auf die zweite unabhängige Prüfung; keine weitere Astra-Abnahme behauptet.]

### W-009 GitHub-Ziele sind ohne Namens- oder Sichtbarkeitsdrift veröffentlicht

Status: in_progress
Depends on: [W-008, W-011]
Blocked by: []
Decisions: [ADR-0069, ADR-0070, ADR-0071, ADR-0073, ADR-0079, ADR-0080]
Outcome: Scoville-Skills, Suites und private Benjamin-Skills sind auf GitHub unter den freigegebenen Namen, Sichtbarkeiten und Versionen veröffentlicht.
Acceptance: PLAN-0011 ist nach beobachteten Abnahmen abgeschlossen und alle Releasegates sind erfüllt. Aktuelle Scoville-Repositories tragen die finalen Namen ohne `anti-ai-slop`. Die vier in ADR-0070 ausgemusterten Repositories sind privat. Private `benjaminstelzer-*`-Skills sind vollständig in privaten Repositories veröffentlicht. Branches, Tags, Releases, Beschreibungen, Themen, Profil-README und Installationslinks stimmen mit den finalen Paketen überein. Releaseassets und Checksummen sind an den richtigen Releases vorhanden. Keine unbeteiligte Historie oder Sichtbarkeit wurde geändert.
Steps:
1. Führe für jedes aktuelle Ziel und die vier Repositories aus ADR-0070 den autorisierten GitHub-Preflight aus und vergleiche Branch, Schutz, Sichtbarkeit, Historie, aktuelle Releases, Tags, Themen und Zielnamen mit W-001 und W-008.
2. Veröffentliche die verifizierten Paketbäume und privaten Skills; benenne aktuelle Repositories um und setze ausschließlich die vier Repositories aus ADR-0070 privat. Erstelle die erforderlichen Releases und lade den zugeordneten Assetsatz hoch.
3. Aktualisiere das Profil und alle betroffenen öffentlichen Metadaten aus den finalen Namen und überprüften Installationswegen; bewahre bestehende unbeteiligte Einträge.
Evidence: [ADR-0082 Defaults umgesetzt und lokal installiert; Ask 23 Workflow 16 Setup 2 Tests bestanden; Codex-Paketprüfung bestanden]
Next action: Finalen Quellenstand committen und Exporte sowie Public-Ziele mit ADR-0082 neu erzeugen; danach Veröffentlichung fortsetzen.

### W-010 Remote-Ergebnis und Neuinstallation sind vollständig verifiziert

Status: todo
Depends on: [W-009]
Blocked by: []
Decisions: [ADR-0069, ADR-0071, ADR-0073, ADR-0079]
Outcome: GitHub und eine isolierte Neuinstallation entsprechen den finalen Quellen ohne alte oder doppelte Skillvarianten.
Acceptance: Remote-Dateibäume, Commit-IDs, Versionen, Tags, Releases, Assets, heruntergeladene Checksummen, Sichtbarkeiten, Repository-Namen, Profil-Links und Themen stimmen mit W-008 und W-009 überein. General- und Codex-Migrationsprompt werden gegen isolierte Altbestände ausgeführt. Danach ist jeder unverändert benannte aktuelle Skill genau einmal als verifizierte aktuelle Installation vorhanden; alle umbenannten oder entfallenen Legacy-IDs sind abwesend und alle Pflichtmitglieder vorhanden. Abweichungen gelten als Veröffentlichungsfehler und bleiben offen.
Steps:
1. Vergleiche jeden veröffentlichten Remote-Baum und Release mit dem zugehörigen Receipt, Commit, Tag, Assetinventar und lokalen Prüfsummen; lade Assets zur Identitätsprüfung erneut herunter.
2. Führe General- und Codex-Migration in getrennten isolierten Installationswurzeln mit repräsentativen Altbeständen aus; prüfe Discovery und die Entfernung der persönlichen Einstellungen aus den deinstallierten Altinstallationen ohne Sicherung oder Übernahme, für unverändert benannte Bestandsmitglieder jeweils genau eine aktuelle verifizierte Installation sowie die Abwesenheit aller umbenannten oder entfallenen Legacy-IDs.
3. Dokumentiere pro Repository und Suite den verifizierten Endstand sowie jede verbleibende Abweichung; schließe den Plan nur bei vollständiger Acceptance.
Evidence: []
Next action: Nach W-009 Remote-Bäume und Releaseassets gegen die lokalen Belege prüfen.


### W-016 Lokale Suites vor dem GitHub-Release vollständig neu installieren

Status: done
Depends on: [W-008]
Blocked by: []
Decisions: [ADR-0071]
Outcome: Codex verwendet die neue vollständige Codex-Suite und Claude die neue General-Suite aus den verifizierten Public-Ausgaben.
Acceptance: Alle bisherigen Scoville- und Ask-Skills in Codex sowie Scoville-Skills in Claude sind einschließlich alter Einstellungen entfernt. Codex enthält sieben und Claude vier neue Suite-Mitglieder bytegleich zu ihren geprüften Paketen; fremde Skills bleiben unverändert.
Steps:
1. Prüfe beide Public-Ausgaben gegen ihre Exportreceipts und ermittle die betroffenen globalen Installationen.
2. Deinstalliere die benannten Skillgruppen und installiere die vollständigen passenden Pakete aus skills/public/.
3. Vergleiche Dateiinventare und Hashes; prüfe verfügbare Discovery und kehre vor GitHub-Veröffentlichung zu W-011 zurück.
Evidence: [2026-09-25: Nutzer priorisiert reale Neuinstallation vor weiterem GitHub-Release für den Workflow im DIVI-5-Projekt., 2026-09-25: Automatische Hostprüfung verweigert Deinstallationsprozess vor Start mit blocked by policy; keine Installation oder Entfernung ausgeführt., 2026-09-25: Nutzer entfernt Altinstallationen; Abwesenheit vor Installation geprüft., 2026-09-25: Codex sieben und Claude vier Skills aus Public installiert; alle Dateien hashgleich; 107 beziehungsweise 27 fremde Dateien unverändert.]
