# Konkrete Skilltexte und Auslieferungsbefehl

Bericht zu [PLAN-0066](../plans/0066-konkrete-skilltexte-und-auslieferungsbefehl.md). Die Abschnitte folgen den Work Items.

## W-001 Auslieferungsbefehl

`../shared/build/release_suite.py` fasst die Schritte zwischen committeter Quelle und veröffentlichten Zielen in zwei Befehle:

- `prepare` prüft saubere Quellen auf main, baut je Profil die Suite- und die Einzelansicht, prüft deren Veröffentlichungsbelege, exportiert und validiert die Quellen, durchsucht den Inhalt nach Pfaden im Benutzerverzeichnis, gleicht jedes Ziel-Repository mit seinem Staging-Baum ab und stellt die Änderungen bereit. Es committet und pusht nichts.
- `publish` läuft nach der Freigabe: Es verweigert bei geändertem Quellenstand, committet, pusht main und vergleicht jeden Remote-Stand mit dem lokalen Commit.

Die Ziele leitet das Skript aus `suite.json` ab. Die Staging-Ordner heißen jetzt einheitlich `suite-<profil>`, `standalone-<profil>` und `export-<profil>`; die alten Ordner `general`, `mainloop` und `export-mainloop` sind entfernt.

Geprüft:

- Neun Tests in `../shared/tests/test_release_suite.py`: Zielableitung, Abgleich mit Hinzufügen, Ändern und Löschen bei unberührtem `.git`, Verweigerung bei fehlendem Staging-Baum, bei nicht bereitgestellten Änderungen, falschem Remote und falschem Branch, Fund eines persönlichen Pfads mit Datei und Zeile, Veröffentlichen gegen ein lokales Test-Remote mit Remote-Vergleich, Verweigerung bei geändertem Quellenstand und ohne Vorbereitung.
- Ein echter `prepare`-Lauf im Arbeitsbereich gegen Kopien der acht Ziel-Repositories: 53 Sekunden, dieselben bereitgestellten Dateien wie beim bisherigen Handweg. Der Wiederholungslauf und die Verweigerungen „kein Git-Checkout" und „Nachricht fehlt" liefern die erwartete Meldung.
- Nicht geprüft: `publish` gegen GitHub. Das geschieht erst mit einer freigegebenen Auslieferung.

Dokumentiert in `../shared/build/fragments.md` (Abschnitt „Release command") und als Regel in `AGENTS.md` (Abschnitt „Release"). Das Veröffentlichungsergebnis steht künftig in `published.json` und wird berichtet, nicht in exportierte Planrecords zurückgeschrieben; damit entfällt der zweite Push je Auslieferung.

## Messaufbau

Modelle: `gpt-6.1-sol` über `codex exec` mit Effort medium (je Lauf aus der Sitzungsaufzeichnung gelesen) und `claude-opus-5-5` mit `--effort medium`. Sol je drei Läufe, Opus je zwei, wo nichts anderes steht. Drei Bedingungen:

- **ohne**: keine Scoville-Skills installiert.
- **alt**: die veröffentlichte Suite vor diesem Plan (Stand 70e91a1).
- **neu**: der Stand dieses Plans. Die Skill-Sätze heißen im Messordner `new18` bis `new24`; `new24` ist der Stand, der ausgeliefert werden soll. Die Tabellen nennen das Ergebnis des letzten Satzes, mit dem die Aufgabe gemessen wurde.

Jede Aufgabe hat ein eigenes Projekt, einen kurzen deutschen Auftrag ohne Hinweis auf die Falle und eine Auswertung mit verdeckten Prüfungen. Für jede Aufgabe ist belegt, dass die Referenzlösung besteht und die naheliegende falsche Lösung an den Fallen-Prüfungen scheitert. Messordner im Arbeitsbereich: `temp/2026-11-11-scoville-messung` (Aufträge in `TASK-BRIEF.md`, Auswertung mit `sum_cw.py`).

