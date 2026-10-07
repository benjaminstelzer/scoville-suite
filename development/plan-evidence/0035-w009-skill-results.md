# W-009: abgegrenzte Skill-Ergebnisse

Aktueller Stand nach W-017 und Selector-EOF-Korrektur. W-009 ist begrenzt abgenommen;
der [abschließende Sol-Review](0035-w009-final-sol-acceptance.md) bestätigt den gebundenen Stand; der [Ask-Sol-6.1/high-Review](0035-w009-final-sol-review.md) ist abgeschlossen. Die folgenden
gezielten Nachweise begründen keine allgemeine Zuverlässigkeitsgarantie.
Aktuelle Paket-/CI-Bindung: [Selector-Fix](0035-w009-selector-eof-fix.json) und
[Paket-/Semantik-/Routenvergleich](0035-w009-eof-final-static.json).
Die darunter erhaltenen früheren Berichte gelten nur für ihren damaligen Stand.

| Skill | Erhaltener ausgewählter High-Nachweis | Neuer praktischer Nachweis und verbleibende Grenze |
| --- | --- | --- |
| Code | Zehn englische Aufgaben: neun je 3/3, Compatibility 4/5, 31 PASS und ein erhaltener FAIL. Code7-Fortsetzung 2/2 trägt nach ADR-0190 den begrenzten praktischen Ersatz des alten abstrakten Falls. | Haushaltsbuch in zwei unabhängigen Ausgangskopien auf Windows und Linux: jeweils zwölf unabhängige Produktgruppen mit 17 CLI-Aufrufen bestanden. Die Medium-Proben ersetzen keine High-Cases. |
| Plan | Verständnis 9/9; Decision 3/3; korrigierter Resume 3/3. Ein neuer Resume-Lauf lässt Datum und erfüllte Instructions stehen; der eingefrorene Effektvertrag besteht. | Beide neuen Planner legen den nativen Dreipunktplan an; die Manager führen und schließen ihn. Der bestätigte Selector-EOF-Fehler ist korrigiert und über sechs OS-/Python-Jobs sowie den ursprünglichen Windows-Consumer nachgetestet. |
| UI | Ausgewählte Verständnis- und gerenderte Funktionsfälle bestanden; historische fehlende Keyboard-/Fokusbeobachtungen bleiben erhalten. | Drei unterschiedliche Browserfälle je Windows/Linux bestehen mit den betrachteten Renders und abgegrenzten echten Interaktionen. Browser-/Viewport-/Accessibility-Grenzen bleiben; kein Nachweis für W-015. |
| Ask | Drei native High-Fälle belegen Routing, richtigen Befund, vollständige Adviser-Finals und geschützte Fixtures. Exakte Klartextgleichheit des verschlüsselten Auftrags bleibt unverifiziert. | Drei Fälle je OS ausgeführt. Linux Ask1/2 vollständige Antworten nachgeliefert. Ask3-Protokoll-FAIL und zusätzliche Guided-Recovery-Abweichung bleiben. Keine vollständige Ask-Abnahme daraus; vorhandene Source-Regel ist eindeutig. |
| Setup | Ausgewählte Verständnis- und korrigierte tatsächliche Consumer-Fälle je 3/3. | Drei Fälle je OS bestehen mit tatsächlichen Konfigurations- und Routing-Consumern. Kein Workflow-/Adviser-Start aus der Konfiguration wird behauptet. |
| Handoff | Verständnis 6/6 und aktueller Unknown-goal-Fall 3/3; frühere Fehlzuordnungen bleiben erhalten. | Drei Fälle je OS sind geprüft; zwei Windows-Textfehler wurden durch dieselben Akteure korrigiert und komplett nachgelesen. Originale bleiben erhalten. Keine neue Source-Regel aus diesen Kompositionsfehlern. |
| Cleanup | Ausgewählte Verständnis- und praktische Änderungsfälle je 3/3. | Drei Fälle je OS bestehen: Safeguards, native Index-/Plan-Zuordnung und ausgelagerte Verfahren bleiben vollständig nutzbar. |
| Workflow | Frühere funktionale Teilnachweise gelten abgegrenzt; frühere vollständige High-Proben enthalten Ausführungsfehler und bleiben ohne uneingeschränkten Vertragspass. | Zwei frische Medium-Gesamtläufe erfüllen die unabhängige Produktabnahme und beobachten je zwei Managerwechsel bei 15/15. Die damalige npm-Invocation bleibt unverifiziert; die isolierte Hostkorrektur besteht zwölf Tests am unveränderten Consumer. Kein vollständiger Protokoll-PASS aus dem Produkt-PASS. Der zusätzliche normale High-Consumer endet mit drei natürlichen Übernahmen, sichtbarer offener Frage und einmaliger Originalantwort; alle 13 Akteure terminal, ergänzende Sol-Abnahme vollständig abgeschlossen. |

