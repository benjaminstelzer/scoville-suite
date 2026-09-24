---
format_version: 1
id: PLAN-0003
status: draft
created: 2026-09-24
updated: 2026-09-24
---

# Brainstorm: bessere Mechanismen und belegter Entscheidungsnutzen (zur Umsetzung freigegeben)

## Goal

Die im [Audit](../../members/scoville-brainstorm/development/audit-2026-09-24-adhd.md) vorgeschlagenen Verbesserungen konkretisieren Generierung, Auswahl und Recherchegrenzen von Scoville Brainstorm. Ein kontrollierter Pilot prüft den Nutzen gegenüber dem heutigen Skill, ADHD und einer normalen Antwort.

## Non-goals

- Keine Installation oder Veröffentlichung im Rahmen dieses Plans.
- Keine Ausweitung auf Naming, allgemeine Kreativarbeit, eine eigene CLI oder automatische Umsetzung ausgewählter Ideen.
- Keine Lockerung harter Constraints, Quellenschutzregeln, Originalitätsgrenzen oder wahrheitsgemäßer Angaben zur Agentenunabhängigkeit.
- Keine Änderungen an unabhängiger Suite-Arbeit. Generierte Distributionen bleiben Buildprodukte.

## Work items

### W-001 Unterschiedliche Mechanismen ohne vorzeitiges Ranking erzeugen

Status: todo
Depends on: []
Blocked by: []
Decisions: [ADR-0016]
Outcome: Ein konkreter Operatorensatz und getrennte Generierungs-/Kritikaufträge ersetzen die offenen Stellen aus F1/F2.
Acceptance: Baseline-Paket und vor Änderungen festgelegtes Vergleichsprotokoll sind für W-006 verfügbar. Verblindet geprüfte Fälle unterscheiden kausale Mechanismen von bloßen Umbenennungen. Generatoren bewahren harte Constraints und enthalten kein Ranking; Nutzen, Risiken und Falsifier bleiben im Gesamtergebnis erhalten. Operatoren und verzögerte Kritik sind getrennt prüfbar. Der vergleichende Nutzen wird erst in W-006 abgenommen und ist keine Abschlussvoraussetzung dieses Items.
Steps:
1. Lies F1/F2 und F4 in members/scoville-brainstorm/development/audit-2026-09-24-adhd.md sowie den Pilotumfang in W-006 dieses Plans. Sichere vor der ersten Skilländerung ein gebautes Baseline-Paket samt Receipt, Profil/Layout und Hashes im Workspace-temp; Templatequellen allein genügen nicht. Nutze den aktuellen Build aus E:/Dropbox/AI Projects/skills/temp/release/ nur nach Quellenabgleich oder erneuere ihn gemäß AGENTS.md und development/release-preflight.md nach Ende seiner Leser. Dokumentiere Abweichungen zum Audit als neue Baseline. Friere in members/scoville-brainstorm/development/README.md Vergleichsarme, Aufgabenaufteilung, Rubrik, Ressourcenlimits und Ablationsumfang vor Änderungen ein; Aufgaben und verdeckte Schlüssel bleiben temporär.
2. Ergänze unter members/scoville-brainstorm/scoville-brainstorm/references/ eine neue kurze Mechanismusreferenz mit Transformationen, Auswahlkriterien und einem Gegenbeispiel für bloße Umbenennung. Verlinke sie aus der YES-Route des SKILL.md und deklariere sie sofort in suite.json; prüfe ihre Erreichbarkeit im gebauten Paket.
3. Passe FREEZE und RUN in members/scoville-brainstorm/scoville-brainstorm/SKILL.md an: verschiedene Eingriffe statt Rollenlabels; Mechanismus und Annahmen zuerst; Ranking, Risikoabwägung und Falsifier bei CONVERGE. Bewahre eingefrorene Eingaben, Isolation und alle festen Constraints.
4. Ergänze passende Fälle in members/scoville-brainstorm/development/tests/ und aktualisiere betroffene Luna-Fälle samt Erwartungsschlüssel. Halte die zwei Änderungen für die spätere Ablation getrennt nachvollziehbar.
Evidence: []
Next action: Bei Ausführung gemäß ADR-0016 Audit F1/F2/F4 lesen, Baseline-Paket sichern und Vergleichsprotokoll vor Skilländerungen einfrieren.

