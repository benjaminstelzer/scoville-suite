# Plan Viewer und Skill-Veröffentlichung trennen

## Geprüfter Quellenstand

W-015 / ADR-0211: Viewer unter `projects/scoville-plan-viewer`, Skills weiter aus
der kanonischen Suite. Die Extraktion erhält 62 Dateien, Modi und acht eigene
Commits: Baum `ea6af11846c7cc0bb79beb142265b4b442e76cf5`, Split
`dd6a3631c7b5dfab0daeb2629623bbeffe535327`. Alle historischen Pfade, vollständigen
Commitmetadaten und 102 verschiedenen Dateiobjekte geprüft; keine privaten
Projektbezüge oder verdächtigen Zugangsdaten gefunden. Anwendungslogik,
Versionsinhaber 1.4.3 und Tauri-Kennung bleiben erhalten.

Suite und Shared enthalten keine zweite Viewer-Quelle, nativen Workflows oder
Viewer-Releasegate. Skill-Pushes verlangen weiterhin saubere Quellen, aktuellen
Buildreceipt, Paketintegrität und Runtime-Nachweis. Sie erzeugen keine Releases
oder neuen Tags. Das Viewer-Repository besitzt Builds und Downloadprüfung.

## Abnahme und Checks

Sol 6.1/high (`ask_sol_viewer_only`) und Opus 5.5/high (Claude-Sitzung
`b68b764d-5426-4c7a-a9ed-7a3cce3e52cc`) haben Vorschläge und vollständige
tatsächliche Patchreviews gegenseitig gelesen und den korrigierten Stand ohne
Blocker angenommen. Modell-/Effort-Telemetrie wurde von den Advisern nicht
unabhängig berichtet. Root blieb einziger Editor.

Bestanden: 83 Shared-Checks, 61 GitHub-Auditchecks, 17 Viewer-Gatechecks,
zehn isolierte Plan-Fortschrittschecks und sechs echte Plan-/Viewer-Vergleiche,
auch gegen den öffentlich gepinnten Vertragsstand `47cecddfe55aaf26d72ab44a66c5d6270abbd32e`.
Vier frische Luna-6/medium-Erstentscheidungen zu Push, Skill-only-Änderung,
Downloadersatz und Fortschrittsvertrag richtig. Die unklare Fixture-Pfadangabe
wurde präzisiert. Profilvalidierung: keine Fehler; zwei bekannte absichtliche
Encoding-Beispiele in PLAN-0035 bleiben Warnungen.

Verifier-only-PRs lösen keine vier unveränderten nativen Builds aus. Der vor jedem
Neubuild nötige Dispatch prüft Gate, echten Planvergleich und alle Plattformen.
Unveränderte erfolgreiche Ergebnisse werden wiederverwendet. Nach Nutzerkorrektur
gelten Luna-Verständnisproben für öffentliche Skilltexte; private Skills und
Buildtools erhalten gezielte technische Checks ohne routinemäßige Modellreviews.

## Auslieferungsgrenze

Nutzerkorrektur: vorhandene elf Binaries und Prüfsummen ohne nativen Neubuild
übernehmen. Alle 60 Anwendungsinputs stimmen exakt mit erfolgreichem Suitebuild
`ba11cab7d2e737c737fefca0db772669ec239529`, Run `37574844077` überein.
Originaler Buildnachweis bleibt erhalten; Gate vergleicht ursprüngliche Jobs und
Artefaktbytes. Der neue native Workflow ist noch nicht in Actions ausgeführt.

Ausgeliefert: [Viewer v1.4.3](https://github.com/benjaminstelzer/scoville-plan-viewer/releases/tag/v1.4.3)
enthält elf unveränderte Programme/Installer und Prüfsummen. Originale Actionsbytes,
Versionen und Inputs geprüft; nach Upload exakt zwölf Namen, Status, Größen und
SHA-256-Digests bestätigt. Erfolgreichen Actionsbyte-Nachweis beim Uploadcheck
wiederverwendet. Sol und Opus haben die Übernahme nach vollständigem Austausch
angenommen. Kein nativer Neubuild gestartet. Release-Tag: `a59909b`; Branch
`57847a3` ist nur durch das Entfernen von „What it costs“ in README fortgeschritten.

Runtime-Matrix `38027886534` erfolgreich, mit aktuellen 19 Paketprojektionen
gebunden; 13 Exportpakete und lokale Suite-Skills geprüft. GitHub-Skill in Codex
und Claude bytegleich installiert; persönliche Einstellungen erhalten. Beide
Suite-Distributionen, Standalone-Plan, privater GitHub-Skill und Profil gepusht;
vollständige Remote-Bäume und Sichtbarkeit bestätigt. Vier unveränderte
Standalone-Ziele übersprungen. README-Downloadlinks führen zu `/releases/latest`.
Zehn alte Skill-Releaseobjekte und ihre Assets entfernt; alle exakten alten
Tagobjekte, Branches und Sichtbarkeiten erhalten. Materiale Änderungsnotizen
stehen weiter in Changelogs; alte Skill-ZIPs sind auf Nutzerauftrag entfernt.

Profil-Eintrag verlinkt `/releases/latest` unter Applications. Fremde lokale
Profil-README-Änderungen bleiben unberührt. EMPCO-Überwachung wurde gelöscht;
nach Nutzerstopp keine EMPCO-Zugriffe. Neue native Starts, Signierung und
Notarisierung werden durch diese Migration nicht nachgewiesen.

Alte Stagingdateien entfernt oder nach `Desktop/_delete` verschoben. Unter
`skills/temp/release/export-prepared-codex` bleiben nur gesperrte leere Ordner
(keine Dateien). Zusätzliches rekursives Löschen wurde mit „blocked by policy“
abgelehnt; die Ausweichverschiebung scheiterte an einer Dateisperre. Das aktuelle
Build liegt weiter ausschließlich unter `skills/temp/release`.
