# Brainstorm im Vergleich zu ADHD

Stand: 2026-09-24. Auftrag: Audit und konkreter Planentwurf; keine Umsetzung.

## Urteil

Brainstorm hat den präziseren Vertrag für Randbedingungen, begrenzte Originalitätsaussagen und ehrliche Solo-Arbeit. ADHD beschreibt konkreter, wie ungewöhnliche Ideen entstehen und wie gute Kandidaten vertieft werden. Der größte Verbesserungshebel ist deshalb eine bessere Generierungs- und Auswahlmethode, ergänzt um Qualitätsnachweise. Mehr Agenten oder zusätzliche Ablaufregeln allein lösen das nicht.

Dies ist ein Quellen- und Vertragsaudit. Aussagen über mögliche Auswirkungen sind begründete Hypothesen, keine gemessenen Modellfehler. Ob Brainstorm bessere oder schlechtere Ideen als ADHD erzeugt, weiß ich ohne kontrollierten Direktvergleich nicht.

## Umfang und Standbindung

- Kanonischer Member: `members/scoville-brainstorm/` im privaten Suite-Repository. Der zuerst genannte öffentliche Ordner ist ein Distributionsziel. Die Zuordnung wurde vom Nutzer bestätigt.
- Suite-HEAD: `c89641a6d73b0ecdfb32f057663261a4aa1dd972`. Geprüft wurde der bereits veränderte Arbeitsbaum, nicht ausschließlich dieser Commit. Laufende Suite-Arbeit bleibt unberührt.
- SHA-256 des kanonischen `scoville-brainstorm/SKILL.md`: `6fc08b92b8a9a23aefe1d1a8ccf7e26248e679d32c4da989e8e0999b3438f08e`.
- SHA-256 des untersuchten Distributions-Skills: `6cd779099c71d9f8ffe07e0efca50e2360302aae327d0b4e7c68d6b1c3e5eac5`. Die Quelle enthält Paketbedingungen und Familienprojektionen; die abweichenden Hashes sind kein Nachweis fehlerhafter Auslieferung.
- ADHD: `UditAkhourii/adhd`, untersuchter Main-Commit `dd08acc38693127cd0ca2325fe6bf9579131ede1`. Brainstorms Third-party Notice nennt den älteren Inspirationsstand `3d9dc487bc2eba4449742e2db0d92be9ebdf95b6`; ein Herkunfts-Pin muss nicht automatisch aktualisiert werden.
- Gelesen: beide Skill-Cores, Brainstorms Kompositionsreferenz, Entwicklungsnotizen und aktuelle Fallkataloge; ADHDs Skill, Frames, Evaluationsmethodik, Benchmark-Runner, Baseline, Judge, relevante Ergebnisabschnitte und Issues. Keine Pakete installiert, Modellvergleiche ausgeführt oder Skill-Agenten gestartet.

## Wie belastbar ist der ADHD-Vorsprung?

Die GitHub-API zeigte beim Abruf 4.274 Sterne und 290 Forks [S1]. Eine reale Integration ist durch den gemergten Repowire-PR #313 belegt [S8]. Das stützt Aufmerksamkeit und mindestens eine Integration. Aktive Nutzerzahlen und eine allgemeine Qualitätsüberlegenheit sind damit nicht belegt.

ADHD meldet 5 Siege bei 6 Aufgaben gegen eine einzelne Modellantwort. Die eigene Methodik nennt denselben Modellfamilienhintergrund des Judges und ausschließlich technische Aufgaben als Grenzen [S3]. Der Runner ruft `run()` aus der Bibliothek mit fünf Frames auf; er testet nicht die Befolgung von `skills/adhd/SKILL.md`. Er gleicht auch den Aufwand der Baseline nicht an und führt pro Aufgabe im sichtbaren Loop einen Vergleich aus [S4]. Seine Zahlen dürfen weder als Skill-Benchmark noch als fairer Vergleich mit Brainstorm übernommen werden.

