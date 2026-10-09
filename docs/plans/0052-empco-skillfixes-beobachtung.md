---
format_version: 1
id: PLAN-0052
status: active
created: 2026-10-09
updated: 2026-10-09
current_item: W-003
---

# Skillfixes im wiederaufgenommenen EMPCO-Lauf beobachten

## Goal

Alle drei Minuten am bestehenden EMPCO-Lauf prüfen, ob die unter PLAN-0051 lokal ausgelieferten Skillfixes korrekt angewendet werden. Bestätigte Anwendungsfehler durch kompaktere Aufrufhilfen korrigieren und den überprüften Build lokal ausliefern. Tatsächliche Aktionen und geladene Regeln sind die Grundlage; ein laufender Agent allein beweist keine Wirksamkeit.

## Non-goals

Keine EMPCO-Änderungen, Tests oder Stopps. Nur die ausdrücklich beauftragte Nachricht zur Skill-Neuladung. Keine Zugriffe auf XMAPI, XMTEST, Holzbau oder Zugangsdaten. Keine allgemeinen Fortschrittsmeldungen oder reine Produkt-/Fixturefehler als Suite-Befunde. Der ergänzte Nutzerauftrag umfasst Push und Releases der geänderten Distributionen.

## Work items

### W-001 Wirksamkeit der Skillfixes beobachten

Status: paused
Depends on: []
Blocked by: []
Decisions: []
Outcome: Neue bestätigte Suite- oder Anwendungsfehler sind mit Ursache, kleinstem Fix und Evidenzgrenze erfasst; die tatsächlich beobachtete Fixwirkung ist nachvollziehbar.
Acceptance: Tatsächliche Aktionen seit der Wiederaufnahme geprüft, danach nur neue relevante Ereignisse; Rollen, Übergaben, Reviews, Ergebnisprüfungen und Planfortschritt gegen geladene Regeln beurteilt; neue Befunde gebündelt durch Scoville Ask mit Sol 6.1/high geprüft und knapp dokumentiert; Sichtbarkeitsgrenzen offen; Abschluss nur für diesen Lauf mit Schlussbewertung und gelöschter Automation.
Instructions: Nach W-003 bei Step 1 fortsetzen. Nur neue bestätigte Ablauffehler melden; bekannte Befunde nur bei relevanter neuer Entwicklung erneut prüfen.
Steps:
1. [status: in_progress] Thread 01a116ce-ac9b-77f0-a6cc-db641fb26f4b auf Host local ab Wiederaufnahmeturn 01a1205e-4bdb-74a1-b1a1-905470d5e3a6 samt tatsächlichen Manager-, Worker- und Reviewer-Aktionen prüfen. Aktuellen geprüften Umfang unter temp/2026-10-09-empco-skillfixes-beobachtung/state.json überschreiben; ungelesene Ereignisse nicht als geprüft markieren.
2. [status: in_progress] Bei neuen relevanten Fehlern Ursachen und kleinste allgemeine Fixes über Ask prüfen. Bestätigte Befunde mit Quelle, Wirkung, zuständigem Skill und offener Grenze knapp in docs/testing/0052-empco-skillfixes-befunde.md sammeln; ohne neue Befunde keine Konsultation oder Planänderung.
3. [status: todo] Bei Ende oder Nutzerstopp dieses konkreten Workflows den tatsächlich beobachteten Umfang abschließend bewerten, Beobachtung schließen und Automation löschen. Keinen anderen Lauf automatisch verfolgen.
Evidence: Neustartaudit und Sol/high-Prüfung durchgeführt; Readerverwechslung erneut belegt. Fixvorschläge und Grenzen: [Befunde](../testing/0052-empco-skillfixes-befunde.md).

### W-002 Aufrufhilfen korrigieren und lokal ausliefern

Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: Die bestätigten Anwendungsfehler haben präzisere Aufrufhilfen im überprüften lokalen Build; EMPCO ist zur Neuladung informiert.
Acceptance: Readerfortsetzung, CLI-Rollengrenzen, Suchbeispiel und Referenzhinweise erhalten die bestehenden Schutzregeln; Änderungen unabhängig mit Sol 6.1/high geprüft; betroffene technische Checks unter Windows und Linux sowie gezielte Luna-Medium-Verständnisproben bewertet; Build aus überprüften Quellen verifiziert, vorhandene lokale Skills bytegleich aktualisiert und Reloadnachricht zugestellt; verbleibende Grenzen benannt.
Instructions: []
Steps:
1. [status: done] Bestätigte Vorschläge aus docs/testing/0052-empco-skillfixes-befunde.md in kanonischem Shared Writing, nativen Readerhilfen und Workflow-Aufrufen umsetzen; generierte Quellen synchronisieren.
2. [status: done] Fokussierte Checks und Verständnisproben ausführen, Änderungen durch Scoville Ask prüfen und belegte Findings korrigieren.
3. [status: done] Überprüfte Quellen committen und den einzigen Build unter skills/temp/release aktualisieren; lokale Codex- und Claude-Skills verifizieren, dann EMPCO zur Neuladung informieren.
Evidence: Review und gezielte Windows/Linux-Checks bestanden; 13 Skills lokal aktualisiert, Reloadnachricht zugestellt. Grenzen: [Nachweis](../testing/0052-aufrufhilfen-auslieferung.md).

### W-003 Überprüften Build auf GitHub veröffentlichen

Status: in_progress
Depends on: [W-002]
Blocked by: []
Decisions: []
Outcome: Geänderte Distributionen sind mit passenden Versionen gepusht und als verifizierte GitHub-Releases verfügbar.
Acceptance: Alle manifestbestimmten Veröffentlichungsziele verglichen, nur geänderte Ziele veröffentlicht; Sichtbarkeit und Historie erhalten; Remote-Dateien, Tags, Releases und nötige Assets stimmen mit dem überprüften Build überein; genau ein aktuelles Release je veröffentlichtem Ziel verbleibt.
Instructions: []
Steps:
1. [status: in_progress] Bestehenden Build und aktuelle Remote-Ziele prüfen, kanonische Changelogs versionieren und Pakete unter skills/temp/release aktualisieren. Unveränderte technische Nachweise wiederverwenden.
2. [status: todo] Geänderte Distributionen pushen, Releases und Assets veröffentlichen, Remote-Bytes und Viewer-Nachweise prüfen, ersetzte Releases erst danach entfernen.
Evidence: Nutzer hat Push und GitHub-Releases ausdrücklich ergänzt; funktionale Abnahme aus W-002 bleibt gültig.
