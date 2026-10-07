---
format_version: 1
id: PLAN-0029
status: completed
created: 2026-10-01
updated: 2026-10-01
---

# Ask und Workflow gezielt vereinfachen

## Goal

Ask, Workflow, Code, Project Context Cleanup, UI und die betroffenen Plan-Regeln wieder schlank, einfach und funktionsfähig machen. Unnötige Absicherungen, selten benötigte Sonderwege und doppelte Koordination vereinfachen. Weniger geladener Text und verzichtbare Schritte sollen Tokenverbrauch und Laufzeit senken. Der Nutzer entfernt den automatischen Kapazitäts-Workaround nach ADR-0135; Ergebnisse, echte Folgefragen und Fortsetzungsstand bleiben erhalten. Die unabhängigen Astra-High-Reviews begründen den Fixplan. Astra High prüft Plan und fertig geänderte Skills; der abschließende Luna-Medium-Verlauf prüft ihre echte Zusammenarbeit.

## Non-goals

Keine Ausführung von Scoville Workflow in diesem Chat und keine neuen Sidebar-Chats außer dem nach ADR-0134 autorisierten Testchat. Keine vorbeugenden Bereinigungsturns oder neuen Cleanup-Kandidatenklassen. Kein späteres Nachtragen als Ersatz für aktuellen Step-Fortschritt, keine Änderung der alleinigen Planpflege durch den Manager, kein Wegfall offener Bedingungen. Kein Funktionsverlust, durcheinandergebrachter Ablauf, Verlust von Arbeitsschritten oder unmögliche Planwiederaufnahme. Keine feste Textgrößengrenze und kein Token-/Laufzeitgewinn allein aus Dateigrößen behaupten. Release-Schritte sind vom Astra-Review ausgeschlossen.

## Work items

### W-001 Ask beendet Beratungen ohne überflüssige Rückfragen und Startmeldungen

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0132]
Outcome: Vollständige native Antworten werden ohne Startbestätigung akzeptiert; Claude-Reviews erzeugen keine Abschlussfrage oder automatische Schließung bei Themenwechsel.
Acceptance: Native Handle und letzter Auftrag identifizieren die vollständige finale Antwort. Fehlende/unvollständige Finals bleiben offen; unklare Spawns erhalten keinen Retry. Inhaltliche Referenz-/Scope-Konflikte werden geklärt, bloße Labels dürfen aus dem erhaltenen Auftrag eindeutig zugeordnet werden. Angeforderte und tatsächliche Modellangaben bleiben getrennt. Claude-ID, Einstellungen und Nachweise bleiben beim Ergebnis, Wiederaufnahme nur auf ausdrücklichen Auftrag. Alle widersprechenden Skill-, Delivery-, Claude- und README-Regeln sind angepasst. Der tatsächliche native Verbraucher und autorisierter Claude-Follow-up sind geprüft; ungetestete Routen sind benannt.
Instructions: []
Steps:
1. [status: done] Veraltete Start-/Abschlussregeln und Referenzen im kanonischen Ask ändern.
2. [status: done] Promptverbraucher, vollständige/fehlende Finals, erneute Frage an denselben Handle und Claude-ID-Follow-up prüfen.
3. [status: done] Betroffene Pakete bauen und die Korrekturen für den gemeinsamen abschließenden Skill-Review bereitstellen.
Evidence: 35 Ask-Tests und zwei echte Luna-Medium-Finals ohne Startcallback, zweites am selben Handle. Reale Claude-CLI ungeprüft. temp/2026-10-01-workflow-plan-state/lean-ask-consumer.json.

