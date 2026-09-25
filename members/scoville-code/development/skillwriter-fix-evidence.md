# Skillwriter-Überarbeitung von Scoville Code

## Umfang und Ausgangsbasis

Der Nutzer beauftragte am 25. September 2026 die parallele Umsetzung von PLAN-0010 neben der laufenden Plan-Skill-Überarbeitung. ADR-0038 und ADR-0039 wurden zuvor in Aufgabe `01a0d2a8-f239-7f51-bc6b-2b80052f8d4f` nach „beide sollen geschlossen werden“ angenommen und mit dem Fixplan in `890441e` gesichert. Diese Umsetzung verändert keine Plan-Skill-Quellen und beansprucht nicht den gemeinsamen aktiven Planplatz. Die Abschlussfortschreibung betrifft nur PLAN-0010.

Vor den Quelländerungen wurde eine bytegetreue Kopie des Code-Members, seiner README-Fragmente, des Manifests und des importierten Familienvertrags gesichert. Der damals beobachtete HEAD war `8e02436f20f260d8c04cd2ce39f7da7dfad60fd7`. Die Kopie enthielt den tatsächlichen Arbeitsbaum, nicht nur diese Revision. W-001, W-002 und W-003 wurden als getrennte Zwischenstände verglichen. Das damalige Paketstaging ist nicht mehr vorhanden.

## Erhaltene und geänderte Verträge

| Besitzer | Vertrag und Änderung |
| --- | --- |
| `SKILL.md` | Modi, Risikoklassen und Structural/High-Override bleiben erhalten. Ergebnis, aktuelle Operation und Referenzauswahl sind getrennt erklärt. Berechtigungen, Opt-out und kanonische Zuständigkeit bleiben erhalten. |
| `references/planning-and-decisions.md` | Verweist für Materialität auf den Kern statt eine zweite Definition zu pflegen. Planbesitz, vollständige Verhaltensarbeitspunkte und Entscheidungshoheit bleiben erhalten. |
| `references/change-workflow.md` | Die belegte begrenzte Quellensuche bleibt erhalten. Wiederholte Kernregeln sind konsolidiert. Die 2.000-Zeilen-Konvention und ihre begründeten Ausnahmen bleiben bestehen. |
| `references/validation.md` | ADR-0038 erlaubt weitere Prüfungen bei entscheidenden offenen Fragen, veränderten Bedingungen oder verbindlichen Anforderungen. Der Zwei-Korrektur-Trigger bleibt erhalten. |
| Kern und Validation | ADR-0039 erlaubt überholte Assertions nur als Folge ausdrücklich autorisierter Vertragsänderungen. Weiterhin erforderliche Garantien dürfen nicht für grüne Tests entfallen. |
| `references/project-conventions.md` | Neuer, bedingt geladener Greenfield-Vertrag mit offiziellen Ökosystemquellen, minimalem Fallback und ausdrücklich eingebundenen Nutzerdateien. Projektvorgaben zuerst. Bestehende Projekte, neue Module und fehlende Einzelregeln aktivieren ihn nicht. |
| README-Fragmente | Modelluntergrenze, Verwendung, Override-Pfade und Updateverhalten sind beschrieben. Die Texte folgen `benjaminstelzer-imitate-me`. Member- und Suite-README wurden aus den kanonischen Fragmenten erzeugt. |

## Vergleich und Beobachtungen

Die Ausführung nutzte frische Subagenten mit geerbtem Modell und Effort. Exakte Variante und Effort waren in deren Kontext nicht verfügbar und werden nicht aus der Modellfamilie abgeleitet. Alle Aufgaben und Werkzeuge waren auf lokale Fixturearbeit oder lesende Auswertung begrenzt. Ein anfängliches Budget umfasste drei Arme mit je sieben Entwicklungsfragen und drei erst anschließend gegebenen Schlussfragen. Eine anschließende gezielte Runde prüfte die angenommenen Verhaltensänderungen und die neuen Greenfield-Grenzen.

