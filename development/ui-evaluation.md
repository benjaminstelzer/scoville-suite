# UI-Vergleich für PLAN-0006

Stand: 2026-09-25. Dieses Protokoll wurde vor der Bewertung des finalen Kandidaten festgelegt. Es trennt Skill-Verständnis, tatsächliche WordPress-Laufzeit und Nutzertests. Die historischen 36 SOL-Medium-Läufe wurden nicht ausgeführt. Der zunächst vorbereitete 36-Arme-Vergleich wurde vor seinem ersten Lauf durch die ausdrückliche Nutzergrenze von maximal 30 Minuten ersetzt. Eine weitere Nutzerpräzisierung verlangt zwei tatsächliche Implementierungsaufträge: Greenfield erstellt eine neue Classic-PHP-Seite „Queue preview“, und eine Änderung repariert bedingt sichtbare Felder und Dialogfokus in der bestehenden React-Seite. Beide Aufgaben wurden vor dem ersten Lauf eingefroren; jeder Arm erhält eine eigene Kopie derselben Fixture. Pro Aufgabe laufen höchstens drei frische SOL-6-High-Arme ohne UI-Skill, mit bisherigem WordPress-Skill und mit gemeinsamem Kandidaten, maximal 120 Sekunden je Arm. Die übrigen Fallgruppen bleiben ein vorbereiteter, nicht ausgeführter Vertrag. Ein einzelner Lauf belegt keine Modellüberlegenheit.

## Vergleichsbasis

- Für jeden der beiden Dreiervergleiche bleiben Aufgabeninhalt, eingefrorene Fixture-Kopie, WordPress-Version, Browser, Viewport, Toolzugang, Modell `gpt-6-sol`, Reasoning `high` und 120-Sekunden-Limit gleich. Jeder Arm nutzt einen frischen Kontext und schreibt ausschließlich in seine Kopie. Die Live-Seite zeigt zunächst die unveränderte Fixture; nur dort tatsächlich gerenderte Änderungen zählen als Runtimebeleg. Die separate direkte Runtime-Stichprobe prüft Backend-Route, Fehler/Speichern/Werterhalt, Fokus und schmalen Viewport soweit in der Frist möglich. Eine Negativkontrolle grenzt Plugin-Frontend und reine Backendlogik vom UI-Adapter ab.
- Die beiden alten Skill-Quellen liegen vor Änderungsbeginn gesichert unter `<workspace-root>/temp/2026-09-25-scoville-ui-merge/baseline/`. Der finale Kandidat kommt ausschließlich aus dem geprüften Release-Build `<workspace-root>/skills/temp/release/ui-merge/yaml-fix/standalone/scoville-ui/scoville-ui/`, dessen Core-SHA-256 `E080DD3AB9CA71868DCC82B8540B39802B508AA9034F573559B279AA2D505592` ist. Paketlayout und Receipt-Hashes werden im Ergebnisbericht festgehalten.
- Die lokale Testumgebung enthält WordPress 7.1.2 und 7.0.6 in getrennten Installationen. Ein kleines, nur dort aktiviertes Fixture-Plugin bietet eine Classic-Einstellungsseite und eine React/Core-Components-Workflowseite. Die Fall- und Fehlerdefinition wird vor dem ersten Kandidatenlauf eingefroren. Seine Defekt- und Bewertungsschlüssel bleiben außerhalb des Repositorys im Task-temp und gelangen nicht in Modellprompts.
- Die vorhandenen `development/luna-tests/ui-cases.md` und `wordpress-cases.md` bleiben Verständnisproben ohne Browser. `prepare_wordpress.py` ist kein Runtime-Harness. Frühere Resultate gelten nicht für die neuen Paketbytes.

## Sechs Fallgruppen

| Auditbefund | Classic und React prüfen | Negativkontrolle |
| --- | --- | --- |
| F1 praktische Wirkung | Quelle, gerenderte Seite und fehlgeschlagene Handlung getrennt beobachten | Source-only darf Rendering als unbekannt benennen |
| F2 gemeinsamer Prüfvertrag | Reflow, Fokus, Eingabewechsel, Kontrast und reduzierte Bewegung bei Relevanz | Native Core-Unterschiede sind kein Skalendefekt |
| F3 Informationsaufbau | Aufgabe, Entscheidungsreihenfolge, Gruppierung, Wirkungsbereich und Wiedererkennen | Legitime Dichte, getrennte Entscheidungsbereiche und geschützte Texte bleiben erhalten |
| F4 Accessibility | Formularfehler, Werterhalt, Dialogöffnung/-schluss, Fokusrückkehr | Keine pauschale Vollprüfung oder universelle 44px-AA-Regel |
| F5 Zustandswechsel | Verzögerung, veraltetes Ergebnis, Doppelaktion, Lade- und Fehlerweg | Lokale Labormessung ist kein Felddatenbeleg |
| F6 Paket und Adapter | Routing, Classic/Core-Owner, Portal, Version, Tokenladeort, PHP-/JS-i18n | Kein React-Zwang, keine Tokenannahme aus Registrierung, ausgeschlossene Flächen bleiben host-owned |

Entwicklungsfälle dürfen zur Regelarbeit verwendet werden. Getrennte Schlussfälle prüfen die finalen Bytes; nach einer Kandidatenänderung werden Build und betroffene Fälle wiederholt. Ein offengelegter Schlussfall gilt dann nicht mehr als unbekannt. Der Prüfer erfasst pro Fall gefundene und verfehlte Defekte, Fehlalarme, Aufgabenabschluss, Owner-/Scope-Verstöße, falsche Nachweisbehauptungen, geladene Instruktionsbytes, Toolaufrufe und Zeit. Source, DOM/Geometrie, selbst betrachteter Screenshot und Interaktion werden getrennt belegt. Ein heuristischer Agentencheck ist kein Nutzertest; tatsächliche Zielgruppenfreundlichkeit oder statistische Überlegenheit werden daraus nicht behauptet.

Rohprompts, Traces, Screenshots, Browserzustand und verdeckte Schlüssel liegen nur unter `<workspace-root>/temp/2026-09-25-scoville-ui-merge/wp-tests/`. Im Repository verbleibt nach Abschluss nur ein knapper Ergebnis- und Grenzbericht. Veröffentlichung ist nicht Teil dieser Prüfung.
