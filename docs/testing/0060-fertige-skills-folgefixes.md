# PLAN-0060: Folgefixes der ausgelieferten Skills

## Ergebnis und Umfang

- Kanonische Owner: Suite `members/`, Shared `prompting/`, `runtime/` und
  `runtime-tests/`. Profile und Pakete werden daraus gebaut.
- Quellenreview: frischer `gpt-6.1-sol / low`, anschließend gezielte Nachprüfung
  seiner zwei korrigierten Befunde; keine erneute Gesamtprüfung unveränderter Texte.
- Veröffentlichung und lokale Aktualisierung sind vom Nutzer nach bestandenen
  Prüfungen beauftragt. Keine Tags, Releases oder erneute Historienänderung.
- PLAN-0059 ist auf ausdrückliche Nutzerentscheidung abgebrochen; die
  Support-Nachverfolgung endet ohne behauptete vollständige Altobjektentfernung.

## Korrekturen und technische Nachweise

| Umfang | Korrektur und beobachteter Nachweis |
| --- | --- |
| Plan | Gemeinsame Abschnittsgrenzen statt Leerzeilenabhängigkeit; Unterüberschriften im Goal bleiben erhalten, unzugeordnete Einleitungen werden diagnostiziert. Fünf Ausgangsabweichungen reproduziert. 128 Plan-Tests, davon ein bestehender POSIX-Skip unter Windows; nachträglicher Leerraum-Gegenfall rot/grün geprüft. |
| Diagnosen und IDs | Parsefehler erzeugen keine falsche Idle-Diagnose. Selectorfehler nennen Stelle und Korrektur. Next-ID blendet falsch benannte Markdown-Records nicht aus. |
| Dispatch | Verlinkter Workspace-Vorfahr funktioniert; Root selbst als Link und verlinkte Recorddateien bleiben gesperrt. 85 Workflow-Tests bestanden. Einfache Eingabefehler werden früh geprüft; angebotene Optionen sind dokumentiert. |
| Capture | EOF statt geerbtem stdin. Expliziter positiver Timeout ohne Standarddeadline. Originalbytes und Status bleiben bei Encodingfehlern bzw. Timeout gespeichert; unbestätigtes Cleanup ist ein Fehler, kein Erfolg. Inkrementelle Reader verhindern den Windows-Lock beim Schließen blockierter Pipes. |
| Capture-Gegenfälle | Historischer Helper übernimmt Eingabebytes und verliert ungültige UTF-8-Ausgabe trotz Speicherauftrag. Erster Timeout-Fix hängt beim beendeten Elternprozess mit weiterlebendem Pipe-Kind am äußeren 20-Sekunden-Limit. Korrigierter Stand besteht lokal mit 26 Runtime-Tests. |
| Plattformen | Finale private [Runtime-Matrix](https://github.com/benjaminstelzer/scoville-runtime-ci/actions/runs/40955452986): Windows, Linux und macOS jeweils Python 3.11 und 3.x, alle sechs Jobs bestanden. Die obsolete zusätzliche 3.10-Stufe entfällt; die erforderlichen Tests laufen in der gültigen Matrix. |
| Native Vorlage | Auf dem Windows-Codex-Host tatsächlicher Erfolg, Exit 7 und Pending mit anschließendem Abschluss geprüft. Ein begrenzter nativer Aufruf pro äußerem Aufruf; laufendes Handle und ursprüngliche Chunks bleiben erhalten. |
| Ask | Caller-Literalschutz steht vor dem Framing in SKILL.md; Adviser-Antwortschutz liegt in der gemeinsamen Adviser-Quelle. Native Aufträge verweisen auf Writing und bei Reviews auf Code-Review, statt diese Texte einzubetten. 55 Ask-Tests bestanden, einschließlich Claude-Transport mit CLI-Platzhalter. |
| Ask-Umfang | Gemessene Startnachricht: Consultation 9840 → 5127, Review 11872 → 5294 UTF-8-Bytes im gleichen Vergleichsaufbau. Das ist keine Messung der gesamten Modellkosten; notwendige Referenzlektüre bleibt erforderlich. Sol-Default ist gpt-6.1-sol/high, bestehende Overrides bleiben erhalten. |
| Wiederholung | Workflow- und UI-Diagramme unterscheiden unterstützte nächste Korrektur von Stillstand. Offene Befunde bleiben offen; kein Zähler und kein erfundener Review-Pass. |
| UI | Windows Edge mit klassischer Scrollbar: innerWidth 800, clientWidth 785, scrollWidth 792. Alter Vergleich übersieht Überlauf, clientWidth erkennt ihn; erlaubter lokaler Scrollcontainer besteht. |
| Fallbacks/Setup | Idle-Fehler und Evidence: [] stimmen mit den Helpern überein; temporäre .gitignore und Fehlerbytes sind berücksichtigt. Setup nennt den ungültigen Skalarwert und hält verschachtelte sensible Inhalte zurück. 20 Setup-Tests bestanden. |
| Profile | General-Plantext ist von Workflow-Bindung befreit; Mainloop-Code behält die Nutzerentscheidung bei gleichrangigen Regelkonflikten. Neue ADR-Markierung bleibt erhalten. Fehlende optionale Setup-Metadaten allein sind kein Defekt; notwendige Paket- und Wiederaufnahmekontexte bleiben bestehen. |

## Tatsächliche Empfänger

Alle fünf frischen Agenten wurden mit `gpt-6.1-sol / low` gestartet; die
lokalen Turn-Metadaten bestätigen dieses Paar, auch für die gezielte
Quellenreview-Fortsetzung. Originale Helper-Ausgaben wurden ohne Promptreparatur
dispatcht; die Agenten benötigten keine Rückfrage.

| Ausgabe/Fall | Beobachtetes Ergebnis |
| --- | --- |
| Dispatch-Reviewer | Findet den absichtlich eingebauten `sum(set(prices))`-Defekt und die grüne Assertion, die wiederholte Preise nicht absichert. Vollständiger scoped Diff und Verbraucher geprüft; keine Tests oder Änderungen. |
| Dispatch-Explorer | Identifiziert Owner, Verbraucher und dieselbe Vertragsverletzung; bleibt lesend und behauptet keine Abnahme. |
| Native Ask / Capture / Complete-File | Wertet 513043 Bytes Berichtsdaten vollständig aus: 3370 Records, 25 Fehler, Summe 37004. Liest alle 850 Vertragsklauseln einschließlich zunächst gekürzter und gezielt nachgelesener Passage. Erhält RESULT_A/B und die Endbedingung. Unterscheidet vollständige Bytes, Producer-Exit 7 und ungültiges UTF-8 korrekt. |
| Korrekturfälle | Erlaubt einen belegten weiteren Ansatz nach zwei unterschiedlichen Fehlversuchen; stoppt denselben unverändert wiederkehrenden Befund ohne nächsten Ansatz. Erhält frische Pflichtreviews und gültige bestehende Nachweise. Dies ist eine Fallbewertung, kein kompletter Workflow-Lauf. |
| Native Ask-Review | Prüft die geänderten Quellen und betroffenen Consumer. Findet Windows-Pipe-Cleanup und Leerraum vor H1; beide Fälle werden vor der Korrektur reproduziert und anschließend gezielt ohne weiteren Befund abgenommen. |

## Echter Workflow im isolierten Testprojekt

Hauptchat, Explorer und Reviewer liefen tatsächlich mit `gpt-6.1-sol / low`;
native Sitzungsdaten bestätigen die gestarteten Paare. Kandidatenpakete wurden
im eigenen Hauptchat mit lokalem Git verwendet, ohne Installation oder Remote.

| Fall | Beobachtetes Ergebnis |
| --- | --- |
| PLAN-9001, regulärer Ablauf | Zwei Implementierungssteps mit sechs fachlichen Tests, frischen Step-Reviews und unabhängiger Closure abgeschlossen. Die Assertions decken Mengen, wiederholte Preise und den Belegverbraucher ab. Akzeptierte Stepstände und Abschluss wurden tatsächlich committet. |
| PLAN-9002, Bericht | Alle 6000 Records eines 1179820-Byte-Berichts geprüft. Unabhängige Driverauswertung bestätigt Soll 1724733, Ist 1724729 sowie Abweichungen bei IDs 1777 und 4172. Erforderlicher Klartextvertrag vollständig gelesen; keine Rohdatenausgabe. Der schreibfreie Step erhielt keinen erfundenen Step-Pass; Closure bestand. |
| Zwischenfrage im aktiven Step | Hauptchat beantwortet die tatsächliche Statusfrage knapp und setzt den ursprünglichen Step fort. Keine zweite Implementierung oder neue Schreibbefugnis. |
| Explorer während Review | Reviewer 7 lief von 22:13:52 bis 22:14:52 UTC; die unabhängige Frage wurde um 22:14:03 zugestellt, der frische Explorer 4 startete um 22:14:33. Hauptchat behält Reviewer und Originalscope, wahrt Quellenruhe und setzt denselben Step fort. Die thematisch passende frühere Folgefrage verwendete dagegen denselben abgeschlossenen Explorer 2. |
| Fehlende Eingabe und Einmaleffekt | Fehlender Driverbeleg hält Step 2 mit INPUT-RELEASE offen. Nach tatsächlicher Lieferung wird derselbe Step fortgesetzt; Effektzähler bleibt 1, Emission bleibt erhalten. Frische Step-Reviews und vollständige W-002-Closure bestanden; akzeptierte Änderungen sind committet. PLAN-9001-Produktdateien blieben unverändert. |

Die erste zeitliche Zustellung verpasste das aktive Review. Zudem verlangte die
Fixture den erst während eines Reviews möglichen Beleg bereits vor diesem
Review. Der tatsächliche blocked-Befund blieb erhalten; nur diese zirkuläre
Step-Prüfvoraussetzung wurde repariert, Outcome und Work-Item-Acceptance blieben
unverändert. Der Einmaleffekt wurde dafür nicht wiederholt. Die spätere reale
Überlappung und ihre unabhängige Closure sind davon getrennte Nachweise.

Die zusätzliche kontrollierte Negativprobe in PLAN-9002/W-003 bleibt offen:
Der echte Dispatcher bettet die im Testplan genannte erwartete Bewertung und
Testregie ein und liefert ein reguläres Step-Review, keine neutrale separate
Komponentenprobe. Der Hauptchat stoppt deshalb vor Spawn und Korrektur mit
CONTRACT-NEUTRALITY. Kein gewünschtes Final wurde erfunden oder durch Wiederholen
erzwungen. PLAN-9002 ist insgesamt nicht abgeschlossen; die bestandenen W-001/
W-002-Kriterien und der abgeschlossene reguläre PLAN-9001 bleiben davon getrennt.

## Grenzen

Auslieferung: Vier Paketvarianten bestehen Struktur- und Veröffentlichungsgates;
beide öffentlichen Planprofile sind gültig. `check_all.py` besteht mit zwölf
Prüfgruppen, null Fehlern und zwei leeren Python-Testpfaden (Code/Handoff;
Modellfälle separat). Acht öffentliche Repositories wurden ausschließlich auf
main gepusht und gegen ihre Remote-HEADs geprüft. 23 vorhandene lokale
Skillverzeichnisse wurden aus den passenden Paketen aktualisiert: neun unter
`.agents`, acht unter `.codex` und sechs für Claude. Inventar, Dateigröße und
erhaltene Änderungszeit sind geprüft; ein Reload bereits laufender Chats ist
damit nicht nachgewiesen.

- Verschlüsselte native Nachrichten verhindern den unabhängigen Bytevergleich
  der übertragenen Nachrichten im Hosttrace. Verlustfreie Builder-Verträge und
  unveränderte Frageübergabe sind technisch geprüft; funktionale Empfängeraktionen
  sind beobachtet. Kein pauschaler Nachweis vollständiger Modellregelbefolgung.
- Beim Langtext wählte der Datenberater ein größeres inneres Ausgabelimit als
  das äußere; die Kürzung wurde vor abhängiger Arbeit vollständig nachgelesen.
  Damit bleibt eine Abweichung bei der Transportnutzung dokumentiert; daraus
  wird keine weitere Quellursache oder neue Pflichtprüfung abgeleitet.
- Native POSIX-Codex-Ausführung bleibt ungeprüft. Python-CI ist dafür kein Ersatz.
- Claude: nur aufzeichnender CLI-Platzhalter ab ersetzter Befehlsauflösung;
  PATH-Suche, .ps1-Behandlung und Modellverhalten bleiben nach ADR-0227 ungeprüft.
- Diese isolierten Fälle belegen weder allgemeine Zuverlässigkeit noch eine
  Erfolgsquote, globale Tokenersparnis oder vollständige Produktlaufabnahme.
