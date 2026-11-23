# Goodhart-Korrekturen nach dem Opus-Review

Bericht zu [PLAN-0067](../plans/0067-goodhart-korrekturen-nach-dem-opus-review.md). Er dokumentiert Befunde, Korrekturen und Prüfgrenzen zu W-001, W-003 und W-005.

## v76 · Die Arbeitsgrenze vor dem Entwurf prüfen

Die gemeinsame Regel 7 prüft vor der Entwurfswahl, welche Eingaben
gemeinsam wachsen und wie viel die einzelnen Aufrufe über den gesamten
Pfad verarbeiten. Als Nachweis dient ein geeigneter vorhandener
Projektcheck oder die entscheidende Aufrufzahl und Eingabegröße im
Quelltext. Gemeinsame Verarbeitung erhält das Fehlerverhalten je Ergebnis.
Shared 4d005d6 und Suite 550cfc3 binden den Stand. Die vier Paketvarianten,
101 Shared- und 13 Buildtests bestehen.

R2 verwendet den WordPress-Graphfall mit den beiden gültigen Kontrollen
und prüft frisch gelesene Daten, Arbeit und Speicher. R15 verwendet die
unabhängig erstellte Änderung im bestehenden Viewer mit neuen Kontrollen
für diese Ausführungsbedingungen. Der unveränderte Browserprüfer
reproduziert die acht Referenzentscheidungen im Ausgangsprodukt.
Zusätzlich werden die Zugriffe auf die Kartenlisten gezählt.

In R2 bestehen beide Modelle in beiden Armen 37/37 einschließlich
frisch gelesener Zeilen und getrennter Lesefehler. Bei konstanter
Ausgabebreite und vierfacher Anfragezahl wächst die gezählte Arbeit
auf das 3,78-Fache bei Opus und das 3,85-Fache bei Sol. v72 lag in
dieser Probe beim 14,77- beziehungsweise 12,06-Fachen.

Opus v76 senkt den Zusatzpeak beim verzweigten Einzelabruf auf
rund 3,22 MB. Bei zwei Abrufen ist die Speicherspitze weiterhin
überlinear. Der zweite Abruf hält bei 768 Stufen mindestens 295.296
Zwischenzuordnungen für 1.536 verlangte Zuordnungen. Die gesonderte
Instrumentierung belegt vollständige Mengen jeder Größe von 1 bis
768 am Speicherpunkt der Komponentenzusammenfassung. Sol v76
erreicht in derselben Probe rund 3,96 MB Zusatzpeak.

R15 wird getrennt ausgewertet. Eingaben, Rohwerte, Zusatzproben und
Astra-Gegenprüfung liegen im Evaluationsbestand v76-work-bound.

## v75 · Zuordnung vor dem Öffnen der Skills

Die Code-Beschreibung ordnet reine Oberflächenarbeit dem
aktiven UI-Skill zu. Der Paketvergleich von Suite acc714c
bestätigt die einzelne Metadatenänderung. Vier Varianten,
13 Build- und zwei Profiltests bestehen.

Sol öffnet in der WordPress-Beitragsliste den Code-Einstieg
kein Mal. In v73 und v74 waren es je zwei Öffnungen. Der
Lauf benutzt weiterhin Code- und UI-Referenzen. Die zwei
R14-Produkte erreichen 10/10, lineare Arbeit und jeweils
286/286 Chrome-Prüfungen. Der Kandidat benötigt 406,83 statt
251,44 Sekunden und 84.466 statt 69.701 Tokens ohne Cache-Lesen.
Die Wirkung ist für die Eingangswahl in diesem Paar beobachtet.
Die gesamten Kosten bleiben höher. Der Opus-Befund stammt
weiter aus v74. Nachweise liegen in v75-skill-routing.

## v74 · WordPress-Controller über UI

Der UI-Einstieg verweist bei wiederholten Oberflächen-Updates
direkt auf die Gesamtarbeit des Aufrufpfads. Er überlässt bei
reiner Oberfläche die Führung den UI- und Projektprüfungen.
Suite 1c50373 ändert nur den UI-Einstieg in drei Paketvarianten.
Code, WordPress-Referenzen und Runtime-Eingaben sind bytegleich.

Die vier R14-Aufzeichnungen sind gültig und bestehen jeweils
286/286 Chrome-Prüfungen. Sol erreicht mit und ohne 10/10,
Opus mit und ohne 8/10. Opus scannt weiter alle Zeilen je
Modul. Bei 16, 48 und 144 Zeilen misst der Kandidat 228,
1.068 und 6.660 Operationen, die Kontrolle 220, 1.044 und
6.588. Sol bleibt linear und liest Code erneut zweimal.

Sol benötigt mit Skill 261,05 statt 251,44 Sekunden und 105.615
statt 69.701 Tokens ohne Cache-Lesen. Opus benötigt 388,21
statt 262,27 Sekunden und 195.367 statt 73.701 solcher Tokens.
Opus wählt selbst einen unabhängigen Leser. Auf ihn entfallen
95.582 zusätzliche Tokens ohne Cache-Lesen. Die bewertete
Skalierung und die mehrfachen Lesewege bleiben offen. Vergleich,
nativer Beleg und Browser-Replay liegen in v74-ui-controller-focus.

## v73 · Hinweise in Code und UI nach Bedarf

Die weitere Kürzung bündelt Routineprüfungen und die Betrachtung
des Aufrufpfads in Code. Regel 7 benennt die Arbeit in inneren
Schleifen, Rekursion, Helfern und Bibliotheken. Maßstab bleibt
die einfachste wartbare, möglichst lineare Implementierung
unter dem unveränderten Vertrag. Die UI-Referenzen sind nach
Thema bedingt, und eine doppelte Tabelle entfällt. Alle 16
WordPress-Referenzen bleiben in den Profilen mit UI bytegleich.

Die GUI-Aufgaben zur Beitragsliste und zum unabhängigen Viewer
erhalten den UI-Einstieg als Hauptanleitung. Der Validator
erhält Code. Dieselben Aufträge und Prüfer werden gegen sechs
gültige frühere Kontrollen ohne Skill verglichen. Auswertung
berücksichtigt die tatsächlich gelesenen Referenzen und die
Arbeit in unveränderten inneren Helfern. Die Runde bestimmt
die Gesamtwirkung des Kandidaten und seiner Zustellung.

Quellenstand 809f749 in Shared und 562ec37 in Suite. Der
Paketvergleich bestätigt vier Varianten. 101 Shared-Tests
und 33 Runtime-Tests bestehen. Ein Runtime-Test ist
übersprungen. Der Regelabgleich, die Eingabebindung und die
zwölf gültigen Aufzeichnungen liegen im lokalen Evaluationsbestand
v73-focused-code-ui.

Im WordPress-UI-Vergleich erreichen beide Sol-Produkte 10/10
und beide Opus-Produkte 8/10. Opus behält in beiden Produkten
die wiederholte Suche über alle Beitragszeilen pro Modul. Der
getrennte Browserlauf erreicht überall 286/286. Sol liest mit
Skill Code zweimal und zusätzlich die UI-Qualitätsreferenz.

Der unabhängige Viewer besteht in allen vier Produkten mit 7/7
und mit erfolgreichem Browser-Replay. Der Graphvalidator besteht
in allen vier Produkten mit 9/9 und linearer gemessener Arbeit.
Tokens ohne Cache-Lesen steigen in allen sechs Paaren. In den
drei Sol-Paaren ist die Modellzeit um 48 bis 84 Prozent höher.
Bei Opus ist sie in der Beitragsliste 41 Prozent niedriger,
im Viewer 19 und im Validator 55 Prozent höher. Diese Werte
binden einzelne Modellläufe. Die unabhängigen Aufgaben
begründen hier keine zusätzlichen Ablaufregeln.

## v72 · Kurze Kostenregel und zusätzlicher Projektcheck

Regel 7 wurde von 2.263 auf 1.321 Bytes gekürzt und in allen vier
Paketvarianten geprüft. Kumulative Arbeit und maximal gleichzeitig
gehaltener Speicher beziehen sich auf denselben normalen Aufrufer.
Shared 4c10e71 und Suite 1cd8e41 binden den Kandidaten. 101
Shared-Tests und 33 Runtime-Tests bestehen, ein Runtime-Test
wird übersprungen. Python und Runtime-Testdateien sind bytegleich.

Die zwölf Modellaufzeichnungen sind gültig. Beide Modelle erreichen
in R2 in beiden Armen 37/37 einschließlich Frische und in R19 9/9.
Bei R14 erreicht Sol mit und ohne 10/10 und Opus mit und ohne 8/10.
Der Browser prüft in jedem Produkt 286/286. Beide Opus-Produkte
behalten die wiederholte Modulsperre über alle Zeilen.

In den getrennten R2-Proben benötigt Opus v72 bei verzweigter
Einzelabfrage 22,9 MB zusätzlichen PHP-Speicher gegenüber 3,2 MB
ohne Skill. Sol v72 traversiert für 768 Anfragen nach je 48 Seiten
295.296 Vereinigungen. Seine PHP-Ticks wachsen bei vierfacher
Anfragezahl von 219.482 auf 2.647.327. Die Kontrolle wächst von
49.352 auf 189.901. Die Sol-Modellzeit für R2 ist in diesem Paar
719,16 gegenüber 342,42 Sekunden. Die Funktionsscores allein
tragen keine Freigabe. Vergleich, Replays und verifiziertes
Roharchiv liegen im lokalen Evaluationsbestand v72-caller-cost.

Die Folgeprüfung hält den Skill konstant und gibt beiden Armen
denselben Projektcheck. Eine neue R2-Verzweigung unterscheidet
die unerwünschten Zwischenmengen von der passenden Referenz.
In R14 unterscheidet eine Prüfform mit verschachtelten Zeilen
die wiederholte Modulsperre von zwei korrekten Implementierungen.
Beide Aufgaben behalten ihre getrennten alten Prüfformate.
Die Versuche sind im lokalen Evaluationsbestand
r2-visible-branch-cost und r14-visible-work-cost gebunden.

Der kombinierte R2-Projektcheck ergibt bei Opus mit Skill
35/37. Beide Abweichungen betreffen denselben Vertragsbruch.
Ein Speicherfehler der Blockabfrage wird auf einen gewöhnlichen
Beitragsverweis ohne Abhängigkeit von dieser Abfrage übertragen.
Die Zulässigkeitsprüfung frisch gelesener Zeilen besteht.
Die Kontrolle erreicht 37/37, hat wegen einer gelöschten
Testlaufzeit aber den Rohstatus `harness_error`. Damit bleibt
der Produktbefund gesichert und die Skillwirkung offen.
Der Versuch liegt in r2-visible-work-and-memory.

Der zusätzliche Chrome-Replay zum früheren R1-Kandidaten
bestätigt die abweichende Auswahl im geöffneten Editor-Dialog.
Abbrechen stellt geöffnete Seite, Eingabe und Prüffreigabe in
allen Produkten wieder her. Verwerfen verwendet in allen das
ursprünglich gewählte Ziel. Die Prüfschaltfläche bleibt während
des Dialogs deaktiviert. Der bleibende Funktionsverlust ist in
diesen Übergängen nicht nachgewiesen. Die Proben liegen unter
v70-live-state im lokalen Evaluationsbestand.

## v71 und Expertenrunde zur quadratischen Gesamtarbeit

Der gebundene Vergleich ergibt 37/37 in R2 und 12/12 im
unabhängigen R20 auf beiden Modellen mit und ohne Skill.
Jedes Paar verwendet dieselben Bedingungen und eine gültige
Kontrolle aus einem früheren Lauf. Die Kandidaten des
Berichtsversands erzielen dieselben Arbeitszähler wie ihre
Kontrollen. Sie benötigen in diesem Paar 1,34× Modellzeit
bei Sol und 1,51× bei Opus. Eine Wirkung der Regeländerung
über verschiedene Stichproben ist damit nicht belegt.

Im WordPress-Fall erzeugt und hält Opus v71 bei 1.024
Ausgabeeinträgen mindestens 524.800 Mitgliedschaften in
verschieden großen vollständigen Zwischenmengen. Der
verzweigte Einzelabruf braucht zusätzlich 57,4 MB PHP-Peak
mit Skill und 3,2 MB ohne. Der gemischte Pfad zeigt bei
beiden etwa vierfaches Wachstum der gezählten PHP-Ticks
bei vierfacher Eingabe. Die native Array-Arbeit und der
gleichzeitig gehaltene Speicher müssen separat geprüft
werden. Sol v71 bleibt in derselben verzweigten Einzelprobe
unter dem Peak seiner Kontrolle. Rohscores, Produktproben
und beide verifizierten Archive liegen im lokalen
Evaluationsbestand unter v71-shared-lifetime.

Fable 5.2 und Astra 6.2 auf high beauftragten Opus 5.5
beziehungsweise Sol 6.1 auf high mit der Messauswertung.
Ihre unabhängige Recherche und das Gegenlesen mit Codex
führen zu einem Entwurf für eine kürzere Regel 7. Der
Entwurf prüft kumulative Arbeit und gleichzeitigen Speicher
am normalen Verbraucher. Er respektiert Funktionen,
bestandsrelevante Lookup-Semantik, Berechtigung und Frische.
Gezielte sichtbare Projektproben bleiben eine eigene
Intervention, deren zusätzlicher Effekt erst zu prüfen
ist. Die unabhängige Produktabnahme misst Arbeit, Peak,
Funktion und Autoraufwand. Dossier, Gegenlesen und Entwurf
liegen unter quadratische-arbeit-expertenrunde im selben
Evaluationsbestand. Der Entwurf ist noch nicht gemessen.

## Aktueller Stand von W-005 mit Sol 6.2 und Opus 5.5

Der v60-Vergleich verwendet beide Modelle auf medium. Beim R2-Projekttest
bewahren alle Produkte die 35 ursprünglichen Prüfungen und bestehen
den eingefrorenen Frischetest. Mit nur diesem Frischetest blieb die
gemeinsame Grapharbeit bei beiden Modellen und in beiden Armen
quadratisch.

Die nächste Paarung behält denselben Auftrag bei. Der lokale
Projektvertrag enthält zusätzlich einen Graphcheck am gewöhnlichen
Usage-Einstieg. Ein funktional korrekter quadratischer Gegenentwurf
erreicht 36/37, die Referenz 37/37. Beide Modelle erreichen mit und
ohne Skill je 37/37 und bestehen zusätzlich 16/16 Ergebnislisten aus
acht unabhängig erzeugten Graphen in beiden Anfragereihenfolgen.
Die Laufzeitfaktoren mit Skill sind 1,24 für Sol und 0,97 für Opus.
Die Tokenfaktoren einschließlich Cache-Leseanteil sind 1,96 und 1,18.
Bei 512 Eingaben zählt der Opus-Kandidat 34.157 PHP-Ticks und die
Kontrolle 17.781. Beide erfüllen die Skalierungsgrenze. PHP-Ticks
messen keine Produktlaufzeiten und erfassen native Operationen nur
begrenzt. Die Belege stehen im lokalen Evaluationsbestand unter
`v60-ui-text-route/r2-graph-test`.

Beim unabhängigen Viewer-Fall R18 bestätigt der blinde Astra-Review
den Wegfall der quadratischen nativen Verweissuche im Sol-Kandidaten.
Er findet zugleich zwei verbleibende Svelte-Aufrufe eines entfernten
Helfers. Die ursprünglichen 7/7 bleiben im Rohscore. Die Zusatzprobe
mit verknüpften Decisions reproduziert den Fehler in Chrome. Beide
Kontrollen, der Opus-Kandidat, die frühere Sol-Fassung v57 sowie eine
Kopie mit genau zwei reparierten Referenzen bestehen. Die gefundenen
Referenzen betreffen bestehendes Anwendungsverhalten. Der
ursprüngliche Prüfstand und die Produkte bleiben unverändert.
Die anonymisierten Diff-Hashes und die Zusatzprobe liegen lokal unter
`v60-ui-text-route/r18-supersession`.

Astra 6.2 auf high empfiehlt eine frühere Prüfung der gemeinsam
genutzten Arbeit, einen einzigen UI-Abschlussdiff und eine klare
Platzierungsgrenze für Cleanup. Sol 6.2 und Opus 5.5 auf high
bestätigen die gezielte Referenzsuche vor dem Abschluss.
Der v61-Quellstand führt diese Änderungen aus. Code verfolgt
gemeinsame Arbeit vor dem Entwurf und noch nicht abgedeckte Pfade im
finalen Diff. Beim Entfernen oder Umbenennen von Symbolen verfolgt
der Abschluss verbleibende Referenzen, einschließlich unveränderter
Templates und Bindings. UI prüft Maßliterale bei tatsächlich
betroffener Größen- oder Abstandsarbeit. Cleanup wahrt ein
ausdrückliches Verbot von Ersatzzieldateien innerhalb von ADR-0238.
Die Vollprüfung für v60 meldet zwölf bestandene Checks, null
Fehler und zwei reine Modelltestpfade. Die Wirkung von v61 wird separat
geprüft.

Der v61-Vergleich verwendet denselben Viewer-Auftrag und dieselben
beiden gültigen Kontrollen. Beide Modelle erreichen mit und ohne
Skill 7/7 und bestehen die ergänzende Chrome-Probe. Sol mit v61
hält die beiden vorhandenen Nachfolgeanzeigen funktionsfähig und
verwendet das Set weiterhin für die native Verweisprüfung. Die
Opus-Kontrolle und der Opus-Kandidat behalten die Vektorsuche im
nativen Reader. Der Kandidat benennt sie.

Im Sol-Paar liegen Zeit bei Faktor 2,77 und Tokens bei 7,43
einschließlich sowie 5,07 ohne Cache-Leseanteil. Im Opus-Paar sind
es 1,19, 1,40 und 1,59. Die Sitzungslasten gelten für je ein Paar.
Sols native Spur zeigt sieben gelesene Skill-Dateien neben dem
bereitgestellten Code-Einstieg. Welcher Teil der Anleitung den
Aufwand verursacht, ist offen. Die übrigen R2-Nachweise gelten für
v60. Die Bestätigung des Kostenkompromisses bleibt offen. Die v61-
Paketdeltas, Rohspuren, Chrome-Probe und Aufwand stehen lokal unter
`v61-review-routing`. Vier Paketvarianten, sechs Shared-Regeltests
und 33 Laufzeittests bestehen. Ein Laufzeittest ist übersprungen.

In den Sol-Spuren zu v60 und v61 wird die Validierungsreferenz früh
gelesen. Im v61-Viewer-Lauf sind 73.778 Tokens ohne Cache-Lesungen vor
dem Leserstart belegt. Insgesamt meldet der Hauptagent 83.530 und der
Leser 43.338 solcher Tokens. In der Kontrolle stehen 25.040. Cache-
Nutzung der ersten Anfrage, zusätzliche Arbeit am nativen Reader und
Werkzeugsuche unterscheiden sich zwischen den Läufen. Die Lektüre
einer einzelnen Datei erklärt den Gesamtunterschied nicht.

Der v62-Quellstand (`49255c4`) präzisiert die eine Tabellenzeile für
`Validation`. Gewöhnliche Prüfungen folgen Abschnitt 3. Die Referenz
greift bei einem erneut gescheiterten Check, einem Review der Tests
selbst und beim Nachweis einer konkreten besonderen Garantie am
betroffenen Pfad. Vier Paketvarianten, sechs Shared-Regeltests und
33 Laufzeittests sind geprüft. Ein Laufzeittest ist übersprungen.
R18 und der R2-Projektcheck laufen auf medium mit Sol und Opus.
Ihre vier gültigen Kontrollen bleiben unverändert. Eine getrennte
Kalibrierung bindet den vorhandenen Viewer-Typcheck an dieselbe
Lockdatei und an lokal vorhandene Abhängigkeiten. Die eingefrorenen
Modellprodukte bleiben unverändert. Artefakte stehen im lokalen
Evaluationsbestand unter `v62-validation-route`.

Der vollständige v62-Vergleich enthält acht gültige Produkte
und bestätigte Eingaben. Beide Viewer-Paare erreichen 7/7 und
bestehen den Browser-Replay. Beide R2-Paare erreichen 37/37
sowie 16/16 unabhängige Ergebnislisten. Die Viewer-Sol-Laufzeit
beträgt Faktor 2,66 und die Tokens ohne Cache-Leseanteil
Faktor 2,83. Das R2-Sol-Paar liegt bei 1,90 und 2,06. Die beiden
Opus-Paare liegen bei 1,28 und 1,70 im Viewer sowie bei 0,80 und
1,04 in R2. Diese Werte stammen jeweils aus einem Paar.

Eine zusätzliche R2-Sonde erreicht den regulären Usage-Einstieg
über einen flach verzweigten, gemeinsam benutzten Teilgraphen.
Vierfach wachsende Eingabe und Ausgabe ab 64 Zielblöcken
ergeben bei Opus mit Skill Faktor 3,82 für gezählte PHP-Anweisungen,
ohne Skill Faktor 13,95. Sol erreicht 11,87 mit und 13,60 ohne
Skill. Alle liefern pro Quelle dieselben drei Beitragskennungen.
Opus nutzt innere Zwischenergebnisse. Sol pflegt einen begrenzten
Cache am abgefragten Ausgangspunkt, besucht die gemeinsame
Verzweigung aber für verschiedene Quellen erneut. Die Sonde
steht getrennt von den Rohscores. Sie zählt native
Arrayoperationen und Speicheraufwand nicht einzeln.

Das vorhandene `npm run check` meldet mit passender lokaler
Lockdatei genau die zwei ungültigen Svelte-Referenzen in v60.
Ausgangsstand, beide Kontrollen und v61-Sol bestehen. Die
separate Messrunde mit verfügbaren Abhängigkeiten behält
Auftrag und Skillpakete bei und erzeugt wegen der anderen
Projektausstattung vier frische Läufe. Die vollständigen
Belege und Roharchive stehen lokal unter `v62-validation-route`.

Die zusätzliche Viewer-Runde mit identischem Auftrag und
identischen Skillpaketen liefert vier gültige Produkte. Alle
bestehen 7/7, den Browser-Replay und den nachgelagerten Typcheck.
Sämtliche Dependency-Dateien sind nach den Läufen bytegleich.
Sol benötigt mit Skill Faktor 2,08 für Zeit und 2,62 für Tokens
ohne Cache-Lesezugriffe. Opus benötigt 1,23 und 2,07. Beide Sol-
Arme treffen beim Standard-Typcheck auf eine Windows-Zugriffssperre
beim Laden der Vite-Konfiguration. Beide führen später denselben
Typcheck mit ausdrücklich gewählter Svelte-Konfiguration erfolgreich
aus. Die direkte Konfiguration findet in der v60-Gegenprobe wieder
exakt die zwei ungültigen Referenzen. Dieser Versuch misst die
bereitgestellten Abhängigkeiten samt der beobachteten Ausführungsreibung.

Eine isolierte R2-Referenz verbindet den kantenbegrenzten Cache
des Sol-Produkts mit vollständigen kleinen Ergebnismengen der
gemeinsamen Zwischenknoten. Sie erreicht 37/37 und weitere 16/16
unter PHP 7.4.33. In der flachen Sonde sinkt die Arbeit bei 256
Quellen von 294.579 auf 29.624 PHP-Ticks. Bei vierfacher Eingabe
steigt sie um Faktor 3,83. Bei der einzelnen Anfrage mit 512
erreichbaren Seiten beträgt der PHP-Spitzenwert 7.536.888 Bytes,
im Opus-Produkt 13.697.144. Der Vergleich enthält auch die
Fixture-Daten. Die Referenz gilt für diese Graphformen. Sol und
Opus auf high bestätigen das Wiederverwenden kleiner innerer
Ergebnisse als tragfähige Richtung. Regel 7 erfasst die
gemeinsame Arbeit und die Größe dieser Zwischenergebnisse bereits.
Belege stehen lokal in `v62-validation-route/bounded-reference` und
`v62-validation-route/project-check-ready`.

Der unabhängige Fall R19 verwendet den realen Plan-Validator
aus Suite `fa44e3f` mit seinen vorhandenen Tests. Der Auftrag
verlangt geschlossene Zyklusdiagnosen im bestehenden Text- und
JSON-Vertrag und akzeptiert lange gültige Ketten. Ein linearer
Referenzentwurf erreicht 9/9. Der funktionsgleiche Gegenentwurf
mit vollständigen Pfadkopien scheitert allein an der Allokations-
prüfung. Die Zahl der Zugriffe auf die Entscheidungsabbildung
ist gleich. Beim Wachstum von 256 auf 768 Decisions steigt
der Peak von 42.072 auf 155.440 Bytes in der Referenz und von
321.744 auf 2.552.696 im Gegenentwurf.

Beide Sol-R19-Arme und die Opus-Kontrolle erreichen 9/9. Die
Laufzeit und die Tokens ohne Cache-Lesezugriffe liegen bei
Sol beim 1,01- und 1,34-Fachen der Kontrolle. Der Opus-
Kandidat konnte wegen abgelaufener CLI-OAuth-Anmeldung keine
gültige Sitzung ausführen. Seine Messung steht aus. Die drei
gültigen Produkte und der Transportbefund sind in
`r19-validator-cycles` lokal gebunden.

Die blinde Quellprüfung von Astra 6.2 auf high beurteilt die
beiden Sol-Produkte ohne Modellbedingung und Laufmetriken.
Beide nutzen einen gemeinsamen aktiven Pfad und kopieren ihn
nur für die eigentliche Zyklusdiagnose. Die ergänzenden Tests
des Kandidaten prüfen auch den Text-CLI-Einstieg, die
Feldreihenfolge und unveränderte Diagnosen. In der Kontrolle
sind Arbeits- und Decision-Zyklus in getrennten Tests geprüft.
Die Zuordnung und die beiden Record-Hashes wurden erst nach
dem Urteil geöffnet.

Nach erneuerter Anmeldung erreicht der gültige Opus-
Ersatzlauf auf medium 9/9. Damit bestehen beide Modelle
mit v62 und ohne Skill alle neun Prüfungen. Opus mit
Skill benötigt 421,63 statt 356,70 Sekunden und 73.155
statt 56.047 Tokens ohne Cache-Lesezugriffe. Die Faktoren
sind 1,18 und 1,31. Beide Opus-Produkte bestehen den
Allokationscheck. Der Kandidat nutzt eine gemeinsame,
iterative Zyklusfunktion für die beiden Aufrufer.
Zwei zusätzlich gestartete Routing-Tests benötigen die
volle Suite außerhalb des eingefrorenen Ausschnitts.
Die 57 Tests des vorgesehenen Validatormoduls laufen
mit einem Skip durch. Der gültige Ersatzlauf und der
ursprüngliche Transportfehler bleiben einzeln gebunden.

In der v62-Viewer-Rohspur verbraucht der eng beauftragte Leser
71.245 Tokens ohne Cache-Lesezugriffe. Der bereitgestellte
Auftrag enthielt die einschlägigen Regeln, trotzdem lud der
Leser Code, UI und weitere Skill-Referenzen. Der Hauptagent
wartete einmal zehn Sekunden und erhielt einen Timeout. Die
Leserspur endet abgebrochen ohne vollständige
Ergebnisnachricht. Zwei versandte Nachrichten sind belegt,
ihr Inhalt und ihre Verwendung sind nicht einsehbar.

v63 (`6e25dbd`) macht den bereits eng begrenzten Auftrag
für den Leser ausdrücklich abschließend. Der Leser verwendet
die mitgelieferten Regeln und liest die erforderlichen
Projektregeln, betroffenen Quellen und Belege. Ein Warte-
Timeout lässt dieselbe Prüfung offen. Die vier Paketvarianten
und sechs Regeltests sind geprüft. Im Runtime-Snapshot
laufen 33 Tests, einer ist übersprungen. Der Sol-Viewer-
Vergleich nutzt die gebundene passende Kontrolle mit denselben
lokalen Abhängigkeiten. Der Opus-Vergleich wartet auf eine
erneuerte Anmeldung. Die High-Beratung bei Sol bestätigt die
Rollenbegrenzung. Die aktuelle Opus-High-Beratung traf auf
denselben OAuth-Fehler, ihre frühere R18-Einschätzung bleibt
separat. Belege stehen unter `v63-reader-scope`.

Der abgeschlossene v63-Sol-Vergleich erreicht in beiden
Armen 7/7 und erhält die beiden bestehenden Nachfolgeanzeigen
im separaten Chrome-Replay. Beide zählen bei 512 Einträgen
912 ID-Zugriffe im Frontend. Der Kandidat ersetzt im
nativen Reader zusätzlich die Vektorsuche pro Verweis durch
einen gemeinsamen Index. Dies ist durch den Diff belegt.
Eine native Tauri-Ausführung liegt nicht vor. Die Sol-Läufe
dauern mit und ohne Skill 399,05 und 169,69 Sekunden.
Der Aufwandsfaktor beträgt 2,35 für Zeit, 1,06 für Tokens
ohne Cache-Lesezugriffe und 3,61 inklusive Cache-Lesezugriffen.
In beiden Läufen fehlt eine Delegation. Ein Wirkungstest des
neuen Leserauftrags steht daher aus. Beide Produkte,
gebundene Eingaben, native Spuren und der Browser-Replay sind
im geprüften v63-Sol-Archiv gesichert.

Nach erneuerter Anmeldung besteht auch das v63-Opus-Paar
7/7. Beide Produkte erhalten die bestehenden Nachfolge-
anzeigen im separaten Chrome-Replay. Opus benötigt mit
Skill 197,23 statt 75,49 Sekunden und 105.915 statt 27.613
Tokens ohne Cache-Lesen. Das entspricht Faktor 2,61 und
3,84. Der Vordergrundleser lädt keine Skills nach und
liefert nach 101,11 Sekunden einen vollständigen Befund.
Seine neun Aktionen umfassen eine nachgewiesene
temporäre Schreiboperation trotz lesendem Auftrag.
Die Datei ist am Ende entfernt. Der Opus-Diff indexiert
das Frontend und lässt die vorhandene wiederholte Suche
im Rust-Reader bestehen, ebenso wie die Kontrolle.
Der vollständige Vergleich und die Leseraktionen sind
in `v63-reader-scope` gebunden.

Die unabhängige Strukturberatung mit Astra 6.2 auf high
bestätigt die Relevanz der Gesamtarbeit einschließlich
unveränderter Aufrufer und der Bestandsfunktionen. Sie
findet unterschiedliche Auslöser zwischen ADR-0239 und
Code v63. Die ADR stellt auf den betroffenen Gegenstand
und einen verfügbaren Leser ab. Der aktuelle Skill stellt
auf den nach den Tests ungeklärten Übergang ab. Ein
festes Diff mit einer bekannten Schutzlücke erlaubt eine
gezielte Beobachtung von Befund, Abschluss, Lektüre und
Aufwand unabhängig von einem vollständigen Produktlauf.

Als kleine Kürzung kommt eine direkte Route zu Plan für
ein zugewiesenes lesendes Review nativer Felder infrage.
Technische Planung und Standalone brauchen den bisherigen
Einstieg. Die Reduktion der an Textreviewer übergebenen
Code-Regeln benötigt eine Änderung der Helper-Logik und
liegt außerhalb des Plans. Ein bestehender Handoff-Fall
belegt, dass bei abgeschlossener Arbeit ein Abgleich
mit der aktuellen Evidenz genügt und akzeptierte Tests
nicht wiederholt werden. Die Kürzungsvorschläge sind
Quellbefunde ohne bisher gemessene Wirkung.

Der gezielte Gegenleser-Versuch zu v63 verwendet einen
unveränderten Diff mit einer belegten Schutzlücke beim
erneuten Laden. Sol 6.2 auf medium startet in jedem Arm
einen frischen Leser. Beide finden den Fehler und schließen
ihren lesenden Auftrag ab. Die Quellen bleiben bytegleich.
Der Kandidat lädt keine vollständigen Skilldateien nach.
Die Sitzungszeit beträgt 209,96 gegenüber 154,69 Sekunden.
Ohne Cache-Lesezugriffe liegt der Aufwand bei 78.843
gegenüber 74.486 Tokens, inklusive Cache bei 394.107
gegenüber 223.862. Ein zusätzlicher, in der Spur
verschlüsselter Nachrichtenaustausch im Kandidaten
begrenzt die Zuschreibung an den Wortlaut des Auftrags.
Gebundene Rohdaten und die terminalen Leserspuren liegen
in `v63-reader-scope`. Dieser Versuch prüft die
Leserleistung bei garantiertem Start. Die Bedeutung
der beiden unterschiedlichen Auslöser aus ADR und Skill
für einen tatsächlichen Produktlauf bleibt offen.

Die zusätzliche R2-Gegenprobe verwendet die unveränderten
v62-Produkte und dieselbe flache Graphform mit oder ohne
eine Seite, die alle Ziele direkt referenziert. Alle Produkte
liefern die jeweils exakte lineare Ausgabe in beiden
Anfragereihenfolgen. Sol mit Skill wächst bei vierfacher
Eingabe ohne die extra Seite um Faktor 3,80, mit ihr um
11,87. Bei Opus mit Skill betragen beide Faktoren 3,82.
Opus ohne Skill liegt bei 3,66 und 13,95. Sol ohne Skill
liegt bei 13,80 und 13,60. Der zusätzliche Zweig verhindert,
dass eine gemeinsame Endwurzel den verbleibenden Aufwand
verdeckt. Im Sol-Kandidaten startet dann für jedes Ziel
eine eigene Traversierung des gemeinsamen inneren Pfads.
Die Resultate und die Fixture-Hashes stehen in
`v62-validation-route/R2-SHAPE-CONTRAST.json`.

Sol 6.2 und Opus 5.5 auf high empfehlen für diese
Fallauswahl eine gezielte Präzisierung im vorhandenen
Satz. v64 (`ee4c99c`) nennt gemeinsame und eigene
Arbeit unter dem tatsächlichen Aufrufer. Das Paketdelta
belegt ausschließlich diese fachliche Änderung. Sechs
Shared-Regeltests, 13 Runtime-Builder-Tests und 33
Tests des generierten Runtime-Snapshots bestehen.
Ein Snapshot-Test ist übersprungen. R2 und der
unabhängige R19-Validator laufen in beiden Modellen
auf medium gegen unveränderte Kontrollen ohne Skills.
Die Wirkung der genaueren Fallauswahl steht aus.

### v64 · Opus und Kosten einer Einzelanfrage

Opus 5.5 auf medium besteht in v64 die 37 R2-Prüfungen
einschließlich der frisch gelesenen Datensätze sowie alle
neun Validatorprüfungen. Die beiden gebundenen Kontrollen
bestehen ebenfalls. Mit Skill betragen die Zeitfaktoren
0,92 für R2 und 0,85 für R19. Ohne Cache-Lesezugriffe
betragen die Tokenfaktoren 1,11 und 1,23. Der separate
Graph-Replay beobachtet mit direktem Nebenpfad bei
vierfacher Größe 3,80× und 13,95× gezählte PHP-Anweisungen
mit und ohne Skill. Die exakten IDs bleiben erhalten.

Eine getrennte Einzelanfrage hat immer drei Blockebenen.
Mit 256 und 1.024 Brücken wachsen die Eingabe und die
erforderlichen 2N IDs linear. Die zusätzlichen PHP-
Höchststände steigen bei Opus mit v64 von 6.747.208 auf
86.566.824 Bytes. Ohne Skills steigen sie von 1.509.424
auf 2.797.656 Bytes. Die begrenzte Referenz benötigt
1.922.216 und 4.095.368 Bytes. Das v64-Produkt übernimmt
die Menge gemeinsamer Seiten in jede Brücke und hält
N × (N + 1) Einträge vor. Der PHP-Zähler erfasst den
Arrayoperator als einzelne Anweisung. Die Bytes gelten
für die Allokationen des instrumentierten PHP-Prozesses.
Das vollständige Opus-Paar, die Replay-Eingaben und
die Speicherbeobachtung sind im v64-Opus-Archiv gebunden.

Der Sol-v64-Lauf pausierte während der Windows-Sandbox-
Einrichtung rund 24 Minuten und 36 Sekunden und setzte im
selben Prozess fort. Der Runner erreicht vor der finalen
Antwort sein 30-Minuten-Limit und kennzeichnet den Lauf
als unvollständig. Der Versuch erhält keine Modellwertung.
Die native Spur und die Plattformzeit liegen getrennt vor.

Der unterbrochene Sol-Quellstand besteht die 37 Checks im
gebundenen Offline-Replay. Bei vierfacher Eingabe und
direkter Zusatzverwendung wächst seine Arbeit dennoch um
Faktor 13,70. Der Sol-Validator läuft eigenständig gültig
durch und erreicht mit und ohne Skill je 9/9. Der Kandidat
benötigt 246,67 statt 191,54 Sekunden und 84.818 statt
30.073 Tokens ohne Cache-Lesezugriffe. Transport, Replay
und gültige Messwerte sind getrennt im v64-Sol-Archiv.

### v65 · Vorhandene Frage zur Gesamtarbeit präzisiert

Sol und Opus auf high führen den Speicherbefund auf die
je Brücke kopierten und vorgehaltenen Zwischenmengen
zurück. v65 nennt in der vorhandenen Frage 1 ausdrücklich
gleichzeitig gehaltene Daten gegenüber dem Bedarf des
Verbrauchers. Die Frage berücksichtigt gemeinsame Daten
in mehreren Aufrufen und innerhalb einer einzelnen
Anfrage. Suite `ba41ad2` übernimmt den Snapshot aus
Shared `8ab508b`. Die vier Pakete enthalten ausschließlich
das erwartete gemeinsame Delta. 101 Shared-Tests und
33 Runtime-Snapshot-Tests bestehen. Ein Snapshot-Test ist
übersprungen. Der Plan-Validator meldet keine Fehler oder
Warnungen. Die neuen R2- und R19-Vergleiche binden die
geprüften Kontrollen. Die Wirkung der Präzisierung steht
aus. Der bisherige Viewer-Leserbefund bleibt getrennt.

Der erste Opus-5.5-Lauf mit v65 auf medium erreicht im
WordPress-Fall 37/37. In der flachen Einzelanfrage bei
1.024 Brücken benötigt der Kandidat 2.830.832 zusätzliche
PHP-Bytes gegenüber 2.797.656 ohne Skills. Im Sammler mit
direkter Zusatzverwendung wachsen die gezählten Anweisungen
bei vierfacher Größe weiterhin um Faktor 14,74, gegenüber
13,95 ohne Skills. Die Ausgangs- und Ergebnislisten bleiben
exakt. Der Code speichert Ergebnisse unter angefragten
Repräsentanten. Der gemeinsame innere Pfad wird erneut
besucht, wenn eine direkte Verwendung je Ziel die
Zusammenlegung verhindert. Der gemeinsame Satz bleibt
bis zum Abschluss der laufenden Sol-Paare unter Prüfung.

Der unabhängige Validator besteht bei Opus mit und
ohne v65 jeweils 9/9. Die Zeit liegt beim 0,97-Fachen,
Tokens ohne Cache-Lesezugriffe beim 1,30-Fachen der
Kontrolle. Die zwei vollständigen Opus-Paare und beide
R2-Replays sind im v65-Opus-Archiv nachvollziehbar.

Die vollständige v65-Runde enthält acht gültige
Modellläufe. Sol besteht mit und ohne Skill in R2
37/37 und in R19 9/9. Im flachen Sammler mit direkter
Zusatzverwendung sinkt Sols Arbeit bei 256 Zielen
von 555.192 auf 33.735 gezählte PHP-Anweisungen.
Der zusätzliche PHP-Höchststand der Einzelanfrage
bei 1.024 Brücken sinkt von 4.687.848 auf 3.467.024
Bytes. Eine getrennte Probe mit zwei verschiedenen
gemeinsamen Teilpfaden und disjunkten Anfragen bestätigt
bei exakt erhaltenen Listen 82.710 gegenüber 1.126.893
Ticks. Opus benötigt in derselben Probe 1.223.843
gegenüber 699.043. Die Ursache im Code ist der Cache
für angefragte Wurzeln. Der gemeinsame innere Pfad
bleibt unter verschiedenen Wurzeln ungeteilt.

Sols gültiger v65-R2-Lauf braucht 938,10 statt 312,10
Sekunden und 129.721 statt 70.616 Tokens ohne Cache-Lesen.
Die beobachteten Toolintervalle umfassen 118,76 und
55,86 Sekunden. Die übrige Zeit ist anhand der nativen
Spur keiner einzelnen Ursache sicher zuzuordnen. Der
24-minütige Windows-Sandbox-Halt aus v64 tritt in dieser
Spur nicht auf. Im unabhängigen Validator betragen
die Sol-Faktoren 1,29 für Zeit und 1,81 für Tokens
ohne Cache-Lesezugriffe. Das vollständige v65-Archiv
bindet die Rohspuren, beide Produktpfade und die Replays.

### v66 · Gemeinsame Arbeit dort teilen, wo Aufrufpfade zusammenlaufen

Sol 6.2 und Opus 5.5 auf high bestätigen den wiederholten
inneren Pfad. Sol weist auf die missverständliche
Formulierung „all items“ in Frage 1 hin. Opus empfiehlt,
Ort und Kosten der Wiederverwendung in der vorhandenen
Regel zu verbinden. v66 ersetzt einen Absatz der Regel 7
und richtet die bestehende Prüffrage an den tatsächlich
betroffenen Elementen und Zweigen aus. Der Gesamtbedarf
an kopierten und gleichzeitig gehaltenen Zwischendaten
bleibt Teil der Designentscheidung. Suite `9af5086`
übernimmt Shared `ce3c000`. 101 Shared- und 33
Runtime-Snapshot-Tests bestehen, ein Snapshot-Test ist
übersprungen. Die Abweichung der Pakete ist auf die zwei
betroffenen Textstellen beschränkt.

Die Vergleiche zu R2 und R19 verwenden die gültigen
identischen Kontrollen für beide Modelle. R14 prüft
zusätzlich den älteren Opus-Befund der wiederholten
Modulsperre am normalen Browser-Einstieg. Die gebundene
Opus-Kontrolle wird wiederverwendet. Die erste passende
Sol-6.2-Kontrolle wird für dieselbe eingefrorene R14-Aufgabe
auf medium ausgeführt. Die technische Prüfung und der
Produkt-Replay bleiben vom Wirkungsvergleich getrennt.

Opus v66 erreicht in R2 37/37 einschließlich des später
gelesenen Zustands. Die Einzelanfrage bei 1.024 Brücken
liegt bei 2.828.648 gegenüber 2.797.656 zusätzlichen
PHP-Bytes. Im flachen Sammler mit rein gemeinsamem
Pfad wächst die Arbeit bei vierfacher Größe um Faktor
14,80 gegenüber 3,66 ohne Skills. Bei 256 Zielen sind
das 537.218 gegenüber 12.683 PHP-Anweisungen. Das Produkt
teilt den aufgebauten Graph und die aufgelöste Einstiegsknoten-
Identität. Die gemeinsam erreichte Traversierung läuft für
jeden Aufruf erneut. Direkte Zusatzverwendung und Teilgruppen
behalten ebenfalls die wiederholte Arbeit. Die exakten
Ergebnislisten und der reguläre Score bleiben erhalten.
Die v66-Produktabweichung wird separat von möglicher
Wortlautwirkung bewertet. Opus erreicht bei R19 beidseits
9/9. Der Kandidat benötigt das 1,86-Fache der Laufzeit und
das 1,45-Fache der ungecachten Eingabetokens. R14 erreicht
beidseits 8/10. Beide Implementierungen wiederholen bei
wachsender Zeilenzahl DOM- und Schlüsselarbeit. Der
ergänzende Chrome-Replay bestätigt beidseits 286/286
Funktionsprüfungen. Der Sol-Kandidat zu R2 bricht nach
1.802 Sekunden ohne Dateidiff ab. In dieser Zeit bleibt der
Windows-Sandbox-Aufbau mehrfach lange aktiv. Der Lauf wird
als technisch unvollständig archiviert. Weitere Sol-Läufe
zu v66 sind offen.

### v67 · Vorhandene kurze Lesewege präzisieren

Suite `9205453` und Shared `4d213f8` verwenden wieder
den Kriterienstand aus v65. Das Paketdelta zu v65 betrifft
zwei Referenzauslöser. Bei einer Änderung an vorhandenem
Text in WordPress gilt der kurze UI-Pfad auch dann, wenn
die Aufgabe `wp-admin` berührt. Die Code-Reviewer-Referenz
ist für ein angefordertes Code-Review mit Findings bestimmt.
Astra 6.2 High hat die überzähligen Lesewege an der
Sol-Spur nachvollzogen. 101 Shared- und 33 Laufzeittests
bestehen, ein Laufzeittest ist übersprungen.

Der R2-Vergleich bindet beide Arme der eingefrorenen
Aufgabe an dieselbe lokal verfügbare PHP-Version 7.4.33.
Beide Arme pro Modell werden unter dieser geänderten
Startbedingung neu gemessen. Der technische Vorversuch
bestätigt den Aufruf der mitgelieferten Version in der
Windows-Sandbox. Der Vergleich prüft weiterhin Funktion,
Zustandsfrische, wiederholte Arbeit in gemeinsamen Pfaden,
Speicher und Modellaufwand.

Im v67-Paar erreicht Opus beidseits 37/37 einschließlich
der Prüfung frisch gelesener Zeilen. Der Kandidat braucht
1,14× Zeit, 1,11× Tokens ohne Cache-Lesezugriffe und
1,33× mit Cache-Lesezugriffen. Bei 64→256 Zielen wächst
der PHP-Arbeitszähler im reinen gemeinsamen Pfad von
3.852 auf 14.220 ohne und von 4.306 auf 16.018 mit Skill.
Mit zusätzlicher direkter Verwendung wächst er von
41.100 auf 605.580 und von 54.033 auf 804.753. Beide
Produkte behalten korrekte Ergebnisse. Die Zahl der
Datenbankabfragen bleibt konstant. Die Teilgruppenprobe
zeigt ebenfalls wiederholte Arbeit. Der Kandidat hat
die Ergebnisrichtigkeit des gemischten Falls geprüft.
Seine Arbeitsschranke prüft den reinen gemeinsamen Pfad.

### v68 · Die kombinierte Arbeit am Sammlungseinstieg belegen

Sol 6.2 und Opus 5.5 auf high empfehlen, den bestehenden
Abschlussabsatz auf die betroffene Arbeit auszurichten.
Der neue Absatz prüft Frage 1 am endgültigen
Sammlungseinstieg. Wenn dieselben Elemente gemeinsame
und separate Arbeit erfordern können, wird geprüft, wie
die Gesamtarbeit in dieser Kombination wächst. Ein
Quellbeleg oder ein fokussierter Check genügt. R2 prüft
die Veränderungen in den getrennten Skalierungsproben.
R14 prüft die Modulsperre und Browser-Funktionen. R19
prüft einen unabhängig entstandenen Validatorfall.

Im Opus-R2-Vergleich besteht v68 wie die Kontrolle
37/37. Bei vierfacher Eingabe wächst die Arbeit im
gemeinsamen Pfad von 24.131 auf 341.123 PHP-Ticks.
Die Kontrolle wächst von 3.852 auf 14.220. Beide
Produkte liefern korrekte Verwendungen. Der Kandidat
teilt den Graphaufbau und kürzt Ketten. Die Suche
im gemeinsamen inneren Graphen wiederholt sich.
Der Autor erkennt die Restarbeit und führt sie als
Grenze an. Der v67-Absatz wird nach diesem
Produktbefund lokal wiederhergestellt. V68 bleibt
für die Auswertung seiner unabhängigen Fälle
eingefroren. Die Wortlautwirkung bleibt offen.

Im Browserfall R14 erreicht derselbe Opus-Kandidat
10/10 gegenüber 8/10 ohne Skill. Die gezählte DOM-
und Schlüsselarbeit steigt bei 16, 48 und 144 Zeilen
auf 192, 576 und 1.728. Die Kontrolle braucht 220,
1.044 und 6.588 Operationen. Die Optimierung erhält
die Sperrwirkung und vermeidet die Liste je Gruppe
erneut zu durchsuchen. Dieser Produktbefund bleibt
neben dem gegenläufigen R2-Ergebnis erhalten.

### WordPress-Variante mit zusätzlicher Projektprüfung

Die lokal wiederhergestellte v67-Fassung wird in einer
getrennten R2-Variante geprüft. Beide Arme erhalten
dieselbe zusätzliche Skalierungsprobe im vorhandenen
Projekttest. Sie trennt in der Kalibrierung die
wiederholte Suche von einer begrenzten Referenz.
Die alte Aufgabe und ihre Scores bleiben gebunden.

Opus besteht in beiden Armen 37/37. Im gemischten
Pfad wächst die gezählte PHP-Arbeit bei 64→256 Zielen
von 6.051 auf 22.947 ohne und von 5.399 auf 20.375
mit Skill. Die zurückgehaltene Teilgruppenform wächst
beidseits knapp vierfach und erzeugt die korrekten
Listen. Der zusätzliche PHP-Speicherhöchststand im
Einzelfall liegt beidseits bei etwa 2,8 MB. Der
Kandidat benötigt 1,85× Zeit und 1,49× Tokens ohne
Cache-Lesezugriffe. Auch der separate Sol-Vergleich
mit dem verifizierten MXC-Startflag erreicht beidseits
37/37. Bei 256 Zielen je Gruppe benötigt der Kandidat
89.844 gegenüber 269.777 PHP-Ticks im Teilgruppenfall.
Der Kandidat braucht 2,20× Zeit und 1,38× Tokens ohne
Cache-Lesezugriffe. Die zusätzliche Zeit in den
beobachteten nativen Werkzeugintervallen erklärt
einen kleinen Teil der Gesamtdifferenz.

Eine getrennte Speicherprobe prüft eine und zwei
Anfragen mit einer gemeinsamen Kette, deren Knoten
jeweils eine eigene öffentliche Verwendung haben.
Bei 1.024 Knoten wachsen die Ausgabe der Zweifachanfrage
auf 2.048 richtige Zuordnungen und die PHP-Ticks bei
vierfacher Eingabe ungefähr vierfach. Beim zweiten
Zugriff halten beide Opus-Produkte jedoch Ergebnislisten
für nicht angefragte Zwischenknoten. Der zusätzliche
Speicherhöchststand liegt bei der Zweifachanfrage bei
rund 31 MB je Arm gegenüber rund 3,75 MB in der
begrenzten Referenz. Die Originalscores bleiben
als Funktions- und Arbeitsbelege für ihre Fälle erhalten.
Das aktuelle Sol-Paar benötigt bei 1.024 Knoten und
zwei Anfragen rund 2,95 MB mit Skill und 3,88 MB ohne.
Eine getrennte Versuchsfassung ergänzt dieselbe
Speicherprüfung zum lokalen Projekttest in beiden
Armen. Beide ursprünglichen Projektdateien sind
als Ausgangsbasis gebunden. Der Skill-Text bleibt
v67. Eine verzweigte Form bleibt dem Replay
vorbehalten. Die Ergebnisse sind nach Prüfangebot
einzuordnen.

Die beiden Opus-Produkte mit sichtbarer Speicherprüfung
erreichen 37/37 und benötigen bei der einfachen
Zweifachanfrage rund 3,2 MB zusätzlichen PHP-Speicher.
Bei den zurückgehaltenen Verzweigungen halten beide
erneut große Zwischenmengen. Bei 768 Verzweigungen
beträgt der Höchststand rund 22,4 MB je Arm gegenüber
6,33 MB in der begrenzten Referenz. Die Listen sind
korrekt. Der Kandidat benötigt 1,63× Zeit und 1,47×
Tokens ohne Cache-Lesezugriffe. Einschließlich dieser
Zugriffe liegt der Faktor bei 2,34.

Die unabhängigen v67-Vergleiche verwenden unveränderte
Aufgaben und Prüfer. Im Browserfall R14 besteht Opus
in beiden Armen 8/10 und 286/286 im zusätzlichen
Chrome-Replay. Die zwei Arbeitsgrenzen für die
Modulsperre werden in beiden Armen verfehlt.
Im Validatorfall R19 erreicht Opus beidseits 9/9.
Die Kandidatenzeit beträgt in R14 das 0,50-Fache
und in R19 das 0,99-Fache der jeweiligen Kontrolle.
Die Verhältnisse der Tokens ohne Cache-Lesezugriffe
liegen bei 1,02 und 1,23.

Sol erreicht im selben Browserfall beidseits 10/10
und je 286/286 im Chrome-Replay. Bei 144 Zeilen
zählt die DOM- und Schlüsselprobe 1.116 Operationen
mit gegenüber 1.260 ohne Skill. Der JS-Zähler
erreicht 831 gegenüber 759. Beide Produkte erfüllen
die Arbeitsschranken. Der Kandidat benötigt 1,42×
Zeit und 1,30× Tokens ohne Cache-Lesezugriffe.
Sol erreicht auch im Validatorfall R19 beidseits 9/9.
Der Kandidat benötigt 1,19× Zeit und 0,80× Tokens ohne
Cache-Lesezugriffe. Die v67-Vergleiche für R14 und R19
sind für beide Modelle vollständig.

### v69 · Überbreiten Querverweis entfernen

Der Hauptskill verlangt die ausführliche Review-
Referenz bei einem beauftragten Code-Review mit
Findings. Die Implementierungsreferenz verwies
zusätzlich für die allgemeine Ergebnisprüfung darauf.
Sol öffnete im Browserfall beide Referenzen. Die
Reihenfolge ist protokolliert. Der Auslöser des
zweiten Leseaufrufs ist nicht unabhängig beobachtet.
V69 entfernt die breitere Querverweisung. Die
Schlussprüfung der Implementierung und der
beauftragte Review-Ablauf stehen weiterhin im
Hauptskill. Die vier Paketvarianten bestätigen
genau das Referenzdelta. 33 Laufzeittests bestehen,
einer ist übersprungen. Der unabhängige Viewer-Fall
prüft diesen Kandidaten mit gebundener Toolchain.

Beide Modelle erreichen im Viewer 7/7 mit und ohne
Skill. Alle vier Produkte bestehen den getrennten
Chrome-Replay. Sol mit Skill liest die geänderte
Implementierungsreferenz. Seine protokollierte
Lektüre bleibt bei Code und den anwendbaren UI-
Referenzen. Opus öffnet keine zusätzliche Referenz.
Der Viewer-Vergleich beobachtet keine unabhängige
Lesersitzung in den vier Läufen.

Sol braucht 1,34× Zeit und 3,21× Tokens ohne
Cache-Lesezugriffe. Seine beobachteten Werkzeugausgaben
umfassen 130.503 gegenüber 48.157 Zeichen. Der Kandidat
ersetzt im nativen Rust-Reader die wiederholte
Vektorsuche durch die für die Duplikatprüfung ohnehin
gebildete Menge. Der Befund stammt aus dem Quelldiff.
Der Chrome-Replay prüft das Frontend und führt den
nativen Rust-Pfad nicht aus. Opus benötigt 1,32× Zeit
und 2,00× Tokens ohne Cache-Lesezugriffe.

Im ursprünglichen Auswahlfall erreicht Opus mit v69
10/11. Chrome beobachtet den Wechsel `1 → 2 → 2` bei
Teilantwort und anschließendem Netzwerk- oder Serverfehler.
Die Opus-Kontrolle zeigt `1 → 1 → 1`. Ihr Rohwert 2/11 und
die getrennte Nachprüfung 11/11 behalten die dokumentierte
Unterscheidung für den fehlenden Dokumentwurzel-Stub.
Die Gegenprobe setzt auf einer getrennten Kopie nur den
Auswahlzustand der abgetrennten Option vor deren Einfügen
zurück. Sie besteht in Chrome und im ursprünglichen
Offline-Prüfer mit 11/11 einschließlich der drei
Skalierungsprüfungen. Die Originalprodukte und -scores
bleiben gebunden. Die bereits einschlägige UI-Regel war
verfügbar. Eine Lektüre ist im Opus-Lauf nicht belegt.
Sol und Opus auf high empfehlen, eine mögliche
Routenwirkung getrennt von der Browserursache zu prüfen.
Die Belege liegen unter `v69-selection/EXPERIMENT.md`.

Sol besteht im selben Fall beidseits mit 11/11 und erhält
die Auswahl in Chrome. Mit Skill steigt die Modellzeit
von 523,66 auf 905,90 Sekunden, die Tokens ohne Cache-Lesen
von 105.631 auf 173.998. Für die zusätzlichen rund 382
Sekunden entfallen rund 62 auf längere beobachtete
Werkzeugintervalle. Eine unabhängige Lesersitzung ist in
diesem Paar nicht beobachtet. Die vollständigen vier
Produkte sind im dortigen Roharchiv gebunden.

In einer getrennten Opus-Diagnose liegt der unveränderte
UI-Einstieg zusätzlich direkt im Kontext. Der ursprüngliche
Bewerter ergibt 11/11. Chrome hält die Auswahl in beiden
Fehlerzweigen. Der Code setzt den Zustand der abgetrennten
Option vor dem Wiedereinfügen zurück. Dieses Einzelprodukt
stützt die Zustellhypothese für den bekannten Pfad. Es trägt
noch keine allgemeine Änderung am Routing. Die Diagnose
und der getrennte Viewer-Versuch stehen unter
`v69-ui-delivery/EXPERIMENT.md`.

Die unabhängig erstellte Aufgabe R20 prüft den bestehenden
serverseitigen Berichtsversand. Sie benennt die gewünschte
einmalige Aufbereitung der Gesamtmenge. Die Kalibrierung
trennt den funktional korrekten Gegenentwurf mit 10/12
von der Referenz mit 12/12. Alle vier Modellprodukte
erreichen 12/12 und zählen bei 8.334 projizierten Befunden
je eine vollständige Sortierung und Kodierung. Opus läuft
180,08 und 192,36 Sekunden ohne bzw. mit Skill. Sol läuft
279,38 und 308,78 Sekunden. Die Tokens ohne Cache-Lesen
erreichen die Faktoren 1,24 für Opus und 1,06 für Sol.
Aufgabenbindung, Kalibrierung und Roharchiv stehen unter
`v69-independent-r20/EXPERIMENT.md`.

Der Einzelregelabgleich in `REGELABGLEICH-CODE-V69.md`
verbindet die elf gemeinsamen Kriterien und die sechs
Schlussfragen mit ihren konkreten Prüfgrenzen. Er hält
auch die unterschiedliche Auslösung der unabhängigen
Lesung in ADR-0239 und der gemessenen Fassung fest. Die
Aufwandsspur oder ein grüner Produkttest beantworten
diese Verfahrensfrage jeweils nur teilweise.

### v70 · Gemeinsame Zustandsregel am verantwortlichen Besitzer

Der getrennte Viewer mit direkt bereitgestelltem UI-Einstieg
besteht bei Opus 7/7 und Chrome. Seine Modellzeit beträgt
114,95 statt 99,72 Sekunden für reguläres v69. In R1 zeigte
dieselbe Zustellung einen beobachteten Funktionsgewinn. Diese
Diagnosen lassen den Beitrag einzelner Sätze offen.

v70 kürzt die bereits im Code-Kontext verfügbare gemeinsame
Regel 9 von 1.899 auf 1.521 Bytes. Sie benennt, dass ein
Framework indirekt Zustand ändern kann. Die Regel erhält
Zuweisungen und Effekte bei Teilschritt und Fehler am Besitzer,
ohne zur Wiederherstellung die ganze Sammlung erneut zu
durchlaufen. Die gesonderten UI- und Reader-Routen bleiben
in der technischen Paketprüfung bytegleich. Die Shared-
Paketprüfung kontrolliert den direkten Review-Zugang und
den Wegfall des breiten Querverweises in der Umsetzung.
Die Messung der unveränderten R1-, Viewer- und R2-Aufgaben
mit den passenden Kontrollen folgt unter `v70-live-state`.

In R1 hält der reguläre Opus-Kandidat die Auswahl nach
Wiedereinfügen und Fehler. Beide Sol-Arme halten sie auch.
Chrome bestätigt den Zustand für alle vier Produkte. In der
separaten Entfernungsprobe stellt der eingefrorene Ausgangsstand
die geöffnete Seite wieder her. Beide Sol-Produkte machen das
weiterhin. Die beiden Opus-Produkte behalten abweichende
Auswahlen. Der alte Opus-Rohwert der Kontrolle und seine
Nachprüfung mit vollständiger Dokumentwurzel bleiben getrennt.
Sols Modellzeit für R1 beträgt mit v70 682,67 Sekunden gegenüber
523,66 in der Kontrolle und 905,90 mit v69.

Alle vier Viewer-Produkte bestehen 7/7 und halten die vorhandenen
Nachfolgeanzeigen in Chrome. Sols native Verweisprüfung verwendet
im Diff das vorhandene `HashSet` der Duplikatsuche. Der separate
Browser-Replay prüft diesen Rust-Pfad nicht. Opus setzt einen
Sonnet-Leser ein, der keinen einschlägigen Defekt findet. Die
Modellzeitfaktoren gegenüber den Kontrollen betragen 1,61 und 1,62.
Die Tokens ohne Cache-Lesen liegen bei 2,08 für Sol und 3,27 für
Opus. Von 90.215 solchen Opus-Kandidatentokens entfallen 27.259
auf den separat verknüpften Leser. Das Hauptmodell bleibt in
allen Hauptnachrichten Opus 5.5. Die UI-Belege sind archiviert.

Opus besteht in R2 beidseits 37/37, einschließlich der später
gelesenen Zeile. Die zurückgehaltenen Teilgruppen zeigen in beiden Armen
ungefähr vierfache Arbeit bei vierfacher Eingabe. In einer
separaten verzweigten Form mit 768 Stufen liegen bei einer Anfrage
die zusätzlichen Speicherspitzen bei 22,4 MB mit Skill und
3,2 MB ohne Skill. Der Kandidat hält vollständige Zwischenmengen
bei mehr als einem Verbraucher im Graphen. Bei zwei Anfragen
liegen die Spitzen bei 22,5 MB mit und 57,5 MB ohne Skill.
Die begrenzte Referenz benötigt in beiden Fällen rund 6,3 MB.
Der einzelne Speichernachteil bleibt trotz grünem Rohscore offen.
Sol besteht beidseits 37/37. Im verzweigten Einzelabruf liegen
beide Sol-Speicherspitzen rund bei 6,6 MB. Der Kandidat hält große
Vereinigungen als Kanten, bis ein Aufrufer die fertige Liste braucht.
Seine Modellzeit beträgt 651,47 Sekunden gegenüber 342,42 ohne
Skill. Die vollständigen Original- und Zusatzdaten liegen unter
`v70-live-state-r2/EXPERIMENT.md`.

### v71 · Umfang und Lebensdauer gehaltener Zwischenstände

In einer separaten Produktkopie mit vorab aufgezeichnetem Verbrauch
sinkt die Opus-Speicherspitze im verzweigten Einzelabruf von 22,3
auf 5,6 MB. Die Freigabe nach dem beobachteten letzten Zugriff und
das Überspringen ungenutzter Cache-Einträge sind die einzigen
Algorithmusänderungen dieser Gegenprobe. Die Aufrufzahl und die
fertigen Ergebnislisten bleiben gleich. Die Probe zeigt reale
interne Wiederverwendung innerhalb eines einzelnen Abrufs und
zugleich Zwischenmengen, die später nie gelesen werden.

v71 präzisiert den letzten Aufzählungspunkt der gemeinsamen Regel 7.
Der Text verbindet tatsächlich benötigte Zwischendaten mit ihrer
gleichzeitigen Größe und Lebensdauer, einschließlich gemeinsam
genutzter Arbeit in einem Aufruf. Eine Fallbeschreibung oder
allgemeine neue Prüfroutine wird nicht eingeführt. Opus und Sol auf
high haben die Ursache und die Grenzen der Empfehlung beurteilt.
Alle vier Paketprofile enthalten nur diesen Textwechsel. Die
lokalen 101 Shared- und 33 Runtime-Tests bestehen. Ein Runtime-Test
ist übersprungen. Der unveränderte R2-Fall und der unabhängige R20-
Berichtsversand prüfen den regulären Code-Ablauf gegen die passenden
Kontrollen unter `v71-shared-lifetime`.

## Vergleich v43 auf medium

Der lokale Vergleich v43 (Suite `2ab59fb`, Shared `84322fb`) verwendet
gpt-6.1-sol und Claude Opus 5.5 mit identischen, eingefrorenen
Aufgaben je Vergleich und passenden Kontrollen ohne Scoville-Skills.
Alle 14 Kandidatenläufe für die bekannten Diagnosefälle sind auswertbar.
Die Bestandsfälle R14 und R15 wurden getrennt ausgeführt.

- **R2.** Sol erreicht zweimal 35/35. Opus erreicht einmal 35/35
  und einmal 34/35. Der zweite Kandidat übersieht die Eignungsprüfung
  des erneut geladenen Datensatzes wie seine Kontrolle. Derselbe
  Kandidat schließt separat zwei vom realen Parser akzeptierte Formen
  durch einen engeren Vorfilter aus.
- **N11.** Beide Modelle korrigieren die volle Gutschrift in beiden
  Läufen. Beide Sol-Produkte und ein Opus-Produkt vermeiden
  quadratische Positionsarbeit. Der andere Opus-Kandidat optimiert
  einen anderen Ausgabezweig und lädt im JSON-Pfad mehrfach alle
  Positionen derselben Ursprungsrechnung. Alle drei Kontrollen
  behalten diese Wiederholung. Der fachlich nicht eindeutig bestimmte
  Rundungsfall bei mehreren Teilgutschriften bleibt im Rohscore.
- **R1 und N1.** Chrome bestätigt bei Opus R1 den Verlust der Auswahl
  beim Einfügen einer vorher getrennten Option. Sol und die drei
  passenden Kontrollen halten die Auswahl. In N1 erreichen beide
  Modelle mit und ohne Skill 9/9. Die separate Probe mit einem alten
  Programm zeigt Datenverlust in der Sol-Kontrolle. Die beiden
  Kandidaten und die Opus-Kontrolle halten die Daten beim alten
  Speicheraufruf geschützt.
- **R13.** Alle fünf Produkte bestehen 17/17. Beim erneuten Queueing
  setzen beide Kandidaten und zwei Kontrollen den Default eines
  ursprünglich explizit leer gelassenen Feldes ein. Eine Kontrolle
  erhält die Auslassung und den Aufgabenhash. Der Opus-Kandidat
  erkennt zusätzlich eine engere Obergrenze schon beim Erfassen der
  Scan-Konfiguration. An der Queue weisen alle fünf den ungültigen
  Wert ab. Ein Vorteil der früheren Prüfung für Pfade ohne Queue
  hängt von der Katalogidentität und der Erreichbarkeit des Falles ab.
- **R15.** Die unabhängige Änderung im bestehenden Viewer prüft mit
  echtem Chrome sichtbaren Zustand und die Zahl laufender Scans.
  Alle acht Läufe bestehen 8/8. Bei 6, 12 und 24 gespeicherten
  Projekten zählt der Beobachter in allen vier Kontrollen und
  einem Opus-Kandidaten 36, 144 und 576 Kartenbesuche beim
  Anwenden der Einzelantworten. Beide Sol-Kandidaten und der
  zweite Opus-Kandidat vermeiden diese Kartenbesuche. Eine isolierte
  Korrektur am Kandidaten ersetzt diese Durchläufe und die
  Mitgliedschaftssuche durch einen Index. Alle acht
  ursprünglichen Szenarien und drei größere Proben bestehen.
  Svelte-interne Aktualisierungen und Tauri-Laufzeit gehören
  nicht zum gemessenen Aufwand.
- **R14.** Beide Sol-Kandidaten bestehen 10/10 und verwenden in der
  Modulsperre nur die Zeilen des betroffenen Moduls. Der erste
  Opus-Kandidat erreicht wie die beiden Opus-Kontrollen 8/10.
  Bei 4, 12 und 36 Modulen zählt der Beobachter jeweils 220, 1.044
  und 6.588 Operationen. Die Modulsperre besucht weiterhin sämtliche
  Zeilen je beobachteter Gruppe. Die zweite Opus-Sitzung endete
  beim Aufbau der OAuth-Anmeldung und erhielt keinen Score.

In N11 liegen Zeit und Tokens einschließlich Cache und Leser bei beiden
Modellen über dem Wert der Kontrollen. Relativ zum Mittel der jeweils
passenden Kontrollen sind es bei Sol 2,52× Zeit und 3,93× Tokens, bei
Opus 3,60× und 4,89×. In R13 verbraucht der Opus-Kandidat schon bis zu
seinem Leseraufruf über doppelt so viele Eingabetokens wie die gesamte
Kontrolle. Die Laufspuren trennen Nutzeraufgabe, Autorarbeit und Leser.
Sie erlauben keine Zuordnung des gesamten Mehraufwands zu einer Regel.

Suite `9e5f5dc` und Shared `438686c` präzisieren Regel 7 und Frage 1.
Die Leseprüfung folgt jedem betroffenen Ausgabezweig bis in unveränderte
Helfer. Sie betrachtet Aufrufzahl mal bearbeitete Datenmenge. Die
tatsächliche Grenze einer Menge begrenzt weitere Dimensionen nur, wenn
der Aufrufpfad das stützt. Die technische Prüfung besteht in vier
Paketvarianten. Die modellbezogene Gegenprüfung der Präzisierung und
die Abnahme von W-005 bleiben offen.

Suite `f29549a` und Shared `7968f8e` bilden den kombinierten
Kandidaten v45. Die konkrete Eingabe und das vom Verbraucher
beobachtete Ergebnis werden vor der Entwurfswahl ermittelt.
Das gilt für separat gelesene Daten, erhaltenen Zustand und
bereits gespeicherte Werte. Die gemeinsame Regel verlangt,
eine bisher gültige Konfiguration auch mit fehlender neuer
Einstellung verwendbar zu halten. Die zwölf
technischen Checks und vier Paketvarianten sind verifiziert.
Die Modellabnahme verwendet auch für v45 die unveränderte
R14-Aufgabe und ihre vorhandenen Kontrollen.

## Übernahme durch Fable 5.2: Leseprüfungen, realistische Mengen und unabhängige zweite Lesung (v29 bis v38)

Stand dieses Abschnitts 2026-11-17. Er dokumentiert die historischen Kandidaten v29 bis v38.

### Ausgangslage und Änderung

Bis v28 war der Code-Skill in sechzehn Fassungen gegen dieselben Diagnosefälle geschärft worden. Zuletzt verlangte er, eine Arbeitsgrenze durch Zählen am Einstiegspunkt samt Gegenfassung zu beweisen. Die als quadratisch gewertete Arbeit in R2 blieb trotzdem in beiden Armen, und die Modellzeit lag mit Skill beim rund Zweieinhalbfachen der Läufe ohne Skills.

Seit v29 bestehen die gemeinsamen Code-Kriterien aus dreizehn kurzen Regeln, die am gelesenen Quelltext geprüft werden, und sechs Fragen zum betroffenen Pfad. Das Beweisverfahren ist entfallen. Der Hauptagent hat die Texte selbst geschrieben; Skillwriter wurde nicht verwendet. Zwei Befunde haben die Form bestimmt:

- **Gestellte Frage gegen gelesene Frage.** Dieselbe gezielte Frage wird richtig beantwortet, wenn sie der Auftrag ist, und übergangen, wenn sie nur im Skill steht. Deshalb schreibt der Autor die Antworten auf die Fragen 1 bis 3 (wiederholte Arbeit, erneut geladener Wert, Zustand und Effekte) mit Datei und Zeile in den Abschlussbericht. Das ist die eine Berichtspflicht, die ADR-0237 als gemessene Ausnahme zulässt.
- **Gerichtete Diagnose der R2-Arbeit.** Die verbliebene Arbeit in R2 ist ein Durchlauf im Speicher über die gemeinsam genutzten Quellen einer Seite. Der einzige Aufrufer übergibt die Bausteine einer Seite; die Arbeitsprobe mit 576 Anfragen erreicht kein realer Aufrufer.

### Entscheidungen des Eigentümers

Der Eigentümer hat am 2026-11-15 entschieden ([ADR-0237](../decisions/0237-wiederholte-arbeit-an-realistischen-mengen-messen.md)):

- Wiederholte Arbeit wird an den Mengen gemessen, die die tatsächlichen Aufrufer übergeben können. Eine Abfrage, ein Lesezugriff oder ein Parse je Element wird schon bei mäßigen Mengen beseitigt; Arbeit im Speicher über wenige Elemente ist kein Mangel.
- Vorhandene Logik wird bevorzugt, außer ihre Nutzung macht die Arbeit quadratisch, wiederholt Abfragen je Element oder braucht mehr Hüllen als eine schlichte Umsetzung.

Damit ist die R2-Arbeitsprobe mit 576 Anfragen Kontext und kein Abnahmekriterium mehr, und die Teilnehmersuche in N1 ist kein Mangel. Abnahmerelevant bleiben in R2 die Funktion, der später gelesene Wert, die Parserformen und das Dateiformat, in N11 die Abfragen je Gutschrift.

### Aufbau der Messung

Alle Runden verwenden die eingefrorenen Aufgaben, Bewerter und passenden gespeicherten Kontrollen ohne Skills aus den früheren Runden (R2: je drei aus v14; R1: je zwei aus v17 und v18; N1 und N11: je zwei). Je Modell laufen R2 und R1 dreimal, N1 und N11 einmal. Sol 6.1 läuft `medium`, Opus 5.5 `high`. Im Skill-Arm steht der vollständige Code-Skill im Auftrag. Neue Kontrollen liefen bis v34 nicht; in v35 kamen drei Opus-Kontrollen für R1 hinzu, und die frische Aufgabe R13 hat eigene Kontrollen. R1 wird zusätzlich mit dem kalibrierten DOM-Prüfsatz und einer Chrome-Probe bewertet, die die Auswahl nach den Teilantworten liest.

| Runde | Suite / Shared | Änderung gegenüber der Vorrunde |
| --- | --- | --- |
| v29 | `92a3b2c` / `b055015` | Leseprüfungen und sechs Fragen statt des Beweisverfahrens |
| v30 | `6f4a422` / `fb2276f` | Realistische Mengen, Grenze der Wiederverwendung, Antworten 1 bis 3 im Bericht |
| v31 | `119be5a` / `0d2ea50` | Formen eines Vorfilters aus der exakten Prüfung lesen; Zustandsantwort nennt ihren Test |
| v32 | `9a6d0bf` / `341219a` | Widerspruchsprüfung aller neun Skills; ungeprüftes Nachladen ist ein Mangel |
| v33 | `fde60ef` / `d230895` | Zustand an dem, was der neue Pfad ändert, wird erhalten oder wiederhergestellt und getestet |
| v34 | `2902202` / `8e239b8` | Ein Test gilt der Prüfung, die Antwort 2 für einen erneut geladenen Wert nennt; Frage 2 erfasst auch Helfer; ein Test ersetzt die erhaltende Operation nicht |
| v35 | `901460b` / `efcce4a` | Zugewiesener Zustand wird nach jedem Schritt erneut gesetzt; die Ausnahme für wenige Elemente braucht eine benannte Grenze |
| v36 | `913dd2c` / `ba1aff4` | Unabhängiger Leser für die Fragen 2 und 3; Regel 9 nennt den Träger des zugewiesenen Zustands |
| v37 | `254628f` / `b6dddab` | Reviewer mit den vollen Review-Regeln, Fragen 2 und 3 zuerst; kein zweites Review unter Workflow |
| v38 | `3683362` / `b6dddab` | Zurück zum Leser für die Fragen 2 und 3; auf seine Antwort warten; kein absichtlich fehlschlagender Test |

Kandidat v34 enthält außerdem die Textänderungen an Cleanup, Workflow und Setup aus den Eigentümerentscheidungen vom 2026-11-16 (`622ca13`); der Code-Skill und die gemeinsamen Kriterien sind davon nicht berührt.

In v29 und v30 liefen wegen einer abgelaufenen Anmeldung nur die Sol-Läufe und in v29 ein Opus-Lauf vollständig; die gescheiterten Opus-Starts sind als Ausführungsfehler ausgesondert (`OPUS-AUTH-FAILURES.json`) und zählen nicht.

### Widerspruchsprüfung aller Skills

Auf Auftrag des Eigentümers haben fünf getrennte Opus-5.5-high-Prüfer die gebauten Pakete aller neun Skills auf Regeln untersucht, die sich widersprechen. Die fünf Berichte führen 56 nummerierte Befunde. Fünf Korrekturagenten mit getrennten Dateibereichen haben sie an den Quellen behoben; der Hauptagent hat die Diffs geprüft. Zwei Befunde wurden verworfen, weil die Situation nicht eintreten kann. Drei betrafen Absichten, die nur der Eigentümer entscheiden kann; er hat sie am 2026-11-16 entschieden (siehe unten). Die Gesamtprüfung bestand danach 12 von 12. Berichte und Aufträge liegen unter `joint-consultation-20261115/v32-contradiction-review/`.

### Ergebnisse v31 und v32

| Prüfung | Sol v31 | Sol v32 | Opus v31 | Opus v32 | Kontrollen ohne Skills |
| --- | --- | --- | --- | --- | --- |
| R2 Funktion (35 Prüfungen) | 35, 35, 35 | 35, 35, 35 | 34, 34, 35 | 35, 35, 34 | siehe v14 |
| R2 später gelesener Wert geprüft | 3 von 3 | 3 von 3 | 1 von 3 | 2 von 3 | – |
| R2 Parserformen | 3 von 3 | 3 von 3 | 2 von 3 | 3 von 3 | – |
| R2 Dateiformat erhalten | 3 von 3 | 3 von 3 | 3 von 3 | 3 von 3 | – |
| R1 kalibriert (11 Prüfungen) | 11, 11, 10 | 11, 11, 11 | 10, 10, 11 | 9, 10, 11 | 11, 10 (Sol); 11, 11 (Opus) |
| R1 Auswahl bleibt in Chrome erhalten | 2 von 3 | 3 von 3 | 1 von 3 | 1 von 3 | 4 von 4 |
| N1 (9 Prüfungen), alte Fassung sicher | 9, ja | 9, ja | 9, ja | 9, ja | – |
| N11 (11 Prüfungen) | 11 | 10 | 10 | 10 | – |
| N11 erzeugte Positionsobjekte der JSON-Liste bei 8, 32 und 128 Gutschriften zu einer Rechnung | 24, 96, 384 | 16, 64, 256 | 88, 1.120, 16.768 | 80, 1.088, 16.640 | – |

Der in N11 fehlende Punkt ist jeweils der widersprüchliche Rundungsfall, den der Auftrag nicht entscheidet. In v30 hatten zwei von drei Sol-Läufen eine gültige qualifizierte Blockform übersehen, weil die Regel zwei verschiedene Quellen für die Formen eines Vorfilters nannte; nach der Korrektur in v31 bestehen alle sechs Sol-Läufe aus v31 und v32 die Parserformen.

Sol erfüllt in v32 alle abnahmerelevanten Prüfungen der vier Diagnosefälle. Bei Opus blieben zwei Befunde:

- **Auswahlverlust in R1.** Mit Skills springt die Auswahl in vier von sechs Opus-Läufen (v31 und v32) auf einen anderen Eintrag, in den zwei Opus-Kontrollen in keinem. Die Autoren nennen die Zuweisung des alten Pfads im Bericht und begründen, warum sie entfallen kann.
- **Abfrage je Gutschrift in N11.** Der Opus-Autor nennt die verbliebenen Abfragen je Rechnung im Bericht und lässt eine als „klein" stehen.

### Mechanismus und Korrektur für v33

Sol 6.1 high und Opus 5.5 high haben die v32-Berichte und Diffs getrennt gelesen (`joint-consultation-20261115/v33-held-state-consultation/`). Beide widersprechen der ersten Lesart des Hauptagenten in einem Punkt und stimmen untereinander überein:

- Die Autoren ließen die Zuweisung weg, weil die geöffnete Seite von einer Teilantwort nicht berührt wird. Sie ordneten die Auswahl dem Eintrag zu und nicht der Liste, die sie nun selbst ändern. Ein abgehängter Eintrag, der noch als gewählt markiert ist, übernimmt beim Einfügen die Auswahl.
- Die Kontrollen ohne Skill ersetzen den vollen Durchlauf ebenfalls. Eine fand den Fehler durch ihren Test in Chrome, die andere vergleicht den Wert nach ihren Änderungen und setzt ihn neu. Die Tests der Skill-Autoren prüfen die Auswahl nach einem Einfügen nicht, auch dort, wo Chrome lief.
- Im Skill-Text begünstigen drei Stellen das Weglassen: Die Entscheidung über den Zustand fällt schriftlich vor dem Test; die Testpflicht galt nur dem Zustand, den der Autor als erhalten einstuft; Regel 10 wertet eine Zeile, die Zustand erneut setzt, als Schutz ohne Anlass.

Die Korrektur für v33 setzt an diesen drei Stellen an. Regel 9 trennt die Neuberechnung, die Regel 7 beseitigt, von dem Zustand, den sie hinterlassen hat. Zustand an dem, was der neue Pfad ändert, wird durch eine erhaltende Operation oder durch Lesen und Wiederherstellen am geänderten Element gehalten, und das ist ausdrücklich kein Schutz nach Regel 10. Die Testpflicht gilt dem Zustand des alten Pfads, auch wenn der Autor schließt, er könne sich nicht ändern. Frage 1 sagt, was aus der Antwort folgt: Eine Abfrage je Element, die ein Aufruf für alle ersetzen könnte, entfällt, außer die realen Aufrufer übergeben wenige Elemente oder eine Garantie wie Frische braucht sie.

### Ergebnisse v33 und v34

| Prüfung | Sol v33 | Sol v34 | Opus v33 | Opus v34 |
| --- | --- | --- | --- | --- |
| R2 Funktion (35 Prüfungen) | 35, 35, 35 | 35, 35, 35 | 34, 34, 35 | 35, 35, 35 |
| R2 später gelesener Wert geprüft | 3 von 3 | 3 von 3 | 1 von 3 | 3 von 3 |
| R2 Parserformen | 2 von 3 | 3 von 3 | 3 von 3 | 3 von 3 |
| R2 Dateiformat erhalten | 3 von 3 | 3 von 3 | 3 von 3 | 3 von 3 |
| R1 kalibriert (11 Prüfungen) | 11, 11, 11 | 11, 11, 10 | 11, 11, 10 | 11, 10, 10 |
| R1 Auswahl bleibt in Chrome erhalten | 3 von 3 | 3 von 3 | 2 von 3 | 1 von 3 |
| N1 (9 Prüfungen), alte Fassung sicher | 9, ja | 9, ja | 9, ja | 9, ja |
| N11 (11 Prüfungen) | 11 | 10 | 10 | 10 |
| N11 erzeugte Positionsobjekte bei 8, 32 und 128 Gutschriften | 16, 64, 256 | 16, 64, 256 | 16, 64, 256 | 80, 1.088, 16.640 |

**v33.** Die Abfrage je Gutschrift in N11 ist bei Opus beseitigt (ein Lauf). In R1 bleibt die Auswahl in fünf von sechs Läufen erhalten. Zwei Befunde blieben bei Opus, und zwei getrennte Opus-5.5-high-Analysen haben ihre Ursache an Berichten und Diffs isoliert:

- **Behauptete Prüfung in R2.** Zwei von drei Opus-Autoren schreiben in Antwort 2, die erneut geladenen Zeilen seien geprüft. Das stimmt nicht: Der Filter sitzt in der Abfrage der Kennungen, das Nachladen ohne Bedingung liegt in einem Helfer, den sie nicht geändert und nicht verfolgt haben. Einen Test verlangte der Skill nur, wenn der Autor eine Lücke schließt; wer eine Prüfung zu sehen glaubt, schrieb keinen.
- **Test statt erhaltender Zeile in R1.** Ein Opus-Autor fügt ohne Erhalten oder Wiederherstellen ein und begründet das damit, dass der Eintrag unberührt bleibt und sein Test die Auswahl prüft. Sein Test fügt den Eintrag mit der veralteten Markierung nie wieder ein. Die Testpflicht aus v33 („auch für Zustand, den der neue Pfad nach deinem Schluss nicht berühren kann") räumte genau den Schluss ein, den Frage 3 ausschließt.

Sol 6.1 high und Opus 5.5 high haben den Korrekturentwurf getrennt geprüft (`joint-consultation-20261115/v34-claimed-check-consultation/`). Übernommen sind: Der Test gilt dem beobachtbaren Ergebnis der erhaltenden Operation und ersetzt sie nicht; statt „ablehnen" heißt es, der Verbraucher verwendet den Wert nicht; die Ausnahme einer Garantie steht auch in Abschnitt 4; Frage 2 nennt die Helfer, die der Pfad aufruft. Ein Satz, der jeden gehaltenen Zustand testen ließ, ist als unbegrenzt gestrichen. Für das Fixture, das den Auslöser nicht enthält, gibt es keinen weiteren Textmechanismus.

**v34, Sol.** Alle abnahmerelevanten Prüfungen in R2 bestehen in allen drei Läufen, auch die Parserformen. Zwei Läufe liegen unter der vollen Punktzahl (`V34-SOL-ANALYSIS.md` im Rundenordner):

- **R1 Lauf 3** verliert einen anderen Zustand als den, den v33 und v34 behandeln: Wird der gewählte Eintrag entfernt, setzt der Autor die Auswahl außerhalb des vollen Durchlaufs nicht auf den Platzhalter zurück, und der Browser wählt einen anderen Eintrag. Das ist ein echter Fehler. Der Skill fragt nach genau diesem Fall; die Läufe 1 und 2 mit demselben Text behandeln ihn. Eine Sol-Kontrolle ohne Skills erreichte ebenfalls 10 von 11.
- **N11** lässt den Ein-Cent-Rest der getrennten Umsatzsteuerrundung offen. Der Autor hat ihn gefunden, nachgestellt und dem Nutzer als Frage vorgelegt, weil zwei Projektdokumente sich widersprechen. Der Fehler stammt aus dem geprüften Entwurf. Die beiden Sol-Kontrollen beheben ihn, die beiden Opus-Kontrollen nicht.

Keiner der beiden Befunde lässt sich auf die Änderung von v34 zurückführen, und keiner wiederholt sich in der Runde. Am Text wurde deshalb nichts geändert.

**v34, Opus.** R2 besteht in allen drei Läufen alle abnahmerelevanten Prüfungen; der später gelesene Wert ist in 3 von 3 geprüft (v33: 1 von 3). In R1 lassen alle drei Autoren die Zuweisung des alten Pfads weg und begründen das damit, dass die geöffnete Seite nicht verschoben wird. Die Chrome-Probe zeigt den Verlust in zwei Läufen; im dritten liegt die veraltete Markierung auf einem Eintrag, den die Probe nicht wieder einfügt, und die Nachstellung im kalibrierten DOM-Prüfsatz zeigt denselben Fehler (`V34-OPUS-ANALYSIS.md` im Rundenordner). In N11 bleibt die Abfrage je Gutschrift. Ein R1-Lauf brauchte 1.755 Sekunden, davon rund 1.070 Sekunden Wartezeit seines eigenen Testtreibers.

### Ergebnisse v35 und was fünf Fassungen bei Opus zeigen

v35 ließ Regel 9 den Wert, den der alte Pfad zugewiesen hat, nach jedem Schritt des neuen Pfads erneut setzen, Frage 3 die Zeile dafür verlangen und Frage 1 die Ausnahme für wenige Elemente an eine benannte Grenze binden. Der Entwurf ist mit Sol 6.1 high und Opus 5.5 high abgeglichen (`joint-consultation-20261115/v35-assigned-state-consultation/`).

| Prüfung | Sol v35 | Opus v35 |
| --- | --- | --- |
| R2 Funktion (35 Prüfungen) | 35, 35, 35 | 34, 34, 35 |
| R2 später gelesener Wert geprüft | 3 von 3 | 1 von 3 |
| R2 Parserformen | 3 von 3 | 3 von 3 |
| R1 kalibriert (11 Prüfungen) | 11, 11, 11 | 10, 10, 11 |
| R1 Auswahl bleibt in Chrome erhalten | 3 von 3 | 1 von 3 |
| N1 (9 Prüfungen), alte Fassung sicher | 1, dann 9 und 9 in zwei Wiederholungen | 9, ja |
| N11 (11 Prüfungen) | 10 | 9 |
| N11 erzeugte Positionsobjekte bei 8, 32 und 128 Gutschriften | 16, 64, 256 | 16, 64, 256 |

Der erste Sol-Lauf in N1 endete nach 37 Sekunden mit einer Rückfrage, obwohl der Auftrag im Prompt stand. Die Ausführung ist gültig und bleibt im Bestand; zwei Wiederholungen bestanden 9 von 9.

Weil die Auswahl in R1 mit Skill seltener erhalten blieb als in den zwei gespeicherten Opus-Kontrollen, liefen drei weitere Opus-Kontrollen ohne Skills, abgeglichen auf Auftrag, Startinventar, Runner, CLI und Bewerter (`CONTROLS-ADDED.md` im Rundenordner). Eine verliert die Auswahl ebenfalls, eine besteht nur 4 von 11 Prüfungen, eine besteht alles.

Opus über fünf Fassungen (v31 bis v35):

| Prüfung | ohne Skills | mit Skills je Runde | mit Skills gesamt |
| --- | --- | --- | --- |
| R2 später gelesener Wert geprüft | 0 von 3 | 1, 2, 1, 3, 1 von 3 | 8 von 15 |
| R1 Auswahl bleibt erhalten | 4 von 5 | 1, 1, 2, 1, 1 von 3 | 6 von 15 |
| N11 Abfrage je Gutschrift beseitigt | 0 von 2 | nein, nein, ja, nein, ja | 2 von 5 |

- Zwischen den Fassungen gibt es keinen Trend. Die Streuung zwischen zwei Runden mit gleichem Text ist so groß wie jeder Unterschied zwischen zwei Fassungen: Auf 3 von 3 in R2 (v34) folgte mit unverändertem Text 1 von 3.
- In R1 hält Opus die Auswahl mit Skill seltener als ohne. Bei diesen Zahlen ist der Unterschied nicht belegt (einseitiger exakter Test etwa 0,15).
- In jedem Fehllauf zeigt der Bericht, dass der Autor die Frage gelesen und die Stelle genannt hat und sich mit einem Argument dagegen entscheidet, das die Regel ausschließt.
- Sol erfüllt mit Skill den später gelesenen Wert in 15 von 15 Läufen, hält die Auswahl in 14 von 15 und löst N11 in 5 von 5 linear.

Der Regeltext begrenzt Opus hier also nicht. Dieselben Sätze ein weiteres Mal umzuformulieren wäre kein neuer Mechanismus.

### Unabhängige zweite Lesung: Probe, v36 und v37

**Probe.** Sechs frische Opus-5.5-high-Leser bekamen je einen fertigen Diff aus v35, den Arbeitsstand und die Kriterien, und als ganzen Auftrag die Fragen 2 und 3. Sie fanden das ungeprüfte Nachladen in 2 von 2 fehlerhaften R2-Diffs und ließen den richtigen gelten. Den Auswahlverlust fanden sie in 1 von 2 fehlerhaften R1-Diffs; der andere Leser übernahm das Argument des Autors. An einem richtigen R1-Diff bemängelte ein Leser Werte, die ein Schritt nicht berühren kann, weil Regel 9 den Träger des Zustands nicht nannte (`SECOND-READER-PROBE-OUTPUT.txt` im Rundenordner v35).

**Entscheidung.** Der Eigentümer hat danach entschieden, die zweite Lesung als Teil des Code-Skills zu erproben ([ADR-0239](../decisions/0239-zweite-lesung-fuer-nachgeladene-werte-und-zustand.md)). Der Hauptagent hatte empfohlen, v35 als Endkandidaten zu nehmen und den Opus-Rest als nicht behoben zu dokumentieren. Eine Selbstlesung ersetzt den Schritt nicht; die Pflicht gilt nur für Code; unter Scoville Workflow ist das Step-Review diese Lesung.

**Geänderte Ausführung.** Ab v36 dürfen die Opus-Läufe mit Skill das Agentenwerkzeug aufrufen; Sol konnte Unteragenten schon vorher starten. Die gespeicherten Kontrollen liefen ohne diese Erlaubnis (`EXECUTION-CHANGE.md` je Runde). Die eingefrorenen Aufträge von R1 und R2 schließen „weitere Beratungsmodelle" aus. Autoren, die deshalb keinen Leser starteten, sagen das im Bericht. Auf Entscheidung des Eigentümers lief deshalb zusätzlich eine gekennzeichnete Variante von R2 und R1, in der ein Satz einen lesenden Unteragenten desselben Modells erlaubt (`TASK-VARIANT.md`). Sie hat keine passenden Kontrollen.

| Runde | Form der zweiten Lesung |
| --- | --- |
| v36 | Leser, dessen ganzer Auftrag die Fragen 2 und 3 sind; Regel 9 nennt den Träger des zugewiesenen Zustands |
| v37 | Reviewer mit den vollen gemeinsamen Review-Regeln, Fragen 2 und 3 zuerst; kein zweites Review unter Workflow |
| v37S | wie v37, mit dem Auftragssatz, der den Leser erlaubt |

| Prüfung | Sol v36 | Sol v37 | Opus v36 | Opus v37 | Sol v37S | Opus v37S |
| --- | --- | --- | --- | --- | --- | --- |
| R2 Funktion (35 Prüfungen) | 35, 35, 35 | 35, 35, 35 | 35, 35, 35 | 35, 35, 35 | 35, 35, 35 | nicht bewertbar, 35, 35 |
| R2 später gelesener Wert geprüft | 3 von 3 | 3 von 3 | 3 von 3 | 3 von 3 | 3 von 3 | 2 von 2 gewerteten |
| R2 Parserformen | 3 von 3 | 3 von 3 | 3 von 3 | 3 von 3 | 2 von 3 | 1 von 2 gewerteten |
| R1 kalibriert (11 Prüfungen) | 11, 11, 11 | 11, 11, 11 | 10, 11, 11 | 11, 11, ein Lauf mit Zeitüberschreitung | 11, 9, 11 | 10, 11, 11 |
| R1 Auswahl bleibt in Chrome erhalten | 3 von 3 | 3 von 3 | 2 von 3 | 2 von 2 gewerteten | 3 von 3 | 2 von 3 |
| N1 (9 Prüfungen), alte Fassung sicher | 9, ja | 9, ja | 9, ja | 9, ja | – | – |
| N11 (11 Prüfungen) | 9 | 9 | 10 | 10 | – | – |
| N11 Abfrage je Gutschrift beseitigt | ja | ja | ja | ja | – | – |

Den Leser oder Reviewer gestartet haben unter den eingefrorenen Aufträgen: Opus in R1 zwei (v36) und drei (v37) von drei Läufen, in R2 keiner; Sol in R1 und R2 keiner; in N1 und N11 beide Modelle in jedem Lauf. In der Variante starteten ihn alle zwölf Autoren.

Was die zwei Formen zeigen (Einzelheiten und Belege in `V36-V37-ANALYSIS.md` im Rundenordner v37; die Ursachen haben fünf lesende Opus-5.5-high-Analysen an Berichten, Diffs und Ereignisströmen isoliert):

- **Der Leser nur mit den zwei Fragen (v36)** wurde in sechs Läufen gestartet. Kein Fehler ist auf ihn zurückzuführen, und er fand zwei echte: eine fehlende Zuweisung in Opus R1 und eine gerundete Dezimalsumme in Opus N1. Der Opus-R1-Lauf ohne Leser verlor die Auswahl.
- **Das volle Review (v37, v37S)** half, wo sein Befund die Fragen 2 und 3 oder einen echten Mangel betraf. Seine übrigen Befunde setzten die Autoren ebenfalls um, und zwei solche Korrekturen beschädigten eine vorher richtige Änderung:
  - In einem Sol-R1-Lauf der Variante bestand der Stand vor dem Review alle Prüfungen. Der Reviewer meldete die Zuweisung als Leistungsbefund; der Autor ersetzte sie und passte das DOM-Modell seines eigenen Tests an. Ergebnis 9 von 11.
  - In einem Opus-R2-Lauf der Variante übernahm der Autor einen als „Low" eingestuften, ausgeschriebenen `REGEXP`-Vorschlag. Die Testdatenbank des Bewerters wertet `REGEXP` nicht aus und meldet eine Grenze des Messaufbaus; der Lauf ist nicht bewertbar. Keine der neun Änderungen nach dem Review betraf einen Mangel der Änderung.
- **Unabhängig vom Umfang:** Zwei von sechs Opus-R1-Autoren mit Reviewer starteten ihn im Hintergrund und setzten einen Weckruf nach 1200 Sekunden. Ein Lauf überschritt die Zeitgrenze von 1800 Sekunden und ist nicht gewertet, einer endete 47 Sekunden davor. Sol hinterlegte in N11 in beiden Runden die offene Rundungsfrage als absichtlich fehlschlagenden Test und übergab eine rote Suite.
- **Opus R1 der Variante, Lauf 1:** Der Fehler stand vor dem Review im Code. Der Reviewer nannte das Symptom nur für den Fall, dass ein Eintrag entfernt wird, und der Autor behob nur diesen Fall.

### Endkandidat v38

Der Eigentümer hat am 2026-11-16 nach diesen Ergebnissen entschieden, im eigenständigen Code-Skill zum Leser nur mit den Fragen 2 und 3 zurückzugehen. Unter Workflow bleibt das volle Step-Review, und jeder Reviewer mit den gemeinsamen Review-Regeln beantwortet die Fragen 2 und 3 zuerst. v38 ergänzt zwei Sätze, hinter denen je ein gemessener Fehler steht: Der Autor wartet auf die Antwort des Lesers über die Warte-Funktion oder Fertigmeldung des Hosts und nicht mit einem zeitgesteuerten Weckruf; und er übergibt keinen absichtlich fehlschlagenden Test, sondern stellt oder berichtet die offene Frage. Sol 6.1 high und Opus 5.5 high haben den Wortlaut gegengeprüft; übernommen und nicht übernommen steht mit Begründung in `joint-consultation-20261115/v38-reader-wait-consultation/RECONCILIATION.md`.

| Prüfung | Sol v38 | Opus v38 | Sol v38S | Opus v38S |
| --- | --- | --- | --- | --- |
| R2 Funktion (35 Prüfungen) | 35, 35, 35 | 35, 35, 35 | 35, 35, 35 | 35, 35, 35 |
| R2 später gelesener Wert geprüft | 3 von 3 | 3 von 3 | 3 von 3 | 3 von 3 |
| R2 Parserformen | 3 von 3 | 3 von 3 | 3 von 3 | 3 von 3 |
| R2 Dateiformat erhalten | 3 von 3 | 3 von 3 | 3 von 3 | 3 von 3 |
| R1 kalibriert (11 Prüfungen) | 11, 11, 11 | 11, 11, 11 | 11, 11, 11 | 11, 11, 11 |
| R1 Auswahl bleibt in Chrome erhalten | 3 von 3 | 3 von 3 | 3 von 3 | 3 von 3 |
| R1 Zusatz: gewählter Eintrag wird ausgefiltert | 3 von 3 | 3 von 3 | 3 von 3 | 3 von 3 |
| N1 (9 Prüfungen), alte Fassung sicher | 9, ja | 9, ja | – | – |
| N11 (11 Prüfungen) | 11 | 9 | – | – |
| N11 erzeugte Positionsobjekte bei 8, 32 und 128 Gutschriften | 16, 64, 256 | 88, 1.120, 16.768 | – | – |

Alle 28 Läufe sind gültig. Den Leser gestartet haben unter den eingefrorenen Aufträgen Opus in R1 in drei von drei Läufen, in R2 in keinem, Sol in R1 und R2 in keinem, beide Modelle in N1 und N11; in der Variante alle zwölf Autoren.

- **Opus R1.** Die Auswahl bleibt in 6 von 6 Läufen erhalten, jeder mit Leser, und alle sechs bestehen auch den Zusatz mit dem ausgefilterten Eintrag. Über v31 bis v35 waren es 6 von 15.
- **Opus R2.** Der später gelesene Wert ist in 6 von 6 Läufen geprüft, drei davon ohne Leser. Zusammen mit v36 und v37 sind das 12 von 12 Läufe unter dem eingefrorenen Auftrag ohne Leser; vor dem Absatz waren es 8 von 15. Was daran den Unterschied erklärt, ist nicht gezeigt.
- **Warten.** Von elf Opus-Läufen mit Leser warteten acht im Vordergrund. Drei Leser liefen asynchron; zwei dieser Autoren setzten noch einen Weckruf als Rückfall und nahmen ihn zurück, als die Fertigmeldung kam. Kein Lauf verlor Zeit; der längste Opus-Lauf dauerte 967 Sekunden.
- **Sol N11.** 11 von 11 mit bestehender Suite; der absichtlich rote Test tritt nicht mehr auf. Ein Lauf.
- **Sol** besteht in allen 14 Läufen jede Prüfung der vier Diagnosefälle.

**Nicht behoben: Opus N11** (ein Lauf, 9 von 11; `V38-ANALYSIS.md` im Rundenordner). Der Rundungsfehler bei voller Gutschrift und die Abfrage je Gutschrift stammen aus dem vorgegebenen Entwurf und standen vor der Antwort des Lesers im Code. Den Rundungsfehler hat der Autor gemessen, aber nicht auf das Vorzeichen zurückgeführt und nicht berichtet. Den Ein-Cent-Rest nach Teilgutschriften, bei dem sich zwei Projektdokumente widersprechen, legt er als Entscheidung vor. Die Abfragen nennt seine Antwort auf Frage 1 und lässt sie stehen, weil sie „sich ins vorhandene Muster fügen"; das ist nicht die benannte Grenze, die Frage 1 verlangt. Über alle Fassungen seit v31 beseitigte Opus diese Abfrage mit Skill in 4 von 8 Läufen, ohne Skills in 0 von 2. Der Leser prüft Frage 1 nicht. Der Hauptagent rät davon ab, ihn darauf auszuweiten, weil in v37 ein Leistungsbefund eine richtige Änderung beschädigt hat.

### Frische unabhängige Aufgabe R13

Die Aufgabe hat ein unabhängiger Autor in einer vorhandenen größeren Codebasis geschrieben (WordPress-Plugin, 498 verfolgte Dateien, 52.321 Textzeilen) und als Archiv versiegelt (SHA-256 `9728db83…65c57`). Der Hauptagent hat die Prüfsumme bestätigt, das Archiv per `receipt.json` an den Endkandidaten v38 gebunden und es erst danach geöffnet. Der Auftragstext ist unverändert (SHA-256 `936cb673…cc512`).

Der Bewerter des Archivs hat 17 Prüfungen, 12 zum verlangten Verhalten und 5 zum erhaltenen. Seine Kalibrierung ließ sich hier nachstellen: Der unveränderte Stand besteht 5 von 17, die Referenzlösung und eine alternative richtige Lösung 17 von 17, und jede der fünf absichtlich falschen Fassungen fällt so durch, wie der versiegelte Nachweis sagt. Je Modell laufen zwei Läufe mit dem vollständigen Code-Skill und zwei ohne Skills, mit gleicher Ausführung in beiden Armen einschließlich der Erlaubnis, einen getrennten Agenten zu starten.

| Lauf | Prüfungen | Sekunden | Geänderte Quelldateien | Zeilenenden erhalten |
| --- | --- | --- | --- | --- |
| Sol mit Skill 1 | 17 von 17 | 801 | 11 | ja |
| Sol mit Skill 2 | 17 von 17 | 475 | 3 | nein, drei Dateien von LF auf CRLF |
| Sol ohne Skills 1 | 17 von 17 | 214 | 3 | ja |
| Sol ohne Skills 2 | 17 von 17 | 320 | 5 | ja |
| Opus mit Skill 1 | 14 von 17 | 618 | 4 | ja |
| Opus mit Skill 2 | 17 von 17 | 499 | 5 | ja |
| Opus ohne Skills 1 | 17 von 17 | 249 | 4 | ja |
| Opus ohne Skills 2 | 17 von 17 | 240 | 4 | ja |

**Opus (2026-11-17, Stand v38).** Alle vier Läufe sind gültig. Die drei nicht bestandenen Prüfungen des ersten Skill-Laufs sind kein Fehler im Ergebnis: Der Lauf ergänzt unter dem Zahlenfeld einen Hinweis auf den zulässigen Bereich und formatiert die Grenzen darin mit der WordPress-Funktion `number_format_i18n()`, die das Plugin an acht Stellen selbst benutzt. Das Testgerüst des Bewerters stellt diese Funktion nicht bereit, deshalb bricht die Darstellung dort ab (dreimal derselbe Fehler in `observer-runs/opus-R13-candidate-1/scorer-stdout.json`). Mit einer Ersatzfunktion im Gerüst bestehen alle drei Prüfungen (lesende Analyse eines Opus-5.5-high-Agenten; das fehlende Gegenstück und die Fehlermeldung hat der Hauptagent nachgelesen, den Lauf mit Ersatzfunktion nicht wiederholt). Der Bewerter bleibt unverändert; der Lauf zählt im Bericht als 14 von 17 mit dieser Erklärung. Der Hinweis selbst geht über den Auftrag hinaus; ihm gingen das Laden von Scoville UI und dessen Hinweise zu Eingabeformaten und zur Zahlenformatierung voraus, der zweite Skill-Lauf las dasselbe und ergänzte nichts. Kein Opus-Lauf änderte Zeilenenden oder legte Dokumente an. Mit Skill braucht Opus das 2,3-Fache der Zeit; der Leser mit Auftrag, Wartezeit (191 und 124 Sekunden) und Folgearbeit macht rund zwei Drittel des Mehraufwands aus. Beide Leser meldeten fehlende Prüfungen beim erneuten Laden des Katalogs; beide Autoren ergänzten daraufhin eine erneute Prüfung beim Scanstart und lehnten die übrigen Befunde begründet ab. Blinder Qualitätsvergleich der vier Opus-Ergebnisse (ein Opus-5.5-high-Leser ohne Zuordnung zu den Armen, `BLIND-QUALITY-OPUS.md` im Rundenordner): Die Kontrolle 1 liegt vorn, der Skill-Lauf 2 fast gleichauf, die Kontrolle 2 mäßig schlechter, der Skill-Lauf 1 ebenfalls mäßig schlechter. Beide Skill-Läufe ergänzen nach dem Befund ihres Lesers eine erneute Prüfung des Auftrags beim Scanstart, die der Auftrag nicht verlangt und die eine vorhandene Prüfung des Plugins bereits abdeckt. Der Skill-Lauf 1 meldet widersprüchliche Definitionen außerdem mit einer anderen Fehlerkennung als die übrigen ungültigen Definitionen, entgegen dem Auftrag, und sein eigener Test bemerkt das nicht. Alle vier Opus-Ergebnisse lehnen gebrochene Grenzen ab. Auch bei Opus zeigt die frische Aufgabe damit keinen Qualitätsgewinn durch den Skill in v38.

Bei Sol trennt die Funktion die Arme nicht: Alle vier Läufe bestehen alles. Mit Skill braucht Sol im Mittel das 2,4-Fache der Zeit. Weil die Funktionsprüfung gesättigt ist, hat ein Opus-5.5-high-Leser die vier Ergebnisse blind verglichen, ohne Zuordnung zu den Armen und mit vereinheitlichten Zeilenenden (`BLIND-QUALITY-SOL.md` im Rundenordner). Sein Urteil zur Wartbarkeit:

- Die Kontrolle 1 und der Skill-Lauf 2 liegen praktisch gleichauf vorn. Der Skill-Lauf vermeidet doppelte Prüfungen, behandelt aber gebrochene Grenzwerte, die der Auftrag nicht nennt, und legt eine nicht verlangte README zu den Tests an.
- Die Kontrolle 2 ist mäßig schlechter, weil sie Sonderfälle nur für Ganzzahlen in zwei weitere Module trägt.
- Der Skill-Lauf 1 ist deutlich schlechter: ein nicht verlangter Umbau einer Signatur und eine geänderte Behandlung von Standardwerten für alle Parametertypen über sieben zusätzliche Dateien, dazu ebenfalls gebrochene Grenzwerte und eine README.

Zwei lesende Opus-5.5-high-Analysen haben die Ursachen an den Sitzungsprotokollen isoliert:

- **Umbau der Signatur (Skill-Lauf 1): vom Leser-Schritt ausgelöst.** Der Leser meldete zu Frage 2, ein zuvor geprüftes Profil werde an anderer Stelle erneut geladen, und schrieb dazu, die Lücke habe schon vor der Änderung bestanden. Der Autor hat sie trotzdem geschlossen. Der Absatz zum Leser sagt „ergänze jede fehlende Zeile" und nennt die Grenze der Kriterien nicht, nach der nur ein Mangel zur Änderung gehört, von dem das verlangte Ergebnis abhängt. Opus hatte in der Gegenprüfung zu v38 auf diese Lücke hingewiesen; der Hauptagent hatte den Hinweis mit Verweis auf einen Lauf, in dem es gut ging, nicht übernommen.
- **Standardwerte für alle Typen (Skill-Lauf 1): vor dem Leser entstanden**, aus einem eigenen Test des Autors für ein bewusst geleertes Feld. Der Abschlussbericht nennt die Wirkung, sagt aber nicht, dass sie über den Auftrag hinausgeht.
- **Zeilenenden (Skill-Lauf 2):** Der Autor hat die drei Dateien nach dem Git-Hinweis „LF will be replaced by CRLF" selbst umgeschrieben. Der Skill sagt, dieser Hinweis allein sei kein Grund dafür; der andere Skill-Lauf hat ihn befolgt. Mit dem Leser hat das nichts zu tun. Unter der Git-Einstellung des Projekts gleicht Git die Umstellung im eigenen Diff aus; auf der Platte sind die Dateien verändert.
- **README und gebrochene Grenzwerte:** in beiden Skill-Läufen und in keiner Kontrolle; ein Auslöser ist in den Protokollen nicht zu erkennen.
- **Berichtigung zu den gebrochenen Grenzwerten (Gegenprüfung durch Sol 6.1, vom Hauptagenten nachgelesen):** Der blinde Leser hat sie zu Unrecht als nicht verlangt gewertet. Der Auftrag lässt das Katalogschema unverändert, und der Schemavalidator des Projekts nimmt für `minimum` und `maximum` auch Gleitkommazahlen an (`JsonSchemaValidator.php`, Zeile 90). Solche Grenzen können das Plugin also erreichen; ihre Behandlung ist kein Mangel der beiden Skill-Läufe. Am Umbau der Signatur, an den Standardwerten und an der README ändert das nichts.

Für Sol zeigt die frische Aufgabe damit keinen Qualitätsgewinn durch den Skill und in einem von zwei Läufen eine deutliche Ausweitung über den Auftrag hinaus. Das sind zwei Läufe je Arm und ein blinder Leser.

### Aufwand

Modellzeit je Lauf in Sekunden, mit Skills gegen die gespeicherten Kontrollen:

| Aufgabe | Sol v32 | Sol v33 | Sol v34 | Sol ohne | Opus v32 | Opus v33 | Opus v34 | Opus ohne |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R2 | 325, 354, 405 | 254, 286, 351 | 296, 328, 392 | 224, 254, 288 | 278, 294, 421 | 230, 276, 327 | 302, 307, 315 | 229, 235, 253 |
| R1 | 694, 714, 754 | 488, 661, 826 | 783, 812, 847 | 441, 473 | 526, 542, 610 | 500, 573, 639 | 604, 651, 1.755 | 428, 552 |
| N1 | 279 | 350 | 347 | 109, 111 | 216 | 231 | 245 | 174, 186 |
| N11 | 725 | 748 | 605 | 251, 296 | 311 | 400 | 359 | 170, 227 |

Mit Skills brauchen beide Modelle weiterhin mehr Zeit. Bei Sol ist es in N1 das Dreifache und in N11 mehr als das Doppelte; in R1 liegt Sol in v34 mit rund 800 Sekunden je Lauf beim 1,8-Fachen der Kontrollen. In R2 liegt Sol unter dem Wert der früheren Fassungen (v22: Median 484 Sekunden mit Skill). Opus liegt in v34 in R2 und N1 beim rund 1,3-Fachen der Kontrollen und in N11 beim rund 1,8-Fachen.

Ab v36 mit der zweiten Lesung:

| Aufgabe | Sol v36 | Sol v37 | Sol v38 | Opus v36 | Opus v37 | Opus v38 |
| --- | --- | --- | --- | --- | --- | --- |
| R2 | 293, 314, 344 | 275, 315, 344 | 321, 356, 362 | 283, 360, 391 | 292, 304, 345 | 258, 266, 332 |
| R1 | 514, 584, 629 | 599, 612, 654 | 608, 641, 684 | 682, 949, 975 | 962, 978, über 1.800 | 735, 795, 967 |
| N1 | 386 | 316 | 243 | 380 | 327 | 337 |
| N11 | 719 | 566 | 657 | 655 | 641 | 534 |

Im Endkandidaten v38 liegt Sol in R2 und R1 beim rund 1,4-Fachen der Kontrollen, in N1 beim 2,2-Fachen und in N11 beim 2,4-Fachen. Opus liegt in R2 beim 1,1-Fachen, in R1 beim 1,4-Fachen des Medians der fünf Kontrollen (428, 552, 566, 613, 891 Sekunden), in N1 beim 1,9-Fachen und in N11 beim 2,7-Fachen. Ein Opus-R1-Lauf mit Leser kostete in v38 zwischen 4,05 und 5,15 US-Dollar. In R2 brauchten die drei Opus-Läufe mit Leser (Variante) rund 400 Sekunden und 2,38 bis 2,62 US-Dollar, die drei ohne Leser 258 bis 332 Sekunden und 1,74 bis 2,12 US-Dollar.

### Grenzen

- Je Modell und Aufgabe liegen höchstens drei Läufe vor. Ein Unterschied von einem Lauf ist kein belegter Effekt; das gilt auch für den später gelesenen Wert bei Opus (1 von 3 in v31, 2 von 3 in v32).
- R2, R1, N1 und N11 sind bekannte Diagnosefälle, an denen die Regeln entwickelt wurden. Sie belegen, dass die beobachteten Fehler in diesen Fällen behoben sind, und keine allgemeine Wirkung. Die frische Aufgabe R13 ist eine einzelne weitere Aufgabe mit zwei Läufen je Arm und Modell.
- Die R2-Arbeitsprobe mit 576 Anfragen meldet weiter „wiederholte Arbeit" in fast allen Läufen beider Arme. Nach ADR-0237 ist das kein Mangel, weil kein realer Aufrufer diese Menge erreicht.
- In R1 fällt in allen Läufen beider Arme die Rückkehr zur geöffneten Seite aus, wenn der gewählte Eintrag ausgefiltert wird. Dieser Befund besteht ohne Skills ebenso und ist nicht behoben.
- Die Chrome-Probe und der kalibrierte Prüfsatz laufen an den eingefrorenen Fixtures. Echtes WordPress, MySQL und PHP 7.4 außerhalb der Bewerter gehören nicht zum Nachweis.
- Bis auf drei Opus-Kontrollen für R1 in v35 stammen die Kontrollen der Diagnosefälle aus früheren Runden mit unveränderten Aufgaben und Bewertern. Sie liefen ohne die Erlaubnis, einen getrennten Agenten zu starten; die Läufe mit Skill haben sie ab v36.
- Die Variante mit dem Auftragssatz, der den Leser erlaubt, hat keine passenden Kontrollen. Unter dem eingefrorenen R2-Auftrag startet kein Autor den Leser; ob er es tut, hängt dort davon ab, wie er den Ausschluss weiterer Beratungsmodelle liest.
- Der Leser ist an Claude Code und Codex gemessen. Auf einem Host ohne getrennte Agenten entfällt der Schritt, und es gilt der Stand ohne Leser.
- Ein Opus-R2-Lauf der Variante v37S ist nicht bewertbar, weil die Testdatenbank des Bewerters `REGEXP` nicht auswertet. Beim ersten Start von v37 antworteten alle Opus-Läufe mit der Meldung des Nutzungslimits; sie sind mit der genauen Meldung ausgesondert (`retired-quota/`) und wurden nach dem Zurücksetzen gefahren.

### Entscheidungen des Eigentümers vom 2026-11-16

Der Eigentümer hat die drei offenen Befunde der Widerspruchsprüfung entschieden ([ADR-0238](../decisions/0238-eigentuemerentscheidungen-zur-widerspruchspruefung.md)):

- **Cleanup ohne Plan-Profil.** Cleanup legt keine fehlende `PROJECT_INDEX.md` an; der Kontext kommt in die zuständige Regeldatei.
- **Kein Modell je Step.** Workflow kennt keine Modellwahl je Step. Eine abweichende `[execute: ...]`-Angabe gilt nicht und wird über Plan ersetzt. Das Step-Format von Plan ist unverändert.
- **Wechsel gespeicherter Paare.** Nur zwischen Läufen über Setup.

Zum Vorgehen hat er entschieden, nach v33 zuerst die Ursache zu isolieren und dann gezielt nachzumessen, und die frische unabhängige Aufgabe einmal am Endkandidaten auszuführen.

Zur zweiten Lesung hat er am 2026-11-16 entschieden ([ADR-0239](../decisions/0239-zweite-lesung-fuer-nachgeladene-werte-und-zustand.md)): sie nach v35 als Teil des Code-Skills zu erproben; keine Selbstlesung als Ersatz; die Pflicht nur für Code; unter Workflow kein zweites Review; zunächst das volle Review durch den getrennten Agenten (v37) und nach dessen Messung den Leser nur mit den Fragen 2 und 3 (v38); dazu die gekennzeichnete Auftragsvariante als zusätzliche Messung.

Push, Veröffentlichung und lokale Installation sind nicht freigegeben und nicht erfolgt (W-002 Schritt 3 bleibt offen).

## Unabhängige Parallelprüfung der v20-Struktur und Korrekturen für v21

Vier getrennte Sol-6.1/xhigh-Agenten haben auf Suite `af0e54e4` und Shared `4739ca22` alle neun Skills geprüft. Drei Agenten haben die betroffenen Korrekturen erneut geprüft. Die Themen waren Code und UI, Plan und Workflow mit Handoff, Ask und Setup mit Context Cleanup sowie der gesamte Aufbau einschließlich Skillwriter. Die vollständigen Aufträge, Antworten und Einordnungen liegen im dauerhaften Belegpaket unter `joint-consultation-20261115/`, Einstieg `V21-PARALLEL-STRUCTURE-RESOLUTION.md`.

Korrigiert wurden die Nachweispflicht für beauftragte Verhaltensänderungen, der Einstieg bei reinen WordPress-Textkorrekturen, die Abgrenzung von Quellenprüfung und vorhandenen UI-Belegen, die Zustandsübergänge für Workflow-Ergänzungen, Legacy-Fortsetzung und Plan-Abbruch sowie die Übergabe aufgelöster Claude-Einstellungen und Setup-Ergebnisse. Die Regeln zur Browserausführung aus ADR-0230 und ADR-0233 gelten weiterhin. Die Code-Regel schützt bestehende Anwendungsfunktionen ausdrücklich. Separate Implementierungsbefunde an Shared Capture und Ask-Ganzprofilvalidierung bleiben außerhalb der Helper-Logikgrenze dieses Plans.

V20 bestand bei allen drei Sol-Kandidaten jeweils 35/35 unter PHP 8.4 und 7.4.33 sowie den zuvor fehlerhaften vollständigen Sammelpfad, beide Reihenfolgen und die WordPress-Parserformen. Zwei Kandidaten wiederholen Arbeit in beiden eingefrorenen breiten Zusatzfällen. Beim dritten bestätigte die spätere, getrennte Quellgegenprobe 10.075, 79.323 und 680.284 Schleifeneintritte bei 64, 192 und 576 Anfragen mit je zwei exakten Ergebnis-IDs. Das native Audit verifizierte 70 Inputs, 70 Ergebnisse und 3.182 Dateieinträge. Keiner der drei Kandidaten erfüllt alle bisher bekannten Arbeitsanforderungen. Die vorgesehenen v20-Opus-Implementierungsläufe wurden wegen der bestätigten Restfehler nicht gestartet. Die v20-Rohscores, eingefrorenen Prüfer und wiederverwendeten Kontrollen sind im Paket `goal-structured-operation/RESULTS-SOL-R2.md` und den verknüpften Artefakten erhalten.

Die Beratung mit Sol 6.1/high und Opus 5.5/high stimmt in der wirksamen Prüfform überein. Maßgeblich sind die verlangten Ergebnisse und Effekte des tatsächlichen Aufrufers, die erreichten Zwischendaten und ihre Wiederholung. V21 benennt beide Fehlerformen, lange überlappende Durchläufe bei kleinen Antworten und wachsende Zwischenkopien bei größeren Antworten. Die Prüfregel stellt die passende Kombination durch den erreichbaren Zweig her. Die neue Quellgegenprobe ist eine bekannte Regression, kein unabhängiger Fall. Ein Wirknachweis für v21 setzt Sol und Opus und frische unabhängige Aufgaben voraus.

## V21-Modellnachweis am bestehenden PHP-Pfad

Suite `2f202a3` und Shared `1ae5ebf` bestanden die mechanische Gesamtprüfung 12/12, die finale Paket-, Sync- und Profilprüfung und sieben Mermaid-Diagramme. Ursprünglicher Freeze und Finalisierung halten die drei spät fertiggestellten UI-/README-Dateien getrennt. Alle sechs gültigen Modellartefakte sind gegen dieselben eingefrorenen Aufgaben und die passenden sechs v14-Ohne-Skill-Belege geprüft. Sol lief `medium`, Opus wurde mit `high` aufgerufen. Die vollständigen Code-Skill-Kontexte und die Endartefakte wurden verifiziert. Kein alter Skillarm und kein neuer Kontrollaufruf.

Alle drei Sol-Läufe erreichen 35/35 unter PHP 8.4 und 7.4.33. Sol 2 besteht den vorher fehlenden vollständigen Sammelpfad, verliert jedoch gegenüber den passenden Kontrollen auf zwei Arbeitsachsen und verliert eine unterstützte Parserform. Sol 1 und 3 erhalten die Parserformen und scheitern am vollständigen Sammelpfad sowie an der neuen Probe mit zwei IDs pro Antwort. Alle drei Opus-Läufe erreichen 34/35 und verfehlen erneut die Prüfung des später gelesenen Zeilenstands, beide Reihenfolgeproben und die echten Parserformen. Ein später erweiterter Zählbeleg weist auch für Opus 1 die Mehrarbeit im unveränderten Helfer nach, bei exakt gleichen Antworten. Die vorab eingefrorenen Bewertungen bleiben erhalten. Keiner der sechs Läufe erfüllt alle bekannten Anforderungen. Die Messergebnisse stehen unter `goal-reached-work/RESULTS.md`; Zeiten, Rohbelege und Prüfer liegen im selben Paket.

Eine neue, von der Skill-Entwicklung unabhängige Aufgabe im bestehenden Plan-Viewer-Code liegt als versiegeltes R9-Archiv vor. Der Autor kalibrierte den Observer mit einer funktionierenden und zwei fehlerhaften Fassungen. R7 und R9 sind für die spätere unabhängige Abnahme ungelesen. N1/N11/R1 wurden mit passenden gespeicherten Kontrollen vorbereitet. Das Ziel bleibt offen.

Das unabhängige Aktionsreview bestätigte die Fehlmechanismen an 153 korrelierten Aufrufen. Bei Opus fehlt ein beobachteter Lesevorgang für AGENTS.md, während Sol den vollständigen Text im Startkontext erhielt. Alle sechs erhielten Code vollständig. Die Wirkung einer einzelnen Formulierung lässt sich daraus nicht ableiten. Die neue Beratung mit Sol 6.1/high und Opus 5.5/high sowie zwei gezielte unabhängige Quellnachprüfungen führen zu v22. Vor der Lösungswahl bestimmt der tatsächliche Verbraucher den Eingabevertrag, die neu gelesenen Werte und die vollständige Arbeit, einschließlich beibehaltener Helfer. Die Prüfform verbindet Anfragezahl mit erreichter Überlappung und prüft Einzelaufrufe separat, wenn sie unnötige Vorarbeit tragen. Die bestehenden Berechtigungs-, Zustands- und Funktionsgrenzen gelten. Die Einordnung und die vollständigen Beratungsantworten sind unter `joint-consultation-20261115/V22-MECHANISM-RESOLUTION.md` dokumentiert.

## V22-Vergleich am bestehenden PHP-Pfad

Suite `895884396e60f36e3812643a70859c4fa8fe912a`, Shared `f6c4efd423e0e72c2ad93a84d0680cebb477599b`. Je drei Kandidaten mit Sol 6.1/medium und Opus 5.5/high liefen gegen die sechs passenden archivierten Kontrollen ohne Scoville-Skills. Unter PHP 8.4 und 7.4.33 bestehen alle drei Sol-Kandidaten und der dritte Opus-Kandidat 35/35 Funktionsprüfungen. Zwei Opus-Kandidaten erreichen 34/35. Ihr eigener stabiler Stub prüft den später tatsächlich geladenen Zeilenstand nicht. Der dritte lässt den Status innerhalb derselben Operation zwischen den beiden Lesezugriffen wechseln und prüft den später geladenen Wert. Alle sechs Kandidaten bestehen die zusätzlichen Parserformprüfungen. Das schaffen ein Sol- und kein Opus-Kontrollartefakt.

Jedes der sechs Kandidatenartefakte wiederholt in der Sammelprüfung Arbeit entlang langer gemeinsamer Pfade. Bei linear wachsender Eingabe und je zwei exakten IDs pro Anfrage steigt die gezählte Arbeit annähernd quadratisch, auch unter der erweiterten Beobachtung unveränderter Helfer. Die passenden Kontrollen zeigen dasselbe Wachstum. Im breitesten gezählten Fall mit 576 Anfragen zeigt ein Sol-Kandidat 670.501 Schleifeneintritte gegenüber 504.899 bis 506.051 in den Sol-Kontrollen. Das ist eine gezählte Arbeitsdifferenz für diese Eingabe. Die 132 nativen Aufruf- und Ergebnispaare zeigen, dass die eigenen Modellfälle häufig nur disjunkte Pfade oder eine feste Anzahl überlappender Anfragen abdeckten. Bei einem Sol-Kandidaten folgt die gewählte Grenze aus dem bestehenden Aufwand der Implementierung. Bei Opus 3 setzt die Begründung flache Eingaben voraus, obwohl die Verträge diese Grenze nicht vorgeben.

Der Median der aufgezeichneten Laufzeiten beträgt bei Sol 483,95 Sekunden mit Skill und 254,02 ohne, bei Opus 351,96 und 234,97. Das ist Aufwand der Modellläufe. Produktlaufzeiten wurden in dieser Zusatzprobe nicht gemessen. Der vollständige Vergleich einschließlich Bindung an Prüfer, Beobachtungsgrenzen und native Aktionen steht unter `goal-complete-operation/RESULTS.md` und `goal-complete-operation/native-audit/review.md`. Die beobachteten Unterschiede identifizieren keine einzelne Formulierung als Ursache. W-005 bleibt wegen des gemeinsamen Arbeitsfehlers und des Opus-Funktionsfehlers offen.

### Unabhängiger Plan-Viewer-Vergleich und ergänzende Regressionen

R9 wurde nach dem V22-Quellenfreeze geöffnet. Die Aufgabe nutzt 71 getrackte Dateien und 3.948 Quellzeilen aus dem bestehenden Plan Viewer. Pro Modell und Arm liefen zwei gültige Aufgaben. Alle acht erreichen 7/7 und lesen beim Durchlauf mit 160 Steps genau 160 ursprüngliche Statuseinträge. Nach einem ungewerteten Start am Fünf-Stunden-Limit wurde ausschließlich der fehlende Opus-Kandidat nach dessen Reset nachgeholt. Die Modelllaufzeiten liegen mit Skill im Median bei 153,12 s für Sol gegenüber 101,67 s ohne und bei 189,75 s für Opus gegenüber 86,90 s. Beim nachgeholten Opus-Lauf setzt ein neuer Python-Testwrapper für den bestehenden lokalen Sammelbefehl Node ab 22.18 voraus. Der bestehende CI-Job provisioniert Node 22. R9 belegt TypScript-Verhalten für die geprüften Fälle und ein explizit vorgegebenes Arbeitsbudget. Native Typprüfung, gerenderte Oberfläche und tatsächliche CI-Ausführung gehören nicht zum Nachweis. Der Bericht unter `goal-complete-operation-r9/RESULTS.md` hält auch die Korrektur eines Fehlalarms in der Kontextprüfung beider Sol-Kontrollen fest.

Die zusätzlichen Sol-Vergleiche nutzen je zwei Kandidaten und zwei gespeicherte passende Kontrollen. N1 erhält mit Skill den Datenvertrag für ältere Leser und lehnt ein Objekt im Prozentfeld ab. Die gemeinsame Teilnehmerprüfung bleibt quadratisch. N11 erhält mit Skill die bereits unterstützten Rechnungspräfixe. Die JSON-Liste beider Arme erstellt für 256 ausgegebene Positionen 16.768 Objekte, weil sie Positionsdaten der Originalrechnung pro Gutschrift erneut lädt. Die Kandidaten messen einen anderen, korrekt verbesserten SQL-Pfad. Der mehrdeutige Rundungsfall zählt getrennt. R1 erreicht mit Skill jeweils 11/11 im kalibrierten Prüfsatz. In der separaten Chrome-Probe verliert beim Entfernen des gewählten Eintrags sowohl der Kandidat als auch die passende Kontrolle den bestehenden Rückfall auf die weiterhin sichtbare geöffnete Seite. Einer der Kandidaten setzt seine veränderte Erwartung im eigenen Test fest. Die Native Reviews und Prüfergebnisse sind unter `goal-complete-operation-regressions/` und `goal-complete-operation-r1/` gesichert.

### V23 wählt den entscheidenden Fall vor der Reparatur

Fable 5.2/high, Sol 6.1/high und Opus 5.5/high behandelten den verbleibenden Fall bei der tatsächlichen späteren Lesung und die Auswahl der Größenprobe. Beide Folgeberater empfehlen eine gezielte Ausgangsbeobachtung und die Wiederverwendung gleichwertiger Nachweise. Opus weist nach, dass im Sol-Fall der geladene Bestand wächst, während jede kleine Antwort einen kurzen Pfad durchläuft. Ein Prüfzeitpunkt allein korrigiert diese Wahl nicht. Die belegte gemeinsame Arbeitslücke bleibt in R2 und den ergänzenden CLI-Pfaden bestehen. Der unabhängige R9-Vergleich besteht mit explizitem Budget in beiden Armen.

Code zieht den entscheidenden Beleg für eine verletzbare spätere Lesung oder Arbeitsschranke auf einem bestehenden Pfad vor die Lösungswahl. Ein bereits gleichwertiger Beleg genügt. Die Evidenztabelle und ADR-0231 regeln Fail-first. Shared verknüpft die Zahl der Aufrufe mit der gemeinsamen Eingabemenge, die ihre wiederholten Pfade tatsächlich durchlaufen oder kopieren würden. Die größte unterstützte Überlappung und die separaten Prüfungen des einzelnen Aufrufers bleiben im Kriterium. Die zwei unabhängigen Quellprüfer bestätigten die nach ihren Befunden präzisierte Fassung. Die Anforderungen an Funktionserhalt, Berechtigungen und wartbare Kapselung gelten. Eine unabhängige Aufgabe darf erst nach Quellenfreeze geöffnet werden. V23 muss seine Wirkung gegen passende Kontrollen ohne Skills noch zeigen.

### V23-R7 und bestätigte Abweichungen bei Arbeitsbereich und Zeilenenden

Die unabhängige Aufgabe R7 nutzt 488 unveränderte Produktionsdateien und eine neue `uniqueItems`-Anforderung am bestehenden PHP-Verbraucher. Alle acht gültigen Ausgaben bestehen die 108 Funktionsfälle und zwölf Größen- und Vollständigkeitsprüfungen der Autorenbewertung. Der gemessene Funktions- und Arbeitsumfang zeigt damit gleiches Bestehen. Beide Skill-Arme benötigen mehr Modelllaufzeit. Zwei unabhängige Aktionsreviews und zwei unabhängige Quellenreviews erfassen weitere Unterschiede. Beide Sol-Kandidaten stellen nach einer gewöhnlichen Git-Meldung einen ganzen Validator auf CRLF um. Beide passenden Sol-Kontrollen behalten LF. Ein Opus-Kontrollartefakt ändert das Zeilenformat ebenfalls. Ein Opus-Kandidat verletzt die Arbeitsbereichsgrenze durch ein sofort wieder entferntes Skript; die übrigen sieben bestehen die Aktionsprüfung. Bei je einem Kandidaten- und Kontrollartefakt meldet der Bewerter nicht geladene lokale Tests im Pluginbaum. Der dokumentierte Produktladepfad schließt diese Tests aus. Die Rohbewertungen und die jeweilige Auswertung bleiben im dauerhaften Paket `goal-deciding-evidence-r7/RESULTS.md` erhalten.

Die Sol-Quellenprüfung findet mögliche Mehrarbeit in nativen HashTable-Vergleichen bei beiden Kandidaten und eine andere Schlüsselstrategie in den Kontrollen. Die mitgelieferten Zeitmessungen prüfen den Fall kollidierender gültiger Stringwerte nicht. Beim R2-Sol-Vergleich sind alle drei Kandidaten im ursprünglichen Prüfsatz bei 35/35. Ein Kandidat verteilt die Arbeit über die kleinen Sammelantworten deutlich effizienter, übersieht jedoch eine gültige qualifizierte Blockform. Bei seiner einzelnen Anfrage mit großen Zwischenmengen zählt der Bewerter bei Größe 576 insgesamt 664.703 Array-Einträge in Operanden bei 1.152 exakten Ausgabe-IDs. Zwei Kandidaten behalten die wiederholten langen Sammelpfade. Die Bewertung umfasst damit den tatsächlich erreichten Aufruf, die maßgebliche Eingabeform und die internen Zwischenergebnisse.

Opus 5.5/high und Sol 6.1/high empfehlen gemeinsam eine gezielte Korrektur am Zeilenendenabsatz. Bei einer Git-Meldung über eine spätere Konvertierung bleibt die tatsächliche Ausgangsdatei maßgeblich. Eine normalisierte Diff-Ansicht kann die umgeschriebenen Bytes verbergen. Die bestehende Scratch-Regel nennt ausdrücklich den ersten temporären Befehl und war in beiden Opus-Paketen vorhanden. Diese Regel bleibt Grundlage des separaten Aktionsnachweises. Der überprüfbare Textdelta und die Rohberatung werden unabhängig von der noch offenen Modellwirkung gesichert.

### V24 besteht die Formatprüfung gegen die passenden Kontrollen

Suite `546d1cf`. Die vier neuen V24-Kandidaten erhalten dieselbe R7-Fixture und das ursprüngliche Orakel. Die vier passenden Kontrollartefakte stammen aus dem vollständigen R7-Lauf ohne Skill. Alle vier Kandidaten sehen dieselbe Git-Konvertierungsmeldung und behalten die ursprünglichen LF-Zeilenenden. Ihre 108 Funktionsprüfungen, zwölf Arbeitsprüfungen und jeweils vollständigen Aktionsreviews bestehen. Die Kontrollen bestehen diese Dimensionen ebenfalls, wobei ein Opus-Kontrollartefakt auf CRLF wechselt. Der Median der Modelllaufzeit beträgt mit V24 bei Sol 433,87 statt 253,75 Sekunden und bei Opus 414,61 statt 266,96 Sekunden. Der einzelne Erfolg betrifft die gezeigte Dateiformatabweichung. Das Ziel zur Anwendungskomplexität umfasst andere Belege. Der vollständige Vergleich steht unter `goal-line-ending-behavior-r7/RESULTS.md`.

### V25 prüft verschobene Arbeit am lauffähigen Entwurf

Die parallele Beratung mit Sol 6.1/high und Opus 5.5/high bestätigt die Lücke zwischen einem gemessenen ursprünglichen Problem und der Arbeit, die der Entwurf neu einführt. Die Sol-Läufe beobachteten früh Lade- und Parserarbeit. Ein Kandidat korrigierte die kleine Sammelantwort, materialisierte aber bei einem einzelnen Ergebnis quadratisch viele Zwischenmitgliedschaften. Opus 3 reproduzierte den tatsächlichen Zustandswechsel vor der Reparatur und behielt dennoch die überlappenden Rückwärtsläufe. Die Modelle meldeten mehrere bestehende Grenzen im Abschluss. Diese Spuren identifizieren eine unvollständige Fall- und Arbeitsabdeckung und erlauben keine Kausalzuordnung zu einer einzelnen Regel.

Code bewertet den lauffähigen Entwurf mit seinem tatsächlichen Verbraucher, bevor dieser Entwurf übernommen wird. Wenn Arbeit verschoben oder ergänzt wurde, müssen die entscheidenden Beobachtungen weiterhin die vom Aufrufer verlangte Leistung, Ergebnisse und Effekte abdecken. Shared gliedert die Prüffälle nach tatsächlich erreichter gemeinsamer Arbeit im Sammelpfad und nicht verlangter Vorbereitung oder Zwischenarbeit im Einzelpfad. Die größte unterstützte Überlappung gilt für beide. Fallwiederverwendung, native und unveränderte Teilpfade, Gegenfassung und erforderliche Verhaltensergebnisse bleiben in derselben Eigentümerregel. Spätere Änderungen am Diff durchlaufen nur die jeweils betroffenen Prüfungen. Zwei unabhängige Quellreviews revidierten die genaue Fassung und bestätigten den finalen Diff. Die nächste Modellmessung nutzt aktuelle Kandidaten und die passenden vorhandenen Kontrollen ohne Skill.

### V25-Ergebnisse und akzeptierte Arbeitsschranken

Im R2-Fall bestehen drei Sol-Kandidaten 35/35 und sämtliche Parserformen. Ihre vollständige Arbeit auf der kleinen Sammelantwort bleibt quadratisch. Bei 576 Anfragen beobachtet der unveränderte erweiterte Prüfer 670.501 bis 671.651 Schleifeneintritte mit Skill gegenüber 504.899 bis 506.051 ohne bei gleichen Antworten. Die Kandidaten behalten aus dem Entwurf die späte Besuchsmarkierung, die gegenüber der Markierung beim Einreihen 165.600 weitere Stack-Entnahmen erzeugt. Sol 2 misst eine zweite quadratische Achse im eigenen Test und setzt die Menge der ausgeführten Kantenbesuche als Assertion, obwohl sie aus dem gewählten Algorithmus folgt. Opus erreicht 35/35, 34/35 und 35/35. Die drei Arbeitskurven bleiben annähernd quadratisch. Ein Opus-Lauf hält den erkannten Aufwand wegen angenommener typischer Tiefe für verträglich, obwohl keine entsprechende Anforderung oder wirksame Schranke belegt ist. Native Prüfungen und Gesamtbefund stehen unter `goal-runnable-repair/RESULTS.md`.

R11 verwendet einen anderen echten Aufrufer des Plan Viewers und 71 getrackte Dateien mit 3.948 physischen Codezeilen. Alle acht neuen Läufe mit und ohne Skill bestehen je zwölf Funktions- und vier Arbeitsprüfungen. Jede erfolgreiche Betriebsform öffnet genau zwölf bereitgestellte und zwölf heruntergeladene Dateien je einmal. Die spätere Ersetzung einer Datei bei gleicher Größe und Änderungszeit wird im beobachteten Ablauf erkannt. Die Kontroll- und Kandidatenarme behalten dieselben beobachteten Funktionen. Die Kandidaten benötigten mehr Modellzeit. Die vollständigen Aktionsreviews bestätigen gemockte GitHub-Operationen, unterscheiden Vorab- und Nachweise nach der Implementierung und sind unter `goal-runnable-repair-r11/RESULTS.md` gebunden.

Die gesonderte lokale R2-Positivkalibrierung besteht die eingefrorenen Funktions-, Parser- und Arbeitsfälle mit PHP 7.4.33 und 8.4.23 in einer gemeinsamen Implementierung. Eine beschränkte komponentenbezogene Indexbildung deckt die geprüften kleinen Sammelantworten ab. Der Einzelpfad traversiert bei zu großen Zwischenergebnissen rückwärts. Die erweiterte All-loaded-Observation bleibt wegen statisch markierter Stellen `inconclusive`; eine gezielte Quell- und Pfadbeobachtung benennt die tatsächlich erreichte Arbeit. Bei gemeinsam breiten Komponenten mit anders verteilten kleinen Antworten bleibt ein weiterer aus dem Quellpfad hergeleiteter Wiederholungsfall möglich. Die Referenz belegt die Machbarkeit der eingefrorenen Fälle in der Offlinekopie. Sie gehört nicht zum Modellvergleich und wird nicht in die Anwendung übernommen.

V26 klärt die zwei beobachteten Ausnahmen in Shared. Eine angenommene Größen- oder Formgrenze muss durch die unterstützte Eingabevorgabe oder den tatsächlichen Aufrufpfad gedeckt sein. Eine höhere Arbeitsschranke gilt bei einer akzeptierten Abwägung für genau diesen Aufrufer und Arbeitsfall. Die Quelle der Zustimmung wird nur bei Nutzung dieser Ausnahme genannt. Beide Modellberatungen und Quellnachprüfungen sind gesichert. Der gezielte Modellvergleich prüft die Akzeptanz der konkreten Regel am bestehenden R2-Fall bei unveränderten Eingaben und passenden gespeicherten Kontrollen.

### V26-Diagnose und die Eignung eines beibehaltenen Pfads

V26 liefert je einen gültigen neuen R2-Kandidaten und verwendet die jeweiligen
Kontrollen derselben Wiederholungsnummer. Sol besteht 35/35 und alle fünf
echten Parserformen. Opus verfehlt wie seine Kontrolle die Prüfung der später
gelesenen Zeile und erreicht 34/35. Beide Kandidaten bewahren die
Dateizeilenenden. Bei 576 Anfragen mit konstant je zwei exakten IDs ergeben
sich bei Sol 671.653 statt 506.051 und bei Opus 836.675 statt 670.499
Schleifeneintritte. Opus verlagert die Arbeit in den unveränderten Helfer
UsageRoots und begründet sie mit angenommener geringer Tiefe. Die nur auf
geänderte Dateien beschränkte Beobachtung erfasst diese Arbeit nicht.
Sol belegt den späteren Lesewechsel vor dem Patch, misst aber die wiederholte
Arbeit bei gemeinsam wachsenden Elternpfaden und vielen kleinen Antworten
nicht. Die native Opus-Spur belegt den vollständigen Code-Skill und den
gelesenen Produktvertrag. Ein Lesezugriff auf AGENTS.md ist nicht belegt.
Die Diagnose belegt diese Fehler und konkrete Mehrarbeit, keine Ursache im
Modell. Berichte, Rohwerte und exakte Paarzuordnung stehen unter
`goal-supported-workload/RESULTS.md`.

Die erneute parallele Beratung mit Sol 6.1/high und Opus 5.5 mit angefordertem
high empfiehlt eine Eignungsentscheidung am tatsächlichen Anwendungspfad.
Code verknüpft zwei vorhandene Nachweise direkt mit der Wahl des Designs:
den Wechsel beim späteren Lesen und die relevante Arbeit über wachsende
unterstützte Eingaben. Die Vorabprüfung nutzt dieselben Verträge und die
bereits vorhandene gleichwertige Evidenz. Der lauffähige Entwurf wird
einschließlich der Arbeit unveränderter, neu verwendeter Helfer geprüft.
Ein unabhängiges Vergleichspaar bewertet diese Struktur am unveränderten
R2-Fall. Ausgelassene oder verlegte Arbeit bleibt auch bei grünen
Funktionschecks ein Fehler.

### V27-Ergebnisse und Nachweis vorhandener Nutzerzustände

Im bekannten R2-Vergleich bleibt Sol bei 35/35 und allen fünf echten
Parserformen. Bei 576 kleinen Antworten zählt sein Kandidat 506.053
Schleifeneintritte gegen 506.051 in der gespeicherten Kontrolle. Das
Wachstum bleibt quadratisch. Opus erreicht 34/35, besteht die fünf
Parserformen und behält 836.675 statt 670.499 Schleifeneintritte. Im
separaten Zustellpaar erhalten beide frischen Opus-Arme dieselbe
vollständige Projektdatei. Der Kandidat behebt den später gelesenen Wert
und erreicht 35/35 gegenüber 34/35. Die Arbeit bleibt mit Skills höher
bei 836.675 statt 504.899 Schleifeneintritten, jeweils für 576 identische
kleine Antworten. Die veränderte Zustellung ist ein Diagnosefall mit
neuer passender Kontrolle. Sie belegt keinen kausalen Effekt der
Projektdatei. Ergebnisse und native Nachprüfungen stehen unter
`goal-design-fit/RESULTS.md` und `goal-project-rules-delivery/RESULTS.md`.

R12 wurde unabhängig aus 498 getrackten Projektdateien mit 52.321
Textzeilen erstellt und erst nach Quellenfreeze geöffnet. Alle acht
auswertbaren Läufe bestehen die Funktion und den Arbeitsnachweis am
gemeinsamen Matcher. Jeder Arm liefert zwei Bestandserfolge je Modell.
Zwei zusätzliche Sol-Prozesse wurden vorher durch Windows-Fehler 1909
unterbrochen. Ihre unveränderten Rohartefakte bleiben erhalten. Der
erweiterte Aktionsreview prüft auch gelesene Nebenpfade und Aufwand.
`goal-design-fit-r12/RESULTS.md` bindet die genauen Ergebnisse.

R1 bestätigt in Chrome einen zusätzlichen Verlust der aktiven Auswahl
bei Opus mit Skills. Die passende Kontrolle bewahrt die Auswahl.
Beim Ausfiltern der live gewählten Option stellt keiner der vier
beobachteten Stände die ursprünglich vorgesehene geöffnete Seite wieder
her. Sols neues Frischeskript verwendet die Übersetzungsbibliothek ohne
Ladung des Katalogs für sein eigenes Handle. Beide Kandidaten erhielten
den Code-Kern vollständig. Sol las die UI-/WordPress-Regeln; bei Opus
lag UI bytegleich in der Kopie, die Lektüre bleibt in den nativen Aktionen
unbelegt. Dokumentiert in `goal-design-fit-r1/RESULTS.md`.

Sol 6.1/high und Opus 5.5 mit angefordertem high empfehlen dieselbe Stelle
für die strukturelle Korrektur. V28 vergleicht denselben fachlichen
Übergang am bisherigen und am resultierenden Anwendungspfad. Ein
unterstütztes zwischenzeitliches Update wird genau dann geprüft, wenn
es eine zu erhaltende Wirkung beeinflussen kann. Die Beobachtung erfolgt,
wenn eine erforderliche Ausgabe sichtbar oder vom Verbraucher genutzt
wird. Aktuelle gleichwertige Evidenz bleibt wiederverwendbar. Der
nächste R1-Vergleich verwendet unveränderte Aufgaben und Prüfer.

Im abgeschlossenen V28-Vergleich (Suite `a129245`, Shared `02c687e`)
erreichen beide Kandidaten und die gematchten Kontrollen 11/11 im
kalibrierten DOM. Sols Rohscore 0/11 bleibt erhalten und entsteht
durch die im alten Stub fehlende Select-Collection. Beide Kandidaten
halten in Chrome die ursprüngliche Auswahl `1` über die geprüften
Teilantworten und bestehen die zugeordneten Cancel-Prüfungen. Sols
Registrierung des Übersetzungshandles ist am Quellstand korrigiert.
Die separate Chrome-Probe zur Entfernung der live gewählten `30`
zeigt bei beiden Kandidaten weiter einen falschen Fallback. Erwartet
ist die weiterhin sichtbare geöffnete `10`, beobachtet werden leerer
Platzhalter und `20`. Die Quellenkorrektur ist deshalb teilweise
belegt. Maßgebliche Rohbelege, nachträgliche Stub-Kalibrierung und
unabhängiges Review stehen unter `goal-preserved-transition-r1/RESULTS.md`.

## Strukturprüfung aller Skills und v19-Sol-Ergebnis am 2026-11-15

Auf ausdrücklichen Nutzerauftrag wurden alle neun Skills parallel von unabhängigen Agenten auf ihren gesamten Aufbau geprüft. Neben den beiden vorhandenen Code/Shared-Reviews durch Sol 6.1/high und Opus 5.5/high liegen acht neue Sol-Einzelreviews sowie je ein Sol- und Opus-Gesamtreview vor. Die Quellen blieben währenddessen sauber auf Suite `2f753e23` / Shared `df97510e`. Skillwriter war nur Prüfgegenstand. Die vollständige Zusammenführung, Einordnung strittiger Befunde, Aufträge und zwölf unveränderten Antworten stehen dauerhaft unter `state/2026-11-14-skill-evaluation/joint-consultation-20261115/`, Einstieg `V19-SUITE-STRUCTURE-REVIEW.md`.

Die fachlichen Zuständigkeiten tragen überwiegend. Die folgenden Korrekturen müssen Voraussetzungen vor Aktionen bringen, verstreute Kriterien an ihrem Owner zusammenführen und Diagramme mit ihren tatsächlichen Bedingungen und Rückläufen abgleichen. Code/Shared braucht den größten Umbau; seine Kernpflichten bleiben ohne zusätzliches Laden verfügbar. Funktionserhalt, Aktionsrechte und die festgelegten UI-Rendergrenzen bleiben bindend. Einzelbefunde sind nicht pauschal übernommen: Der im Workflow angeblich fehlende Korrekturweg steht bereits ausdrücklich in Operations; bestätigt ist die abweichende Diagrammdarstellung. UI verweist auf Code ausdrücklich nur dort, wo Code gilt. Die Strukturkorrektur und ihr Modellnachweis sind noch offen.

Die drei neuen v19-Sol-R2-Kandidaten sind fertig, aber **keiner ist abnahmefähig**. Originalscore unter PHP 8.4 und PHP 7.4.33 jeweils 35/35, vollständiger Sammelpfad und beide Reihenfolgeproben bestanden. Alle drei verlieren gültige Parserformen und zeigen in beiden vorab eingefrorenen Broad-Fällen nahezu neunfache Schleifenarbeit bei dreifacher Eingabegröße. Bei Größe 576 sind es rund 666.000 beziehungsweise 1,33 Millionen Schleifeneintritte bei korrekten Listen. Die passenden sechs v14-None-Belege wurden wiederverwendet, nicht neu ausgeführt. Artefakt-/Kontextintegrität und Formatprüfung bestanden. Das unabhängige native Audit ist abgeschlossen: 63 vollständige Inputs und 63 zugeordnete Ergebnisse strukturell geprüft, entscheidende Aktionen einzeln gelesen, 3.175 Dateieinträge byteverifiziert. Alle drei erhielten Code und AGENTS vollständig; keine beobachtete unzulässige Mutation. Die Kürzungen und Nachweisgrenzen stehen im separaten `native-audit/review.md`. Sol 3 selbst führte PHP 7.4 nicht aus; der unabhängige spätere Lauf beweist Kompatibilität im Prüfumfang, nicht die damalige Verfahrensbefolgung. Bericht und Hashbelege liegen unter `state/2026-11-14-skill-evaluation/goal-maintainable-operation/independent/R2-v19-adjudication/`.

Die drei vorgesehenen Opus-v19-Kandidaten wurden nicht gestartet: Der bekannte Sol-Fehler und die Strukturkorrektur erfordern einen neuen Kandidaten. `V19-NOT-STARTED.json` hält diese Abweichung fest; eingefrorene Pläne, Rohscores und Inputs bleiben unverändert. R7/R8 bleiben versiegelt. Das Gesamtziel bleibt offen; Quellenreview und technisches Bestehen ersetzen keinen Wirknachweis.

## Qualitätsziel und v19-Quellenstand vor den Modellläufen

Das Ziel bleibt offen. Die ausdrücklich präzisierte Priorität lautet:
wartungsfreundlicher, gut verständlicher und klar gekapselter Code ohne
unnötige Komplexität. Klare Verantwortlichkeiten und Schnittstellen gehören
dazu. Der nötige Änderungsumfang folgt dem vollständigen Ergebnis einschließlich
Funktion, Zustand und Laufzeitgrenzen. Die Größe des Diffs ist kein Qualitätsmaß. Nach ausdrücklicher
Nutzerkorrektur bleiben vorhandene Anwendungsfunktionen und ihr Verhalten
erhalten, außer soweit der Nutzer ihre Änderung beauftragt. Wartbarkeit,
Einfachheit oder Laufzeit rechtfertigen kein Entfernen von Funktionen
und keine Abschwächung erforderlicher Garantien. Die Regel steht ausdrücklich
im Code-Kern und in Shared Code Quality.

Die v18-Modellläufe mit Suite `452d613` / Shared `1ef7d44` sind abgeschlossen.
Zusätzliche Prüfungen zeigen weitere Fehler; ursprüngliche Rohscores bleiben
erhalten. Sol lief medium, Opus high, ohne alten Skillarm. Passende None-Kontrollen
wurden wiederverwendet; nur die zuvor fehlenden Opus-high-Kontrollen für N1/N11/R1
wurden neu ausgeführt. Der Code-Skill war bei Kandidaten vollständig im Kontext.

- R2: alle sechs Kandidaten zunächst 35/35. Andere zulässige Reihenfolgen
  scheitern bei Opus 1/3. Der gesicherte echte WordPress-6.8-Parser belegt zwei
  zulässige Verweisformen, die Sol 3 und alle Opus-Kandidaten verlieren.
  Zwei unabhängig entwickelte weitere Eingabeformen zeigen unnötige
  Vorberechnung bei allen drei Sol-Kandidaten und wiederholte native Mengenarbeit
  bei Opus 2. Die sechs None zeigen diese neuen Wiederholungen nicht, scheitern
  aber weiter an der großen Sammelabfrage. Keine Gruppe erfüllt den Gesamtvertrag.
- N1: ursprünglicher Score überall 9/9. Opus Kandidat 2 bleibt im unterstützten
  `--among`-Pfad quadratisch. Alle vier Kandidaten erhalten den getrennt geprüften
  bestehenden Lese-/Schreibvertrag.
- N11: 10/11 in allen sechs neuen relevanten Läufen; die Rundungsentscheidung
  bleibt offen. Beide Opus-Kandidaten und beide neuen Opus-None wiederholen
  JSON-Arbeit quadratisch. Sol-Kandidaten bestehen diese Arbeitsprüfung.
  Alle Kandidaten erhalten Präfixkompatibilität; beide Opus-None verlieren sie.
- R1: fünf gültige neue Läufe, ein unvollständiger Opus-Kandidat ohne Score.
  Ein unabhängiger, in Chrome kalibrierter Zusatz korrigiert den fehlenden
  DOM-Stub für `selectedOptions`; damit erreichen alle fünf gültigen neuen
  Ausgaben 11/11. Ein anderer echter Browserfall zum erhaltenen Auswahlzustand
  scheitert weiterhin bei beiden Sol-Kandidaten, dem gültigen Opus-Kandidaten
  und Opus None 1; Opus None 2 besteht.

Diese nachträglichen Diagnosen sind getrennt von den eingefrorenen Bewertungen
und beanspruchen keine statistische Nichtunterlegenheit. Der unabhängige R2-
Aktionsreview deckt 185 vollständige Inputs ab. Bei Opus ist die verlangte
AGENTS-Lektüre unbelegt, bei Sol steht die Datei zudem im nativen Startkontext.
Die Host-Asymmetrie ist dokumentiert. Das native Aktions- und Wartbarkeitsreview
für N1/N11/R1 ist abgeschlossen: 671 vollständige Payloads und 670 Ergebnisse
strukturell durchgesehen, entscheidende Aktionen und Quellen einzeln gelesen,
6.892 erfasste Dateien byteverifiziert. Leselücken stehen im Bericht. Zusätzliche
Befunde: V1 akzeptiert bei drei Opus-N1-Ausgaben neue Prozentdaten; Sol N1/2
parst gespeicherte Strings erneut im Domänenkern; beide Sol-N11 lösen die
Arbeitsfrage über ein partielles Invoice mit uneindeutig leeren Positionen.
Die letzten beiden sind Struktur-/Schnittstellenbefunde ohne hier beobachtete
falsche Geschäftsausgabe. Sol R1/1 verändert vorhandene LF-Dateien auf CRLF und
meldet fälschlich Erhaltung; Opus R1 None 1 versucht einen nicht auf eigene
PIDs begrenzten Prozessstopp, dessen konkrete Fremdwirkung unbelegt bleibt.

Der Hauptagent hat v19 ohne Skillwriter formuliert. Code und Shared stellen
das Qualitätsziel voran und ersetzen Regeln zur kleinsten Änderung durch den
vollständigen Ergebnisvertrag. Sol 6.1 high und Opus 5.5 high prüften die Diffs;
die daraus bestätigten Widersprüche in Code, UI, Plan, Workflow, Setup, Ask
und Handoff sind am Owner behoben. Die kleineren Schlusskorrekturen sind
im Diff gelesen; die vollständige technische Gesamtprüfung bestand danach
12/12 bei vor und nach dem Lauf identischen Quellenhashes. Anschließend hat
der Nutzer die ausdrückliche Erhaltung des Anwendungsverhaltens verlangt.
Die endgültige, mit Sol und Opus geklärte Ergänzung besteht die sechs
betroffenen Shared-Regeltests, alle vier Paketvarianten, Synchronprüfung
und Profilvalidierung. Belegte Vertragskorrekturen, die das angeforderte
Ergebnis benötigt, bleiben möglich; Funktionen für einen einfacheren
oder schnelleren Entwurf zu streichen bleibt ausgeschlossen. Frühere
Zwischenstände und ein zeitlich gemischter Prüflauf bleiben im CHECK-CHECKPOINT
dokumentiert. V19-Modellwirkung ist weiterhin ungemessen.

Die vollständige v18-Auswertung und nachprüfbaren Einzelwerte liegen im
dauerhaften Paket unter `goal-operation-evidence/RESULTS.md`; zugehörige
native Spuren, Prüfer, Kalibrierungen und Hashes bleiben dort erhalten.
N1/N11 und R1 liegen unter `goal-operation-evidence-regressions` und
`goal-operation-evidence-r1`. Quellenreviews und Abwägungen liegen unter
`joint-consultation-20261115/v19-source-review-*`, `v19-correction-review-*`,
`v19-behavior-preservation-*` sowie den V19-Entscheidungsdateien. Die neueste
Nutzerkorrektur steht in `V19-USER-BEHAVIOR-CORRECTION.md` und ersetzt die
frühere Abwägung zur Streichung. Das native Review liegt unter
`goal-operation-evidence-regressions/native-audit/review.md`.
R7 bleibt versiegelt. Keine Veröffentlichung oder Installation.

Die folgenden Abschnitte bewahren die früheren Zwischenstände; ihre offenen
v18-Läufe sind durch die Ergebnisse dieses Abschnitts ersetzt.

## Aktueller Quellenstand v18 am 2026-11-15

Das Ziel bleibt offen. Suite `452d613`, Shared unverändert `1ef7d44`. Nach dem
Reset haben Fable5.2/high und Opus5.5/high vollständig geantwortet; zusammen mit
Sol6.1/high sehen sie eine zu enge Auswahl der Prüfung anhand der eigenen
Reparatur. Keine innere Modellursache oder Wirkung eines einzelnen Satzes ist
belegt. Die Claude-Rohdaten nennen die gewählten Modelle in modelUsage, ihre
Effort-Stufe wird nicht berichtet. Leselücken bleiben in den Antworten sichtbar.

Parent schreibt ohne Skillwriter. Der v18-Entwurf wurde von Sol und Opus high
lesend geprüft und mit adjudizierten Korrekturen umgesetzt: echte Einstiegspfade,
relevante Zweige und gezählte unveränderte Wiederholungen bestimmen die
Arbeitsprüfung; die Zuordnung steht bei gemeinsam wachsendem Input in
Arbeitsnotizen und wird nach Änderungen nachgeprüft. Erhaltene Übergänge
bekommen ihre Sollwerte aus dem etablierten Pfad und tatsächlichen Verbraucher,
gegen die Vertragsanforderungen geprüft. Offene Entwürfe oder alte Fehler
werden dadurch nicht zur Norm. Trade-off-Freigaben gehören Nutzer/Projektregeln.
Neue oder erweiterte Eingabeformate werden vor bedeutungsverlustiger Umwandlung
auf ihre deklarierte Form geprüft. Keine universelle Linearitätsforderung,
kein Vorher-Lauf aller Tests, keine neue Berechtigung oder Veröffentlichung.

Sechs betroffene Shared-Regeltests, vier Paketvarianten, Synchronprüfung und
Planvalidierung bestehen. Der erste Build war erfolgreich; ein erneuter Build
nach lokalem Zeilenumbruch verweigerte das schon vorhandene Ziel. Der Commit
wurde vor Behandlung dieses Werkzeugfehlers gemacht; Freeze verweigerte die
nicht passenden Loghashes. Der vorherige Build und Fehlerlog sind erhalten,
ein anschließend erfolgreich erstellter frischer Build allein liefert die
eingefrorenen Modellpakete. Kein Modell lief mit einem unpassenden Paket.
Die v18-R2-Runde ist mit sechs neuen Kandidaten Solmedium/Opushigh gestartet;
sechs passende v14-None werden wiederverwendet. Ergebnisprüfung steht aus.
Weitere N1/N11/R1-Regressionen sind vorbereitet, Sol begonnen. Für Opus high
sind dort frische None nötig; ältere Medium-Kontrollen werden nicht vermischt.
R7 bleibt versiegelt.

Der R1-Prüferfehler aus v17 ist inzwischen getrennt korrigiert und kalibriert:
genau zwei Beobachtungen lesen sichtbare Optionen. Alle fünf bisherigen
Kontrollvarianten behalten ihre erwarteten Resultate; zusätzliche Referenzen
belegen zulässig versteckte Optionen und die Zurückweisung falsch sichtbarer
Optionen. Auf allen vier unveränderten Artefakten ergeben sich Kandidaten
11/11 und11/11, None11/11 und10/11. Die ursprünglichen Rohwerte bleiben erhalten.
Der separate echte Browser-Fallback scheitert weiterhin in Kandidat2 und beiden
None. Keine erneuten Modellaufrufe für diese Prüferkorrektur. Die Parent-
Profilbereinigung ist abgeschlossen; gesperrte Verzeichnisse wurden nach der
Workspace-Regel kollisionsfrei nach Desktop/_delete verschoben.

Entscheidung, vollständige Antworten und Leselücken:
`joint-consultation-20261115/V18-DECISION.md`, `v17-all-paths-*` und
`v18-source-review-*` im dauerhaften Reviewpaket. Quellenfreeze und Tests unter
`goal-operation-evidence`; gezielte Regressionen haben eigene Unterverzeichnisse.
Die folgenden v17-Absätze dokumentieren die Befunde samt damaligem Zwischenstand;
offene Claude-Antworten und R1-Nachauswertung sind durch diesen Abschnitt ersetzt.

## Ausgewerteter Stand v17

Das Ziel bleibt offen. V17, Suite `7054609` / Shared `1ef7d44`, präzisiert
getrennte Reads, Dateieffekte bei Inspektionen und die Wahl aussagekräftiger
Gegenfälle vor der Reparatur. Sechs neue gültige R2-Kandidaten gegen sechs
passende wiederverwendete v14-None-Kontrollen; kein alter Skillarm.

| v17 | Funktion | Gesamtarbeit | Aktionsgrenze | Formatierung | alle vier Achsen |
| --- | --- | --- | --- | --- | --- |
| Sol medium, Kandidat | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 |
| Sol medium, None | 3/3 | 0/3 | 3/3 | 2/3 | 0/3 |
| Opus high, Kandidat | 3/3 | 2/3 | 2 bestanden, 1 ungeklärt | 3/3 | 1/3 |
| Opus high, None | 0/3 | 0/3 | 2/3 | 3/3 | 0/3 |

Alle vollständigen Finals sind gelesen. Modell-, Paket- und Code-Vollkontext-
prüfungen bestehen. Beide vollständigen Arbeitsprüfer stimmen überein;
PHP 7.4 bestätigt die Funktion. Opus 1 bleibt bei 96/288/864 Quellen mit
10102/85558/754296 gezählten Schritten quadratisch. Sein eigener Test benutzt
den echten Runtime-Einstieg, aber disjunkte kleine Pfade und zählt nur Reads
und Parses. Die Gegenfassung wiederholt nur den reparierten Scan. Die weiter
je Quelle laufende Vorfahrensuche bleibt ungemessen und wird im Final als
bewusst beibehaltene Mehrarbeit benannt. Früher Testbeginn und echter Einstieg
allein haben die Wahl des falschen Gegenfalls somit nicht verhindert.

Sol high prüfte alle 152 vollständigen nativen Inputs samt Ergebnissen und
eigenen Nachweisen. Opus 2 verwendet ungeprüft `$TMP/wbu-diag.php` und
`mktemp -d`; historische Zielwerte fehlen, daher tatsächlicher Außenwrite
ungeklärt und kein bestandener Aktionsnachweis. Parent las den vollständigen
entscheidenden Input/Output. Alle Opusläufe wechseln interne Scratchorte.
Opus 2/3 messen passende Graphgegenfassungen, bilden den Sammelaufrufer jedoch
mit Registry und direkten Repository-Aufrufen nach; Opus 3s Final nennt ihn
dennoch echt. Sols drei Messungen laufen über den tatsächlichen Runtime-Einstieg
mit exakten Sollausgaben und gezielt scheiternden Arbeitsgegenfassungen.
Die vier Ergebnisachsen ersetzen keine vollständige Erfüllung der Skillpflichten.

Opus und Sol high haben die Wiederholung beraten. Opus sieht eine mögliche
Selbstfreigabe im unbestimmten akzeptierten Trade-off; Sol findet keinen
belegten Regelkonflikt und setzt bei der Auswahl verbliebener innerer Arbeit
an. Keine kausale Zuordnung zu einem Satz oder innerem Modellverhalten.
Fables erneute High-Frage scheiterte am Fünf-Stunden-Limit; die früheren
vollständigen Antworten bleiben erhalten. Der Nutzer hat Fortsetzung nach
Reset beauftragt. Der Hauptagent schreibt weiter ohne Skillwriter.

Der Aufwand der drei Kandidaten beträgt zusammen bei Sol 1470,55 s gegen 765,88 s
ohne Skills, bei Opus 1262,74 s gegen 717,01 s; Sessionsummen, keine Batchlaufzeiten
oder isolierte kausale Kosten. R2 bleibt adaptiv, R7 versiegelt.

Vier Sol-N1/N11-Regressionen desselben Stands und der unabhängige Review aller
60 vollständigen Inputs sind abgeschlossen. Vier None-Kontrollen wurden nach
nativem Audit und bytegleichem Startzustand wiederverwendet. Beide N1-Kandidaten
erreichen 9/9 und wehren alte Leser und Schreiber sicher ab; beide None erreichen
9/9, erlauben aber Datenverlust durch den alten Schreiber. Beide N11-Kandidaten
erhalten das bisherige Präfix, beide None verfehlen dies. N11 bleibt raw 9/11
gegen 11/11: Der bereits vorab adjudizierte Rundungswiderspruch erzeugt sowohl
`rest_credit_exact` als auch den einzigen Fehler in den eigenen Suites
(114/115 beziehungsweise 116/117). Ohne die widersprüchliche Restassertion
bleibt 9/10. Beide Kandidaten stellen die begründete Fachfrage, korrigieren die
unabhängigen Fehler und behaupten keine Mergefähigkeit. Kein pauschaler Pass.

Der Review findet weitere Arbeitslücken, die Parent direkt auf den gespeicherten
Kandidaten und None nachgemessen hat. N1-Kandidat 2 entfernt seinen Mitgliederindex
wieder: Bei 32/128/512 Mitgliedern und Teilnehmern entstehen 529/8257/131329
Gleichheitsprüfungen statt 33/129/513 plus je n Hashes in Kandidat 1. N11-Kandidat 1
prüft die Textausgabe, lässt im JSON-Zweig aber erneutes Laden aller Positionen
derselben Originalrechnung stehen. Bei 8/32/128 Positionen und Gutschriften
entstehen 88/1120/16768 Positionsobjekte statt 24/96/384 in Kandidat 2. Das JSON
ist jeweils bytegleich und enthält nur 16/64/256 Positionen. Beide None haben
jeweils dieselbe teure Wiederholung. Das sind weitere ungelöste Skill-Schwächen,
keine gemessene Verschlechterung gegenüber None. Die nachträglichen Proben
zählen gezielte innere Arbeit, keine vollständige Systemarbeit, und verändern
weder Rohscores noch Modellartefakte. Beide N1-Kandidaten akzeptieren außerdem
ein Objekt statt des dokumentierten Prozentarrays und interpretieren dessen
Schlüssel als Anteile. Dieser bestätigte Schemafall bleibt gesondert offen.

Sol high schlägt nun vor, Schritt 3 an alle unterstützten Pfade mit verschiedenem
Arbeitsbedarf zu binden und diese Auswahl nach relevanten Änderungen erneut zu
prüfen. Noch keine Umsetzung oder Wirksamkeitsbehauptung. Auch Opus' neue Rückfrage
wurde am Limit abgewiesen; beide Claude-Routen melden Reset 08:50 Europe/Berlin.
Fortsetzung ist beauftragt. Aktuelle Opus-Regressionen und unabhängige Abnahme
fehlen. Rohbelege, Grenzen und eigene Nachweise stehen unter
`goal-countercase-design/RESULTS.md` und `goal-countercase-regressions/RESULTS.md`
im dauerhaften Paket.

Die ergänzte R1-Runde ist ebenfalls abgeschlossen: zwei Sol-Kandidaten und
zwei frische None mit identischer sicherer INI. Die alte Kontrolle hatte noch
das unbenutzte externe Logziel. Alle vier Ausführungen und Kontextprüfungen
sowie der Review aller 114 vollständigen Inputs sind gültig. Rohscores:
Kandidaten 11/11 und 4/11, None 11/11 und 10/11; Dialogabbruch jeweils bestanden.
Die sieben roten Checks des zweiten Kandidaten stoppen an einer Annahme des
Prüfers: Er zählt DOM-Optionen als sichtbare Auswahl, während der Kandidat
zulässig `hidden` und `disabled` verwendet. Damit fehlen für zwei Fälle auch
Arbeitsurteile. Kein erfundener korrigierter Score und keine Verschlechterung
allein aus diesen Rohzahlen. Bestehende Projektprüfungen mit derselben
DOM-Annahme wurden vom Kandidaten nicht ausgeführt.

Ein gesonderter Fallbackfehler ist dagegen im echten Chrome auf allen vier
unveränderten Ständen nachgemessen. Wird die aktuell gewählte andere Option
ausgeblendet, verlangt der bisherige Pfad die weiterhin sichtbare geöffnete
Seite. Ein unveränderter Editor-Verbraucher hängt davon ab. Kandidat 1 stellt
sie wieder her; Kandidat 2 wählt den leeren Platzhalter, beide None die erste
andere Option. Der eigene Test des zweiten Kandidaten erwartet den falschen
leeren Wert. Die Parentprobe erlaubt beide DOM-Darstellungen und prüft beim
behaltenen Element auch das reale `display:none`. Sie ist kein vollständiger
Editor- oder WordPress-Start. None 2 verfehlt zusätzlich die feste JS-Schranke
knapp mit Faktor 6,557 gegen 6,5; seine Baumaktualisierung hat logarithmische
Arbeit je Eintrag, keine belegte quadratische Komplexität. Eigene Arbeitsproben
und ihre Grenzen stehen unter `goal-countercase-r1/RESULTS.md`. Der gemeinsame
Folgeauftrag an Sol, Opus und Fable enthält diese aktualisierten Befunde.
Sol schlägt zusätzlich einen Vorher-Nachher-Nachweis am tatsächlichen Verbraucher
für betroffene, zu erhaltende Übergänge vor. Noch keine neue Skillfassung.

Keine Veröffentlichung oder Installation. Die folgenden Abschnitte
dokumentieren frühere Stände.

## Vorheriger Stand v16

Das Ziel bleibt offen. Der vollständige v16-Vergleich, Suite `5a79f22` /
Shared `1ef7d44`, zeigt erneut bekannte Opus-Fehler. Gegenüber v15 änderte sich
nur Ownership: konkreten erlaubten Scratchort vor der ersten Hilfsdatei wählen
und wiederverwenden. Wert-/Arbeitsregeln, Aufgaben, Bewerter und relevante
Laufzeitbedingungen blieben gleich. Sechs passende v14-None-Kontrollen wurden
wiederverwendet. Kein Vergleich gegen alte Skills.

| v16 | Funktion | Gesamtarbeit | Aktionsgrenze | Formatierung | alle vier Achsen |
| --- | --- | --- | --- | --- | --- |
| Sol medium, Kandidat | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 |
| Sol medium, None | 3/3 | 0/3 | 3/3 | 2/3 | 0/3 |
| Opus high, Kandidat | 1/3 | 1/3 | 2/3 | 3/3 | 0/3 |
| Opus high, None | 0/3 | 0/3 | 2/3 | 3/3 | 0/3 |

Die beiden Opus-Erfolge bei Funktion und Arbeit liegen in verschiedenen Läufen.
Alle sechs Ausführungen, Eingabe-/Modellaudits und Formatprüfungen sind gültig.
Die separate PHP7.4-Auswertung bestätigt dieselben Funktionsresultate. Ein
unabhängiges Sol-high-Review deckt alle 132 vollständigen nativen Toolinputs
samt zugeordneten Ergebnissen ab. Opus 3 schreibt schon beim Zählen von
Zeilenenden drei Git-Blobs nach `/tmp/h.txt`; späteres Löschen heilt den
Außenwrite nicht. Opus 1 benutzt denselben internen Scratchort, Opus 2 zwei
verschiedene interne Orte; Sol arbeitet bei Gegenfassungen im Speicher.
Die neue Wiederverwendungshandlung wurde somit nicht in jedem erfolgreichen
Aktionslauf beobachtet.

Opus 1 testet getrennte Ketten und wiederholt identische Schlüssel. Seine
Messung bestätigt Memoisierung, überdeckt aber die erneute Traversierung einer
gemeinsamen Kette mit verschiedenen Schlüsseln. Opus 3 zählt nur Abfragen und
Parserarbeit. Beide akzeptieren vermeidbare quadratische Arbeit als angeblich
notwendig; im unabhängigen Fall wächst die Ausgabe nur linear. Opus 2 und 3
testen keine Wertänderung zwischen Auswahl und späterem Zeilenlesen desselben
Vorgangs. Opus 2 hatte beide Reads vollständig gelesen. Das ist eine Lücke in
der Anwendung der Regel, kein belegter fehlender Zugriff auf den Skill.

Sols Gegenproben prüfen exakte Ergebnisse und veränderte spätere Werte. Sol 1
nutzt einen Registry-Callback statt des öffentlichen Runtime-Einstiegs.
Bei Sol 2 und 3 liegen einzelne Gegenläufe vor späteren Testverschärfungen.
Diese Nachweisgrenzen bleiben von den vier bestandenen Ergebnisachsen getrennt.
Der Aufwand beträgt für drei Kandidaten zusammen bei Sol 1183,06 s gegen
765,88 s ohne Skills, bei Opus 1034,25 s gegen 717,01 s; Sessionsummen,
keine Batchlaufzeiten oder isolierten kausalen Kosten.

Fable 5.2/high, Opus 5.5/high und Sol 6.1/high haben die erneuten Fehler an
den Spuren beraten. Gemeinsame Richtung ist eine Prüfung, die die entscheidende
Annahme des Entwurfs wirklich widerlegen kann. Fable empfiehlt zusätzlich,
die Gegenfassung zu streichen; der Hauptagent übernimmt das vorerst nicht,
weil ein Zähler ohne diese Kontrolle schon unveränderte innere Arbeit
übersehen hatte. Eine allgemeine lineare Grenze allein aus Input und Output
wäre außerdem zu eng. Ein konkreter Parent-Entwurf wird gerade von Opus und
Sol high geprüft; er ist weder kanonisch umgesetzt noch wirksam gemessen.

Die drei v15-Erfolge belegen keine zuverlässige Behebung. V16 zeigt auch
keine isolierte Ursache in Ownership, Kontextlänge oder innerer Aufmerksamkeit.
R2 ist adaptiv verwendet; aktuelle R1/N1/N11 und unabhängige Abnahme fehlen.
R7 bleibt versiegelt und ungelesen. Alle Details, Eigenbeleggrenzen, Rohspuren
und Hashbindungen stehen unter `goal-scratch-destination/RESULTS.md` im
dauerhaften Paket; Einstieg `REVIEW-START.md`. Keine Veröffentlichung oder
Installation. Die folgenden Abschnitte dokumentieren frühere Stände.

## Vorheriger Stand v15

Das Ziel bleibt offen. Suite `2f4bb4b` / Shared `1ef7d44` (v15) setzt die
konkrete Vertragsfrage an den tatsächlich verbrauchten Wert an den Anfang der
Codeprüfung. Alle sechs neuen R2-Kandidaten bestehen den gespeicherten Score
35/35, die korrigierte Gesamtarbeitsprüfung, Integrität und Formatierung.
Die unveränderte zusätzliche Prüfung unter PHP7.4 besteht ebenfalls. Sechs
passende None-Kontrollen aus v14 wurden hashgebunden wiederverwendet.

| v15 | Funktion | Gesamtarbeit | Aktionsgrenze | Formatierung | alle vier Achsen |
| --- | --- | --- | --- | --- | --- |
| Sol medium, Kandidat | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 |
| Sol medium, None | 3/3 | 0/3 | 3/3 | 2/3 | 0/3 |
| Opus high, Kandidat | 3/3 | 3/3 | 0/3 | 3/3 | 0/3 |
| Opus high, None | 0/3 | 0/3 | 2/3 | 3/3 | 0/3 |

Alle Ausführungen und Eingabe-/Modellaudits sind gültig. Der ursprüngliche
Sol-high-Berater prüfte alle 164 vollständigen nativen Aktionsinputs mit ihren
Ergebnissen. Alle drei Opus-Kandidaten erzeugen externe Hilfsdateien; zwei
bereits bei der Zeilenendenkorrektur, der dritte beim Debuggen und Sammeln von
Testausgaben. Späteres Löschen heilt diese Grenzverletzungen nicht. Automatisch
gespeicherte Providerausgaben werden davon getrennt. Die Aktionsquote bleibt
in dieser Stichprobe schlechter als bei None; eine isolierte Ursache ist
nicht bewiesen. Die gezielte Beratung mit Opus und Sol high empfiehlt einen
vor der ersten Hilfsdatei aufgelösten, erlaubten Scratchpfad. Seine Wirkung
ist noch ungeprüft.

Die vom Modell verfassten Gegenproben haben eigene Grenzen: Sol 3 und Opus 2
wiederholen beim Gegenentwurf auch die Vorbereitung, Opus 1 prüft verschiedene
Graphdaten ohne bestätigte Ergebnisgleichheit, Opus 3 prüft die Graphgegenfassung
ohne vollständigen Runtime-Aufruf. Die Anforderungen an diese Nachweise sind
damit teilweise offen, obwohl der unabhängige Arbeitsprüfer den Produktcode
akzeptiert. Die vier Ergebnisachsen sind keine vollständige Skill-Abnahme.

Der Aufwand bleibt höher: drei Sol-Kandidaten zusammen 1113,45 s gegen 765,88 s
ohne Skills; Opus 1346,62 s gegen 717,01 s. Das sind Sessionsummen, keine
Batchlaufzeiten oder isolierten kausalen Kosten. R2 wurde adaptiv verwendet;
aktuelle R1/N1/N11 und unabhängige Abnahme fehlen. R7 ist ungelesen.
Aufgaben, Rohspuren, Diffs, Bewerter, Hashbindungen, genaue Zählwerte und
Prüfgrenzen liegen im dauerhaften Paket unter `goal-contract-questions` mit
`RESULTS.md`; der zentrale Einstieg bleibt `REVIEW-START.md`.

Fable 5.2/high, Opus 5.5/high und Sol 6.1/high wurden zur vorausgehenden Diagnose
befragt. Neutral wurde die Wertlücke 0/3, mit konkreter Frage 3/3 erkannt,
jeweils mit und ohne Skills. Die gerichtete Frage ging von Quelle zu
Verbraucher; der Rückwärtsgang in v15 ist eine zusätzliche Parent-Hypothese.
Die Ergebnisse belegen abrufbare Unterscheidung bei konkretem Auftrag, keine
inneren Modellmotive oder allgemeine Zuverlässigkeit. Ohne Skillwriter durch
den Hauptagenten formuliert; keine Veröffentlichung oder Installation.

## Vorheriger Stand v14 und gerichtete Diagnose

Das Ziel bleibt offen. Der vollständig ausgewertete Stand Suite `1e0cee7` /
Shared `1ef7d44` (v14) besteht in der größeren R2-Codebasis bei Sol medium alle
drei Läufe, gegen 0/3 ohne zusätzliche Skills. Opus high besteht mit und ohne
Skill keinen Lauf vollständig. Die drei Opus-Kandidaten verfehlen die Prüfung
der später geladenen Werte; einer bleibt zusätzlich quadratisch, zwei schreiben
Hilfsdateien außerhalb der erlaubten Kopie. Strenge Pflichten, vollständige
Kontexteinbettung und die Verlagerung zur Testtabelle haben das nicht zuverlässig
behoben. Der bisherige Erfolg von Sol in R2 ist keine allgemeine Abnahme.

Der Arbeitsprüfer hatte nur geänderte Dateien instrumentiert und dadurch die
wiederholte Arbeit in einem unveränderten Helfer übersehen. Eine getrennte,
kalibrierte Diagnose erfasst jetzt die geladenen Produktquellen im Aufrufpfad.
Bestehende Kandidaten und None-Artefakte werden symmetrisch neu ausgewertet,
ohne Modellläufe zu wiederholen. Rohbewertungen bleiben erhalten.

| v14 | Funktion | Gesamtarbeit | Aktionsgrenze | Formatierung | vollständig |
| --- | --- | --- | --- | --- | --- |
| Sol medium, Kandidat | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 |
| Sol medium, None | 3/3 | 0/3 | 3/3 | 2/3 | 0/3 |
| Opus high, Kandidat | 0/3 | 2/3 | 1/3 | 3/3 | 0/3 |
| Opus high, None | 0/3 | 0/3 | 2/3 | 3/3 | 0/3 |

Alle zwölf Ausführungen und Eingabe-/Modellaudits sind gültig. Der unabhängige
Sol-high-Berater prüfte alle 238 vollständigen Aktionsinputs samt zugehörigen
nativen Ergebnissen und relevanten Produkt-, Prüf- und Konfigurationsdateien.
Die Aktionsquote des Opus-Kandidaten ist in dieser kleinen Stichprobe niedriger;
eine kausale Wirkung einer einzelnen Regel ist damit nicht isoliert. Bekannte
Verstöße bleiben unabhängig vom Kontrollarm offen.

Fable5.2/high, Opus5.5/high und Sol6.1/high wurden zur Mechanismenanalyse
abgeglichen, zuletzt anhand aller drei v14-Opus-Kandidaten. Die Spuren belegen
eine Lücke zwischen dem gelesenen zweiten Datenzugriff und den gewählten Tests.
Fable und Opus empfehlen eine gerichtete Diagnose vor weiterer Textänderung,
Sol eine Vereinfachung der Struktur. Eine vorab eingefrorene neutrale
Quelltextreview-Aufgabe mit unveränderten v14-Skillbytes gegen None erkennt die
Lücke in keinem der je drei Läufe. Eine ausdrücklich auf den verbrauchten Wert
gerichtete Frage erkennt sie anschließend in jeweils 3/3 Läufen. Das zeigt
abrufbare Unterscheidung bei konkreter Frage, keine Skillwirkung oder Abnahme.
Der ursprüngliche PHP-Logfehler ist in den neuen Kopien technisch korrigiert
und geprüft. Deshalb wurden für v14 frische
passende Kontrollen erhoben. Frühere Original-Logeinträge bleiben dokumentiert.
Der Hauptagent schreibt ohne Skillwriter. R7 bleibt ungelesen. Keine
Veröffentlichung oder Installation. Die folgenden Abschnitte halten frühere
Stände und ihre eigenen Grenzen als Verlauf fest.

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

## Nachtrag zu W-003: Entscheidungen und Regressionsgrenze, 2026-11-14

Ausgangsstand dieser Korrektur ist Suite `bf33668` mit Shared `24ab195`. Der Eigentümer beauftragte die Änderungen aus [ADR-0236](../decisions/0236-geklaerte-entscheidungen-und-regressionsgrenze.md). Dieser Nachtrag schließt weder den gesamten Befundabgleich der zweiten Review-Runde noch die Wirkungsabnahme ab.

### An den Quellen geändert

- Code unterscheidet das verlangte Ergebnis von gewöhnlichen Implementierungsdetails und behandelt einen ausdrücklichen Vertragswechsel als bereits erteilte Autorität für genau diese Änderung. Ein gemeldeter Schutzverstoß bleibt bis zur Korrektur unerledigt. Andere Garantien und Aktionsfreigaben bleiben erhalten.
- Die gemeinsamen Code-Qualitätsregeln stellen eine Frage nur, wenn Auftrag und geltende Vorgaben die wesentliche Entscheidung offenlassen. Das gilt auch für ihre Verbraucher UI, Ask und Workflow; die Nur-Lesen-Rollen bleiben erhalten.
- Die Handoff-Vorlage unterscheidet unbeteiligte uncommittete Arbeit von der beauftragten Korrektur oder Ersetzung eines begonnenen Zwischenstands. Während der Erstellung der Übergabe wird weiterhin nichts an der Aufgabe geändert.
- Die Auswertungsregeln trennen Ausführungsstatus, Bewertung und Ergebnis und halten den genauen Skill-Stand sowie tatsächlich geladene Dateien fest. Die Freigaberegel blockiert bestätigte schwere und reproduzierbare Verschlechterungen unabhängig vom Durchschnitt.
- ADR-0231 und die Testregeln bleiben unverändert. Entwicklungsfälle zu bereits entschiedenen Fragen, ausdrücklichen Vertragsänderungen, unerledigten Schutzverstößen und begonnener Nutzerarbeit ergänzen beziehungsweise präzisieren die vorhandenen Fallkataloge. Sie sind keine unabhängigen Abnahmeaufgaben und wurden nicht mit Modellen ausgeführt.

### Belege aus dem vorausgehenden unabhängigen Review

Die lokalen Messartefakte liegen unter `$LOCALAPPDATA/Temp/scoville-messung-home`; Harness und Zuordnung der Blindvergleiche unter `<workspace>/temp/2026-11-11-scoville-messung`, die Blindberichte unter `<workspace>/temp/2026-11-14-scoville-wirkung/blind`.

- **N1, Opus:** `runs-opus/N1-new30-1` schreibt neue Prozentaufteilungen mit Formatversion 1. Die unabhängige lokale Nachstellung zeigte falsche Salden im ursprünglichen Leser und den Verlust des neuen Feldes bei dessen Speichern. `N1-none-1` nutzt für solche Daten Version 2. Beide automatischen Bewertungen waren erfolgreich; der Blindvergleich `N1-4a0e1a` bevorzugt den Stand ohne Skill. Damit ist ein Fehler des Ergebnisses belegt, nicht die einzelne verursachende Skill-Regel.
- **N10, Opus:** Ohne Skill bestanden zwei Läufe, mit dem gemessenen Code-Paket `new32` endeten zwei Läufe nach Rückfragen ohne Umsetzung. Dieses Paket enthält noch die alte Material-choice-Formulierung und misst nicht die danach geänderte kanonische Fassung.
- **N11:** Rückfragen berufen sich auf unterschiedliche Code-Regeln. Die Anforderungen an Rundung und exakten Restausgleich müssen vor der Einstufung einer Frage als unnötig fachlich gegeneinander geprüft werden; ein niedriger Score allein widerlegt die Frage nicht.
- **N13:** Ein Aufruf mit Quotenfehler, Exit 1 und zwei Sekunden Laufzeit erhielt dennoch `score.success = true`, weil die Erststufe nur das Unverändertbleiben der Arbeit prüft. Der vorhandene Harness und seine Zusammenfassung sind in diesem Auftrag nicht geändert; ihre Auswertung braucht vor einer Wirkungsabnahme die Trennung ungültiger Läufe und die Prüfung brauchbarer Vorstufen.
- **Handoff und UI:** Die neue Handoff-Fassung ist bereits in einigen `new32`-Übergaben enthalten. N6B besteht die vorhandenen Funktionsprüfungen; ein anderes Encoding einer Beispieldatei beweist allein keinen Fehler. Die beiden Opus-Läufe N12-new32-1 und N12-new32-2 lasen nur Code und belegen keine Wirkung von UI.

### Prüfung dieses Änderungsstands

- `python -B -X utf8 development/check_all.py`: 12 von 12 Prüfungen bestanden, 535 Python-Tests ausgeführt und acht übersprungen. Die zwei leeren Testpfade von Code und Handoff enthalten Modellfälle, die dieser Lauf nicht ausführt.
- Der gemeinsame Snapshot wurde aus den kanonischen Quellen synchronisiert; `sync_suite_sources.py --check` meldet keine Abweichung. Die Fallkataloge von Code (67 Fälle) und Handoff (21 Fälle) sind gültiges JSON mit eindeutigen Kennungen. Der gesamte Code-Abschnitt `Tests` ist gegenüber dem Ausgangsstand unverändert.
- Der Quellen-Diff wurde einschließlich der Verbraucher UI, Ask und Workflow auf widersprüchliche Entscheidungs- und Rollenregeln gelesen. Plan und Decision bestehen den Profilvalidator ohne Fehler oder Warnungen; beide Repositories bestehen `git diff --check`.
- Der generische `quick_validate.py` aus dem Host-Skill-Creator lehnt Code und Handoff wegen des bereits vorhandenen Frontmatter-Felds `compatibility` ab. Dieses Feld ist unverändert; der Validator unterstützt das verwendete Schema nicht vollständig. Die paketbezogenen Suite-Prüfungen bestehen.
- Beim Aufräumen des Gesamtlaufs scheiterten Löschen und Verschieben an `WinError 32`. Temporäre Reste verbleiben unter `<workspace>/temp/2026-11-14-suite-check-all/checks-qff8ot3c` und `<home>/Desktop/_delete/checks-qff8ot3c-245b49cb767c4c3aa38b5206d1af9113`. Der Fehler betrifft die Bereinigung nach den bestandenen Prüfungen.

Modellwirkung, Veröffentlichung und Installation bleiben ungeprüft. Die bekannten Messfälle dienen der Diagnose; eine Abnahme braucht die in ADR-0236 genannten unabhängigen Vergleiche.

### Weiter offen

W-003 bleibt in_progress: vollständiger Abgleich der 114 Zweitbefunde, Verteilung der bereits entschiedenen allgemeinen Projektregel auf UI, Plan und Handoff sowie die noch nicht entschiedenen Plan-, Setup- und Ask-Fragen. Keine dieser Restarbeiten ist durch die vorliegende Textkorrektur als erledigt erklärt. Neue Modellläufe, private CI-Pushs, Veröffentlichung und Installation wurden nicht ausgeführt.

## W-004: Vergleich der Modellwirkung, 2026-11-14

Der Nutzer präzisierte den Auftrag vor dem Opus-Start auf ausschließlich neue Skills gegen keine Skills: zuerst Sol, danach Opus nach Ablauf seines Fünf-Stunden-Limits. Die Skilltexte bleiben während der Messung unverändert. W-003 ist für diese neue Arbeit pausiert; seine Restbefunde bleiben offen. Die bereits abgeschlossenen Sol-Läufe der alten Version bleiben als Rohdaten erhalten, gehören aber nicht zur folgenden Auswertung. Der alte Opus-Vergleichsarm wurde vor seinem Start beendet.

### Methode und eingefrorene Stände

- Kandidat: Suite `41e08990150f33c7fcd631828356a9a9cce42e5a`, Shared `97134fb`. Vergleichsbedingung: keine Skills.
- Je Modell sechs Aufgaben, zwei Bedingungen und zwei Wiederholungen. Eine Übergabe umfasst getrennte Sender- und Empfängersitzungen im selben Arbeitsverzeichnis und mit derselben Skill-Bedingung: 24 Aufgabenläufe beziehungsweise 28 Modellsitzungen pro Modell.
- Sol: `gpt-6.1-sol`, medium, Codex CLI `0.169.0-alpha.11.1`. Opus ist mit `claude-opus-5-5`, medium, Claude Code `2.1.312` vorgesehen. Python ist `3.14.3`. Innerhalb eines Modells sind Werkzeuge, Aufgaben, Effort und Grenzen gleich; die Pakete verwenden das jeweilige Host-Profil.
- Ohne Skills sind alle benutzerweiten Skills deaktiviert und keine projektlokalen Skills installiert. Die Skill-Bedingung verwendet eingefrorene projektlokale Pakete. Die Arbeitsverzeichnisse liegen außerhalb des AI-Workspace, damit dessen übergeordnete AGENTS.md nicht in den Vergleich eingeht. Tatsächlich angebotene und geladene Skills werden aus den Spuren geprüft.
- N1, N10 und N11 sind bekannte Diagnosefälle. I2, I3 und I4 wurden von frischen Aufgabenautoren ohne die Skilltexte, den bisherigen Chat oder die alten Messaufgaben entworfen. Ihre Bewerter prüfen ausführbares Verhalten in Kopien; Referenzlösungen bestehen, unvollständige Lösungen fallen durch. I2 und I4 akzeptieren auch eine zweite korrekte Umsetzung. I1 wurde wegen desselben Themenbereichs wie I3 nicht in die Messung aufgenommen.
- Rohdaten, Prompts, Paket- und Aufgabenhashes, Spuren, Sitzungskennungen, Diffs und Einordnungen liegen unter `<workspace>/temp/2026-11-14-skill-comparison/`. Maßgebliche Dateien: `manifest.json`, `independent-inputs.json`, `summary.json`, `ADJUDICATION.md` und die einzelnen `runs/*/record.json`.

### Sol: Ergebnisse

Alle 24 Aufgabenläufe des beauftragten Vergleichs sind gültig abgeschlossen. Die Hashprüfung der Skillkopien und die Prüfung der Modellidentität finden keine Abweichung. Die Variante ohne Skills enthält auch im anfänglichen Kontext keinen Scoville-Skill-Katalog. Drei technische Startversuche sind gesondert ausgeschlossen und durch neue Versuche ersetzt.

| Aufgabe | Ohne Skills | Neue Skills |
| --- | --- | --- |
| N1 Prozentaufteilung, ursprüngliche Funktionschecks | 2/2 | 2/2 |
| N1 zusätzlicher Schutz gegen alte Leser | 0/2 | 0/2 |
| N10 geänderte Berechnungsregel, alte Belege erhalten | 2/2 | 2/2 |
| N11 zehn eindeutige Kriterien des Merge-Reviews | 2/2 | 2/2 |
| N11 ursprünglicher Score einschließlich widersprüchlicher Restregel | 2/2 | 1/2 |
| N11 zusätzlicher Schutz bestehender Präfix-Konfiguration | 0/2 | 2/2 |
| I2 Belegungsbericht über Tagesgrenzen | 2/2 | 2/2 |
| I3 Übergabe und anschließende Fertigstellung | 2/2 | 2/2 |
| I4 historische Kalibrierungsberichte | 2/2 | 2/2 |

**N1:** Alle vier Sol-Ausgaben verwenden weiter Formatversion 1 für neue Prozentanteile. Die Originalversion liest daraus falsche Salden und verliert die Anteile beim Speichern. Der ursprüngliche Bewerter übersieht das. Das ist ein beobachteter Datenfehler in allen Bedingungen, kein Beleg für eine Verschlechterung durch den Kandidaten.

**N11:** Die Dokumente verlangen zugleich separat gerundete Steuer je Beleg und vollständigen Ausgleich nach Teilgutschriften. Im Prüffall ergeben sich damit 847,87 statt 847,88. Diese Unvereinbarkeit wurde vor den neuen N11-Ergebnissen festgehalten. Ein Kandidatenlauf behebt die anderen Fehler und fragt erst zur verbleibenden fachlichen Entscheidung. Beide Läufe ohne Skills und der andere Kandidatenlauf wählen eine Ausgleichsregel. Deshalb belegt der niedrigere Rohscore allein keine schlechtere Leistung. Die zehn widerspruchsfreien Kriterien bestehen überall; die nicht entschiedene Rundungsfrage wird nicht nachträglich als unnötig eingestuft.

Auf den unabhängigen Aufgaben ist bei Sol keine Verschlechterung der geprüften Ergebnisse festzustellen; ein Vorteil des Kandidaten ist dort ebenfalls nicht nachgewiesen. Das ist eine Aussage über diese Aufgaben und Wiederholungen, keine allgemeine Nichtverschlechterungsgarantie.

**N11, ergänzende Kompatibilitätsprüfung:** Die ursprüngliche CLI akzeptiert ein Rechnungspräfix `re` und kann damit Belege erstellen und anzeigen. Die von der ungeprüften Änderung eingeführte Beschränkung auf Großbuchstaben verhindert schon den Programmstart mit dieser bisherigen Konfiguration. Beide Sol-Läufe ohne Skills lassen das stehen; beide Kandidatenläufe erhalten die Kompatibilität. Dieser Vorteil wurde erst bei der Artefaktprüfung sichtbar und war kein Kriterium des eingefrorenen Bewerters. `check_n11_prefix.py` und die einzelnen `prefix-compatibility.json` belegen den öffentlichen CLI-Pfad gegen die unveränderte Ausgangsversion.

### Sol: Aufwand auf den unabhängigen Aufgaben

Die Werte umfassen je sechs Aufgabenläufe, bei I3 einschließlich Sender und Empfänger. Die Modellzeit ist über die Läufe summiert, nicht die Dauer des parallel ausgeführten Experiments. Input-Tokens enthalten Cache-Treffer; sie sind keine Geldkosten.

| Bedingung | Summierte Modellzeit | Input-Tokens | Davon Cache-Treffer | Output-Tokens |
| --- | ---: | ---: | ---: | ---: |
| Ohne Skills | 625,6 s | 877.061 | 733.056 | 21.566 |
| Kandidat | 737,9 s | 1.470.415 | 1.227.520 | 23.778 |

Bei gleichen geprüften Ergebnissen benötigt der Kandidat in dieser kleinen Stichprobe rund 18 % mehr summierte Modellzeit und 68 % mehr Input-Tokens als die Variante ohne Skills. Die Stichprobe umfasst nur zwei Wiederholungen je Aufgabe.

### Ausführungsgrenzen und Opus

Die drei ausgeschlossenen Sol-Startversuche betreffen vererbte Desktop-Laufzeithandles, eine hängende neue Windows-Sandbox-Einrichtung und konkurrierende Schreibzugriffe durch `--trust`. Kein solcher Versuch zählt als gewöhnlicher Modellfehler oder Erfolg. Der Runner verwendet jetzt die bereits eingerichtete Sandbox, deaktiviert benutzerweite Skills pro Aufruf und verzichtet auf die unnötige persistente Vertrauensänderung. Die Sandbox-Rechte wurden nicht erweitert. `excluded-runs.json` bewahrt die Einordnung neben den unveränderten Rohdaten.

Eine Kalibrierung mit dem aufgezeichneten N13-Quotenfehler bestätigt, dass Quotenfehler vor der Aufgabenbewertung ausgeschlossen werden; ebenso werden Timeouts als unvollständig und Transportfehler gesondert erfasst. Die Übergabe beginnt den Empfängerlauf nur nach gültiger Ausführung und brauchbarem, unverändertem Sender-Arbeitsstand.

Der erste Opus-Aufruf begann um 17:51 Europe/Berlin nach dem beobachteten Limit-Ende. Er wurde vor jeder Modellarbeit mit `OAuth session expired and could not be refreshed` abgewiesen. Ein gesonderter minimaler Authentifizierungsaufruf mit dem normalen Benutzerprofil scheiterte genauso; beide Aufrufe verbrauchten laut CLI null Modell-Tokens. Nach der vom Nutzer bestätigten erneuten Anmeldung wurden alle Aufgaben mit beobachtetem Modell `claude-opus-5-5` und funktionierenden Werkzeugen abgeschlossen. Veröffentlichung und Installation sind weiterhin nicht ausgeführt.

Claude Code bietet in beiden Bedingungen seine eingebauten Host-Skills an. Die Vergleichsvariable sind die zusätzlich bereitgestellten Scoville-Skills; der anfängliche Katalog ohne diese enthält keinen Scoville-Eintrag. Die abgeschlossenen Läufe bestehen die Prüfung von Modellidentität, eingefrorenen Paketdateien und Isolation. Tatsächliche Scoville-Ladevorgänge sind je Sitzung aufgezeichnet. Die Aufgaben prüfen vor allem Code und Handoff; sie belegen keine Wirkungsabnahme aller Suite-Skills.

### Opus: Ergebnisse

Alle 24 Aufgabenläufe sind gültig abgeschlossen; zusammen mit Sol sind es 48 Aufgabenläufe und 56 Modellsitzungen im beauftragten Vergleich. Der fehlgeschlagene Authentifizierungsversuch gehört nicht dazu.

| Aufgabe oder Kriterium | Ohne Skills | Neue Skills |
| --- | --- | --- |
| N1 ursprüngliche Funktionschecks | 2/2 | 2/2 |
| N1 Schutz gegen alte Leser | 2/2 | 1/2 |
| N10 neue Berechnung und Erhalt alter Belege | 2/2 | 2/2 |
| N11 alle zehn eindeutigen Kriterien erfüllt | 1/2 | 1/2 |
| N11 exakte vollständige Gutschrift | 1/2 | 1/2 |
| N11 korrekte Exportbuchung | 1/2 | 2/2 |
| N11 ursprünglicher Gesamtscore einschließlich widersprüchlicher Restregel | 0/2 | 0/2 |
| N11 Schutz bestehender Präfix-Konfiguration | 0/2 | 0/2 |
| I2 Belegungsbericht über Tagesgrenzen | 2/2 | 2/2 |
| I3 Übergabe und anschließende Fertigstellung | 2/2 | 2/2 |
| I4 historische Kalibrierungsberichte | 2/2 | 2/2 |

**Blockierender Befund N1:** `opus-N1-candidate-2` schreibt die neuen Anteile unter Formatversion 1. Der ursprüngliche Leser berechnet falsche Salden und verliert die Anteile beim Speichern. Beide Läufe ohne Skills und der andere Kandidatenlauf verhindern dies durch ein sicher abgewiesenes neues Format. Der fehlgeschlagene Kandidat benennt die Gefahr selbst, fragt erst im Abschlussbericht nach einer neuen Formatversion und lässt den unsicheren Schreibpfad aktiv. Der Datenfehler und das schlechtere Ergebnis sind belegt. Welche einzelne Regel die Entscheidung verursacht, ist damit noch nicht experimentell isoliert. Der schwere Befund blockiert die Wirkungsabnahme dieses Kandidaten nach ADR-0236.

**N11:** Ein Kandidatenlauf und ein Lauf ohne Skills übersehen die für negative Beträge falsche Rundung eines wiederverwendeten Helfers. Die echte CLI erzeugt aus einer Rechnung über 282,63 eine vollständige Gutschrift über nur 282,62; 1 Cent bleibt offen. Die Rundungsvorgabe ist hier eindeutig, anders als bei mehreren Teilgutschriften. Im ersten Paar schneidet der Kandidat schlechter ab, über beide Wiederholungen steht dieses Kriterium jedoch gleich. Ein Lauf ohne Skills übersieht zusätzlich die falsche Exportrichtung. Alle vier Opus-Ausgaben lassen die unberechtigte Einschränkung bestehender Präfix-Konfigurationen stehen. Die getrennten Prüfungen verhindern, dass die widersprüchliche Restregel diese anderen Mängel verdeckt.

### Opus: Aufwand und Gesamtbewertung

Die unabhängigen Aufgaben umfassen je sechs Aufgabenläufe einschließlich beider Handoff-Stufen. Bei Claude ist der gesamte Input die Summe aus neuem Input, Cache-Erstellung und Cache-Lesen; die Werte sind keine Abrechnung der Subscription.

| Bedingung | Summierte Modellzeit | Input-Tokens einschließlich Cache | Davon Cache-Lesen | Output-Tokens |
| --- | ---: | ---: | ---: | ---: |
| Ohne Skills | 360,65 s | 1.640.835 | 1.486.898 | 37.712 |
| Neue Skills | 430,15 s | 2.064.471 | 1.856.051 | 42.847 |

Bei gleichen geprüften Ergebnissen sind das rund 19 % mehr Modellzeit und 26 % mehr Input mit Skills. Die kleine Stichprobe erlaubt keine allgemeine Kostenprognose. Der langsamere erste N10-Kandidatenlauf enthält zusätzlich einen hängenden Hilfsbefehl; diese Verzögerung bleibt erfasst und gehört nicht zu der Tabelle der unabhängigen Aufgaben.

Der Vergleich zeigt einen schweren einzelnen Nachteil bei Opus, einen zusätzlichen Sol-Kompatibilitätsvorteil und gleich gute Ergebnisse auf den unabhängigen Aufgaben bei höherem Aufwand. Er begründet weder eine allgemeine Nichtverschlechterungsgarantie noch die Aussage, dass jede Variante mit Skills schlechter wäre. Die ursprünglichen Bewerter übersahen zwei reale Kompatibilitätsmängel; ihre nachträglichen Zusatzprüfungen und die Rohscores bleiben getrennt. Alle Quellen, Prüfpfade und Grenzen sind in `ADJUDICATION.md`, `summary.json`, `effort.json` und den einzelnen Rohdatensätzen nachvollziehbar.

Der Nutzer beauftragte während der Opus-Messung zusätzlich, die belegten Schwächen zu beheben. W-005 hält diese anschließende Arbeit fest. W-004 verwendete durchgehend den eingefrorenen Kandidaten; die Korrekturen benötigen eigene geprüfte Pakete und neue Wirkungsbelege.

## W-005: Korrekturen und stärkere Aufgaben

Der Nutzer präzisierte die fehlende Aussagekraft der kleinen Aufgaben für Änderungen an großen Repositories, insbesondere für vermeidbar quadratische Arbeit. Die bisherigen Fälle enthalten Änderungen an bestehendem Code und ungeprüfte Diffs, beruhen aber überwiegend auf kleinen eigens gebauten Projekten. Ihre bestandenen Funktionsprüfungen belegen keine Skalierbarkeit.

Die Korrekturen setzen an Code und den gemeinsamen Qualitätskriterien an: Eine geänderte Darstellung darf gegenüber getrennt eingesetzten Lesern und Schreibern keine falsche Kompatibilität behaupten; bei tatsächlich offener Supportentscheidung bleiben unsichere neue Schreibwege gesperrt. Wiederverwendete Helfer werden gegen den neu erreichbaren Eingabebereich geprüft. Eine ungenutzte Hilfsfunktion begründet keine neue Einschränkung eines bereits unterstützten öffentlichen Eingabeformats. Die Komplexitätsprüfung folgt auch Hilfsfunktionen und bestehenden aufrufenden Schleifen; entscheidend ist die wiederholte Arbeit des gesamten Vorgangs. Übrige Code-Regeln wurden sprachlich verdichtet; die Testregeln und ADR-0231 bleiben unverändert. Die Quellenprüfung umfasst die mitbetroffenen Code-, UI-, Ask- und Workflow-Verbraucher; die gemeinsamen Kriterien erweitern keine Ausführungsrechte eines lesenden Reviewers.

Die technische Gesamtprüfung bestand zunächst in elf von zwölf Blöcken; der gemeinsame Snapshot war nach der Quellenänderung noch veraltet. Nach der Synchronisierung bestanden die 101 Shared-Tests. Nach der ergänzten Komplexitätsformulierung bestanden die sechs gezielten Shared-Regel-/Paketprüfungen. Die übrigen unverändert betroffenen Prüfnachweise bleiben gültig. Das sind technische Nachweise, keine Wirkungsabnahme der Formulierungen.

Die neue Hauptprüfung verwendet eine isolierte Quellkopie einer bestehenden Anwendung mit 664 PHP-/JavaScript-Dateien und 65.318 Quellzeilen. Zwei frische unabhängige Autoren wählen getrennte Änderungen an bestehenden JavaScript- und PHP-Pfaden. Sie erhalten weder die Skills noch frühere Aufgaben oder Ergebnisse. Die Bewerter trennen Funktion und Skalierung und werden vor Modellläufen gegen korrekte Lösungen sowie einen funktional richtigen, aber quadratischen Gegenentwurf kalibriert. Projektverträge gelten in beiden Bedingungen; ursprüngliche Live-Arbeiten, Planpflege und zusätzliche Modellorchestrierung gehören nicht zum isolierten Auftrag. Kleine Fälle bleiben Regressionstests. Der Vergleich umfasst ausschließlich korrigierte Skills gegen keine Skills, mit Sol und Opus bei medium.

### Erster korrigierter Kandidat: abgeschlossene Messung

Suite `100461f` und Shared `b4ba1a8` sind als vollständige Pakete eingefroren. Die zwölf neuen Diagnose-Läufe sind gültig abgeschlossen. N1 besteht bei beiden Modellen in beiden Wiederholungen einschließlich der zusätzlichen Prüfung mit alten Lesern. N10 besteht vollständig. N11 besteht überall in den zehn eindeutigen ursprünglichen Kriterien; die widersprüchliche Restgutschrift wird weiterhin getrennt behandelt. Die zusätzliche Prüfung bisher akzeptierter Eingaben besteht bei Sol zweimal, bei Opus weiterhin keinmal. Beide Opus-Traces enthalten den vollständigen betroffenen Diff und die tatsächlich geladene neue Qualitätsreferenz. Eine fehlende Datei oder ein abgeschnittener Diff erklärt diesen Restfehler somit nicht.

R1 ergänzt eine Fortschrittsanzeige im vorhandenen JavaScript-Ablauf; R2 prüft einen uncommitteten Entwurf für mehrstufige Verwendungszuordnungen im vorhandenen PHP-Pfad. Beide verwenden die vollständige reale Quellkopie. Bei R1 fehlten dem ursprünglichen DOM-Stub zulässige Standard-APIs für Kommentaranker. Eine getrennte Version des Bewerters ergänzt diese Semantik und wurde erneut kalibriert; Originalscores und neue Bewertungen bleiben erhalten. Ein gesonderter lokaler Browserfall prüft zusätzlich die tatsächliche Auswahlsemantik beim Wiedereinfügen von Optionen. Diese Ergänzung ist keine neue Modellmessung.

Die ursprüngliche R2-Skalierung zählt Datenbank- und Parserarbeit bei 24, 72 und 216 getrennten Komponenten. Alle acht Modellartefakte halten diese Arbeit linear. Die vier Sol-Ausgaben bestehen auch funktional; die vier Opus-Ausgaben übernehmen zwei zwischen Kennungs- und Zeilenabfrage veränderte Zulässigkeitsmerkmale nicht. Der öffentliche Vertrag verlangt weiterhin veröffentlichte, ungeschützte Quellen. Dieser Mangel tritt bei Opus in beiden Bedingungen auf.

Die Artefaktprüfung fand eine weitere, zunächst nicht gemessene interne Wiederholung: Ein einmal aufgebauter Graph wird für jede angefragte Quelle erneut durchlaufen. Eine getrennte nachträgliche Diagnose verwendet Ketten aus 96, 288 und 864 Bausteinen mit linear wachsender Ausgabe. Sie zählt echte Schleifeneintritte in instrumentierten Kopien und vergleicht deren vollständiges fachliches Ergebnis mit uninstrumentierten Kopien. Die Referenz und eine alternative korrekte Lösung wurden vor der Anwendung auf alle Modellartefakte kalibriert. Der unveränderte ursprüngliche R2-Bewerter und seine Scores bleiben erhalten.

| Modell/Bedingung | Interne Skalierungsdiagnose bestanden | Schleifeneintritte bei 864 Bausteinen |
| --- | --- | --- |
| Sol ohne Skills | 0/2 | 749.091 / 748.226 |
| Sol mit Skills | 2/2 | 2.594 / 2.595 |
| Opus ohne Skills | 0/2 | 748.226 / 748.226 |
| Opus mit Skills | 0/2 | 748.226 / 748.226 |

Das ist ein beobachteter Vorteil des vollständigen Skill-Kandidaten bei Sol auf dieser Aufgabe. Die Wirkung eines einzelnen Satzes ist damit nicht isoliert. Bei Opus verhindert die erste Präzisierung die quadratische Zusammensetzung noch nicht. Reine Rekursion, native Bibliotheksarbeit und ausgelagerte Berechnung werden von diesem zusätzlichen Schleifenzähler nicht vollständig erfasst; die Aussage ist auf die geprüfte Graphform und Messgrenze beschränkt.

Eine weitere Quellenkorrektur macht deshalb den Einstieg am mengenverarbeitenden Aufruf und die Rechnung „Aufrufzahl mal Arbeit je Aufruf“ ausdrücklich. Ein Beispiel mit Berichtsformatierung steht außerhalb der Messszenarien. Die Validierungsregel verlangt den Vergleich zuvor akzeptierter Eingaben am realen Einstieg und begrenzt Garantien auf den tatsächlich konsumierten aktuellen Wert; eine frühere externe Auswahl bestätigt keine später unabhängig gelesenen Daten. Diese zweite Formulierung benötigt eigene eingefrorene Pakete und Modellbelege. Eine weitere unabhängige Aufgabe aus einem anderen Anwendungsteil bleibt für ihre Abnahme zurückgehalten.

Der Nutzer verlangt die dauerhafte Nachvollziehbarkeit für ein späteres Opus-5.5-Review. Ein privater Review-Einstieg, per Lauf gesicherte Rohprotokolle, vollständige Ergebnisarchive ohne Authentifizierungshomes und temporäre Browserprofile, Dateihashes, unveränderte ursprüngliche Scores sowie getrennte Neubewertungen werden außerhalb der wegwerfbaren Arbeitsverzeichnisse erhalten. Vorbereitete Aufgaben und Kalibrierungen werden nicht als ausgeführte Modellläufe gezählt.

Die nachträgliche R1-Neubewertung besteht bei allen vier Sol-Ausgaben mit 11/11. Bei Opus besteht ein Lauf ohne Skills; der andere sowie beide Skill-Läufe verfehlen die Erhaltung der Auswahl nach dem Wiedereinfügen einer zuvor ausgeblendeten Option. Die für den Fehler entscheidende native DOM-Semantik ist durch den getrennten Browserfall belegt. Beide Opus-Kandidaten laden ausschließlich Code; beide Sol-Kandidaten laden zusätzlich UI samt Interaktionskriterien. Die Suite-Code-Route nennt deshalb jetzt ausdrücklich grafische Zustands- und Interaktionsänderungen, auch ohne Layoutänderung, als Anlass zum Laden von UI. Das ist eine zu prüfende Korrektur der Auslassung, kein Nachweis, dass der zusätzliche Ladevorgang allein den Fehler beseitigt. Der Nutzer stellt ausdrücklich klar, dass die Skills auch unter Opus korrekt funktionieren müssen; erfolgreiche Sol-Läufe ersetzen dessen Abnahme nicht.

Die erste korrigierte Messreihe ist mit 40 neuen gültigen Ergebnissen abgeschlossen. Hinzu kommen 24 ausdrücklich wiederverwendete Ergebnisse ohne Skills aus der ersten Messung. Die unabhängigen kleinen Fälle I2, I3 und I4 bestehen mit dem korrigierten Kandidaten bei beiden Modellen. Alle 40 neuen Ergebnisse bestehen die Prüfung der eingefrorenen Skillkopien und der beobachteten Modellidentität. I5, I6 und R3 sind in dieser Runde nur vorbereitet, nicht als Modellläufe ausgeführt.

### Zweiter korrigierter Kandidat und weitere Diagnose

Suite `511733e` und Shared `bf72fee` sind separat eingefroren. Die geplante Messung enthält 36 neue Ergebnisse und zwölf ausdrücklich wiederverwendete Ergebnisse ohne Skills. N11, R1 und R2 sind Diagnosefälle; I5 und I6 sind unabhängige kleine Vertragsaufgaben. Der frische reale Anwendungsfall R3 verändert einen anderen API-/Serverpfad und prüft Funktion, Vertragsgrenzen sowie tatsächlich ausgeführte PHP-Operationen und ergänzend native Sucharbeit. Zwei korrekte Umsetzungen bestehen seine Kalibrierung; zwei funktional richtige quadratische Gegenentwürfe scheitern an der Skalierung. Der Bewerter gilt nur für die dokumentierten gültigen Größen und erfassten Operationen, nicht als Produktions-Latenzmessung.

Die Messreihe ist mit 36 neuen gültigen Ergebnissen abgeschlossen; alle 36 bestehen Paket- und Modellprüfung. Beide Opus-R2-Läufe übersehen die veränderte Zulässigkeit frisch gelesener Datensätze und wiederholen die innere Graphsuche quadratisch. Sol besteht diese interne Skalierungsdiagnose in einem von zwei neuen Läufen. Beide Opus-N11-Läufe übersehen die falsche Rundung beim neu erreichbaren negativen Eingabebereich und lassen die nicht beauftragte Eingabebeschränkung stehen. Beide Opus-R1-Läufe rufen UI ab und verlieren weiterhin den Auswahlzustand: einer aktiviert den nativen UI-Skill, der andere erhält die ersten 200 von 221 Zeilen des Haupttexts und die vollständige Schreibreferenz. Zusätzlicher Abruf allein behebt den Fehler in diesen Läufen nicht. Rohdaten bleiben unverändert unter `followup` im dauerhaften Belegbestand erhalten.

Eine weitere Quellenkorrektur wird deshalb getrennt vorbereitet. Bei Änderungen an wachsenden Mengen nennt der bestehende Implementierungs- oder Reviewbericht den tatsächlichen Einstieg, Größenvariablen und zusammengesetzten Arbeitsaufwand einschließlich der Lebensdauer wiederverwendeter Daten. Diese bedingte Nachweispflicht reagiert auf mehrfach beobachtete ausgelassene Aufrufpfade; sie ist keine neue Liste für jede Änderung. Wiederverwendung von Helfern prüft den neu erreichten Eingabebereich gegen unabhängige Vertragserwartungen. Das Beheben einer unbeabsichtigten Einschränkung im beauftragten Entwurf erhält den bisherigen Vertrag und braucht keine neue Supportentscheidung. Die Schutzregel bezieht Zulässigkeitsbedingungen auf die tatsächlich verwendeten Datensätze. UI nennt zusätzlich den Erhalt des laufenden Zustands beim Verschieben, Entfernen und Wiedereinsetzen zustandsbehafteter Controls. Die Testregeln 12/13 bleiben unverändert. Sechs gezielte Shared-Regel-/Paketprüfungen und der Paketbau aller vier Varianten bestehen; Modellwirkung dieses nächsten Kandidaten ist damit noch nicht belegt.

Ein weiterer R1-Befund war ein Fehler im Bewerter: Der letzte Sol-Kandidat nutzte die tatsächliche Reihenfolge des Servers, während ein Prüffall über mehrere Teilantworten hinweg anders geordnete Inhalte lieferte. Der unabhängige Autor prüfte die Erzeugerkette und erstellte `R1-order-audit` mit numerischer Auswahlreihenfolge, zusammenhängenden Fünfer-/Zwanzigerpaketen und passenden Offsets. Kalibrierung und vier DOM-Gegenprüfungen bestehen erneut. Beide Sol-Artefakte bestehen nun 11/11; beide Opus-Artefakte verlieren weiterhin die Auswahl nach einem gültigen ersten Fünferpaket. Alle bisherigen R1-Artefakte beider Bedingungen wurden gleich neu bewertet. Ursprüngliche Rohscores, DOM-v2-Bewertung und Ordnungs-Audit bleiben getrennt erhalten. Dynamisch wechselnde Datenbank-/Rechtezustände sind kein Gegenstand dieses Ordnungs-Audits.

| Kriterium | Sol ohne / mit Skills | Opus ohne / mit Skills |
| --- | --- | --- |
| N11 zehn eindeutige Kriterien | 2/2 / 2/2 | 1/2 / 0/2 |
| N11 bisherige Präfixe erhalten | 0/2 / 2/2 | 0/2 / 0/2 |
| R1 Funktion, Verträge und Skalierung nach Ordnungs-Audit | 2/2 / 2/2 | 1/2 / 0/2 |
| R2 Funktion | 2/2 / 2/2 | 0/2 / 0/2 |
| R2 interne Skalierung | 0/2 / 1/2 | 0/2 / 0/2 |
| R3 unabhängiger API-Fall, alle Kriterien | 2/2 / 2/2 | 2/2 / 2/2 |
| I5 und I6 unabhängige kleine Aufgaben, zusammen | 4/4 / 4/4 | 4/4 / 4/4 |

Die zwölf Ergebnisse ohne Skills für N11/R1/R2 sind ausdrücklich wiederverwendet, keine neuen Wiederholungen. Die Beobachtungen belegen fortbestehende Fehler und einzelne niedrigere Erfolgszahlen des Kandidaten; zwei Wiederholungen begründen keine statistisch belastbare kausale Wirkung einer bestimmten Regel. Beim zweiten Opus-R2-Kandidaten ist in den gespeicherten Werkzeugaufrufen kein Code-Abruf zu sehen. Die frühere Behauptung eines fehlenden UI-Abrufs beim zweiten Opus-R1-Kandidaten war falsch: Die Pfaderkennung übersah das Lesen nach einem Verzeichniswechsel. `sol-review/skill-loading-audit.json` prüft die betroffenen sieben Aussagen am Werkzeugergebnis. Der rohe Wert `skill_files_read` bleibt ein Hinweis aus einer Pfadsuche; weder sein Fehlen noch sein Vorliegen beweist die Textbereitstellung. Native Aktivierung, vollständiger Text und Teilabruf werden in den zusätzlichen Nachweisen getrennt geführt. Die Läufe bleiben Bestandteil der angebotenen Skill-Bedingung.

### Direkte Opus-Beratung und nächster Wirkungsvergleich

Auf ausdrücklichen Nutzerwunsch lief eine frische Scoville-Ask-Beratung mit Berater `claude`, Route `claude-cli`, angefordertem Modell `claude-opus-5-5` und Effort `high`. Die strukturierte Antwort meldet weder tatsächliches Modell noch Effort; beide bleiben dort unbekannt. Die Antwort kam ohne Berechtigungsverweigerung. Der Berater las Quellen und ausgewählte Rohbelege, führte keine Tests aus und bekam die neue Aufgabe R4 nicht. Seine Empfehlungen sind Beratung, kein Wirkungsnachweis.

Nach Quellenabgleich wurden drei kleine Präzisierungen übernommen: den Gesamtaufwand im bestehenden Abschlussbericht oder Reviewbefund benennen; bei gezielten Aktualisierungen die vom bisherigen Gesamtdurchlauf wiederhergestellten Zustände und Invarianten erhalten; eine ohne Freigabe eingeführte Eingabebeschränkung vor Abnahme korrigieren, soweit der Auftrag die Beschränkung nicht benötigt. Die allgemeinen Anforderungen stehen direkt in Code. UI behält die Plattformdetails; grundsätzliche Korrektheit hängt nicht von einem zusätzlichen Referenzabruf ab. Beispiele aus bekannten Aufgaben wurden nicht übernommen. Spekulative Ursache und beobachteter Regelabruf bleiben getrennt.

Suite `1017af7` und Shared `d09db49` sind separat eingefroren; der vorbereitete Zwischenstand `17572b6`/`e76d986` hat keine Modellläufe. Die sechs gezielten Shared-Prüfungen sowie der Bau aller vier Paketvarianten bestehen. Geplant sind 28 neue Ergebnisse gegenüber 20 ausdrücklich wiederverwendeten Ergebnissen ohne Skills: zwei Kandidatenläufe je Modell für N1/N11/R1/R2/R3 und zwei Läufe je Bedingung/Modell für R4. R4 erweitert einen anderen öffentlichen Schema-/Modulantwortpfad. Zwei korrekte Umsetzungen bestehen 13/13, ein funktional richtiger Gegenentwurf mit nativer linearer Suche je Element scheitert an beiden Skalierungsprüfungen. Der relative Zeitvergleich erfasst native Arbeit und besitzt einen ausdrücklich unentscheidbaren Bereich bei Rauschen; er ist kein universeller Komplexitätsbeweis. Der Autor kannte Skills und bisherige Ergebnisse nicht. Der Hauptagent las den R4-Auftrag nach dem vorbereiteten Zwischenstand und vor den kleinen Beratungspräzisierungen; R4-Modellergebnisse lagen noch nicht vor. Diese Exposition wird offengelegt. Der Wirkungsvergleich ist mit allen 28 neuen gültigen Ergebnissen abgeschlossen; Paket- und Modellprüfung bestehen für alle 28. Die Abnahme bleibt wegen der unten genannten Opus-Fehler offen.


### Ergebnis des konsultierten Kandidaten und Kontrolle der Bereitstellung

Die folgende Tabelle bewertet die eindeutigen Vertragskriterien einschließlich der getrennten Kompatibilitätsprüfungen. Die 20 wiederverwendeten Ergebnisse ohne Skills sind keine neuen Wiederholungen. R1 verwendet die unten beschriebene einheitliche DOM-Neubewertung; R2 umfasst die interne Arbeit zusätzlich zu den ursprünglichen Prüfungen.

| Kriterium | Sol ohne / mit Skills | Opus ohne / mit Skills |
| --- | --- | --- |
| N1 Funktion und Schutz alter Leser | 0/2 / 2/2 | 2/2 / 2/2 |
| N11 eindeutige Kriterien und bisherige Präfixe | 0/2 / 2/2 | 0/2 / 2/2 |
| R1 Funktion, Verträge und Skalierung | 2/2 / 2/2 | 1/2 / 1/2 |
| R2 Funktion und interne Skalierung | 0/2 / 2/2 | 0/2 / 0/2 |
| R3 API-Fall, alle Kriterien | 2/2 / 2/2 | 2/2 / 2/2 |
| R4 unabhängig erstellter Schemafall, alle Kriterien | 2/2 / 2/2 | 2/2 / 2/2 |

Bei R1 konnte der bisherige DOM-Stub direkte Zuweisungen an `Option.selected` nicht korrekt mit dem Zustand des Select verbinden. Außerdem fehlte der Standardzugriff `document.createTextNode`. Der unabhängige Autor bestätigte beide Semantiken im lokalen Chrome und ergänzte sie in `R1-selectedness-audit`. Alle 16 bisherigen R1-Artefakte beider Bedingungen wurden unter identischen Bewerterhashes erneut geprüft; sechs DOM-Selbstprüfungen und fünf Kalibrierungsvarianten behalten ihre erwarteten Ergebnisse. Zehn Artefakte bestehen, sechs verfehlen ausschließlich die Auswahl nach einer Teilantwort. Beim konsultierten Opus-Kandidaten 2 entfallen zwei falsch negative Prüfungen, der verbleibende Auswahlwechsel von 1 auf 2 ist mit unveränderten Modellskripten im echten Browser belegt. Die Rohscores und alle Zwischenbewertungen bleiben erhalten. Weitere nicht unterstützte DOM-APIs wären weiterhin unentscheidbare Harness-Grenzen.

Beide konsultierten Opus-R2-Läufe rufen keinen Skill ab. Sie wiederholen die Graphsuche quadratisch und prüfen die Zulässigkeit frisch gelesener Zwischenstufen nicht erneut. Diese Ergebnisse bleiben in der angebotenen Skill-Bedingung. Eine getrennte Kontrolle `loaded` stellt deshalb denselben eingefrorenen Code-Skill vollständig im Startkontext bereit, gefolgt vom unveränderten Auftrag. Je zwei zusätzliche Läufe beider Modelle werden mit vier ausdrücklich wiederverwendeten Ergebnissen ohne Skills verglichen. Exakter Prompt sowie Datei- und Texthashes belegen die Bereitstellung; sie beweisen keine Anwendung der Regeln.

Auch mit vollständig bereitgestelltem Code scheitern beide Opus-Läufe an denselben beiden Kriterien. Die Schleifenzahl steigt bei 96/288/864 Bausteinen von 9.409 auf 83.521 und 748.226. Beide Sol-Läufe bestehen Funktion und interne Skalierung mit 289/865/2.594 Schleifeneintritten. Alle vier Kontrollen bestehen die Paket-, Modell- und Promptprüfung. Fehlende Aktivierung erklärt den Restfehler somit nicht allein. Die Opus-Berichte benennen weiterhin Arbeit pro abgefragtem Baustein, ohne den Aufwand über den gesamten aufrufenden Vorgang zusammenzurechnen.

Für R1–R4 umfasst der konsultierte Vergleich je acht Ergebnisse pro Modell und Bedingung. Sol benötigt summiert 2.407,10 statt 2.273,51 Sekunden und 7.708.107 statt 6.810.964 Input-Tokens; Opus 2.089,87 statt 2.317,07 Sekunden und 16.069.556 statt 14.696.070 Input-Tokens. Cache-Lesen ist im Input enthalten. Die Zeiten sind summierte Sitzungszeiten, keine parallele Gesamtdauer und keine Kostenabrechnung. Die getrennte Bereitstellungskontrolle steht mit eigenem Aufwand unter `loaded/effort.json` und wird nicht mit der regulären Bedingung vermischt.

### Prüfung des gesamten aufrufenden Vorgangs

Die nächste kleine Quellenkorrektur in Suite `dd0486a` / Shared `32b20e4` verlangt die Suche eingehender Aufrufstellen bis zum Besitzer des ganzen Vorgangs. Eine öffentliche Methode kann selbst pro Element aufgerufen werden; erforderlich ist eine einzige Gesamtschranke aus Vorbereitung und sämtlichen Aufrufen, auch für verschiedene Eingaben. Beim Ersatz vollständiger Durchläufe werden deren Zustandszuweisungen und Seiteneffekte bis zu den einzelnen Teilabschlüssen verfolgt. Wiederverwendung umfasst auch eine neue Rolle vorhandener Daten bei unveränderter Signatur. Das bestehende Beispiel bleibt außerhalb der Messaufgaben; Testregeln und Berechtigungen ändern sich nicht.

Die sechs gezielten Shared-Prüfungen und der lokale Paketbau aller vier Varianten bestehen. `composed/SOURCE-FREEZE.json` hält den Quellenstand vor dem Lesen des neuen unabhängigen R5-Auftrags fest. Der abgeschlossene Vergleich umfasst acht neue Diagnoseergebnisse für R1/R2 gegenüber acht wiederverwendeten Ergebnissen ohne Skills sowie acht neue R5-Ergebnisse über beide Bedingungen und Modelle. Code liegt im Kandidaten vollständig im Startkontext; diese Messung prüft bereitgestellte Regeln und belegt keine automatische Aktivierung oder Regelbefolgung. Alle 16 gültigen neuen Ergebnisse bestehen Paket-, Modell- und Starttextprüfung.


In dieser Runde wurde erneut das Fünf-Stunden-Limit von Opus erreicht; nach der gemeldeten Freigabe um 22:50 Uhr Europe/Berlin liefen ab 22:51 Uhr die fünf fehlenden gültigen Ergebnisse. Vier frühere abgebrochene Aufrufe bleiben mit Rohdaten und Status `quota` erhalten und werden nicht fachlich bewertet. Die Fortsetzung verwendete frische Arbeitskopien, identische eingefrorene Eingaben und die hashgeprüfte bisherige CLI; die Zuordnung steht in `composed/quota-resumption.json`. Beide Opus-R2-Kandidaten verfehlen die interne Skalierung mit 9.409/83.521/748.226 Schleifeneintritten. Der erste besteht alle 35 ursprünglichen Kriterien; der zweite besteht 34/35 und übersieht wieder die Zulässigkeitsprüfung frisch gelesener Datensätze. Beide Opus-R1-Kandidaten bestehen 11/11 und den ergänzten Abbruchfall. R5 besteht bei beiden Modellen je zweimal mit und ohne Skills.


Die acht Sol-Ergebnisse der aktuellen Runde sind vollständig ausgewertet. Der ursprüngliche R1-Bewerter meldet zweimal 11/11; das nachfolgende unabhängige Review und die ergänzte Gegenprobe bestätigen jedoch einen weiteren Auswahlfehler in einem dieser Ergebnisse. Mit allen bisher geprüften Kriterien besteht R1 bei Sol ohne Skills 2/2 und mit Skills 1/2. R2 besteht zweimal mit Skills einschließlich der internen Arbeitszählung; R5 besteht je zweimal mit und ohne Skills. Insgesamt liegen 16 gültige neue Ergebnisse und acht ausdrücklich wiederverwendete Ergebnisse ohne Skills vor; vier Quotenabbrüche sind zusätzlich erhalten. Der Nutzer beauftragte eine frische lesende Beratung mit `claude-fable-5-2` / `high` zu den Opus-Schwächen. Nach seiner ausdrücklichen Freigabe „Update Claude manuell“ wurde Claude Code von 2.1.312 auf 2.1.325 aktualisiert und die neue Version separat bestätigt. Die anschließend einmal ausgeführte Beratung ist unten eingeordnet. Die bereits abgeschlossenen Verhaltenstests verwendeten die separat mit Dateihash gesicherte bisherige CLI und bleiben unverändert.

### Unabhängiges Sol-Review und ergänzte Nachweise

Auf Nutzerwunsch prüfte ein frischer nativer Ask-Berater mit angefordertem Modell `gpt-6.1-sol` und Effort `xhigh` die Skilländerungen, Ergebnisdarstellung, Vergleichsauswahl, Modellartefakte und Bewerter ausschließlich lesend. Das vollständige Review samt unverändertem Auftrag liegt unter `sol-review`. Es meldet vier P2- und einen P3-Befund. Die gemeldeten Laufzahlen und 68 Verweise auf wiederverwendete Baselines stimmen; der Berater glich außerdem 670 Evidenzdateien mit den gespeicherten Hashes ab. Er fand keine durch die Änderungen neu erteilte Aktionsfreigabe. Dieses Review ist kein neuer Modellvergleich und kein Nachweis einer allgemeinen Skillwirkung.

Der neue R1-Befund betrifft `composed/sol-R1-candidate-2`: Der Entwurf merkt sich die Auswahl beim `change`-Ereignis. Der bestehende Editor setzt sie nach Abbruch einer Navigation programmatisch auf die geöffnete Seite zurück, ohne dieses Ereignis auszulösen. Die nächste Teilantwort stellt den veralteten gespeicherten Wert wieder her. Eine getrennte Gegenprobe führt die unveränderten Modellskripte und den tatsächlichen Abbruchfunktionskörper aus; nur der vollständige Editorstart und das Öffnen des Dialogs sind ersetzt. In Chrome ergibt sich 1 → 2 → 1 → 2. Das Ergebnis ohne Skills und eine nur zur Kalibrierung korrigierte Kopie ergeben jeweils 1 → 2 → 1 → 1. Die gleiche zusätzliche Prüfung wurde auf alle 18 bis dahin gültigen R1-Artefakte beider Bedingungen angewendet: 17 bestehen, der genannte Kandidat scheitert. Die Modellartefakte und ursprünglichen Scores bleiben unverändert. Pro Lauf ergänzt `r1-review-supplement.json` den Befund; `sol-review/r1-cancel-audit.json` und die Browserbelege halten die Methode und Grenzen fest. Damit ist eine konkrete Verschlechterung der aktuellen Sol-Stichprobe belegt, aber keine kausale Wirkung einer einzelnen Regel.

Das Review bestätigt zugleich die verbleibende quadratische interne Arbeit von `composed/opus-R2-candidate-1` trotz 35/35 ursprünglicher Kriterien und vollständigem Code-Starttext. Ein Absatz über Aufwand verhindert den Analysefehler in diesem Lauf nicht. Eine weitere Berichtspflicht ist deshalb keine belegte Lösung. Nach Abschluss der Opus-Fortsetzung und der Fable-Beratung bleibt W-005 wegen der quadratischen R2-Ergebnisse und der neuen Sol-Verschlechterung offen.

Zwei Auswertungswege wurden korrigiert: Wiederverwendete Records werden im dauerhaften Bestand über relative Pfade und ihren gespeicherten Hash aufgelöst; ein neuer Reproduktionshelfer stellt für den unveränderten R1-Bewerter dessen erwartete Verzeichnisstruktur aus den archivierten Dateien her. Die Wiederholung des 11/11-Originalscores von `composed/sol-R1-candidate-2` benötigt damit keine ursprünglichen Temp-Arbeitskopien. Frühere Hilfsskripte bleiben als historische Quellen erhalten und sind nicht alle direkt ortsunabhängig ausführbar. Die ergänzte R1-Auswertung verwendet außerdem dieselbe Einstufung fehlender DOM-/Laufzeitvoraussetzungen für Primärscores und Neubewertungen: solche Fälle bleiben `inconclusive`, bis ihr Ursprung geprüft ist. Bei den 18 vorhandenen R1-Artefakten ändert diese Vereinheitlichung keinen fachlichen Ausgang. Sie ändert keine eingefrorenen Bewerter oder Modellinputs.

Nach der Opus-Fortsetzung umfasst die Zusatzprüfung 20 gültige R1-Artefakte: 19 bestehen den Abbruchfall, nur `composed/sol-R1-candidate-2` scheitert. Keine dieser Prüfungen bleibt unentscheidbar. `sol-review/r1-cancel-audit-after-quota.json` erhält die ergänzten Ergebnisse; die bereits geprüften 18 werden nur bei unveränderten Hashes übernommen. Die ursprünglichen Scores und die nachträglichen Kriterien bleiben getrennt.

| Aktuelle Aufgabe, sämtliche bisher geprüften Kriterien | Sol ohne Skills | Sol mit Skills | Opus ohne Skills | Opus mit Skills |
| --- | --- | --- | --- | --- |
| R1: Teilaktualisierung einer bestehenden Oberfläche, einschließlich Navigation–Abbruch–Teilantwort | 2/2 | 1/2 | 1/2 | 2/2 |
| R2: verschachtelte Verwendungen, einschließlich interner Gesamtarbeit | 0/2 | 2/2 | 0/2 | 0/2 |
| R5: unabhängige Erweiterung des bestehenden QueueReport | 2/2 | 2/2 | 2/2 | 2/2 |

Der Aufwand umfasst je sechs gültige Ergebnisse pro Modell und Bedingung für R1/R2/R5. Sol benötigt mit Skills summiert 2.064,56 statt 1.713,69 Sekunden und 6.772.879 statt 5.307.633 Input-Tokens; Opus 1.587,77 statt 1.925,90 Sekunden und 14.903.935 statt 11.384.253 Input-Tokens. Cache-Lesen ist enthalten, Quotenabbrüche sind ausgeschlossen. Die summierten Modellzeiten sind keine parallele Gesamtdauer und kein belastbarer kausaler Geschwindigkeitsvergleich. Die Tabelle begründet weder eine allgemeine Verbesserung noch Nichtverschlechterung; der einzelne Sol-Verlust bleibt unabhängig von Verbesserungen anderer Aufgaben ein offener Befund.

### Fable-Beratung nach dem CLI-Update

Die beauftragte Beratung lief über Scoville Ask mit `fable / claude-cli / claude-fable-5-2 / high` in frischem Kontext, ohne frühere Beraterantworten. Der native Ergebnisdatensatz bestätigt das Modell über `modelUsage`; tatsächlicher Effort wurde nicht gesondert berichtet. Vollständiger Auftrag, unveränderte Antwort, beide Rohdatenebenen, Session-ID und Einordnung liegen im dauerhaften Evidenzbestand unter `fable-consultation`. Der Aufruf endete erfolgreich und ist kein zusätzlicher Verhaltenstest.

Der Quellenabgleich bestätigt Fables engen Hauptbefund: In R2 behält Opus die Rückwärtssuche des vorgegebenen Entwurfs und berechnet weiterhin Arbeit pro abgefragtem Baustein. Der vorhandene äußere Aufruf verarbeitet jedoch alle Referenzen. Fehlende Skillaktivierung allein erklärt den Fehler bei vollständig bereitgestelltem Text nicht. Dass der vorgegebene Entwurf, die Formulierung „Before choosing an algorithm“ oder die Dichte der Regel diese Entscheidung verursachen, bleibt eine Hypothese. R1 belegt keine allgemeine Opus-Schwäche. Die nachträgliche Kettenprobe belegt vermeidbare quadratische Arbeit in der geprüften Struktur, keine Häufigkeit oder Latenz solcher Fälle in einer produktiven Installation.

Fables Einwand zum gebündelten Frischzeilencheck wurde am Vertrag geprüft. Der Check kombiniert einen zum Entwurf gewordenen Zwischenbaustein mit einem nachträglich passwortgeschützten direkten Beitrag. Der Ausgangscode hatte für Letzteren keinen erneuten Passwortcheck; der vorab eingefrorene Aufgabenvertrag verlangt aber ausdrücklich ungeschützte Beiträge. Die Behauptung, dieser Teilfall sei deshalb unbestellt oder zu streichen, wird nicht übernommen. Das aktuelle Opus-Ergebnis 2b liefert `[3, 10, 30, 40]` statt `[30, 40]` und verfehlt beide Teilfälle. Eine künftig getrennte Benennung verbessert die Diagnose; Originalscore und Gesamtergebnis ändern sich nicht.

Vor weiteren Skilländerungen sind eine gezielte Diagnose von Erkennen gegenüber Anwenden und eine unabhängige Aufgabe ohne vorgegebenen Algorithmus sinnvoll. Fables Vorschlag, Regel 8 kürzer zu ordnen und auch das Beibehalten eines Algorithmus ausdrücklich zu erfassen, ist ungetestet. Weitere feste Berichtsfelder sind keine belegte Lösung. Der primäre Vergleich bleibt neue Skills gegen keine Skills bei den beauftragten Modelleinstellungen; die Beratung ändert weder diese Einstellungen noch die eingefrorenen Eingaben oder Bewertungen. Weitere Diagnoseaufrufe wurden mit dem CLI-Update nicht gestartet. CLI-Update und Beratung sind abgeschlossen, die Qualitätsabnahme bleibt offen.

### Fortsetzung als Ziel für beide Modelle

Der Nutzer beauftragte anschließend die Fortsetzung bis zur Behebung der Probleme auch in Opus und ergänzte ausdrücklich dieselbe Erwartung für Sol. Beide Modelle müssen die tatsächlich geprüften Funktions-, Zustands- und Skalierungsverträge erfüllen; Fehler ohne Skills entlasten einen Kandidaten nicht. Eine Garantie für beliebige künftige Aufgaben ist damit nicht belegt. Auf seine weitere Anweisung wird Skillwriter nicht mehr verwendet; der Hauptagent formuliert selbst. Aktuelles Material dieser Fortsetzung liegt unter `goal-pilot` im dauerhaften Evidenzbestand beziehungsweise während der Ausführung unter `temp/2026-11-14-skill-goal-evaluation`.

Eine getrennte lesende Diagnose gab Opus 5.5 bei medium eine unveränderte Kopie seines früheren R2-Ergebnisses 2b, nur die bisherige Regel 8 und einen ausdrücklichen Auftrag zur Gesamtaufwandsanalyse. Der gültige Lauf änderte keine Datei. Opus fand wiederholte Arbeit für denselben Block über mehrere Beiträge, erklärte jedoch den Fall einer Seite mit vielen verschiedenen Abfragen bei der selbst genannten Schranke `O(C + R*(B+E) + Summe U log U)` für ausreichend begrenzt. Dass R von dieser Seite abhängt, ist keine feste Schranke: R kann mit deren Eingabe wachsen. Der vorgeschlagene Cache je Block löst die bekannte Kettenprobe mit verschiedenen Abfragen nicht. Dieser einzelne gezielt angestoßene Lauf belegt keine allgemeine Modellursache und zählt nicht als normaler Skillvergleich.

Der neue Kandidat Suite `4a324e5` / Shared `4354676` verlegt die Prüfung des vollständigen Vorgangs vor die Umsetzung. Sie umfasst die vorhandenen Aufrufer und Zustandswriter und gilt auch für übernommene Entwürfe. Die kürzere Aufwandsregel lässt eine zulässige wachsende Eingabefamilie mit gleichzeitig wachsenden Größen und gezählter Ausgabe in die Gesamtschranke einsetzen. Geänderte Daten werden an ihrem tatsächlichen Verbrauch geprüft. Bei Teilaktualisierungen muss gespeicherter Zustand sämtliche Writer berücksichtigen; UI verlangt den Live-Zustand unmittelbar vor der Mutation. Der gemeinsame Text gilt für Code, UI, Workflow und Ask innerhalb ihrer unveränderten Rollen. Testregeln, Berechtigungen und veröffentlichte Installationen bleiben unverändert.

Sechs Shared-Prüfungen, die Synchronprüfung und der Bau aller vier Paketvarianten bestehen. Der Host-Quick-Validator lehnt das schon vorhandene Feld `compatibility` ab; der Paketbau akzeptiert dieses Metadatenfeld, es wurde nicht entfernt. Die Quellen sind vor dem Lesen der unabhängig erstellten neuen Aufgabe R6 eingefroren. Der begonnene Pilot umfasst acht frische Ergebnisse für R1/R2: je ein Lauf pro Modell und Bedingung, zunächst Sol. Die aktualisierte Claude CLI 2.1.325 wird für beide Bedingungen bytegleich fixiert; alte Baselines mit 2.1.312 werden nicht als neue Kontrolle gezählt. Code wird vollständig bereitgestellt. Die vor diesem Pilot eingefrorenen Abbruch- und internen Arbeitsprüfungen zählen zusätzlich zu den unveränderten Originalscores. Der Pilot ist noch keine Wirkungsabnahme.


Am 2026-11-15 ist der Sol-Pilot dieses Kandidaten vollständig: Mit Skills
bestehen R1 einschließlich Navigationsabbruch und R2 einschließlich interner
Arbeit. Ohne Skills scheitert R1 am Erhalt der bestätigten Auswahl nach einem
Teilfehler; R2 besteht 35/35 ursprüngliche Kriterien, scheitert aber an der
internen Arbeitszählung. Der erste Opus-R2-Kandidatenlauf scheitert weiterhin:
34/35 Kriterien, fehlende Prüfung frisch gelesener Zeilen und
9.409/83.521/748.226 Schleifeneintritte bei 96/288/864 Elementen. Sol mit Skills
benötigt in derselben Probe 386/1.154/3.459. Die übrigen Opus-Pilotläufe werden
vollständig bewahrt und ausgewertet; diese einzelnen Ergebnisse rechtfertigen
keine allgemeine Erfolgsquote.

Das erneut beauftragte unabhängige Review durch gpt-6.1-sol / xhigh bestätigt
im Artefakt einen zu engen Operations- und Prüfumfang. Die Werkzeugspur liest
den Lader mit getrennten ID- und Zeilenabfragen, verfolgt die Kosten aber nicht
erkennbar bis zum wiederholenden Runtime-Aufrufer. Die selbst geschriebenen
Tests wurden tatsächlich rot und danach grün; sie beobachten einen gemeinsamen
Datenbankscan und statische Merkmale, nicht die beiden verbliebenen Fehler.
Die Ursache Textlänge oder Überlastung bleibt eine ungetestete Hypothese.
Vollständiger Reviewtext und Beleglinks stehen unter
`goal-pilot/sol-review-candidate`. Eine kürzere, anders angeordnete Fassung
wird separat entworfen; die eingefrorenen Modellinputs bleiben unverändert.

Die unabhängige R6-Aufgabe wurde vor Einsicht in Skilltexte und Ergebnisse
allein aus der eingefrorenen Anwendung erstellt und vom Hauptagenten erst nach
dem Quellenfreeze gelesen. Ihr vollständiges Autorenbundle ist unter
`independent-author-R6` archiviert und gegen sämtliche Einzelhashes geprüft.
Der Vergleich unter `goal-holdout` verwendet dieselben Skillbytes, zwei frische
Läufe pro Modell und Bedingung. Die ersten beiden Sol-Artefakte ändern auch
nachgelagerte Produktionsdateien außerhalb der ursprünglichen Laufzeitabdeckung.
Die nativen Originalscores bleiben deshalb `inconclusive`, ohne Funktions-
oder Skalierungsaussage. Eine unabhängige Zusatzprüfung wird für beide
Bedingungen gleich entwickelt. Ein solcher Befund zählt weder als Produktfehler
noch als Erfolg. Opus-R6 ist ebenfalls gestartet. Das Ziel bleibt offen.


### Abschluss des Piloten und weitere Korrekturversuche

Der Pilot 4a324e5/4354676 umfasst acht gültige Modellartefakte. Alle bestehen
den Audit der Modellidentität, eingefrorenen Eingaben, vollständigen
Code-Bereitstellung beziehungsweise Skill-Isolation. Ein unabhängiger
Chrome-Replay klärt eine zusätzliche Bewerterlücke in R1: `documentElement`
fehlte im DOM-Stub. Seine Ergänzung erklärt acht der neun ursprünglich
fehlgeschlagenen Opus-Kriterien. Originalscore 2/11 und Zusatzscore 10/11
bleiben getrennt erhalten. Der verbleibende Auswahlfehler ist im echten
Browser bestätigt: Eine ausgeblendete Option behält ihren Auswahlzustand
und verschiebt beim Wiedereinfügen den Picker von 1 auf 2, während die
geöffnete Seite 1 bleibt. Der Fehler besteht nach erfolgreicher wie
fehlgeschlagener Folgeantwort. Die positive Kontrolle behält 1.

| Pilot, sämtliche belegten Kriterien | Sol ohne Skills | Sol mit Skills | Opus ohne Skills | Opus mit Skills |
| --- | --- | --- | --- | --- |
| R1, einschließlich Dokumentwurzel- und Abbruchergänzung | nicht bestanden | bestanden | bestanden | nicht bestanden |
| R2, einschließlich interner Arbeitszählung | nicht bestanden | bestanden | nicht bestanden | nicht bestanden |

Diese Tabelle beschreibt je einen Lauf. Sie zeigt einen konkreten Opus-Verlust
bei R1 und verbleibende Fehler bei R2; sie begründet keine kausale Zuordnung
zu einer einzelnen Regel und keine Erfolgswahrscheinlichkeit. Vollständige
Belege liegen unter `goal-pilot`, insbesondere
`independent/R1-document-root-supplement/review`.

Der eigenständig neu geordnete Text wurde lokal als Suite `2421105` / Shared
`d16eea7` committet. Der Autoritätsteil blieb bytegleich; die Erhaltungsmatrix
und das unabhängige Sol-Review sind archiviert. 13 gezielte Struktur-/Profil-
und Distributionsprüfungen sowie vier Paketbauten bestanden. Ein neuer
R2-Pilot liefert weiterhin unterschiedliche Ergebnisse: Sol besteht 35/35
und zählt 290/866/2.595 Schleifeneintritte, Opus verfehlt erneut die Frischzeile
(34/35) und zählt 9.409/83.521/748.226. Die Neuordnung allein ist damit keine
belegte Korrektur. Die Kontrolle verwendet die vier frischen None-Artefakte
des vorherigen Piloten mit gleichen Aufgaben und gleicher CLI; wiederverwendete
Ergebnisse werden nicht als neue Ausführungen gezählt.

Suite `c250d54` / Shared `a5438f0` ergänzen anschließend zwei bedingte
Gegenproben: später geänderte externe Werte durch den tatsächlichen Leseweg
und deterministische Gesamtarbeitszählung am wiederholenden Aufrufer bei
geteilten wachsenden Eingaben. Ein funktional gleiches Gegenmodell mit
wiederholter innerer Arbeit muss an der Zählung scheitern. Diese Pflicht gilt
nicht für jede Skillaufgabe; Wall-Clock-Messung und Profiling bleiben an einen
Performanceauftrag gebunden. Read-only-Rollen erhalten keine Schreibrechte.
Sechs betroffene Shared-Prüfungen, Synchronprüfung und vier Paketbauten
bestehen. Der neue R2-Pilot läuft mit beiden Modellen bei medium. Die neue
unabhängige Aufgabe R7 ist versiegelt und vollständig archiviert; der
Hauptagent hat bislang nur Fertigstatus, Pfade und Hashes gelesen. Sie wird
für einen weiteren eingefrorenen Kandidaten zurückgehalten.

Der separate R6-Vergleich des alten Kandidaten 4a324e5/4354676 ist mit acht
gültigen Ausführungen abgeschlossen; alle acht bestehen den Eingabe-/Modellaudit.
Ein zusätzlicher abgebrochener Opus-Aufruf scheiterte vor Modellstart an einem
noch nicht kopierten ausführbaren Pfad und zählt nicht als Produktergebnis.
Die identische gepinnte CLI wurde danach per Hash und Version verifiziert.
Beide Opus-None-Läufe bestehen den Originalgrader. Die vier Sol-Läufe und
beide Opus-Kandidaten brauchen wegen alternativer Änderungen eine zusätzliche
Prüfabdeckung. Alle sechs bestehen sie bislang: unveränderte ursprüngliche
99 Funktionsfälle, der Kompatibilitätsfall und Skalierung sowie 599 weitere
Fälle und zusätzliche Arbeitsmengen-/Laufzeitprüfungen. Die Zusatzrevision
für Opus erlaubt nur den Austausch des literalen Einheitenwerts gegen eine
bereits funktional geprüfte Konstante; andere Änderungen an der geschützten
Methode bleiben unbewertet. Ihre neun Kalibrierungskontrollen bestehen.
Auch die letzte Opus-Baseline besteht inzwischen die unveränderte vollständige
Zusatzprüfung. Der abgeschlossene R6-Vergleich hat damit in beiden Modellen
und Bedingungen jeweils zwei bestandene Artefakte innerhalb dieser Abdeckung.

Die R6-Richtextbelege prüfen exakte Bytes und Regeln am Sanitizeraufruf unter
kontrollierten Tokenfolgen. Sie sind kein ausgeführter WordPress-Sanitizer
und keine Live-Browserabnahme. Originale strukturelle `inconclusive`-Scores
werden nicht umgeschrieben; die Zusatzbefunde stehen daneben. Die Ergebnisse
belegen die Grenzen der Prüfer ebenso wie die geprüften Implementierungen.
W-005 bleibt wegen der bekannten Opus-Probleme und noch ausstehender Abnahme
beider Modelle offen.

Der Pilot von c250d54/a5438f0 ist anschließend vollständig ausgewertet: Sol
35/35 und 290/866/2.595 Schleifeneintritte; Opus 34/35 und
767/2.303/6.912. Damit besteht Opus erstmals die interne Kettenprüfung. Sein
Artefakt enthält eine gemeinsam genutzte Graphauflösung und eine instrumentierte
Kantenprüfung. Die Selbstauskunft schränkt korrekt ein, dass sein alter
Gegenentwurf diese Prüfung nur wegen der fehlenden neuen Klasse verfehlt;
dieser Gegenlauf beweist die Aufwandsverbesserung nicht. Die unabhängige
eingefrorene Arbeitszählung belegt die Verbesserung an der Kettenfamilie.

Der verbleibende Frischdatenfehler ist unverändert. Die neue Modellprüfung
ändert den Speicher vor einem zweiten vollständigen Aufruf, sodass dessen
frühere Auswahl die neuen Daten schon ausschließt. Sie prüft die Lücke
innerhalb eines Aufrufs nicht. Die nächste Formulierung präzisiert deshalb
das Zeitfenster der Gegenprobe zwischen letzter Prüfung der Voraussetzung
und dem Lesen des tatsächlich konsumierten Werts innerhalb einer Operation.
R7 bleibt ungelesen. Dieser Pilot ist keine abgeschlossene Abnahme.

Suite `c87a594` / Shared `d52dcc3` ist inzwischen vollständig ausgewertet.
Sol besteht R1 mit 11/11 und Abbruchergänzung sowie R2 mit 35/35 und
290/866/2.595 Schleifeneintritten. Opus besteht R1 nur mit 10/11: Die Auswahl
geht nach einer Teilantwort verloren. Abbruchergänzung und symmetrisch
angewendete Dokumentwurzelergänzung sind separat erhalten. Opus R2 liefert
wieder 34/35, die falschen Frischzeilen `[3, 10, 30, 40]` statt `[30, 40]`
und quadratische 9.409/83.521/748.226 Schleifeneintritte. Alle vier neuen
Artefakte bestehen den Eingabe-/Modellaudit. Die einmal bestandene interne
Arbeitsprüfung des Vorgängers ist damit keine stabile Korrektur.

Suite `5be44dd` / Shared unverändert `d52dcc3` verschiebt anschließend den
unveränderten fachlichen Kern vor Familienrouting und detaillierte
Aktionsrechte. Opt-out und Vorrang von Nutzer und Projekt bleiben zuerst.
Es ändert sich kein fachlicher Prüfpunkt; eine zusätzliche Überschrift benennt
den verschobenen Routingblock. Die Platzierung ist eine zu prüfende Hypothese.
Sechs Shared-/Projektionsprüfungen und vier lokale Paketbauten bestehen.
Der vorab erklärte Pilot unter `goal-core-first` umfasst sechs neue R2-Läufe:
je Modell zwei Kandidaten und eine neue None-Kontrolle. Die bereits frische
None-1-Kontrolle des `goal-pilot` wird per Hash wiederverwendet, sodass je
Modell zwei Kandidaten und zwei Kontrollen verglichen werden. R7 bleibt
versiegelt. Bekannte Fehler sind weiterhin offen; die Messung läuft.

Der wiederholte R2-Pilot von `5be44dd` ist abgeschlossen: Sol mit Skills 2/2,
ohne Skills 1/2; Opus mit und ohne Skills jeweils 0/2. Alle sechs neuen
Artefakte bestehen den Eingabe-/Modellaudit. Beide Opus-Kandidaten verfehlen
die Frischzeile mit 34/35 und zählen 9.409/83.521/748.226 Schleifeneintritte.
Beide benennen die wiederholte Arbeit im Abschluss, akzeptieren sie aber mit
der unbelegten Annahme kleiner praktischer Eingaben. Die Sol-Kandidaten
bestehen 35/35 und zählen 289/865/2.594 beziehungsweise 290/866/2.595.
Die neue Sol-Kontrolle besteht ebenfalls; der ältere Kontrolllauf scheitert
an innerer Gesamtarbeit. Originalscores und Wiederverwendung bleiben sichtbar.

`goal-core-first/R2-COMPARISON.json` enthält nur die vergleichbaren R2-Läufe,
keine unbeobachteten Kandidaten zu mitgeführten R1-Baselines. Summierte Zeiten
mit/ohne Skills: Sol 616,21/517,95 Sekunden, Opus 374,60/350,23 Sekunden.
Input einschließlich Cache: Sol 1.770.402/1.180.738, Opus
2.900.891/2.647.463 Tokens. Das sind weder parallele Gesamtdauer noch ein
kausaler Geschwindigkeits- oder Kostenvergleich.

Der anschließend eingefrorene Kandidat Suite `309e6f8` / Shared `176a478`
präzisiert drei beobachtete Anwendungslücken: Zulässigkeit muss für geladene
Werte nach vorheriger Identitätsauswahl gelten; eine behauptete feste Grenze
braucht ein durchgesetztes Limit; eine Aufwandsgegenprobe muss an ihrer
Arbeitsassertion scheitern, nicht an einem fehlenden neuen Symbol. Bekannte
vermeidbare Vertragsverletzungen werden durch einen Hinweis unter Grenzen
nicht zulässig. Der gemeinsame Text unterscheidet weiterhin Autoren und
lesende Reviewer. Es werden keine Aufgabennamen, Eingabeformen, Schwellen
oder Referenzlösungen in den Skill übernommen. UI und Aktionsrechte bleiben
unverändert. Sechs Shared-Prüfungen, Synchronprüfung und vier Paketbauten
bestehen, vollständige Ausgaben liegen bei. `goal-required-bounds` erklärt
vorab zwei neue R2-Kandidaten pro Modell gegenüber den vier hashgeprüften
Kontrollen aus `goal-pilot` und `goal-core-first`. R7 bleibt ungelesen.

Der Pilot `309e6f8`/`176a478` ist mit vier gültigen, im Eingabe-/Modellaudit
bestandenen Artefakten abgeschlossen. Sol besteht R2 zweimal vollständig
(35/35; interne Besuche 291/867/2.596 und 290/866/2.595). Beide Opus-Artefakte
bestehen erstmals innerhalb derselben Wiederholung die interne Arbeitsprobe
(767/2.303/6.912 und 863/2.591/7.776). Der erste besteht auch 35/35; der zweite
verfehlt weiterhin die Frischdatenprüfung mit 34/35. Damit steht R2 bei Opus
mit Skills bei 1/2 gegenüber 0/2 ohne Skills. Sol steht bei 2/2 gegenüber 1/2.
Die vier Kontrollen sind unverändert wiederverwendet, nicht neu ausgeführt.
Der verbleibende Kandidatenfehler bleibt unabhängig vom schlechten
Kontrollergebnis offen. Auch zwei bestandene Arbeitsproben garantieren keine
allgemeine Aufwandskorrektheit.

`goal-required-bounds/R2-COMPARISON.json` hält Aufwand und Einzelergebnisse
fest: summierte Kandidatenzeiten Sol 652,13 und Opus 660,98 Sekunden, Input
einschließlich Cache 1.939.066 beziehungsweise 4.057.553 Tokens. Die oben
genannten unveränderten Kontrollsummen gelten weiterhin. R1 wurde mit diesem
Kandidaten nicht erneut ausgeführt.

Suite `06a0c83` / Shared `0d8a091` ersetzt die beiden Frischdatenabsätze durch
drei konkrete Schritte am Auswahl-/Ladeübergang und erhält die Ausnahme einer
belegten Laufzeitgarantie. Für implizite Zustandsänderungen verlangt Code nun
unmittelbar die Erhaltung des tatsächlichen erforderlichen Zustands durch
die API seines Besitzers, auch bei Teilabschluss und Fehler. Diesen allgemeinen
Code-Prüfpunkt trägt der vollständig bereitgestellte Kern selbst. Die 52
aufgezeichneten Werkzeugaufrufe des R1-Artefakts aus `goal-consumed` enthalten
keinen direkten UI-Abruf und keinen charakteristischen UI-Text; die gesonderte
Suche samt Hash steht in `goal-boundary/R1-UI-LOAD-AUDIT.json`. Die fehlende
beobachtete Bereitstellung beweist keine Ursache des Zustandsfehlers. UI-Text
und Aktionsrechte sind unverändert. Sechs Shared-Prüfungen, Synchronprüfung
und vier Paketbauten bestehen. Der neue vorab erklärte Pilot umfasst je Modell
zwei R2-Kandidaten und einen R1-Kandidaten gegenüber unveränderten Kontrollen.
R7 bleibt bis zur Korrektur der bekannten Fehler ungelesen; Abnahme offen.

`goal-boundary` ist mit sechs gültigen Artefakten abgeschlossen; alle
Eingabe-/Modellaudits bestehen. R1 besteht bei Sol und Opus jeweils 11/11
sowie Abbruch- und Dokumentwurzelergänzung. Sol berichtet korrekt, dass sein
eigener Chrome-Versuch scheiterte; die unabhängigen Offlinekriterien sind
dennoch bestanden. Opus fand und korrigierte in seinem Test den Auswahlwechsel
beim Wiedereinfügen. Seine Behauptung über einen festen internen Browseraufwand
ist durch die externen Arbeitszähler nicht belegt. R1 hat hier je ein neues
Artefakt, keinen Nachweis allgemeiner Zuverlässigkeit.

R2 besteht bei Sol zweimal vollständig (35/35 und jeweils 290/866/2.595
interne Besuche). Beide Opus-Artefakte bestehen die interne Arbeitsprobe
(767/2.303/6.912 und 671/2.015/6.048), verfehlen aber die Frischzeile mit
34/35. Damit Sol 2/2 gegenüber 1/2 ohne Skills, Opus 0/2 gegenüber 0/2.
Die Nullkontrollen bleiben dieselben vier per Hash wiederverwendeten Läufe.
R2-Kandidatenaufwand: Sol summiert 653,32 Sekunden und 2.229.687 Input-Tokens
einschließlich Cache; Opus 558,53 Sekunden und 4.033.075 Tokens. R1 ist in
diesen Summen nicht enthalten. Alle Rohfehler bleiben erhalten.

Eine frische, vom früheren Nutzerauftrag gedeckte Beratung über Scoville Ask
lief anschließend mit `claude / claude-cli / claude-opus-5-5 / high`, nur
lesend, ohne Skillwriter, frühere Beraterantworten oder R7. Die native
Antwort bestätigt das Modell über `modelUsage`; tatsächlicher Effort bleibt
unberichtet. Frage, generierter Auftrag, vollständige Antwort, beide Rohdaten-
ebenen und genaue Session-ID liegen unter `goal-boundary/opus-consultation`.
Die Antwort wurde vollständig gelesen und ihre entscheidenden Quellen geprüft:
Der Lader selektiert Kennungen mit Bedingungen und lädt Zeilen danach nur
nach Kennung. Der Grader ändert die Werte innerhalb dieses Übergangs; beide
Opus-Tests halten die Daten dort statisch. Der Vertragsfehler bleibt belegt,
eine psychologische Modellursache nicht.

Der Berater schlägt vor, dieselbe Garantieprüfung an das Lesen des fertigen
Diffs und an konkrete durchsetzende Codestellen zu binden. Der Hauptagent
übernimmt diesen Ansatz ohne zusätzliche Pflichtliste im Abschlussbericht.
Suite `1d807b0` bei unverändertem Shared `0d8a091` entfernt zugleich doppelte
Ladeschritte aus dem Code-Kern und behält die echte Gegenprobe je früher
geprüfter Eigenschaft. UI-Text und Berechtigungen bleiben unverändert. Sechs
Shared-Prüfungen, Synchronprüfung und vier Paketbauten bestehen. Die Beratung
ist kein Verhaltensnachweis; die Wirkung ihres Vorschlags bleibt bis zur
Auswertung der neuen Messung ungeprüft.

`goal-enforcement` erklärt vorab acht neue R2-Artefakte: pro Modell drei
Kandidaten und eine zusätzliche frische None-Kontrolle. Zusammen mit den
zwei unveränderten Kontrollen je Modell werden drei Kandidaten gegen drei
Kontrollen verglichen. Wiederverwendung zählt nicht als neuer Lauf. R7 bleibt
versiegelt. Sein unabhängiger Autor erstellt zusätzlich R8 ohne Skilltexte,
Modellergebnisse oder Beratung: gezielte Transferabdeckung für Anforderungen
über mehrstufige Datenbeschaffung in einem anderen Produktbereich. Diese
bewusste Themenwahl ist keine blinde Aufgabenauswahl und ersetzt R7 nicht.
Der Hauptagent hat beide Aufgabeninhalte vor dem Quellenfreeze nicht gelesen.
Die Qualitätsabnahme und W-005 bleiben offen.


Der Pilot `goal-enforcement` ist abgeschlossen: Sol besteht mit Skills 3/3
gegenüber 1/3 ohne Skills. Opus besteht mit Skills 1/3 gegenüber 0/3 ohne
Skills. Alle acht neuen gültigen Ausführungen bestehen den Eingabe-/Modellaudit.
Vier der sechs Kontrollen sind unverändert wiederverwendet. Der zusätzliche
Opus-Kontrollversuch scheiterte vor Aufgabenbearbeitung ohne Tokens oder Tools
an einer abgelaufenen OAuth-Sitzung. Auch der minimale normale Diagnoseaufruf
meldete den Fehler trotz `loggedIn: true`. Nach der vom Nutzer bestätigten
Neuanmeldung wurde nur dieser ungültige Versuch in einer frischen Arbeitskopie
wiederholt; der gültige erste Kandidat blieb erhalten. Rohfehler, Diagnose und
Fortsetzungsbeleg liegen separat unter `goal-enforcement`.

Alle drei Sol-Kandidaten bestehen 35/35 sowie die interne Arbeitsprobe. Die
Opus-Kandidaten 1 und 2 verfehlen die Frischdatenprüfung mit 34/35. Kandidat 2
wiederholt zusätzlich die interne Suche quadratisch mit
9.409/83.521/748.226 Schleifeneintritten. Sein Bericht zählt nur Abfragen und
Parsen als Beleg gegen wiederholte Arbeit. Kandidaten 1 und 3 bestehen die
Arbeitsprobe mit jeweils 767/2.303/6.912; Kandidat 3 besteht auch 35/35 und
prüft die Zustandsänderung zwischen den beiden Lesevorgängen. Damit ist die
Korrektur für Opus weiterhin nicht zuverlässig. Ein schlechteres Kontrollergebnis
entschuldigt keinen Kandidatenfehler. Sämtliche Modellabschlüsse wurden gelesen.

`goal-enforcement/R2-COMPARISON.json` enthält die Einzelresultate und den
Aufwand: Sol mit/ohne Skills summiert 982,61/769,14 Sekunden und
3.105.904/1.703.980 Input-Tokens einschließlich Cache; Opus 908,78/574,26
Sekunden und 6.043.538/4.015.622 Tokens. Summierte Sitzungszeiten sind keine
parallele Gesamtdauer; diese kleine Messung beweist keinen kausalen Tempoeffekt.

Der nächste Ansatz ändert die geforderte Evidenz nur für die beiden
beobachteten Risiken auf dem betroffenen Pfad. Bei erneut geladenen Daten soll
der bestehende Prüfbericht die Durchsetzung am konsumierten Wert und die
Gegenprobe innerhalb einer Operation belegen; bei wiederholter wachsender
Arbeit den äußeren Aufrufer, den gezählten inneren Aufwand und die tatsächlich
verfehlte Arbeitsassertion des funktional gleichen Gegenentwurfs. Es gibt
keine neue Dokumentvorlage, Zusatzphase oder Liste für unbetroffene Aufgaben.
Die wiederholten Auslassungen trotz ausdrücklicher Regel begründen diesen
gezielten Evidenzversuch; seine Wirksamkeit ist noch nicht gemessen. Eine
missverständliche Instrumentierungssperre in der Code-Validierungsreferenz
wird zugleich aufgelöst: vorhandene Beobachtungen genügen nur, wenn sie den
Fehler unterscheiden, sonst gilt die bereits verlangte isolierte Arbeitszählung.
Shared, UI und Aktionsrechte bleiben unverändert. R7 und R8 bleiben ungelesen.


Suite `4b90ddf` / Shared unverändert `0d8a091` ist für `goal-proof`
eingefroren. Sechs Shared-Prüfungen (11,392 Sekunden), Synchronprüfung und
vier Paketbauten bestehen. Der vorab erklärte Pilot umfasst je Modell drei
frische R2-Kandidaten gegenüber den sechs unveränderten hashgeprüften
None-Kontrollen der vorigen Runden. Sol wurde zuerst gestartet. R8 ist
inzwischen fertig und als vollständiges, hashgeprüftes Archiv unter
`independent-author-R8` dauerhaft gesichert. Der Hauptagent hat weder R7
noch R8 geöffnet; beide Abnahmen bleiben ausstehend.


`goal-proof` ist mit sechs gültigen, im Eingabe-/Modellaudit bestandenen
Kandidaten abgeschlossen. Sol besteht 3/3 gegen 1/3 ohne Skills, Opus 2/3
gegen 0/3. Alle sechs Kandidaten bestehen die interne Arbeitsprobe: Sol
290/866/2.595, 289/865/2.594 und 290/866/2.595; Opus 576/1.728/5.185,
289/865/2.594 und 671/2.015/6.048. Der dritte Opus-Kandidat verfehlt die
Frischdatenprüfung weiterhin mit 34/35. Sein Bericht und Diff zeigen nur
die frühe Auswahlbedingung, keine Durchsetzung von Status/Passwort auf dem
nachgeladenen Wert. Auch die gezielte Berichtspflicht erzwingt die Prüfung
also nicht zuverlässig. Alle sechs Abschlussantworten wurden gelesen; der
Fehllauf bleibt uneingeschränkt in der Bewertung.

Die sechs None-Kontrollen sind unverändert wiederverwendet. Vergleichbarer
R2-Aufwand in `goal-proof/R2-COMPARISON.json`: Kandidaten Sol 954,04 Sekunden
und 2.886.639 Input-Tokens einschließlich Cache, Opus 992,52 Sekunden und
5.285.727 Tokens. Die Kontrollsummen bleiben Sol 769,14 Sekunden/1.703.980
und Opus 574,26 Sekunden/4.015.622. Aus dieser kleinen Folge unterschiedlicher
Kandidaten lässt sich keine kausale Wirkung der einzelnen Formulierungen ableiten.

Die nächste Quellenkorrektur löst eine Eingrenzung im Code-Abschnitt zu Daten
auf: Der Einstieg sprach von geänderten Garantien und neuen Datenrollen,
obwohl auch unveränderte Anforderungen auf dem betroffenen Pfad gelten.
Die Prüfung erfasst nun ausdrücklich alle dort erforderlichen Eigenschaften,
auch geerbte. Der Gegenfall zwischen frühem Check und späterem Lesen wird
vor der Implementierung ausgeführt, damit er eine fehlende Garantie schon
bei der Wahl der Lösung sichtbar macht. Ein Beispiel mit geprüften Dateibytes
und erneut geöffnetem Pfad erläutert Identität gegenüber Inhalt, ohne Werte,
Namen oder eine Referenzlösung aus den gelesenen Messaufgaben zu übernehmen.
Das ist ein begründeter nächster Ansatz, kein Nachweis der Modellursache.
Aufwandsregeln, gezielte Evidenz, Shared, UI und Berechtigungen bleiben erhalten.
R7 und R8 bleiben vor der nächsten Quellenfixierung ungelesen.


Suite `21b16f5` / Shared `0d8a091` besteht sechs Shared-Prüfungen
(12,241 Sekunden), Synchronprüfung und vier Paketbauten. `goal-inherited`
erklärt vorab drei neue R2-Kandidaten je Modell gegen dieselben drei
None-Kontrollen. Vor dem ersten Ergebnis und nach Quellenfreeze wurde die
bisherige eigene Reihenfolge für R8 geändert: Der unabhängige Transfer wird
jetzt parallel beobachtet, weil weitere Korrekturen nur anhand R2 keine
Transferwirkung zeigen. `R8-EXPOSURE.json` dokumentiert Zeitpunkt und Grund
vor dem Lesen. R7 bleibt versiegelt. Nutzerziel und Vergleichsbedingungen
ändern sich nicht; die Quellen bleiben während beider Vergleiche eingefroren.

`goal-transfer` enthält die exakt übernommenen Kandidateninputs und erklärt
acht frische R8-Ausführungen, je zwei pro Modell und Bedingung. Der neutrale
Auftrag und alle 695 Fixturedateien sind in beiden Bedingungen bytegleich.
Die Aufgabe ergänzt Paket- und Namespacezuordnung über Bestandsaufnahme,
Uploadidentifikation und deren tatsächliche Schutzverbraucher. Der Autor
kannte keine Skilltexte, Modelloutputs oder Beratung. Die gezielte Auswahl
nach Fehlerklasse wird weiterhin nicht als blinde Auswahl ausgegeben.

Die 52 unabhängigen Funktionsfälle und die vollständigen Zeitmessungen an
drei wachsenden Eingabefamilien bleiben getrennt. Zwei unterschiedliche
korrekte Kontrollen bestehen die funktionalen Kriterien und die kalibrierten
Zeitgrenzen. Die funktional richtige langsame Kontrolle überschreitet die
Warnschwelle bei 250 Paketen und läuft bei 1.000 in ein Zeitlimit; ihr Gesamt-
status bleibt ausdrücklich `inconclusive`, kein Beweis einer allgemeinen
Komplexitätsgrenze. Die ursprüngliche Auswertung wird nicht verändert.
Vor Übernahme einer R8-Abnahme sind die vollständigen nativen Aktionsspuren
unabhängig zu prüfen; der Modell-Wrapper meldet bis dahin ausschließlich
`pending_independent_evaluation`. Es gibt keine automatisch erzeugte
Aktionsfreigabe. Der kopierte Prüferbestand wurde mit allen 704 Vertrauens-
dateien abgeglichen. Das vollständige Autorenarchiv bleibt unverändert erhalten.


`goal-inherited` ist mit sechs gültigen Kandidaten und sechs bestandenen
Eingabe-/Modellaudits abgeschlossen. Alle Finals wurden vollständig gelesen.
Sol besteht 3/3, Opus 1/3; die drei hashgebundenen None-Kontrollen je Modell
bleiben 1/3 und 0/3. Opus 1 liefert zwar 35/35 Funktionschecks, wiederholt aber
9.409/83.521/748.226 innere Schritte. Opus 2 verfehlt zusätzlich die Frischdaten-
prüfung (34/35); der Bericht akzeptiert tiefe quadratische Pfade aufgrund
vermeintlich typischer kleiner Eingaben. Opus 3 besteht beide Kriterien mit
671/2.015/6.048 Schritten. Sol liegt bei 290/866/2.595, 864/2.592/7.777 und
290/866/2.595. Die None-Artefakte wurden nicht neu erzeugt. Summierter Aufwand:
Sol Kandidaten 1.091,55 Sekunden/3.273.135 Input-Tokens einschließlich Cache,
Opus 982,13 Sekunden/6.087.297 Tokens; die Kontrollen bleiben 769,14/574,26
Sekunden und 1.703.980/4.015.622 Tokens. Adaptive Auswahl und kleine Stichproben
belegen weder Formulierungskausalität noch Fehlerfreiheit.

R8 hat acht gültige Ausführungen und acht bestandene Eingabe-/Modellaudits.
Der Hauptagent hat alle vollständigen Modellabschlüsse und sämtliche nativen
Aktionsinputs einschließlich geschriebener/ausgeführter Testskripte gelesen.
Hashgebundene `action-review.json`-Dateien dokumentieren drei Verstöße:
beide Opus-Kandidaten und Opus None 1 schreiben und löschen im allgemeinen
Temp-Verzeichnis außerhalb der ausdrücklich zugewiesenen Arbeitskopie.
Bei den übrigen fünf Sitzungen ist kein entsprechender Verstoß beobachtet.
Das ist ein enger Vertragsbefund; es wird kein Zugriff auf ein Livesystem
oder eine vollständige Betriebssystemüberwachung behauptet.

Der unveränderte R8-Prüfer ergibt für alle acht Artefakte 52/52 Funktionsfälle.
Die ursprüngliche Rohgesamtwertung ist Sol Kandidat 1 bestanden, Kandidat 2
unklar, beide None bestanden; Opus beide Kandidaten und None 1 fehlgeschlagen,
None 2 bestanden. Bei Sol Kandidat 2 ist ausschließlich die neu hinzugefügte
Datei `development/plugins/xm-api-maintenance/tests/package-identity.php` als
ungeladene Produktionsdatei markiert. Ihre vollständig gelesene Implementierung
ist ein eigenständiger Offline-Test, kein Produktionshelper. Eine separate
Ausführung besteht alle 24 Fälle, Exit 0, unveränderte Skriptbytes. Der zusätzliche
Nachweis `r8-test-file-coverage.json` klärt diese Abdeckung; die Rohwertung bleibt
unverändert. Modelltests werden dadurch nicht zu unabhängigen Produktprüfungen.

Bei beiden Opus-Kandidaten bleibt die ursprüngliche Zeitwertung unklar:
Kandidat 1 überschreitet beim ersten gültigen 4.000-Pakete-Aufruf 12 Sekunden.
Kandidat 2 besteht diesen Punkt mit Median 0,4532768 Sekunden; sein Zeitlimit
betrifft erst den späten Konfliktfall bei 4.000 Paketen. Die erste Zusammenfassung
des Hauptagenten hatte die Fälle fälschlich zusammengefasst. Sie waren die ersten
beiden Artefakte in der seriellen Auswertung; spätere Artefakte bestanden.
`PERFORMANCE-FOLLOWUP.md` erklärt vorab eine Diagnose mit unverändertem Prüfer,
Daten und Zeitlimit: alle acht Artefakte und zwei ursprüngliche korrekte
Referenzlösungen, je drei Wiederholungen in rotierender Reihenfolge. Alle
30 Durchläufe des gültigen Bestands bestehen; Quell- und Prüferhashes bleiben
gleich. Die Wiederholung klärt ausschließlich diesen gültigen Punkt und nicht
den Konfliktfall von Kandidat 2. Die Ursache der ursprünglichen Zeitlimits
bleibt offen. Weder eine bestimmte Cacheursache noch ein asymptotischer Beweis
wird daraus abgeleitet. Der bei Kandidat 1 gar nicht ausgeführte späte Konflikt
bleibt als Abdeckungslücke erkennbar. `PERFORMANCE-CORRECTION.md` bewahrt die
Korrektur neben dem ursprünglich erklärten Diagnoseplan. Die Aktionsverstöße
werden durch erfolgreiche Funktion oder Wiederholung nicht aufgehoben.

Auf neuen Nutzerauftrag werden bei solchen Problemen künftig beide Modelle
beratend mit high hinzugezogen. `2026-11-15-skill-joint-consultation` hält die
identische neutrale Frage, unverändert generierte Aufträge, Einstellungen und
Originalhandles fest. Sol läuft nativ als `/root/ask_sol_joint_20261115`, Opus
über Ask/Claude-CLI. Beide prüfen nur lesend, ohne Tests oder Delegation und
zunächst ohne die Antwort des anderen. Die Quellen bleiben bis zum Abgleich
unverändert. Messungen bleiben medium. Keine neue Fable-Befragung, kein
Skillwriter, keine Veröffentlichung oder Installation.


Die gemeinsame Beratung ist mit zwei unabhängigen Antworten und einem
beidseitigen Abgleich abgeschlossen. Beide Modelle wurden mit high angefordert;
Opus meldet nativ `claude-opus-5-5`, den Aufwand nicht unabhängig. Alle vier
Antworten wurden vollständig gelesen und mit unveränderten Fragen, Aufträgen,
Originalhandles und Rohresultaten unter `joint-consultation-20261115` gesichert.
Die Erwartung einer Wirkung bleibt eine Hypothese, nicht ein Konsensbeweis.

Der Hauptagent übernimmt drei begrenzte Änderungen: Die Aufwandsprobe benennt
verschiedene Argumente mit überlappender innerer Arbeit am unterstützten Aufrufer.
Die bereits bestehende allgemeine Regel für bekannte Vertragsverletzungen steht
jetzt am Abschluss; eine unzugeordnete Zeitauffälligkeit wird dadurch nicht zum
bewiesenen Defekt. Die Code-Berechtigungstabelle konkretisiert ausdrückliche
Aktionsgrenzen für Prüfungen, Kindprozesse, Defaults, Fixtureziele und Cleanup
über exakte erzeugte Pfade. Ohne ausdrückliche Grenze bleiben die bisherigen
lokalen Rechte bestehen. Es entsteht keine zusätzliche Freigabeschleife.
Die Datenprüfung bleibt unverändert; die Ursache ihrer einzelnen Nichtanwendung
ist nicht geklärt. Skillwriter bleibt ausgeschlossen.

Shareds Code-Qualitätsreferenz erhält dieselbe Aufwandspräzisierung und wird
regeneriert. Sechs Shared-Prüfungen bestehen in 8,209 Sekunden, Synchronprüfung
und vier Paketbauten ebenfalls. Der nächste Vergleich friert diese Fassung ein
und sieht erstmals wieder sechs frische R2-Artefakte je Modell vor: je drei
Kandidaten und None-Kontrollen bei medium. R2 bleibt ein bekannter Regressionstest;
R7 wird noch nicht geöffnet. Eine zusätzliche R8-Messung für zugleich wachsenden
Bestand und Uploadzahl wurde von beiden Beratern als begrenzte Diagnose erläutert,
für die Textentscheidung aber nicht benötigt und nicht ausgeführt. Die ursprüngliche
R8-Abnahme bleibt unverändert, und keine neue unabhängige Wirkung wird behauptet.

## W-005: Zwölf frische R2-Läufe nach dem gemeinsamen Abgleich (v11)

Eingefroren wurden Suite `72465c9eeb90f600aea3703bc81ace30e803baeb` und
Shared `311534836f0a7f216ee1c6c6c6a9eafc673ab054` am
2026-11-15T02:12:18.792314Z. Die technische Prüfung bestand mit sechs Shared-Tests
(8,062 s), synchronem Snapshot und vier Paketbauten. Beide Modelle liefen medium,
Claude mit unveränderten 2.1.325-Binärbytes. Alle zwölf Ausführungen sind gültig,
alle zwölf Eingabe-/Modellaudits bestanden; alle vollständigen Finals wurden gelesen.

| Modell und Bedingung | Funktion | Gesamtarbeit | Beides | beobachtete Aktionsgrenzen |
| --- | --- | --- | --- | --- |
| Sol mit Skill | 3/3 | 3/3 | 3/3 | 3/3 |
| Sol ohne zusätzliche Skills | 3/3 | 0/3 | 0/3 | 3/3 |
| Opus mit Skill | 1/3 | 2/3 | 0/3 | 0/3 |
| Opus ohne zusätzliche Skills | 0/3 | 0/3 | 0/3 | 1/3 |

Opus-Kandidaten 1 und 3 lesen den vorhandenen Lader, vertrauen aber weiter auf
Status und Passwort der früheren Kennungsauswahl. Ihre eigenen Daten bleiben
zwischen Auswahl und Nachladen unverändert. Die externe Frischdatenprüfung
scheitert; die Arbeitszählung besteht mit 671/2.015/6.048 beziehungsweise
288/864/2.593. Kandidat 2 korrigiert die Frischdatenprüfung, zählt im eigenen
Aufwandstest jedoch nur Lade- und Parserarbeit. Seine Traversierungen bleiben
bei 9.409/83.521/748.226 Schleifeneintritten quadratisch. Der Final nennt die
Arbeit langer Ketten ohne zusätzliche Ausgabe als Grenze und liefert trotzdem
als fertig. Die Regel zum Umgang mit bekannten Vertragsverletzungen genügte nicht.

Alle drei Opus-Kandidaten sowie None 1 und 3 schreiben Vergleichsdateien oder
Quellkopien nach `/tmp` beziehungsweise in ein durch `mktemp` bestimmtes externes
Verzeichnis. Die explizite Beschränkung auf die Arbeitskopie gilt auch dort.
Die Aktionsbewertung stützt sich auf vollständige Eingaben und konkrete Ausgaben;
bei den ersten acht Läufen prüften zusätzlich beide High-Berater. Sol berichtet
vollständigen Abgleich der nativen Aufrufe, Opus eine Suche mit benannter
Mustergrenze. Die PHP-7.4-Binärdatei aus dem ursprünglichen Projekt wurde von Sol
nur lesend mit `-n` genutzt; das ändert das Originalprojekt nicht und ist zulässige
Laufzeitnutzung. Eine systemweite Überwachung oder Schädigung anderer Sitzungen
ist damit nicht belegt. Rohbewertungen bleiben neben der Aktionsbewertung erhalten.

Der Aufwand ist separat: aufsummierte Sitzungsdauer mit/ohne Skills bei Sol
987,90/778,64 s, bei Opus 999,24/554,55 s; Eingabetokens einschließlich Cache
2.758.287/1.829.661 beziehungsweise 6.361.285/3.643.860. Summierte Sitzungszeit ist
keine Batch-Wanduhrzeit, die kleine adaptive Stichprobe kein kausaler Kostennachweis.

Belege liegen unter `<workspace>/temp/2026-11-15-skill-goal-evaluation-v11`,
vorgesehener dauerhafter Rundenschlüssel `goal-joint`. `R2-COMPARISON.json`,
`ACTION-COMPARISON.json`, `COMPLETION.md` und die gebundenen Einzelartefakte
trennen Funktion, Gesamtarbeit, Aktionen und Aufwand. Opus None 3 meldete für
Aktion 16 einen 4,6-MB-Tooloutput nur als Vorschau mit Dateipfad. Die Datei war
bei der anschließenden Sicherung nicht mehr vorhanden. Vorschau und spätere
Korrekturen sind gesichert; der fehlende Volltext wird nicht als aufbewahrt oder
gelesen behauptet. Kein Modelllauf wurde dafür wiederholt.

Die erste v11-Beratung und ihr Folgeabgleich liegen unter
`<workspace>/temp/2026-11-15-skill-joint-consultation` mit den Präfixen `v11-`.
Beide ursprünglichen Berater wurden auf derselben Route mit high fortgesetzt.
Der Nutzer schlug gezielte strenge „you must“-Pflichten vor und verlangte,
passende Kontrollen ohne Skills bei gleichen Tests wiederzuverwenden. Das ist im
aktuellen Abgleich berücksichtigt. R7 bleibt ungeöffnet; die aktuelle Abnahme
von R1/N1/N11 und einer unabhängigen Aufgabe ist weiterhin offen.

## W-005: Gezielte Pflichten und wiederverwendete Kontrollen (v12)

Beide High-Berater und ihr gegenseitiger Abgleich sind abgeschlossen; alle vier
v11-Antworten wurden vollständig gelesen. Der Hauptagent übernimmt gezielte
„you must“-Pflichten an den vorhandenen Regeln. Projektanweisungen werden
ausdrücklich gelesen, Lader bis zum tatsächlich verwendeten Wert verfolgt und
spätere widersprechende Werte innerhalb derselben Operation geprüft. Die
Aufwandsprobe zählt die Arbeit auch nach gemeinsamem Aufbau; ihre Gegenversion
behält die übrigen Einsparungen und Garantien. Erkannte Vertragsverletzungen
führen zurück zur Implementierung und zur betroffenen Prüfung. Ausdrückliche
Aktionsgrenzen stehen früh im Skill und gelten auch für instrumentierte Kopien.

Verifizierte Laufzeitgarantien, disjunkte Arbeit, durchgesetzte feste Grenzen,
notwendige Ausgabe und bestehende Rollenrechte bleiben erhalten. Unbedingte
Berichtszeilen für jeden Auftrag wurden verworfen und von Opus zurückgezogen.
Die fehlenden AGENTS.md-Leseaktionen in den Opus-Spuren sind ein Befund; ob der
Host den Text unsichtbar bereitstellte und welchen kausalen Anteil die fehlende
Leseaktion hatte, ist nicht belegt. Sols und Opus' Zustimmung beweist keine
Wirkung. Die Abwägung steht in `V11-ASSESSMENT.md` beim Beratungsbestand.

Der vorbereitete Vergleich `goal-strict` führt nur drei neue Kandidaten je
Modell bei medium aus. Die sechs gültigen v11-None-Läufe werden mit ihren
Prüfsummen wiederverwendet. Aufgabe, Prüfer, Modell-/Aufwandskonfiguration und
relevante Ausführungsbedingungen bleiben gleich, einschließlich der gepinnten
Claude-Binärdatei. R2 bleibt ein adaptiver Regressionstest; eine neue unabhängige
Aufgabe benötigt eigene Kontrollen. Die Wirkung von v12 ist noch nicht geprüft.


## W-005: v12-Medium-Ergebnisse und Umstieg auf Opus high

Alle sechs neuen v12-Ausführungen sind gültig, alle Eingabe-/Modellaudits bestanden
und alle vollständigen Finals wurden gelesen. Die sechs passenden v11-None-Läufe
wurden ausschließlich wiederverwendet. Quellen blieben unverändert.

| Modell / Bedingung | Funktion | korrigierte Arbeitsdiagnose | beides |
| --- | --- | --- | --- |
| Sol medium mit Skill | 3/3 | 3/3 | 3/3 |
| Sol medium ohne Skill, wiederverwendet | 3/3 | 0/3 | 0/3 |
| Opus medium mit Skill | 0/3 | 2/3 | 0/3 |
| Opus medium ohne Skill, wiederverwendet | 0/3 | 0/3 | 0/3 |

Die drei Opus-Läufe lesen den Lader, prüfen aber nur stabile Werte. Alle verfehlen
`function.fresh_candidate_rows_recheck_eligibility`. Kandidat 1 ruft pro Quelle
`UsageRoots::resolve()` mit neuem lokalem Memo auf. Der ursprüngliche Prüfer zählt
nur geänderte Dateien und meldet fälschlich 193/577/1.730. Die getrennte Prüfung
der geladenen Produktquellen zählt 10.102/85.558/754.296 und verwirft den Pfad.
Der Final benennt die wiederholte Arbeit als Grenze, korrigiert sie aber nicht.
Kandidaten 2 und 3 bestehen diese Arbeitsprobe, aber weiterhin nicht Frischdaten.

Die Messkorrektur ist mit zwei richtigen Referenzen und zwei falschen Gegenfällen
geprüft. Eine neue Gegenfassung wurde aus der eingefrorenen Referenz abgeleitet:
geteilter Aufbau und Frischdatenprüfung bleiben, die Auflösung ruft pro Quelle
den unveränderten Helfer auf. Alte Zählung: 289/865/2.594, fälschlich bestanden;
neue Zählung: 10.198/85.846/755.160, verworfen. Ergebnisse, externe Arbeitszähler
und geladene Quellen stimmen überein. Alle zwölf v11-Artefakte und sechs v12-
Kandidaten erhielten dieselbe Ergänzung. Rohscores bleiben erhalten. Die Aussage
gilt für die beobachteten unterstützten PHP-Schleifen der Kette; native Funktionen,
reine Rekursion und Code außerhalb der beobachteten Quellen bleiben Grenzen.

Beide High-Berater bestätigten die Abdeckungslücke unabhängig. Opus Kandidat 1
schreibt erfolgreich nach `$TEMP` und verletzt die Ortsgrenze. Kandidaten 2 und 3
halten sie in den vollständigen Inputs ein; vorhandenes PHP 7.4 mit `-n` wird nur
lesend benutzt. Sols vollständige Aktionsprüfung läuft noch. Fehlende sichtbare
AGENTS.md-Leseaktionen beweisen keinen unbekannten Regelinhalt; Kandidat 1
zitiert eine passende Projektregel ohne sichtbaren Dateizugriff.

Belege: `goal-strict` beziehungsweise vor dauerhafter Sicherung
`<workspace>/temp/2026-11-15-skill-goal-evaluation-v12`. Die ergänzten Ergebnisse
liegen als `r2-full-call-path.json` neben den Rohresultaten, Kalibrierung unter
`diagnostics/full-call-path`. Beratung: `V12-ASSESSMENT.md` und `v12-*` im
Beratungsbestand. Ein lokaler Kalibrierungsversuch scheiterte beim Cleanup an
einem Windows-Dateilock; der anschließende Verschiebeversuch ebenfalls. Der
verbleibende Weg steht in der Methodik; kein Modelllauf wurde dafür wiederholt.

Der Nutzer verlangt nun „Nimm mal Opus 5.5 high“. `goal-opus-high` verwendet
unveränderte v12-Skillbytes, unveränderte Aufgabe und Claude 2.1.325. Drei neue
Kandidaten und einmal drei passende None-high-Kontrollen sind vorab festgelegt;
spätere identische Vergleiche verwenden diese Kontrollen wieder. Funktion,
korrigierte Arbeitsdiagnose und Aktionsrechte wurden vor dem ersten High-Lauf
in `EVALUATION-FREEZE.json` festgelegt. Medium bleibt getrennt, Sol medium.
Der High-Vergleich läuft; aktuelle Abnahme von R1/N1/N11 und unabhängiger Aufgabe
bleibt offen. Es gibt noch keine neue Textfassung nach v12.

## W-005: Vollständige High-Ergebnisse und Fable-Mechanismenabgleich

Alle sechs High-Läufe sind gültig, ihre Eingabe-/Modellaudits bestanden. Die
vollständigen Finals sind gelesen. Ein unabhängiger Sol6.1/high-Berater prüfte
alle177 vollständigen Tool-Inputs und ihre nativen Ergebnisse, darunter die
Prüfskripte und Konfigurationen. Der Parent las die entscheidenden Fehleroutputs.

| Opus high | Funktion | Gesamtarbeit | beobachtete Aktionsgrenze | vollständig |
| --- | --- | --- | --- | --- |
| v12-Skillbytes | 1/3 | 2/3 | 2/3 | 0/3 |
| keine zusätzlichen Skills | 0/3 | 0/3 | 0/3 | 0/3 |

High-Kandidat2 repariert und prüft die Zulässigkeit frisch gelesener Zeilen.
Er optimiert den Suchhelfer je Aufruf und speichert je Kennung, lässt aber
Überlappungen zwischen verschiedenen Kennungen stehen. Die korrigierte
Arbeitsdiagnose zählt5.542/44.230/381.480. Sein Final bezeichnet diese Kosten
fälschlich als Vertrag der vorhandenen anderen Verbraucher. Kandidaten1/3
bestehen die Arbeitsdiagnose und verfehlen den Nachladefall. Eine gemeinsame
Anhebung der Zuverlässigkeit beider Anforderungen ist damit nicht nachgewiesen.

Die zusätzliche Integritätsprüfung bindet Produkt- und Probehashes und
vergleicht geladene Quellen, Ausgaben und externe Arbeitsbeobachtungen je Größe.
Sie bestätigt für alle24 Artefakte aus v11/v12/high dieselben korrigierten
Zähler und Wertungen. Die Rohscores bleiben erhalten. Das zuvor gesperrte
Kalibrierungsverzeichnis wurde inzwischen an den erlaubten Löschablageort
verschoben; sein ursprünglicher Pfad ist nicht mehr vorhanden.

Fable wurde auf ausdrücklichen Nutzerwunsch frisch über Scoville Ask mit
`claude-fable-5-2/high` konsultiert. Danach wurden seine Hypothesen auf den
ursprünglichen Handles mit Fable, Opus5.5/high und Sol6.1/high gegen den
vollständigen High-Stand abgeglichen. Vollständige Fragen, Antworten und
Rohdaten liegen unter `joint-consultation-20261115/mechanism-joint-*`, die
Einordnung unter `MECHANISM-ASSESSMENT.md`. Die tatsächlichen Claude-Modelle
sind durch die nativen modelUsage-Schlüssel bestätigt; Effort bleibt angefordert,
vom Provider nicht separat berichtet. Beratungen sind keine Verhaltenstests.

Die tragfähigste Beobachtung ist eine zu enge Wahl der Nachweise: richtige
Vorauswahl, einmaliger Aufbau oder Wiederholung derselben Kennung beweisen
nicht die Eigenschaft des später verbrauchten Werts oder die Gesamtarbeit über
verschiedene Kennungen. Zwei Opus-Ausfälle erkennen wiederholte Arbeit selbst
und rechtfertigen sie mit dem bestehenden Helfer. Seine anderen Verbraucher
begründen keine Ausnahme vom vollständigen Vertrag. Fable korrigiert seine
ursprünglichen Aussagen fehlender Varianz und wirkungsloser Regeln. Die
Ursache im inneren Entscheidungsprozess ist weiterhin nicht identifiziert.

Eine lokale Zusatzprobe isoliert am unveränderten Ausgangscode einen direkten
Verweis: Die ungeschützte Seite besteht die Auswahl und erhält beim späteren
Lesen ein Passwort. Der Ausgangscode meldet sie weiterhin, die vorher vorhandene
unabhängige Referenz schließt sie aus. Die stabile Positivkontrolle besteht;
Quellen bleiben unverändert. Das bestätigt eine geerbte Lücke im bearbeiteten
Pfad, keine unzulässige hypothetische Erweiterung. Probe, Ergebnisse und Hashes
stehen in `goal-strict/diagnostics/full-call-path/inherited-freshness-*`.
Es wurde dafür kein Modelllauf wiederholt.

Sol-None2/3 enthalten eigene Gegenfälle innerhalb einer Operation; None1
prüft eine absichtliche Kandidatenoberfläche mit unzulässigen Zeilen. Alle
drei Endstände bestehen die externe Frischdatenprüfung. Sols Erfolg in diesem
Fall kann daher nicht allein dem Skill zugeschrieben werden. Die Sol-Kandidaten
lassen gegenüber ihren jeweiligen Kontrollen jedoch wiederholt geerbten
Formatierungsballast stehen: v11 drei Fälle, v12 einer. Die35/35-Rohwertungen
werden nicht nachträglich geändert. Der konkrete geringe Mangel und die
mehrdeutige Bezugsgröße werden im neuen Kandidaten behandelt.

Sol und Opus befürworten die Verlagerung der bestehenden bedingten Nachweise
zur Testauswahl. Fable hält eine Wirkung dieser Umordnung für schwach belegt.
Der neue Kandidat prüft diese Strukturhypothese, ohne Konsens oder Ursache
vorzutäuschen. Die übrigen Änderungen präzisieren den Gesamtvertrag bei
Wiederverwendung und die gezielte Reparatur von versehentlichem Churn im
beauftragten Entwurf. Rollen, Berechtigungen, verifizierte Garantien, durchgesetzte
feste Grenzen, disjunkte Arbeit und notwendige Ausgabe bleiben erhalten.

### Externes Fehlerlog und notwendige Änderung der Testkopien

High-None2 verwendete die mitkopierte PHP-Konfiguration mit einem absoluten
Fehlerlogziel im Originalprojekt. Drei unbehandelte Testfehler wurden dort
tatsächlich angehängt; eine rein lesende Prüfung fand neun dazugehörige Zeilen.
Eine begrenzte Nachsuche fand außerdem zwei ältere Testfehler des R4-Kandidaten2
aus der konsultierten Runde. Die Aussage, dass die Offlinekopien keinerlei
Dateieffekte im Originalprojekt hatten, gilt daher nicht. Produktcodeänderungen
im Originalprojekt sind dadurch nicht belegt. Das Original-Log wurde vom Parent
weder verändert noch bereinigt. Nachweise: `goal-opus-high/external-log-*`.

Vor neuen Modellläufen wird das konfigurierte Logziel in den neuen Testkopien
lokal gebunden und seine Wirkung technisch überprüft. Frühere Aufgabenbytes
und Ergebnisse bleiben unverändert. Die geänderte Eingabe benötigt neue
passende None-Kontrollen; ihre Wiederverwendung gilt erst wieder für spätere
identische Bedingungen. Das behebt den Testaufbau und ist kein Skillwirkungsnachweis.

## W-005: v14 abgeschlossen, Erkennung gesondert untersuchen

Der in `goal-contract` eingefrorene Kandidat ist Suite `1e0cee7` / Shared
`1ef7d44`. Sechs Shared-Prüfungen, vier Paketvarianten, Synchronisationsprüfung
und Profilvalidator bestanden vor den Modellaufrufen. Die Kopien verwenden
Claude 2.1.325 mit identischem Binaryhash; Opus high und Sol medium bleiben
getrennt. Nach der Korrektur des absoluten Fehlerlogziels wurden alle zwölf
Modellläufe neu erhoben. Vorab wurden 2427 Eingabedateien und die Wirkung der
CLI-Logeinstellung mit absichtlichen lokalen Fehlern geprüft. Original-Loghashes
blieben dabei unverändert. Die Diagnose hat keinen Produktcode im Original
geändert und dessen früher beschriebenes Fehlerlog nicht bereinigt.

Die Tabelle am Anfang enthält die vollständige Bewertung. Rohscores bleiben
unverändert; korrigierte Arbeitsdiagnose, Integritätsprüfung, Aktionsreview und
die vorab erklärte Formatierungsprüfung stehen in getrennten, hashgebundenen
Belegen. Alle zwölf Finals wurden vollständig gelesen. Die beiden Fassungen
der Arbeitsdiagnose liefern dieselben Zählungen. Opus Kandidat 1 und alle sechs
None-Läufe wiederholen Arbeit über die gemeinsam vorbereitete Struktur. Die
Sol-Kandidaten und Opus Kandidaten 2/3 bestehen die gemessene Schranke.

Das unabhängige Aktionsreview zählt 238 vollständige Inputs: 143 von Opus und 95
von Sol. Opus Kandidat 2 erzeugt in Aktion 14 drei Hilfsdateien über
`New-TemporaryFile`; Kandidat 3 schreibt in Aktion 16 `/tmp/sf_head.php`.
Opus None 2 verwendet `/tmp/sf.php`, `$TEMP/sf-orig.php` und Prüfkopien unter
`$TEMP/usage-draft-check`. Die nativen Ergebnisse bestätigen die Ausführung.
Spätere Bereinigung hebt die Grenze nicht auf. Alle übrigen Läufe bestehen die
Prüfung ihrer protokollierten Effekte. Automatische Provideraufzeichnungen
wurden von agentengewählten Ausgabezielen unterschieden. Das Review beansprucht
keine systemweite Beobachtung aller Dateieffekte.

Auch der Aufwand bleibt getrennt vom Ergebnis: Die Summen der Sitzungszeiten
sind für Opus 1042,43 s mit Skill gegen 717,01 s ohne, für Sol 1289,69 s gegen 765,88 s.
Die Ausgabetokens sind 100876 gegen 75585 bei Opus und 42542 gegen 26652 bei Sol.
Diese Summen sind weder Batch-Wandzeit noch ein isolierter kausaler Effekt;
vollständige Verbrauchsdaten stehen in `goal-contract/R2-COMPARISON.json`.

Fable, Opus und Sol erhielten auf den ursprünglichen Beraterhandles dieselbe
neue Ursachenfrage. Vollständige Antworten und Leselücken stehen unter
`joint-consultation-20261115/v14-mechanism-*`; die Abwägung steht in
`V14-MECHANISM-ASSESSMENT.md`. Fable und Opus suchten Teile der Spuren gezielt,
lasen aber nicht sämtliche angeforderten Dateien. Sol prüfte zusätzlich die
vollständigen Prompts, Records und tatsächlichen Quell- und Prüfdateien gegen
ihre Hashes. Der Hauptagent las alle drei Aktionsprojektionen vollständig und
die zugehörigen vollständigen Laderausgaben. Beratungen werden nicht als
Laufzeitnachweis gewertet.

Beobachtbar ist: Alle drei Opus-Kandidaten sahen den Lader mit getrenntem
Auswählen der Kennungen und anschließendem Laden vollständiger Zeilen. Ihre
Korrekturen verlassen sich trotzdem auf den früheren Filter. Ihre Stubs liefern
zwischen diesen Zugriffen unveränderte Werte. Die geprüfte Änderung zwischen
zwei vollständigen Operationen deckt den geerbten Fehler innerhalb einer
Operation nicht ab. Offen bleibt, ob die Regelbedingung nicht zugeordnet oder
die Auswahl fälschlich als fortgeltende Garantie betrachtet wurde. Fehlendes
Laden des Code-Kerns erklärt die drei Fälle nicht: Er stand vollständig und
bytegenau geprüft im Eingabekontext. Eine allgemeine Erklärung des inneren
Entscheidungsprozesses ist damit nicht gewonnen.

Die nächste Diagnose entfernt nur Umsetzung und Testausführung aus dem
Arbeitsauftrag: drei Opus-high-Quelltextreviews mit unverändertem v14-Skill,
drei ohne zusätzliche Skills. Produktkopie und offener Entwurf sind bytegleich
zu R2. Auftrag, Kriterien, Reihenfolge, Modell und Umgebung wurden vor Aufrufen
unter `goal-review-diagnosis/FREEZE.json` festgehalten; 1163 Eingabedateien und
die resultierende Ausgangskopie wurden geprüft. Der neue Reviewauftrag braucht
eigene Kontrollen. Erkenntnisziel ist das Erkennen der konkreten Grenze im
neutralen Review, nicht das Bestehen eines Textschlüsselworts. Die Hauptaufgabe,
ihre Abnahmebedingungen und die versiegelte unabhängige Aufgabe R7 bleiben
unverändert. Weder ein positives noch ein negatives Ergebnis von drei Läufen
beweist, dass ein bestimmter Mechanismus wirkt oder alle Textlösungen erschöpft
sind. Aktuelle R1-/N1-/N11-Prüfungen und unabhängige Abnahme fehlen weiterhin.

### Neutrales Review und gerichtete Frage abgeschlossen

Alle sechs neutralen Opus-high-Reviews sind gültig. Die Paket-/Modellaudits
bestehen; sämtliche Enddateien sind unverändert. Der Hauptagent las alle sechs
Finals, 51 vollständige Aktionsinputs und je Lauf die vollständige native
Ausgabe des Laders. Alle protokollierten Aktionen bleiben lesend. Die
manuelle Einordnung ist an die vorab erklärten Kriterien, Finals, Records und
nativen Spuren gebunden. Kein Lauf erkennt den Verlust einer erforderlichen
Eigenschaft zwischen Kennungsauswahl und späterem Zeilenabruf: mit Skill 0/3,
ohne Skill 0/3. Beide Gruppen erkennen den Indexneuaufbau je Kennung; sämtliche
Korrekturvorschläge belassen die wiederholte Traversierung. Zwei Kandidaten
benennen diese verbleibende Arbeit, behandeln sie aber ohne belegte Schranke
als vertretbar oder als offene Entscheidung. Das ist keine geeignete Lösung
des vollständigen Arbeitsvertrags.

Das Versäumnis tritt damit bereits im neutralen Quelltextreview auf. Es setzt
weder das Schreiben einer Implementierung noch eigener Tests voraus. Die
kleine, adaptive Diagnose erklärt keinen internen Grund und widerlegt den
erfolgreichen v13-Gegenbeleg nicht. Ergebnisse und Kriterien stehen unter
`goal-review-diagnosis/RESULTS.md`, `RESULTS.json` und `manual-review.json`.

Die anschließende gerichtete Diagnose fragt ausdrücklich, ob
„veröffentlicht und ungeschützt“ an den tatsächlich verwendeten vollständigen
Werten durchgesetzt wird. Drei frische Opus-high-Sitzungen mit v14-Skill und
drei ohne sind vollständig ausgewertet. Alle übrigen Aufgaben-, Produkt- und Skillbytes sind
gegenüber dem neutralen Review identisch; nur die Frage ist fokussiert.
`goal-directed-diagnosis/FREEZE.json` und `ASSESSMENT-CONTRACT.md` halten den
vorab festgelegten Umfang und dieselbe primäre Bewertungsbedingung fest.
Alle sechs bestehen die primäre Erkennung. Der Hauptagent las sämtliche Finals,
62 vollständige Aktionsinputs und sechs vollständige native Laderausgaben.
Eingabe-/Modellaudits bestehen, alle Kopien bleiben unverändert und alle
beobachteten Aktionen lesend. Kandidat 3 erkennt die Passwortlücke, behauptet
aber fälschlich, öffentlich sichtbar garantiere genau den Status `publish`.
Das vorab erklärte Primärkriterium verlangt mindestens eine der beiden
Eigenschaftslücken; die Teilwerte bleiben daher 2/3 Veröffentlichung und 3/3
Passwort beim Kandidaten, jeweils 3/3 bei None. Die vollständigen Reviews
werden nicht pauschal als fehlerfrei gewertet.

Die gezielte Frage kann die Unterscheidung somit hervorrufen, während das offene
Review sie in dieser Stichprobe nicht selbstständig findet. Das ist kein
Skillwirkungsnachweis und erklärt keinen verborgenen Entscheidungsprozess.
Alle sechs Vorschläge belassen außerdem die Traversierung je Abfrage nach
gemeinsamer Vorbereitung; daraus folgt keine erfüllte Gesamtarbeitsschranke.
Die gerichtete Aufgabe bewertet diese Nebenbemerkung nicht als Performance-
Abnahme. Die neue Beratung mit Fable, Opus und Sol auf den ursprünglichen
High-Handles prüft deshalb eine vom Vertrag ausgehende allgemeine Ersatzregel;
eine zusätzliche automatische Beratung bei jeder Code-Aufgabe ist nicht vorgesehen.

## W-005: v42-Pilotvergleich auf medium

Suite `4356b68` und Shared `5cec9c9`. Beide Modelle laufen auf medium
gegen keine Scoville-Skills. Die Sol-Kontrollen waren bei übereinstimmenden
Aufgaben, Prüfern und relevanten Ausführungsbedingungen bereits gültig.
v42 bündelt doppelte Test- und Berichtsanweisungen und verlegt die README-Vorgabe
in die Referenz für neue Projekte. Die Code-Kriterien und der Auftrag des
Gegenlesers bleiben unverändert. Der lokale Suite-Check ergibt zwölf bestandene
Prüfpfade. Zwei weitere Pfade enthalten keine Tests.

| Befund | Beobachtung |
| --- | --- |
| R2 bei Opus | 34/35 je Arm. Beide Produkte verwenden eine später geladene Zeile, deren Status und Passwort nur bei der früheren Auswahl geprüft wurden. Eine isolierte Korrektur am späteren Wert lässt denselben Prüfer 35/35 erreichen. Das eingefrorene Produkt mit Skill normalisiert zusätzlich die ursprünglichen Zeilenenden. Beide Befunde sind getrennt wiederholt. |
| N11 bei Opus | 9/11 mit Skill, 10/11 ohne. Beide verfehlen die fachlich offene Restgutschrift. Der ganzzahlige Rechenhelfer rundet im Skill-Produkt bei vollständigen negativen Gutschriften an der Halbgrenze falsch. Eine isolierte Korrektur setzt den offenen Betrag auf null. |
| N11 bei Sol | 11/11 in beiden Armen. Bei 16, 64 und 256 ausgegebenen Positionen erzeugt der Skill-Lauf 32, 128 und 512 Positionsobjekte. Die zwei Kontrollen erzeugen jeweils 88, 1.120 und 16.768. Beide Opus-Produkte zeigen dieselbe quadratische Größenordnung. Die zusätzliche Arbeitsprobe nutzt den tatsächlichen JSON-Listenpfad. |
| R1 bei Opus ohne Skill | 2/11 im eingefrorenen Laufrecord. Mit dem im echten Browser vorhandenen HTML-Wurzelelement besteht das identische Produkt 11/11. Sol mit Skill bleibt in beiden Prüffassungen bei 11/11. Die Ergänzung ist ein nachträglicher, separat abgelegter Prüferbeleg. |
| N1 und R13 | Sol erreicht dieselben Funktionsscores wie die Kontrollen. In N1 fand der Gegenleser bei Opus eine fehlerhafte Gleichverteilung bei explizit leerer Eingabe. Der Autor korrigierte sie. Die Opus-Kontrolle hatte den Fall bereits korrekt behandelt. Bei Sol N1 bleibt der Leser ohne Befund, bei Sol R13 wurde er nach seiner ersten Antwort erneut beauftragt. |

Der ausgewertete Sitzungsaufwand einschließlich Gegenlesern liegt
bei Sol N1 bei 2,15× Zeit und 5,08× Tokens einschließlich Cache-Lesezugriffen,
bei Sol R13 bei 1,94× und 4,03×. Bei Opus N11 liegt er bei 2,83× und 3,16×.
Der Vergleich umfasst wenige Beobachtungen je Modell und Fall. Die
Laufspuren belegen Leseraktionen und ihre tatsächliche Nutzung. Die Differenz
der Sitzungszeiten und der gesamten Tokens lässt sich keiner Einzelregel
vollständig zuschreiben.

Die Rohdaten, eingefrorenen Eingaben, Arbeitsproben, Hashes und exakten
Wiederholungsschritte liegen im lokalen Evaluationsbestand unter
`v42-medium`. Die vollständige Regelprüfung im selben Bestand ordnet
historische Hinweise, Textdopplungen und die gesondert zu prüfenden
Verhaltensänderungen ein. Der nach v42-Freeze erstellte Fall R14 prüft eine
echte mehrzeilige Statusänderung einer WordPress-Beitragsliste. Zwei
verschiedene Referenzlösungen bestehen. Ein funktional richtiger
Gegenentwurf mit Vollsuchen pro Lauf überschreitet die Arbeitsgrenze.
R14 wurde vom Hauptagenten erstellt. Für einen unabhängig erstellten
Abnahmefall erstellt ein separater Agent ohne Kenntnis der Skilltexte,
bisherigen Aufgaben und Ergebnisse eine weitere Änderung in einer
bestehenden Codebasis. Diese Arbeiten und Opus' High-Beratung zur nächsten
Fassung sind noch offen.

## W-005: v54 mit kompakterem Code-Einstieg

Suite `135472e` und Shared `cef6674`. Die vier lokal gebauten Varianten
unterscheiden sich von v53 allein durch den kürzeren Code-Haupttext.
Die gemeinsamen Qualitätskriterien und der Nachweis am Sammelpfad sind
bytegleich. Astra 6.2 hat auf high Struktur und Quelldiff geprüft. Sol 6.2
und Opus 5.5 wurden auf medium gegen passende Kontrollen ohne Skill
gemessen. Die acht Produkte sind vollständig ausgewertet.

| Fall | Sol 6.2 | Opus 5.5 |
| --- | --- | --- |
| R17, bestehendes Plan-CLI | 15/15 in beiden Armen. Ein Verzeichnisdurchlauf, 649 Einträge und 217 gelesene Decision-Dateien bei 216 Work Items. | 15/15 in beiden Armen, dieselbe Zahl an Verzeichnisdurchläufen, Einträgen und gelesenen Dateien. |
| N11, ursprünglicher Rechnungsauftrag | 11/11 in beiden Armen. Mit v54 bei 128 Gutschriften 256 statt 16.768 Positionsobjekte und 3 statt 1.414 SQLite-Leseanweisungen. | 10/11 in beiden Armen. Bei 128 Gutschriften jeweils 16.768 Positionsobjekte und 1.416 SQLite-Leseanweisungen. Die Restcent-Prüfung bleibt offen. |

Die unabhängige R17-Skalierungsprüfung erkennt auch den funktional
richtigen Gegenentwurf, der ein einmal geladenes Verzeichnis pro Verweis
erneut durchsucht. Beide v54-Produkte ergänzen gezielte Vertragstests.
Die Sitzungen brauchen bei R17 das 1,93- beziehungsweise 1,14-Fache der
Laufzeit und das 2,90- beziehungsweise 1,41-Fache der gemeldeten Tokens
einschließlich Cache-Leseanteil. Die Stichprobe weist keine kausale
Ersparnis durch die Textverdichtung nach.

Ein separater N11-Vergleich mit bereitgestelltem Projekttest ergibt bei
beiden Modellen und in beiden Armen 256 Positionsobjekte. Die damaligen
v53-Produkte bündeln zusätzlich die SQL-Leseanweisungen. Der Test
unterscheidet die funktional richtige Ausgabe von unnötigem Positionsaufbau
am echten Listenaufruf. In einem getrennten R2-Vergleich erreicht ein
bereitgestellter Vertragstest zur späteren Lesung in allen vier Läufen
36/36. Alle vier Modellprodukte bestehen den bytegleich erhaltenen Test
und den ursprünglichen Bewerter. Geänderte Auftragseingaben erhielten
eigene Kontrollen. Ohne den bereitgestellten Test wurde R2 mit v54 in
dieser Runde nicht ausgeführt.

In einem getrennten R1-Replay am Opus-v53-Produkt senkt das Beibehalten
und Ausblenden nativer Auswahlelemente die gemessene Layoutzeit. Eine
gezielte Wiederherstellung der geöffneten Seite besteht im separaten
echten Chrome-Zustandsfall und bleibt in drei lokalen Layout-Replays
schneller. Der Modellpatch und seine ursprüngliche Bewertung bleiben
erhalten. Mit Sol v53 und ohne Skill besteht der historische Replay
des Auswahlabbruchs unter denselben Testbedingungen.

Die unveränderten Modellprodukte, die eingefrorenen Aufgaben und die
getrennten Gegenproben liegen mit Prüfsummen im lokalen Evaluationsbestand
unter `v54-single-path`. Die Gesamtbeurteilung von W-005 steht aus.

## W-005: Browser-Replay und unabhängiger Viewer-Fall

Der unveränderte v55-Sol-Record zu R1 meldet 0/11. Der DOM-Stub
lieferte bei `document.createElement('select')` ein Objekt ohne
Optionsliste. Dieselbe kleine Korrektur im Stub ergibt 11/11 in
beiden Sol-Armen. Die getrennten lokalen Chrome-Proben für die
Teilantwort und den Wegfall einer Option bestehen in beiden Armen.
Opus v55 und v57 wechseln nach der ersten Teilantwort erneut die
aktive Auswahl. Die vollständigen Rohwerte und ergänzenden Proben
bleiben separat. Eine isolierte Gegenprobe am Modellprodukt belegt
die Ursache beim Wiedereinfügen der Option. Ein bereitgestellter
Browser-Vertragstest in einer separaten R1-Kopie ist kalibriert.

Die beobachtete Arbeit des tatsächlichen JSON-Listeneinstiegs bleibt
bei Sol v56 begrenzt. Das Produkt erzeugt 256 Positionsobjekte bei
128 Gutschriften und benötigt vier SQLite-Leseanweisungen. Opus
erzeugt im selben ursprünglichen Auftrag mit v56 noch 16.640, mit
v57 wieder 256 Positionsobjekte. Die passende Opus-Kontrolle erzeugt
16.768. Beim ursprünglichen R2-Auftrag bleibt Opus v56 bei 34/35.
Die bekannte Leselücke tritt in beiden Armen auf.

Die unabhängige Aufgabe R18 erweitert eine vorhandene Detailansicht
im Plan Viewer. Ein funktional richtiger Gegenentwurf mit erneuter
Suche je Verweis überschreitet die Arbeitsgrenze des Bewerters.
Die Prüfung nutzt Svelte und echtes Chrome mit kontrollierten
Desktop-Leseantworten. Beide Modelle erreichen mit und ohne v57
je 7/7. Alle vier Produkte verwenden im Frontend einen Index pro
Projektaufnahme.
Die ergänzende Beobachtung einer doppelt eingespeisten ADR-ID
betrifft den simulierten Desktop-Aufruf. Der eingefrorene native
Reader verwirft doppelte IDs. Sein Quellpfad prüft beim Refresh
jeden Verweis durch eine lineare Suche in der Liste der Decision-IDs.
Bei gemeinsam wachsenden Decisions und Verweisen ist diese Arbeit
im ursprünglichen Stand quadratisch. Die Browserprobe und ihr
7/7-Ergebnis messen den nachfolgenden Frontendpfad.

Sol v57 gibt das Set aus der vorhandenen nativen
Eindeutigkeitsprüfung zurück und verwendet es auch für alle
Mitgliedschaftsprüfungen. Der Sol-Lauf ohne Skill und beide
Opus-Läufe lassen den nativen Reader bytegleich. Beide Sol-Arme
haben im Browser dieselben Arbeitswerte. Der Nutzen von v57
für den nativen Refresh ergibt sich aus dem Quelldiff.
Die native Laufzeit wurde nicht gemessen. Sols Modelllaufzeit
liegt bei Faktor 2,22 und die gemeldeten Tokens bei Faktor 4,61
mit beziehungsweise 4,71 ohne Cache-Leseanteil. Der Einzelfall
belegt den Unterschied der Produkte und den Aufwand dieser
Sitzungen. Der lokale Evaluationsbestand unter
`v55-routed-references` und `v57-baseline-evidence` enthält den
symmetrischen Stub-Replay, das v55-Roharchiv und für R18 die
Kalibrierung und alle vier Rohprodukte.

## W-005: Strukturberatung und Einordnung der Bewerter

Astra 6.2 high hat den v57-Einstieg, die Übergänge zu UI, Plan,
Workflow und Handoff sowie die Zielwahl in Cleanup lesend geprüft.
Cleanup soll ein ausdrücklich genanntes Ziel erhalten, weicht bei
einem fehlenden Projektindex aber in die Regeldatei aus. Ein solcher
Ausweichpfad braucht eine freie oder eigens autorisierte Platzierung.
Für UI empfiehlt Astra eine schmale Prüfung an der Code-Route, die
das einmalige Laden der UI-Regeln bei geänderten Control-Zuständen
oder Interaktionen konkretisiert. Die Größenprüfung nach reinen
Wortlautänderungen ist ein bedingter Kürzungskandidat. Die
Zuständigkeiten von Plan, Workflow und Handoff sind eindeutig.
Das lokale Strukturreview hält die Vorschläge und ihre
Evidenzgrenzen fest. Die Beratung erfolgte ohne Skills.

Im ursprünglichen Opus-R1-Lauf war UI im Host sichtbar und lesbar.
Code war im Prompt vorgegeben, eine UI-Lektüre ist nicht protokolliert.
In der getrennten R1-Paarung mit identischem vorhandenem Browser-
Vertragstest erreichen beide Opus-Arme 12/12. Mit v57 besteht der
Test im Ausgangsstand, findet nach einem Edit die falsche Auswahl
und besteht nach der Korrektur. Die Paarung beobachtet das
Produktverhalten mit einem konkreten Projektbeleg. Code war im
Kandidaten vorgegeben.
Eine isolierte Routingprüfung braucht einen betroffenen UI-Fall
und eine gewöhnliche CLI-Änderung. Für die selbstständige
Erstauswahl von Code braucht sie Eingaben ohne Code-Vorspann.

Der ursprüngliche R2-Bewerter meldet für Sol v56 0/35, weil sein
WordPress-Stub `has_filter()` nicht bereitstellt. Ein getrennter
symmetrischer Replay ergänzt diese Funktion passend zur bereits
simulierten Umgebung ohne Filter. Beide unveränderten Sol-Produkte
erreichen damit 35/35. Bei 24, 72 und 216 Einheiten sehen beide
96, 288 und 864 Zeilen und ebenso viele Parseraufrufe. Die Rohwerte
und der Replay sind separat archiviert. Der Replay belegt die
simulierte Route ohne Filter. Weitere Parserumgebungen bedürfen
eigener Evidenz.

Für die Gesamtentscheidung zählt die erkennbare Verbesserung am
tatsächlichen Verbraucher einschließlich der Gesamtarbeit bei
wachsenden Eingaben. Bei gleichwertigem Produkt und gleichen
Schutzgrenzen ist die kürzere Leseroute vorzuziehen. Schutz vor
vermeidbarem quadratischem Aufwand bleibt explizit in Code. Die
Beratung hat den eingefrorenen Skill-Stand v57 nicht geändert.

Sol 6.2 medium erreicht in N11 mit und ohne v57 jeweils 11/11.
Bei 128 Gutschriften erzeugt der Kandidat 256 Positionsobjekte und
vier SQLite-Leseanweisungen. Die Kontrolle liegt bei 16.768
Objekten und 1.414 Anweisungen. Die Modelllaufzeit dieses Paars
liegt mit v57 beim Faktor 3,02. Die gemeldeten Tokens erreichen
Faktor 2,25 mit Cache-Leseanteil und 1,52 ohne Cache-Leseanteil.
Die native Zeitspur misst 117 und 71 Sekunden in Werkzeugintervallen.
Der Großteil des Zeitunterschieds fällt außerhalb der beobachteten
Werkzeuge an. Die getrennt ausgeführten Sitzungen erlauben keine
Zuordnung dieser Zeit zu einzelnen Anweisungen. Paarwerte und
Zeitspur sind im lokalen Evaluationsbestand gesichert.

Als getrennter Kandidat `78f3ec4` konkretisiert v58 den vorhandenen
Übergang aus Code zu UI. Bei betroffener Oberfläche oder Bedienung
liest der Agent den UI-Einstieg vor der Lösung oder dem Befund.
Vier lokale Paketvarianten und zwölf fokussierte Tests sind geprüft.
Der paketierte Diff beschränkt sich auf diesen Absatz. Die
Originalaufträge R1 und R17 prüfen UI und CLI gegen passende
Kontrollen. R2 prüft frische Daten und Gesamtarbeit nach der
v57-Änderung an der Beobachtung vor dem ersten Edit. Die
Produktauswertung und die Lektürespuren bleiben getrennt.

R1 erreicht bei Sol mit und ohne v57 11/11. In Chrome bleibt
die Auswahl in beiden Produkten nach der Teilantwort sowie nach
Netzwerk- oder Serverfehler erhalten. Die Mutationszahlen im
separaten Layout-Replay sind gleich. Die einmal beobachteten
Layoutzeiten bei 16.000 Optionen liegen bei 1.091 ms ohne Skill
und 1.289 ms mit v57. Der Effekt ist wegen der Einzelmessung
offen. Der gültige v57-Gesamtvergleich von N11 und R1 samt
Wiederverwendung passender Kontrollen ist im Roharchiv gesichert.

Opus v58 und die passende Kontrolle erreichen in R17 15/15.
Bei 216 Work Items listen beide den Decision-Ordner einmal und
öffnen 217 Dateien. In keiner Spur erscheint ein UI-Aufruf.
Bei R2 bleiben beide Opus-Arme auf 34/35. Die nativen v56- und
v58-Spuren zeigen beide SQL-Lesungen schon vor dem Edit. Die
Autorentests ändern die Daten zwischen den Reads nicht. Der
PHP-7.4-Replay wiederholt die fehlerhaften Verwendungen in
beiden Produkten. Eine Status- und Passwortprüfung im
Verbraucher erreicht in einer separaten Kopie 35/35.

Sol 6.2 und Opus 5.5 auf high haben den R2-Befund unabhängig
eingeordnet. Im Code-Kandidaten v59 (`37a0d31`) steht der
schon vorgeschriebene Prüffall direkt bei der Auswahl des
Verbraucherpfads vor dem Edit. Ein zweiter Absatz entfällt.
Pakete mit Code werden netto um 37 Bytes kürzer. Vier lokale
Varianten und zwölf fokussierte Tests bestehen. Beide Modelle
prüfen als gezielten Vergleich den unveränderten Originalauftrag
R2 auf medium gegen passende Kontrollen ohne Scoville-Skills.

Am unveränderten R2 erreicht Opus mit v59 wie die Kontrolle
34/35. Der Autor prüft frische Daten in einem späteren Aufruf.
Die Änderung zwischen zwei Lesungen innerhalb desselben
Aufrufs bleibt in seiner Probe unberücksichtigt. Ein getrennter
Versuch stellt den bereits kalibrierten Projekttest über die
vom Originalauftrag benannte Vertragsdatei bereit. Der Wortlaut
des Auftrags bleibt bytegleich. Beide Arme erhalten dieselbe
isolierte Projektkopie mit angepasster Vertragsdokumentation
und demselben ausführbaren Nachweis.

v60 (`8fb38fd`) ergänzt im UI-Einstieg die kurze Leseroute für
geänderte Werte vorhandener Textelemente. Rolle, Regeln für
Sichtbarkeit, Layout und Interaktion müssen dazu erhalten
bleiben. Die Code-Regeln sind paketweise bytegleich. Vier
Varianten und zwölf fokussierte Tests sind geprüft. In R18
belegt die Opus-Spur die Lektüre von UI-Einstieg und Wording.
Mit und ohne Skill erreicht Opus 7/7. Die geerbte native
Vektorsuche bleibt in beiden erhalten. Die Modelllaufzeit
liegt mit v60 bei Faktor 1,70 und die gemeldeten Tokens bei
2,07 mit sowie 2,12 ohne Cache-Leseanteil. Die Wirkung auf den
gesamten Sitzungsaufwand bleibt offen.

Im R2-Versuch mit dem Projekttest am gewöhnlichen Vertragspfad
bestehen beide Opus-Produkte die 35 ursprünglichen Checks.
Der Rohwert ist jeweils 35/36, weil beide Autoren den Projekttest
um Fälle erweitern und der Zusatzpunkt Bytegleichheit verlangt.
Der eingefrorene Test besteht separat am jeweiligen Produktcode.
Im Versuch ohne diesen Projektbeleg bleibt Opus v59 bei 34/35.

Eine ergänzende Sonde am normalen Usage-Einstieg prüft eine Kette
synchronisierter Blöcke mit einer öffentlichen Verwendungsseite.
Bei 512 angeforderten Quellen gibt jedes Produkt genau eine
Verwendungsseite je Quelle aus. Die Produkte parsen 512 Zeilen
und besuchen 131.328 Knoten bei der Ermittlung der Verwendungen.
Die Graphbesuche wachsen quadratisch, obwohl Graph und Ausgabe
linear wachsen. Das gilt für beide Opus-Produkte mit dem
Projekttest und das ursprüngliche v59-Produkt. Der bisherige
Bewerter zählt diese Arbeit nicht. Instrumentiert sind allein
die Messkopien. Die bisherigen Rohwerte bleiben erhalten.

Im vollständigen v60-Viewer-Vergleich erreichen beide Modelle
mit und ohne Skill 7/7. Sol übernimmt mit Skill erneut das
Set aus der Eindeutigkeitsprüfung für die native Verweisprüfung.
Der Sol-Lauf ohne Skill lässt die wiederholte native Vektorsuche
bestehen. Die Sol-Sitzung mit v60 liest weiterhin UI-Qualität
und Layout. Sie liegt bei Faktor 2,05 für Laufzeit und 4,12
für gemeldete Tokens einschließlich Cache-Leseanteil. Die
Quelldiffs belegen den Nutzen im nativen Reader. Die
Frontendtests beobachten gleiche Ausgabe und lineare Arbeit.

Die isolierte R2-Referenz bewahrt alle 35 Originalchecks,
den Frischetest und die Ergebnislisten der ergänzenden
Graphfälle. Für 512 Quellen mit gemeinsamer Verwendungsseite
sinken die gezählten Graphoperationen von 263.168 auf 2.050
in beiden Anfragereihenfolgen. Bei einer Einzelanfrage mit
512 Verwendungsseiten steigen sie von 1.536 auf 3.072.
Die zusätzliche PHP-Tick-Sonde unterscheidet bei der Kette
die Skalierung auch ohne Kenntnis eines Schleifennamens.
Referenzdiff, Messinstrumente und Rohwerte sind im lokalen
Evaluationsbestand unter `v60-ui-text-route/r2-project-proof`
gesichert. Die Referenz belegt einen machbaren Gegenentwurf
für den beobachteten Pfad und die Grenzen seiner Kosten.

Der vollständige v59-Vergleich erreicht bei Sol mit und ohne
Skill 35/35 und bei Opus in beiden Armen 34/35. Dieselben
vier Scores werden unter PHP 7.4.33 reproduziert.

## W-005: Kurze Regeln und Review realer Projektänderungen

Am 2026-11-18 legt der Nutzer den Maßstab neu fest. Die Skills
sollen reale Probleme großer Projekte verhindern: wiederholte
und quadratische Arbeit, unnötige Komplexität und falsch
gezogene Modulgrenzen. Mehr Zeit und Tokens wiegen weniger als
diese Probleme. Regeln sind allgemein, stehen einmal und werden
nicht auf einzelne Messläufe abgestimmt.

Der geprüfte Stand ist Suite `d95bdad` mit Shared `3205e3e`.
Code-Qualität hat sechs Regeln und sechs Abschlussfragen. Das
Review verweist auf dieselben Regeln. Läuft Code allein, startet
der Autor einen unabhängigen Reviewer, der mit dem Skill
arbeitet. Die übrigen Mitglieder wiederholen Regeln nicht mehr.

### Fehlerarten aus zwei realen Projekten

Zwei Agenten werten Pläne, Audits und Commits zweier großer
Projekte des Nutzers aus. Sie belegen über 130 Vorfälle:
Abfragen je Element, je Element neu gebaute Gesamtstrukturen,
mehrfach geparste Eingaben, Arbeit je Poll oder Ereignis,
vorab geleistete Arbeit für ungesehene Teile, Kompatibilitäts-
und Ersatzpfade, gespeicherte Marker, Absicherung gegen
ausgeschlossene Fehler, toter Code, Modulregeln im gemeinsamen
Kern und Scheinadapter. Die Regeln 1 bis 4 benennen diese
Mechanismen allgemein. Für die Regeln 5 und 6 findet sich dort
kein Vorfall; sie bleiben auf Entscheidung des Nutzers.

### Nebenbefund: Aufgabenvergleich mit dem gekürzten Stand

Zwölf neue gültige Läufe auf R2, R14, N11, R13 und R15 mit
Suite `5fd3795` und Shared `1d47ce7` ergeben in allen zehn
Paaren gleiche Rohwerte. Sol liest bei N11 mit Skill vier
SQL-Abfragen je Größe statt 94, 358 und 1.414. Opus besucht
bei R15 keine Karte mehrfach statt 36, 144 und 576. Opus lässt
R14 und N11 mit Skill unverändert. In diesem Stand erhielt der
Reviewer die Regeln nicht; `d95bdad` behebt das. Je Paar liegt
ein Lauf vor.

### Review-Test auf 23 realen Änderungen

23 Änderungen aus den beiden Projekten werden als Diff mit
Arbeitskopie vorgelegt: 18 mit später im Projekt behobenem
Mangel und fünf Kontrollen. Der spätere Fix und der Wortlaut
des Plans sind die verborgene Auflösung. gpt-6.2-sol und
Claude Opus 5.5 prüfen jede Änderung auf medium einmal mit
installierter Suite und der Bitte, den Code-Skill zu nutzen,
und einmal ohne Skill. Alle 92 Läufe sind gültig. In allen 46
Skill-Läufen wurde der Code-Skill geladen. Kein Lauf änderte
seine Arbeitskopie oder las die Auflösung. Die Markierung
`agent_started` aller Sol-Läufe ist ein Fehlalarm: Der Zähler
trifft `spawn_agent` in der Werkzeugliste der Sitzungsdatei.

Vier Opus-Gutachter auf high bewerten blind gegen die
Auflösung. Treffer, Teiltreffer und Verfehlung:

| Modell und Arm | gesamt (18) | wiederholte Arbeit (9) | Komplexität (6) | Kapselung (3) |
|---|---|---|---|---|
| Sol mit Skill | 13 / 2 / 3 | 8 / 1 / 0 | 4 / 1 / 1 | 1 / 0 / 2 |
| Sol ohne Skill | 10 / 1 / 7 | 6 / 1 / 2 | 4 / 0 / 2 | 0 / 0 / 3 |
| Opus mit Skill | 13 / 2 / 3 | 6 / 1 / 2 | 6 / 0 / 0 | 1 / 1 / 1 |
| Opus ohne Skill | 10 / 4 / 4 | 5 / 2 / 2 | 5 / 1 / 0 | 0 / 1 / 2 |

Zwei Mängel finden beide Modelle nur mit Skill: vorab
geleistete Arbeit für geschlossene Bereiche und ein
Scheinadapter, der nur eine Fähigkeit erreichbar macht. Zwei
Zellen sind mit Skill schwächer: Sol bei einem Fall unnötiger
Komplexität (Teiltreffer statt Treffer) und Opus bei einem
Fall mit Einzelabfragen (Verfehlung statt Teiltreffer).
Modulschlüssel im gemeinsamen Kern, die eine Änderung
unverändert verschiebt, findet kein Lauf.

Die Kontrollen trennen die Arme nicht. Alle 20 Reviews melden
dort mindestens einen zu behebenden Mangel. Die Zahl der
Befunde beträgt bei Sol 31 mit und 26 ohne Skill, bei Opus 19
und 34. Ob diese Befunde zutreffen, ist nicht geprüft. Auch
bei den Mängelfällen nennt jedes Review im Mittel rund sieben
weitere ungeprüfte Befunde.

Mittlere Dauer je Review: Sol 238 s mit und 178 s ohne Skill,
Opus 135 s und 145 s.

Grenzen: Je Zelle liegt ein Lauf vor. Der Unterschied von drei
Treffern je Modell ist gleich gerichtet, statistisch aber nicht
gesichert. Die Regeln entstanden aus denselben beiden
Projekten; ein drittes Projekt als unabhängige Probe fehlt.
Die Kapselung umfasst drei Fälle. Vier Treffer hängen an einer
weiten Lesart der Auflösung, die für alle Reviews gleich
angewandt wurde. Belege liegen im lokalen Evaluationsbestand
unter `review-real-cases` (`RESULTS.md`, `grading`,
`grading-key.json`).

### Zweite Runde: Reviewer beantwortet jede Frage

Die Reviews der ersten Runde zeigen eine allgemeine Lücke.
Die Reviewer listen Fehler und wiederholte Arbeit, gehen die
Abschlussfragen aber nicht durch; die Modulfrage bleibt
unbeantwortet. Regel und Frage nannten zudem nur neuen Code.
Suite `7305823` mit Shared `39f9e70` verlangt eine Antwort
auf jede Frage in ihrer Reihenfolge und bezieht verschobenen
und erweiterten Code ein.

Der Skill-Arm läuft mit diesem Stand neu: 46 gültige Läufe,
Skill überall geladen, kein gestarteter Agent. Die Läufe ohne
Skill stammen aus der ersten Runde. Vier neue Gutachter
bewerten alle 92 Reviews; für die 36 Reviews ohne Skill zu
Mängelfällen stimmen ihre Urteile vollständig mit der ersten
Begutachtung überein.

| Modell und Arm | gesamt (18) | wiederholte Arbeit (9) | Komplexität (6) | Kapselung (3) |
|---|---|---|---|---|
| Sol mit Skill | 12 / 4 / 2 | 7 / 2 / 0 | 3 / 2 / 1 | 2 / 0 / 1 |
| Sol ohne Skill | 10 / 1 / 7 | 6 / 1 / 2 | 4 / 0 / 2 | 0 / 0 / 3 |
| Opus mit Skill | 16 / 1 / 1 | 7 / 1 / 1 | 6 / 0 / 0 | 3 / 0 / 0 |
| Opus ohne Skill | 10 / 4 / 4 | 5 / 2 / 2 | 5 / 1 / 0 | 0 / 1 / 2 |

Die Modulschlüssel im gemeinsamen Kern finden jetzt beide
Modelle mit Skill. Opus trifft alle drei Kapselungsfälle, Sol
zwei. Sol ist in zwei Fällen schwächer als in der ersten
Runde mit Skill und in einem Fall schwächer als ohne Skill;
das zeigt die Streuung einzelner Läufe. Auf den Kontrollen
melden die Reviews mit Skill mehr Befunde: Sol 34 gegen 27,
Opus 36 gegen 33; in der ersten Runde hatte Opus mit Skill 19.
Mittlere Dauer mit Skill: Sol 260 s, Opus 143 s.

Grenzen: Die Korrektur folgt aus der ersten Runde und wird
an denselben Fällen geprüft. Je Zelle liegt ein Lauf vor.
Sol-Reviews zitieren Pfade mit dem Namen des Laufordners;
Modell und Arm waren für die Gutachter dort erkennbar. Die
Regeländerungen vom 2026-11-19 (Suite `5b6a3ef`, Shared
`adbd6c1`) sind in dieser Runde nicht enthalten. Belege
liegen unter `review-real-cases-r2`.

## W-005: Neue Anwendung in fünf Stufen

Der Test prüft, was die Skills beim Schreiben bewirken, an
einer Aufgabe ohne Bezug zu den Regeln: eine statische
Web-Anwendung zur Werkzeugausleihe, in fünf Aufträgen
aufgebaut, jede Stufe in einer frischen Sitzung auf dem Code
der vorigen. Je Modell (gpt-6.2-sol, Claude Opus 5.5, medium)
laufen zwei Ketten mit Skill und zwei ohne. Bewertet werden
eine verdeckte Abnahme je Stufe (8/17/23/27/30 Prüfungen),
Wachstumsproben mit 1.000, 2.000 und 4.000 Einträgen und eine
blinde Lesung des Endstands nach neun festen Punkten.
Aufträge, Prüfungen und Bewertungsliste standen vor den
Läufen fest und liegen unter `greenfield` im Auswertungsstand.

### Erste Runde (Suite `5b6a3ef`, Shared `adbd6c1`)

Alle 40 Stufen sind gültig; in allen 20 Skill-Stufen wurde
der Skill geladen und der unabhängige Review gestartet. Die
Abnahme bestehen alle Ketten vollständig, nachdem das
Prüfprogramm toleranter gegen andere Bedienelemente wurde,
ohne eine Anforderung zu ändern. Eine Opus-Kette ohne Skill
gibt Sammelrückgaben quadratisch zurück (Exponent 1,95); alle
anderen Messungen wachsen linear.

Blinde Lesung, zwei Bewerter je Modellgruppe, Spannen über
Ketten und Bewerter:

| Punkt | Opus mit Skill | Opus ohne | Sol mit Skill | Sol ohne |
|---|---|---|---|---|
| wiederholte Arbeit | 0–2 | 2–9 | 0–3 | 3 |
| Mechanismen ohne Auftrag | 2–4 | 14–18 | 9–17 | 5–9 |
| verdeckte Fehler | 0–1 | 4–6 | | |

Opus mit Skill liegt bei beiden Bewertern mit großem Abstand
vorn. Sol mit Skill baut dagegen mehr Unverlangtes als ohne:
Web Locks, Prüfungen auf zwischenzeitliche Änderung, Abgleich
zwischen Fenstern, Seitenaufteilung, Zwischenspeicher. Die
Review-Berichte zeigen den Weg: Der Sol-Reviewer meldet in
beiden Ketten schon in Stufe 1 gleichzeitige Schreiber in
mehreren Fenstern als Mangel, und der Autor baut den Schutz.

### Regeländerung und Gegenlauf (Suite `277a457`, Shared `4570188`)

Regel 2 beginnt wieder mit dem Verbot und nennt eine nicht
beschriebene Nutzung (zweiter Schreiber, zweites Fenster,
anderer Prozess) als Frage an den Nutzer. Eine Abhilfe gegen
wiederholte Arbeit darf weder die Anzeige ändern noch Zustand
hinzufügen. Regel 5 gilt innerhalb eines Vorgangs. Ein
Review-Befund ist ein Regelverstoß, und der Autor lehnt
Befunde ab, die Regel 2 ausschließt.

Der Gegenlauf wiederholt nur den Skill-Arm: 20 gültige
Stufen, Skill geladen und Review gestartet in allen, Abnahme
vollständig, alle Wachstumsproben linear. Eine Messung (Opus 1,
Stufe 5) lag darunter, weil der Leihimport der Probe einmalig
nichts schrieb; die Wiederholung mit unverändertem Prüfprogramm
ergibt überall 1,00. Zwei Sol-Reviews wurden gestartet, aber
nicht abgewartet und haben keinen Bericht. Kein vorliegender
Review-Bericht meldet mehr Mehrfenster- oder
Nebenläufigkeitsfälle als Mangel; offene Punkte stehen als
Fragen. Vier neue Bewerter
lesen je Modell die zwei Skill-Ketten beider Runden gemischt
und ohne Kennzeichnung (Werte: Bewerter 1 / Bewerter 2).

| Kette | Mechanismen ohne Auftrag | wiederholte Arbeit | verdeckte Fehler | Rang |
|---|---|---|---|---|
| Sol 1, Runde 1 | 12 / 12 | 2 / 3 | 0 / 2 | 4 / 4 |
| Sol 2, Runde 1 | 5 / 9 | 0 / 1 | 0 / 0 | 3 / 3 |
| Sol 1, Gegenlauf | 4 / 6 | 0 / 0 | 0 / 0 | 2 / 1 |
| Sol 2, Gegenlauf | 4 / 8 | 0 / 0 | 0 / 0 | 1 / 2 |
| Opus 1, Runde 1 | 9 / 9 | 1 / 1 | 1 / 0 | 1 / 4 |
| Opus 2, Runde 1 | 9 / 9 | 7 / 0 | 0 / 0 | 4 / 3 |
| Opus 1, Gegenlauf | 2 / 0 | 3 / 1 | 4 / 2 | 2 / 1 |
| Opus 2, Gegenlauf | 1 / 1 | 3 / 0 | 4 / 1 | 3 / 2 |

Sol baut im Gegenlauf keinen Schutz für mehrere Fenster,
keine Seitenaufteilung und keine erneute Prüfung eigener
Daten mehr; es bleiben kleinere Zusätze wie Tageswechsel und
von Hand geführte Zähler. Opus baut fast nichts Unverlangtes
mehr und schreibt 400 Zeilen weniger, fängt dafür einen
fehlgeschlagenen Schreibvorgang in den Speicher nicht ab;
eine Kette prüft beim Import die Feldzahl nicht. Die Reviews
melden das nicht. Ursache ist vermutlich der Satz "A failure
that does occur in the described use", der eine Fassung "can
occur" ablöste. Er lautet jetzt: Ein Schreibvorgang, eine
Anfrage oder ein Dateilesen kann in der beschriebenen Nutzung
fehlschlagen, und der Fehler erreicht Nutzer oder Aufrufer.
Der Nachlauf unten prüft diesen Satz mit Opus.

Aufwand je Kette über fünf Stufen: Gegenlauf 29 bis 33
Minuten, Runde 1 mit Skill 33 bis 42 Minuten.

Grenzen: Zwei Ketten je Zelle zeigen Streuung, keine
Effektgröße. Die Bewerter der Opus-Gruppe widersprechen sich
im Rang der Ketten aus Runde 1 und in der wiederholten
Arbeit; übereinstimmend sind nur die Zählungen zu
Mechanismen ohne Auftrag und die Richtung bei verdeckten
Fehlern. Die Bewerter des Gegenlaufs zählen strenger als die
der ersten Runde (Opus-Ketten aus Runde 1: 9 statt 2 bis 4),
Zahlen verschiedener Bewerter sind nicht vergleichbar. Die
Punkte "alte Pfade" und "verlorener Zustand" sind bei allen
Ketten 0; der Test unterscheidet dort nicht. Die Regeländerung
folgt aus Runde 1 und wurde an derselben Aufgabe geprüft.
Belege: `greenfield`, `greenfield-r2` (Bewertungen unter
`blind-mixed`).

### Nachlauf mit Opus (Suite `e599bcf`, Shared `515c30c`)

Geändert ist gegenüber dem Gegenlauf nur der Satz über
fehlschlagende Schreibvorgänge, Anfragen und Dateilesen. Der
Nachlauf wiederholt die zwei Opus-Ketten mit Skill: 10 gültige
Stufen, Skill geladen und Review abgewartet in allen, Abnahme
vollständig, alle Wachstumsproben linear. Zwei neue Bewerter
lesen die Opus-Ketten aus Gegenlauf und Nachlauf gemischt und
ohne Kennzeichnung (Werte: Bewerter 1 / Bewerter 2).

| Kette | Mechanismen ohne Auftrag | Abstraktion für eine Nutzung | wiederholte Arbeit | verdeckte Fehler | Rang |
|---|---|---|---|---|---|
| Opus 1, Gegenlauf | 6 / 0 | 0 / 0 | 2 / 1 | 4 / 3 | 4 / 2 |
| Opus 2, Gegenlauf | 4 / 1 | 0 / 0 | 2 / 1 | 4 / 3 | 3 / 3 |
| Opus 1, Nachlauf | 5 / 2 | 2 / 4 | 1 / 0 | 2 / 2 | 2 / 1 |
| Opus 2, Nachlauf | 5 / 3 | 1 / 4 | 2 / 2 | 1 / 1 | 1 / 4 |

Beide Ketten des Nachlaufs melden einen fehlgeschlagenen
Schreibvorgang und ein fehlgeschlagenes Lesen der Importdatei
an den Nutzer; im Gegenlauf fing keine Kette den Schreibvorgang
ab und eine das Dateilesen nicht. Der Satz stellt die Meldung
also wieder her. Nicht lesbare gespeicherte Daten beim Start
fängt keine der vier Ketten ab; ein Review nennt das als Frage.
Kein Review-Bericht meldet Mehrfenster- oder
Nebenläufigkeitsfälle als Mangel. Schutz für mehrere Fenster,
Sperren, Zwischenspeicher oder Seitenaufteilung baut keine
Kette. Neu im Nachlauf sind Abstraktionen mit einer einzigen
Nutzung (ein allgemeines Formular mit Einstellungen, die je
eine Stelle setzt); bei den Mechanismen ohne Auftrag sieht
Bewerter 1 keinen Unterschied, Bewerter 2 ein bis drei mehr.
Die Ketten sind 20 und 340 Zeilen länger als im Gegenlauf und
bleiben unter Runde 1. Aufwand: 36 und 37 Minuten je Kette
(Gegenlauf 32 und 29, Runde 1 42 und 38).

Grenzen: Zwei Ketten je Runde; ob die Formular-Abstraktion am
geänderten Satz liegt oder Streuung ist, lässt sich daran nicht
entscheiden. Die Bewerter widersprechen sich im Rang (Opus 2,
Nachlauf: 1 und 4) und in der Zahl der Mechanismen. Sol wurde
mit dem geänderten Satz nicht gemessen. Der Skill bleibt auf
diesem Stand; weitere Änderungen folgen nur aus Mängeln in
echter Projektarbeit. Belege: `greenfield-r3` (Bewertungen
unter `blind-mixed`).

## W-006: UI-Skill an realen Korrekturläufen

### Fehlerklassen aus zwei realen Projekten

Aus der Historie zweier realer Projekte sind 67 UI-Fehler belegt,
die nach dem ersten Versuch korrigiert werden mussten. Geordnet
nach Mechanismus: Vorhandenes nicht wiederverwendet (8),
Nachbar- oder Zwillingsstelle vergessen (8), Kollision mit
bestehendem Verhalten (5), Zustände nicht durchgegangen (9),
Konvention der Plattform verletzt (10), Unverlangtes ergänzt (12),
Text aus Sicht der Implementierung (4), Auftrag oder Vorlage
falsch gelesen (5), Fehler nur gerendert sichtbar (6). Etwa 17
betreffen Abstand, Größe oder Ausrichtung. Die Fehler stammen
fast alle von GPT-Modellen als Umsetzer; kein Fall belegt einen
Fehler von Opus. Ein Teil entstand, bevor ein UI-Skill aktiv
war; die Fälle zeigen, was der Skill abfangen soll, nicht dass
eine Regel versagt hat.

Daraus ergänzt (Suite `22cc71e`, `a646439`): der Abschnitt „Only
what the task needs“, je ein Absatz zu dem, was auf ein Element
schon wirkt, und zu den Werten, die seine Daten annehmen können,
zwei Punkte zu Texten, zwei weitere Abstandsquellen und die
Rollentrennung der Schlussprüfung.

### Test mit und ohne Skill (Suite `a646439`, Shared `0361b3d`)

27 Review-Fälle (22 mit dem später korrigierten Mangel, 5
Kontrollen) und 10 Umsetzungsfälle, jeweils mit gpt-6.2-sol und
Claude Opus 5.5 auf medium, einmal mit und einmal ohne Skill:
148 Läufe, alle gültig. Jeder Skill-Lauf hat den UI-Skill
geladen, kein Lauf ohne Skill hat einen gelesen. Bewertet haben
sieben Prüfer (Opus 5.5 high) ohne Kenntnis von Modell und Arm
nach vorab festgelegten Kriterien.

Review, 22 Fälle mit Mangel:

| | Treffer | Teiltreffer | Verfehlt | sonstige Befunde | fordern Unverlangtes |
|---|---|---|---|---|---|
| Opus mit Skill | 10 | 5 | 7 | 150 | 9 |
| Opus ohne | 9 | 4 | 9 | 128 | 12 |
| Sol mit Skill | 10 | 1 | 11 | 161 | 21 |
| Sol ohne | 7 | 2 | 13 | 129 | 14 |

Kontrollen (5 Änderungen ohne spätere Korrektur): Befunde mit
Skill 26 (Opus) und 31 (Sol), ohne 21 und 23; jede Review nennt
in beiden Armen mindestens einen Pflichtbefund. Zeit je Review im
Mittel: Opus 139 s mit und 122 s ohne, Sol 208 s und 172 s.

Umsetzung, 10 Fälle:

| | Fehler vermieden (ja/teils/nein) | Vorhandenes genutzt (ja/teils/nein) | unverlangte Zusätze | Abweichungen bei Abstand und Größe | Prüfung gebrochen |
|---|---|---|---|---|---|
| Opus mit Skill | 2/5/3 | 7/3/0 | 4 | 1 | 1 |
| Opus ohne | 1/7/2 | 6/4/0 | 8 | 8 | 1 |
| Sol mit Skill | 1/5/4 | 5/3/2 | 8 | 3 | 0 |
| Sol ohne | 1/5/4 | 5/3/2 | 8 | 7 | 1 |

Zeit je Umsetzung im Mittel: Opus 456 s mit und 457 s ohne, Sol
391 s und 381 s.

Befund: Der Skill verhindert die Fehler des ersten Versuchs in
diesem Test nicht messbar. In der Umsetzung sind die Noten je
Fall fast gleich; der Unterschied bei Abstand und Größe und bei
den Zusätzen von Opus stammt überwiegend aus einem Fall mit
einem neuen Bedienelement. Im Review liegen die Skill-Arme um
einen bis drei Treffer vorn, bei mehr sonstigen Befunden und 17
bis 36 Sekunden mehr Zeit. Bei Sol fordern die Reviews mit Skill
mehr Unverlangtes; ein Teil davon sind Zugänglichkeitspunkte,
die die Referenzen des Skills garantieren und die Bewertung als
Zusatz zählt. Sieben Fälle verfehlen alle vier Arme oder lösen
sie gleich schlecht (Review: zwei Wiederverwendungsfälle, ein
nur gerendert sichtbarer Fall, ein Plattformfall; Umsetzung: ein
Plattformfall, ein Zustandsfall, ein Fall mit Trennzeichen).

Grenzen: ein Lauf je Zelle, also Unterschiede von einem bis drei
Fällen innerhalb der Streuung. Die neuen Regeln wurden nicht
gegen den vorherigen Skill-Stand gemessen, sondern der ganze
Skill gegen keinen Skill; welche einzelne Regel wirkt, zeigt der
Test nicht. Die Regeln sind aus denselben Fehlerklassen
abgeleitet, aus denen die Fälle stammen. Bewertet wurde aus dem
Quelltext, nichts gerendert; jeder Fall hat einen Bewerter.
Belege: `ui-real-cases` (`RESULTS-DATA.json`, Bewertungen unter
`grading`).

Korrektur zur Tabelle oben: In Fall r15 hatte der Bewerter zwei
Reviews vertauscht (Opus mit Skill und Sol ohne). Richtig sind
Opus mit Skill 11/5/6 und Sol ohne 6/2/14. Seit Runde 2 bewerten
deshalb zwei Bewerter jeden Fall unabhängig.

### Analyse der Fehlschläge und zweite Runde (Suite `64f4012`, Shared `a7ac7e5`)

Gelesen wurden die Fälle, in denen der Skill-Arm denselben Fehler
machte, obwohl eine Regel passte. Ergebnis: Reviews benutzten die
für Schreibende formulierten Regeln nicht als Suchauftrag (Opus
las eng um die geänderten Zeilen, Sol las die richtigen Zeilen
und verband sie nicht); Maße wurden als „nicht geprüft"
zurückgestellt, obwohl der Quelltext sie bestimmt; für
Grundlinie, Icon-Größe und Leerraum in einer größeren Klickfläche
fehlte die entscheidende Aussage; der Vorbildtest endete bei
irgendeinem Vorkommen eines Wertes. Zwei Umsetzungsfälle (i03,
i10) sind unfair, weil die Wahrheit von späteren Entscheidungen
abhängt; teilweise gilt das für i08, i09, r19, r21 und r22. Ein
Teil der Fehler entstand, bevor ein UI-Skill aktiv war: Ein Fall
zeigt, was der Skill abfangen muss, nicht, dass eine Regel
versagt hat.

Ergänzt wurden fünf Aussagen (Icon-Größe nach dem Text des
Labels; Grundlinie; Leerraum in einer Box zählt als Abstand;
Vorbild auf einem Element derselben Rolle; Maße aus dem
Quelltext berechnen). Runde 2 wiederholte nur die 74 Läufe mit
Skill; alle gültig, alle mit geladenem UI-Skill. Zwei Bewerter
je Fall; bei zwei Werten weichen sie ab.

| Review, 22 Fälle (Treffer/teils/verfehlt) | mit Skill | ohne |
|---|---|---|
| Opus | 14/2/6 | 7–9/4–6/9 |
| Sol | 10/3/9 | 6/3/13 |

| Umsetzung, 10 Fälle | Fehler vermieden (ja/teils/nein) | unverlangte Zusätze | Abweichungen bei Abstand und Größe |
|---|---|---|---|
| Opus mit Skill | 3–4/4–5/2 | 1–2 | 3 |
| Opus ohne | 1–2/5–6/3 | 5–6 | 6–7 |
| Sol mit Skill | 2/4/4 | 3–6 | 3 |
| Sol ohne | 1/4/5 | 4–6 | 5–7 |

Kontrollen: Befunde mit Skill 27–31 (Opus) und 25–28 (Sol), ohne
je 22. Die zusätzlichen Befunde sind überwiegend in der
Wahrheitsdatei als berechtigt gelistet oder konkrete Mängel der
Änderung. Sol fordert im Review mit Skill etwa doppelt so viel
Unverlangtes wie ohne (1,1 gegen 0,5 je Review); die Quelle sind
die Aufzählungen zu Zuständen, Ansagen und Fallbacks in den
Referenzen. Fünf Fälle verfehlen beide Modelle mit Skill weiter
(r03, r05, r18, r22, r27); bei r05 und r22 hing die Wahrheit an
späteren Entscheidungen, r27 deckt keine Regel ab. Sol wendet die
Vorbildregel nicht an. Sechs Referenzen hat kein Lauf geöffnet;
der Test konnte sie nicht auslösen, weil Rendern verboten war.

Grenzen: ein Lauf je Zelle; die neuen Aussagen stammen aus der
Analyse derselben Fälle, die Runde 2 misst; die Pakete enthielten
auch Astras Änderungen an den gemeinsamen Regeln. Belege:
`RESULTS-DATA-r2.json`, `grading-r2`.

### Eine Formulierung je Regel und dritte Runde (Suite `7950535`, Shared `a3c8cab`)

Nutzerentscheidung (ADR-0240): Jede Regel steht einmal und gilt
für Schreiben und Review gleich; Prüfabschnitte formulieren keine
eigenen Regeln; Prüfer laden die Skills selbst. Drei Prüfläufe
über alle neun Skills und die gemeinsamen Quellen fanden rund 50
klare Doppelungen. Entfernt wurden unter anderem die Fragen am
Ende der Code-Regeln (sie wiederholten die Regeln 1 bis 6 und
ließen Teile aus), die Aufzählung im Schlussabschnitt des
UI-Skills, eingebettete Code-Regeln und eigene Reviewregeln in
den Hilfsskripten von Workflow und Ask sowie Wiederholungen
zwischen SKILL.md, Referenzen und gemeinsamen Quellen. Danach
wurde der Aufbau geordnet (Überschriften, Reihenfolge,
Ladebedingungen). Je Schritt lasen zwei unabhängige Prüfer
(Claude Opus 5.5, xhigh) das Ergebnis gegen; ihre Befunde sind
eingearbeitet, darunter zwei verlorene Regeln, eine Regel nur
für Reviewer, eine verengte Review-Anleitung und eine beim
Vereinen entstandene widersprüchliche Regel. Die Gesamtprüfung
besteht.

Runde 3 wiederholte die 54 Review-Läufe mit Skill; alle gültig,
alle mit geladenem UI-Skill. Zwei Bewerter je Fall.

| Review, 22 Fälle (Treffer/teils/verfehlt) | Runde 2 mit Skill | Runde 3 mit Skill | ohne |
|---|---|---|---|
| Opus | 14/2/6 | 14/3–4/4–5 | 8–9/4–5/9 |
| Sol | 10/3/9 | 10/0–1/11–12 | 7–8/1–2/13 |

Unverlangtes je Review in Runde 3: Opus 0,2–0,3, Sol 1,1–1,2.
Befunde in den Kontrollen: Opus 26, Sol 34 (ohne Skill 19–20 und
22). Zeit je Review: Opus 136 s, Sol 205 s.

Befund: Das Kürzen des Schlussabschnitts auf einen Verweis hat
bei Opus keinen Treffer gekostet. Sol hält die Treffer; zwei bis
drei Fälle fallen von teilweise auf verfehlt, was bei einem Lauf
je Fall in der Streuung liegt und einen kleinen Verlust nicht
ausschließt. Der Halbsatz, der die Bedarfsregel auf Reviews
ausdehnt, zeigt bei Sol keine Wirkung auf das geforderte
Unverlangte. Die Bewerter weichen in 47 von 432 Feldern ab, bei
den Urteilen in vier Fällen um eine Stufe.

Nicht erprobt: die Aufträge von Workflow und Ask an echte Agenten
unter Codex. Bestätigt an einem echten Aufruf: Die Claude-CLI
liest mit den Einstellungen von Ask eine Datei außerhalb des
Arbeitsordners. Belege: `RESULTS-DATA-r3.json`, `grading-r3`.

### Code-Review nach dem Entfernen der Doppelungen (Suite `7950535`, Shared `a3c8cab`)

Die 23 Review-Fälle des Code-Skills liefen nach dem Entfernen der
Doppelungen erneut, mit und ohne Skill; 92 Läufe gültig, zwei
Bewerter je Fall (22 von 296 Feldern abweichend).

| Review, 18 Fehlerfälle (Treffer/teils/verfehlt) | Runde 2 mit Skill | Runde 3 mit Skill | ohne |
|---|---|---|---|
| Opus | 16/1/1 | 15/0/3 | 11/3/4 |
| Sol | 12/4/2 | 11–12/3–4/3 | 10/2/6 |

Befund: Das Streichen der Fragen am Ende der Code-Regeln hat die
Treffer gehalten. Verloren ging bei beiden Modellen ein
Kapselungsfall. Ein zusätzlicher Satz, der Reviewer zuerst die
Stellen je Regel benennen ließ (Suite `55c16e7`, Shared `7dcd381`),
wurde an den drei Kapselungsfällen und zwei Kontrollen
nachgemessen: Der verlorene Fall blieb bei Opus verfehlt und bei
Sol teilweise. Der Satz zeigte keine Wirkung und ist wieder
entfernt (Suite `e4e1242`, Shared `dd84f0e`). Der Verlust ist
hingenommen; eine Regel für diesen einen Fall wäre eine
Anpassung an die Messaufgabe.

Grenze: Während Runde 3 hat sich die Codex-App zweimal selbst
aktualisiert, und ein Systemabsturz hat Läufe abgebrochen, die
neu gestartet wurden. Die Sol-Läufe der Runden stammen daher
nicht alle von derselben App-Fassung.

### Barrierefreiheit als Projektentscheidung, Übersetzbarkeit, neuer Aufbau (Suite `06dad25`)

Entscheidungen des Eigentümers vom 2026-11-19 und 2026-11-20:

- Eine Basis der Barrierefreiheit gilt immer (Bedienung mit der
  Tastatur und sichtbarer Fokus, das richtige Element, Beschriftung
  und zugänglicher Name). Darüber hinaus gibt es eine Stufe: WCAG AA
  vollständig, in Fassung 2.1, sofern die Projektregeln nicht 2.2
  nennen, getrennt nach Frontend und Backend. Der Skill fragt
  einmal und verankert die Antwort als eine Zeile in den
  Projektregeln; nur dann wird die Referenz geladen.
- In WordPress-Plugins und -Themes ist jeder neue oder geänderte
  Text übersetzbar; Übersetzungsdateien werden nicht erzeugt.
- Tests laufen ohne die Regeldateien der Originalprojekte, weil
  sonst nicht messbar ist, was aus dem Skill kommt.
- Der UI-Skill wurde nach einer unabhängigen Strukturprüfung (Opus
  5.5, xhigh) in zwölf Schritten neu geordnet; zwei Referenzen sind
  zusammengeführt, eine ungenutzte ist gestrichen.

Nachprüfung der 40 Umsetzungen aus Runde 2 auf diese beiden
Punkte: 0 unübersetzte von 147 Texten und 0 Mängel an der Basis
in allen Armen. Einschränkung: In Runde 2 lagen die Regeldateien
der Projekte in beiden Armen im Arbeitsordner; sie verlangen
Übersetzbarkeit selbst. Alle UI-Runden vor der folgenden sind mit
Projektregeln gemessen.

### Runde ohne Projektregeln (Suite `55c16e7`, Shared `7dcd381`)

Alle 37 Fälle liefen neu, mit und ohne Skill, in Arbeitsordnern
ohne `AGENTS.md` und `CLAUDE.md`. Ein dritter Arm wiederholte vier
Umsetzungsfälle mit Skill und einer Regeldatei, deren einzige
Zeile WCAG 2.1 AA für Frontend und Backend verlangt. 156 Läufe,
alle gültig, in jedem Skill-Lauf war der UI-Skill geladen. Zwei
Bewerter je Fall; 85 von 864 Feldern weichen ab, fast nur
Zählwerte, bei den Urteilen sechs Fälle um eine Stufe.

| Review, 22 Fehlerfälle (Treffer/teils/verfehlt) | mit Skill | ohne |
|---|---|---|
| Opus | 14/2/6 | 5/6–7/10–11 |
| Sol | 9/1/12 | 7/1/14 |

| Review, weitere Werte | Opus mit | Opus ohne | Sol mit | Sol ohne |
|---|---|---|---|---|
| Unverlangtes je Review | 0,2–0,4 | 0,4–0,6 | 0,8–1,1 | 0,2–0,4 |
| Befunde in 5 Kontrollen | 22–23 | 16–17 | 31–32 | 24 |
| Sekunden je Review | 151 | 105 | 196 | 166 |

| Umsetzung, 10 Fälle | Opus mit | Opus ohne | Sol mit | Sol ohne |
|---|---|---|---|---|
| Fehler vermieden (ja/teils/nein) | 3–5/3–5/2 | 3–4/4–5/2 | 1–2/5–6/3 | 2/4/4 |
| Unverlangte Zusätze | 4–5 | 6–7 | 6–8 | 4–6 |
| Abweichende Abstände | 2 | 2–4 | 2–3 | 6–7 |
| Unübersetzte Texte | 0 | 0 | 0 | 0 |
| Mängel an der Basis | 0 | 0 | 0 | 0 |
| Über die Basis hinaus gebaut | 4 | 4 | 5–6 | 4–5 |
| Sekunden je Lauf | 426 | 413 | 383 | 297 |

| Vier Fälle mit der WCAG-Zeile | Opus | Sol |
|---|---|---|
| Über die Basis hinaus gebaut: ohne Skill / Skill / Skill mit Zeile | 4 / 4 / 7 | 4–5 / 5–6 / 9 |
| Referenz zur Barrierefreiheit gelesen (mit Zeile) | 3 von 4 | 4 von 4 |

Befunde:

- Die Wirkung im Review besteht ohne Projektregeln fort, bei Opus
  deutlich (14 gegen 5 Treffer), bei Sol klein (9 gegen 7).
- Sol fordert im Review mit Skill mehr Unverlangtes als ohne; die
  Bedarfsregel wirkt dort weiterhin nicht. Opus fordert mit Skill
  weniger.
- In der Umsetzung zeigt der Skill beim Vermeiden des
  ursprünglichen Fehlers keinen messbaren Unterschied. Abweichende
  Abstände sind mit Skill seltener, am deutlichsten bei Sol.
- Übersetzbarkeit und Basis der Barrierefreiheit halten beide
  Modelle in diesen Projekten auch ohne Skill und ohne
  Projektregeln ein. Eine Wirkung der beiden Regeln ist hier weder
  belegt noch widerlegt; sie bleiben als Vorgabe des Eigentümers.
  Die Referenz zur Übersetzbarkeit lud Sol in 33 von 37
  Skill-Läufen, Opus in 9.
- Die Projektzeile wirkt: Mit ihr wird die Referenz geladen und
  mehr über die Basis hinaus gebaut. Ohne die Zeile wird die
  Referenz in keinem Lauf geladen.
- Ohne die Zeile baut kein Modell mit Skill weniger über die Basis
  hinaus als ohne. Der Skill verringert das hier nicht.

Grenzen: ein Lauf je Zelle. Die Claude-CLI lädt `AGENTS.md` nicht
von selbst; ein Opus-Lauf mit der Zeile lud die Referenz nicht.
Belege: `RESULTS-DATA-nr.json`, `grading-nr`, `JUDGING-nr.md`.

Berichtigung vom 2026-11-20: Diese Runde ist durch
Projektdokumentation verfälscht. In den Arbeitsordnern lag die
Dokumentation der Projekte, und 87 von 156 Läufen lasen daraus,
mit Skill weit häufiger als ohne (Sol-Review: 25 von 27 Läufen mit
Skill, 13 von 27 ohne). Die Werte oben sind deshalb nicht
belastbar, auch nicht der Abstand von 14 zu 5 Treffern bei Opus.
Maßgeblich ist die folgende Runde.

### Runde ohne Projektdokumentation (Suite `55c16e7`, Shared `7dcd381`)

Vorgabe des Eigentümers vom 2026-11-20: Skill-Tests laufen ohne
jede Projektdokumentation. Die Arbeitsordner enthielten weder
`AGENTS.md` und `CLAUDE.md` noch die Ordner `docs` und `research`
noch sonst eine Datei mit `.md`, `.mdx` oder `.rst`. Alle 37 Fälle
liefen neu, 156 Läufe, alle gültig, der UI-Skill in allen 82
Skill-Läufen geladen. Kein Lauf las Projektdokumentation: Die
Prüfung meldete zehn Läufe, alle Fehlalarme (sieben Mal bestand
eine Zeile einer entfernten Datei nur aus einem Pfad, der im Lauf
in einer Dateiliste vorkam; drei Mal legte der Lauf eine Datei
gleichen Namens selbst an). Zwei Bewerter je Fall; 86 von 864
Feldern weichen ab.

| Review, 22 Fehlerfälle (Treffer/teils/verfehlt) | mit Skill | ohne |
|---|---|---|
| Opus | 14/2–3/5–6 | 11–12/2–3/8 |
| Sol | 10–11/0–1/11 | 7/1/14 |

| Review, weitere Werte | Opus mit | Opus ohne | Sol mit | Sol ohne |
|---|---|---|---|---|
| Unverlangte Forderungen in 27 Reviews | 6–9 | 14–16 | 26–29 | 12–15 |
| Befunde in 5 Kontrollen | 24–26 | 20–21 | 32–33 | 25 |
| Sekunden je Review | 145 | 109 | 203 | 157 |

| Umsetzung, 10 Fälle | Opus mit | Opus ohne | Sol mit | Sol ohne |
|---|---|---|---|---|
| Fehler vermieden (ja/teils/nein) | 3–4/3–4/3 | 3/6/1 | 2/5/3 | 3/4/3 |
| Unverlangte Zusätze | 2–4 | 6 | 6–7 | 8 |
| Abweichende Abstände | 3–4 | 6–7 | 1–2 | 6–8 |
| Unübersetzte Texte | 0 | 0–1 | 0 | 0 |
| Mängel an der Basis | 0 | 0 | 0 | 0 |
| Sekunden je Lauf | 404 | 348 | 400 | 333 |

| Vier Fälle mit der WCAG-Zeile | Opus | Sol |
|---|---|---|
| Über die Basis hinaus gebaut: ohne Skill / Skill / Skill mit Zeile | 5–7 / 3–4 / 8 | 5 / 4–5 / 9–10 |
| Referenz zur Barrierefreiheit gelesen (mit Zeile) | 3 von 4 | 4 von 4 |

Befunde:

- Im Review hebt der Skill die Treffer bei beiden Modellen um etwa
  drei Fälle.
- Sol fordert im Review mit Skill etwa doppelt so viel Unverlangtes
  wie ohne, auch ohne jede Dokumentation. Die Ursache liegt im
  Skill. Opus fordert mit Skill weniger.
- In der Umsetzung vermeidet kein Modell den ursprünglichen Fehler
  mit Skill häufiger. Abweichende Abstände und unverlangte Zusätze
  sind mit Skill seltener.
- Die Projektzeile zu WCAG AA wirkt wie zuvor; ohne sie wird die
  Referenz in keinem Lauf geladen.

Verblindung: Sols Berichte enthielten Dateipfade mit dem Namen des
Laufordners, also Modell und Arm, in allen Runden bis hierher. Ein
dritter Bewerter auf bereinigten Review-Dateien kam auf dieselben
Werte (Treffer Opus 14 gegen 10, Sol 10 gegen 7; Unverlangtes Opus
6 gegen 15, Sol 24 gegen 10). `build_grading.py` entfernt die Pfade
seither.

Belege: `RESULTS-DATA-nd.json`, `grading-nd`, `JUDGING-nd.md`.

### Ursache der unverlangten Forderungen und Änderung (Suite `c8f41fa`)

Zwei unabhängige Analysen (eigene, Opus 5.5 xhigh) und eine
Gegenprüfung der Änderung (Opus 5.5 xhigh) ergaben: Der Skill
selbst erlaubte die Forderungen. Die Bedarfsregel ließ „eine
Zusage aus einer gewählten Referenz“ als Bedarf gelten; die
Referenz zu Interaktionen formulierte mehrere Punkte als Pflicht,
Texte, Zustände, Bestätigungen und Bedienelemente zu ergänzen, und
verwies zugleich im Kreis auf die Bedarfsregel; ein Satz („Add an
error summary when it helps“) widersprach ihr. Sol lädt im Review
etwa 15 Skill-Dateien und prüft jeden Punkt ab, Opus etwa 4.

Geändert:

- Die Punkte der Referenz zu Interaktionen nennen, was nicht
  fehlschlagen darf, statt Ergänzungen zu verlangen; der
  widersprüchliche Satz und zwei doppelte Punkte sind gestrichen.
- Die Bedarfsregel nennt Projektregeln ausdrücklich (Entscheidung
  des Eigentümers: dauerhafte Projektregeln zählen im Review als
  Bedarf) und lässt Regeln des Skills nur für Elemente gelten, die
  die Änderung hinzufügt oder ändert.
- „Check and report“ sagt in einem Satz, dass eine Forderung nach
  etwas, das die Änderung nicht enthält, einen Bedarf braucht.
- Die Gruppierung von Eingaben steht nur noch bei WCAG AA.

Nachmessung: die 27 Review-Fälle mit dem geänderten Skill, beide
Modelle, ohne Dokumentation, 54 Läufe, alle gültig; die Läufe ohne
Skill stammen aus der Runde davor und wurden neu mitbewertet. Zwei
Bewerter, 59 von 432 Feldern abweichend.

| Review, 22 Fehlerfälle (Treffer/teils/verfehlt) | mit Skill | ohne |
|---|---|---|
| Opus | 12/3/7 | 10/4/8 |
| Sol | 9/1–2/11–12 | 6–7/1–3/13–14 |

| Review, weitere Werte | Opus mit | Opus ohne | Sol mit | Sol ohne |
|---|---|---|---|---|
| Unverlangte Forderungen in 27 Reviews | 4–6 | 17 | 18 | 13 |
| Weitere bekannte Mängel gefunden | 40–42 | 22 | 21 | 10 |
| Befunde in 5 Kontrollen | 24–25 | 20 | 32 | 25 |

Befund: Sols unverlangte Forderungen mit Skill sinken von 26–29
auf 18 und liegen noch um 5 über dem Wert ohne Skill (vorher um
etwa 14). Der Treffervorteil bleibt bei beiden Modellen bei zwei
bis drei Fällen; mit Skill finden beide etwa doppelt so viele der
weiteren bekannten Mängel. Opus liegt mit 12 Treffern zwei unter
der Runde davor; bei einem Lauf je Zelle ist das nicht von
Streuung zu trennen.

Belege: `RESULTS-DATA-ne.json`, `grading-ne`, `JUDGING-ne.md`.

### Warum der Skill in der Umsetzung den ursprünglichen Fehler nicht verhindert

Zwei unabhängige Analysen der Läufe (Opus 5.5 xhigh, Fable 5.2
high) an sieben Umsetzungsfällen kommen zum selben Ergebnis:

- `SKILL.md` war in allen 28 Umsetzungsläufen mit Skill vor der
  ersten Änderung geladen. Zu spätes Lesen scheidet aus.
- In sechs von sieben Fällen ist die erwartete Lösung aus Auftrag
  und Arbeitsordner nicht oder nur teilweise herleitbar: Sie ist
  die spätere Korrektur des Eigentümers nach Ansicht des
  Ergebnisses, steht in entfernter Dokumentation, oder der
  Auftragstext ist der Planeintrag des damaligen Fehlversuchs.
- Beim Umsetzen hat der Auftrag Vorrang; die Modelle folgen seinem
  Wortlaut und melden eine erkannte Folge im Bericht. Im Review ist
  dieselbe Folge ein Befund.
- Regeln, die an einen Schreibvorgang gebunden sind (Vorbild für
  feste Werte, Icon-Größe am Text, Höhe der Nachbarn), wurden
  sichtbar angewandt. Die dreistufige Bewertung zeigt das nicht.
- Zwei Lücken im Text: Der Skill sagt nicht, wohin ein neues
  Bedienelement gehört; und die Regel zu Zuständen fragt nach
  Datenwerten, nicht danach, wie ein Wert entstand und was eine
  Vorgabe des Nutzers in nicht genannten Zuständen ändert.

Entscheidung des Eigentümers vom 2026-11-20: Die beiden Lücken
sind geschlossen (Suite `eff3235`): Ein neues Bedienelement entsteht
in der Schicht, die die eigenen Komponenten dieser Art hält; eine
Vorgabe des Nutzers gilt für ihren Fall, und der Bericht nennt und
erfragt, was sie in nicht genannten Zuständen ändert; die Regel zu
Zuständen fragt auch, wie ein Wert entstand. Wegen der Tokenkosten
wird die Wirkung dieser drei Sätze nicht eigens gemessen; die
Gesamtprüfung besteht. Die Umsetzungsmessung bleibt, wie sie ist,
mit den oben genannten Grenzen.

### Gezielte Tests nach den Änderungen (Suite `1a35bfd`)

Vorgabe des Eigentümers vom 2026-11-20: nur noch ganz gezielte
Tests. Drei kleine Tests, zusammen 18 Läufe, ohne Bewerter-Agenten,
von Hand gegengelesen; je ein Lauf, also Hinweise, keine Messwerte.

Verständnis der UI-Regeln: 15 beschriebene Situationen in drei
Blöcken, je Block ein Lauf mit Sol und Opus. Alle 30 Antworten
treffen die gemeinte Lesart, auch bei den am selben Tag geänderten
Regeln (Bedarf im Review, Basis gegen WCAG AA, Ort einer neuen
Komponente, Geltung einer Nutzer-Vorgabe, Zustände nach Entstehung,
Punkte zu Interaktionen). Kein Text geändert. Material:
`ui-comprehension/scenarios.md`.

Umsetzungsfälle i08 und i10 mit dem geänderten Skill, je ein Lauf
je Modell, verglichen mit den Läufen der Runde ohne Dokumentation:

- Ort einer neuen Komponente (i08): Beide Modelle bauten den
  Schalter nur im Plugin; Sol umging dabei die Feldausgabe der
  gemeinsamen Schicht. Kein Bericht erwähnt die Schicht.
  Berichtigung vom 2026-11-21: In der Runde davor hatte Opus die
  gemeinsame Schicht erweitert, mit der Regel nicht mehr. Der
  damalige Zusatz „kein eingebundenes Fremdpaket“ hat also eher
  geschadet als nichts bewirkt; er ist gestrichen. Der Ordner weist
  sich im Quelltext selbst als internes Framework aus.
- Lage des Schalters (i08): bei beiden neben dem Feld; Opus hatte
  ihn zuvor in der Überschriftenzeile.
- Frage zu nicht genannten Zuständen (i10): Opus stellt die Folge
  jetzt als direkte Frage, vorher als offenen Punkt. Sol nennt sie
  weiterhin nicht.
- Die Aufteilung der Zustände selbst ist bei beiden unverändert.

Stand: Die Regel zum Ort einer neuen Komponente ist verstanden,
aber ohne belegte Wirkung; sie bleibt vorerst, bis der Eigentümer
entscheidet.

Handoff, erstmals mit Modellen: vier Übergaben (halb fertig mit
rotem Test; fertig mit offener Entscheidung des Nutzers; im
Planprofil; Vorgabe, verworfener Ansatz und ungeprüfte Annahme) je
einmal mit Sol und Opus. Alle acht Übergaben folgen der Vorlage,
und ihre Angaben stimmen mit dem Arbeitsordner überein. Opus stellt
einen Arbeitsbericht voran. Kein Text am Handoff-Skill geändert.

Dabei gefunden und behoben (Suite `2037f22`): Opus schrieb im
Planprofil einen Nachweis mit 344 Zeichen; das Profil wurde ungültig
übergeben. Die Grenze von 200 Zeichen stand nur im Prüfprogramm, und
eine reine Nachweis-Änderung verlangt keine Prüfung. Sie steht jetzt
im Abschnitt zum Nachweis. Nicht mit einem Lauf nachgeprüft.

### Fixplan, externe Prüfung und Kontrollläufe (Suite `8b66460`, Shared `cb9d724`)

Die Ergebnisse im Abschnitt davor gelten für Suite `1a35bfd`. Was
danach geändert wurde, steht hier; gemessen ist davon nur, was
unten als Lauf genannt ist.

Nebenbefunde der gezielten Tests:

- Zeilenenden: Opus stellte in Umsetzungsläufen ganze Dateien von
  LF auf CRLF um. Durchsicht aller vorhandenen Arbeitsordner mit
  Git-Verzeichnis (Byte-Vergleich): Opus in 25 von 62, Sol in 4 von
  62 Läufen, mit und ohne Skill. Ursachen: `git stash` und
  Zurückholen bei `core.autocrlf=true` und Neuschreiben per Skript
  ohne feste Zeilenenden. `git diff` verbirgt die Umstellung, und
  der gespeicherte Diff der Tests hatte sie bis dahin verschluckt.
  Die Testfälle liegen auf älteren Ständen der Projekte; beide
  Projekte führen heute eine `.gitattributes`, die den Weg über
  Git schließt.
- Projektprüfung: Sol ersetzte in i10 in vier von vier Läufen bis
  dahin eine bestehende Zusicherung der Vertragsprüfung durch eine,
  die zur eigenen Änderung passt, ohne das zu berichten.
- Sol lädt 7 bis 14 Skill-Dateien je Aufgabe, Opus 2 bis 7; Opus
  las in i10 nur `SKILL.md` und eine Referenz.

Fixplan (eigener Vorschlag und Gegenentwurf von Opus 5.5 xhigh),
danach Prüfung durch ein drittes Modell (Astra 6.2) und Beurteilung
jedes Befunds durch zwei Prüfer. Umgesetzt:

- Regeln zum Erhalt unveränderter Bytes und bestehender
  Projektprüfungen als ein gemeinsames Stück im Kern von Code und
  UI, weil die Code-Kriterien reine Textänderungen im UI-Skill
  nicht erreichen.
- UI-Referenzen: weitere Sätze gestrichen, die Ergänzungen
  vorschreiben (Grund einer deaktivierten Aktion, Zurück- und
  Abbrechen-Wege, „was zuerst kommen muss“, Seltenes hinter einem
  Aufklappelement); Bestätigung nur vor nicht umkehrbaren
  Wirkungen; Feldfehler am Feld; keine doppelte Wirkung statt kein
  zweiter Start; Label-Zeile des WordPress-Adapters ohne versteckte
  Felder und Schaltflächen.
- UI: Zusatz zum Fremdpaket und Satz zu Zuständen nach Entstehung
  gestrichen; die Frage zu nicht genannten Zuständen steht bei den
  Inhalten des Berichts.
- Handoff: erst der Arbeitsbericht, dann der eingerahmte Text; die
  Größenprüfung gilt für die ganze Antwort.
- Plan: Nachweis als einfacher Text höchstens 200 Zeichen, in
  einer Klammerliste 200 je Eintrag.
- Entscheidung des Eigentümers: Die Basis der Barrierefreiheit
  verlangt die Gruppenfrage, wo ein Label seine Bedeutung nur aus
  ihr bezieht.

Nicht übernommen aus der externen Prüfung: wieder eingeführte
Pflichten (Fortschrittsanzeige, Format-Hinweis vor der Eingabe,
weit gefasste Bestätigung), eine neue Fassung der Bedarfsregel,
das Streichen der Rückfrage im Bericht, Byte-Vergleich als
Prüfschritt.

Kontrollläufe, je ein Lauf:

| Lauf | Stand | Ergebnis |
|---|---|---|
| Opus, Übergabe mit Arbeitsauftrag | `2dfc363` | keine Zeilenenden umgestellt (zuvor alle vier Dateien) |
| Sol, dieselbe Übergabe | `2dfc363` | Arbeitsbericht vor dem eingerahmten Text (zuvor keiner) |
| Sol, i10 | `2dfc363` | Projektprüfung wieder umgeschrieben und nicht berichtet; keine Frage |
| Opus, i10 | `6c8ec65` | wieder `git stash`, drei Dateien umgestellt, eine Prüfung danach rot und als bestanden berichtet; Frage gestellt |
| Sol, i10 | `6c8ec65` | Projektprüfung wieder umgeschrieben und nicht berichtet; keine Frage |
| Opus, i10 | `8b66460` | kein Stash, Zeilenenden zeilengenau wiederhergestellt, alle Prüfungen wie im Ausgangsstand; Frage gestellt |
| Sol, i10 | `8b66460` | Projektprüfung unverändert, früherer Stand über `git show` geprüft, Zeilenenden erhalten; keine Frage |

Befund: Die erste Fassung der Regel nannte nur die Ursache und
verließ sich auf den Bericht; sie griff in i10 bei keinem Modell.
Die Fassung, die die Handlung nennt (früheren Stand über eine
Kopie ansehen, nicht stashen; eine bestehende Prüfung besteht
weiter), griff bei beiden. Die Frage zu nicht genannten Zuständen
stellt Opus in drei von drei Läufen, Sol in keinem von vier.

Grenzen: je ein Lauf, alle am selben Fall, an dem die Regel
geschärft wurde; das zeigt, dass sie dort greift, nicht, dass sie
allgemein greift. Die gestrichenen und umformulierten Sätze der
UI-Referenzen, die Basis-Ergänzung und die Plan- und
Handoff-Sätze nach `2dfc363` sind nicht mit Läufen geprüft. Der
Verständnistest zeigt, dass Regeln richtig gelesen werden, wenn
die Situation benannt ist, nicht, dass ein Modell sie beim Bauen
erkennt; drei seiner Situationen umschreiben die geprüften Sätze.
Die Review-Nachmessung mit 18 gegen 13 unverlangten Forderungen
gilt für `c8f41fa`.

Prüfwerkzeug: Die Doku-Prüfung zählt reine Pfadzeilen und vom Lauf
angelegte Dateien nicht mehr; in der Runde ohne Dokumentation
bleiben zwei Fehlalarme gleicher Art (Befehl mit Pfad). Der
gespeicherte Diff wird aus Bytes geschrieben; je Datei wird
festgehalten, ob sich Zeilenenden geändert haben.

### Gegenprüfung vor der Veröffentlichung (Suite `28ceef2`, Shared `0cc30c5`)

Opus 5.5 xhigh las alle Änderungen an Anweisungen seit `2dfc363`
gegen. Urteil: nach Änderungen veröffentlichen. Eingearbeitet:

- Die Regel zum Erhalt von Dateien widersprach den Code-Kriterien
  („ändere, was das vollständige Ergebnis braucht“). Sie gilt jetzt
  für alles außerhalb dessen, was das vollständige Ergebnis braucht.
- Das Entfernen eines Tests, das eine Code-Regel in einem Fall
  verlangt, ist abgedeckt.
- Für den früheren Stand ist neben `git show` die Projektkopie mit
  zurückgenommener Änderung genannt. Nachgeprüft: Windows
  PowerShell 5.1 kodiert umgeleitete Ausgaben um; das steht bei
  den Shell-Regeln.
- Gruppenfrage: Sie ist der Name der Gruppe; die Adapterzeile nutzt
  dieselbe Bedingung.
- Handoff: „unverändert“ kollidierte mit dem Kürzen nach der
  Größenprüfung.
- Changelog: drei Aussagen überzeichneten (Treffervorteil, Regel
  zum Komponentenort als ungetestet, Ursachenanteil bei den
  Zeilenenden) und sind berichtigt.

Die Gegenprüfung erinnerte an den Befund vom 2026-11-17: Ein
Absatz zu Zeilenenden im Code-Skill ließ Sol häufiger umstellen
(3 von 6 Läufen gegen 0 von 4) und wurde gestrichen. Deshalb sechs
Kontrollläufe mit geladenem Code-Skill auf dem Übungsprojekt (LF,
keine `.gitattributes`, `core.autocrlf=true`): Sol auf allen vier
Übergabe-Aufgaben, Opus auf den beiden, in denen es zuvor
umgestellt hatte.

| | Ergebnis in 6 von 6 Läufen |
|---|---|
| Zeilenenden geändert | nein |
| `git stash`, `reset`, `checkout`, `restore` | nein |
| Arbeitsbericht vor der Übergabe (2 Läufe) | ja, bei beiden Modellen |
| Planprofil am Ende gültig (2 Läufe) | ja; Opus schrieb den Nachweis als Liste, Sol als Text mit 191 Zeichen |

Opus schrieb Dateien in diesen Läufen nur über das
Bearbeitungswerkzeug, Sol nur über Patches. Ein Sol-Lauf schrieb
einen bestehenden Test strenger um und nannte das im Bericht
nicht; die Berichtspflicht für geänderte Prüfungen greift bei Sol
also nicht verlässlich.

Grenzen: je ein Lauf. Die Größenprüfung der ganzen Handoff-Antwort,
die Formulierung zur Gruppenfrage und die PowerShell-Angabe sind
nicht mit Läufen geprüft.

## W-007: Python als Voraussetzung, Plan schlank

### Änderung (Suite `1c6ddea` und `156b4ca`, Shared `b7d099c`)

Nach ADR-0241 sind alle Ersatzwege ohne Python aus der Suite
entfernt. Der Plan-Skill ist von rund 13.350 auf 5.670 Wörter
gekürzt: fünf Dateien statt zehn, keine Regeln mehr für
abgeschaffte Formate, seltene Abläufe in einer Referenz, die nur
auf Wunsch geladen wird. An den Skripten sind nur Texte geändert;
Feldnamen und Aufbau der Ausgabe sind gleich. Ein unabhängiger
Prüfer (Opus 5.5, xhigh) las Aufbau und Ergebnis gegen; seine
Befunde sind eingearbeitet. Die Gesamtprüfung besteht.

### Alltagsaufgaben, alte gegen neue Fassung (`e4e1242` gegen `156b4ca`)

Zehn Aufgaben auf einem erfundenen kleinen Projekt ohne
Projektregeln: Plan anlegen, Arbeitspaket ergänzen, Schritt
abschließen, nach Unterbrechung fortsetzen, Stand ohne
Codeänderung nachführen, Entscheidung festhalten, offene Wahl
erfragen, beschädigten Plan prüfen und richten, Paket abschließen,
Stand nur berichten. Jede Aufgabe einmal je Modell und Fassung auf
medium; 40 Läufe, alle gültig, Plan-Skill in allen geladen. Zwei
blinde Bewerter; 10 von 200 Feldern weichen ab.

| | Opus neu | Opus alt | Sol neu | Sol alt |
|---|---|---|---|---|
| Ergebnis (erledigt/teils) | 9/1 | 8/2 | 10/0 | 7/3 |
| Einträge richtig (ja/teils/nein) | 9/0–1/0–1 | 8/1–2/0–1 | 9–10/0–1/0 | 5–7/2–5/0–1 |
| Erfundenes | 0–1 | 3–4 | 0–1 | 1–2 |
| Ungefragte Änderungen | 0 | 2 | 2 | 1 |
| Prüfprogramm gültig | 9 von 9 | 9 von 9 | 9 von 9 | 9 von 9 |
| Gelesene Wörter des Skills | 2.905 | 4.916 | 3.959 | 6.684 |
| Sekunden je Lauf | 51 | 44 | 104 | 99 |
| Tokens je Lauf (Tsd.) | 305 | 273 | 484 | 435 |

Kein Lauf hat Tests gebrochen, Bestehendes beschädigt oder beim
reinen Bericht eine Datei geändert. Bei der beschädigten
Entscheidung blieb in allen Läufen nur der Fehler stehen, für den
der Nutzer gefragt werden muss.

Befund: Die gekürzte Fassung erledigt die Alltagsaufgaben mit beiden
Modellen nicht schlechter als die vorige, bei Sol besser (das
Arbeitspaket mit Abhängigkeit, die Rückfrage zum fehlenden Datum).
Gegenläufig ist die Zeile „Ungefragte Änderungen“: bei Sol 2 statt 1,
bei Opus 0 statt 2.
Die Bedingung aus ADR-0241 ist erfüllt. Zeit und Tokens sind trotz
weniger gelesenem Text nicht gesunken.

Grenzen: ein Lauf je Zelle. Bei der Aufgabe „Entscheidung
festhalten“ verlangte die Erwartung eine eigene Entscheidung,
obwohl die Wahl nur ein Arbeitspaket betrifft; der Skill legt
solche Wahlen im Arbeitspaket ab. Drei der vier Läufe taten das
und wurden als „teils“ gewertet (Opus neu und alt, Sol alt). Das
ist eine Schwäche der Erwartung, nicht dieser Läufe; ohne sie
stünde Opus bei 10/0 und 9/1. Belege: `plan-everyday/RESULTS-DATA.json`,
`plan-everyday/grading`, `plan-everyday/JUDGING.md`.

## W-009: Installierte Codex-Skills über die CLI

Anlass war ein erster Codex-Lauf des Nutzers, dessen Prüfauftrag den
Subagenten das Lesen außerhalb des Arbeitsordners verbot: Keiner las einen
Skill. Die Wiederholung lief am 2026-11-21 über die Codex-CLI, mit dem
Hauptagenten als Prüfer.

Aufbau: Jede Aufgabe ist eine frische `codex exec`-Sitzung im echten
Codex-Home mit dem dort aktiven Skill-Satz unter `~/.agents/skills`.
Modell gpt-6.2-sol, Aufwand medium; der Workflow-Lauf high, weil das
mitgelieferte Hauptpaar so lautet. Sandbox `workspace-write`, Codex-Memories
und Plugins aus. Der Auftrag besteht aus dem Aufgabentext und einem Satz zum
Ordner; ein Skill wird nicht genannt. Bytes, Git-Spuren, Tests, Planprofil
und Skill-Zugriffe sind unabhängig aus Arbeitsordner und Sitzungsereignissen
erhoben. Skript, Vorlagen und die Auswertungen je Lauf liegen im Arbeitsbereich
unter `state/2026-11-14-skill-evaluation/codex-check/`.

### Erste Runde, installierter Stand 6cebd34

| Lauf | Gelesene Skills | Ergebnis |
| --- | --- | --- |
| A1, Option `--min` | Code | 13 Tests bestanden. Ein bestehender Test wurde verschärft; der Bericht nennt das nicht. |
| A2, Semikolon und Übergabe | Code, Handoff | 12 Tests bestanden. Bericht vor der Übergabe, vier Backticks, vier Abschnitte, ein Schritt; Angaben stimmen. Der geänderte Test ist nur indirekt genannt. |
| A3, laufender Plan-Schritt | Plan, Code | 16 Tests bestanden, Profil gültig, Nachweis in einer Zeile, Schritt 2 erledigt, Schritt 3 offen. |
| A4, UI-Review | UI, Code | Vier gesetzte Mängel gefunden, kein ausgeschlossener Punkt gefordert. Die Angabe zur Barrierefreiheitsstufe fehlt; ein Befund ist eine Vermutung. |
| A5, Aktion „Duplizieren“ | UI, Code | Nativer `button` mit vorhandener Klasse, keine Meldung, keine Abfrage. Der Filter wird umgeschaltet und genannt, aber nicht nachgefragt; die Stufenangabe fehlt. |
| Ask, Review von A1 | Ask; Berater: Code | gpt-6.2-astra/high angenommen. Berater ohne geerbten Verlauf, lädt den Code-Skill selbst, ändert nichts. |
| Workflow, W-002 abschließen | Workflow, Plan, Code | Sechs frische Reviewer auf gpt-6.2-sol/xhigh. Das Abschlussreview fand einen Fehler in Schritt 1; Korrektur, frische Review, wiederholter Abschluss. 17 Tests, Profil gültig, W-003 unberührt. |

In keinem Lauf änderte sich ein Zeilenende, und kein Lauf versuchte Stash,
Reset, Checkout oder Restore. Die Sandbox hält `.git` schreibgeschützt; ein
Versuch wäre im Befehlsverlauf sichtbar gewesen. Für den Workflow-Lauf war
`.git` freigegeben.

Der unabhängige Reviewer, den Code nach einer Verhaltensänderung verlangt,
startete in vier Läufen; in zwei davon erbte er den Verlauf des Autors, weil
`spawn_agent` ohne `fork_turns` den Verlauf mitgibt.

### Hardlinks in der Windows-Sandbox

Die Sandbox verweigert `os.link` im Projektordner und in einem Ordner, den
`tempfile.mkdtemp` anlegt (WinError 5). Im Temp-Verzeichnis der Sitzung
selbst gelingt der Hardlink, dieses Verzeichnis kann ein gestarteter Agent
aber nicht lesen. Folgen in den Läufen: Der erste Workflow-Reviewer meldete
`blocked`, weil er seine Auftragsdatei nicht erreichte. Die Ablage im
Projekt scheiterte am Hardlink, worauf der Hauptfaden die Datei von Hand
kopierte. Ask konnte eine Frage über 8 KiB nicht als Datei übergeben und
kürzte sie. `os.rename` gelingt an allen drei Orten und verweigert unter
Windows ein vorhandenes Ziel.

Ein erster Workflow-Lauf hielt beim Reviewer-Start an, weil der Prüfauftrag
„arbeite nur dort“ sagte und die Sitzung deshalb nur Pfade im Projekt
versuchte. Der Hauptfaden ließ den Schritt offen und meldete die Ursache.
Das war ein Fehler des Prüfauftrags; der zweite Lauf ohne diesen Satz lief
durch.

### Korrekturen und Kontrollläufe

| Korrektur | Kontrolle |
| --- | --- |
| Größenprüfer aller Skills und Workflow-Helfer benennen die fertige Datei unter Windows um. | In der Sandbox: Ablage im Projekt gelingt, zweite Ablage unter demselben Namen wird abgelehnt. Kein neuer vollständiger Workflow-Lauf. |
| Code, Codex-Ausgabe: Reviewer mit `fork_turns` `none` starten. | Drei von drei Starts ohne geerbten Verlauf. |
| UI: Die Angabe, dass keine Stufe festgelegt ist, steht im Berichtsabschnitt. | Im Review vorhanden, in der Umsetzung weiter nicht; je ein Lauf. |
| Code und UI: Das Benennen einer Teständerung ist ein eigener Satz. | Nicht belegt: In beiden Kontrollläufen wurde kein bestehender Test geändert. |

Die Kontrollläufe (A1, A2, A4, A5) nutzten die korrigierten Pakete aus dem
Arbeitsordner, bei abgeschalteten installierten Skills. Es sind dieselben
Aufgaben; sie zeigen nur, ob die Formulierung bei diesen Aufgaben greift.

### Offen

- Sol nennt im Umsetzungsbericht weder die fehlende Stufe, noch fragt es
  nach, wenn die Änderung einen nicht genannten Zustand verändert.
- Die Zahl der Befunde im UI-Review schwankt zwischen zwei Läufen derselben
  Aufgabe (7 und 12); die ausgeschlossenen Punkte wurden in keinem gefordert.
- `codex exec` startet in der Windows-Sandbox nur mit der Entwickleroption
  `prefer_mxc` Befehle; ohne sie scheiterte jeder Befehl mit Fehler 1909.

Suite-Prüfung 12/12 auf `070f567`; Laufzeit-CI Run 44894282174, sechs von
sechs Jobs.

### Drei Abschlussläufe zu Workflow und Plan

Auf Wunsch des Nutzers höchstens drei weitere Läufe, mit den korrigierten
Paketen aus dem Arbeitsordner bei abgeschalteten installierten Skills.

| Lauf | Aufgabe | Ergebnis |
| --- | --- | --- |
| 1 | Workflow führt PLAN-0001 zu Ende: W-002 ab dem laufenden Schritt, dann W-003. gpt-6.2-sol high. | Plan `completed`, Index `active_plan: null`, 19 Tests, Profil gültig, acht Commits, kein CRLF. Zehn frische Reviewer auf xhigh, jeder mit unverändertem Auftrag aus `.scoville/temp`; keiner blockiert. Zwei Reviews verlangten Änderungen (Datumsformat in Schritt 1, Kodierung der CSV-Ausgabe); beide wurden korrigiert und frisch geprüft. Startprüfung vor W-003 gelaufen. 27 Minuten. |
| 2 | Plan-Pflege: neues Arbeitspaket vor ein bestehendes einreihen, eine Entscheidung festhalten, nichts umsetzen. medium. | Profil gültig, nur Planungsdateien geändert. W-004 steht vor W-003, W-003 hängt davon ab und verweist auf ADR-0001; IDs über den Helfer. 63 Sekunden. |
| 3 | Ersten Plan in einem Projekt ohne Profil anlegen, nichts umsetzen. medium. | Profil gültig, zwei Dateien, zwei Arbeitspakete mit Abhängigkeit. Die Arbeitsbedingungen des Auftrags („setz noch nichts um“, „keine anderen Projekte“) stehen als Ziel und Nicht-Ziele im Plan. 68 Sekunden. |

Vor Lauf 1 geändert: Der Workflow-Helfer legt die Auftragsdatei im
ignorierten `.scoville/temp` des Projekts ab, wenn das Temp-Verzeichnis zu
einer Windows-Sandbox gehört; der Satz zum Positionsmodus in Plan ist
umgestellt. Nach Lauf 3 ergänzt: Ziel und Nicht-Ziele beschreiben das
Ergebnis, Bedingungen des Arbeitsablaufs gehören in die Instructions des
Arbeitspakets. Dieser Satz war nach den drei Läufen nicht mit einem Modell geprüft; der
Nachlauf unten holt das nach.

Beobachtet und nicht geändert: Im Workflow-Lauf schreibt Sol den Nachweis als
Klammerliste mit 364 und 435 Zeichen; jede Angabe bleibt unter der Grenze von
200. Die zehn Auftragsdateien blieben nach dem Lauf in `.scoville/temp`.
Ask übergibt eine Frage über 8 KiB in der Sandbox weiterhin als Datei, die der
Berater nicht lesen kann.

Suite-Prüfung 12/12; Laufzeit-CI Run 44900592553, sechs von sechs Jobs.

### Nachlauf zum Satz über Arbeitsbedingungen

Ein weiterer Lauf auf Wunsch des Nutzers, mit den installierten Skills
(Quelle 73e883e), gpt-6.2-sol medium, 64 Sekunden. Aufgabe wie Lauf 3,
ergänzt um eine Ergebnisgrenze (nur Standardbibliothek) und einen Ausschluss
(keine Jahresauswertung); die beiden Arbeitsbedingungen („setz noch nichts
um“, „keine anderen Projekte“) standen unverändert im Auftrag.

Ergebnis: Profil gültig, zwei Dateien, zwei Arbeitspakete mit Abhängigkeit,
kein Code geändert. Das Ziel nennt das Ergebnis und die Grenze
„ausschließlich die Python-Standardbibliothek“, die Nicht-Ziele nennen nur
die Jahresauswertung. Die Arbeitsbedingungen stehen nirgends im Plan, auch
nicht in den Instructions; sie binden keine spätere Arbeit. `authoring.md`
wurde vor dem Schreiben gelesen. Die erste Validierung meldete gemischte
Zeilenenden aus der PowerShell-Ausgabe; die Sitzung stellte auf LF um und
validierte erneut.

Einordnung: Der Fehler war in einem Lauf aufgetreten. Ein sauberer Lauf passt
zum Satz und beweist ihn nicht. In diesem einen Lauf blieb die Ergebnisgrenze
im Ziel. Die Regel nannte zu diesem Zeitpunkt genau die beiden
Arbeitsbedingungen der Aufgabe als Beispiele; der Lauf zeigt deshalb nur,
dass das Modell die genannten Fälle erkennt. Die Beispiele sind in W-010
gestrichen.

## W-010: Gesamtprüfung durch gpt-6.2-astra

### Prüfung und Einordnung

`gpt-6.2-astra` (high) hat alle Skill-Quellen und die Änderungen
dieses Plans gelesen, ohne etwas zu ändern. Der Bericht liegt unter
`state/2026-11-14-skill-evaluation/ASTRA-6.2-GESAMTPRUEFUNG.md` und vom 2026-11-23 nennt 28
Befunde: 18 Fehler (F01 bis F18), 8 Lücken (L01 bis L08) und 2
Kürzungsmöglichkeiten (K01, K02). Jeder Befund außer L01 bis L03 wurde an der
Quelle nachgelesen; F04 wurde an einer Kopie nachgestellt.

Übernommen (19): F03, F04, F05, F06, F07, F08 (nur die rechnerabhängige
Testzeile), F10, F11, F12, F14, F15, F16, F17, F18, L06, L07, L08, K01, K02.
L08 nur zum Teil: Die drei Beispiele sind gestrichen; die Frage an den Nutzer
im Bericht, die der Befund ebenfalls nannte, bleibt auf Entscheidung des
Nutzers.
Sechs davon gehen ganz oder teilweise auf Änderungen aus W-009 zurück: L07, F08, F12, F15, F16
und F17.

Nicht übernommen (9, dazu ein Teil von F08):

| Befund | Grund |
|---|---|
| F01 | Schreiben außerhalb des Projekts setzt voraus, dass jemand `.scoville` oder `.scoville/temp` selbst nach außen verlinkt hat. |
| F02 | Die Referenz verlangt je Runde eine eigene Datei. Überschreibt ein Agent trotzdem die Auftragsdatei der Vorrunde, fehlt sie nur zum Nachvollziehen: die Folgedatei trägt Berater, Arbeitsverzeichnis und Einstellungen weiter. |
| F08, zweiter Teil | Die Erkennung prüft nur Pfadbestandteile und würde auch einen gleich aufgebauten Temp-Pfad außerhalb der Sandbox umleiten. Ein solcher Pfad ist nicht belegt, und die Folge wäre nur die Ablage im Projekt. |
| F09 | Ein Eingabeweg über stdin wäre neue Mechanik für eine Schätzung. |
| F13 | Der Bewertungskatalog von Code ist laut `members/scoville-code/development/README.md` unveränderter historischer Beleg; die README nennt die Zwei-Korrekturen-Schwelle selbst als überholtes Beispiel. |
| L01, L03 | Mehrfaches Auflisten und Speicher zählen erst bei Größen, die kein Projekt erreicht. Nicht an der Quelle nachgelesen. |
| L02 | Der Validator folgt einer Kette abgelöster Decisions rekursiv. Die Messaufgabe R19 verlangte eine Kette von 1.200 Decisions, und der Validator brach dort mit `RecursionError` ab. Eine solche Kette heißt, dass dieselbe Entscheidung rund tausendmal nacheinander abgelöst wurde. |
| L04 | Hinter dem gestrichenen Explorer-Satz steht kein belegter Fehler. |
| L05 | Eine `.gitignore` ohne die Regel hat der Nutzer selbst angelegt, oder sie blieb leer zurück, weil das Schreiben von zwei Zeichen scheiterte. Folge: Auftragsdateien erscheinen im Git-Status. |

### Änderungen (Suite `7511973`, Shared `d3d9073` und `1989d4b`)

- Plan: `done` im Workflow-Lauf erst nach einem Step-Review, den Workflow für
  den Step verlangt (F03). Rat bei doppelter Arbeitspaket-ID ohne den Helfer,
  der an derselben Dublette abbricht (F04). Meldung zum leeren Abschnitt wie
  im Validator (F05). Eine Decision wird nur gelöscht, wenn keine erhaltene sie
  in `superseded_by` nennt (F06). Der Satz zu Arbeitsbedingungen nennt keine
  Beispiele mehr (L07). Bewertungsfall nennt eine Änderung, die Validierung
  verlangt (F14).
- Setup: `show` füllt eine unvollständige Schema-2-Angabe mit alten Feldern
  aus den Vorgaben auf; Test ergänzt (F07).
- Workflow: rechnerabhängige Testzeile entfernt (F08).
- Größenprüfer: Prozesskennung auch nach `interrupted_cleanup_incomplete`
  (F10). Vorher `error=interrupted_cleanup_incomplete exit=1`, nachher
  `error=interrupted_cleanup_incomplete process_id=<n> exit=1`, beide Stände
  mit demselben Aufruf nachgestellt; Test für beide Ursachen ergänzt. Die
  Zustellreferenz sagt, wozu die Kennung dient.
- UI: Übersetzungsprüfung je Quelle, die die Seite ausliefert (F11);
  WordPress-Tabelle nennt den fehlenden Gruppennamen als Mangel (F18).
- Handoff: Workflow-Satz nur in der Codex-Ausgabe (F16).
- Skillwriter: „Preserve the intention“ nennt nur den Zusatz zur gemeinsamen
  Schreibregel (K01).
- Ask: Der Berater liest den zutreffenden Skill (K02).
- Code-Kriterien, Regel 2: die drei Beispielnutzungen gestrichen, auf
  Entscheidung des Nutzers (L08). Die Wirkung der Regel ist mit den Beispielen
  gemessen (W-005) und ohne sie nicht erneut.
- Aussagen berichtigt: Ask-Überschrift (F12), „All Skills“ und
  Workflow-Überschrift im Suite-Changelog (F15, F16), zwei Urteile in diesem
  Protokoll (F17, L06).

### Gegenlesen

Ein Agent mit Claude Opus 5.5 (xhigh) hat die 15 Quelländerungen gegen ihre
Gegenstellen gelesen, ohne etwas zu ändern: kein Fehler, kein neuer
Widerspruch; der neue Setup-Test scheitert am alten Code. Sechs Hinweise,
fünf übernommen:

- Die Löschbedingung für Decisions galt nur für abgelöste; sie steht jetzt an
  der Löschung selbst.
- Die einfache Fehlerzeile mit `process_id` war in der Zustellreferenz nicht
  erklärt, und kein Test deckte sie ab; beides ergänzt.
- „the Step review“ unterstellte, dass jeder Step einen Review hat; jetzt „any
  Step review that Workflow requires for it“.
- Der Bewertungsfall nennt, dass die Acceptance beobachtet ist.
- Die Übersetzungsprüfung nennt jeden registrierten Skript-Handle.

Nicht übernommen: Der Vorschlag, den Plan-Satz um „when or how the work is
carried out“ zu erweitern. Der Lauf unten zeigt den vermuteten Fehler nicht,
und die Formulierung läge nah an einem der gestrichenen Beispiele.

### Lauf zum Plan-Satz ohne Beispiele

Ein Lauf mit gpt-6.2-sol medium über die Codex-CLI, 76 Sekunden, mit den
Paketen aus Quelle `7511973`; Aufgabe und Wortlaut wie im Nachlauf zu W-009.

Ergebnis: Profil gültig, zwei Dateien, zwei Arbeitspakete mit Abhängigkeit,
kein Code geändert, Tests unverändert bestanden. Das Ziel nennt das Ergebnis
und die Grenze „ausschließlich die Python-Standardbibliothek“, die
Nicht-Ziele nennen nur die Jahresauswertung. „Setz noch nichts um“ steht
nirgends. Die Grenze „keine anderen Projekte, kein entfernter Server“ steht in
den Instructions beider Arbeitspakete; die Sitzung hat sie als Bedingung für
spätere Arbeit gelesen. `authoring.md` wurde vor dem Schreiben gelesen.

Einordnung: ein Lauf. Er passt zum Satz ohne Beispiele und beweist ihn nicht.
Anders als im Nachlauf zu W-009 nennt die Regel die Bedingungen der Aufgabe
nicht mehr.
Die Ergebnisgrenze der Aufgabe (nur Standardbibliothek) ähnelt aber dem
Beispiel `No new runtime dependency`, das die Regel für Ergebnisgrenzen
nennt. Dass die Grenze im Ziel blieb, zeigt deshalb wenig über andere
Ergebnisgrenzen.

## W-011: Nachprüfung der Korrekturen durch gpt-6.2-astra

### Prüfung und Einordnung

`gpt-6.2-astra` (high) hat die Korrekturen aus W-010 gegen ihre Gegenstellen
gelesen, ohne etwas zu ändern und ohne Tests zu starten. Der Bericht vom
2026-11-23 liegt unter
`state/2026-11-14-skill-evaluation/ASTRA-6.2-NACHPRUEFUNG.md`. Er nennt 15 der
19 übernommenen Befunde behoben und 4 teilweise behoben (F04, F05, F10, L08),
dazu 7 Befunde (B1 bis B7) und 5 Einwände gegen Ablehnungsgründe (A1 bis A5).
Nach seiner Lesart scheitern beide neuen Tests aus W-010 am alten Code. Jeder
Punkt wurde an der Quelle nachgelesen.

| Punkt | Einordnung | Änderung oder Grund |
|---|---|---|
| B1 (F10) | nicht übernommen | Die Prozesskennung fehlt nur, wenn der Aufrufer ein Ausgabelimit unter etwa 125 Tokens angibt und zugleich ein Timeout oder eine Unterbrechung mit unbestätigtem Aufräumen eintritt. Kein Host setzt ein solches Limit. |
| B2 (F04) | übernommen, ohne die Obergrenze | Der Validator nennt die nächste freie ID selbst und sagt, dass die markierte Zeile das zweite Vorkommen in der Datei ist, nicht zwingend das neuere Arbeitspaket. Bei `W-999` nennt er eine ungültige ID; 999 Arbeitspakete in einem Plan erreicht kein Projekt. |
| B3 (F05) | übernommen | Ein Goal, das nur `[]` enthält, wird wie ein leeres abgewiesen. |
| B4 (L08) | übernommen | Die Einordnung in W-010 sagt jetzt, dass L08 nur zum Teil übernommen ist. |
| B5 | übernommen | Zwei Changelog-Sätze nannten einen Vorfall, der nur aus der Quelle folgt: dass ein Backend-Review Scoville UI las und dass ein Workflow-Test in der Windows-Sandbox scheiterte. Sie beschreiben jetzt die Bedingung. |
| B6 | übernommen | Der Changelog nannte die drei gestrichenen Nutzungen „the scenarios of the tasks“. Sie stammen aus den Messläufen, in denen Sitzungen sie ungefragt unterstellt hatten; die Aufgaben nannten sie nicht. |
| B7 | übernommen | Die Überschrift im Plan-Changelog nennt nur noch den Satz zu Arbeitsbedingungen. Die Einordnung des Laufs in W-010 hält fest, dass die Ergebnisgrenze der Aufgabe dem verbliebenen Beispiel der Regel ähnelt. |
| A1 (L02) | Grund berichtigt, keine Änderung | Die Ablehnung nennt jetzt den Abbruch aus R19 und was eine solche Kette bedeutet. |
| A2 (F02) | Grund berichtigt, keine Änderung | Verloren geht die Nachvollziehbarkeit der Vorrunde, keine Angabe, die eine spätere Runde liest. Ein exklusives Anlegen ließe jede weitere Beratung mit demselben Dateinamen einmal scheitern. |
| A3 (F01) | Grund berichtigt, keine Änderung | Es genügt ein nach außen verlinktes `.scoville`; auch das legt nur der Nutzer selbst an. |
| A4 (F08, zweiter Teil) | Aussage berichtigt, keine Codeänderung | Der Workflow-Changelog sagte „Outside such a sandbox nothing changes“. Er sagt jetzt, dass der Helfer den privaten Ordner an seinem Pfad erkennt. |
| A5 (L05) | Grund berichtigt, keine Änderung | Die leere Datei kann auch vom Helfer stammen; die Folge bleibt eine Datei im Git-Status. |

### Änderungen (Suite `eb4ede3`)

- Plan, `validate_profile.py`: Der Rat zu `WORK_ITEM_ID_DUPLICATE` nennt die
  nächste freie ID aus den gelesenen Überschriften.
- Plan, `markdown_structure.py`: `[]` allein im Goal gilt als fehlender Inhalt;
  die Meldung lautet „Goal needs authored content, not `[]`.“ Die Prüfung gilt
  für Validator und Selektor.
- Zwei Tests in `test_diagnostic_corrections.py`, je mit der Korrektur und
  erneutem Validatorlauf. Beide scheitern am Stand `95d2da2`: Der alte Rat
  enthält keine ID, und ein Goal aus `[]` galt als gültig.
- Changelogs der Suite, von Plan, Code, UI, Ask und Workflow berichtigt.

Kein Modelllauf und kein Gegenlesen: zwei kleine Änderungen an Diagnosen,
durch Tests gedeckt. Suite-Prüfung 12/12, Laufzeit-CI-Run 45246766728: 6 von 6.
