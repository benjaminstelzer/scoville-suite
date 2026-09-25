# Releaseinventar für PLAN-0012

Stand: 2026-09-25. Entwicklungsstand auf HEAD 84b0468347a8e4f4fbec79fc6a4b3de9622e2a83 mit uncommitteten Änderungen. Kein eingefrorener Releasekandidat.

## Aktuelle Quellen und Ziele

Quelle je Mitglied: members/<Paket-ID>. Öffentliches Repository unter benjaminstelzer, sofern nicht anders angegeben. General enthält vier Mitglieder; Codex alle sieben. suite.json besitzt diese Zuordnung.

| Aktuelle Paket-ID | Ziel-ID | Profile | Veröffentlichungsziel | Quellversion / letzter beobachteter Release |
| --- | --- | --- | --- | --- |
| scoville-code | scoville-code | General und Codex | scoville-code durch Umbenennung | v2.0.0 / v1.0.36 |
| scoville-handoff | unverändert | General und Codex | scoville-handoff | v2.0.17 / v2.0.17 |
| scoville-plan | unverändert | General und Codex | scoville-plan | v1.9.0 / v1.7.7 |
| scoville-ui | unverändert | General und Codex | scoville-ui neu | v2.0.0 / noch kein Ziel |
| scoville-workflow-for-codex | unverändert | Codex | nur Codex-Suite | v0.6.0 / kein eigener aktueller Release |
| scoville-ask-for-codex | unverändert | Codex | scoville-ask-for-codex neu und Codex-Suite | v1.0.0 / noch kein Ziel |
| scoville-setup | unverändert | Codex | nur Codex-Suite | kein eigener Changelog |

General-Ziel: scoville-suite v2.0.0, öffentlich, letzter Release v1.0.10.
Codex-Ziel: scoville-suite-for-codex v2.0.0, noch nicht in der Live-Repositoryliste.
Die member.repository-Angaben von Workflow und Setup nennen scoville-suite. Der geprüfte Codex-Receipt löst beide profilabhängig auf benjaminstelzer/scoville-suite-for-codex auf.
Plan Viewer v1.3.3 gehört als neuer Build zu den Releases von Scoville Plan und beiden Suites. Die kleinsten wahrheitsgemäßen SemVer-Schritte sind Major für Suite, Code und UI wegen geänderter Paket- und Installationsverträge, Minor für Plan und den noch vor Version 1 liegenden Workflow sowie v1.0.0 für den erstmals zusammengeführten Ask-Skill. Handoff bleibt unverändert. Gleiche Versionsnummern beweisen keine unveränderten Paketbytes.

Der kurze Migrationsauftrag installiert danach direkt aus dem jeweiligen GitHub-Repository. General verwendet https://github.com/benjaminstelzer/scoville-suite, Codex verwendet https://github.com/benjaminstelzer/scoville-suite-for-codex. Die vollständige URL steht im kopierbaren Auftrag, nicht nur in Begleittext oder einem lokalen Buildpfad.

## Historische Pakete

| Altbestand | Nachfolger / Behandlung | Beobachteter letzter Release |
| --- | --- | --- |
| scoville-ui-anti-ai-slop | scoville-ui gemäß ADR-0040 | v1.2.9 |
| scoville-wordpress-ui-backend-anti-ai-slop | scoville-ui gemäß ADR-0040 | v1.3.0 |
| fünf Ask-Varianten | scoville-ask-for-codex | ask-suite-for-codex v1.0.3 |
| scoville-workflow-codex | scoville-workflow-for-codex in Codex-Suite | v0.3.6; Repository bereits privat |
| scoville-brainstorm | ersatzlos ausmustern; beim Release privat gemäß ADR-0070 | v1.1.14 |
| scoville-research | ersatzlos ausmustern; beim Release privat gemäß ADR-0070 | v1.1.12 |
| scoville-design-anti-ai-slop | ersatzlos ausmustern; beim Release privat gemäß ADR-0070 | v1.2.10 |
| scoville-scribe-anti-ai-slop | ersatzlos ausmustern; beim Release privat gemäß ADR-0070 | v1.0.34 |

Die fünf Ask-IDs sind ask-astra-for-review-for-codex, ask-sol-for-review-for-codex, ask-claude-for-codex, ask-claude-and-astra-for-codex und ask-claude-and-sol-for-codex.
Live-GitHub bestätigt weiterhin zehn alte Scoville-Pakete sowie diese fünf Ask-Pakete. Die vier ausgemusterten Mitglieder sind noch öffentlich und im aktuellen lokalen Manifest nicht vorhanden. ADR-0070 bestätigt ihre ersatzlose Stilllegung und die spätere Umstellung auf privat.

