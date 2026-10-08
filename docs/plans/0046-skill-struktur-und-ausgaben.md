---
format_version: 1
id: PLAN-0046
status: completed
created: 2026-10-08
updated: 2026-10-08
---

# Skilltexte und erzeugte Anweisungen gliedern

## Goal

Die 28 von Sol gefundenen Änderungsgruppen an ihren kanonischen Quellen kompakter und eindeutiger gliedern. Sequenzen, Zustände und Zuständigkeiten sichtbar machen, ohne Verhalten oder Befugnisse zu ändern.

## Non-goals

Keine neuen Funktionen, Prüfpflichten oder Ausgabeformate. Kein EMPCO-Eingriff, Workflowstart, Commit, Installation oder Release.

## Work items

### W-001 Strukturänderungen umsetzen und gegenprüfen

Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: Die freigegebenen Skilltexte, Referenzen, Shared-Texte, README-Fragmente und erzeugten Helperanweisungen sind klarer gegliedert, vom selben Sol-Reviewer geprüft und mit Luna/Medium praktisch auf Verständnis geprüft.
Acceptance: Bestehende Anforderungen, Bedingungen, Rollen, Freigaben und Fehlerstopps bleiben erhalten; stabile Schnittstellen und vollständige Übertragung bleiben unverändert. Generierte Verbraucher entsprechen den Quellen. Drei unterschiedliche Luna/Medium-Verständnisfälle je Skill sind ausgewertet; bestätigte Fehler sind behoben und gezielt nachgeprüft, verbleibende Grenzen benannt.
Instructions: []
Steps:
1. [status: done] Die 28 Änderungsgruppen aus SCOVILLE-LISTEN-INVENTUR-2026-10-08 an den kanonischen Suite- und Shared-Quellen überarbeiten; Ausgangsstände Suite 9116c2e und Shared 2cdd6d90 für den Vergleich verwenden.
2. [status: done] Betroffene generierte Kopien aktualisieren und relevante Generatorausgaben, Paketstruktur und Übertragung unter Windows und Linux prüfen.
3. [status: done] Dieselbe Sol-Session ask_sol_listen_inventur gegen den vollständigen Diff prüfen lassen; bestätigte Fehler beheben und betroffene Checks wiederholen, dann abschließen.
4. [status: done] Danach die acht Skills jeweils in drei verschiedenen hypothetischen Anwendungsfällen mit Luna/Medium prüfen; Windows und Linux verwenden, konkrete Fehlverständnisse korrigieren und nachtesten.
Evidence: Sol/high PASS; Win/Linux: Paket- und Consumerchecks PASS, je 24 Luna/Medium-Fälle fachlich geprüft. Handoff-Fix nachgetestet; drei Sprachabweichungen bleiben als Modellgrenze.