| Prüfung | Beobachtetes Ergebnis |
| --- | --- |
| Vorheriger Skill, W-001 und einfacher Zielprompt | Je zehn Entscheidungsantworten gelesen und bewertet. Keine offene W-001-Regressionsabweichung. Der einfache Prompt löste die allgemeinen Aufgaben ebenfalls angemessen, liefert aber keine Scoville-Routenklassifikation. |
| W-001 gegenüber Endkandidat, sechs Stop-/Schutzfälle | W-001 blockierte die notwendige Prüfung nach wiederhergestellter Infrastruktur und die erneute Endprüfung nach einer konkurrierenden Änderung. Der Endkandidat erlaubte beide. Beide Varianten stoppten nutzlose Wiederholung, erhielten den Zwei-Korrektur-Trigger und verhinderten das Entfernen einer weiterhin erforderlichen Schutzregel. |
| Autorisierte überholte Assertion | Beide Varianten erlaubten im gegebenen Fall die Anpassung an den ausdrücklich neuen Vertrag. Die Präzisierung ist hier kein gemessener Verhaltensgewinn. |
| Sechs Greenfield-Entscheidungsfälle | Endkandidat unterschied vollständiges Greenfield, Projektvorgaben, neue Module und fehlende Einzelregeln. Unlesbare ausdrücklich eingebundene Vorgaben blieben offen. WordPress-Namen überschrieben keine PSR-4-Ladeanforderungen. |
| Reales Fixture: neues leeres Modul im Bestandsprojekt | Agent ergänzte `app/shipping/shipping_cost.py` und passende Tests. Bestehende Dateien blieben erhalten. `python -m unittest discover -s tests` bestand mit fünf Tests. Der gemeldete tatsächliche Lesepfad enthielt Kern, Change und Validation, nicht die Greenfield-Referenz. |
| Reales Fixture: neue Datei ohne explizite Namensregel | Agent ergänzte `app/discount_total.py` nach vorhandener snake_case-Konvention. `python -B -m unittest discover -s tests -v` bestand mit vier Tests. Die Greenfield-Referenz wurde laut Lesebeleg nicht gelesen. |
| Unabhängiges Quellreview | Keine handlungsrelevanten Befunde. Review umfasste Baselinevergleich, vollständigen Kern und Referenzen, Familienvertrag, README-Fragmente und Manifest. Relative Paketlinks existierten, Template-Tags waren aufgelöst. |

Die beiden Fixture-Artefakte und Tests wurden vom ausführenden Agenten anschließend inspiziert. Ein eigener Lauf der neun Tests bestätigte die Ergebnisse. Der dauerhafte Evaluationskorpus enthält zwölf zusätzliche Fälle und insgesamt 44 Definitionen. Diese Zahl bezeichnet definierte Fälle, nicht 44 ausgeführte Modellläufe.

Die Lesereihenfolge der Greenfield-Fälle in der gebündelten Entscheidungsrunde ist kein isolierter Nichtlade-Nachweis. Dafür dienen die zwei getrennten Fixture-Aufgaben mit ihren gemeldeten tatsächlichen Referenzlesevorgängen. Ein vollständig instrumentierter Hostzugriffstest wurde nicht ausgeführt.

Der ursprüngliche Markdown-Instruktionsumfang betrug 4.053 Wörter, W-001 3.802. Der Endstand umfasst durch den zusätzlich beauftragten Greenfield-Vertrag 4.714 Wörter, dessen Referenz nur bedingt geladen wird. Keine allgemeine Tokenersparnis oder höhere Modellleistung wird daraus abgeleitet. Es gab keine vergleichbaren Anthropic-Läufe, keine Kontingentmessung und keine Aussage zur Leistung sämtlicher vorausgesetzter Modellfamilien.

## Paket- und Formatprüfung

Alle drei unterstützten Ausgaben wurden mit dem kanonischen Builder erstellt und gegen ihre Quellen geprüft: general/standalone, general/suite und codex/suite. Code enthält jeweils elf Distributionsdateien. Die Suite-Builds sind Momentaufnahmen der parallelen Arbeitsstände und keine Releasefreigabe für andere Mitglieder.

- Aktueller Standalone-Buildreceipt: `2787e25a62cb76d98fde37c3cc0fe4ca7c2162c66d7dad3f1d0423deae550296`.
- General-Suite-Buildreceipt: `84228f714d317b71dfa281d2aae0e19f44884da1cb05904869bff97fd4647013`.
- Codex-Suite-Buildreceipt: `f39fa03dc85fa7565807d50bf0a0a64f2df62c126ccd49316145d163c4fc2885`.

Die parallele UI-Umbenennung änderte später ausschließlich Code-Familienprojektionen in der Standalone-README und im Standalone-Einstieg. Diese Ausgabe wurde aus dem aktuellen Manifest neu gebaut und geprüft. Die beiden Code-Suite-Projektionen blieben unverändert.