## Private Quellen

Gemeinsamer aktueller Quellort: E:/Dropbox/AI Projects/skills/private/benjaminstelzer/.

| Unter skills/private/benjaminstelzer | Paket-ID | Git-Zustand | GitHub-Ziel |
| --- | --- | --- | --- |
| benjaminstelzer-github-skill | benjaminstelzer-github | sauber; 1ad03d81e22cee346ea7be3c0fb8e690b62d37f3 | benjaminstelzer-github-skill privat; v1.0.1 |
| benjaminstelzer-imitate-me-skill | benjaminstelzer-imitate-me | sauber; f2a584327fc6b21278ca42a3c7c65b468cbfdd52 | benjaminstelzer-imitate-me privat; v1.0.5 |
| benjaminstelzer-skillwriter-skill | benjaminstelzer-skillwriter | kein Git-Repository | fehlt in Live-Repositoryliste |

Die frühere Annahme von drei existierenden Git-Repositories ist falsch. W-004 muss vorhandene Historie erhalten und den dritten Quellordner als neues privates Veröffentlichungsziel vorbereiten. Vollständiger Paketvergleich folgt dort.

## Installationen und lokale Ausgaben

- C:/Users/benja/.codex/skills enthält die fünf Ask-Varianten, Code, Handoff, Plan, beide alten UI-Varianten, Workflow und die drei Benjamin-Skills.
- C:/Users/benja/.claude/skills enthält Code, Handoff, Plan, beide alten UI-Varianten sowie Benjamin GitHub und Imitate Me.
- C:/Users/benja/.agents/skills fehlt. Neue UI-, Ask- und Setup-Pakete sind in den beiden geprüften Installationswurzeln noch nicht installiert.
- packages/ enthält alle sieben aktuellen Manifestmitglieder. Deren bloße Existenz ist kein finaler Buildbeleg.
- skills/public/ enthält noch die fünf alten Ask-Einzelrepositoryverzeichnisse.
- Feste Suite-Ausgabeziele gemäß PLAN-0002/W-006: skills/public/scoville-suite und skills/public/scoville-suite-for-codex; beide fehlen derzeit.
- Reguläres Staging unter skills/temp/release/general und codex hat Receipts und Suite-Verzeichnisse. standalone enthält noch die beiden alten UI-Pakete.
- Testbauten bleiben getrennt von finalen Ausgaben. PLAN-0011 verwendet plan-0011-review-fixes sowie plan-0011-w025-final. Nicht während laufender Leser überschreiben oder pauschal löschen.

## Nachweise und Veröffentlichungssperren

- PLAN-0011/W-001: HOST-POLICY bleibt offen. Kein erneuter oder alternativer Versuch der abgewiesenen Rechnermaßnahmen.
- PLAN-0011/W-002: tatsächliche GitHub-Matrix auf Windows/macOS/Ubuntu mit Python 3.11 und aktueller Version fehlt.
- PLAN-0011/W-026 belegt native Workflow-Abnahme mit den im Prüfbericht genannten Grenzen. W-025 belegt Plan-Vergleiche und fokussierte Prüfungen. Kein Beleg allgemeiner Kosten- oder Laufzeitersparnis.
- Frühere UI- und Ask-Nachweise bleiben historische Evidenz. Ihre Anwendbarkeit auf den finalen Kandidaten wird anhand betroffener Quellen geprüft; neue Paketnamen und Projektionen benötigen neue Build- und Migrationstests.
- Keine alten Viewer-Binaries als neue Artefakte ausgeben. W-008 besitzt Neubau und Zuordnung.
- W-001-Abgleich: build_suite.py --check-packages besteht für general und codex mit --layout suite --public-only gegen plan-0011-w025-final. Beide vollständigen Paketprojektionen entsprechen den aktuellen Quellen. PLAN-0011-Nachweise bleiben für diesen Stand mit ihren dokumentierten Grenzen verwendbar. Ältere Nachweise aus PLAN-0002 und PLAN-0006 bis PLAN-0010 gelten als historische Vorstufen und werden nicht als unabhängige Abnahme des künftigen Releasekandidaten übernommen.
- Veröffentlichung bleibt gemäß ADR-0069 gesperrt. Die Inventur hat keine Installation oder Remote-Mutation ausgeführt.

