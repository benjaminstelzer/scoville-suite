# PLAN-0020: Umsetzung und Nachweise

Ausgangsstand: `8ad605edbb87aa2a3f024d6b1e9f74b6eaab6540`.
Die betroffenen Skill-Quellen waren vor Umsetzung unverändert. Der Ausgangsstand
ist in Git und als Testeingabe unter dem lokalen Testverzeichnis erhalten.
Rohantworten und Testeingaben wurden auf Nutzerwunsch nach
`C:/Users/benja/Desktop/test/plan0020/` verlegt. Weitere Test-Chats verwenden
das gespeicherte Codex-Projekt `test`. Alte absolute Pfade in unveränderten
Rohprotokollen bezeichnen den ursprünglichen Testort, keine aktuellen Pfade.

## Geändertes Verhalten

- Workflow beendet nach dem erforderlichen Host-Wait und einem Timeout den Turn,
  wenn keine unabhängige Arbeit bleibt. Keine zusätzliche Abfrageschleife.
- Manager-Rollover überträgt das tatsächlich gestartete eigene Modell/Effort
  ausdrücklich sowie offene Fragen und ihren Antwortstand.
- Zusammenhängende Reviewbefunde werden als begrenzte Zustandsunterscheidung mit
  direkten Verbrauchern beauftragt; einzelne Befunde bleiben klein.
- Plan unterscheidet normale Fortsetzung, bloße Auswahl eines blockierten
  Nachfolgers und den strengeren expliziten Rückkehrpunkt. Die bestehende
  Abschluss-/current_item-Semantik bleibt erhalten, keine Migration.
- ADR-0116 ist ausschließlich die angeforderte Deployment-Entscheidungsvorlage.
  Eine neue Auslieferungsrolle wurde nicht eingeführt.
- Ask entfernt die zusätzlichen Genehmigungsregeln und erhält einen kleinen
  Prompt-/Startargument-Helper. Der Caller holt native Antworten nach ADR-0117 ab.

## Beobachtete Prüfungen

| Prüfung | Ergebnis |
| --- | --- |
| Workflow-Tests einschließlich neuer Lifecycle-Verbindung | 25 bestanden |
| Ask-Tests einschließlich Prompt-Helper | 33 bestanden |
| Plan-Tests | 80 bestanden |
| Suite-Entwicklungstests einschließlich Helper-Verträgen | 37 bestanden |
| Gebautes Codex-Paket nach Helper-Erweiterung | check-packages valid:true |
| Planprofil während Umsetzung | valid:true |
| Skill-Creator quick_validate | bestehendes Frontmatter-Feld compatibility wird von dieser Validatorversion abgelehnt; kein behaupteter Pass |

Der neue technische Durchlauf verbindet echte paketierte Helper in einem
temporären Projekt: Auswahl/Modellauflösung, Worker-, Reviewer-, Korrektur- und
Fortsetzungsprompt, Auswahl eines blockierten gewöhnlichen Nachfolgers und
finaler Plan-/Indexabschluss. Produktarbeit, Reviewurteile und Host-Ereignisse
sind dabei simuliert. Der Validator meldete einen falsch formatierten
Testblocker; die Fixture wurde gemäß seinem bestehenden Format korrigiert.

## Modellvergleich

Katalog: `development/plan0020-cases.json`. Luna medium, jeweils frischer Kontext,
keine nativen Aktionstools. Die nativen Sitzungsdaten bestätigen gpt-6-luna/medium.
Ausgangsstand, Kandidat und einfacher Prompt wurden auf denselben Kernfällen
verglichen. Antworten wurden inhaltlich geprüft, nicht durch Worttreffer gewertet.

- Alter Workflow: nach Timeout weiteres Warten und eine Nachricht an den Worker
  empfohlen. Kandidat: Turn beenden, keine Folgeabfragen.
