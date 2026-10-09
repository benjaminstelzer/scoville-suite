# Aktuelle Fixauslieferung im EMPCO-Beobachtungsplan

W-010 und W-011 sind aus Suite b0a8b5e und Shared d2c0a42 ausgeliefert. Temporäre Lese-Captures brauchen die Erlaubnis der aktuellen Rolle und Phase für diese konkrete Datei. Der Entwicklungs-Export prüft seinen Snapshot gegen vorhandene kanonische Geschwisterquellen; isolierte veröffentlichte Bäume bleiben selbstständig. Frühere Reader-, Wiederverwendungs-, Guard- und Suchpfadkorrekturen bleiben enthalten.

Sol 6.1/high und Opus 5.5/high nahmen den tatsächlichen Stand nach vollständigem gegenseitigem Austausch ab. Exporttests 2 und Build-Abnahmetests 6 bestehen. Eine injizierte unbekannte öffentliche Spiegeldatei stoppt vor sämtlichen Paketänderungen. Luna 6/medium trifft vier klare Capture- und drei konzeptionelle Quellen-/Installationsentscheidungen korrekt. Testgrenzen stehen im Befundbericht; keine allgemeine Verbesserung, Ausführungssicherheit oder Live-Wirkung behauptet.

Alle 19 aktuellen Paketprojektionen sind geprüft. Die vollständigen Paketbytes beider Suite-Exporte stimmen mit allen 13 passenden Buildprojektionen überein. 13 lokale Codex-/Claude-Pakete und beide festen öffentlichen Suite-Spiegel sind bytegleich aktualisiert; persönliche Einstellungen blieben erhalten. Unbekannte lokale Dateien bleiben geschützt. Reloadhinweis an genau Runner 01a120d7-5fcf-7122-b741-76eb3a203fc5 zugestellt; vollständige neue writing.md beim Runner, Manager14 und Worker18 tatsächlich beobachtet. Allgemeine Live-Wirkung bleibt ungeprüft.

| GitHub-Ziel | Release | Commit |
| --- | --- | --- |
| scoville-suite | [v2.4.14](https://github.com/benjaminstelzer/scoville-suite/releases/tag/v2.4.14) | 3aea42e |
| scoville-suite-for-codex | [v2.4.17](https://github.com/benjaminstelzer/scoville-suite-for-codex/releases/tag/v2.4.17) | e99fa4c |
| scoville-code | [v2.1.14](https://github.com/benjaminstelzer/scoville-code/releases/tag/v2.1.14) | 895e24a |
| scoville-handoff | [v2.1.13](https://github.com/benjaminstelzer/scoville-handoff/releases/tag/v2.1.13) | 0d5f88e |
| scoville-plan | [v1.12.14](https://github.com/benjaminstelzer/scoville-plan/releases/tag/v1.12.14) | 4cd2fdf |
| scoville-ui | [v2.1.13](https://github.com/benjaminstelzer/scoville-ui/releases/tag/v2.1.13) | 5ef7786 |
| scoville-ask-for-codex | [v1.4.13](https://github.com/benjaminstelzer/scoville-ask-for-codex/releases/tag/v1.4.13) | f43c4aa |

Vollständige Remote-Dateibäume, annotierte Tags, Release-Inhalte, ZIP-Dateibäume und Asset-Digests sind verifiziert. Unveränderte Runtime-, README- und Viewer-1.4.3-Nachweise mit Actions-Herkunft wurden wiederverwendet. Sichtbarkeit und Topics blieben erhalten. Ersetzte Releases und Versionstags wurden nach geprüfter Auslieferung entfernt; je ein aktuelles Release/Tag verbleibt.

Die vorherige Veröffentlichung enthielt trotz korrekter lokaler Pakete einen veralteten Shared-Snapshot. Dieser Nachweis schränkt die frühere Behauptung einer konsistenten Auslieferung ein; der Quellen-Gate und aktuelle vollständige Projektionsvergleich beheben diese Grenze. Details: [Befunde](0053-empco-abschluss-befunde.md). Technische Belege: temp/2026-10-09-takeover-capture-fix/. Der aktuelle Releasebuild liegt unter skills/temp/release.

Die Beobachtung desselben EMPCO-Laufs wird fortgesetzt. Die Auslieferung ersetzt keinen Aktionsaudit: Fixpausenaktionen sind bis zu den exakten gespeicherten Grenzen einschließlich Manager14 und Worker18 geprüft; spätere Aktionen bleiben offen. Native Kontrollnachrichten und tatsächliche Modelltelemetrie bleiben unsichtbar.