[Zusatzbericht](0035-w009-additional-os-skills.md) erhält alle dreißig
Originalfinals, unveränderte Erwartungen, Korrekturen, tatsächliche Linux-
Modelle und unbekannte Windows-Modelltelemetrie. Ein zusammenhängender
Sol-Review bewertet die fünf Skill-Blöcke; die nötigen Korrekturen sind über
denselben Handle abgenommen. Originale und Nachlieferungen werden nicht
gepoolt. Die Guided-Recovery ist kein unveränderter Ask-Dispatch-PASS.

[Integrationsbericht](0035-w009-final-integration.md) bindet die tatsächlichen
Plan-/Code-/Workflow-Produkte, Managerübernahmen, Pflichtreviews, Korrekturen,
Hostgrenzen und vollständigen unabhängigen Aufrufe. Linux verwendet Node
22.22.0, Windows Node 25.9.0. Beide schützen dieselben fünf ursprünglichen
Eingabedateien. Alle nativen Akteure sind vor der unabhängigen Prüfung terminal.
Luna/medium ist hier ausdrücklich beauftragt; die ursprünglichen High-Blöcke
behalten ihre eigenen Sprach-, Profil-, Varianten- und Modellgrenzen. Ein
vollständiger macOS-Agentenlauf bleibt unverifiziert.

Python-Helper und Portabilität: Runtime und Development bestehen am aktuellen
privaten Snapshot jeweils 6/6 auf Windows, macOS und Linux, Python 3.11/3.x.
Vier aktuelle Testexporte bestehen. W-017 hält das maschinelle Inventar der
öffentlich ausgelieferten Skill-Pfade, Diagnosen, bestätigten Korrekturen und
Consumer-Nachtests. Der EOF-Nachtrag betrifft vier Selector-Kopien und verändert
keinen Anleitungstext seit dieser Bindung. Keine festen Prosa-Gates.

Die historischen Source-/Case-Korrekturrunden sind in den Originalberichten und
Rohquellen erhalten; eine vollständige summierte Rundenzuordnung je Skill ist
weiterhin nicht abgeglichen. Code-Nachläufe sind nach ADR-0188 freigegeben;
Fixture- und Hostreparaturen sind keine Skill-Umschreibungsrunde. Der aktuelle
Zusatzblock rechtfertigt keine weitere Source-Umschreibung. Kostenflächen und
fehlende globale Usage sind im [Usage-Bericht](0035-w009-usage-report.md)
getrennt. Alle historischen FAILs und unverifizierten Pflichtwege bleiben
sichtbar. Der [Follow-up desselben Sol-Advisers](0035-w009-final-sol-followup.md)
bestätigt die Teilnachweise ohne neuen Source-Defekt. Die wiederhergestellte
High-Familie bleibt Guided/BLOCKED; beide tatsächlichen Protokolllektüren
bestehen nach dem Hostfix. Der einmalige neue normale High-Consumer hat die
authentifizierte Übernahme der ausstehenden W-002-Entscheidung, echte Frage,
einmalige Originalantwort und regulären Abschluss tatsächlich belegt. Sol
bestätigt die Schließung dieser fehlenden Kombination; seine [vollständige abschließende Antwort](0035-w009-final-sol-acceptance.md)
ist erhalten. Kein weiteres Wiederholen der
alten terminalen Familie.