### W-002 Ask und Workflow besitzen einen gemeinsamen Kapazitätsvertrag

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0126, ADR-0132]
Outcome: Gemeinsame Recovery-Regeln haben eine kanonische Pflegestelle; kurze lokale Rollenregeln bewahren das bisherige Verhalten.
Acceptance: Quelle liegt unter shared/runtime und wird im Build in beide selbstständig installierbaren Skills übernommen. Nur eindeutige Kapazitätsablehnung ohne erzeugten Agenten erlaubt eine Runde und einen Retry mit identischen Argumenten. Eigene exakte Handles, letzter vollständig erledigter Auftrag, vollständiges Ergebnis/übernommene Übergabe, bestätigtes natives Ende, aktueller completed-Status und keine offene/unklare Folgezustellung begrenzen Kandidaten. Ask verwendet abgeschlossene eigene Berater; Workflow ausschließlich vom Runner übergebene alte Manager. Neue CAPACITY_RECOVERY_DONE-Finals werden einzeln geprüft, gesamte Runde bleibt auf 60 Sekunden begrenzt. STOP, Fehlschlag und Unsicherheit sperren Retry; Antworten und Handles bleiben erhalten. Keine Routine-ACKs oder zusätzlichen normalen Cleanup-Turns. Beide gebauten Verbraucher funktionieren ohne Zugriff auf eine Nachbarinstallation.
Instructions: []
Steps:
1. [status: done] Gemeinsamen Kern aus den bestehenden Regeln ableiten und Rollenadapter belassen.
2. [status: done] Manifest-/Build-Ziele registrieren, Pakete bauen und tatsächlich geladene Texte prüfen.
3. [status: done] Eindeutige Ablehnung, fehlender Kandidat, pausierter Auftrag, offene Folgefrage, fehlgeschlagene Bereinigung, STOP und unklarer Spawn prüfen.
Evidence: Beide Codex-Pakete gebaut und geprüft; Szenarien und Hostgrenze: temp/2026-10-01-plan-0029/w2-capacity-check.md. Nativer Ablehnungs-/Retry-Nachweis offen für W-006.

### W-003 Workflow korreliert Kapazitätswiederherstellung mit weniger Protokolltext

Status: done
Depends on: [W-002]
Blocked by: []
Decisions: [ADR-0126]
Outcome: Der Manager erreicht die berechtigten alten Manager weiterhin über den Runner, ohne separaten Versuchszähler und doppelte Regelbeschreibungen.
Acceptance: Ein vorhandener eindeutiger Assignment-/Taskname ordnet Anfrage und Ergebnis dem exakt abgelehnten Spawn zu. Die verbrauchte Recovery-/Retry-Möglichkeit bleibt erhalten, auch über verspätete oder doppelte Nachrichten, STOP/Resume und Rollover. Eine Anfrage und eine zugeordnete Ergebnisantwort ersetzen wiederholte Nachrichtenfamilien, ohne bei einem Childspawn die Recovery durch den Runner zu verlieren. Keine Erfolgsfreigabe aus alten Ergebnissen und kein Retry bei unbekanntem Start. Zuerst Text-/Zustandsänderung gegen den bestehenden Ablauf prüfen, dann minimal umsetzen.
Instructions: []
Steps:
1. [status: done] Bestehende Token/Zähler durch einen vollständigen Zuordnungsvertrag mit vorhandenem Assignment-ID ersetzen.
2. [status: done] Manager-/Runner-Anweisungen und Rückwege zusammen ändern.
3. [status: done] Tatsächliche Verbraucher mit doppelten, verspäteten und falschen Antworten sowie STOP/Resume prüfen.
Evidence: Luna-Medium-Verbraucher prüfte acht Kontrollfälle und bestätigte zwei Korrekturen; temp/2026-10-01-plan-0029/w3-consumer-check.md. Nativer Hostlauf bleibt W-006.

