---
format_version: 1
id: PLAN-0012
status: active
created: 2026-09-25
updated: 2026-09-25
current_item: W-008
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
2. Inventarisiere `suite.json`, `packages/`, `E:/Dropbox/AI Projects/skills/private/`, lokale Skillinstallationen und die Live-Repositories von `benjaminstelzer` und ordne jeden aktuellen oder historischen Skill genau einem Ziel zu.
3. Gleiche frühere Evidenz aus PLAN-0002 und PLAN-0006 bis PLAN-0011 mit den finalen relevanten Bytes ab; übernimm nur weiterhin gültige Nachweise und halte offene Releasegates fest.
Evidence: [2026-09-25: Quellen und Live-Ziele in docs/release-inventar-2026-09-25.md erfasst; offene Abnahmen bleiben Releasegates., 2026-09-25: Nutzer nimmt ADR-0070 an; vier Altmitglieder ersatzlos ausmustern und erst beim Release privat setzen., General und Codex check-packages gegen plan-0011-w025-final bestanden; Quellenzuordnung und Nachweisgrenzen im Releaseinventar.]

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
Acceptance: `benjaminstelzer-github-skill`, `benjaminstelzer-imitate-me-skill` und `benjaminstelzer-skillwriter-skill` liegen mit erhaltener vorhandener Git-Historie unter `E:/Dropbox/AI Projects/skills/private/benjaminstelzer/`. Git-Roots, lokale Änderungen, Historie und Verbraucherpfade bleiben erhalten. Paket- und Repository-Namen folgen dem freigegebenen Schema. Fehlende private Repositories sind als konkrete Veröffentlichungsziele vorbereitet; keine private Quelle wird öffentlich.
Steps:
1. Prüfe die zwei bestehenden Git-Roots sowie den bisher nicht versionierten Skillwriter-Quellordner und alle Verbraucher ihrer bisherigen Pfade; bewahre Arbeitsstände und vorhandene Historie.
2. Verschiebe die vollständigen Quellverzeichnisse nach `E:/Dropbox/AI Projects/skills/private/benjaminstelzer/` und aktualisiere ausschließlich belegte Workspace-, Build-, Test- und Dokumentationsverweise.
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
2. Baue alle vorgesehenen Layouts im einzigen Release-Staging unter `E:/Dropbox/AI Projects/skills/temp/release/`; prüfe Receipt, Inventar, Quellenhashes, Links und isolierten Wiederaufbau.
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
1. Prüfe die finalen kanonischen README-Fragmente aller Scoville-Mitglieder und Suites sowie die READMEs unter `E:/Dropbox/AI Projects/skills/private/benjaminstelzer/` auf Fakten, Gruppenkonsistenz und Einbettung gemeinsamer Bausteine.
2. Überarbeite nur die betroffenen Quellen mit `benjaminstelzer-imitate-me`; erhalte Anforderungen, Grenzen, Installation und technische Identifikatoren.
3. Erzeuge alle Projektionen über den Builder und prüfe vollständige Dokumente, Links, Beispiele, Gruppenterminologie und Abwesenheit veralteter aktiver Namen.
Evidence: [README-Arbeit unabhängig von der gesperrten Löschprüfung vorgezogen; W-006 bleibt direkte Voraussetzung von W-008., Sieben Mitglieds- und drei private READMEs geprüft; vierzehn README-Tests grün; beide Profile gebaut; Generatorkopien synchronisiert.]

### W-008 Releasekandidaten und Executables sind aus demselben finalen Stand belegt

Status: in_progress
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
Evidence: [2026-09-25: Viewer v1.3.3 und vier Plattformziele samt gemeinsamem SHA256SUMS.txt statisch geprüft; npm ci sowie npm run check und npm run build grün., 2026-09-25: Kandidatenversionen und direkte profilbezogene GitHub-Installationslinks im Releaseinventar festgelegt; native Rust- und GitHub-Matrix-Builds stehen aus., 2026-09-25: General mit 4 Mitgliedern und 63 Dateien sowie Codex mit 7 Mitgliedern und 111 Dateien frisch gebaut; Receipt- Quellen- Helper- und LF-Prüfungen grün., 2026-09-25: 187 fokussierte Tests grün; git diff --check sowie native Planprüfung mit 0 Fehlern und 0 Warnungen bestanden., 2026-09-25: Vier Buildlayouts samt Standalone-Zielen receipt-genau und LF-only; Builder normalisiert nun auch Receipts und alle sieben `packages/`-Projektionen sind bytegleich., 2026-09-25: Alle vier Kandidaten nennen Commit 10cd737b62c12536310124bc243248fd98b15285 und source_dirty false; Paket- Release- und Helperprüfungen bestanden.]
Next action: Nach einem sauberen Commitbezug Viewer v1.3.3 über die GitHub-Matrix bauen; alle elf Plattformartefakte und `SHA256SUMS.txt` prüfen und erst danach die regulären lokalen Zielausgaben synchronisieren.

