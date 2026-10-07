---
format_version: 1
id: PLAN-0023
status: completed
created: 2026-09-29
updated: 2026-09-29
---

# Fixplan: Code-Laufzeitschutz und vollständige Ask-Rückgabe

## Goal

Scoville Code prüft vor und nach Implementierungen gezielt vermeidbare
Laufzeit- und Speicherkosten. Es nutzt geeignete vorhandene Caches korrekt,
schlägt neue nur begründet vor und überlässt deren Einführung dem Nutzer.
Scoville Ask sammelt beauftragte native Reviews auch nach Warte-Timeouts
vollständig ein und präsentiert sie im aufrufenden Chat.

## Non-goals

Kein pauschales O(n²)-Verbot, keine Optimierung unbeteiligter Codebereiche,
keine allgemeine Benchmarkpflicht und kein automatischer Cache-Einbau.
Kein neuer Skill, keine neue Runtime-Referenz, kein Release und keine Installation.

## Work items

### W-001 Kostenprüfung und begrenzte Cache-Entscheidung verankern

Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: Scoville Code erkennt relevante Kostenfallen vor und nach Änderungen, bevorzugt einfache günstigere Lösungen und wahrt die Nutzerentscheidung bei neuen Caches.
Acceptance: Die drei unten genannten Regelorte ergeben einen widerspruchsfreien Ablauf. Prüfungen bleiben auf das geänderte Verhalten und konkret betroffene Aufrufpfade begrenzt. Vor der Umsetzung werden erwartete oder begründet angenommene Datenmengen, Aufrufhäufigkeit sowie Zeit- und Speicherbedarf betrachtet. Nach der Umsetzung wird der tatsächliche Code auf dieselben Kostenfallen und günstigere Alternativen geprüft. Verschachtelte Durchläufe, wiederholte lineare Suche, wiederholte I/O-Aufrufe, verzweigte Rekursion und mehrfach berechnete Teilprobleme sind Prüfsignale. Begrenztes O(n²) darf begründet bestehen bleiben; asymptotische Verbesserung rechtfertigt keine beliebige Komplexität oder Speicherkosten. Passende bestehende Caches werden über ihren kanonischen Zugriff verwendet, unter Beachtung von Schlüsseln, Kontext-/Mandantengrenzen, Lebensdauer und Invalidierung. Ungeeignete Caches werden nicht erzwungen. Vor einem neuen Cache werden algorithmische Vereinfachung, geeignete Datenstrukturen und vermiedene Doppelarbeit geprüft. Ein Cache-Vorschlag erklärt konkreten Nutzen, Speicherbedarf, Gültigkeit, Invalidierung und Alternative. Ohne bestehende konkrete Autorisierung entscheidet der Nutzer vor dem Einbau; nur davon abhängige Arbeit wartet. Ein lokaler Index oder ein Set für einen einzelnen Durchlauf ohne zusätzliche Gültigkeits-/Invalidierungsregeln ist eine gewöhnliche Implementierungswahl. Ein neuer wiederverwendeter Ergebnisspeicher mit eigenen Gültigkeitsregeln fällt unter die Cache-Entscheidung, auch wenn er nur aufruflokal lebt. Materiale Änderungen bestehender Cache-Verträge folgen weiterhin den vorhandenen Entscheidungs- und Risikoregeln. Gezielte Prüffälle decken ab: große verschachtelte Suche mit günstigerer Alternative; kleiner begrenzter quadratischer Durchlauf; verzweigte Rekursion; korrekter und ungeeigneter vorhandener Cache; sinnvoller neuer Cache ohne sowie mit konkreter Nutzerfreigabe; lokaler Suchindex ohne Rückfrage. Erwartet werden Kostenprüfung vor und nach Umsetzung, passende Wahl und korrekte Autorisierungsgrenze. Nachweise unterscheiden Textprüfung, Strukturprüfung und tatsächlich beobachtetes Modellverhalten. Relevante unklare Kosten werden gezielt gemessen; keine universelle Benchmarkreihe. Bei geänderter Cache-Nutzung werden Aktualität und Kontexttrennung geprüft.
Steps:
1. [status: done] Vor Umsetzung aktuellen Quellenstand und uncommittierte Änderungen sichern. In `members/scoville-code/scoville-code/references/change-workflow.md` bei „Implement for the outcome“ die Kosten- und Wiederverwendungsregel ergänzen und bei „Review implementation“ auf deren erneute Anwendung verweisen.
2. [status: done] In `members/scoville-code/scoville-code/SKILL.md` unter „Resolve material choices“ die Cache-Entscheidungsgrenze mit bestehender Autorisierung und unabhängiger Weiterarbeit verankern. Risiko bleibt verhaltensbezogen; ein Cache allein eskaliert es nicht.
3. [status: done] In `members/scoville-code/scoville-code/references/validation.md` unter „Select proportional checks“ gezielte Kostennachweise und Cache-Korrektheit einordnen. Keine doppelte Regelpflege und keine Ausweitung bestehender Prüfpflichten ohne konkreten Anlass.
4. [status: done] Gesamte betroffene Anweisungskette gegen Ausgangsstand und Prüffälle lesen, Skill-Struktur validieren und kleine isolierte Verhaltensprüfungen für die geänderten Entscheidungen durchführen. Modell, Fälle, Ergebnisse und Grenzen im Umsetzungsnachweis festhalten; fehlende Modellbelege nicht als Erfolg ausweisen. README-Aussagen nur bei betroffener Beschreibung aus `development/readme/scoville-code/` konsistent nachführen; generierte Dateien nur über den Buildpfad ändern.
Evidence: Luna-Kosten-/Cache-Fälle und ausführbare Checks bestanden; Metadaten geprüft. Kein Performancevergleich behauptet.