Beobachtungen: suite.json und lokale Verzeichnis-/Git-Prüfungen; gh repo list; GitHub contents/packages für beide alten Suites; Releases-Endpunkte für die aufgeführten bestehenden Repositories. Letzter gelisteter Release ist eine Momentaufnahme und kein final geprüfter Releasevertrag.

## W-002: Familien- und Aktivierungsprüfung

Die sieben Einstiegspunkte und ihre Familienprojektionen trennen Code, Plan, UI, Handoff, Ask, Workflow und Setup. UI lädt den WordPress-Adapter nur für dessen Oberfläche. Plan startet keinen Workflow. Ask lässt Berater nur lesen; Setup speichert Einstellungen ohne Ask oder Workflow zu starten. Explizite Aktivierungsgrenzen und Nutzerausschlüsse bleiben in Suite-Projektionen erhalten.

Windows/Python 3.14: acht Tests in development/tests/test_build_suite.py und vier in ../shared/tests/test_distribution_profiles.py bestanden. Zwei ergänzte Fälle prüfen die ausgelieferten Aktivierungs-/Ausschlussregeln in General/Standalone, General/Suite, Codex/Suite und Codex/Ask-Standalone sowie die Ablehnung partieller Suite-Builds beider Profile vor Anlage des Ausgabeordners. Die vorhandenen Profiltests prüfen zusätzlich fehlende Fallbacks in Codex, Familienprojektionen und isolierte Exporte.

Dies belegt Instruktions- und Buildverträge, keine neue native Modellverhaltensprüfung. Vorhandene native Evidenz bleibt mit ihren Grenzen gültig. Keine Skill-Anweisung musste für W-002 geändert werden.

## W-003: Lokale Namensmigration

Code heißt jetzt scoville-code in Quell- und Paketverzeichnissen, SKILL-Frontmatter, UI-Metadaten, Manifest, Familienverweisen, README-Fragmenten und Testverbrauchern. Die bisherigen Releaseeinträge bleiben erhalten; ein Unreleased-Eintrag nennt die Umbenennung. Der alte GitHub-Name bleibt bis W-009 live. Die lokale und entfernte Zielprüfung fand keine Namenskollision.

General- und Codex-Builds liegen unter skills/temp/release/plan-0012-names. Die vier General-Paketkopien in packages/ wurden nach belegter Übereinstimmung mit ihrem alten Build aktualisiert; Inventare sind identisch zum neuen Build. UI und Ask besitzen bereits ihre endgültigen Quellen. Für die vier gemäß ADR-0070 ausgemusterten Mitglieder gibt es keine aktuelle Quelle im Manifest.

Acht Suite- und fünf Familientests unter Windows/Python 3.14 bestehen. README- und Shared-Snapshot-Prüfung melden keine Abweichung. Alle Code-Laufzeitdateien wurden gegen die unveränderte temporäre Vorlage verglichen: nur freigegebene Namensänderungen. Keine neue Verhaltensänderung oder Modellprüfung behauptet.

Verbleibende alte Namen in historischen Plänen, Nachweisen, alten Releaseeinträgen und den Inventar-/Migrationstabellen sind beabsichtigt. Die früheren Vergleichsunterlagen development/luna-tests/suite-simplification-comparison.md und development/readme-unification.md bleiben historische Beschreibungen. Alte Teststagingbauten bleiben bis zur vorgesehenen Bereinigung erhalten. Live-Installationen werden erst über W-006/W-008 migriert.

Skill Creator quick_validate lehnt das bestehende compatibility-Frontmatter weiterhin ab. Bekannter Werkzeugkonflikt aus PLAN-0011/W-007; kein grüner Skill-Creator-Befund. Die Suite baut erfolgreich.

## W-004: Private Quellen zusammengeführt

Alle drei Verzeichnisse liegen jetzt unter E:/Dropbox/AI Projects/skills/private/benjaminstelzer/. Vorher/nachher wurden sämtliche Dateien einschließlich .git verglichen: GitHub 223, Imitate Me 48, Skillwriter 4 Dateien unverändert. Die GitHub- und Imitate-Me-Commits entsprechen der Tabelle oben; beide Arbeitsbäume bleiben sauber. Skillwriter hatte und hat noch keine Git-Historie.

