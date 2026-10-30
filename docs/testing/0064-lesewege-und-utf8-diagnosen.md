# PLAN-0064: Lesewege und UTF-8-Diagnosen

## Quellen und Änderungen

Suite-Baseline ed125d7a14129a46b53d2ea8640debe6dc943c8b, Shared-Baseline 7e199a7356f640000f0eec6a35deb29c7661417b. Die bereits freigegebene, noch nicht committete AGENTS.md-Testauswahl wird übernommen. Auftrag erlaubt Veröffentlichung und lokale Updates vollständig für Codex, bei Claude ausschließlich Plan.

- skill_composition.md ersetzt die redundante Layoutreferenz durch unverändert anwendbare Aktivierungs-/Nutzerausschlüsse. Standalone-/Suitebedingungen bleiben in ihren vorhandenen Paketblöcken.
- machine-data.md nennt Quellenpassagen, Quellsuchtreffer und Quelldiffs ausdrücklich als direkt lesbar. Eingebettete Berichte und strukturierte Zustände bleiben auswertungspflichtig. Rohdump-Schutz und vollständiges Lesen erforderlicher Quellen bleiben erhalten.
- output-delivery.md und die UTF-8-Fehlermetadaten unterscheiden vollständige Originalbytes, tatsächlichen Kindstatus und offene Textinterpretation. Der Checker bleibt bei 125, notwendiger Text ist weiter keine erfolgreiche Abnahme. Nur textabhängige Arbeit stoppt. Kein Encodingraten, Ersatzzeichen oder erneuter Produzent.
- common.md präzisiert nach beobachtetem zusätzlichem Read den vorhandenen Owner: Instruction Design gilt für agentenbezogene Ausgaben, geladen wird es beim Bearbeiten des produzierenden Skills, der Regel oder Vorlage. Empfänger folgen ihrem Auftrag und den gemeinsamen Schreibregeln. Keine zusätzliche Ausnahmeverwaltung oder Loaderlogik.

## Tatsächlich beobachtete Ladewege

Drei native Fälle mit gpt-6.1-sol/low. Modell/Effort aus turn_context geprüft, nicht aus Selbstberichten abgeleitet. Read-only-Fixture: Katalog mit 100.000 Zeilen, 20.000 eindeutigen Integer-Auswahl-IDs und Pflicht zum Erhalt von Reihenfolge und doppelten Zeilen. Erster Fall nutzt echtes Standalone-Codepaket, zweiter unverändert erzeugten nativen Ask-Reviewauftrag, dritter frisches Codepaket mit präzisiertem common.md. Alle Antworten empfehlen den lokalen Set-Lookup unter Erhalt von Reihenfolge/Duplikaten; keine Implementierung oder Projekttests durch die Empfänger.

| Fall | Native Sitzung | Skilldateien gelesen | UTF-8-Dateibytes | Zusätzliche Beobachtung |
| --- | --- | --- | --- | --- |
| Codeempfehlung | 01a18d54-3f24-7ba2-9056-a4ce0cd6d7e4 | 6 | 32.255 | SKILL, Qualität, Writing, Instruction Design, Shell und Output Delivery |
| Helpergenerierter Ask-Review | 01a18d54-8a21-75b0-89dc-76e74883549f | 4 | 19.655 | Writing, Qualität, Shell und Output Delivery; kein Instruction Design |
| Erneute Codeempfehlung | 01a18d58-0fcd-7cf2-a16d-152678327911 | 6 | 33.621 | Instruction Design entfällt, Change kommt hinzu; zusätzlich eine kleine Dateinameninventur |

Alle Fälle lesen außerdem die zwei benannten Fixturequellen. Keine wiederholten Dateipfade, Schreibaktionen oder abgeschnittenen Toolausgaben beobachtet. Reads stammen aus tatsächlichen Get-Content-Aufrufen der nativen Sitzungsaufzeichnungen, nicht aus behaupteten Leselisten. Dateibytes sind keine Tokenabrechnung oder vollständige Kontextmessung: Hostinjektionen, Prompttext und Transportframing sind nicht enthalten. Der vorhandene --load-trace/--size-report-Weg verarbeitet die daraus abgeleiteten Referenzlisten.

Die einzelne gezielte Klärung wirkt im erneuten Fall auf den Instruction-Design-Read, spart insgesamt jedoch keine Bytes. Keine statistische oder allgemeine Wirkungsbehauptung aus diesen drei Fällen. Weitere Ladeverbote oder Umstrukturierungen sind durch diese Stichprobe nicht begründet.

## Bewusste Grenzen abgeschlossen

- bundled Scoville Plan: im aktuellen beanstandeten Einstieg nicht vorhanden; Standalone-Unabhängigkeit bereits ausdrücklich erklärt. Kein weiterer Fix.
- Unabhängige Reviews: eigene Codeprüfung bleibt verpflichtend, zusätzliche unabhängige Prüfung folgt Nutzer-/Projektauftrag. Keine neue allgemeine Reviewphase.
- Reviewschleife: evidenzbasierter Wiederholungsstopp bleibt. Immer neue echte Befunde können weitere Runden erfordern; keine erfundene Konvergenz- oder Kostenobergrenze.

## Relevante Prüfungen

- Sechs Shared-Regel-/Consumer-Tests bestanden.
- 34 Runtime-Tests bestanden, ein POSIX-Signalfall unter Windows ausgelassen. Enthalten sind vollständige ungültige Originalbytes, Kindstatus 7, unveränderte Einmalwirkung und die neue Diagnoseanweisung. Keine schwächere UTF-8-Abnahme.
- Keine erneute vollständige check_all.py-Runde: Buildtool, Manifest und unabhängige Plan-/Setup-/Asklogik sind unverändert. Neue private Runtime-Matrix ist wegen geändertem paketiertem Python und CI-Test erforderlich.
- Changelogs an Root und acht tatsächlich betroffenen Membern ergänzt. Skillwriter-Payload unverändert. README-Inhalte unverändert.

## Auslieferung und Abschluss

- Quellenstand: Suite a0ac508, Shared f7e16ae. Die neue private [Runtime-Matrix](https://github.com/benjaminstelzer/scoville-runtime-ci/actions/runs/41078747966) besteht mit sechs Jobs auf Windows, Ubuntu und macOS. Der lokale POSIX-Skip bleibt als lokale Grenze erhalten.
- Vier Paketansichten gebaut und ihre Veröffentlichungsbelege geprüft. Beide Quellenexporte bestehen den Planvalidator. README-Dateien unverändert, vorhandene Prüfung wiederverwendet. Vollständige Git-Kandidatenbäume und Remote-main-Stände stimmen überein.
- Veröffentlicht: General efb8b3cd, Mainloop 0ed92b4e, Code 83aef6a2, Handoff 3c37d33e, Plan 4a947716, UI c41552d0, Ask e12f8ff1. Skillwriter dfd02113 bleibt unverändert. Abschließende Planrecords folgen als reine Suite-Metadatenaktualisierung.
- Lokale Pakete über den Skill-Installer vom verifizierten veröffentlichten Commit bezogen. 16 bestehende Codex-Kopien und ausschließlich Claude-Plan aktualisiert. Codex-Skillwriter unverändert aktuell. Inventar, Einstiegstexte und betroffene Runtimekopien geprüft. 82 Dateien der übrigen fünf Claude-Skills unverändert.
- Keine neue Installation fehlender Pakete, Tags oder Releases. Keine Behauptung eines Reloads in bereits laufenden Chats oder allgemeiner Modellzuverlässigkeit. Die neuen lokalen Skills stehen ab dem nächsten Turn bereit.