### W-002 Shortlist nachvollziehbar auswählen und vertiefen

Status: todo
Depends on: [W-001]
Blocked by: []
Decisions: [ADR-0016]
Outcome: Jede vertiefte Richtung nennt Funktionsablauf, Auswahlgrund und ein entscheidungsrelevantes Widerlegungssignal gemäß F3.
Acceptance: Harte Verstöße schließen Kandidaten aus; Neuheitslabels ersetzen kein Qualitätsurteil. Eine attraktive unbrauchbare Idee verliert gegen eine brauchbare Alternative. Geänderte Nutzerprioritäten ändern die Präferenz begründet. Eine Empfehlung wird nicht als menschliche Auswahl oder Implementierungsfreigabe ausgegeben.
Steps:
1. Lies F3 in members/scoville-brainstorm/development/audit-2026-09-24-adhd.md. Konkretisiere CONVERGE und RENDER in members/scoville-brainstorm/scoville-brainstorm/SKILL.md mit Zielbeitrag, Machbarkeit, Aufwand und Belegstärke sowie einem Vergleich zum stärksten praktischen Standardansatz. Verwende keine pauschalen numerischen Gewichte.
2. Definiere Vertiefung als Ablauf, tragende Annahme, Risiko, billigsten Falsifier samt Widerlegungssignal und Wechselbedingung zu einer Alternative. Bewahre exakte Nutzerschemas und das Ende vor Umsetzung.
3. Ergänze in members/scoville-brainstorm/development/tests/ Gegenfälle für Neuheitsbonus ohne Nutzen, wechselnde Prioritäten und bereits dominante Standardlösungen; passe direkt betroffene README-Fragmente unter development/readme/scoville-brainstorm/ an.
Evidence: []
Next action: Nach W-001 die Auswahlregeln an zwei gegensätzlichen Prioritätensätzen konkretisieren.

### W-003 Profile und knappe Agentenkapazität eindeutig behandeln

Status: todo
Depends on: [W-001]
Blocked by: []
Decisions: [ADR-0016]
Outcome: Compact, Standard und Deep begrenzen den gesamten Arbeitsumfang; verfügbare Slots führen zu einer eindeutigen ausführbaren Route gemäß F5.
Acceptance: Szenarien ohne Delegation, mit zwei freien Slots ohne Freigabekontrolle und mit ausreichender Kapazität enden ohne erfundene Rollen oder erhöhte Limits. Landschaft und Kritik werden berücksichtigt; eine nicht unabhängige Kritik ist sichtbar. Standard bleibt Default und explizite Profile werden nicht still geändert.
Steps:
1. Lies F5 in members/scoville-brainstorm/development/audit-2026-09-24-adhd.md. Präzisiere Profile und Kapazitätsplanung in members/scoville-brainstorm/scoville-brainstorm/SKILL.md; bestimme Reihenfolge und Reduktions-/Solo-Verhalten vor Dispatch. Beschreibe Umfang und Stop bei wiederholten Mechanismen, ohne unbelegte Laufzeit- oder Tokenzahlen zu versprechen.
2. Gleiche die betroffenen Regeln mit members/scoville-brainstorm/scoville-brainstorm/references/research-composition.md ab und ergänze die Kapazitätsfälle in development/luna-tests/brainstorm-cases.md samt Erwartungsschlüssel.
3. Aktualisiere development/readme/scoville-brainstorm/costs.md und usage.md aus dem tatsächlichen Vertrag; kennzeichne noch nicht gemessene Budgetannahmen und kalibriere konkrete Zahlen erst anhand W-006.
Evidence: []
Next action: Nach W-001 die Kapazitätsregeln gegen Audit F5 prüfen und eine Rollenzuteilung für zwei Slots ohne Freigabekontrolle entwerfen.