Die Prüfung von Skripten und Konfigurationen in Suite, Shared und privaten Quellen sowie Workspace-Dateien ergab keine aktiven absoluten Verbraucher der alten Quellpfade. Gespeicherte Codex-Projekte verweisen ebenfalls auf keinen der drei alten Ordner. Historische Pläne und Inventurbelege bleiben als solche erhalten.

Vollständiger Remote-Paketvergleich gegen main:
- benjaminstelzer-github-skill: Commit 2e6d3383d08127538bcc544da34ff23209a426b5. Drei inhaltlich abweichende Dateien: SKILL.md, references/readme-and-public-copy.md und references/release-and-publication.md. Zwölf weitere Unterschiede betreffen ausschließlich CRLF/LF. Vier lokale pyc-Dateien bleiben Entwicklungsreste und sind keine Veröffentlichungsdateien.
- benjaminstelzer-imitate-me: Commit 4bafc9e23c1a5b7419c1c0bad1c55bea5d2ab9a3. Inhaltliche Unterschiede in SKILL.md und references/voice-profile.md. agents/openai.yaml unterscheidet sich nur durch Zeilenenden.
- benjaminstelzer-skillwriter: noch kein Remote-Ziel vorhanden. Vorgesehenes privates Repository benjaminstelzer/benjaminstelzer-skillwriter mit Paket benjaminstelzer-skillwriter.

Bestehende private Repository-Namen bleiben benjaminstelzer-github-skill und benjaminstelzer-imitate-me. Repository-Ordner und installierbare Paket-ID sind im Inventar ausdrücklich getrennt; daraus entsteht kein zweites Paket. W-007 prüft die privaten README-Quellen, W-008/W-009 bereiten die vollständigen bereinigten Veröffentlichungskandidaten und deren private Veröffentlichung vor. Keine Installation oder GitHub-Mutation in W-004.

## W-005: Finale Namen und Buildprofile

Windows/Python 3.14: alle 53 Shared-Tests bestanden, einschließlich reproduzierbarer Pakete, isoliertem Suite-Export und Wiederaufbau, vollständiger Mitgliedschaft, Linkprüfung, Quell-/Receipt-Abgleich und CRLF-Normalisierung. Die vier Layouts unter plan-0012-names enthalten General/Suite 4, Codex/Suite 7, General/Standalone 4 und Codex/Standalone 1 Mitglied. Sämtliche geprüften Markdown-, Python-, JSON-, TOML-, YAML- und Textdateien enthalten kein CR.

Die gebauten Plan-Validatoren beider Profile wurden gegen einen tatsächlich fehlenden Profilpfad ausgeführt: Exit 2 und valid null statt Erfolg. General enthält genau profile-without-python.md und select-context-without-python.md mit bedingter Ladung nur bei fehlendem Python. Codex enthält keine solche Referenz und verlangt seine Helfer. Die Fehlergrenze steht im Einstiegspunkt; ein anfänglicher Prüfausdruck suchte sie irrtümlich in profile-validation.md und wurde nach Quellenprüfung korrigiert.

Ask behält die verpflichtende Modellabfrage, Python 3.11 und den Claude-CLI-Vertrag; diese Laufzeitquellen wurden durch die Namensänderung nicht verändert. Manuelle General-Routen wurden als Instruktionsvertrag geprüft, nicht durch einen neuen Modelllauf ohne Python. Die Beobachtung behauptet keine neue native Modellabnahme oder vollständige Plattform-CI. Diese Grenzen und die eigenständigen Releasegates bleiben bestehen.

## W-006: Einfacher Migrationsauftrag

Auf ausdrückliche Nutzerkorrektur beschränkt sich der Migrationsprompt auf Deinstallation der exakten profilbezogenen Altlisten, Überspringen fehlender Skills und anschließende vollständige Installation oder Aktualisierung. Die ausdrücklich freigegebene Entfernung umfasst die persönlichen Einstellungen der entfernten Installationen. Keine Sicherung, Einstellungsübernahme oder Fallback-Kopie. Unbeteiligte Skills bleiben unangetastet. Eine vorgeschaltete Discovery-Abfrage oder ein Originalvergleich wird nicht verlangt.

Der vorherige umfangreichere Entwurf wurde verworfen. Dessen bereits laufender isolierter Test endete erfolgreich: acht Bestände (General/Codex jeweils alt, gemischt, angepasst und aktuell) wurden umgestellt; die tatsächliche Codex-skills/list-Abfrage erkannte die erwarteten Pakete im jeweiligen Testpfad. Das belegt die Dateiumstellung und Discovery der unveränderten Pakete, nicht die Verständlichkeit des später gekürzten Prompts. Reale Installationen blieben unverändert.

