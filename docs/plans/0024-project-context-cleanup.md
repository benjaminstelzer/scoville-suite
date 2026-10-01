---
format_version: 1
id: PLAN-0024
status: completed
created: 2026-09-30
updated: 2026-09-30
---

# Scoville Project Context Cleanup erstellen und in die Suite integrieren

## Goal

`scoville-project-context-cleanup` steuert Nutzeraufträge zum Ergänzen oder
Überarbeiten von `AGENTS.md` und `PROJECT_INDEX.md`, einschließlich vorhandener
Schreibweisen der Dateinamen. Er entscheidet anhand des Auftrags und der
Projektregeln, welche Datei gemeint ist, prüft Informationsnutzen und
Formulierung und ordnet den Inhalt verständlich ein. Notwendiger Kontext,
Berechtigungen, Schutzregeln und Plansemantik bleiben erhalten. ADR-0119 hält
die vom Nutzer gewählte Aktivierung und Zuständigkeitsgrenze fest.

Kanonische Mitgliedsquellen liegen unter
`members/scoville-project-context-cleanup/`, der Skill darunter im gleichnamigen
Paketordner. `suite.json` besitzt Mitgliedschaft und Paketdateien,
`development/readme/` die README-Fragmente. Gemeinsame Schreibprinzipien gehören
zu `../shared/instruction-writing.md` und dessen Referenzen. Der neue Skill
ergänzt deren Anwendung auf Projektkontext, ohne einen zweiten Regelbestand
zu pflegen. Scoville Plan besitzt weiter Indexformat, Verweise und Lebenszyklus.

Der Nutzer hat nach Planerstellung und GPT-6.1-Review am 30.09.2026 die
Umsetzung des Plans beauftragt. Das Review und seine Grenzen stehen in
`docs/plan0024-review.md`, Umsetzungsnachweise in
`docs/plan0024-implementation-evidence.md`.

Recherche vom 30.09.2026: kurze relevante Regeln, bedarfsgesteuerte Verweise und
klare Zuständigkeiten statt pauschaler Prozessrezepte. Die Gliederung in W-001
ist eine abgeleitete Empfehlung, kein empirisch bewiesenes Optimum.
Unterschiedliche Studien belegen keine pauschale Tokenersparnis; Prüfungen
müssen Verhalten und Bedeutung erhalten, nicht nur die Dateilänge verringern.