- Alter Plan: bei begrenztem Auftrag Abschluss ohne erforderliche Nachfolgerwahl
  empfohlen. Kandidat: Nachfolger auswählen, außerhalb des Auftrags nicht starten.
- Alter Ask: zusätzliche Chat-/Nachrichtenfreigabe verlangt. Kandidat: Beratung
  ausführen und antworten ohne neue Freigabe.
- Modellübernahme, erhaltene Implementierung, gezielte Korrektur, Stops und
  Nichtaktivierung funktionierten in den entsprechenden Kandidatenfällen.
- Der einfache Prompt löste grundlegende Ask-Fälle, kannte aber nicht die genaue
  Plan-/Workflow-Semantik. Keine allgemeine Überlegenheit oder Zeitersparnis belegt.

Erste Harness-Versuche scheiterten vor Modellaufruf an Receipt-Pfaden. Erste
einfache Baselines luden teils doch Referenzen nach bzw. forderten Vertragsdaten;
diese sind als Vergleich ausgeschlossen. Die isolierten Wiederholungen verbieten
Referenznachladen ausdrücklich. Alle Fehlversuche sind erhalten. Die finale native Ask-Prüfung ist unten getrennt dokumentiert.

## Nativer Ask-Test und tatsächliche Grenze

Luna-Chat `01a0ebd5-922f-7ff0-88ba-bfe0699c8313` erstellte einen lesenden
PHP-Kompatibilitätsbefund, fragte nach konkreter Nachforderung die Mindestversion
beim Caller nach, erhielt die Antwort und stellte den finalen Befund zu.
Anfangs wurde die eigene ID voreilig als unbekannt bezeichnet; nach der
Instruktionspräzisierung las der Chat CODEX_THREAD_ID und lieferte den richtigen
Wert. Das ist reale Host-Interaktion, keine produktive Projektprüfung.

Der verpackte neue Helper wurde erfolgreich direkt an create_thread übergeben:
Astra-Chat `01a0ebdb-b7fb-7cb2-97ad-984c090c656c`, Referenz
`plan0020-helper-consumer`. Astra bestätigte lesend Prompt-Erzeugung, Unicode,
Rückadresse und leeres stdout bei ungültiger UUID. Es verweigerte jedoch die
aktive Rücknachricht wegen der Host-Regel für Agentenaufträge. Der Caller las
das vollständige Ergebnis im bekannten Chat. Keine Auto-Approval-Ablehnung,
kein technischer Sendefehler: Die Nachricht wurde nicht versucht.

Damit ist aktive Rückzustellung nicht zuverlässig durch Skilltext erzwingbar.
ADR-0117 wurde auf Nutzerwunsch angenommen. Der native Ergebnisabruf ist umgesetzt
und mit Astra erfolgreich geprüft, siehe finaler Stand.

## Finaler Stand nach Nutzerpräzisierungen

Native Startargumente erzeugen die Ask-/Dispatch-/Manager-Helper. Gemeinsame
Titel- und Erstellungslogik liegt in shared/runtime/native_task_arguments.py.
Manager übernehmen ihre eigenen nativen Einstellungen, nicht Worker-Routen.
Finale Titel: `SC-WRK-7: Test App · PLAN-0042/W-009/steps-1-3`, entsprechend
SC-REV und SC-MGR. Ask verwendet ausschließlich `SC-ASK-ASTRA: Prüfe den Patch`:
aufgelöste Berater-ID uppercase, keine Nummer und kein zusätzliches Projektfeld.
Der technische Modellparameter und die Schreibweise des Titeltexts bleiben erhalten.
Diese späteren Nutzerpräzisierungen ersetzen die ältere Titelbeschreibung in W-010.
Alle neu erstellten Chats werden anhand der zurückgegebenen tatsächlichen ID angepinnt.