Der gekürzte kanonische Prompt und die generierte README stimmen überein. Die abschließende Prüfung der beiden Profilprojektionen des gekürzten Prompts steht noch aus.

Nutzerkorrektur: Auch persönliche Einstellungen der entfernten Installationen sollen entfallen. Frühere Erhaltungsprüfungen belegen diesen geänderten Zielzustand nicht.

## W-006: Korrigierter Endstand und offene Ausführungsprüfung

Beide finalen Profilprojektionen wurden geprüft: exakte Listen, fehlende Skills überspringen, Einstellungen entfernen, keine Sicherung/Migration/Fallback-Kopie und anschließend frische Installation. Codex-Zusatznamen sind in General nicht enthalten.

Die automatische Freigabeprüfung hat einen lokalen Versuch mit isolierten Testordnern vor Prozessstart abgewiesen. Das ist kein Blocker für den Migrationsauftrag: W-006 weist den später installierenden Agenten an, die genannten Alt-Skills vollständig und ohne Sicherung zu deinstallieren und danach frisch zu installieren. Die aktuellen lokalen Installationen werden bei der Planumsetzung nicht vorab manuell entfernt. Die tatsächliche Ausführung und Discovery nach Veröffentlichung werden in W-010 abgenommen.

Lesende W-007-Vorprüfung: suite-deprecated.md behauptet noch zwei UI-Skills und Workflow-Mitgliedschaft in General. Dieser Absatz muss nach Freigabe der abhängigen Arbeit den vier General-Mitgliedern und einem gemeinsamen UI-Skill entsprechen. Keine Änderung an historischem Release-Text erforderlich.

## W-007: README-Abgleich

Die sieben Mitglieds-READMEs und die drei privaten README-Quellen wurden auf Zweck, Voraussetzungen, Installation, Beispiele und Zuständigkeiten geprüft. Die privaten Kurzfassungen benötigen keine Änderung. Plan erklärt die vier regulären Reasoning-Stufen sowie manuelle Zusatzwerte. Ask bleibt einzeln installierbar und im General-Katalog sichtbar, ohne General-Laufzeitmitglied zu werden.

Korrigiert: Der General-Deprecated-Absatz nennt jetzt Code, Plan, einen UI-Skill und Handoff. Die Codex-Einleitung nennt Setup. Workflow verweist bei Neuinstallation auf den Suite-Migrationsprompt. Der gemeinsame Codex-Kompatibilitätstext nennt .scoville/config.json statt der abgeschafften persönlichen config.json und verlangt keinen widersprechenden Erhalt der Altinstallation.

Vierzehn README-Tests unter Windows/Python 3.14 bestanden. General- und Codex-Builds unter plan-0012-readmes sind erfolgreich. Codex-Mitgliedsvorschauen sowie die betroffenen Paket-READMEs wurden aus diesen Generatorausgaben synchronisiert. Historische Release-Texte blieben unverändert. Die neuen Repository-Ziele sind weiterhin Releaseziele und noch keine live verifizierten Installationslinks.

W-006 bleibt direkte Voraussetzung von W-008; maßgeblich ist der geprüfte Agentenauftrag, nicht eine vorgezogene Deinstallation der aktuellen lokalen Installation.

Frische General- und Codex-README-Projektionen unter skills/temp/release/plan-0012-w006-readmes bestätigen den finalen Auftrag. General enthält genau die neun gemeinsamen Alt-IDs und keine Codex-Zusatz-ID. Codex enthält zusätzlich alle sieben vorgesehenen Codex-IDs. Beide Projektionen verlangen vollständige Entfernung einschließlich persönlicher Einstellungen ohne Sicherung, Migration oder Fallback-Kopie und anschließend eine frische Vollinstallation. Alle geprüften Dateien verwenden LF. W-006 ist abgeschlossen; die reale Ausführung bleibt Teil der Neuinstallationsabnahme in W-010.

Nach Nutzerkorrektur besteht der Migrationsprompt nur noch aus zwei Anweisungen und den Alt-ID-Listen. Die General-Projektion nennt Python 3.10 oder neuer als optional, weil manuelle Fallbacks bestehen. Die Codex-Projektion verwendet das in Codex integrierte Python 3.11 oder neuer und enthält keinen manuellen Installationsweg. Beide frisch generierten README-Projektionen stimmen mit ihren Quellen überein.
## W-008: Releasekandidaten und Viewer-Buildweg

