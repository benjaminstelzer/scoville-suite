# PLAN-0014 W-015: finale Ask-Titelprüfung

ADR-0095 gibt die zuvor zurückgestellte Änderung frei. Kanonische Titelregel
und README-Fragment wurden geändert und der Codex-Build neu erzeugt.
Paketprüfung und alle 18 bestehenden Ask-Tests bestehen.

Snapshot: Workspace temp/2026-09-26-private-helper-tests/candidate-ask-titles.
Nativer SOL-Chat: 01a0dd06-62d1-7891-8b25-b3c8f636f6ea.
Referenz: plan14-ask-title-final-sol.

Der gebaute ask.py lieferte gpt-6-sol / medium; create_thread verwendete diese
technischen Werte unverändert. Angeforderte Werte sind durch den Toolaufruf
belegt; unabhängige Modelltelemetrie wurde nicht erhoben.

SOL prüfte native.md, die erzeugte README und seinen tatsächlichen Titel per
read_thread: S-ASK GPT-6-SOL - Plan überprüfen. Kein Befund. Die vollständige
Antwort kam per nativer Nachricht vom gespeicherten Chat mit passender Referenz
und Scope zurück. Der Caller hat sie übernommen.

Die Anzeige schreibt nur die Modell-ID groß. Technische Modellwerte bleiben
unverändert; bestehende Chats wurden nicht umbenannt. Die Quellen erhalten
Follow-up-Identitäten. Eine bestehende Follow-up-Kette wurde in diesem gezielten
Titeltest nicht erneut ausgeführt. Die vorherigen Ablaufprüfungen bleiben in
suite-simplification-comparison.md dokumentiert.

Der vollständige Astra-Medium-Schlussreview unter W-018 ist mit seinen
Korrekturen und Nachprüfungen in astra-final-review.md abgeschlossen.