### W-004 Vereinfachte Managerübergabe hat eine belastbare Designentscheidung

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0126]
Outcome: Ein geprüfter Vergleich entscheidet, ob eine dauerhafte Übergabedatei den aktuellen Managerdialog sinnvoll ersetzt.
Acceptance: Der Entwurf enthält echten Auftrag, Scope, Plan-/Dateistand, offene Fragen/Auflösungen, Berichtpfad und bekannte Kinder. Speichern und Vorgängerabschluss kommen vor Nachfolger-Schreibfreigabe; der Nachfolger prüft Datei und kanonischen Zustand. STOP während Übergabe, fehlende/partielle Datei, ungeklärte Wirkung und unklarer Spawn sind abgedeckt. Der Entwurf berücksichtigt den Zuordnungs-/Recovery-Vertrag aus W-003, ohne dessen Umsetzung vorauszusetzen. Kontrollnachrichten, normale Zusatzturns und geladenen Rollentext mit dem bestehenden Ablauf vergleichen. Kein Kapazitätsgewinn wird aus weniger Nachrichten allein abgeleitet. Design und begründete Entscheidung erhalten Astra High; eine Implementierung wird erst mit festgelegtem Vertrag als eigener Planpunkt hinzugefügt.
Instructions: []
Steps:
1. [status: done] Dateibasierte Übergabe und bestehenden Ablauf anhand derselben Fehler-/Fortsetzungsfälle vergleichen.
2. [status: done] Astra High bewertet den konkreten Entwurf und die Mess-/Nachweisgrenzen.
3. [status: done] Entscheidung festhalten und nur bei bestätigter Verbesserung einen Implementierungspunkt mit vollständiger Acceptance ergänzen.
Evidence: Astra High empfiehlt direkten Weg; Dateientwurf hat ungeklärte Übergangs-/Reparaturzustände, kein gemessener Gewinn. temp/2026-10-01-plan-0029/w4-handoff-design.md.

### W-005 Anzeige- und Fortschrittsregeln sind kürzer und eindeutig

Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: Workflow und Plan erklären Anzeige, Scope und Fortschrittszustände ohne unnötige Wiederholung.
Acceptance: Rein sprachliche Anzeigeabweichung wird aus dem erhaltenen autorisierten Scope korrigiert; ein inhaltlicher Auftragskonflikt bleibt vor Ausführung zu klären. Die Anzeige benennt korrekt Projekt, Plan und tatsächlichen Punkt; sie bleibt auf Punktwechsel begrenzt. Der letzte Anzeigeschlüssel überlebt Resume und Übergabe, SC-WFL-Titel folgt bestätigter Plan-ID. Work-Status beschreibt Gesamtzustand, Step-Status tatsächlichen Fortschritt, Instructions zusätzliche bindende Bedingungen; Next action bleibt nur Legacy. Aktive Steps, progress_pending, akzeptierter Abschluss und geeigneter Nachfolger bleiben korrekt. Veraltete Migrationsregeln werden nur bei Reparatur geladen. Wirkungslose pin_threads-Vorgaben nur dann aus neuer Standardausgabe entfernen, wenn bestehende Konfiguration weiterhin lesbar bleibt. Jede verbleibende Sonderregel nennt ihren konkreten relevanten Fehler und dessen Folge; unnötige Wiederholungen und Absicherungen werden entfernt oder in den seltenen Ladepfad verschoben. Kürzung misst geladenen Rollentext und bewahrt Verhalten; keine bytebasierte Freigabe.
Instructions: []
Steps:
1. [status: done] Kosmetische Anzeigeabweichung von inhaltlicher Scope-Unklarheit abgrenzen.
2. [status: done] Titel- und Fortschrittsbeschreibung verdichten, ohne Regeln oder offene Bedingungen zu verlieren.
3. [status: done] Kontextlast pro Rolle und aktuelle Step-/Pause-/Resume-Verbraucher prüfen.
Evidence: 41 fokussierte Tests, Paket-/Profilprüfung; geladene Texte -216 Zeichen, keine Tokenbehauptung. temp/2026-10-01-plan-0029/w5-progress-check.md.

### W-007 Code trifft Routing- und Prüfentscheidungen mit weniger Text

Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: Code lädt die nötigen Referenzen mit einem kompakten Vertrag; Risiko erzeugt gezielte Prüfung statt unbeauftragter Vollgates.
Acceptance: Routingtabelle, tatsächlich autorisierte Handlung und kombinierte benötigte Referenzen bleiben eindeutig. Der Harden-Widerspruch zu Validation ist beseitigt: breite Gates benötigen die passende Abschlussentscheidung oder bindende Projektregel. Erst danach identisch behandelte Risikoetiketten zusammenfassen; konkrete Fehlerfolgen und bestehende Autorisierung bleiben erhalten. Die gemeinsame Risikostufe erhält den bisherigen Change-Override auch bei reiner Klassifikation; Referenzlektüre erweitert keine Handlungsbefugnis. Einmalige bewusste Inhaltsprüfung eigener Änderungen bleibt, bereits geprüfte unveränderte Inhalte werden nicht erneut gelesen; generierte Mengen werden am Quellbesitzer und relevanten Ausgaben geprüft. Aufgeschobene riskante Arbeit aktiviert keine Implementierung.
Instructions: []
Steps:
1. [status: done] Code-Routing und Harden/Validation-Vertrag zusammen vereinfachen.
2. [status: done] Gleichwertige Risikobehandlung und abschließende Inhaltsprüfung verdichten.
3. [status: done] Betroffene Klassifikations-/Verbraucherfälle prüfen und für W-006 bereitstellen.
Evidence: Codex-Paket geprüft; Luna-Medium-Verbraucher klassifizierte sechs Fälle, natürliche Ausführung bleibt W-006. temp/2026-10-01-plan-0029/w7-code-consumer.md.