## Erhaltener früherer Abschlussstand

Stand: 06.10.2026. W-009 bleibt offen. Dies ist der gemeinsame Ergebnisbericht,
kein abgeschlossener Abnahmenachweis. Position, Budget und vollständige
Fall-/Review-Verweise stehen in [0035-w009-current.md](0035-w009-current.md).
Alte FAILs bleiben erhalten; Kandidaten und Testarten werden nicht gepoolt.

| Skill | Testart und beobachtetes Ergebnis | Korrektur/Nachtest und Grenze |
| --- | --- | --- |
| Code | Zehn englische praktische Aufgaben: neun je 3/3, Compatibility 4/5; insgesamt 31 PASS und ein FAIL in 32 aktuellen Beobachtungen. | Der FAIL lässt die bisherige Exporter-Schnittstelle als Entscheidungsoption aus. Zwei weitere Läufe bestehen mit unveränderter Code-Guidance; kein neuer Source-Fix daraus. Ältere Fehler und abstrakte 0/3 bleiben getrennt; ADR-0190 ersetzt nur dessen begrenzte Abnahme. [Sol](0035-w009-core-followup-sol-review.json). |
| Plan | Verständnis 9/9; ursprüngliche Decision-/Resume-Effekte je 3/3. Aktuell Decision zuvor 3/3 und korrigierter Resume 3/3. | Sichere Vorbereitung vollständiger Schreibdaten nachgetestet. Alter leerer-Plan-FAIL bleibt. Neuer Lauf 3 lässt Datum und erfüllte Instructions stehen; der eingefrorene Effektvertrag besteht. [Aktuelle Beobachtungen](0035-w009-plan-safe-write-observations.json), [Sol](0035-w009-core-followup-sol-review.json). |
| UI | Verständnis 3/3; praktische Auditfälle mit betrachteten Renders 3/3. | Kein bestätigter Source-Fehler in diesen Fällen. Fehlende Keyboard-/Fokusbeobachtungen bleiben unverifiziert; kein Nachweis für W-015. [Auditreview](0035-w009-ui-effects-review.json). |
| Ask | Drei native Fälle zeigen Routing, vollständige Adviser-Ergebnisse, Empfängerfinal und Fixture-Schutz. | Exakte Helper-/Spawn-Klartextgleichheit bleibt UNVERIFIED; vorhandene SDK-Beobachtung schließt diese Grenze nicht. Keine identischen Wiederholungen dafür und kein allgemeines Ask-PASS. [Sol](0035-w009-ask-native-sol-review.json). |
| Setup | Verständnis 3/3; praktische Auflösung am revidierten Kandidaten 3/3. | Tatsächlicher Ask-Consumer wählt einmalig high bei gespeichertem medium. Konfiguration bleibt erhalten, kein Adviser startet. Frühere Fehler bleiben. [Revision-1-Review](0035-w009-remaining-correction-review.json). |
| Handoff | Verständnis 6/6; historischer Funktionsblock 3 PASS/2 FAIL; aktueller Unknown-goal-Fall 3/3. | Unbekanntes Ziel blockiert; unbekannte Acceptance verlangt Klärung bei abhängiger Handlung. Frühere falsche Quellenzuordnung bleibt. Acceptance-only und echte Prozess-Recovery sind damit nicht belegt. [Aktueller Sol-Block](0035-w009-handoff-narrowing-review.json). |
| Cleanup | Verständnis 3/3 und praktische Änderungen 3/3. | Auslagerung bewahrt verbindliche Safeguards und Leseverweis. Kein neuer Source-Fix aus diesen Ergebnissen; nur ausgewählte Fälle. [Gruppenreview](0035-w009-remaining-block-review.json). |
| Workflow | Aktueller voller Nachtest: fünf Kriterien SUCCESS, drei FAIL, Child-Crossing unverifiziert. Beide Fixture-Punkte fertig; kein Coordinator-Checkpoint, Nachfolger oder Handoff. | Opus-Handoff-Klarstellung eingebaut und von Astra geprüft; ihre Verhaltenswirkung bleibt unbelegt. Abgeschnittene Pflichtlektüre ohne Nachlesen beobachtet. Vollständige Abnahme offen. [Sol](0035-w009-full-handoff-clarified-sol-review.json), [Lektüre](0035-w009-manager-required-read-observation.json). |

