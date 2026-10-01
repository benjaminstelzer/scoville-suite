---
format_version: 1
id: PLAN-0027
status: completed
created: 2026-10-01
updated: 2026-10-01
---

# Optionalen Stepstatus für Plan und Viewer einführen

## Goal

Agenten und Viewer erkennen geschriebenen Stepfortschritt direkt, ohne alte
Pläne umzudeuten. Vor Umsetzung prüft Astra Medium diesen Plan. ADR-0129 hält
Kompatibilität, Zuständigkeit und Statussemantik fest. ADR-0130 ersetzt Next action
für neue Arbeit durch verpflichtende Steps. ADR-0131 ergänzt optionale zusätzliche Instructions und bewahrt alte Rückkehrhinweise. Luna Medium prüft den gebauten Skill
mit echten Helpern und beobachteter Step-Progression.

## Non-goals

Keine automatische Bestandsmigration, zusätzlichen Statusdateien, Step-Abhängigkeiten,
Installation, Veröffentlichung oder Commits. Keine Änderung fremder laufender Arbeit.
PLAN-0026 läuft im Chat „Scoville Workflow“ weiter. Umsetzung zunächst in isolierter
Kopie; Übernahme erst nach Abgleich und Schreibruhe, ohne dessen Index umzuschalten.

## Work items

### W-001 Plan und Agenten nutzen ausdrücklich geschriebenen Stepstatus

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0129, ADR-0130, ADR-0131]
Outcome: Optionale Statusannotation und bestehende Steps sind durch Anleitung, Validator, Selector und Workflow einheitlich nutzbar.
Acceptance: Alte und gemischte Listen einschließlich Work Items ohne Steps und mit Legacy-Next-action bleiben gültig. Neue Work Items haben immer mindestens einen markierten Step und kein Next action; neue Formen ohne dieses Feld validieren. Nur geschriebene todo/in_progress/done/cancelled werden ausgewertet; fehlender Status bleibt unbekannt. Route-/Execute-Annotationen, Stepnummern, Gruppen und LF/CRLF bleiben erhalten. Fehler nennen Step, erlaubte Form und Korrektur. Selector-Ausgabe erreicht den echten Dispatch-Builder unverändert. Aufträge unterscheiden Restarbeit von Kontext und erhalten Review/Korrektur an erledigten Steps. Instructions ist optionaler Zusatzkontext, fehlend bleibt von [] unterscheidbar. Helper liefert pausierte Rückkehrkontexte und verknüpfte offene ADRs ohne Freitextinterpretation. Plan bleibt alleinige Fortschrittsquelle, Work-Item-Abnahme unverändert. Positionsmodus liefert keine geratenen Steps und benennt nötigen Evidence-/Resultatabgleich; mehrere aktive Gruppen, unbekannte Lücken, Pause/Blocker und all-Steps-terminal ohne Work-Item-Abnahme bleiben erkennbar. Luna Medium nutzt die gebauten Helper zur Auswahl, ungültigem/korrigiertem Aufruf, Fortschritt, Wiederaufnahme und Neuerstellung mit nur einem Step. Fokussierte Tests und betroffene Paketverträge einschließlich General-Fallbacks/Codex-ohne-Fallback bestehen.
Instructions: []
Steps:
1. [status: done] Astra-Medium-Review sichern und belegte Planbefunde korrigieren. In isolierter Arbeitskopie PLAN-0027 aktivieren; kanonischen PLAN-0026 und Index des parallelen Chats unverändert lassen.
2. [status: done] In members/scoville-plan/scoville-plan die optionale erste Annotation [status: VALUE] vor route/execute definieren; Validator und Selector einschließlich --plan PLAN-NNNN --position erweitern: aktuelles W-Item, geschriebene aktive Steps und bei unmarkierter Restarbeit konkrete Anweisung zum Evidence-/Resultatabgleich. Bestehende Modi bleiben gültig; General-Fallbacks spiegeln jeden Modus, Codex enthält keine Fallbacks.
3. [status: done] Neue Work Items stets mit mindestens einem Step und ohne Next action schreiben; neue Leser/Helper akzeptieren das fehlende Legacy-Feld. Astra Medium prüft ADR-0130 und die ergänzte Auswahl-/Kompatibilitätslogik vor Umsetzung. Planpflege, Wiederaufnahme und members/scoville-workflow-for-codex-Aufträge anpassen; neue Steps markieren, alte nur bei belegtem Stand ergänzen, erledigte/entfallene Arbeit nicht automatisch wieder ausführen.
4. [status: done] Alte, neue und gemischte Profile mit tatsächlichem Selector und Dispatch-Builder prüfen: normale Ausführung mit unbekannten/erledigten Steps, Review und gezielte Korrektur eines done-Steps sowie Fortsetzung einer gemischten Gruppe. Dokumentation und Paketverträge abgleichen. Luna Medium danach mit dem gebauten Skill und isolierten Rohaufgaben auf Helper-Verwendung, neue Ein-Step-Planpunkte und Step-Progression prüfen.
Evidence: Astra berücksichtigt; 91 Plan-/49 Workflowtests und Luna-Helperläufe bestanden. Siehe docs/plan0027-implementation-evidence.md.