### W-008 Diagnose kann angemessen reproduzieren, ohne Produktänderung

Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: Auftragsbezogene lokale reversible Checks sind bei Diagnose/Review erlaubt; unerlaubte Wirkungen bleiben ausgeschlossen.
Acceptance: Bekannte begrenzte Wirkungen und entbehrliche Testausgaben entscheiden, nicht bloß ein ignorierter Ordner. Lokale Reproduktion benötigt keine weitere Freigabe. Explizites Ausführungsverbot sowie nicht autorisierte dauerhafte/externe Wirkung sperren den betroffenen Check. Diagnose repariert keine Produktdateien. Die Regel stimmt mit gezielter Validation und Hostgrenzen überein; keine neue allgemeine Prüf- oder Genehmigungsrunde.
Instructions: []
Steps:
1. [status: done] Read-only-Formulierung um klar begrenzte Reproduktion ergänzen.
2. [status: done] Natürliche Diagnose sowie verbotenen/extern wirkenden Gegenfall für Luna testen.
Evidence: Luna-Medium reproduzierte CSV-Fehler lokal; zwei Gegenfälle führten Upload nicht aus. Paketprüfung: temp/2026-10-01-plan-0029/w8-diagnosis-check.md.

### W-009 Neue Code-Projekte sind eingerichtet, prüfbar und fortsetzbar

Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: Greenfield-Arbeit hat eine passende Zielruntime, nutzbare Befehle und kurze Dokumentation ohne zusätzliche Frameworkpflicht.
Acceptance: Zielruntime und kompatible Abhängigkeiten kommen aus dem Auftrag und belastbaren Quellen, nicht allein aus der lokal installierten Version. Passender offizieller Initializer ist eine Option; Lockfile/Pinning folgt dem Ökosystem. Neue direkte Paketidentität wird aus offizieller Projektdokumentation und vorgesehener Quelle geklärt, vorhandener Nachweis wiederverwendet. Vorhandene/native Prüfmöglichkeiten gehen vor neuem Testframework; nur ein angemessener nötiger Prüfbefehl wird eingerichtet. Das vorhandene oder bei Bedarf neue README dokumentiert erforderliche Voraussetzungen sowie passende Einrichtungs-, Nutzungs-/Start- und Prüfbefehle. Betroffene Vertrauensgrenzen werden bis zur gefährlichen Operation verfolgt und mit sicheren Schnittstellen behandelt; externe Daten lösen nicht pauschal High aus. Bestandsorganisation und rein lokale technische Anforderungen neuer Teilmodule bleiben erhalten.
Instructions: []
Steps:
1. [status: done] Greenfield-Einrichtung, Prüfung und README am bestehenden Regelbesitzer präzisieren.
2. [status: done] Paketidentität und konkret betroffene Vertrauensgrenze knapp ergänzen.
3. [status: done] Neues Projekt, frischen README-Verbraucher und Bestands-Teilmodul für W-006 vorbereiten.
Evidence: General-/Codex-Pakete geprüft, drei Luna-Aufträge und unabhängige Kriterien vorbereitet. temp/2026-10-01-plan-0029/w9-greenfield-check.md.

