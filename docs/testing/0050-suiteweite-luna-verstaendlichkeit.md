# PLAN-0050: Verständnis aller Suite-Skills

Ziel ist die richtige Einordnung fiktiver Aufgaben durch Luna 6/Medium. Die
Teilnehmer führen keine Fachaufträge aus. Ein Pass belegt weder korrekte reale
Implementierung noch die Beherrschung ungesehener Aufgaben.

## Design und Ausgangsstand

| Bereich | Entwicklungsaufgaben |
| --- | ---: |
| Code | 12 |
| Handoff | 8 |
| Plan | 21 |
| UI | 19 |
| Workflow | 17 |
| Ask | 9 |
| Setup | 6 |
| Cleanup | 8 |
| Gemeinsame Regeln und Fallbacks | 9 |
| Gesamt | 109 |

Die Anzahl folgt unterscheidbaren Routen und Entscheidungen, keiner festen
Quote je Skill. Mehrfachsituationen haben getrennte Kriterien. Variante und
Paket werden nur dort getrennt geprüft, wo sie Verhalten ändern.

Frische Teilnehmer erhalten den Einstieg, frei wählbare Referenzen desselben
Paketbaums und erforderliche Rohfakten. Die Erwartungen bleiben getrennt.
Negative und positive Routen prüfen auch übervorsichtige Fehlinterpretationen.
Helperausgaben stammen unverändert aus isolierten Fixtures; die Claude-CLI
ist dabei eine lokale Attrappe. Kein Adviser oder Workflow wurde für diese
Fixtures gestartet. Autorenblöcke und Nachrichten sind ausdrücklich fiktiv.

Alle 320 Paketdateien des Ausgangsinputs stimmen bytegenau mit frisch aus den
kanonischen Quellen erzeugten Kandidaten überein. Der unveröffentlichte
Ausgangsstand ist vor Textkorrekturen gesichert. Laufzeit-CI-Kandidaten haben
keinen Release-Receipt; die Releaseprüfung ist auf sie nicht anwendbar.

Opus 5.5/High und Sol 6.1/Xhigh verlangten vor dem Start neutralere Fragen,
passenden Profilkontext, klare Kriterien, echte Rohausgaben und fehlende
positive Routen. Opus hat die korrigierten 109 Entwicklungsaufgaben und ihren
Dispatch abgenommen. Seine Transferprüfung war eine benannte Stichprobe,
keine vollständige Satzprüfung des Pools. Sol hat die alten Fixtures und den
Lösungshinweis korrigiert und den Pool vor Textarbeit neu eingefroren; Astra
Medium hat die danach geänderten Transferstellen geprüft. Unveränderte Fälle wurden dabei nicht erneut geprüft.
Bei verändertem Verständnis einer Helperausgabe muss der Transferfall auch
andere fiktive Rohwerte enthalten. Der Pool blieb der Textarbeit verborgen.
34 frische Luna-6/Medium-Teilnehmer haben alle 109 Entwicklungsaufgaben
beantwortet. Die vollständigen Antworten und tatsächlichen Handles sind im
temporären Bereich gesichert. Teilantworten aus Nachrichten bleiben erhalten,
wenn die finale Nachricht nur den Abschluss bestätigt. Sol hat 359 Required-
und zwei Forbidden-Merkmale ausgewertet: 96 PASS, zwölf FAIL und eine
Testdesign-Grenze. Fehlende Antworten: null.

## Befunde und Testgrenzen