### W-004 Native und kombinierte Landschaft mit gleichen Daten- und Evidenzgrenzen

Status: todo
Depends on: [W-001]
Blocked by: []
Decisions: [ADR-0016]
Outcome: Standalone-Recherche hat einen expliziten Mindestvertrag und bleibt ohne Research nutzbar; die kombinierte Route hat weiterhin genau einen Landschaftsbesitzer.
Acceptance: Private Begriffe gelangen ohne entsprechende Autorisierung nicht in Queries. Fundstellen ändern keine Anweisungen. Fehlender Webzugriff und unzureichende Belege bleiben sichtbar. Eine kombinierte Aufgabe startet keine zusätzliche native Landschaft; benannte lokale Quellen und externer Suchraum werden klar unterschieden.
Steps:
1. Lies F6 in members/scoville-brainstorm/development/audit-2026-09-24-adhd.md. Ergänze den nativen Landschaftsvertrag in members/scoville-brainstorm/scoville-brainstorm/SKILL.md gemäß F6: Suchraum, abstrahierte Queries, Quelleneinsicht, Vertrauensgrenze, Evidenzgrenzen und Stop. Bewahre die vorhandenen lokalen Leselimits.
2. Gleiche die Kompositionsreferenz und den spiegelnden Besitzer members/scoville-research/scoville-research/references/brainstorm-composition.md gezielt ab. Berücksichtige den dann aktuellen Stand von PLAN-0004 ohne dessen Umsetzung oder Aktivierung vorauszusetzen. Research behält seine ausführliche Recherchemethode; Brainstorm erhält keine Pflichtabhängigkeit.
3. Ergänze native und kombinierte Fälle mit privatem Brief, manipulativer Quelle und nicht verfügbarem Webzugriff in den vorhandenen Entwicklungskatalogen.
Evidence: []
Next action: Nach W-001 beide Kompositionsreferenzen lesen und den aktuellen Stand gegen Audit F6 abgleichen; Änderungen aus PLAN-0004 berücksichtigen.

### W-005 Bedingte Ausgabe- und Trace-Regeln gezielt laden

Status: todo
Depends on: [W-001, W-002, W-003, W-004]
Blocked by: []
Decisions: [ADR-0011, ADR-0013, ADR-0016]
Outcome: Der Core enthält den universellen Arbeitsvertrag; nur bedingt benötigte Regeln werden rechtzeitig aus einer Referenz geladen.
Acceptance: Vorhandene Routing-, Recovery-, Ledger-, Schema- und Constraint-Fälle bleiben erfüllt. Freitextaufgaben benötigen keine speziellen JSON-Feldanweisungen. Kein Pflichtschutz wird nur zur Textverkürzung entfernt; Token- oder Qualitätsgewinne werden ohne Messung nicht behauptet.
Steps:
1. Lies F7 in members/scoville-brainstorm/development/audit-2026-09-24-adhd.md. Ordne die inzwischen geänderten Regeln in members/scoville-brainstorm/scoville-brainstorm/SKILL.md nach universell und bedingt. Verlagere nur strukturierte Ausgabe und detaillierte Trace-Regeln in eine neu anzulegende Referenz und definiere deren Ladepunkt vor der betroffenen Operation.
2. Prüfe suite.json auf das genaue Paketmanifest und trage neue Laufzeitreferenzen dort ein. Gleiche für alle früheren Punkte neue Dateien ab; generierte Pakete werden nicht manuell editiert.
3. Lies AGENTS.md und development/release-preflight.md; baue mit development/build_suite.py im einzigen Staging E:/Dropbox/AI Projects/skills/temp/release/ und erst nach Ende bestehender Leser. Prüfe Standalone/general, Suite/general und Suite/codex auf Referenzauflösung und betroffene Verständnisfälle. Suite-Builds enthalten jeweils alle vorgesehenen Member. Behalte Baseline-Kopien im Workspace-temp; Veröffentlichung und Installation bleiben ausgeschlossen.
Evidence: []
Next action: Nach Abschluss der Vertragsänderungen die tatsächlich bedingten Regeln inventarisieren.