### W-010 Context Cleanup hat eindeutige Ziele auch bei fehlenden Dateien

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0119]
Outcome: Projektregel- und Indexaufträge nutzen den richtigen Owner ohne unnötige Frage oder parallelen Regelbestand.
Acceptance: Bei eindeutigem projektweitem Regelauftrag darf fehlende AGENTS.md am geklärten Projektroot entstehen; vorhandene zuständige Host-/Teilbaumregeln bleiben berücksichtigt. Native Indexpflege verwendet Plans passenden Bearbeitungsweg im selben Edit, dessen Validator bleibt bei Plan. Fehlender Index folgt dem geklärten Auftrag: Scoville-Profil über Plan, explizit freies Format bleibt erlaubt; nur materielle Format-/Zielunklarheit erzeugt eine Frage. Kein Planprofil allein wegen eines Indextextauftrags initialisieren; keine unbeauftragte Migration oder generelle Hostadapter-Erweiterung. README-Aussagen stimmen mit diesen Grenzen überein.
Instructions: []
Steps:
1. [status: done] Zielwahl und fehlende Dateien in Cleanup knapp klären.
2. [status: done] Nativen Planweg, fremden Index und vorhandene andere Regeldatei abgrenzen.
3. [status: done] Natürliche Greenfield-/Index-/Negativfälle für W-006 vorbereiten.
Evidence: README aus Quelle gebaut; beide Pakete und native Testprofil geprüft; Luna-Fälle vorbereitet. temp/2026-10-01-plan-0029/w10-target-check.md.

### W-011 Cleanup entfernt Ballast nachvollziehbar ohne Bedeutungsverlust

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0119]
Outcome: Gezielte Bereinigung erhält nötige eigenständige Regeln und berichtet relevante Entfernungen knapp.
Acceptance: Quellenlektüre darf konkrete Veraltung prüfen, ohne pauschale Bestandsaufnahme oder Ausführung gefundener Befehle. Wiederholung bleibt, wenn eigenständige Verwendung sie braucht. Lange Verfahren nutzen geeignete vorhandene Referenzen; neue Datei nur bei vom Auftrag gedeckter Auslagerung, sonst Text vollständig zusammenlassen. Bericht nennt inhaltlich relevante Entfernung mit kurzem Grund, ohne vollständiges Löschprotokoll oder neue Freigabe. Ausnahmen, Scope, Bedingungen und Regeln, deren Veraltung nicht belegt ist, bleiben erhalten; passender Text bleibt bei Wiederholung gleich.
Instructions: []
Steps:
1. [status: done] Evidenzlektüre, Auslagerung und eigenständige Regelkopien im vorhandenen Vertrag klären.
2. [status: done] Entfernungsbericht ergänzen und realistisch gewachsene Bereinigungsfälle vorbereiten.
Evidence: Pakete geprüft, natürliche Aufgabe vorbereitet: temp/2026-10-01-plan-0029/w11-cleanup-check.md. Luna-Verbraucher folgt W-006.

### W-012 UI-Routing und Regelbesitz sind kompakt und präzise

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0040]
Outcome: UI lädt nur nötige Detailverträge und hat keine mehrfach gepflegten Regeln oder Eval-Ausgabedetails im normalen Router.
Acceptance: Positive Ladebedingungen unterscheiden Implementierung, Eigentümerfrage, Quellenprüfung und Belegprüfung. Quality/Validation werden weder nötigen Fällen entzogen noch reinen Eigentümerfragen pauschal aufgezwungen. Stylingbegründung, Einheiten und Prüfablauf haben einen Detailbesitzer mit kurzen nötigen Verweisen. Strukturierte Ausgabepräzedenz/Enums liegen in classification-output, semantische Routinggrenzen bleiben im Router. Opt-out beendet nur Skillanwendung; vorhandener Ergebnis-/Testbericht genügt für Belege. Ausgeschlossene WordPress-Flächen bleiben hostgeführt und nicht automatisch allgemein unterstützt. Versionsgrenzen bleiben erhalten; WordPress 7.2 wird nicht ungeprüft bestätigt.
Instructions: []
Steps:
1. [status: done] UI-Ladebedingungen und Detailbesitz zusammen vereinfachen.
2. [status: done] Ausgabeformatdetails aus dem Normalrouter auslagern, Opt-out/record präzisieren.
3. [status: done] Betroffene Routing-/Nachweisklassifikationen für W-006 prüfen.
Evidence: Beide Pakete geprüft, fünf natürliche Fälle vorbereitet: temp/2026-10-01-plan-0029/w12-ui-routing-check.md. Luna-Verbraucher folgt W-006.

