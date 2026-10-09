# Aktuelle Fixauslieferung im EMPCO-Beobachtungsplan

Der Reader-Folgefix aus Suite-Quellen d3ed071 und Shared-Quellen 8e27ad3 erklärt die Argumentpositionen des Checkers und Dokuments. Er ergänzt die zuvor ausgelieferten Korrekturen zu Wiederverwendung, Prozessmetadaten und Guardgrenzen. Sol 6.1/high und Opus 5.5/high haben denselben Patch nach vollständigem Ergebnisaustausch angenommen. Der geänderte Befehlextraktions-Consumer-Test besteht; neun gezielte Luna-6/medium-Verständnisentscheidungen stimmen mit den vorab festgelegten Anforderungen überein. Keine allgemeine praktische Wirksamkeit behauptet.

Ein aktueller Releasebuild liegt unter skills/temp/release. Alle 13 lokalen Codex-/Claude-Pakete und beide festen Suite-Verzeichnisse sind bytegleich synchronisiert; persönliche Einstellungen blieben erhalten. Reloadhinweis an Runner 01a120d7-5fcf-7122-b741-76eb3a203fc5 zugestellt. Seine tatsächliche Neulektüre dieses Builds ist noch nicht geprüft.

| GitHub-Ziel | Release | Commit |
| --- | --- | --- |
| scoville-suite | [v2.4.11](https://github.com/benjaminstelzer/scoville-suite/releases/tag/v2.4.11) | ae0ffaa |
| scoville-suite-for-codex | [v2.4.14](https://github.com/benjaminstelzer/scoville-suite-for-codex/releases/tag/v2.4.14) | 53c5076 |
| scoville-code | [v2.1.11](https://github.com/benjaminstelzer/scoville-code/releases/tag/v2.1.11) | 1e1b530 |
| scoville-handoff | [v2.1.10](https://github.com/benjaminstelzer/scoville-handoff/releases/tag/v2.1.10) | 72f8825 |
| scoville-plan | [v1.12.11](https://github.com/benjaminstelzer/scoville-plan/releases/tag/v1.12.11) | afe089f |
| scoville-ui | [v2.1.10](https://github.com/benjaminstelzer/scoville-ui/releases/tag/v2.1.10) | 014d4d8 |
| scoville-ask-for-codex | [v1.4.10](https://github.com/benjaminstelzer/scoville-ask-for-codex/releases/tag/v1.4.10) | a8d3b6f |

Vollständige Remote-Dateibäume, annotierte Tags, Release-Inhalte und Asset-Digests sind verifiziert. Die sieben ZIPs entsprechen ihren Buildbäumen. Unveränderte Viewer-1.4.3-Dateien mit Actions-Herkunft und SHA-256-Nachweis hängen an beiden Suites und Plan. Sichtbarkeit und Topics blieben erhalten. Ersetzte Releases und Versionstags wurden erst nach Ersatzprüfung entfernt; je ein aktuelles Release/Tag verbleibt. Unveränderte Runtime- und Viewer-Nachweise wurden wiederverwendet.

Windows blockierte das Entfernen eines vorbereiteten General-Exports; ein anschließender Löschaufruf wurde automatisch abgewiesen. Der Rest wurde stattdessen sicher nach C:/Users/benja/Desktop/_delete/reader-followfix-export-prepared-general-20261009-d3ed071 verschoben. Nur der noch offene Codex-Export wurde fortgesetzt, keine erfolgreichen Paketbuilds oder Tests wiederholt. Die erste Branch-Abfrage nach dem General-Push zeigte einen abweichenden Commit; spätere API- und Git-Remote-Abfrage bestätigten den erwarteten Stand vor Fortsetzung allein des fehlenden Releases.

Technische Belege: temp/2026-10-09-reader-folgefix/ im Workspace. [Befunde und Verständnisgrenzen](0053-empco-abschluss-befunde.md). Die Überwachung bleibt auf denselben EMPCO-Lauf begrenzt; während Fixphasen pausiert sie. Aktuelle tatsächliche Auditgrenzen stehen im überschreibbaren state.json und wurden durch die Auslieferung nicht vorgerückt.