### W-002 Der Viewer zeigt Stepfortschritt und Wiedereinstieg

Status: done
Depends on: [W-001]
Blocked by: []
Decisions: [ADR-0129, ADR-0130, ADR-0131]
Outcome: Der lesende Viewer zeigt geschriebenen Stepstatus, aktive Steps und gemischte Bestandslisten verständlich an.
Acceptance: Rust-Reader und Svelte zeigen jeden vorhandenen Stepstatus mit Icon und zugänglicher Bezeichnung. Statuslose Steps behalten ihren Text und einen leeren Iconplatz bei identischer Einrückung. Schriftstärke und Textfarbe bleiben einheitlich; nur cancelled ist grau/durchgestrichen. Zahl, Icon und erste Textzeile liegen auf gleicher Höhe. Statusbezeichnungen werden mit mittlerem Punkt getrennt. Done erhält Haken, cancelled X und Durchstreichung. Übersicht nennt belegte erledigte Steps und aktive Stepgruppe ohne unbekannte Steps als offen/erledigt zu zählen. Pausiert/Blocked bleibt Work-Item-Kontext. Grüne Felder heißen Next step und zeigen allein die deterministisch ausgewählten geschriebenen Steps; bei fehlendem Stepstatus verborgen, keine Legacy-Next-action-Anzeige. Gruppen/Lücken und ausstehende Abnahme dürfen keine falsche aktuelle Aktion erzeugen. Instructions und offene verknüpfte Decisions erscheinen separat; fehlende/leere Instructions erzeugen keinen Auftrag. Reader-Tests, Svelte-Prüfung und Build bestehen. Reale gerenderte Prüfung deckt Altformat, Mischliste, Gruppe, Pause/Blockierung, lange Texte und schmale Breite ab; Screenshots und Messungen werden gesichert. Vollständiges Planprofil validiert; Kanonischer PLAN-0026 und sein Index bleiben während des fremden Laufs unverändert.
Instructions: []
Steps:
1. [status: done] members/scoville-plan/development/viewer/src-tauri/src/reader.rs und src/lib/types.ts um optionale strukturierte Stepstatusdaten ergänzen; Text und Nummerierung erhalten.
2. [status: done] In src/App.svelte und src/app.css Next action durch aus geschriebenem Status ermitteltes Next step ersetzen; Altpläne ohne Stepstatus zeigen kein grünes Feld. Vorhandene Statusicons und Tokens nutzen. Nur ausdrücklich markierte aktive Steps anzeigen; ausschließlich lückenlose aktive Bereiche zusammenfassen. Arbeitsbeginn, auch gemeinsamer Gruppenbeginn, wird tatsächlich festgestellt; Zuweisung allein setzt keinen Status. Demo um gemischte und getrennte aktive Steps ergänzen.
3. [status: done] Reader-Tests, npm run check und npm run build ausführen; betroffene Anzeige im Browser rendern, bedienen, messen und ansehen.
4. [status: done] Viewer-Nachweise sichern und Gesamtdiff gegen den gesicherten Ausgangsstand prüfen.
Evidence: 16 Reader-Tests, Svelte/Build und Browserprüfung bei 1440/390 px bestanden. Siehe docs/plan0027-implementation-evidence.md.