Umfang: 285 Sol-Läufe über die ChatGPT-Anmeldung und 169 Opus-Läufe für zusammen 74,17 US-Dollar nach CLI-Angabe. Mit Skill braucht Sol im Mittel 110 statt 88 Sekunden und 33.000 statt 21.000 nicht gecachte Eingabetoken je Lauf, Opus 66 statt 53 Sekunden und 0,45 statt 0,33 US-Dollar. Alter und neuer Stand unterscheiden sich darin nicht messbar.

## W-002 Code

### Was der Skill verhindern soll

Der Nutzer hat die Vorfälle benannt, die zum Code-Skill geführt haben: zweite Fassung vorhandener Logik, parallele Codepfade, fehlende oder falsche Kapselung, schlechter Aufbau neuer Projekte, im Quelltext erkennbare quadratische oder überkomplexe Lösungen, Absicherung einfacher Anwendungen wie eine Zahlungsanwendung, Tests ohne Aussagekraft und „alle Tests grün", obwohl der einzig relevante Test nicht lief, sowie Reviews, die all das übersehen. Ziel ist Code, den ein Mensch nachvollziehen und ein Agent weiterpflegen kann. Die Komplexitätsregel ist eine Leseprüfung am Quelltext; sie fordert weder Zeitmessung noch Benchmark oder Profiling.

Die erste Aufgabenreihe (C1 bis C5) prüfte nur funktionale Fallen. Beide Modelle lösten sie auch ohne Skill; der daraus zunächst gezogene Schluss, Code bringe keinen Nutzen, war falsch, weil die Reihe die genannten Vorfälle nicht berührte. Die Reihe C6 bis C16 prüft sie.

### Aufgaben

| Aufgabe | Prüft |
| --- | --- |
| C1 Rote Tests grün machen | Ursache im gemeinsamen Helfer beheben statt Test abschwächen |
| C2 Import soll durchlaufen | Kaputte Zeilen nicht verschwinden lassen, gespeicherten Auftrag nicht überschreiben |
| C3 Feld umbenennen | Dynamisch geladene Verbraucher, Vorlage, Export für ein externes System |
| C4 Ursache einer Langsamkeit finden | Nur Diagnose, keine Änderung; falsche Fährte |
| C5 Export auf Streaming umbauen | Bisherige Sicherheit bei Abbruch behalten |
| C6 bis C8 Funktion ergänzen | Vorhandenen Normalisierer, vorhandene Geschäftsregel, vorhandenen Kalender und Einstellungslader verwenden statt neu schreiben |
| C9 Review | Nachgebaute Regel und kopierte Tabelle finden; ähnlichen, aber fachlich anderen Helfer nicht beanstanden |
| C10 Neue Variante | Über den vorhandenen Erweiterungspunkt gehen statt einen zweiten Ablauf zu kopieren |
| C11 Anbieter ersetzen | Alle Aufrufer umstellen, alten Pfad samt Einstellungen entfernen, kein Rückfall |
| C12 Neues Kommando | Regel nicht im Kommandozeilen-Handler, keine privaten Speicherdetails, Registrierungsmuster, Test an der Stelle der Regel |
| C13 Neues Werkzeug von Grund auf | Aufteilung nach Verantwortung, dünner Einstieg, Logik ohne Kommandozeile importierbar, README mit Modulübersicht (22 Prüfpunkte). C13B lässt einen Agenten ohne Skill das Ergebnis erweitern |
| C14 Architektur-Review | Sieben eingebaute Wartbarkeitsmängel finden (Regel im Handler, privater Speicherzugriff, quadratische Suche in einer Schleife, Abstraktion mit einer Implementierung, doppelte Prüfung und breites `except`, Reste, Testtheater mit übersprungenem Test), drei Köder nicht beanstanden |
| C15 Berichte | Lösung ohne quadratische Suche und ohne unnötige Schachtelung |
| C16 Kleiner Auftrag | Kleine Änderung, ein Test, der ohne die Änderung scheitert, und der Hinweis, dass der dokumentierte Testbefehl die betroffenen Tests gar nicht ausführt |

