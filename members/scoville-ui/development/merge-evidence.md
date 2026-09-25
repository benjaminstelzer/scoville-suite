# Zusammenführung zu Scoville UI

Stand: 2026-09-25. PLAN-0006, ADR-0040 und ADR-0041 besitzen Auftrag und Grenzen.

## Kandidat und Review

`suite.json` liefert einen UI-Member `scoville-ui` aus. WordPress-Regeln liegen
als lokale Referenzen darin. Ihr Auslöser ist ausschließlich die Entwicklung
oder Prüfung plugin-eigener Backend-UI in `wp-admin`. Frontendausgaben von
Plugins, Themes und Sitefrontends verwenden die allgemeine UI-Route.

Die sichtbare Aufgabe `ASK Scoville UI Abnahme ASTRA RUN [#1]`
(`01a0d7ee-9cfb-71b2-a50a-141719114c36`) erhielt `gpt-6-astra`, Reasoning `high`.
Separate tatsächliche Modellmetadaten lagen nicht vor. Die Erstprüfung war
frisch, die Folgeprüfung nutzte denselben Kontext. Konsultation
`ui-merge-astra-pretest-20260925-02` gab die Instruktionen und damaligen Paketbytes
für den Teststart frei. Die fehlenden Discovery-Ausschlüsse und der gemeinsame
Permission-Guard waren zuvor korrigiert worden. Keine neuen Findings im
erneut geprüften Umfang. SOL fand anschließend ungültiges YAML durch einen
unquotierten Doppelpunkt in der Description. Nach Ergänzung der beiden Quotes
gab Astra mit `ui-merge-astra-pretest-20260925-03` die neuen Bytes erneut für
Tests frei. Der Diff enthielt ausschließlich diese Quotierung. Der Reviewer
führte keine Tests oder Builds aus.

| Entwicklungsbuild unter `skills/temp/release/ui-merge/yaml-fix/` | SHA-256 |
| --- | --- |
| Standalone `SKILL.md` | `e080dd3ab9ca71868dcc82b8540b39802b508aa9034f573559b279aa2d505592` |
| Standalone Receipt | `364a9c340f645c3565e2288ff67818d6aafc5a4d64b4abb0bc6e52f2e987c309` |
| Suite/general Receipt | `321800823ce0e21b3854bad4465bc3d1695811c26ff64eae6a0c9aeb0bdd3902` |
| Suite/codex Receipt | `e39fc213205821b5f181f48d9299657b8e45c1eade8b56c3de9de60eb06779b3` |

Astra glich je Paket alle 19 Laufzeitdateien mit dem Receipt ab und fand genau
einen UI-Member sowie auflösbare lokale Markdown-Dateiverweise. Das ist eine
statische Reviewaussage, keine Runtime-, Wirksamkeits- oder Releasefreigabe.
Die Receipts weisen Entwicklungsstände mit uncommitteten Quellen aus.

## Delegierte Prüfungen

SOL 6 High hat getrennte lokale Installationen von WordPress 7.1.2 und 7.0.6
unter `C:/xampp_lite_8_5/www` eingerichtet. Zugangsdaten liegen außerhalb des
Repositories. Paketprüfungen und der praktische Vergleich nach
`development/ui-evaluation.md` wurden erst nach Astra-Freigabe beauftragt.
Nach ADR-0044 begrenzt der Nutzer die Tests auf 30 Minuten. Die praktische
Stichprobe unterscheidet Greenfield-Erstellung und Änderungen an bestehender
UI. Historische Medium-Läufe und die vollständige 36-Arme-Matrix gelten nicht
als ausgeführt.

SOL 6 High bestätigte am YAML-Fix-Kandidaten:

- Fünf fokussierte Build-Regressionstests bestanden.
- Alle drei Paketprüfungen und exakten Buildinventare bestanden: Standalone ein
  Paket/24 Dateien, Suite/general vier/72 und Suite/codex fünf/110, jeweils
  einschließlich Build-Receipt. Das UI-Paket selbst enthält 23 Dateien.
- Shared-Snapshot unverändert, gültiges YAML-Frontmatter und 52 vorhandene
  lokale Markdown-Dateiverweise im UI-Skill.
- Isolierter Export aus temporärem Snapshot-Commit
  `89ad299a99d7ea5e1fef53d584d8033ccb286f7e`: 559 Receipt-Dateien ohne
  Hashabweichung. Die 71 Paketdateien in Export, isoliertem Wiederaufbau und
  neuem General-Kandidaten sind byteidentisch.
- Native Profilprüfung nach Korrektur einer parallelen ADR-ID-Kollision:
  30 Dateien, sieben Pläne, 70 Work Items, 22 Decisions, null Fehler/Warnungen.

Der Standardvalidator `quick_validate.py` bleibt bei Exit 1, weil seine
Allowlist das etablierte Suite-Feld `compatibility` ablehnt. Diese Grenze wird
nicht als grüner Check ausgegeben. PyYAML bestätigt die gültige Syntax.
Die temporären Git-Commits dienen nur dem Exporttest. Das kanonische Repository
wurde nicht committed. Das geprüfte General-Paket wurde unter
`packages/scoville-ui/` ergänzt. SOL bestätigte anschließend exakt 23 gleiche
Paketdateien und null Hashabweichungen gegenüber dem geprüften General-Build.

## Verbleibende Grenzen

Der erste begrenzte praktische Auftrag endete nach rund elf Minuten. Der erste
Greenfield-Vergleichsarm scheiterte an automatischen Policy-Rejections einfacher
Lesezugriffe; fünf weitere Implementierungsarme wurden nicht gestartet.
`development/ui-evaluation-results.md` dokumentiert die direkte WordPress-7.1.2-
Stichprobe separat. Sie zeigt Fehler der unveränderten Testfixture und belegt
keine vom Kandidaten erstellte oder geänderte UI.

Der danach ausdrücklich beauftragte sichtbare SOL-High-Task führte Greenfield
und UI-Änderung innerhalb von 22 Minuten aus. `development/ui-visible-sol-results.md`
belegt die tatsächlich implementierten Classic-/React-Oberflächen, Tastaturwege
und i18n-Vorbereitung. Der kontrollierte Baselinevergleich und Übersetzungskataloge
bleiben ungeprüft. Der Nutzer beauftragte anschließend ausdrücklich den Abschluss
von PLAN-0006. Die frühere TEST-POLICY-Sperre gilt nicht für diesen erfolgreichen
sichtbaren Lauf; Abschluss und Grenzen stehen in
`docs/skill-update-closure-2026-09-25.md`.

Automatische Approval-Prüfung blockierte die Entfernung der alten Member-Ordner.
Nach der angekündigten Nutzerbereinigung sind beide alten UI-Member-Verzeichnisse
nicht mehr vorhanden. Manifest und frische Builds enthalten nur den neuen UI-Member.
Die ursprüngliche Historie bleibt in Git und der gesicherten Baseline. Alte
generierte Paketordner sind davon getrennt und nicht als aktuelle Builds zu verwenden.
Es gab weder eine Skillinstallation noch Veröffentlichung oder kanonischen Commit.
Rohdaten und Reviewantworten bleiben im auftragsbezogenen Workspace-temp.
