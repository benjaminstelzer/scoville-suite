---
format_version: 1
id: ADR-0048
status: accepted
created: 2026-09-25
accepted: 2026-09-25
scope: plan/writing-profile
transition_batch: f4ac9627ee1ebc83f5a18c0e13e4603d1b8485d4b1e82bf5fda3951a69d634b4
transition_batch_members: [ADR-0047, ADR-0048, ADR-0049, ADR-0050, ADR-0051]
---

# Plan-Schreiben ohne verpflichtende Modellprofilauswahl

## Decision

Empfohlen: Plan direkt auf eine kompakte vollständige Schreibregel ohne Modellprofilresolver umstellen. Kein vorgeschalteter Fallback-Umbau. Workflow kann optionale Profile für eigene Zusatzanweisungen behalten, wenn ihr Nutzen belegt ist.

## Problem

Eine Formulierungshilfe blockiert Plan-Schreiben bei altem Python; ihre verpflichtende Auswahl verursacht zusätzliche Arbeit.

## Drivers

- Codex behält bis zu einer ausdrücklich anderen Entscheidung seine geeignete Python-Laufzeit.
- Fehler eines geeigneten Helpers oder einer ungültigen Konfiguration werden nicht als fehlendes Python kaschiert.
- ADR-0014 besitzt den bisherigen gemeinsamen Profilvertrag.

## Considered alternatives

- Eigener TOML-Parser für Python 3.10: zusätzliche Pflege für eine Formulierungshilfe.
- Bestehende manuelle Route für general erweitern: nur als separat benötigter Vorabfix, wenn die direkte Resolverentfernung warten muss; nicht Teil des empfohlenen Standardablaufs.
- Planresolver entfernen: einfachster Dauerweg, erfordert gezielte Ablösung des Plan-Anteils von ADR-0014.

## Consequences

- Erst nach Annahme den betroffenen Teil von ADR-0014 ordnungsgemäß ersetzen; keine stille Historienänderung.
- Kontextvollständigkeit, Acceptance und Autorisierung bleiben unabhängig vom Profil erhalten.
- Die entfallende Modellprofilpflicht ist von Validator-/Selector-Laufzeiten getrennt. Codex behält die bisherige geeignete Python-Laufzeit für weiterhin erforderliche Helper; deren Fehler bleiben sichtbar.
- Dieser Vorschlag entscheidet weder Evidence-Syntax noch Workflowrollen.

## Confirmation

1. Prüfe F-01 am gebauten general-Profil: Eine Planänderung mit Python 3.10 läuft ohne Modellprofilresolver und ohne dessen Konfiguration bis zur erfolgreichen Validatorprüfung. Die Schreibregel bleibt vollständig.
2. Prüfe den unveränderten Vertrag der weiterhin benötigten Validator-/Selector-Helper separat: insbesondere codex ohne geeignete Laufzeit bleibt sichtbar blockiert. Workflow-Verbraucher gemeinsam genutzter Helper funktionieren weiterhin.
3. Vergleiche typische Planänderungen mit dem zuvor gesicherten Ausgangsstand auf Ergebnis, Verständlichkeit und Aufwand. Nur bei separat gewähltem Vorabfix zusätzlich die alte-Python-Fallback-Matrix prüfen.

## Revisit when

Die einfache Schreibregel in realen Aufgaben nachweislich benötigte Empfängerinformationen verliert.