| Einordnung | Fälle und Konsequenz |
| --- | --- |
| Falsche Entscheidung | H05 wiederholt einen fiktiven Secretwert in der Warnung; W13 verwechselt Child-Recovery mit Managerübernahme; K03 verlangt sämtliche Work-Item-Acceptance vor Step-Abschluss. Vorhandene Pflichten präzisieren. |
| Relevante Auslassung | H07 fehlt konkrete Template-Reparatur; P06 der sofortige Kollisionscheck; G07 die Reviewer-Inputroute; G03 höchster Wert plus eins und alle Vorschläge. U17 lässt Pflichtfelder weg und nimmt unbelegte Shell-Owner an. Vorhandenen Text präzisieren; Auslassung beweist keinen realen Ausführungsfehler. |
| Testproblem | W06 widersprüchlicher Rohfixture, separat korrigiert PASS. U13 und K05 verlangten keinen vollständigen Prüfnachweis; W10 keinen Vollrecap; W05 belegte eine angeblich fehlende Startnachricht nicht. P21 erlaubte nur Prüfung, read-only korrekt. Neutrale Zusatzfragen testen Nachweis, vollständige Startkette und ausdrücklich autorisierte Recordreparatur. |
| Transport | Fehlende MESSAGE-Ausgaben erneut vom ursprünglichen Teilnehmer geliefert, laut ihm wortgetreu; kein neuer Versuch. Verschlüsselte Originalblöcke erlauben keinen unabhängigen Bytevergleich. |
| Ausführungsselbstauskunft | Python auf Markdown, fehlendes --file, falscher Setup-Pfad und Lesen hinter last wurden berichtet. Ohne unabhängige Originalcalls bleiben Ursachen offen. Reader-Vertrag am Beispiel gruppieren; tatsächlichen Ask-Skill benennen. |

Opus lieferte wegen CLI-Sitzungslimit keine Gegenprüfung. Der Nutzer wählte
Astra Medium als Ersatz; Astra prüfte Originalbelege und Testgrenzen.
Sol 6.1/Xhigh bleibt der andere ursprüngliche Reviewer. K03 besteht die
ursprünglichen Owner-Kriterien, enthält aber die falsche zusätzliche
Step-Abschlussbedingung; beides bleibt getrennt sichtbar.

Sol bewertet die erste gezielte Runde mit 15 PASS und zwei FAIL bei 17 Fällen:
H05 wiederholt den Secretwert, H07 lässt Template-Schritte aus. Die späteren
frischen Proben redigieren vollständig und nennen vier Abschnitte sowie drei
Resume-Schritte. W13 trennt Recoveryrollen; P06 nennt im konkreten Zeitfall
den sofortigen Kollisionscheck; G03 und G07 beantworten die präzisierten
Routen. Die reparierten Nachweisfragen bestehen, ohne neue Skillpflichten.

U17 blieb auch bei klar verlangtem Objekt falsch: unbekannte Platzierung,
aber angenommene Core-Shell. V5 präzisiert die bestehende Vorrangtabelle und
kürzt die doppelte Erklärung. Die neue Antwort setzt nun `shell_owner:
unknown`, `needs-clarification` und alle erforderlichen Verbote richtig;
Sol und Astra bewerten sie PASS. Frühere FAILs bleiben bestehen. Eine
U16-Variante nennt nur allgemein Eingabemethoden, eine andere explizit die
Alternative ohne Drag; daraus folgt keine neue Skillregel. Die getrennten Transferproben prüfen diese Entscheidungsgrenzen zusätzlich.

## Transfer und Endstand

Sol wählte nach der Textarbeit 26 Fälle aus dem vorher eingefrorenen Pool:
zehn geänderte Entscheidungen und 16 erhaltenswerte Grenzen, je zwei pro Skill.
Frische Luna-Teilnehmer erhielten weder Kriterien noch Entwicklungsfeedback.
Das ist eine begründete Stichprobe, kein vollständiger Test der 126 Poolfälle.

Vier Teilnehmerinputs verloren bei der Zusammenstellung erforderliche Fixtures:
T-H07, T-G06, R-P10 und R-S02. Testfehler, keine Skill-FAILs. Nur diese vier
wurden mit den hashgleichen Originalfixtures frisch wiederholt; unbeeinträchtigte
Antworten blieben erhalten. Der Workflowauftrag wurde schon vor Dispatch repariert.

Beide Reviewer bestätigen im gültigen ursprünglichen Transfersatz 23 PASS und
drei getrennte Grenzen:

