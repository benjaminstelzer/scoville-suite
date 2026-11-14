# Goodhart-Korrekturen nach dem Opus-Review

Bericht zu [PLAN-0067](../plans/0067-goodhart-korrekturen-nach-dem-opus-review.md). Er nennt Anlass, Befunde, Korrekturen, offene Punkte und Grenzen.

## Anlass und Aufbau der Prüfung

Am 2026-11-13 lasen sechs Prüfer (Claude Opus 5.5, Reasoning-Stufe xhigh, nur lesend) die gebauten Pakete aller Skills, wie ein Modell sie sieht. Fünf prüften je eine Skill-Gruppe auf zwei Fehlerarten: Regeln, bei denen der Prozess zum Ziel wird, und Sätze, die ein Modell missverstehen kann. Der sechste verglich jedes Beispiel der Skilltexte mit den Aufgaben der Messungen zu PLAN-0066.

| Prüfer | Umfang | Befunde |
| --- | --- | --- |
| 1 | Code mit seinen Referenzen und den gemeinsamen Code-Qualitätsregeln | 22, dazu 4 mit geringer Sicherheit |
| 2 | UI ohne WordPress | 25 |
| 3 | WordPress-Adapter von UI | 33 |
| 4 | Plan, Handoff, Project Context Cleanup, Setup | 33 |
| 5 | Skillwriter, Ask, Workflow, gemeinsame Schreib- und Freigaberegeln, Prompttexte der Helfer | 33 |
| 6 | Beispiele gegen Messaufgaben | 25 Übereinstimmungen, dazu Listen der Bewerter |

Jeder Befund nennt Datei, Zitat, eine konkrete Aufgabensituation und das falsche Verhalten darin. Rund 60 Zitate wurden am Quelltext nachgeschlagen; alle standen so da. Fünf Agenten (Opus 5.5, Stufe high) setzten die Befunde je Skill-Gruppe an den kanonischen Quellen um und prüften dabei jeden Befund erneut; jeder Diff wurde danach gelesen und an drei Stellen nachgebessert.

## Entscheidungen des Eigentümers

Drei Korrekturen ändern Verhalten und wurden am 2026-11-14 entschieden:

- [ADR-0232](../decisions/0232-plan-kleine-zusatzarbeit-direkt-erledigen.md): Arbeit, die kein Work Item abdeckt, die nicht geplant werden sollte und in der Sitzung fertig wird, erledigt der Agent direkt.
- [ADR-0233](../decisions/0233-ui-code-review-liest-nur-den-quelltext.md): Ein Code-Review von Oberflächen-Quelltext liest den Quelltext und rendert nichts.
- [ADR-0234](../decisions/0234-workflow-step-review-als-abschluss-bei-einem-step.md): Bei einem Work Item mit einem Step gilt das bestandene Step-Review als Abschluss-Review.

## Korrekturen

### Beispiele aus Messaufgaben

Entfernt oder durch Beispiele aus fremden Domänen ersetzt:

- **Code:** „seven weekdays by three shifts", „permission check, validation and audit record", der Benachrichtigungskanal in Regel 3, die Domänenwörter in Regel 2, das Rundungsbeispiel, das Skript für einen Nutzer, die Liste nach „such as a file name", `test_slugs.test_umlauts_are_transliterated`, `pricing.py`, das Beispiel zum umbenannten Feld.
- **Code-Qualitätsregeln:** der Export über eine temporäre Datei, die Liste der Abstraktionsformen und zwei der drei Köder unter „Not defects". Der dritte bleibt in anderen Worten, weil er eine eigene Regel gegen Fehlalarme ist: Code, der einer vorhandenen Funktion ähnelt, aber eine andere Frage beantwortet.
- **UI:** die Beispiele zu Schritt 1 und 2 (Toolbar-Button 44 neben 32, Icon-Button im Tag-Eingabefeld, kompakte Bedienelemente in der Kartenüberschrift), das 18px-Icon, zwei Beispiele in den Prüfreferenzen.
- **WordPress:** die Beispielfrage zur Block-Editor-Sidebar samt Antwort, `width: 1200px`, die Selektorliste und die Zustandsnamen in den Zeilen 7 und 9 der Prüfliste.
- **Übrige:** der Satz zu endenden Umständen in Cleanup, das Konfigurationsbeispiel in Ask, das Evidence-Beispiel in Plan, das Beispiel in der Schreibanleitung.