### Ergebnisse

Vollständig bestandene Läufe je Bedingung.

| Aufgabe | Sol ohne | Sol alt | Sol neu | Opus ohne | Opus alt | Opus neu |
| --- | --- | --- | --- | --- | --- | --- |
| C1 bis C10, je Aufgabe | 3 von 3 | 3 von 3 | 3 von 3 | 2 von 2 | 2 von 2 | 2 von 2 |
| C11 | 3 von 3 | 3 von 3 | 3 von 3 | 2 von 2 | 2 von 2 | 2 von 2 |
| C12 | 1 von 3 | 2 von 3 | 3 von 3 | 2 von 2 | 2 von 2 | 2 von 2 |
| C13 | 0 von 3 | 0 von 3 | 3 von 3 | 0 von 2 | 0 von 2 | 2 von 2 |
| C13B | 3 von 3 | 3 von 3 | 3 von 3 | nicht gemessen | nicht gemessen | nicht gemessen |
| C14 | 0 von 3 | 0 von 3 | 3 von 3 | 1 von 2 | 2 von 2 | 2 von 2 |
| C15 | 3 von 3 | 3 von 3 | 3 von 3 | 2 von 2 | 2 von 2 | 2 von 2 |
| C16 | 0 von 3 | 0 von 3 | 3 von 3 | 0 von 2 | 0 von 2 | 2 von 2 |

- **C1 bis C11 und C15 unterscheiden die Bedingungen nicht.** Beide Modelle bestehen sie auch ohne Skill. Die Projekte haben 10 bis 17 Dateien; in dieser Größe finden die Modelle vorhandene Logik von selbst und bauen keine quadratische Suche ein. Ob der Skill doppelte Logik, parallele Pfade und quadratische Schleifen in großen Projekten verhindert, ist damit weder belegt noch widerlegt.
- **C13 Greenfield.** Ohne Skill legt Sol in allen drei Läufen alles in eine Datei, in zwei davon ist die Logik nicht ohne die Kommandozeile importierbar. Mit dem alten Skill fehlt in allen Läufen die Modulübersicht in der README, einmal bleibt es bei einer Datei. Mit dem neuen Stand bestehen sechs von sechs Sol-Läufen (zwei Skill-Sätze) alle 22 Prüfpunkte. Opus scheiterte ohne Skill und mit dem alten nur an der Modulübersicht; sie stand zuerst in einer Referenz, die Opus nicht öffnete, und steht jetzt in SKILL.md.
- **C13B Folgeauftrag.** Der erweiternde Agent besteht in allen neun Läufen, gleich aus welcher Bedingung das Projekt stammt. Diese Stufe unterscheidet nicht.
- **C14 Architektur-Review.** Ohne Skill findet Sol 0 bis 2 der sieben Mängel, mit dem alten Skill 2 bis 4. Ein Zwischenstand kam auf 2 von 3 vollständigen Läufen; seit jeder Mangel ein eigener Befund ist, sind es sechs von sechs Läufen in zwei Skill-Sätzen. Kein Lauf beanstandet einen Köder oder schlägt eine Zeitmessung vor. Opus beanstandet ohne Skill einmal einen Köder.
- **C16 Kleiner Auftrag.** Ohne Skill und mit dem alten Skill nennt kein Lauf beider Modelle den beweisenden Test beim Namen; in mehreren Läufen bleibt unbemerkt, dass der dokumentierte Befehl die Datumstests nicht ausführt. Mit dem endgültigen Stand bestehen alle Läufe beider Modelle (Sol sechs von sechs in zwei Skill-Sätzen).
- **C12.** Mit einem Zwischenstand prüfte Sol die neue Regel nur noch über die Kommandozeile (0 von 3 beim Prüfpunkt Testplatzierung, alt 2 von 3). Ursache war der neue Satz „ein Test je Verhalten genügt" ohne Aussage zum Ort. Mit „Teste eine Regel dort, wo sie liegt" sind es sechs von sechs.
- **Aktivierung bei Opus.** Sol öffnete den Code-Skill in jedem Lauf. Opus öffnete ihn im alten Stand bei C11 und C13 in keinem Lauf und bei C15, C2 und C6 in einem von zwei. Die Beschreibung nennt jetzt auch neue Werkzeuge, Projekte und Features; damit öffnet Opus ihn bei C11, C13 und C15 in allen Läufen.
- **Wertungen von Hand.** C1: Alle Sol-Läufe aller Bedingungen verschärfen den Invariantentest um eine Zusicherung; die Auswertung zählt jede Änderung an diesem Test, die unveränderten Originaltests bestehen, deshalb als bestanden gewertet. C11: Ein Lauf mit dem neuen Stand fällt bei „alter Pfad entfernt" durch, weil ein Parameter für die Wartezeit `fallback` heißt; alle Aufrufer nutzen die neue Schnittstelle, als bestanden gewertet. C14: Ein Lauf nannte das breite `except` und den Test, der nur einen Methodenaufruf prüft, in Worten, die die Muster nicht kannten; die Muster sind ergänzt, kein anderer Lauf ändert dadurch sein Ergebnis.