| Fall | Grenze und gezielte Ergänzung |
| --- | --- |
| T-P06 | ID- und Reihenfolgeregeln richtig, sofortiger Kollisionscheck ausgelassen. Eine neue neutrale Zeitfrage wird frisch beantwortet: aktuellen Plan lesen, ID unmittelbar vor Anlage als Maximum plus eins bestimmen und erneut Kollisionen prüfen. Kein belegter gegenteiliger Timingentscheid. |
| T-G06 | 750, Neustart bei Teil 1 und Leseabfolge richtig; verlangter konkreter Aufruf fehlt. Derselbe Teilnehmer ergänzt den PowerShellblock und nach neutraler API-Formatpräzisierung das vollständige JSONobjekt. JSON, literales `$value`, Leser-/Toollimit 750, Teil 1 und Wrappererhalt statisch geprüft; der fiktive Befehl wurde nicht ausgeführt. |
| T-U17 | Erfindet Settings-/Tooltyp. Die Beschreibung des vorhandenen allgemeinen Surfacewerts vermischt Kategorie und Runtime. Ein Wort korrigiert die bestehende Zeile zu `unspecified category`; keine neuen Enumwerte oder Regeln. Drei frische Fälle unterscheiden allgemeine Pluginseite, unbekannte Platzierung und ausdrücklich belegte Settingsseite korrekt. |

Ergänzungen schließen die benannten Entscheidungen und Nachweislücken; sie
machen die ursprünglichen Transferantworten nicht rückwirkend vollständig.
Frühere FAILs, Testfehler und Auslassungen bleiben sichtbar. Sol 6.1/Xhigh (`ask_sol0047_consensus`) und Astra Medium
(`ask_astra0050_boundaries`) nehmen V6 und die Ergänzungen ab. Die finalen
kritischen Entscheidungen sind belegt; keine verpflichtenden Findings offen.

Zehn kanonische Markdownquellen sind geändert, erforderliche Verbraucher
neu erzeugt. V6 enthält netto 154 LF-Zeichen mehr; Handoff wird um 144,
Plan-Edit um 39 Zeichen kürzer. Die gezielte Rollen- und Ownershippräzision
belegt keine allgemeine Textverkürzung. Keine Runtime-Pythonänderung.

Je vier relevante Checks bestehen unter Windows und Linux: gemeinsame
Writing-Verbraucher, kanonische Regelprojektion, Mitgliedschaft/Fallbacks und
wiederholbare Generierung in vier Profilen sowie dokumentierte Helperargumente.
Diese V5-Ergebnisse gelten weiter: V6 ändert ausschließlich ein Wort der
UI-Kategoriebeschreibung. Alle 320 Dateien in vier V6-Profilen wurden neu
erzeugt und ihre bytegleiche Übertragung geprüft. Keine pauschale Wiederholung
unveränderter Pythonprogramme.

Die kritischen Entscheidungen sind durch Entwicklungs-, frische Korrektur-
und Transferfälle belegt. Das beweist weder robuste reale Ausführung noch
Verständnis jeder ungesehenen Aufgabe. Modell/Effort wurden angefordert;
unabhängige tatsächliche Modelltelemetrie wird vom Host nicht ausgewiesen.

## Korrekturmaßstab

1. Testprobleme, falsches Verständnis, unvollständige Antworten und
   Transportfehler unterscheiden. Testprobleme zuerst getrennt korrigieren
   und erneut prüfen; unverlangte Vollrecaps sind kein Skillfehler.
2. Vorrangig vorhandenen Text kürzer und eindeutiger formulieren, strukturieren
   oder Dopplungen entfernen; Verhalten und Schutzwirkung erhalten.
3. Jede neue Regel oder nötige Erweiterung mit einer konkreten fehlenden
   Verhaltens- oder Absicherungslücke begründen.
4. Fehlerentscheidung und erhaltene richtige Grenzen mit frischen Fällen
   prüfen; Endabnahme durch die ursprünglichen Reviewer und getrennte
   Transferfälle. Frühere Fehlschläge nicht nachträglich grün rechnen.

Nur technisch betroffene Checks werden unter Windows und Linux ausgeführt.
Raw-Testbank, Kriterien, Quellenstand und vollständige Antworten liegen im
temporären Bereich `temp/2026-10-09-suite-luna-verstaendlichkeit/`;
Teilnehmerinputs getrennt in `temp/2026-10-09-luna0050-inputs/`.
