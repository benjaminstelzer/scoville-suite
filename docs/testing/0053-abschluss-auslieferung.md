# Aktuelle Fixauslieferung im EMPCO-Beobachtungsplan

Der Suchpfad-Fix aus Suite-Quellen f34e97a und Shared-Quellen 1f7b930 trennt exakte vorhandene Pfade von Dateimustern in rg -g. Einzeldateien, Verzeichnisse und reguläre Suchausdrücke bleiben erlaubt; kein neuer Prüfschritt. Frühere Reader-, Helferaufruf-, Wiederverwendungs-, Prozessmetadaten- und Guardkorrekturen bleiben enthalten. Sol 6.1/high und Opus 5.5/high nahmen denselben tatsächlichen Patch nach vollständigem Ergebnisaustausch an.

Luna 6/medium: Vier klare Erstentscheidungen am isolierten Absatz und ein frischer einfacher C-Fall bestehen. Ursprüngliche unaufgelöste Testvorlage, der fehlerhafte Regex im Test und die anschließende Escape-Verfälschung zählen nicht als vollständiger Erfolg. Vergleich mit bisherigem Text beweist keine Verbesserung gegenüber dem alten Text: dessen vier eindeutige Vergleichsfälle stimmen ebenfalls. Geprüft ist begrenztes Verständnis, keine Ausführung oder Live-Zuverlässigkeit.

Ein aktueller Releasebuild liegt unter skills/temp/release. Alle 19 Paketprojektionen, 13 lokale Codex-/Claude-Pakete und beide festen Suite-Verzeichnisse sind vollständig geprüft beziehungsweise bytegleich synchronisiert; persönliche Einstellungen blieben erhalten. Reloadhinweis an Runner 01a120d7-5fcf-7122-b741-76eb3a203fc5 zugestellt. Neulektüre dieses neuesten Builds ist noch nicht beobachtet.

| GitHub-Ziel | Release | Commit |
| --- | --- | --- |
| scoville-suite | [v2.4.13](https://github.com/benjaminstelzer/scoville-suite/releases/tag/v2.4.13) | 41280e6 |
| scoville-suite-for-codex | [v2.4.16](https://github.com/benjaminstelzer/scoville-suite-for-codex/releases/tag/v2.4.16) | 5af33dc |
| scoville-code | [v2.1.13](https://github.com/benjaminstelzer/scoville-code/releases/tag/v2.1.13) | 275e714 |
| scoville-handoff | [v2.1.12](https://github.com/benjaminstelzer/scoville-handoff/releases/tag/v2.1.12) | db3f4ff |
| scoville-plan | [v1.12.13](https://github.com/benjaminstelzer/scoville-plan/releases/tag/v1.12.13) | 45f5431 |
| scoville-ui | [v2.1.12](https://github.com/benjaminstelzer/scoville-ui/releases/tag/v2.1.12) | 453262c |
| scoville-ask-for-codex | [v1.4.12](https://github.com/benjaminstelzer/scoville-ask-for-codex/releases/tag/v1.4.12) | 90fcfa4 |

Vollständige Remote-Dateibäume, annotierte Tags, Release-Inhalte und Asset-Digests sind verifiziert. Die sieben ZIPs entsprechen ihren Buildbäumen. Unveränderte Viewer-1.4.3-Dateien mit Actions-Herkunft und SHA-256-Nachweis hängen an beiden Suites und Plan. Sichtbarkeit und Topics blieben erhalten. Ersetzte Releases und Versionstags wurden erst nach Ersatzprüfung entfernt; je ein aktuelles Release/Tag verbleibt. Unveränderte Runtime-, README- und Viewer-Nachweise wurden wiederverwendet.

Die unmittelbare GitHub-Branchprüfung stoppte Handoff nach dem Push wegen einer abweichend gelesenen Commit-ID. Die spätere Abfrage bestätigte den erwarteten Commit und unveränderte übrige Inputs; nur der fehlende Release wurde fortgesetzt und verifiziert. Erfolgreiche Veröffentlichungen wurden nicht wiederholt. Windows hielt Teile temporärer Exportordner fest; ein nativer Verschiebeversuch führte nur teilweise nach _delete. Genaue verbleibende Pfade stehen in state.json, geprüftes Staging bleibt vollständig. Keine Test- oder Uploadwiederholung wegen Bereinigung.

Technische Belege: temp/2026-10-09-rg-path-fix/ im Workspace. [Befunde und Verständnisgrenzen](0053-empco-abschluss-befunde.md). Die Überwachung wird für denselben EMPCO-Lauf fortgesetzt. Die Auslieferung ersetzt keinen Aktionsaudit; geprüfte Grenzen bleiben in state.json erhalten.