### W-013 UI-Prüfumfang und Greenfield haben klare kleine Verträge

Status: done
Depends on: [W-012]
Blocked by: []
Decisions: [ADR-0040]
Outcome: Neue zusammengehörige Oberflächen und gemeinsame Komponenten werden mit relevantem Render-/Interaktionsnachweis geprüft, ohne pauschale Messmatrix.
Acceptance: Vorab auswählen: relevante Layoutbehauptungen, normative Grenzen und konkrete Risiken. Quelle, erforderliche Messung und Sicht bleiben in dieser Reihenfolge; eigenes neues CSS liefert nachträglich keinen unabhängigen Sollwert. Anforderungen sowie eine vor der Umsetzung aus dem Auftrag abgeleitete Richtung und geeignete gemeinsame Werte können Greenfield-Sollwerte begründen. Mehrere beauftragte Ansichten verwenden diese Werte einmal am passenden Codebesitzer; vorhandene Struktur nutzen, sonst die kleinste gemeinsame Ablage wählen. Kein zusätzliches Tokenregister oder Designsystemprojekt ist erforderlich. Native Semantik und unterstützte vorhandene Primitive gehen vor eigenen Widgets; eigene Composite-Widgets erhalten passende Fokus-/Tastaturprüfung. Unmittelbar mitbetroffene unterschiedliche Nutzungsweisen gemeinsamer Besitzer werden repräsentativ gerendert. Interaktionen nutzen kontrollierte Daten/Ziele, nicht unautorisierte externe Wirkungen. Wenige WCAG-Kontrast-/Reflowwerte bleiben mit ihren tatsächlichen Ausnahmen korrekt; praktische breite Ansicht wird nicht zur Normpflicht. Sprache folgt Produkt/Plattform, nur relevante Unklarheit wird gefragt.
Instructions: []
Steps:
1. [status: done] Begrenzten Messumfang, unabhängige Greenfield-Sollwerte und gemeinsame Besitzer klären.
2. [status: done] Verbraucherprüfung, kontrollierte Interaktion und relevante Semantik-/WCAG-Grenzen knapp ergänzen.
3. [status: done] Zwei kleine reale Ansichten, gemeinsame Komponentenänderung und gezielte Negativfälle für W-006 vorbereiten.
Evidence: Beide Pakete geprüft, Luna-Aufträge vorbereitet: temp/2026-10-01-plan-0029/w13-ui-check.md. Natürliche Ausführung folgt W-006.

### W-006 Abschließender Luna-Medium-Verlauf prüft die vereinfachten Skills vollständig