Beim in der README hervorgehobenen Timeout-Beispiel gewinnt im Ergebnisbericht sogar die Baseline: `builder_usefulness` 9 statt 4, trotz höherer ADHD-Werte für Breite und Neuheit [S5]. Mehr ungewöhnliche Ideen sind offenbar auch im eigenen Bericht nicht automatisch die nützlichere Entscheidungshilfe. Die Issues #17 und #18 dokumentieren zudem Einwände zur Abgrenzung von Frames und zur Übertragung von Forschung mit wesentlich mehr Samples; ihr Status `closed` beweist allein keine erfolgreiche Replikation [S7].

## Befunde und konkrete Korrekturen

Priorität P1: direkt entscheidungsrelevante Lücke. P2: sinnvolle Verbesserung, deren Aufwand gegen den Nutzen geprüft werden sollte. Die Prioritäten bewerten den Vertrag, nicht gemessene Fehlerhäufigkeit.

### F1 · P1 · Mechanismus-Operatoren bleiben zu abstrakt

**Beobachtung:** `SKILL.md:110–127` verlangt unterschiedliche Mechanismen und je einen Operator, liefert aber keinen konkreten Operatorensatz und kein Auswahlkriterium für dessen Verschiedenheit. ADHD gibt 15 Frames mit ausführbaren Blickrichtungen und Auswahlhinweisen vor [S2, S6].

**Mögliche Folge:** Mehrere korrekt isolierte Generatoren liefern dieselbe Architektur mit anderen Bezeichnungen. Isolation allein stellt mechanische Vielfalt nicht sicher.

**Fix:** Eine kurze, nur bei YES geladene Referenz mit sechs bis acht Transformationen: Komponente entfernen, Kontrolle verlagern, Ausführung zeitlich verschieben, Informationsbedarf reduzieren, zentral/dezentral umkehren, Gegenproblem invertieren und einen fremden Mechanismus übertragen. Je Operator: genaue Transformation, geeignete Fragestellung und Gegenbeispiel bloßer Umbenennung. Auswahl nach unterschiedlichen Eingriffen, nicht Rollenbezeichnungen. Analogie muss in einen konkreten Ablauf übersetzt werden. Harte Constraints bleiben unverändert.

**Nachweis:** Identische Aufgaben vor/nach Änderung; verblindet nach unterschiedlichen kausalen Abläufen clustern. Mehr Labels zählen nicht als Gewinn. Siehe W-001 und W-006.

### F2 · P1 · Kritik beginnt möglicherweise schon beim Generieren

**Beobachtung:** `SKILL.md:124–127` verlangt vom Generator bereits Nutzen, tragendes Risiko und billigsten Falsifier. Ein ausdrückliches Verbot von Ranking oder vorzeitiger Aussortierung fehlt. ADHD trennt kurze, unbewertete Kandidaten von späterer Kritik [S2].

**Mögliche Folge:** Ein Generator verwirft ungewöhnliche Ansätze vorschnell, obwohl die spätere Konvergenz sie sinnvoll konkretisieren könnte. Das ist eine Hypothese; die bisherigen Fälle messen sie nicht.

**Fix:** Generator liefert zunächst Mechanismus und notwendige Annahmen, ohne Ranking. Harte Constraints gelten weiter; erkennbare Verstöße werden nicht als zulässige Kandidaten ausgegeben. Risiko, Evidenz und Falsifier folgen im Kritikschritt. Keine starre Mindestzahl erzwingen und offensichtliche Standardlösungen nicht wie bei ADHD pauschal verbieten.

**Nachweis:** Ablation mit unveränderten Operatoren: heutiger Generatorvertrag gegen verzögerte Bewertung. Prüfen, ob zusätzliche brauchbare Mechanismen entstehen, ohne mehr Constraint-Verstöße. W-001/W-006.

### F3 · P1 · Auswahl und Vertiefung sind schwächer spezifiziert als der Ablauf

**Beobachtung:** `SKILL.md:147–155` benennt Normalisierung, Duplikate und eine begrenzte Shortlist; „deepen“ hat keine inhaltliche Definition. Es fehlt eine explizite Regel, warum eine zulässige Richtung vor einer anderen bleibt. ADHD definiert Kriterien, Vertiefungsskizze und Folgerichtungen [S2].

**Mögliche Folge:** Der Output hält das Format ein, hilft aber wenig bei der Entscheidung. Originalitätslabels werden möglicherweise als Qualitätsranking missverstanden.

