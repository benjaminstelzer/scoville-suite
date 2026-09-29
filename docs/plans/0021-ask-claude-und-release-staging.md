---
format_version: 1
id: PLAN-0021
status: completed
created: 2026-09-29
updated: 2026-09-29
---

# Ask-Claude und verbleibende Prüfungen abschließen

## Goal

Die am Ende von PLAN-0020 benannten Restprobleme auf Nutzerauftrag beheben:
alte Claude-Genehmigungsfelder entfernen, reale Session-Fortsetzung belegen,
Ask ohne alte installierte Instruktionen prüfen und aktuelles Staging herstellen.

## Non-goals

Kein Commit, Push, Release oder Installation. PLAN-0019 bleibt draft.
Keine Löschung gespeicherter Claude-Gespräche oder Änderung fremder Sessions.

## Work items

### W-001 Restprobleme sind behoben und geprüft

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0115, ADR-0117]
Outcome: Ask-Claude folgt dem einfachen Aufrufvertrag und erhält Session-Rückfragen; Staging entspricht geprüften Quellen.
Acceptance: Helper benötigt keine separaten Genehmigungsfelder. Reale Claude-Beratung und Folgefrage verwenden dieselbe bestätigte Session-ID. Ask-Modelltest ist frei von alter Skill-Injektion. Aktuelle General-/Codex-Stagingpakete bestehen Byte-/Profilprüfung; technische Regressionen bestehen. Grenzen und tatsächliche Ergebnisse sind dokumentiert.
Steps:
1. Ask-Helper und Referenzen beim kanonischen Member korrigieren, Fehler-/Erfolgsfälle prüfen.
2. Reales Claude-Review mit Rückfrage im Desktop-Testprojekt ausführen; gezielten nativen Ask-Modellfall ohne UI-Einstiegsprompt prüfen.
3. Gesichertes Release-Staging ohne Verzeichnislöschung aktualisieren und prüfen.
Evidence: docs/plan0021-evidence.md: realer Claude-Resume bestanden; isolierter Luna-High-Ask-Test und aktuelle Staging-Prüfung bestanden.

### W-002 Luna High prüft Skills und einen vollständigen Workflow

Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: Alle geänderten Skills und Helper sowie ein kompletter Testplan sind mit GPT-6 Luna High geprüft.
Acceptance: Tests liegen im Desktop-Projekt test. Helperprüfung umfasst korrekte und falsche Aufrufe sowie reale Consumer oder explizite Grenzen. Ein nativer Workflow arbeitet einen echten Plan vollständig ab; Modelle sind Luna High, Projekt-Schwellen 15/15. Tatsächlich erfolgte Manager-/Worker-Rollover, Titel, Pinning, Review und Abschluss werden anhand der Chats geprüft; Simulation wird separat ausgewiesen.
Steps:
1. Gebaute Testpakete, begrenztes Testprojekt und Plan vorbereiten; nur dort 15/15 setzen.
2. Unabhängige Luna-High-Prüfung der Skills/Helper und nativen Workflow ausführen, Befunde beheben und gezielt erneut prüfen.
3. Endzustand und Belege prüfen; finale Änderungen in Staging übernehmen.
Evidence: docs/plan0021-evidence.md und Desktop/test/plan0021/workflow-result.md: Testplan abgeschlossen, reale 15/15-Rollover, Luna-High-Helperprüfung und kontrollierte Nachprüfungen bestanden.

### W-003 Tatsächliche Übergaben und Kontextkosten sind geprüft

Status: done
Depends on: [W-002]
Blocked by: []
Decisions: []
Outcome: Der reale Workflow belegt korrekte Helper-Verwendung und knappe, vollständige Übergaben ohne unnötige Worker-/Reviewer-Ausgaben.
Acceptance: Tatsächliche Aufrufe und Erstellungsargumente werden mit Helper-Ausgaben verglichen. Handoffs erhalten erforderliche Fakten, fertige Arbeit und Adressen; Archivierungsreihenfolge entspricht den Regeln. Wiederholte Kontextblöcke, unnötige Lesezugriffe, Narration und große Toolausgaben werden konkret belegt. Rücklieferungen enthalten korrekte entscheidende Ergebnisse. Begründete Skill-/Helperfehler sind behoben und gezielt nachgeprüft; Beobachtungen ohne Fehlerbeleg werden nicht zu neuen Regeln.
Steps:
1. Native Logs des Testlaufs lesen, Ausgabegrößen und konkrete Übergaben auswerten.
2. Belegte Defekte beim kanonischen Owner korrigieren; betroffene Fälle und finale Pakete erneut prüfen.
Evidence: docs/plan0021-evidence.md: native Übergaben geprüft, belegte Fehler korrigiert, gezielte Luna-Proben bestanden; Erstlauf und kontrollierte Fortsetzung getrennt dokumentiert.

### W-004 Setup steuert das Anpinnen getrennt für Ask und Workflow

Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: ask.pin_threads und workflow.pin_threads sind über Setup schaltbare boolesche Parameter mit Default true.
Acceptance: Beide Bereiche sind unabhängig ein-/ausschaltbar. False unterbindet neue Pin-Aufrufe einschließlich Workflow-Manager/Rollover; bestehende Pins bleiben erhalten. Claude ist nicht betroffen. Falsche Typen ergeben konkrete Diagnose ohne Speicherung. Resolver, Setup, Anleitungen und Builds stimmen überein; technische und Luna-High-Prüfung bestanden.
Steps:
1. Kanonische Defaults, Validierung, Resolver-Ausgabe und Setup ergänzen, bedingte Pin-Regeln nachführen.
2. Fehlende Defaults, true/false und ungültige Typen an echten gebauten Consumern testen; Luna High prüft Gegenfälle.
Evidence: docs/plan0021-evidence.md: Setup-/Consumer-Tests und 14 Luna-High-Pin-Prüfungen bestanden.

### W-005 READMEs erklären Nutzen und Planung vor der Umsetzung

Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: Workflow und Plan erklären ihren Nutzen früh und nachvollziehbar.
Acceptance: Kanonische Einleitungen nennen sorgfältige Planung mit unabhängigen Reviews, langfristige wartbare Entwicklung und prüfbare Fortschritte. Workflow erklärt frühe Fehlererkennung und den kontrollierten Rollover gegenüber Komprimierung mitten in der Arbeit, mit Plan als Backbone. Kosten/Cache-Aspekte stehen bei What it costs ohne erfundenes Geschwindigkeitsversprechen. Generierte Vorschauen und beide Buildprofile entsprechen den Quellen.
Steps:
1. Nutzerargumente in den beiden kanonischen Beschreibungstexten ausarbeiten; Kosten zentral halten.
2. Vorschauen/Staging regenerieren und die betroffenen README-Projektionen prüfen.
Evidence: Kanonische Beschreibungen und generierte READMEs in beiden Profilen aktualisiert; 16 betroffene README-Tests und beide Paketprüfungen bestanden.