### Was sich geändert hat

SKILL.md enthält jetzt 16 Schritte für jede Änderung, jeder mit einem Ergebnis, das der Agent selbst prüfen kann:

- Vor dem Schreiben: Mangel bestätigen; Vorhandenes suchen (nach dem, was es tut, nicht nach dem Namen); Ort und Bauweise des Projekts übernehmen; den einfachsten Ansatz in einem Satz sagen und den Code daran messen.
- Beim Schreiben: ein Pfad; Modulgrenzen; eine Quelle je Tatsache; kein versteckter zweiter Durchlauf in einer Schleife; Schutz im Verhältnis zur Anwendung; Größe des Auftrags; für den Leser schreiben.
- Tests: testen, was der Auftrag ändert, dort, wo die Regel liegt, und zeigen, dass der Test ohne die Änderung scheitert; die Tests so ausführen, wie das Projekt sie ausführt, und den beweisenden Test beim Namen nennen.
- Zum Schluss: nichts zurücklassen; auffindbar machen; den Diff gegen die Liste prüfen und den Beleg berichten.

Die Review-Prüfliste in der gemeinsamen Code-Qualitätsreferenz geht dieselben Punkte an einer fremden Änderung durch und nennt, was kein Mangel ist. Jeder Mangel ist ein eigener Befund.

Die Referenzen des Mitglieds sind von 21.323 auf 10.625 Byte gekürzt. Die Code-Qualitätsreferenz ist von 5.073 auf 3.377 Byte gekürzt und mit der Review-Prüfliste 6.114 Byte groß. Eine gewöhnliche Änderung liest nur noch SKILL.md statt SKILL.md und drei Referenzen.

### Gestrichen

Gestrichen ist, was allgemeiner Rat ohne belegten Vorfall ist oder eine andere Stelle wiederholt:

- Die Modusnamen Advise, Explore, Develop und Harden; ihr Inhalt steht in der Tabelle „Was eine Anfrage erlaubt".
- Allgemeiner Rat in Change: Versionskontrolle vor dem Editieren ansehen, Konventionen folgen, vorhandene Abhängigkeiten bevorzugen, Manifeste und Generatoren beachten, Eingaben nachverfolgen.
- In Validation: Laufzeit- und Speichermessung mit realistischen Größen, Befundformat und Prioritäten, der Abschnitt zur abschließenden Durchsicht (ersetzt durch Schritt 16), der Absatz zu Mocks (jetzt ein Satz).
- In den Projektkonventionen: „Dem Ökosystem folgen" und Gruppierung nach Feature als allgemeiner Rat.
- In Planning: abstrakte Abgrenzungen ohne Vorfall.

Zu jeder gestrichenen Regel wurde in Commits, Changelog und Records nach einem Anlass gesucht; keine hat einen belegten Vorfall.