**Fix:** Nach Constraint-Prüfung nach Zielbeitrag, Machbarkeit, Kosten und Belegstärke vergleichen. Unsicherheit getrennt von Qualität halten. Je Finalist: konkreter Ablauf, wichtigste Annahme, tragendes Risiko, beobachtbarer Falsifier einschließlich Widerlegungssignal und Bedingung, unter der eine andere Richtung vorzuziehen ist. Optional eine begründete Favoritenempfehlung formulieren, ausdrücklich ohne menschliche Auswahl oder Umsetzung zu ersetzen. Den stärksten praktischen Standardansatz mitführen; keine willkürlichen Dezimalgewichte übernehmen.

**Nachweis:** Ein absichtlich attraktiver, aber unbrauchbarer Kandidat wird verworfen; unterschiedliche Prioritäten ändern die Rangfolge nachvollziehbar. W-002.

### F4 · P1 · Qualitätsnachweis fehlt im untersuchten Testumfang

**Beobachtung:** `development/luna-tests/brainstorm-cases.md:3–6` erklärt die 25 Fälle ausdrücklich zu hypothetischen Szenarien ohne Spawns, Suche, Mutation oder Experimente. Der Member-Katalog `development/tests/recovery-cases.json` beschreibt Recovery und Routing, keine gemessene Ideenqualität. `acceptance-astra.md` begrenzt ältere Proben ausdrücklich auf zwei supplied-text-Fälle mit deaktivierten Tools.

**Folge:** Diese Belege können Regeln und Verständnis prüfen, aber keine Überlegenheit bei Ideenvielfalt, Nutzbarkeit oder tatsächlicher Isolation. Es wird nicht behauptet, dass im gesamten Projekt nie andere Tests stattfanden.

**Fix:** Kleinen Direktvergleich ergänzen: normale Antwort, heutiger Brainstorm, vorgeschlagener Brainstorm und gepinnter ADHD-Skill. Zwei getrennte Fragen prüfen: Nutzen bei jeweiligem Standardaufwand und Nutzen unter gemeinsamem Ressourcenlimit. Bibliotheksresultate nur als gesonderten Arm führen. Kosten, Toolverfügbarkeit, Abbrüche und Solo-Modus sichtbar halten.

**Nachweis:** Sechs passende Aufgaben mit drei Wiederholungen als erster Pilot; Mechanismusvielfalt, harte Verstöße, unbelegte Behauptungen, Qualität der Falsifier und Entscheidungsnutzen bewerten. Blindfolge wechseln, Länge nicht belohnen und mindestens einen menschlichen Review vorsehen. Ergebnisse samt Streuung und Aufwand berichten; kein allgemeines Siegesversprechen aus einem Pilot. W-006.

### F5 · P2 · Profile begrenzen Agenten, definieren aber kaum Arbeitsbudget

**Beobachtung:** `SKILL.md:17–23` fixiert Standard als Default; Compact/Standard haben nur Obergrenzen. Anzahl oder Tiefe der Kandidaten, Rechercheaufwand und Vertiefungsumfang bleiben weitgehend offen. `:32–43` behandelt fehlende Slot-Freigabe ausführlich, ohne eindeutige Priorisierung aller Rollen bei knapper Kapazität. ADHD benennt Ideenbudget und Stop bei wiederholten Formen, auch wenn seine konkreten Kostenangaben hier nicht verifiziert wurden [S2].

**Mögliche Folge:** „Compact“ spart eventuell Agenten, liefert aber ähnlich viel Aufwand oder Text. Ein Host mit wenigen dauerhaft belegten Slots kann den Kritiker verlieren.

**Fix:** Für jedes Profil Umfang und Stoppregel der gesamten Aufgabe erklären; vorhandenen Default zunächst bewahren. Vor Dispatch Platz für benötigte Landschaft und Kritik berücksichtigen. Bei zu wenig Kapazität eine eindeutige, ehrlich bezeichnete reduzierte oder Solo-Route wählen. Kein stiller Profilwechsel, keine erfundenen Slots, keine pauschale Erhöhung von Limits. Neue Zahlen erst nach Pilot kalibrieren.