### W-003 Planprüfung korrigiert belegten Fortschritt nachträglich

Status: done
Depends on: [W-001]
Blocked by: []
Decisions: [ADR-0129, ADR-0130, ADR-0131, ADR-0127, ADR-0128]
Outcome: Auf „Überprüfe und korrigiere den Plan“ gleicht der Agent Work Items und Steps mit ihren Nachweisen ab und trägt fehlenden Fortschritt korrekt nach.
Acceptance: Ein kurzer bedingt geladener Prüfablauf behandelt alte Steps ohne Status, vergessene Fortschrittsupdates, Abbruch, Fehler und widersprüchliche Nachweise. Evidence, relevante Originalnachweise und bei Lücken aufgabenspezifische Arbeitsresultate tragen die Bewertung; Work-Item-done erfordert beobachtete vollständige Acceptance samt fälligem Review. Fehlende Nachweise bleiben Lücken, Abbruch ist kein cancelled und Erfolg eines Teilchecks kein Gesamtabschluss. Der Ablauf erhält historische Abnahme, Scope, Reihenfolge und belegte Effekte, migriert bewiesene Fortschritte und bewahrt Zusatzbedingungen aus Legacy-Next-action/Evidence in Instructions, ohne unklare Historie zu erfinden; korrigiert nur sicher bestimmbaren Fortschritt und Evidence und validiert atomare Plan-/Index-Übergänge. Luna Medium prüft die beauftragte Reparatur, reine lesende Prüfung und Wiederaufnahme getrennt. Tests prüfen typische Reparaturprofile durch echten Validator und Selector. Anwenderdokumentation und Paketprüfung decken den Aufruf ab. Das vollständige Suite-Planprofil bleibt gültig.
Instructions: []
Steps:
1. [status: done] Im Überprüfen-/Reparatur-Routing auf eigene kompakte references/repair.md in members/scoville-plan/scoville-plan verweisen; nur diese Route lädt den Ablauf, normale Pflege/Wiederaufnahme nicht. Reine lesende Prüfung von Korrekturauftrag unterscheiden.
2. [status: done] Nachweiskriterien für Steps und ganze Work Items festlegen; bei unzureichender Evidence die aufgabenspezifischen Arbeitsresultate gegen Anforderungen prüfen, etwa Code/Tests oder Texte/Dokumente. Nötige gezielte Checks ausführen; bloße Existenz beweist keine Abnahme.
3. [status: done] Altplan-Nachtrag, Code-/Textresultate, Teilabschluss, Fehler/Abbruch und fehlende/widersprüchliche Evidence prüfen. Überprüfen mit/ohne Korrektur lädt repair.md; normale Pflege/Wiederaufnahme nicht. Resultate werden geprüft, nicht umgeschrieben. Kanonische Dokumentation und Exporte abgleichen.
4. [status: done] Nach Schreibruhe gegen aktuelle kanonische Quellen abgleichen und nur autorisierte Änderungen übernehmen. Gesamtnachweise sichern und PLAN-0027 über konsistente Lifecycle-Übergänge abschließen; fremden Laufstand erhalten.
Evidence: Reparatur/Migration und kanonische Übernahme geprüft; fremder Laufstand erhalten. Siehe docs/plan0027-implementation-evidence.md.
