# Skillwriter-Fixplan: Astra-Review vom 2026-09-25

Geprüft wurde [PLAN-0008](../../../docs/plans/0008-plan-skillwriter-compatibility.md), nicht die Umsetzung einer neuen Skillversion. Der Nutzer verlangt insbesondere, dass alte Pläne und laufende Projekte nach einem Upgrade ohne Migration weiter funktionieren. Die getrennten general-/codex-Verträge bleiben erhalten.

## Review und Bearbeitung

Astra bewertete den Entwurf als grundsätzlich ausführbar und sinnvoll begrenzt. Es gab zwei P2-Befunde und keine P0-/P1-Befunde:

1. W-001 Acceptance schränkte erlaubte todo-Planpflege und die bestehende Execute-Ausnahme zu stark ein. Am nativen Work-Item-Vertrag bestätigt und korrigiert: reine Lektüre und Upgrade bleiben byte-stabil; beauftragte Pflege und Fortschritt werden gegen ihre jeweils bisher erlaubten Diffs geprüft.
2. Bestehende evaluation-cases enthalten veraltete Sollwerte für fehlende Helper und dateibasierte Steps. In `evaluation-cases.json` bestätigt. W-001 verlangt nun vor dem Vergleich einen begründeten Sollwertabgleich für `validator-unavailable-preserves-manual-fallback`, `large-plan-progress-selective-output` und `compact-plan-is-worker-ready`, einschließlich expliziter Erwartungen für beide gerenderten Profile.

Zusätzlich wurde klargestellt: Fortsetzungsfälle müssen tatsächlich auf isolierten Projektkopien schreiben und ihre Diffs prüfen. Bloße Antwortsimulation beweist keine Upgrade-Verträglichkeit.

Die zwei Befunde wurden vom erstellenden Agenten im Plan eingearbeitet und gegen die angegebenen Quellen geprüft. Die korrigierte Fassung erhielt kein zweites Astra-Review. Skillquellen, Helper und Testfälle wurden nicht geändert. PLAN-0008 bleibt `draft`; es wurde keine Umsetzung oder Aktivierung gestartet.

## Nachweise und Grenzen

- Geprüfter Entwurf SHA-256: `a20ee69e105ca0bd5122be11c59d0a9bf037436b29b155e34c9cbdda6985af19`.
- Korrigierter Plan SHA-256: `c8bb6f069e4905c2f859a2906f119b8d587b432734565788a4fc072cd5aa33fa`.
- Nativer Profilvalidator nach Korrektur: `valid: true`, 0 Fehler, 0 Warnungen; 25 Dateien, 7 Pläne, 68 Work Items und 17 Decisions. Parallel entstanden andere Projektakten; deren Umsetzung war nicht Gegenstand dieses Reviews.
- Astra führte ausschließlich Quellprüfung durch, keine Builds, Tests oder Upgrade-Proben. Die geplanten Kompatibilitätstests sind noch auszuführen; weder dieses Review noch Strukturvalidierung beweisen die Verträglichkeit einer zukünftigen Skillfassung.
- Angefordert: `gpt-6-astra`, Reasoning `high`; tatsächliche Modell-/Effort-Metadaten vom Host nicht exponiert. `context_mode: fresh`.
- Zustellung vollständig empfangen und mit dem Task-Lifecycle-Helper erfolgreich gegen Task, Referenz und Scope abgeglichen. Reviewer bleibt für Follow-ups offen.

## Retained task handle

```json
{
  "state": "ready",
  "family": "ask",
  "role": "adviser",
  "projectId": "d6642364-f303-420e-9399-d059324ad8a5",
  "title": "ASK PLAN-0008 Skillwriter ASTRA RUN [#1]",
  "reference": "plan-0008-skillwriter-astra-20260925-01",
  "prior_task_ids": [],
  "threadId": "01a0d7a3-1010-7110-8dfe-d8eea5a1b085",
  "hostId": "local"
}
```

Return task: `01a0d79a-cc19-7140-b08c-f0e21b3f17d3`. Scope: `PLAN-0008 Skillwriter-Fixplan und Bestandskompatibilität`.
