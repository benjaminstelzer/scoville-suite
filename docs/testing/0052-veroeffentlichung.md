# Veröffentlichung der Aufrufhilfen

Der Releasebuild stammt aus Suite-Commit 859c9f18fc5df79cd01341ebbfc5d61296ec717e und Shared-Commit 792b4a4. Gegenüber dem funktional abgenommenen Stand 758a9fd kamen nur Versionsnotizen und Planfelder hinzu. Die gezielten Windows/Linux-Consumerchecks, sechs Luna-Medium-Verständnisproben und der Sol/high-Review aus W-002 werden wiederverwendet, ohne eine neue Gesamtmatrix zu behaupten.

Alle sieben manifestbestimmten Ziele waren geändert. Vollständige Remote-Dateien, stabile Releases, annotierte Tags, Zielcommits, Release-Text und Asset-Digests wurden geprüft. Sichtbarkeit, Topics und Installationspfade bleiben erhalten. Je Ziel verbleibt genau ein aktuelles Release mit einem Versions-Tag.

| Ziel | Release | Commit | Assets |
| --- | --- | --- | --- |
| Suite | [v2.4.9](https://github.com/benjaminstelzer/scoville-suite/releases/tag/v2.4.9) | 62be760 | 14 |
| Suite für Codex | [v2.4.10](https://github.com/benjaminstelzer/scoville-suite-for-codex/releases/tag/v2.4.10) | d119de7 | 14 |
| Code | [v2.1.9](https://github.com/benjaminstelzer/scoville-code/releases/tag/v2.1.9) | dd7fb19 | 2 |
| Handoff | [v2.1.8](https://github.com/benjaminstelzer/scoville-handoff/releases/tag/v2.1.8) | b379f57 | 2 |
| Plan | [v1.12.9](https://github.com/benjaminstelzer/scoville-plan/releases/tag/v1.12.9) | aed1cee | 14 |
| UI | [v2.1.8](https://github.com/benjaminstelzer/scoville-ui/releases/tag/v2.1.8) | 42a86ae | 2 |
| Ask für Codex | [v1.4.8](https://github.com/benjaminstelzer/scoville-ask-for-codex/releases/tag/v1.4.8) | e38e1ea | 2 |

Plan Viewer 1.4.3 bleibt unverändert. Seine vorher verifizierte Actions-Provenienz wurde nur bei identischen Viewerquellen und allen identischen Assetbytes wiederverwendet. Beide Suite-Releases und Plan tragen jeweils sämtliche elf Anwendungen/Installer und SHA256SUMS.txt direkt. Keine neue Viewerkompilierung oder macOS-Laufzeitabnahme.

Alle 13 lokalen Skill-Installationen sind bytegleich zum Build. Beide festen lokalen Suiteexports und ZIPs sind aktuell. Beim Export lehnte der Helper ein bestehendes Ausgabeverzeichnis ab; die bereits erfolgreichen Paket- und Installationsschritte wurden erhalten, der Export über ein frisches Verzeichnis abgeschlossen. Keine dadurch verursachten Skilländerungen.

EMPCO hat die Neuladung gemeldet. Das beweist noch keine fehlerfreie praktische Anwendung. W-001 setzt die Beobachtung fort. Vorherige Befunde und Testgrenzen bleiben im Auslieferungsnachweis erhalten. Technische Veröffentlichungsnachweise: temp/2026-10-09-plan0052-release/ im Workspace. Kein Profil- oder Familienbestand geändert.
