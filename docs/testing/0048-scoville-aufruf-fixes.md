# PLAN-0048: Umsetzung und gezielte Abnahme

Der Opus-5.5/high- und GPT-6.1/xhigh-Konsens ist in den kanonischen Quellen umgesetzt. Die EMPCO-Überwachung wurde auf Nutzerwunsch gelöscht; der EMPCO-Workflow wurde nicht verändert. Der beobachtete historische Umfang bleibt in [PLAN-0047](0047-empco-beobachtungsbefunde.md) begrenzt.

## Änderungen

- Workflow erzeugt vollständige, korrekt quotierte Readerbefehle für Managerprotokoll, Auftrag und erforderliche Skilldokumente. Protokoll vor READY, Auftrag und weitere Dokumente nach START; die gemeinsame Readererklärung steht einmal im Einstieg.
- Der Windows-Prozessstart behält ProcessStartInfo und die bestehende Argumentquotierung. Start-/Wartefehler nennen das Programm und die vollständige Ausnahme, liefern Status 125 und stoppen abhängige Arbeit. Kindfehler behalten ihren Status; Erfolg beendet die aufrufende Shell nicht.
- `check_text_size.py --file <artifact> --sha256 --max-output-tokens <limit>` liefert ausschließlich Originalbytezahl und SHA-256. Der Verbraucher vergleicht den erwarteten Hash. Fehler oder Abweichung stoppen abhängige Arbeit; anschließend bleibt vollständiges Lesen aller unveränderten Teile erforderlich. Normale Quellen brauchen keine zusätzliche Hashprüfung.
- Gemeinsame Texte erklären direkte PowerShell-Aufrufe, unveränderte generierte Befehle und `rg <directory> -g <pattern>` ohne verschachtelte Shell oder erwartete Globexpansion durch `--run`.
- Plan edit.md ordnet Aktionen Steps, beobachtete Ergebnisse Evidence und zusätzliche aktuelle Bedingungen Instructions zu. Bindende Schutzregeln und ausstehende Reviews bleiben erhalten.

## Prüfungen

Acht gezielte unittest-Fälle bestehen auf beiden Systemen:

1. Hashmodus: korrekte Originalbytezahl und Prüfsumme, geänderte Bytes, Budget einschließlich Zeilenende und Fehlerdiagnosen, ungültige Kombinationen, fehlende/ungültige UTF-8-Dateien, keine Dateiänderung.
2. Prozessaufruf: leere Argumente, Leerzeichen, Apostroph, Anführungszeichen, Backslash und Shellzeichen; Erfolg mit nachfolgendem Shellbefehl, Kindfehler, stderr und fehlendes Programm.
3. Sämtliche sieben erzeugten Manager-Readerbefehle lesen die tatsächlichen Dokumente vollständig und bytegetreu.
4. Bestehende UTF-8-Dateiverbraucher und Größenprüfung in allen vier Paketvarianten.
5. Vollständige Rekonstruktion budgetierter UTF-8-Teile und Ablehnung ungültiger Leseaufrufe.
6. Generierte Teilreader und vollständige Kommandoausgabe erreichen die echte Shell mit unverändertem Ergebnis und Status.
7. Exakte Paketdateien, Helperregistrierung und Testquellen entsprechen den vorbereiteten Hashinventaren.
8. Bestehende Workflow-Verbraucher einschließlich initialem Manager, Nachfolger, Dispatch und gebundenem Plan bestehen.

Windows: Python 3.14.3, PowerShell 5.1.26100.9549 und 7.6.5. Linux: WSL Ubuntu-24.04, Python 3.12.3 und sh. Lauf mit `PYTHONDONTWRITEBYTECODE=1` und `python -B`, entsprechend bestehender CI. Der erste Windows-Test zeigte den fehlenden Programmpfad in der Diagnose; korrigiert und betroffene Prüfungen erneut bestanden. Lokale Cachedateien aus dem ersten Testaufruf wurden entfernt.

Gemeinsamer Snapshot und Quellvorschauen melden `changed=[]`. Vier lokale Testpaketvarianten wurden aus diesen Quellen erzeugt; Inventarprüfung und `git diff --check` bestehen. Testkandidat: `temp/2026-10-09-scoville-aufruf-fixes/runtime` im Workspace. Keine Veröffentlichung oder Installation.

## Grenzen

Kein neuer Luna-Verständnistest und keine neue Modellabnahme der Umsetzung: weniger Fehlanwendung ist nicht bewiesen. Die technischen Tests decken die geänderten Verträge und Verbraucher ab, nicht sämtliche Suitefunktionen. Keine EMPCO-Tests oder Agentennachrichten.

Skill-Creator quick_validate lehnt bei Plan und Workflow ausschließlich das unveränderte Frontmatterfeld `compatibility` ab; kein neuer Metadatenfehler wurde daraus abgeleitet und das Feld nicht entfernt. Der Paket-Helpercheck benötigt ein Release-Build mit Receipt; hier wurden lokale Testpakete und deren vollständiges Inventar geprüft. Keine Validator-, Evidence- oder Host-Routingänderungen.