Der lokale Skill-Creator-Validator wurde ausgeführt und meldete das bereits in der Baseline enthaltene `compatibility`-Frontmatter-Feld als nicht erlaubt. Das Feld und sein Inhalt wurden unverändert erhalten. YAML-Parsing, Paketaufbau, Referenzauflösung und scoped `git diff --check` wurden gesondert geprüft. Es gibt keinen behaupteten Skill-Creator-PASS. Diese bekannte Validator-Kompatibilitätslücke bleibt offen und ist kein Nachweis eines neu eingeführten Paketfehlers.

Keine Installation, Veröffentlichung oder Commit der Umsetzung wurde ausgeführt. Der vorherige Astra-High-Befund gilt für den Plan. Das abschließende Implementierungsreview war ein separates lesendes Subagentenreview und wird nicht als Astra-High-Abnahme ausgegeben.

Die abschließende native Planprofilprüfung bestand mit null Fehlern und Warnungen. PLAN-0010 ist abgeschlossen, der gemeinsame aktive Plan wurde nicht geändert. Die automatische Freigabeprüfung lehnte die Bereinigung der beiden oben genannten temporären Aufgabenverzeichnisse vor Ausführung mit `blocked by policy` ab. Sie bleiben erhalten. Kein alternativer Löschweg wurde versucht.

## Astra-Implementierungsreview und ergänzende Nachweise

Auf Nutzerauftrag wurde die Umsetzung in der frischen normalen Projektaufgabe `01a0d7f3-08e4-7bc3-82ae-f8c0c698bd3a` geprüft. Angefordert: `gpt-6-astra`, Effort `high`, `context_mode: fresh`. Der Reviewer konnte die tatsächliche Modellvariante und Effort nicht bestätigen. Konsultation: `code-implementation-astra-high-20260925-01`, Scope: `PLAN-0010 implementation snapshot 2026-09-25`.

Die erste Abnahme wurde verweigert: zwei P2-Nachweislücken betrafen den eigenständigen zweiten Alternativcheck in W-002 sowie eine lesbare externe Konventionen-Datei und getrennte Teilprojekt-/Refactoringfälle in W-004. Im ausgelieferten Anweisungsvertrag fand der Reviewer keinen belegten neuen Fehler. Er bestätigte den vollständigen Quellenvergleich, drei im Speicher rekonstruierte bytegleiche Code-Pakete mit je elf Dateien, scoped `git diff --check` und unveränderte Hashes aller 44 erfassten Dateien vor und nach dem Review. Der bekannte `compatibility`-Validatorfehler blieb offen. Neue Modell- oder Fixtureläufe führte der Reviewer nicht aus.

Der zuvor erklärte Abschluss war hinsichtlich dieser Pflichtnachweise voreilig. Terminale Planhistorie wird nicht zurückgesetzt und der parallele aktive Plan bleibt unverändert. Die fehlende Abnahme bleibt bis zur ergänzenden Prüfung ausdrücklich offen.

Die gezielten Ergänzungen verwenden bestehende Evaluator-Kontexte, keine frischen oder verblindeten Modellläufe. Exakte Modellvariante und Effort sind nicht verfügbar. Das Budget umfasst einen Vergleichsfall mit zwei Entscheidungsantworten sowie drei begrenzte Projektfälle. Es begründet keine allgemeine Wirksamkeits- oder Anbieterbehauptung. Der kanonische Korpus enthält nach drei Ergänzungen 47 Definitionen; diese Zahl bezeichnet weiterhin keine Anzahl ausgeführter Modelltests.

- Zweite Alternative ohne Zustandsänderung: Nach blockierter DB-Integration und erfolgreicher, aber nicht beweiskräftiger Syntaxprüfung wählte W-001 den Stopp. Der Endkandidat wählte den vorhandenen DB-unabhängigen Serializer-Vertragstest zur offenen Erhaltung von `status/reason/error/source`. Er beanspruchte weder einen bereits erfolgten Testlauf noch Integrationsnachweis. Beide Antworten entstanden im selben bestehenden Kontext nach Lesen beider Kerne und Validation-Referenzen. Dies ist ein Entscheidungsvergleich, kein ausgeführter Serializer-Test.
- Refactoring: Der Evaluator extrahierte `_validate_weight` in der bestehenden Versand-Fixture, erhielt die Preisgrenzen und Fehlermeldung und meldete fünf bestandene unittest-Tests. Der ausführende Agent inspizierte das Ergebnis und die Tests. Tatsächlich gemeldet wurden Kern, Change und Validation als Lesepfade, nicht die Greenfield-Referenz.
- Teilprojekt: Für Reporting innerhalb der bestehenden Rabatt-Fixture wählte der Evaluator `app/order_report.py` und `tests/test_order_report.py` nach den beobachteten Nachbarmodulen. Es wurden keine Dateien angelegt und keine Tests behauptet. Tatsächlich gemeldet wurden Kern und Change als Lesepfade, nicht die Greenfield-Referenz. Dieser Fall belegt eine konkrete Planungsentscheidung, keine implementierte Reportingfunktion.

