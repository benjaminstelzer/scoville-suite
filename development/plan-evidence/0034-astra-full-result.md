# PLAN-0034: unabhängiges Gesamtreview und Korrekturen

Astra wurde über Scoville Ask mit frischem Kontext als gpt-6-astra/high unter
`/root/astra_full_plan0034` beauftragt (PLAN-0034-FULL-ASTRA-1). Tatsächliche
Adviser-Modell-/Effort-Telemetrie war unbekannt. Vollständige Antwort und Dispatch
liegen im privaten Testprojekt als `astra-full-review-final.md` und
`astra-full-review-dispatch.json`. Frühere Review-Urteile wurden nicht gelesen.

Astra fand drei konkrete P2-Befunde und darüber hinaus keinen konkreten Verlust
von Zuständigkeiten, Aktivierungsgrenzen, Profilsemantik oder Schutzregeln im
geprüften Text-/Helper-Diff. Der Adviser meldet 94 bestandene lokale Tests,
aktuelle Payload-Identität aller vier Kandidaten, unveränderte 164 Originalfälle
und 275 identische W-004-Vorher-/Nachher-Hashes. Das ist keine Modellabnahme.

## Bestätigte Korrekturen

1. Der Handoff-Receiver-Test konnte src.export nicht importieren. cases-v9 ergänzt
   den Fixture-Projektpfad für das unveränderte erlaubte Kommando. Der echte
   Testprozess besteht mit richtigem Header und scheitert mit AssertionError bei
   falschem Header; kein Importfehler verdeckt die Fachprüfung.
2. Runner und Gruppierung konnten Fallprompt und Laufbedingungen falsch zuordnen.
   `case_binding.py` bindet die verifizierte Vorbereitung an Datensatzregistrierung,
   Fall, Variante, Receipt und den genau erzeugten Prompt. Der Runner prüft dies
   vor Budgetreservierung. Die Gruppierung prüft den gespeicherten Erstprompt,
   die gefrorene Fallidentität sowie identische Turn- und Zeitlimits. Vorhandene
   Verhaltenfehler werden nur mit bestätigter nativer Identität bewertet.
3. Die Plan-Fixture enthielt keine zu schützenden Ausführungsannotationen.
   cases-v9 enthält nun gültige Route-/Modell-/Effort-Annotationen und führt sie
   explizit als zu bewahrende Werte auf. Das native Plan-Profil ist gültig.

`astra-full-fix-checks.log` belegt 14 gezielte Kontrollen, darunter der tatsächliche
Vorbereiter → Runner → Gruppen-Consumer. Falscher Fall, ersetzter Prompt, falsche
Datenrevision sowie gemischte Zeit-/Turn-Limits werden abgewiesen. Prozess- und
native Modell-I/O sind in diesem lokalen Test ersetzt. Die 19 bestehenden
Runner-/Prozesstests bestehen separat in `astra-full-cli-checks.log`.

cases-v9 ändert nur Katalog-ID, Fixture-Metadaten und die zwei abgeleiteten
Fixture-Dateien. Originale Given/Expect-Dateien bleiben unverändert. Skill-Payloads
ändern sich durch diese Korrekturen nicht; Kandidat bleibt `w001-opus-fixed/`.

## Nachprüfung des Runners und Hostvertrags

Astra bestätigte unter PLAN-0034-FULL-ASTRA-2 einen P1 im READ-Parser: frühe
Anforderungen wurden ignoriert und leere Abschlussmeldungen führten zum Abbruch.
Alle Textmeldungen werden jetzt bis zum Turn-Ende ausgewertet. Gleiche offene
READs werden einmal bedient; spätere Wiederholungen und unmanifestierte Pfade
bleiben Fehler. Leere oder abgeschnittene Turns werden nicht vervollständigt.
22 Runner-/Prozessprüfungen und 14 Bindungs-/Verbraucherprüfungen bestanden.
Native Toolaufrufversuche werden auch bei stderr-Abbruch aus der nativen
Aufzeichnung übernommen, ohne eine erfolgreiche externe Aktion zu behaupten.

Der frühere angepasste Textkatalog überschreibt Lunas vorgegebenen Toolmodus.
Die damaligen Kontrollen und Läufe sind deshalb keine aktuelle Abnahme.
`astra-full-review-followup-summary.md` und
`selected-300/parser-and-host-validity.json` im privaten Testprojekt nennen
Begründung und invalidierte Resultate. Alle Rohdaten und Versuchszahlen bleiben.

Die neue Route erhält den gebündelten Katalog und aktiviert den benötigten
Code-Modus mit dokumentierten Namespace-Ausschlüssen. Astra bestätigte unter
PLAN-0034-FULL-ASTRA-2-HOST die Grundlage für die Kontrollen. Die tatsächlichen
Kontrollen in `host-qualification/qualification-bundled.json` belegen danach
erfolgreiche READ-Fortsetzung und erwartetes Turn-Limit bei bestätigtem
Luna/high, vollständigen Ereignissen, leerem stderr und ohne native Toolaufrufe.
Dies belegt den begrenzten Verständnisweg, keine fachliche Skill-Abnahme.

ADR-0166 legt 300 Versuche insgesamt und eine gezielte Auswahl fest.
`0034-selected-300.md` hält die laufende Auswahl und Grenzen fest. Trigger-,
Befolgungs-, Wirkungs-, Claude-, native Workflow-/Ask- und CI-Nachweise werden
aus Verständnisprüfungen nicht abgeleitet.