Status: done
Depends on: [W-001, W-002, W-003, W-004, W-005, W-007, W-008, W-009, W-010, W-011, W-012, W-013]
Blocked by: []
Decisions: [ADR-0126, ADR-0132, ADR-0134, ADR-0135, ADR-0136, ADR-0137]
Outcome: Die am Ende von Astra High geprüften Skills bestehen einen realen End-to-End-Test im Projekt test; Ablauf, Wiederaufnahme und Fortschritt bleiben trotz Vereinfachung verlässlich.
Acceptance: Zuerst prüft Astra High alle geänderten Skills und ihre Zusammenhänge; Findings werden korrigiert und im selben Kontext nachgeprüft. Danach laufen Runner, Manager, Worker, Reworker und Reviewer mit gpt-6-luna/medium über gebaute Pakete im vorhandenen Projekt test. Nur dessen Testkonfiguration verwendet coordinator_percent=15 und worker_percent=15; Produktionsvorgaben bleiben erhalten. Gemessene Schwellenüberschreitungen und kontrollierter Rollover werden tatsächlich beobachtet, Simulation nicht als Kompaktierung oder nativer Wechsel bezeichnet. Abbruch vor Start und während Arbeit, Wiederaufnahme nach Pause und Managerwechsel, Zwischenfragen in unterschiedlichen Phasen und ein begonnener blockierter Punkt mit späterer Freigabe durch einen anderen Punkt werden geprüft. Der Koordinator kehrt zurück und beendet die restliche Arbeit ohne doppelte Ausführung oder vergessene Schritte. Projekt-/Plan-/Punkt-Anzeige und Scope bleiben richtig; notwendige Fragen/Pausen samt Auflösungen stehen im selben gezielten Laufbericht, normale Reviews/Fortschritte erzeugen keine Einträge oder wiederholte Statusausgabe. Auftragsschluss gibt den fertigen Bericht aus; ein problemfreier Kontrolllauf endet mit No issues occurred during this run. Frische unabhängige Ask-Antworten, fehlende Finals und Folgefragen an denselben Handle bleiben korrekt zugeordnet. Zusätzlich laufen natürliche Code-, Cleanup- und UI-Fälle am gebauten Skill. Code: kleine Bestandsänderung gegen unabhängige Consumererwartung; lokale Diagnose und verbotener Gegenfall; neues kleines Projekt mit frischem README-Verbraucher, gültiger/ungültiger Eingabe an einer konkret betroffenen Vertrauensgrenze und vor Installation geklärter Identität einer erstmals benötigten direkten Abhängigkeit; Bestands-Teilmodul; kurze Klassifikation aufgeschobener riskanter Arbeit für den Change-Override. Cleanup: Projektregel im leeren eindeutigen Projekt plus Wiederholung; gewachsene Bereinigung; direkte Pflege eines vollständigen nativen Profils mit Plan-Validator und eines fremden Index; fehlender Index bei explizit freiem Format, gewünschtem Scoville-Plan und materiell unklarem Format; eindeutig zuständige andere Regeldatei ohne parallele AGENTS; Beratung, bloße Dateierwähnung und gewöhnlicher Planfortschritt ohne Cleanup-Aktivierung. UI: zwei kleine zusammengehörige Ansichten über die allgemeine Route ohne vorhandenen visuellen Owner, mit gewünschter ausgearbeiteter Darstellung, realistischem gefülltem Inhalt, breiter Ansicht und relevantem Reflow; gemeinsame Komponentenänderung für zwei unterschiedliche Nutzungsweisen und kontrollierte Fehlerinteraktion. Nach ausdrücklichem Nutzerstopp gemäß ADR-0137 wird die begonnene Linden-Komponentenänderung nicht fortgesetzt oder als bestanden gewertet; W-015 prüft stattdessen den Skill-Defekt am erhaltenen Original read-only. Kurze Gegenfälle prüfen Quellen-/Screenshotbeweis, ausgeschlossene WordPress-Fläche, ungeprüfte Version und bewusste Variantenabweichung. Der Prüfer wertet tatsächliche Referenzlektüre, Checks und Wirkungen aus. Sollkriterien bleiben beim Prüfer; natürliche Aufgaben nennen die Ausgangslage, nicht die zu prüfenden Schutzregeln. Fälle dürfen passend gebündelt werden, keine Kreuzprodukt-Matrix. Nur konkret betroffene Fälle werden nach Korrekturen wiederholt. Nach ADR-0135/0136 ersetzt der Auftrag zur vollständigen Entfernung die frühere Ablehnung-Cleanup-Retry-Akzeptanz: W-014 prüft den neuen Kapazitätsfehlervertrag ohne Bereinigungs-/Retry-Weg. Frühere Recovery-Tests bleiben historische Belege; nicht erzeugbare Hostfehler bleiben ausdrücklich ungetestet. Vorher-/Nachher-Vergleich erfasst geladenen Rollentext, Kontrollnachrichten, zusätzliche Turns, Laufzeit, Nutzereingriffe und tatsächlich verfügbare Tokenmesswerte mit gleicher Szenariobasis. Fehlende Messwerte bleiben unbekannt. Bestätigte Fehler werden automatisch korrigiert; betroffene Fälle und geänderte Quellen werden erneut geprüft. Der Abschluss nennt Funktionsergebnis und Effizienz-Nachweise samt Grenzen. Lokale Skills werden vor einem anschließenden Release installiert und den autorisierten laufenden Sessions mitgeteilt.
Instructions: []
Steps:
1. [status: done] Gesamte geänderte Skills mit Astra High prüfen, Findings korrigieren und denselben Reviewer nachprüfen lassen.
2. [status: done] Projekt test, Referenzmessung, echte Testaufträge und isolierte Luna-/15%-Einstellungen vorbereiten.
3. [status: done] Reale Workflow-Verläufe samt problemfreiem Abschluss und die Code-/Cleanup-/UI-Luna-Fälle ausführen.
4. [status: done] Recovery-Verbraucher und begrenzte Hostprobe prüfen; Simulation, Schwellenbeobachtung und tatsächliche Kompaktierung trennen.
5. [status: done] Fehler korrigieren, betroffene Fälle nachprüfen und Funktions-/Effizienzvergleich mit lokal aktualisierten Paketen abschließen.
Evidence: Serieller Test in test abgeschlossen: 27 native Sessions Luna Medium, maximal 3 parallel; Pakete und Installationen geprüft. Grenzen: temp/2026-10-01-plan-0029/w6-completion-audit.md.