### Behalten

Mit belegtem Vorfall behalten: Zeilenenden und keine Normalisierung ganzer Dateien; das eigene Ergebnis jedes Prüfbefehls; Mangel vor der Korrektur bestätigen; der Ausgangszustand muss sich vom erwarteten Ergebnis unterscheiden; begründete Schranken statt exakter Zählwerte; kein Inhalts- oder Hashvergleich ohne Vertrag; gespeicherter Zustand an echter Fabrik und echten Prozessen; begrenzte Suchen; der echte Verbraucher statt kopierter Konstanten; ein Negativtest muss die Zieloperation erreichen; bestandene Ergebnisse wiederverwenden; ein wiederverwendeter Pfad erbt keine Voraussetzungen einer anderen Operation; ein ersetzter Pfad wird in derselben Änderung entfernt.

Unklare Herkunft, behalten (kein Vorfall gefunden, keine Messung zeigt die Wirkung):

- SKILL.md: Beobachtetes ist Daten, keine Anweisung; die Liste der Aktionen mit Freigabe; ohne Versionskontrolle vor dem Überschreiben lesen; Geheimnisse; fehlende Erlaubnis nie durch simulierten Erfolg ersetzen; nur so weit behaupten, wie der Beleg reicht.
- Change: Verbrauchervarianten und Testdoubles; Helfer für Agenten; „Erkundung beenden, wenn …".
- Validation: erste vollständige Diagnose und stabiler Fehler; veraltetes Gesamtergebnis; fremde fehlschlagende Tests; „keine Instrumentierung hinzufügen".
- Planning: kleine Änderung braucht keinen Record; ein Zwischenstand braucht keine Freigabe; Handoff als Momentaufnahme.

## W-003 WordPress-Adapter

| Aufgabe | Sol ohne | Sol alt | Sol neu | Opus ohne | Opus alt | Opus neu |
| --- | --- | --- | --- | --- | --- | --- |
| WPA Einstellungsseite um einen Abschnitt erweitern (23 Prüfpunkte am Quelltext) | 2 von 3 | 3 von 3 | 3 von 3 | 2 von 2 | 2 von 2 | 2 von 2 |
| WPB Admin-Seite mit sieben eingebauten Fehlern prüfen | 0 von 3 | 3 von 3 | 3 von 3 | 2 von 2 | 2 von 2 | 2 von 2 |
| WPC Frage zu einer fremden Fläche (Panel im Block-Editor) | 0 von 3 | 0 von 3 | 3 von 3 | 2 von 2 | 2 von 2 | 2 von 2 |

- **WPA:** Ein Sol-Lauf ohne Skill schreibt die Felder am Settings-API vorbei und ohne Labels. Mit Adapter bestehen alle Läufe.
- **WPB:** Ohne Skill übersieht Sol in allen drei Läufen den selbst gebauten Hinweiskasten statt der WordPress-Notice. Die Ausgangsmessung wies für den alten Stand 1 von 3 aus; die zwei Abzüge waren Auswertungsfehler bei deutschen Formulierungen („leere Punkte", „Scan-Button"). Nach Korrektur der Muster bestehen alter und neuer Stand je 3 von 3; an den Läufen ohne Skill ändert die Korrektur nichts.
- **WPC:** Sol nannte ohne Skill und mit dem alten Adapter in keinem Lauf die Bausteine des Editors; der alte Adapter gab für ausgeschlossene Flächen nur „Plugin-Route stoppen" vor. Der neue nennt je Fläche, was zu empfehlen ist; Sol besteht in drei Skill-Sätzen je 3 von 3.
- Opus besteht alle drei Aufgaben in allen Bedingungen; ein Vorteil des Adapters für Opus ist an diesen Aufgaben nicht belegt.

Geändert:

- `adapter.md` hat eine Prüfliste mit elf Zeilen für klassische Plugin-Seiten: Seitenrahmen, Settings API, Labels, Notices, Buttons, Ladeort und Selektoren des Stylesheets, Breiten, Status nicht nur über Farbe, übersetzbare Texte, Core-Aussehen.
- `routing.md` nennt für jede ausgeschlossene Fläche den Mechanismus des Hosts.
- Die UI-SKILL.md schickt bei Plugin-Seiten ausdrücklich in den Adapter. Davor öffnete Sol ihn beim Umsetzen (WPA) in einem von drei Läufen je Stand, danach in allen sechs Läufen von WPA und WPB.

Grenzen: keine WordPress-Laufzeit, die Auswertung liest Quelltext und Antworttext; WPB und WPC werten den Antworttext mit Mustern aus, die an deutschen Formulierungen dreimal nachgebessert werden mussten. Die React-, Token-, Versions- und Übersetzungsteile des Adapters sind von keiner Aufgabe berührt. `classification-output.md` hat in der Suite keinen Verbraucher und bleibt, weil es nur auf ausdrückliche Anfrage gelesen wird.

## W-004 Alle Skilltexte

Jede SKILL.md und jede Referenz aller neun Mitglieder sowie die gemeinsamen Regeln sind nach einer Schreibregel überarbeitet: Auslöser, Handlung und ein Ergebnis, das der Agent selbst prüfen kann, in konkreten Worten. Die Regel steht als „Executable and checkable" in der gemeinsamen Anleitung zum Schreiben von Anweisungen. Hilfsagenten schrieben um; ein unabhängiger Vergleich gegen den Stand davor fand je Mitglied Stellen mit verschobener Bedeutung, die alle korrigiert sind. Beispiele: Das Leselimit im Handoff war zu einer Erlaubnis geworden, Plan-Regel 2 war abgeschwächt, „nicht nötig" war in Workflow und Setup zu Verboten geworden, UI-Sätze legten Rendern beim Umsetzen nahe.