### W-009 GitHub-Ziele sind ohne Namens- oder Sichtbarkeitsdrift veröffentlicht

Status: todo
Depends on: [W-008]
Blocked by: []
Decisions: [ADR-0069, ADR-0070]
Outcome: Scoville-Skills, Suites und private Benjamin-Skills sind auf GitHub unter den freigegebenen Namen, Sichtbarkeiten und Versionen veröffentlicht.
Acceptance: PLAN-0011 ist nach beobachteten Abnahmen abgeschlossen und alle Releasegates sind erfüllt. Aktuelle Scoville-Repositories tragen die finalen Namen ohne `anti-ai-slop`. Bestätigte Deprecated-Repositories sind privat. Private `benjaminstelzer-*`-Skills sind vollständig in privaten Repositories veröffentlicht. Branches, Tags, Releases, Beschreibungen, Themen, Profil-README und Installationslinks stimmen mit den finalen Paketen überein. Releaseassets und Checksummen sind an den richtigen Releases vorhanden. Keine unbeteiligte Historie oder Sichtbarkeit wurde geändert.
Steps:
1. Führe für jedes Ziel den autorisierten GitHub-Preflight aus und vergleiche Branch, Schutz, Sichtbarkeit, Historie, aktuelle Releases, Tags, Themen und Zielnamen mit W-001 und W-008.
2. Veröffentliche die verifizierten Paketbäume und privaten Skills; benenne aktuelle Repositories um und setze bestätigte Deprecated-Repositories privat. Erstelle die erforderlichen Releases und lade den zugeordneten Assetsatz hoch.
3. Aktualisiere das Profil und alle betroffenen öffentlichen Metadaten aus den finalen Namen und überprüften Installationswegen; bewahre bestehende unbeteiligte Einträge.
Evidence: []
Next action: Nach W-008 für jedes Ziel GitHub-Zustand und geplante Mutation erneut erfassen.

### W-010 Remote-Ergebnis und Neuinstallation sind vollständig verifiziert

Status: todo
Depends on: [W-009]
Blocked by: []
Decisions: [ADR-0069]
Outcome: GitHub und eine isolierte Neuinstallation entsprechen den finalen Quellen ohne alte oder doppelte Skillvarianten.
Acceptance: Remote-Dateibäume, Commit-IDs, Versionen, Tags, Releases, Assets, heruntergeladene Checksummen, Sichtbarkeiten, Repository-Namen, Profil-Links und Themen stimmen mit W-008 und W-009 überein. General- und Codex-Migrationsprompt werden gegen isolierte Altbestände ausgeführt. Danach ist jeder unverändert benannte aktuelle Skill genau einmal als verifizierte aktuelle Installation vorhanden; alle umbenannten oder entfallenen Legacy-IDs sind abwesend und alle Pflichtmitglieder vorhanden. Abweichungen gelten als Veröffentlichungsfehler und bleiben offen.
Steps:
1. Vergleiche jeden veröffentlichten Remote-Baum und Release mit dem zugehörigen Receipt, Commit, Tag, Assetinventar und lokalen Prüfsummen; lade Assets zur Identitätsprüfung erneut herunter.
2. Führe General- und Codex-Migration in getrennten isolierten Installationswurzeln mit repräsentativen Altbeständen aus; prüfe Discovery und die Entfernung der persönlichen Einstellungen aus den deinstallierten Altinstallationen ohne Sicherung oder Übernahme, für unverändert benannte Bestandsmitglieder jeweils genau eine aktuelle verifizierte Installation sowie die Abwesenheit aller umbenannten oder entfallenen Legacy-IDs.
3. Dokumentiere pro Repository und Suite den verifizierten Endstand sowie jede verbleibende Abweichung; schließe den Plan nur bei vollständiger Acceptance.
Evidence: []
Next action: Nach W-009 Remote-Bäume und Releaseassets gegen die lokalen Belege prüfen.