Die Regeln selbst bleiben, auch wo eine Aufgabe genau ihren Gegenstand als Mangel einbaut, etwa der Zugriff auf interne Namen eines anderen Moduls oder die Zeilen der WordPress-Prüfliste. Die Aufgaben wurden gebaut, um diese Regeln zu prüfen.

### Prozess als Ziel und missverständliche Sätze

- **Code:**
  - Der Eingang der Regeln nennt sie Regeln und nicht mehr Schritte.
  - Eine Schutzprüfung richtet sich danach, ob der Fall im unterstützten Gebrauch oder über einen konkreten Angriffsweg erreichbar ist. „Nicht erneut prüfen" gilt nur diesseits einer Prozess- oder Netzgrenze.
  - Fail-first verlangt ein Scheitern an der Assertion.
  - Der Bericht nennt den beweisenden Test; die Zeilen zu wiederverwendetem Code, Schutzprüfungen und Schleifen entfallen.
  - Der Name des Tests stammt aus der Ausgabe des projekteigenen Testbefehls.
- **UI:**
  - Die beiden Arten von Review sind überall benannt.
  - Die Übergänge in `ui-interactions.md` sind Eigenschaften des Codes statt Bedienschritte.
  - Schritt 7 vergleicht die Größe, die herauskommt, statt Variantennamen aufzulisten.
  - Die Regel „beim Umsetzen nicht rendern" steht einmal, die Wiederholungen in fünf Referenzen sind gestrichen.
  - Prüfberichte brauchen keinen Status je bestandener Stelle.
- **WordPress:**
  - Auslöser, die beim Umsetzen WordPress, einen Browser oder mehrere Versionen starten ließen, sind auf verlangte Prüfungen beschränkt.
  - Eine Stilausnahme hat eine Begründung statt zweier Aufzeichnungen.
  - Die Textdomain ist die vorhandene des Plugins.
  - Anweisungen zur Pflege der Quellenstände stehen jetzt in `members/scoville-ui/development/wordpress-source-revalidation.md`.
- **Plan:**
  - ADR-0232 ist in Beschreibung, Eingangssatz, Regeln 3, 5 und 7 und in `authoring.md` umgesetzt.
  - Ein Step-Status oder eine Evidence-Zeile löst keinen eigenen Validatorlauf aus.
  - Evidence nennt, was ausgeführt oder gelesen wurde und was es zeigte.
  - Eine Decision hält eine Wahl zwischen Alternativen fest; Aktivieren, Abbrechen und Löschen stehen in Statusfeldern.
- **Handoff:** ein bis drei Resume Steps; leere Kategorien entfallen.
- **Cleanup:** Eine Regel, die nur bis zu einem Ereignis gilt, nennt dieses Ende in der Regel.
- **Skillwriter und Freigaberegeln:**
  - Ein erneuter Lauf des gescheiterten Falls belegt nur, dass die Reparatur zu diesem Fall passt.
  - Ein Treffer eines Bewerters, der nur Antworttext abgleicht, belegt die Formulierung und nicht das Verhalten.
  - Die Pflicht, jede Regel als prüfbaren Schritt zu schreiben, ist gestrichen.
- **Workflow:**
  - ADR-0234 ist umgesetzt; der Helfer selbst ist unverändert und kennt die Zahl der Steps nicht, deshalb nennt der Hauptablauf sie in den Belegen.
  - Der Reviewer darf für die Suche nach vorhandener Logik unveränderte Dateien lesen.
  - Eine Frage, die der Hauptablauf selbst beantworten kann, braucht keinen Explorer.
- **Ask:** Code-Qualitätsregeln gelten nur für ein Code-Review; „hidden expectation keys" ist gestrichen.
- **Gemeinsame Regeln:**
  - Ein Abschlussbericht nach einer kleinen Änderung lädt die Schreibreferenz nicht mehr.
  - Die Konsolenzusammenfassung eines Testläufers ist keine Maschinendaten.
  - Eine vollständige Kopie einer Referenz im Kontext gilt als gelesen.

## Einordnung je Befund