### W-002 Native Ask-Ergebnisse nach Warte-Timeout vollständig abholen

Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: Der aufrufende Chat führt eine beauftragte Ask-Beratung bis zur vollständigen Ergebnisrückgabe fort, auch wenn einzelne Warteaufrufe auslaufen.
Acceptance: Ein Timeout beendet nur den einzelnen wait_threads-Aufruf, nicht die Beratung oder den aufrufenden Turn. Der Aufrufer wartet mit begrenzten ereignisbasierten Aufrufen und dem zurückgegebenen Cursor weiter; keine engen Statusabfragen, Timer, doppelten Adviser oder erneuten Autorisierungsfragen. Explizite Nutzerunterbrechungen und tatsächliche Fehler bleiben wirksam. Vollständige Antworten werden anhand Task-ID, Referenz und Scope zugeordnet und im Aufrufer präsentiert; fehlende oder abgeschnittene Ergebnisse werden gezielt aus demselben Chat gelesen. Rückfragen bleiben im bestehenden Adviser-Chat. Die Frage zur weiteren Nutzung kommt erst nach vollständiger Review-Rückgabe vom Aufrufer. Ein gezielter Test mit mindestens einem Timeout und späterem Adviser-Abschluss belegt die Rückgabe ohne neue Nutzernachricht; mehrere Adviser, Rückfrage und Fehler dürfen nicht als vollständig abgeschlossen erscheinen.
Steps:
1. [status: done] In `members/scoville-ask-for-codex/scoville-ask-for-codex/SKILL.md` und `references/native.md` den Widerspruch zwischen vollständiger Sammlung, Pollingverbot und Turn-Ende nach Timeout beseitigen. Begrenztes ereignisbasiertes Warten ausdrücklich von engem Status-Polling unterscheiden. Vorhandene parallele Änderungen erhalten.
2. [status: done] `references/native-delivery.md`, `scripts/build_adviser_prompt.py` und betroffene Tests auf Konsistenz prüfen. Adviser liefert weiterhin seine vollständige finale Antwort im eigenen Chat; der Aufrufer besitzt die Abholung. Keine zusätzliche Callback- oder Autorisierungsarchitektur einführen. Betroffene README-Aussagen nur an ihren kanonischen Quellen anpassen.
3. [status: done] Den beobachteten Ablauf mit kurzem erstem Timeout und späterer Antwort gezielt nachstellen. Nachweisen, dass der Aufrufer aktiv bleibt, das vollständige Review abholt und präsentiert und erst danach die Abschlussfrage stellt. Tatsächliche Beobachtung von reiner Text-/Helperprüfung unterscheiden.
Evidence: Nativer Timeout mit Cursor fortgesetzt und Review vollständig abgeholt; Luna-Szenarien und Metadatenkorrektur geprüft. Separate README-Testabweichung blieb ausgewiesen.
