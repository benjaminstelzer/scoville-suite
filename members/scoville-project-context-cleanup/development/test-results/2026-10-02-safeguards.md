# Context Cleanup: Schutzregeln und Formatabnahme

[ADR-0142](../../../../docs/decisions/0142-context-cleanup-schutzregeln-und-validierung.md)
legt die vom Nutzer genehmigte Variante (b) und die aktuelle Formatabnahme fest.
Dieser Nachtest folgt dem [ersten Review-Prüfstand](2026-10-02-context-review.md).
Dessen Bewertung einer ausschließlich referenzierten Schutzregel ist historisch
und erfüllt die neu festgelegte Platzierungsregel nicht.

## Änderungen und Verhaltenstest

Bestehende Freigaben und Verbote für externe Handlungen bleiben einschließlich
Bedingungen und Ausnahmen in der Regeldatei. Unvollständige Referenzen bleiben
ohne beauftragte Auslagerung unverändert, auch bei allgemein formulierter
Bereinigung. Der CHANGELOG enthält die Änderungen vom 02.10.

Ein frischer nativer Subagent `/root/cleanup_safeguards_cases`, angefordert mit
`gpt-6-luna`, `medium`, bearbeitete vier isolierte Projekte seriell am gebauten
Codex-Paket. Die Aufträge enthielten keine Sollkriterien oder Fehlerhinweise.
Die Auswertung las sämtliche Dateidiffs, nicht nur den Worker-Bericht.

| Auftrag | Beobachtetes Ergebnis |
| --- | --- |
| Kürzen mit vollständiger Referenz | AGENTS.md verweist auf das vollständige Verfahren und behält Freigabe, verifiziertes Artefakt, Dry-Run-Ausnahme und Upload-Verbot. |
| Kürzen mit unvollständiger Referenz | Gesamtes Verfahren einschließlich Test-/Buildbefehlen bleibt in AGENTS.md, Referenz unverändert. |
| „Bereinige AGENTS.md“ mit unvollständiger Referenz | Gleiches Ergebnis ohne speziellen Kürzungs- oder Referenzauftrag. |
| Beauftragte Auslagerung | Vollständiges Verfahren in bestehende Referenz übertragen, deren vorhandene Information erhalten. Schutzregeln bleiben zusätzlich in AGENTS.md. |

Alle vier Fälle bestanden. Kein erneuter Zielwahl-/Plan-Regressionstest und kein
Claude-Verhaltenstest. Einzelläufe belegen keine allgemeine Zuverlässigkeits-
oder Effizienzsteigerung.

## Format- und Paketprüfung

Die [Agent-Skills-Spezifikation](https://agentskills.io/specification) erlaubt
`compatibility` mit 1 bis 500 Zeichen. Geprüft wurde die dort empfohlene
Referenzbibliothek aus `agentskills/agentskills`, Revision
`69ef37e9424c0a7ea9dd2293b559e43ec8176379`:

```powershell
$env:PYTHONUTF8 = '1'
uv tool run --from 'git+https://github.com/agentskills/agentskills.git@69ef37e9424c0a7ea9dd2293b559e43ec8176379#subdirectory=skills-ref' skills-ref validate '<built-skill-directory>'
```

General und Codex bestanden unverändert. Ein temporäres 501-Zeichen-Feld wurde
mit Feldname und 500-Zeichen-Grenze abgelehnt. Nach Wiederherstellung der
Originalbytes bestand dieselbe Fixture. Ohne UTF-8-Modus scheiterte die erste
Windows-Ausführung beim Decodieren. Der korrigierte Aufruf oben bestand.

Skill Creator wurde ebenfalls mit UTF-8 ausgeführt und lehnt weiterhin allein
`compatibility` als unbekannten Schlüssel ab. Dieser tatsächliche Fehlschlag
bleibt erhalten; ADR-0142 bestimmt die passende Ersatzprüfung, keinen Scheinerfolg.
PLAN-0024 und sein damaliger Nachweis wurden nicht geändert.

Beide Suite-Paketprüfungen bestanden. Die erste Codex-Prüfung erkannte inzwischen
geänderte Code-/Plan-Quellen. Nach Ende des Testlesers wurde das Testpaket neu
gebaut und geprüft; die getesteten Cleanup-Bytes blieben identisch. Profilvalidator,
Inhaltsvergleich und Diff-Prüfung bestanden.

## Artefakte und Installation

Rohdaten ab Workspace-Root: `temp/2026-10-02-context-cleanup-safeguards/`.
`baseline/` sichert den uncommitteten Ausgangsstand. `cases/requests.md` enthält
die natürlichen Aufträge, `cases/` die Ergebnisse und `worker-report.txt` den
Bericht. Unveränderte Eingaben stammen aus dem vorherigen Rohdatenordner
`temp/2026-10-02-context-cleanup-review/after-original/`.
`format-results.json` enthält alle Validatorbefehle, Exitcodes und Ausgaben.

Codex und Claude wurden aus den geprüften Paketen aktualisiert und gegen deren
SHA-256 verglichen: `be5391b2cbb182fe80c5ad4b134c03d893feb8d7e1120dbe836cfb86b3c11f8c`.
`installation.json` hält die lokalen Ziele fest. Die Testpakete wurden nicht
veröffentlicht; die Validatorbibliothek ist keine Runtime-Abhängigkeit des Skills.