Rohartefakte der Ergänzungen liegen im bestehenden temporären Aufgabenbaum unter `astra-implementation/`; Refactoring und Teilprojekt nutzen die vorhandenen Fixtureverzeichnisse. Die Lesepfade sind Evaluatorberichte, keine instrumentierte Zugriffskontrolle.
- Lesbare externe Konventionen: Ein vollständiges neues Python-Projekt referenziert aus seiner `AGENTS.md` ausdrücklich `docs/project-conventions.md`. Alle Evaluator-Shellaufrufe starteten und blieben in `astra-implementation/unrelated-cwd/`. Die Datei wurde relativ zur Projekt-AGENTS.md gelesen. Tatsächlich erzeugt wurden `app/label_tool.py`, der Paketmarker `app/__init__.py` und `checks/test_label_tool.py` gemäß den externen Struktur- und Namensregeln. Keine Default-Verzeichnisse `src/` oder `tests/` wurden angelegt. Fünf unittest-Fälle bestanden einschließlich Unicode-Whitespace und tatsächlichem Paketimport. Der ausführende Agent inspizierte Funktion und Tests. Der Evaluator las den gebauten Standalone-Kern, Change, Validation und Greenfield-Referenz sowie genau die ausdrücklich eingebundene Projektdatei. Dieser positive Fall lief im fortgesetzten Vergleichskontext.

Die vier ergänzenden Fälle erfüllen die zuvor fehlenden konkreten Nachweisbereiche. Die erneute unabhängige Abnahme ist separat zu bestätigen. Es wurden keine ausgelieferten Skill- oder README-Bytes geändert.
### Abschließende Astra-Abnahme

Die fortgesetzte Konsultation `code-implementation-astra-high-20260925-02` in derselben Reviewaufgabe erteilte **Abnahme: JA** für `PLAN-0010 supplemental acceptance 2026-09-25`. Beide P2-Nachweislücken sind geschlossen. Es verbleiben keine handlungsrelevanten Befunde im geprüften Code-Umfang. `context_mode: continued`; weiterhin angefordert `gpt-6-astra` mit `high`, tatsächliche exakte Modellvariante und Effort für den Reviewer unbestätigt.

Astra las die vier neuen Originalantworten, Fixturequellen, Testquellen, Definitionen und ergänzten Plan-/Evidenzangaben. Der zweite Alternativfall belegt die Prüfentscheidung; dafür wurde kein ausgeführter Serializer-Test verlangt oder behauptet. Der positive Override belegt Struktur und Dateinamen. Teilprojekt und Refactoring belegen die jeweiligen negativen Aktivierungsentscheidungen innerhalb der dokumentierten Lesebeleggrenzen. Der voreilige frühere Abschluss bleibt dokumentiert und ist nach Ergänzung der Nachweise kein aktueller Abnahmeblocker.

Zu Beginn und Ende der Nachprüfung waren 41 von 44 Snapshotdateien unverändert. Nur die angekündigten Entwicklungsdateien Evaluationskorpus, Evidenzbericht und PLAN-0010 wichen ab. Sämtliche ausgelieferten Code-/README-Quellen und alle drei Code-Pakete blieben unverändert; jeweils elf Paketdateien entsprachen ihren Buildreceipts. Scoped `git diff --check` bestand, 47 Definitionen enthielten keine doppelten IDs. Die Planprofilprüfung des ausführenden Agenten hatte null Fehler und Warnungen.

Die Abnahme ist weder Releasefreigabe noch allgemeiner Wirksamkeitsnachweis. Bestehende Evaluatorkontexte, nicht instrumentierte Lesepfade/Arbeitsverzeichnisse, nicht vom Reviewer wiederholte Tests und der bestehende `compatibility`-Validatorfehler bleiben die oben beschriebenen Grenzen. Nach der Abnahme wurde ausschließlich dieser Ergebnisvermerk ergänzt. Keine Installation, Veröffentlichung oder Commit. Die Reviewaufgabe bleibt für Rückfragen offen.