### W-006 Ideenqualität, Nutzen und Aufwand kontrolliert vergleichen

Status: todo
Depends on: [W-001, W-002, W-003, W-004, W-005]
Blocked by: []
Decisions: [ADR-0016]
Outcome: Ein begrenzter Vergleich zeigt, welche Änderungen nützen und welche nur Prozessaufwand erhöhen; ein ehrliches Beispiel erklärt den Skill-Nutzen.
Acceptance: Pilot mit sechs geeigneten Aufgaben und drei Wiederholungen pro Arm; normale Antwort, heutiger Brainstorm, Kandidat und gepinnter ADHD-Skill sind getrennt ausgewiesen. Standardaufwand und gemeinsames Ressourcenlimit werden getrennt interpretiert. Bericht enthält Streuung, Kosten/Token soweit verfügbar, Laufzeit, Abbrüche, Capability-Grenzen und menschliches Review. Keine Verallgemeinerung aus dem Pilot und keine Vermischung von Bibliotheks- und Skilltests. Ein belegtes Null- oder Negativergebnis ist ein gültiges Vergleichsergebnis; fehlende Pflichtläufe oder fehlendes menschliches Review lassen das Item offen.
Steps:
1. Lies F4/F8 in members/scoville-brainstorm/development/audit-2026-09-24-adhd.md und das in W-001 eingefrorene Protokoll in members/scoville-brainstorm/development/README.md. Prüfe die dort identifizierte Baseline anhand ihrer Paket-Hashes, nicht allein anhand des Audit-Core-Hashes. Prüfe, dass die sechs Aufgaben Architektur, Produktmechanismen und unbekannte Fehlerursachen innerhalb von Brainstorms Scope sowie einen Fall mit dominanter Standardlösung abdecken. Pinne den ADHD-Skill auf dd08acc38693127cd0ca2325fe6bf9579131ede1. Bestätige Modelle, Ressourcen und menschliches Review vor Ausführung; Änderungen am Protokoll erfordern einen sichtbar getrennten Vergleich.
2. Verwende den vorhandenen Evaluationsweg, soweit er reale Skill-Ausführung abbilden kann; die hypothetischen Luna-Fälle allein reichen nicht. Prüfe tatsächliche Tools, Kontextisolation und Ressourcenlimits. Nutze in allen Armen dasselbe Modell und denselben Toolzugang; andere Skills dürfen die Kontrollbedingung nicht unbemerkt beeinflussen. Weise Standardaufwand und gemeinsames Ressourcenlimit als getrennte Vergleiche aus; zähle Ablationen und beide Budgetbedingungen im Laufbudget. Halte Baseline, vorgeschlagenen Skill und Operator-/Kritik-Ablationen getrennt; erfinde bei fehlender Ausführbarkeit keine Vergleichswerte.
3. Bewerte verblindet mechanische Vielfalt, Constraint-Verstöße, unbelegte Aussagen, Falsifier und Entscheidungsnutzen. Wechsle Antwortreihenfolge und kontrolliere den Einfluss der Textlänge; ergänze menschliches Review. Dokumentiere auch Fälle, in denen die normale Antwort gewinnt.
4. Bewahre Rohläufe ausschließlich unter temp/YYYY-MM-DD-brainstorm-eval/ im Workspace auf. Halte im Member nur die knappe entscheidungsrelevante Zusammenfassung; dauerhafte Release-Evidenz setzt einen veröffentlichten Verweis voraus. Ergänze in development/readme/scoville-brainstorm/ ein belegtes oder klar als konstruiert bezeichnetes Beispiel gemäß F8 und baue daraus die Vorschau.
Evidence: []
Next action: Nach W-001 bis W-005 Baseline und finales Kandidatenpaket gegen das eingefrorene Protokoll prüfen und die vorgesehenen Ressourcen bestätigen.