| Bericht | Behoben | Verworfen | Offen |
| --- | --- | --- | --- |
| 1 Code | F1 bis F22; aus der Liste mit geringer Sicherheit Regel 1 und zwei Stellen in `validation.md` | „modulweiter veränderlicher Zustand, außer das Projekt nutzt ihn": die Ausnahme würde eine eigene Regel aufweichen. `validation.md`, Satz zum verlangten unabhängigen Review: Schutz für Reviews im Workflow. | Welche Datei bindet, wenn AGENTS.md und CLAUDE.md beide gelten |
| 2 UI allgemein | F1 bis F25 | keiner | Ob eine reine Textkorrektur nur die Wortwahl-Referenz lesen soll |
| 3 WordPress | W1 bis W28, W30 bis W32 | keiner; bei W11 ohne Zeilenliste, weil jede Liste die Messaufgabe zum gezielten Audit steuern würde | W29 (Versionsmuster im PHP-Beispiel), W33 (`submit_button( esc_html__( … ) )`): beide hängen an ungeprüften WordPress-Fakten |
| 4 Plan, Handoff, Cleanup, Setup | F1 bis F6, F8 bis F16, F18 bis F21, F23 bis F30 | keiner | F7, F17, F22, F31, F32, F33, siehe unten |
| 5 Skillwriter, Ask, Workflow, gemeinsame Regeln | F1 bis F25, F27 bis F33 | keiner | F26 und die Regel zur unbegründeten Zustimmung in Ask |
| 6 Beispiele | alle Übereinstimmungen der Stufen „identisch" und „gleiches Szenario" | Regeltexte, die den Gegenstand einer Aufgabe benennen; das Herstellerbeispiel „CRITICAL: you MUST" | keiner |

Offene Befunde, die eine Entscheidung des Eigentümers brauchen:

- **Plan F7:** Die Decision-Vorlage enthält „Binding sections: complete" vorausgefüllt, obwohl der Vermerk ein Urteil voraussetzt. ADR-0224 regelt die bindenden Abschnitte.
- **Setup F17 und F22:** Bei einer Migration verweist Evidence auf eine Datei in einem ignorierten temporären Ordner; eine einmalige Modellwahl wird in einem Plan-Step festgehalten.
- **Plan F31 bis F33:** Aufräumen alter Decisions beim Anlegen eines Plans; Prüfung auf umgeleitete Zielpfade vor jedem Schreiben; eine Decision für geänderte Acceptance eines begonnenen Work Items.
- **Ask F26 und Zeilen 98 bis 101:** Jede Antwort wiederholt Kennungen des Beraters; ein Befund, dem der Aufrufer widerspricht, soll mit dem Berater geklärt werden.

## Prüfungen

- `python development/check_all.py`: 12 von 12 bestanden, darunter 101 Shared-Tests, 73 Suite-Tests, 147 Plan-Tests, 87 Workflow-Tests, 63 Ask-Tests und 31 Setup-Tests.
- Eine Suche in allen Skilltexten, Referenzen, Prompttexten und gemeinsamen Regeln nach 18 der entfernten Beispiele und Formulierungen findet keine mehr.
- Sechs Modellfälle in den `evaluation-cases.json` von Plan und Handoff sind an ADR-0232 und die neuen Handoff-Regeln angepasst.

## Grenzen

- **Keine Modellläufe.** Die Wirkung der Korrekturen ist nicht gemessen. Sie folgen aus dem Lesen der Texte.
- **Die vorhandenen Messaufgaben taugen dafür nur eingeschränkt.** Ihre Mängelarten stammen aus den Regeln, und bei etwa der Hälfte entscheidet Text in der Antwort über den Erfolg, siehe den Nachtrag im [Bericht zu PLAN-0066](0066-konkrete-skilltexte-und-auslieferungsbefehl.md). Eine belastbare Aussage braucht Aufgaben, deren Ersteller weder die Skills noch die bisherigen Aufgaben kennt und die an Dateien, Tests und Befehlen bewerten.
- **Der Bewerter der Handoff-Aufgabe** (`score_hs.py` im Messordner) verlangt weiter drei Resume Steps und passt nicht mehr zum Skill.
- **Das Mermaid-Diagramm** in Workflow wurde gelesen, nicht mit einem Parser geprüft.
- **Die Datei `skills/AGENTS.md`** außerhalb des Repositories sagt weiter „Every future model test uses gpt-6.1-sol"; die Freigaberegeln ergänzen jetzt, dass eine Aussage über ein anderes Modell einen Lauf mit diesem Modell braucht.
- **Geänderte Python-Helfer:** In drei Helfern von Workflow und Ask sind nur Prompttexte geändert. Vor einer Auslieferung braucht es dafür einen neuen Lauf der privaten Laufzeit-CI.