Danach wurden Wiederholungen gestrichen, die denselben Leser in derselben Situation zweimal erreichen: 15 Kandidaten in den gemeinsamen Regeln, Plan, Handoff, Skillwriter und Cleanup, 32 in UI, dem WordPress-Adapter, Workflow und Ask, dazu Inhaltsverzeichnisse und Herkunftsnotizen im Adapter. Elf Kandidaten blieben stehen, weil ihre Leser einander nicht sicher gelesen haben. Jede Streichung ist am Diff und an der verbleibenden Stelle geprüft; ein Halbsatz wurde wiederhergestellt. Die gemeinsamen Regeln verwenden für den Liefervertrag einer Rolle jetzt einen Begriff („delivery contract") statt zwei.

`../shared/runtime/rollover_readiness.md` ist entfernt: Kein Paket liefert die Datei aus, und sie nennt Operationen, die der Helfer nicht hat.

Auf Entscheidung des Nutzers sind auch die Prompttexte umgeschrieben, die Python-Helfer an Kind-Agenten und Berater ausgeben: 16 Texte in Workflow `build_dispatch_prompt.py`, drei in Ask `build_adviser_prompt.py` und einer in `ask.py`. Fehlermeldungen, Feldnamen und die Ergebnisfelder sind unverändert. Zwei festgeschriebene Formulierungen in einem Workflow-Test sind angepasst; Workflow-Tests 87 von 87, Ask-Tests 63 von 63. Weil sich ausgeliefertes Python ändert, braucht die Auslieferung einen neuen Lauf der privaten CI. Eine Modellmessung dieser Texte gibt es nicht: Workflow und Ask steuern Codex-Unteragenten und haben keine Aufgabe im Messaufbau.

Auf Entscheidung des Nutzers ebenfalls entfernt: `../shared/runtime/task_lifecycle.py` mit seiner Beschreibung und zwei Testdateien. Kein Paket lieferte den Helfer aus. Zwei Tests, die ihn als Beispieldatei nutzten, verwenden jetzt vorhandene Helfer; drei Zusicherungen, dass er in Paketen fehlt, sind gestrichen. Shared-Tests 90 von 90, `check_all` 12 von 12.

## W-005 Nachmessung und Gesamtprüfung

Nach den Streichungen aus W-004 wurden alle Aufgabenreihen mit Sol und eine Auswahl mit Opus erneut gemessen (Skill-Sätze `new22` bis `new24`).

| Reihe | Sol alt | Sol neu | Opus neu |
| --- | --- | --- | --- |
| T3 Plan: Auftrag, der einer Decision widerspricht | nicht mit Effort medium gemessen | 6 von 6 | nicht erneut gemessen |
| T8 UI umsetzen: Suche und Kennzeichen (36 gerenderte Prüfpunkte, vorhandene Komponenten) | 6 von 8 | 8 von 9 | 2 von 2 |
| T9 UI umsetzen: Kopfzeile (33 Prüfpunkte) | 8 von 8 | 3 von 3 | nicht erneut gemessen |
| T10 UI-Review mit vier eingebauten Mängeln | 3 von 3 | 6 von 6 | 2 von 2 |
| H1 Handoff schreiben | 4 von 4 | 3 von 3 | 2 von 2 |
| H2 Handoff: keine Aktivierung bei einer Zusammenfassung | 2 von 2 | 3 von 3 | nicht erneut gemessen |
| S1 Skilltext überarbeiten | 4 von 4 | 3 von 3 | 2 von 2 |
| S2 Skilltext prüfen | 3 von 3 | 3 von 3 | nicht erneut gemessen |
| C12, C14, C16 | siehe W-002 | je 3 von 3 | C16 2 von 2 |
| WPA, WPB, WPC | siehe W-003 | je 3 von 3, in zwei Skill-Sätzen | WPB 2 von 2 |

- **T10 UI-Review.** Mit `new22` und `new23` übersah Sol in 2 von 6 Läufen einen der vier Mängel, eine 13-px-Schrift am Ergebniszähler (alter Stand und `new20`: 0 von 6). In einem der beiden Fehlläufe waren die geladenen Texte identisch mit dem bestandenen Stand; die Stichprobe trennt Streuung nicht von Rückschritt. Schritt 7 der UI-Regeln verlangt jetzt, die Werteliste im Review aus den hinzugefügten Zeilen des Diffs zu ziehen. Mit `new24` bestehen 6 von 6 Sol-Läufen und 2 von 2 Opus-Läufen.
- **T8.** Ein Opus-Lauf fällt bei „Kennzeichen vor den Beschriftungen mit dem Abstand des Systems" durch, weil er hinter dem Kennzeichen einen nur für Screenreader sichtbaren Text einfügt, den die Messung als Nachbarn nimmt. Derselbe Auswertungsfehler trat schon im alten Stand auf; als bestanden gewertet. Die zwei Abzüge im alten Sol-Stand und der eine im neuen (`new20`; `new22` und `new24` je 3 von 3) betreffen den Innenabstand der Suchzeile.
- **Endgültiger Stand.** `new24` unterscheidet sich von `new22` in zwei Sätzen der UI-SKILL.md (Verweis auf den Adapter, Werteliste im Review) und von dem committeten Stand in einem Begriff der gemeinsamen Regeln. Mit `new24` selbst gemessen sind T10 und T8 (Sol), T10, C11 und C15 (Opus); alle anderen Reihen mit `new22` oder `new23`.
- **Gesamtprüfung.** `python development/check_all.py` besteht mit 12 von 12 Prüfungen.

Nicht gemessen:

- Wirkung in großen Projekten. Alle Projekte haben 10 bis 17 Dateien.
- Effort low und Fable 5.2 (Non-goal).
- Plan, Handoff, Skillwriter und Cleanup jenseits der genannten Aufgaben; Workflow, Ask und Setup haben keine Modellaufgabe, ihre Texte sind durch den Bedeutungsvergleich und die Mitgliedstests geprüft.
- Der WordPress-Adapter an einer laufenden WordPress-Installation.