Verständnisfragen und praktische Aufträge sind getrennte Testarten. Englische
Erklärungen hypothetischer deutscher Handoffs belegen keinen ausgeführten
deutschen Transfer. Aktuelle native Code-/Plan-/Workflow-Kontexte weisen
gpt-6-luna/high aus; Gruppenbewertungen stammen von gpt-6.1-sol/high.
Die Originalberichte behalten ihre jeweiligen Sprach-, Modell- und Profilgrenzen.

Source-Deltas und Vorher-/Nachher-Texte stehen in den bestehenden
[externen Korrekturen](0035-w009-external-close-source-changes.json),
[Entwicklungspfad-Korrekturen](0035-w009-development-path-test-corrections.json)
und der [Startup-Korrektur](0035-w009-workflow-startup-source-correction.json).
Die korrigierte Plan-Schreibregel und der Startup-Absatz haben gezielte Nachtests.
Fallrevisionen bleiben in ihren Originalberichten; die vollständige summierte
Zuordnung der Korrekturrunden je Skill ist noch nicht abgeglichen.
Fixture-Reparaturen zählen nicht als Skill-Korrekturrunden.

Aktuelle Runtime- und Entwicklungsmatrizen bestehen jeweils 6/6 auf Windows,
macOS und Linux, Python 3.11/3.x. [Actions-Bindung](0035-w009-manager-handoff-ci-result.json)
und [vier Paketprüfungen](0035-w009-manager-handoff-package-check.json) halten den
geprüften Stand fest. Python-Toolprüfungen belegen keine vollständige Modellwirkung.
Die erneute Linux-Agentenprobe ist ausgeführt mit den oben genannten Grenzen;
ein nativer macOS-Agentenlauf wird nicht behauptet.

Paket-/Semantik-/Routenkosten und tatsächliche Usage stehen im
[Usage-Bericht](0035-w009-usage-report.md). Fehlende Messungen bleiben unverifiziert;
Tokenzahlen werden nicht in Preise oder Ersparnis umgedeutet. Ausgelassene
Varianten bleiben gemäß ADR-0180 unverifiziert. README-Compatibility beschreibt
ausgewählte Ergebnisse, keine vollständige Suite-/Workflow-Baseline.
Der Workflow-Blockreview ist abgeschlossen. Der abschließende W-009-Review
folgt nach dem Abgleich der offenen Pflichtnachweise; die vollständige
Workflow-Abnahme bleibt offen.

Aktueller [Sol-Blockreview](0035-w009-full-handoff-clarified-sol-review.json):
vollständiger Vertrag FAIL. Beide Fixture-Punkte sind fertig, aber der Manager
ließ den Coordinator-Checkpoint aus; kein Nachfolger und kein Handoff.
Die [Pflichtlektüre](0035-w009-manager-required-read-observation.json) war durch
einen gebündelten Werkzeugaufruf abgeschnitten: 5 × maximal 5.000, kombiniert
12.008 Tokens gegen die äußere Standardgrenze 10.000. Keine Suite-Limitänderung.
Ausgelassene Abschnitte wurden nicht nachgelesen. Astra prüft die gezielte
Lese-Klarstellung vor einer Source-Änderung; noch kein neuer Modelltest.
