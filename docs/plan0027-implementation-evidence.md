# PLAN-0027: Umsetzung und Nachweise

## Ergebnis

Formatversion 1 bleibt bestehen. Stepstatus ist optional; fehlend bleibt unbekannt.
Neue Work Items schreiben mindestens einen markierten Step und Instructions,
ohne Next action. Altformen bleiben lesbar. Instructions ist einzeiliger Freitext
oder []; fehlend bleibt von ausdrücklich leer unterscheidbar.

Der Positionsmodus in select_context.py liefert aktuelles Work Item, aktive
Stepgruppen, sicher ausgewählten todo-Step, unbekannte Steps, Acceptance/Evidence,
Instructions, pausierte Rückkehrkontexte und verknüpfte offene ADRs. Freitext wird
nicht automatisch in Rückkehr oder Abnahme übersetzt. Der bestehende Validator
prüft das erweiterte Format. General hat zwei separate bedingte Fallbacks,
Codex keine. Keine zusätzliche Fortschrittsdatei und kein neuer Helper nötig.

Viewer und Workflow verwenden die tatsächliche Selector-Ausgabe. Review und
Korrektur dürfen ausdrücklich zugewiesene done-Steps prüfen; normale Fortsetzung
erhält abgeschlossene Effekte. Die separate Reparaturreferenz lädt nur bei einer
beauftragten Prüfung, Reparatur oder Migration, nicht bei normaler Wiederaufnahme.

## Reviews und praktische Skilltests

Astra Medium prüfte Plan, Next-step-Auswahl und Instructions-Alternative. Die
Einzelfeldvariante wurde empfohlen; Legacy-Kontext, offene ADRs und alle pausierten
Rückkehrhinweise wurden berücksichtigt. Review-Agent: /root/stepstatus_astra_plan.
Referenz: stepstatus-plan-20261001. Angefordertes Modell/Effort bestätigt;
zusätzliche Hosttelemetrie für die tatsächliche Ausführung ist nicht verfügbar.

Luna Medium nutzte gebaute General-/Codex-Payloads und reale Helper in isolierten
Rohprojekten. Agenten: /root/plan_luna_medium und /root/luna_cold_resume.

- Positionshelper: ungültige Kombination --position/--work-item lieferte eine
  konkrete USAGE_ERROR-Diagnose; korrigierter Aufruf lieferte W-002/Step 1.
- Reine Prüfung blieb lesend und meldete fehlende Parser-Evidenz ohne Laufzeitbehauptung.
- Kalte Fortsetzung lud nur SKILL.md und edit.md. Ein unmarkierter fertiger Step
  wurde am vorhandenen Text nachgewiesen; ein vorhandenes Übergabeprotokoll wurde
  berücksichtigt, ohne einen simulierten externen Effekt erneut auszuführen.
  W-001 abgeschlossen, W-002 ausgewählt und nicht begonnen.
- Neue Ein-Step-Aufgabe: Instructions: [], kein Next action; Step und Work Item
  durchliefen todo → in_progress → done. Einladung und Bericht bestanden den Brief;
  der Plan endete completed mit idle Index. Ein zu enger Inhaltscheck und eine
  unterbrochene Indexänderung wurden diagnostiziert und korrigiert, nicht als Erfolg gewertet.
- Migration: historischer Textabschluss erhalten, W-003 am Brief/Ergebnis geprüft,
  verbindliche Rückkehr zu W-002 vollzogen. Parserchecks widerlegten den alten
  Erfolgsbericht: ValueError bei leerer/nichtnumerischer Eingabe, Unicode-Ziffern
  angenommen. Reviewpflicht blieb in Instructions. Produkte und Berichte unverändert.
  Ein Feldreihenfolgefehler wurde nach Validator-Diagnose korrigiert; final valide.

Normale Fortsetzung lud im ersten Kandidaten unnötig repair.md. Das Routing wurde
präzisiert; der kalte Nachtest bestätigte die Korrektur. Die Schreibregel benennt
bestehende ausdrückliche Richtung für einen unveränderten vorbereiteten Übergang;
unklare oder concurrent Änderungen stoppen weiterhin die betroffene Arbeit.

## Technische und visuelle Prüfung

- 91 Plan-Tests: Alt-/Mischformat, LF/CRLF, Annotationen, Diagnosen und korrigierte
  Aufrufe, Instructions, pausierter Kontext, offene ADRs, tatsächliche CLI-Ausgaben.
- 49 aktuelle Workflowtests, einschließlich realem paketiertem Selector →
  Dispatch-Builder für Ausführung, Review, Korrektur und Fortsetzung.
- 16 Rust-Reader-Tests; Svelte-Prüfung ohne Fehler/Warnungen; Produktionsbuild bestanden.
- 13 Suite-Buildtests und 3 Helper-Aufrufvertragstests bestanden. Kanonische
  Quellenhashes, generierte READMEs und vollständiges Planprofil ohne Befund.
  Final gerenderte Plan-Payloads: General standalone/suite je 17 Dateien,
  Codex suite 15. Der zusätzliche lokale skill-creator-Schnellprüfer lehnt das
  bereits bestehende compatibility-Frontmatter ab; er bestätigt diese Pakete
  daher nicht. Der bestehende Suite-Paketvertrag wurde unverändert beibehalten.
- Positionshelper und tatsächliches Viewer-Modul liefern bei Gruppen, unbekannten
  Lücken und ausstehender Work-Item-Abnahme dieselbe Stepauswahl.
- Browser bei 1440 und 390 Pixeln: alle Texte einer Liste gleich eingerückt,
  Schriftstärke 400, einheitliche Textfarbe außer cancelled. Iconzentrum liegt in
  der ersten 18-Pixel-Zeile, auch bei Umbruch. Kein horizontaler Seitenüberlauf.
  Altformat ohne grünes Feld, aktive Gruppen, todo-Kreis, Pause/Blocker,
  Instructions und offene ADRs sichtbar. Disclosure per Enter bedienbar;
  Fokus bleibt erhalten. Keine Konsolenfehler oder Warnungen, Fonts geladen.

Originale Reviews, Model-Testprojekte, Screenshots und Messungen liegen unter
../../../temp/2026-10-01-stepstatus/. Screenshots: output/playwright/steps-wide.png
und steps-narrow.png; Messungen: proof-wide.txt und proof-narrow.txt.

## Übernahme und Grenzen

Ausführung erfolgte in isolierter Suitekopie mit aktivem PLAN-0027. Die 28
betroffenen Quellen wurden gegen den gesicherten Ausgangsstand und aktuelle
kanonische Dateien abgeglichen. Der neue native Workflow-Übergabeaufruf blieb
erhalten. Hashvergleich vor Übernahme bestätigte Schreibruhe; fremder PLAN-0026
und dessen Index wurden nicht umgeschaltet oder geändert. Sein Lauf bleibt eigenständig.

Nach isoliertem Abschluss wird dessen tatsächlicher PLAN-0027-Verlauf als
abgeschlossener Datensatz übernommen; der kanonische aktive Plan bleibt beim
anderen Chat. README-Projektionen entstehen aus den kanonischen Fragmenten.
Keine Installation, Veröffentlichung, Releaseversion oder Commit beauftragt.
Native Desktop-Bedienung wurde nicht behauptet: Reader läuft als Rust-Test,
die Anzeige als Produktionsbuild im realen Browser.