- [OpenAI: moderne Skills und AGENTS.md](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra)
- [Anthropic: Context Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- [Claude Code: dauerhaft geladene Projektregeln](https://code.claude.com/docs/en/best-practices#write-an-effective-claudemd)
- [AGENTS.md: freies Markdownformat](https://agents.md/)
- [AGENTbench: Nutzen und Kosten von Kontextdateien](https://arxiv.org/abs/2602.11988)
- [Effizienzstudie mit anderen Ergebnissen](https://arxiv.org/abs/2601.20404)

## Non-goals

Keine Hooks, Watcher oder garantierte Überwachung aller Schreibzugriffe.
Keine allgemeine Prose-, README-, Skill- oder Plantextbereinigung.
Kein neues Planformat, keine Änderung von Planstatus oder Berechtigungen durch
Cleanup. Keine vollständige Repository-Lesepflicht, starre Wort-/Tokenlimits
oder erzwungene Gliederung. Keine eigenständige Veröffentlichung, Installation,
Commits oder Änderung bestehender Modell-/Workfloweinstellungen.

## Work items

### W-001 Der Skill pflegt Projektkontext knapp und bedeutungstreu

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0119]
Outcome: Das kanonische Skillpaket enthält einen klar begrenzten Schreibablauf für Projektregeln und Indextexte.
Acceptance: Skill Creator validiert das Paket. Die Beschreibung nennt die tatsächlichen Schreibaufträge und aktiviert keine beliebigen Dokumentarbeiten. Der Ablauf liest Zieltext und relevante übergeordnete Regeln, prüft Ergänzung und betroffene Gesamtstruktur, schreibt nur den beauftragten Zusammenhang und prüft gespeicherten Text. Er erhält Geltungsbereiche, Bedingungen, Ausnahmen, Berechtigungen, notwendige Begründungen und Schutzregeln. Er entfernt keine verbindliche Regel allein aufgrund allgemeinen Modellwissens. Geeigneter Text bleibt unverändert. Im Scoville-Index bleiben Frontmatter und Referenzen gültig, laufender Planstatus wird nicht im Text dupliziert. Fremde Indexformate werden erhalten. Bedeutungstreue und Verständlichkeit werden getrennt von Dateilänge bewertet.
Steps:
1. [status: done] SKILL.md und nötige Metadaten unter members/scoville-project-context-cleanup/scoville-project-context-cleanup/ mit Skill Creator und Skillwriter verfassen. Die unten verlinkte Recherche und die kanonischen Shared-Schreibregeln nutzen. Nur tatsächlich benötigte Referenzen ergänzen, keine pauschale Quellenladepflicht oder spekulativen Helper.
2. [status: done] Für AGENTS.md eine anpassbare Ordnung vermitteln: Zweck/Geltungsbereich, verbindliche Grenzen, kanonische Quellen/Zuständigkeiten, projektspezifische Arbeit, Prüfung/Abschluss, bedingte Verweise. Leere Abschnitte vermeiden. Voraussetzungen vor Aktionen, Ausnahmen bei der Regel, einzelne lokale Regeln bei ihrem Bereich erhalten. Ausführliche Verfahren nur bei Bedarf referenzieren; notwendige Schutzregeln nicht unzugänglich auslagern.
3. [status: done] Mit isolierten Beispielen echte Ergänzung, vorhandene Dublette, lange mehrdeutige Regel, relevante Ausnahme, widersprüchliche Ergänzung, bereits geeignete Datei und Indexpflege prüfen. Explizite neue Nutzerentscheidungen dürfen frühere Regeln im beauftragten Umfang ersetzen; ungelöste materielle Widersprüche benötigen eine gezielte Rückfrage. Fehlende Orientierung nicht durch erfundene Regeln oder Ordnerpfade ersetzen. Einen zweiten unveränderten Durchlauf als Stabilitätsfall prüfen und tatsächlich beobachtete Ergebnisse samt Modell/Host festhalten.
Evidence: docs/plan0024-implementation-evidence.md: Skill Creator, acht Luna-Dateifälle und drei bytegleiche Wiederholungen bestanden.

### W-002 Die gebaute Suite liefert den Skill und routet passende Schreibaufträge

Status: done
Depends on: [W-001]
Blocked by: []
Decisions: [ADR-0119]
Outcome: General- und Codex-Suite enthalten das vollständig gebaute Skillpaket und wählen Cleanup für passende Projektkontextaufträge unter Erhalt der übrigen Zuständigkeiten.
Acceptance: Aufträge „Füge das den Projektregeln hinzu“, „Ergänze AGENTS.md“ und „Aktualisiere PROJECT_INDEX.md“ erreichen Cleanup ohne ausdrücklichen Skillnamen in beobachteten Fällen mit der gebauten Suite. Hinweise werden nur beim zuständigen Schreiber ergänzt. Plan besitzt Indexstruktur und Statusübergänge, Cleanup Formulierung und Informationsqualität. Normale Planfortschritte lösen keine umfassende Neuordnung aus. Reine Codeänderung, gewöhnliche README-Arbeit und bloße Dateierwähnung aktivieren keine Bereinigung. Eine benannte Datei bleibt das Ziel; mehrdeutige „Projektregeln“ werden anhand vorhandener Regeln aufgelöst oder gezielt geklärt. Keine zweite Schreibinstanz, rekursiven Skillaufrufe oder zusätzliche Freigaberunde für autorisierte Ergänzungen. suite.json erfasst kanonische Quellen, genaue Paketdateien, General-/Codex-Mitgliedschaft, Family-Metadaten und README-Fragmente. Bestehende Layouts und isolierte Exporte bleiben baubar, generierte Dateien haben keine eigene Pflegequelle und exportierte Pakete benötigen keinen privaten Checkout. Bestehende Sichtbarkeit und Workflow-Grenzen bleiben erhalten. Gezielte technische Checks decken Mitgliedschaft, Links, Runtime-Dateien und Profiltrennung ab. README nennt Nutzen, Auslöser und Kosten ohne unbelegte Einsparungen. Technische Konformität und beobachtetes Modellverhalten werden getrennt berichtet. Build-Erfolg erteilt keine Veröffentlichungs- oder Installationsfreigabe.
Steps:
1. [status: done] In members/scoville-code/scoville-code/ und members/scoville-plan/scoville-plan/ die zuständigen Schreib-/Routingstellen prüfen und knapp anbinden. Nur unmittelbar betroffene weitere Verbraucher einbeziehen. Aktivierungsbeschreibung und Aufrufregel erhalten einen eindeutigen Owner.
2. [status: done] suite.json und development/readme/scoville-project-context-cleanup/ ergänzen, gemeinsame Templates nutzen und README-Vorschauen regenerieren. Ohne neues Standalone-Repository in die vorhandenen Layouts einpassen. Shared-Buildcode nur bei einer belegten Vertragslücke kanonisch ändern und Kopien bauen. Falls Runtime-Helper nötig werden, helper_contracts-/Fallback-Regeln vollständig anwenden. Ein erstes verwendbares Suite-Paket bauen, bevor Verhaltensfälle beginnen.
3. [status: done] Mit den gebauten Suite-Anweisungen positive Aufträge ohne Skillnamen und die Negativfälle prüfen. Beobachtete Auswahl und Schreibhandlung samt Modell/Host dokumentieren; keine garantierte Host-Aktivierung aus einer Beschreibung ableiten. Korrekturen beim kanonischen Owner vornehmen, neu bauen und betroffene Fälle erneut prüfen.
4. [status: done] Relevante Tests unter development/tests/ beziehungsweise ../shared/tests/ ergänzen und ausführen. Beide General-Layouts und Codex-Suite samt isolierten Exporten prüfen. Buildausgaben ausschließlich unter skills/temp/release/ führen. Vor Refresh bestehende Leser und Inventar prüfen. Veröffentlichung, Synchronisierung öffentlicher Ziele und Installation bleiben außerhalb dieses Plans. Keine feste historische CLI-Testreihe wieder einführen, siehe ADR-0118.
Evidence: docs/plan0024-implementation-evidence.md: 13 Buildtests, vier Profil-/Exporttests, drei Builds und sieben implizite Auswahlfälle bestanden.