Manager- und Kind-Rollover beginnen mit derselben generierten FIRST ACTION:
sobald benötigte Informationen vorliegen, Archivierungsnachricht an den Vorgänger
senden, erst danach gewöhnlich lesen oder arbeiten. Nur unverzichtbare fehlende
Informationen werden vorher beschafft. Kein Warten auf Archivierungsbestätigung;
fehlgeschlagene oder vom Host untersagte Sendung wird gemeldet und stoppt Übernahme.
Workflow ist Codex-only; dafür gibt es bewusst keinen manuellen Fallback.

Finale Checks im Desktop-Testprojekt: workflow-final.txt (25), ask-final.txt (33),
plan-final.txt (80), build-final.txt (37), profiles-final.txt (4) bestanden.
Die Profiltests bauen auch isolierte Exporte erneut. Negativtests prüfen fehlende
Registrierung, falsche Bibliotheksklassifizierung, fehlende/falsch zugeordnete
Fallbacks, bedingungslose oder eingebettete Routen, unregistrierte verwendete
Helper und Codex-Leaks. General-Einzel- und Suite-Pakete sind abgedeckt.
Modellfall runs/final-v3-helper-final besteht inhaltlich: endgültige Titel,
Helper-Fehlerbehandlung, Manager-Modell, Pinning und Archivierungsnachricht zuerst.
Keine gemessene Geschwindigkeits- oder Tokenersparnis behauptet.

Astra/medium-Chat 01a0ec17-3a46-7cc1-8d42-989b79a4a5cd wurde direkt mit
unverändertem Helper-JSON erstellt und angepinnt. Er fragte normal nach der
PHP-Mindestversion. Der Caller antwortete im selben Chat mit PHP 7.4 und holte
anschließend den korrekten vollständigen Befund über wait_threads ab:
str_contains benötigt PHP 8; strpos mit strikt geprüftem false ist hier kompatibel.
Keine Rücksendeberechtigung oder zusätzliche Genehmigung verlangt.
Rohdaten: ask-pull-arguments.json und ask-pull-result.json. Der spätere kurze Titel
wurde mit set_thread_title erfolgreich angewendet. Technische Tests prüfen den
finalen Generator einschließlich fehlender Berater-ID und korrigiertem Aufruf.

Weitere native Consumer: Worker 01a0ec05-5ef1-7330-a83a-716b49d484ad,
Manager 01a0ec05-8c3a-73d2-b3b6-59d12cbf8ad9 und Reviewer
01a0ec08-7c7d-76e3-8506-d02817a7f7b4 akzeptierten unveränderte Helper-Argumente.
Worker und Reviewer meldeten ihre Ergebnisse, Manager schickte die Übernahmenachricht.
Das waren begrenzte Tests, kein produktiver Gesamtworkflow. Diese frühen Chats
verwendeten noch frühere Titelformate; sie belegen nicht die endgültige Schreibweise.

Grenzen: runs/final-v3-ask ist als Kandidatennachweis ausgeschlossen, weil das
Modell einen zusätzlich geladenen alten installierten Ask-Skill mit abweichenden
Regeln meldete. Der eigenständige native Astra-Test belegt den neuen Rückfrageweg.
Einige Titeländerungen älterer Testchats scheiterten mit no rollout found.
Release-Staging wurde wegen einer Windows-Verzeichnissperre nicht aktualisiert;
der begonnene General-Refresh wurde exakt aus der Sicherung wiederhergestellt.
Verifiziert sind Quellen und isolierte Builds. Keine Installation, Veröffentlichung,
Commit oder Push. PLAN-0019 bleibt draft und unausgeführt.

Die neun finalen nativen und Modell-Testchats wurden nach Sicherung der Ergebnisse
erfolgreich archiviert; einzelne Toolantworten stehen in final-cleanup.json im Testprojekt.
PLAN-0020 ist abgeschlossen. Abschließende Profilprüfung: valid:true, keine
Fehler oder Warnungen; README-/Shared-Quellabgleich und git diff --check bestanden.
