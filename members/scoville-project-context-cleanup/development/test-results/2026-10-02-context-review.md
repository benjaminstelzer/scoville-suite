# Context Cleanup: Review-Fixes und Nachtests

Historischer Prüfstand vor der anschließend genehmigten Schutzregel-Variante (b).
Die neue Platzierungsregel und Formatabnahme stehen im
[Folgenachweis](2026-10-02-safeguards.md).

Der Nutzer genehmigte die geprüften Vorschläge aus dem Opus-Review: Regeldatei
nach Geltungsbereich wählen, fehlende Projektdatei trotz Workspace-Regeln anlegen,
eigenständig nötige Kopien bewahren und vollständige Referenzen von beauftragter
Auslagerung unterscheiden. Die Diff-Prüfung umfasst alle geänderten Dateien.
Kein Host-Adapter und keine zusätzliche Secrets-Regel wurden ergänzt.

## Versuchsaufbau

Ausgangsrevision: `00bc56b6800aad276950da39cf85c3334172cbd6`; der Skill entsprach
noch `c31ba05`. Acht identische isolierte Projekte je Ausgangs-/Kandidatenlauf.
Vier frische native Subagenten, jeweils angefordert mit `gpt-6-luna`, `medium`,
ohne Gesprächshistorie; Läufe seriell. Sie erhielten natürliche Aufgaben und das
jeweils eingefrorene gebaute Codex-Paket, keine Sollantworten oder Fehlerhinweise.
Bewertet wurden gespeicherte Dateien und Diffs, nicht nur die Abschlussberichte.

Rohdaten ab Workspace-Root: `temp/2026-10-02-context-cleanup-review/`.
`inputs.json` und `prepare_cases.py` enthalten Eingaben und Aufbau;
`before-original/`, `after-original/` die unveränderten Projekte. Paketstände,
Ergebnisdateien und vier `*-report.txt` bleiben dort getrennt erhalten.

| Fall | Geprüftes Ergebnis |
| --- | --- |
| Teilbaumregel ohne Dateinamen | pnpm-Regel nur in `web/AGENTS.md`; Root-Regel bleibt erhalten. |
| Andere zuständige Regeldatei ohne Dateinamen im Auftrag | `PROJECT_RULES.md` ergänzt; keine parallele AGENTS.md. README und Regeldatei belegen den Owner. |
| Gewachsene Regeln | Dublette entfernt, veralteter Verweis belegt korrigiert; Schutzregeln und verbindliche Erhaltungsanweisung für web bleiben bestehen. Bericht nennt relevante Entfernungen ohne Aufforderung dazu. |
| Fremder Index | Neuer Setup-Eintrag in vorhandener Tabelle, ohne Formaterhaltung im Prompt vorzugeben. |
| Vollständige Referenz | Prozedur durch genauen Pfad mit Lesetrigger ersetzt; alle Schritte und Ausnahmen in der unveränderten Referenz vorhanden. |
| Unvollständige Referenz | Bei reinem Kürzungsauftrag bleibt die vollständige Prozedur in AGENTS.md und die Referenz unverändert. |
| Beauftragte Auslagerung | Vollständige Prozedur in bestehende Referenz verschoben; deren vorhandene Information erhalten, AGENTS.md verweist darauf. |
| Neues Projekt mit Workspace-Regeln | Eigene AGENTS.md mit der angeforderten Regel angelegt. |

## Tatsächlicher Verlauf

- `/root/cleanup_baseline_cases`, acht Fälle: Dateiwahl und Bedeutungserhalt
  funktionierten. Im unvollständigen Referenzfall ergänzte der alte Skill die
  Referenz beim bloßen Kürzungsauftrag. Dies zeigt die bisher offene Grenze.
- `/root/cleanup_candidate_cases`, acht Fälle: sechs bestanden. Im gewachsenen
  Fall entfiel die verbindliche Erhaltungsanweisung; der unvollständige
  Referenzfall verteilte das Verfahren auf zwei Dateien. Beide Sätze präzisiert.
- `/root/cleanup_final_cases`, vier betroffene Fälle: Erhaltungsanweisung und
  zwei Referenzfälle bestanden. Die unvollständige Referenz wurde weiterhin
  ergänzt. Daher Kürzung/Referenznutzung ausdrücklich von Auslagerung abgegrenzt.
- `/root/cleanup_reference_cases`, drei Referenzfälle: alle bestanden, anhand
  vollständiger Dateidiffs nach dem damaligen Referenzkriterium bestätigt.
  Damit endete dieser Prüfstand.

Der Worker des Vier-Fälle-Nachtests behauptete, Git-Diffs seien ohne
Repository nicht verfügbar. Die Auswertung verwendete `git diff --no-index`.
Dies rechtfertigt keine zusätzliche allgemeine Git-Regel in diesem Skill.

## Validierung und Grenzen

General- und Codex-Testpakete mit dem kanonischen Builder erzeugt und jeweils
mit `--check-packages` erfolgreich geprüft. README-Mindestanforderung und
Testgrenzen bleiben explizit; gemeinsamer Schreibvertrag und UI-Metadaten sind
unverändert. Abschließender Inhaltsvergleich und `git diff --check` bestanden.

Skill Creators `quick_validate.py` lehnt das bereits bestehende Frontmatter-Feld
`compatibility` ab, auch beim unveränderten Ausgangsstand. Mit `python -X utf8`
entfällt der zusätzliche Windows-Decodierungsfehler. Keine Änderung am Validator
oder an Metadaten vorgenommen; dessen vollständige Freigabe bleibt aus.

Die lokalen Codex-/Claude-Kopien wurden nach Baseline-Abgleich aus den geprüften
Paketen aktualisiert und per SHA-256 bestätigt:
`7d3a6be1b4358998256ffcf22cae75846203216761b3f12b44d3be7288df4416`.
Installationsnachweis: `installation.json` im Rohdatenordner.

Gezielte Einzelläufe belegen die beobachteten Ergebnisse, keine allgemeine
Zuverlässigkeits- oder Effizienzsteigerung. Die unveränderten Zielwahlfälle
wurden nach den abschließenden Referenzkorrekturen nicht erneut ausgeführt.
Kein Claude-Verhaltenstest, kein neuer vollständiger Plan-/Index-Regressionslauf.
Die Pakete sind isolierte Testartefakte, keine Veröffentlichung.