Der Viewer steht in package.json, package-lock.json, src-tauri/tauri.conf.json, Cargo.toml und seinem eigenen Cargo.lock-Paketeintrag auf 1.3.3. Der neue Suite-Workflow .github/workflows/plan-viewer.yml baut Windows x64, Linux x64 sowie macOS ARM64 und x64 aus members/scoville-plan/development/viewer. Die Standalone-Kopie unter members/scoville-plan/.github/workflows/plan-viewer.yml verwendet denselben Vertrag mit ihrem relativen development/viewer-Pfad.

Beide Workflows verwenden Node 22 und Rust stable. Sie erzeugen Windows-EXE/MSI/Setup, Linux-Binary/AppImage/DEB/RPM sowie macOS-App-ZIP/DMG und führen alle elf Downloads in einem SHA256SUMS.txt zusammen. Die Version wird aus den drei primären Versionsquellen gelesen und auf Übereinstimmung geprüft. YAML-Struktur, vier Matrixziele, Pfade und Checksummenjob wurden lokal statisch geprüft. npm ci, npm run check und npm run build bestehen für den Viewer. Rust ist lokal nicht verfügbar, deshalb stehen cargo test, die nativen Builds und die tatsächliche GitHub-Matrix noch aus.

Kandidaten: Suite v2.0.0, Code v2.0.0, Plan v1.9.0, UI v2.0.0, Workflow v0.6.0, Ask v1.0.0, Viewer v1.3.3 und unverändert Handoff v2.0.17. Die Changelogs nennen diese Stände. Vor dem Kandidatenbau wurden zwei irreführende Formulierungen korrigiert: Ask verändert keine Sidebar-Platzierung und Setup bietet regulär low bis xhigh, während weitere Plan-Werte nur manuell und bei Modellunterstützung gelten.

Frische Entwicklungsbuilds liegen unter `E:/Dropbox/AI Projects/skills/temp/release/plan-0012-w008-candidate/`. General enthält 4 Mitglieder mit 63 Paketdateien. Codex enthält 7 Mitglieder mit 111 Paketdateien. Beide `build-receipt.json` bestehen die unabhängige Receipt-Prüfung und den Quellenvergleich des Builders. Alle Paket- und README-Texte sind UTF-8 ohne BOM und LF-only. Der Installationsblock enthält je Profil genau einmal die richtige direkte Repository-URL und keine URL des anderen Profils. Die Receipts tragen wahrheitsgemäß `source_dirty: true` und sind deshalb Entwicklungsnachweise statt veröffentlichbarer Exporte.

Auch die eigenständigen Ziele sind frisch gebaut: General-Standalone enthält Code, Handoff, Plan und UI; Codex-Standalone enthält Ask. Damit liegen vier getrennte Buildlayouts mit gültigen Receipts und Quellenvergleich vor. Der gemeinsame Builder schreibt nun auch `build-receipt.json` ausdrücklich mit LF. Ein Windows-Regressionsfall prüft beide reproduzierbaren Receipts. Alle vier vollständigen Stagingbäume sind UTF-8 ohne BOM und LF-only. Die sieben generierten `packages/`-Verzeichnisse im Quellrepository sind bytegleich mit der jeweils zuständigen General- oder Codex-Projektion.

Nach LF-Normalisierung der kanonischen Textquellen bestehen 26 Suite-, 53 Shared-, 68 Plan-, 16 Workflow-, 22 Ask- und 2 Setup-Tests. `git diff --check` ist fehlerfrei. Beide Viewer-Workflows lassen sich als YAML lesen und enthalten genau die vier Ziel-IDs `linux-x64`, `windows-x64`, `macos-arm64` und `macos-x64`, dynamische Versionsprüfung und einen gemeinsamen Checksummenjob. Cargo und rustc sind lokal nicht vorhanden. Die nativen Viewer-Tests und Plattformartefakte müssen daher aus einem sauberen Commit über die GitHub-Matrix entstehen.

Der noch nicht gestartete W-010-Prüfschritt wurde an die ausdrückliche Nutzerkorrektur angepasst: Die persönlichen Einstellungen der entfernten Altinstallationen müssen ebenfalls entfernt sein. Kein Konfigurationserhalt und keine Sicherung als Abnahmebedingung.
