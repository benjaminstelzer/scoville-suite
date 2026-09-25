---
format_version: 1
id: ADR-0051
status: superseded
created: 2026-09-25
accepted: 2026-09-25
scope: suite/project-configuration
superseded_by: ADR-0061
transition_batch: f4ac9627ee1ebc83f5a18c0e13e4603d1b8485d4b1e82bf5fda3951a69d634b4
transition_batch_members: [ADR-0047, ADR-0048, ADR-0049, ADR-0050, ADR-0051]
---

# Eine gemeinsame Konfigurationsdatei pro Projekt

## Decision

Empfohlen: `.scoville/config.json` in der kanonischen Projektwurzel enthält projektbezogene Einstellungen für ASK und Workflow sowie Plan nur bei verbleibendem Bedarf. Die Rangfolge lautet explizite Anfrage oder Plan-Step, Projektdatei, persönliche Datei im jeweiligen Skill, mitgelieferte Defaults. Skill-Einstellungen sind damit Vorgaben für Projekte ohne eigene Auswahl.

## Problem

ASK erhält Projekteinstellungen bisher als übergebenes Objekt; Workflow lädt seine Installationstabelle. Es fehlt ein einheitlicher, direkt bearbeitbarer Projektbesitzer.

## Drivers

- Der Nutzer möchte Modellwahl innerhalb des Projekts speichern.
- ADR-0046 erhält persönliche Konfiguration im Skill und vermeidet Absicherung laufender Einstellungswechsel.
- Vorhandene Adviser- und Routingbegriffe sollen erhalten bleiben.

## Considered alternatives

- Eine Datei pro Skill im Projekt: einfache Einzelzuordnung, aber verstreute Einstellungen.
- Eine gemeinsame Projektdatei mit getrennten Bereichen: ein Ort und ein Ladeweg, begrenzte gemeinsame Validierung.
- Einstellungen in Plan-Records oder AGENTS.md: vermischt konkrete Arbeitsanforderungen beziehungsweise Anweisungen mit maschinenlesbaren Defaults.

## Consequences

- Die Datei verwendet `schema_version: 1` und optionale Bereiche `workflow`, `ask` und gegebenenfalls `plan`. Beispiel:

```json
{
  "schema_version": 1,
  "workflow": {
    "execute": {
      "low": { "model": "chosen-model-id", "reasoning": "medium" }
    }
  },
  "ask": {
    "presets": {
      "sol": { "model": "chosen-model-id", "effort": "high" }
    }
  }
}
```

- Das Beispiel zeigt die Form, keine ausführbare Modellvorgabe. IDs und erlaubte Werte werden gegen den jeweiligen Anbieter geprüft.
- Bestehende Workflow-Paare und ASK-Presets bleiben in ihren Bereichen erhalten. Keine zusätzliche gemeinsame Rollen- oder Modellsprache.
- Eine kleine kanonische Ladefunktion in `../shared/runtime/` liest genau die ausgewählte Projektwurzel und liefert den jeweiligen Bereich. Der Build bündelt sie in jedem betroffenen Skill. Kein Laufzeitimport aus einem Geschwisterskill.
- Projektwurzel ist dieselbe explizit aufgelöste Wurzel wie für Plan beziehungsweise ASK-Auftrag. Keine Suche über Eltern-/Homeverzeichnisse und keine zweite Prioritätskaskade für Monorepos.
- Fehlende Datei oder Werte verwenden niedrigere Ebenen. Ungültiges JSON oder ungültige Werte liefern eine konkrete Fehlermeldung; kein stiller Default bei Tippfehlern.
- ASK behält seinen expliziten Objektparameter als kompatiblen Aufruf-Override. Seine vollständige Reihenfolge lautet Defaults < persönliche Skilldatei < Projektdatei < request.project_config < request.overrides. Bei Datei und abweichendem project_config gewinnt also das ausdrücklich übergebene Objekt; overrides gewinnt weiterhin zuletzt.
- Der vorhandene ASK-Mergevertrag bleibt innerhalb jeder Ebene maßgeblich für Listen und Presets. Eine neue generische Tiefenverschmelzung darf Adviserlisten nicht unerwartet kombinieren.
- Einstellungen enthalten keine Zugangsdaten. Projektdatei darf bewusst versioniert werden; kein automatischer Commit. Eine per Git oder Dropbox geteilte Projektwahl überschreibt persönliche Skill-Defaults auf jedem Rechner. Das ist der beabsichtigte projektbezogene Vorrang und wird in der README erklärt.
- Die Datei ist optional und wird beim bloßen Lesen nicht angelegt. Ohne laufenden Auftrag können Modelle direkt geändert werden. Keine Hashes, Snapshots oder Konfigurationsüberwachung.

## Confirmation

1. Prüfe ohne Projektdatei die bisherige Auswahl und mit Projektdatei nur die gewollten Overrides.
2. Prüfe die Rangfolge einschließlich explizitem Step und persönlicher Skilldatei sowie ungültige Dateien. Prüfe bei ASK einen abweichenden Wert gleichzeitig in Projektdatei, project_config und overrides und den Erhalt der bisherigen Adviser-/Preset-Semantik.
3. Prüfe dieselbe Projektdatei über die tatsächlich gebauten ASK-/Workflow-Pakete und die unveränderte Auswahl von Advisern.

## Revisit when

Ein reales Monorepo mehrere ausdrücklich getrennte Projektwurzeln benötigt oder ein weiterer Member tatsächlich Modelle auswählt.