### W-014 Ask und Workflow verzichten auf automatische Kapazitätsbereinigung

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0135, ADR-0136]
Outcome: Kapazitätsfehler bewahren Ergebnisse und Fortsetzungsstand ohne Drain-/Recovery-/Retry-Protokoll oder reine Bereinigungsturns.
Acceptance: Workflow-, Ask- und gemeinsame Runtimequellen, Managerprompt, Registry, Tests und aktuelle Dokumentation enthalten keinen automatischen Kapazitäts-Workaround oder dessen CAPACITY_REQUEST/CAPACITY_RESULT/CAPACITY_RECOVERY_DONE-Zustände. Historische Decisions/Evidence bleiben erhalten. Notwendige Follow-ups, echte Übergabe mit Empfang vor Vorgängerabschluss, offene Finals, Scope und Modelle bleiben korrekt. Kapazitätsfehler bewahren Diagnose, Blocker und exakte Fortsetzung ohne Ersatzchats. Gebaute Pakete und tatsächliche Luna-Medium-Verbraucher prüfen den neuen Vertrag; nicht erzeugte Hostfehler werden nicht als nativ ausgeführt bezeichnet. README empfiehlt 256, lokales Codex-Limit ist auf ausdrücklichen Auftrag erhöht; serielle Testzahl bleibt begrenzt.
Instructions: []
Steps:
1. [status: done] Kanonische Workflow-/Ask-Anbindung, gemeinsame Runtimequelle und nur dafür benötigte Zustände entfernen; Prävention und echte Folgefragen bewahren.
2. [status: done] Betroffene Projektionen erzeugen, technische Gates und gebaute Luna-Medium-Verbraucher seriell prüfen.
Evidence: Entfernung, vier Builds, serielle Luna-Verträge und echter Manager-Startverbraucher geprüft; Hostfehler nicht erzwungen. temp/2026-10-01-plan-0029/w14-removal-check.md.

### W-015 UI-Prüfung erfasst die innere Ausrichtung von Statuskomponenten

Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: Der beobachtete Badge-Fehler wird als Skill-Prüfdefekt behandelt und am bestehenden Validation-Vertrag korrigiert.
Acceptance: Tatsächliche Referenzlektüre, Quellen-, Mess- und Sichtprüfung des fehlgeschlagenen Luna-Laufs sind ausgewertet. Innere Textplatzierung gilt auch für nicht interaktive Statuskomponenten und wird nicht durch reine Overflow-Prüfung ersetzt. Keine pauschale Zentrierung gegen eine bewusste Variante und keine neue Prüfmatrix. Ein serieller Luna-Medium-Audit am gebauten Skill prüft den erhaltenen Fehlerfall ohne Produktreparatur; der erste Fehlbefund bleibt erhalten. Angefangene Fixture-Korrekturen gelten nicht als Skill-Nachweis.
Instructions: []
Steps:
1. [status: done] Fehlgeschlagenen Prüfablauf auswerten und den bestehenden komponentenbezogenen Prüfschritt präzisieren.
2. [status: done] Gebauten Skill im realen Testprojekt seriell read-only prüfen und tatsächliche Fehlererkennung belegen.
Evidence: Luna-Audit erkannte Badge-Drift ohne Produktänderung; ursprüngliche Fixture blieb unverändert.