**Nachweis:** Fälle mit null, zwei und ausreichend Slots; Compact bleibt erkennbar kleiner und endet bei mechanischer Wiederholung. W-003.

### F6 · P1 · Native Landschaft hat nicht denselben expliziten Recherchevertrag

**Beobachtung:** Die nur explizit kombiniert geladene `references/research-composition.md:11` enthält klare Regeln zu privaten Suchbegriffen, nicht vertrauenswürdigen Quellen, Quelleneinsicht und wiederholten Ursprüngen. Der native Landschaftsauftrag in `SKILL.md:127–129` nennt diese Regeln nicht vergleichbar ausdrücklich. `READ` erlaubt ausschließlich benannte Aufgabenquellen; die Abgrenzung zur anschließenden externen Suche bleibt knapp.

**Mögliche Folge:** Standalone-Verhalten hängt stärker von Host-Regeln ab; lokale Kontextlektüre und erlaubte externe Suche können verwechselt werden. Kein beobachteter Datenabfluss und kein Beleg, dass höhere Host-Schutzregeln fehlen.

**Fix:** Einen kurzen gemeinsamen Vertrag für jede Landschaftsrecherche definieren: erlaubter Suchraum, abstrahierte Queries, private Details nur mit entsprechender Autorisierung, tatsächliche Quelleneinsicht, Beleggrenzen, Stoppregel. Die kombinierte Route delegiert die Ausführung weiterhin an Research. Keine Pflichtinstallation und keine zweite Landschaft. Fehlender Webzugriff bedeutet begrenzte Evidenz und gegebenenfalls `Unresolved`.

**Nachweis:** Native und kombinierte Szenarien mit privatem Brief, manipulativer Fundstelle und fehlendem Webzugriff. W-004.

### F7 · P2 · Kerntext trägt zu viele bedingte Ausgabedetails

**Beobachtung:** `SKILL.md:90–108` und `:156–175` mischen universelle Aufgabenführung mit Ledger-Ausgabe, speziellen JSON-Feldern, Einrückung und eng begrenzter Formatkorrektur. Der einzige geladene Zusatztext behandelt Research-Komposition.

**Mögliche Folge:** Der Agent muss für eine normale Ideensuche viele nicht benötigte Regeln verarbeiten. Die Mischung erschwert Wartung; ein gemessener Token- oder Qualitätsverlust ist damit noch nicht belegt.

**Fix:** Bedingte strukturierte Ausgabe und detaillierte Trace-Regeln in eine gezielt geladene Referenz verschieben. Kern behält Autorität, Constraints, Phasentrennung, Kapazitätswahrheit und Stop. Mit jedem bisherigen Fall prüfen, ob die ausgelagerte Regel weiterhin rechtzeitig erreichbar ist. Pflicht-LEDGER nicht ersatzlos entfernen, solange seine Trace-Funktion benötigt wird.

**Nachweis:** Freitext- und JSON-Aufgaben laden nur notwendige Regeln; bestehende Routing-, Constraint- und Schemafälle bleiben korrekt. W-005.

### F8 · P2 · Nutzen ist erklärt, aber nicht an einem kompakten Ergebnis demonstriert

**Beobachtung:** Die kanonischen README-Fragmente erklären Mechanismen, Ablauf und Mehrkosten. `usage.md` liefert zwei Aufrufe, aber keinen ausgearbeiteten Beispieloutput. ADHD zeigt ein konkretes Vorher/Nachher-Beispiel, überzeichnet dessen Vorteil jedoch gegenüber dem eigenen Gesamturteil [S5].

**Fix:** Nach einem aussagekräftigen Pilot ein knappes Beispiel veröffentlichen: drei Varianten desselben Mechanismus gegenüber wirklich verschiedenen Abläufen, dazu eine verworfene Falle und ein Falsifier. Ein konstruiertes Beispiel ausdrücklich so nennen. Keine Qualitätszahlen oder Zeitersparnis ohne Nachweis. Nur kanonische README-Fragmente ändern und daraus bauen.

**Nachweis:** Leser erkennt den Unterschied ohne Kenntnis interner Prozesslabels; jedes Ergebnisversprechen ist belegt. In W-006 enthalten.

