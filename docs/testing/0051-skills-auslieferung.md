# PLAN-0051: Auslieferung

Quelle sind die abgenommenen Änderungen aus PLAN-0048 bis PLAN-0050.
Technische Windows-/Linux-Nachweise und Verständnisgrenzen bleiben bei diesen
Plänen. Nur betroffene Prüfungen und aktuelle Paket-/Remoteintegrität gehören
in diese Auslieferung.

Deklarierte Ziele: scoville-suite, scoville-suite-for-codex, scoville-code,
scoville-handoff, scoville-plan, scoville-ui und scoville-ask-for-codex.
Workflow, Setup und Context Cleanup bleiben Suitebestandteile.

## Build und lokale Installation

Buildquelle: Suite-Commit `65b44803f725eed0c2c714854821fe6d066f6710`,
Shared-Commit `c153d65`. Vier Varianten umfassen 320 Paketdateien. Sie stimmen
mit dem abgenommenen V6-Kandidaten überein, bis auf die Releasechangelogs und
eine entfernte überflüssige EOF-Leerzeile im UI-Referenztext. Alle ausgelieferten
Pythondateien bleiben gegenüber dem nach PLAN-0049 getesteten Ausgangsstand
von PLAN-0050 unverändert.

Release-Receipts, Quellenprojektion, generierte READMEs, Paketstruktur,
Helperverträge, Metadaten sowie ZIP-Inhalt, CRC und Prüfsummen sind verifiziert.
Die passenden Windows-/Linux-Nachweise aus PLAN-0049 und PLAN-0050 wurden
wiederverwendet; keine pauschale neue Python-Testserie. Verständnisproben sind
weiterhin keine Ausführungsabnahme.

Zuerst wurden acht vorhandene Codex-Skills und fünf vorhandene Claude-Skills
bytegleich aus diesen Paketen aktualisiert. Persönliche Einstellungen blieben
unverändert; geprüft wurden ihre Dateimetadaten, keine Zugangsinhalte.
Die beiden festen öffentlichen Suiteverzeichnisse entsprechen ihren Exports.
Ein aktueller Build verbleibt unter `skills/temp/release/`. Gesperrte Reste
des alten CI-Kandidaten wurden mit eindeutigen Namen nach
`C:/Users/benja/Desktop/_delete/` verschoben; kein Rest bleibt im Staging.

## GitHub

| Ziel | Release | Veröffentlichter Commit |
| --- | --- | --- |
| scoville-suite | [v2.4.8](https://github.com/benjaminstelzer/scoville-suite/releases/tag/v2.4.8) | `9d6cadf5fbddda42bb77bc3daafb3bb84029572e` |
| scoville-suite-for-codex | [v2.4.9](https://github.com/benjaminstelzer/scoville-suite-for-codex/releases/tag/v2.4.9) | `cf4c67b9e48d49d1a4d503ef45690fe298e80f3e` |
| scoville-code | [v2.1.8](https://github.com/benjaminstelzer/scoville-code/releases/tag/v2.1.8) | `091baca0744f803d5f8255159b9b02b44e30bc5b` |
| scoville-handoff | [v2.1.7](https://github.com/benjaminstelzer/scoville-handoff/releases/tag/v2.1.7) | `beeeef91da8276d1ad54fc6301fa222e8476c178` |
| scoville-plan | [v1.12.8](https://github.com/benjaminstelzer/scoville-plan/releases/tag/v1.12.8) | `7e3ba30f65d249cf2a4c54ebcebdd7bf443dcf67` |
| scoville-ui | [v2.1.7](https://github.com/benjaminstelzer/scoville-ui/releases/tag/v2.1.7) | `e9518faa5ec52a2ebde82b6dad871fbeed3f8176` |
| scoville-ask-for-codex | [v1.4.7](https://github.com/benjaminstelzer/scoville-ask-for-codex/releases/tag/v1.4.7) | `70eb3dd19117a12d9e63ac7e82e5659b59b827b1` |

Für alle sieben Ziele sind vollständiger Remote-Dateibaum, Branchcommit,
annotierter Tag, Releasebody und sämtliche Assetgrößen/-digests verifiziert.
Beide Suites und Plan haben je 14 Assets, die übrigen Ziele je zwei.
Viewer 1.4.3 wurde bytegleich mit seiner erfolgreichen Actions-Provenienz
wiederverwendet, einschließlich Windows-, Linux- und macOS-Assets. Kein neuer
Viewerbuild oder macOS-Runtime-Test wird behauptet. Alte Releases und
Versionstags wurden erst danach entfernt: je Ziel genau ein aktueller Release
und Versionstag. Sichtbarkeit, Topics, Defaultbranch und Git-Historie bleiben
erhalten. Der unterbrochene Handoff-Publikationsschritt wurde nach bestätigtem
Branchstand nur um den fehlenden Tag und Release ergänzt.

Der alte Family-Prüfer setzt lückenlose Reihenfolgewerte voraus und zählt
Member-Unterpfade als doppelte Rootlinks. Diese Annahmen passen nicht zu den
bisherigen gefilterten Manifesten und dem Profilabschnitt `Scoville Suite`.
Release-/Strukturaudits bestehen; aktuelle Profilmitgliedschaft, eindeutige
globale Reihenfolgewerte, öffentliche Pakete, je ein Repository-Rootlink und
gültige Member-Quellpfade wurden getrennt geprüft. Keine öffentliche Quelle
wurde an einen veralteten Prüfer angepasst.

## EMPCO-Recovery

Thread `01a116ce-ac9b-77f0-a6cc-db641fb26f4b` erhielt nach lokaler Installation
die Reload- und Wiederaufnahmeanweisung. Die erste Rückmeldung bestätigte
neu geladene Einstiege, blieb aber wegen des alten Managers
`01a11cec-4b70-78d3-8144-5fa27ad35867` in `pending_init` blockiert.
Der Nutzer bestätigte anschließend ausdrücklich, dass kein Worker mehr läuft,
und autorisierte einen neuen Start am tatsächlichen verbleibenden Schritt.

Diese Anweisung ist zugestellt. Neue Managerinstanz:
`01a12062-a6f3-7f82-88be-76912ac78b1b`, nativer Handle
`/root/scoville_manager_3_5a96e02d38ff4b9e8e98d6289ae5aa61`.
Sie hat die START-Stufe erreicht und die aktualisierten Rollenregeln geladen.
Der Runner bestätigt nach ihrem tatsächlichen Abgleich W-370/Schritt 3 als
Fortsetzungspunkt: offene lokale Prüfharness-Korrektur samt erforderlichem
Review, danach das unabhängige vollständige Projektreview. Der neue Worker
`01a1206a-4a99-7722-81f6-db162ac97756` (Executor 14) ist tatsächlich aktiv.
Er liest den Arbeitsauftrag in geordneten Teilen und meldet Scoville Code
für die gezielte Harnesskorrektur und Fehlerfallprüfung. Damit ist die
Ausführung wieder angelaufen; Korrektur und Review sind noch offen.
Keine erfolgreiche alte Übernahme oder Abschaltung
wird behauptet. Der ursprüngliche Run-Report und die Remoteverbote bleiben
erhalten; diese Auslieferung hat selbst keine EMPCO-Produktaktion ausgeführt.

Rohbelege der Auslieferung liegen überschreibbar unter
`temp/2026-10-09-plan0051-release/`: Build-/Uploadgate, Installationsnachweis,
Publikationsplan und finale Audits. Historische Testgrenzen gehören weiterhin
in die verlinkten ursprünglichen Testberichte.