## Bewahren und bewusst nicht übernehmen

- Begrenzte Originalitätslabels einschließlich `Unresolved`; Originalität ist kein Nutzenbeweis.
- Starke praktische Baseline. ADHDs Verbot der ersten drei offensichtlichen Antworten ist kein geeigneter Standard für Brainstorm.
- Harte Constraints, Trennung von Fakten und Annahmen, keine erfundene Agentenunabhängigkeit und keine Umsetzung ohne Auswahl/Autorisierung.
- Enge Aktivierung für unterschiedliche Mechanismen. Naming, allgemeine Kreativität oder eine eigene CLI sind hier keine automatisch fehlenden Features.
- Ehrlicher Solo-Modus. Gleichzeitigkeit allein ist weniger entscheidend als getrennte Kontexte ohne gegenseitige Ergebnisweitergabe.
- Bestehende Lizenzhinweise. Neue Übernahmen benötigen Herkunftsprüfung; ein eigener Mechanismus-Operatorensatz kann eigenständig formuliert werden.

## Plan und nächste Entscheidung

Der konkrete Entwurf liegt in [PLAN-0003](../../../docs/plans/0003-brainstorm-qualitaet.md). Alle Punkte sind `todo`; der Plan bleibt `draft`. Er ändert weder den aktiven Suite-Plan noch den Skill. Empfohlene Reihenfolge: F1/F2, F3, Kapazität und Recherchegrenze, danach bedingte Regeln auslagern; Nutzen im gemeinsamen Pilot prüfen. Varianten getrennt halten, damit ein Ergebnis einer Änderung zugeordnet werden kann.

## Quellen

Externe Dateien sind auf den untersuchten Commit fixiert; Metadaten und PR-/Issue-Zustände wurden am Auditdatum abgerufen.

- S1: [GitHub-Metadaten](https://api.github.com/repos/UditAkhourii/adhd).
- S2: [ADHD Skill](https://github.com/UditAkhourii/adhd/blob/dd08acc38693127cd0ca2325fe6bf9579131ede1/skills/adhd/SKILL.md), insbesondere Phasen, Frames, Calibration und Cost.
- S3: [Evaluationsmethodik und Grenzen](https://github.com/UditAkhourii/adhd/blob/dd08acc38693127cd0ca2325fe6bf9579131ede1/documentation/evals.md).
- S4: [Benchmark-Runner](https://github.com/UditAkhourii/adhd/blob/dd08acc38693127cd0ca2325fe6bf9579131ede1/bench/run-evals.ts) und [Judge](https://github.com/UditAkhourii/adhd/blob/dd08acc38693127cd0ca2325fe6bf9579131ede1/bench/judge.ts).
- S5: [Ergebnisse einschließlich llm-hang-cli](https://github.com/UditAkhourii/adhd/blob/dd08acc38693127cd0ca2325fe6bf9579131ede1/EVALS.md) und [README-Darstellung](https://github.com/UditAkhourii/adhd/blob/dd08acc38693127cd0ca2325fe6bf9579131ede1/README.md).
- S6: [Frame-Definition und Auswahl](https://github.com/UditAkhourii/adhd/blob/dd08acc38693127cd0ca2325fe6bf9579131ede1/documentation/frames.md).
- S7: [Issue 17: Frames und Personas](https://github.com/UditAkhourii/adhd/issues/17), [Issue 18: Sample-Anzahl](https://github.com/UditAkhourii/adhd/issues/18). Aussagen über Studien wurden hier nicht unabhängig wissenschaftlich geprüft.
- S8: [Repowire-Integration, gemergt am 2026-05-28](https://github.com/prassanna-ravishankar/repowire/pull/313).

Lokale Befunde beziehen sich auf [Core](../scoville-brainstorm/SKILL.md), [Komposition](../scoville-brainstorm/references/research-composition.md), [Recovery-Fälle](tests/recovery-cases.json), [begrenzte ältere Acceptance](acceptance-astra.md), [Luna-Fälle](../../../development/luna-tests/brainstorm-cases.md) und [kanonische README-Fragmente](../../../development/readme/scoville-brainstorm/).
