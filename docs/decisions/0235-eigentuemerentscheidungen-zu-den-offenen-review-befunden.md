---
format_version: 1
id: ADR-0235
status: accepted
created: 2026-11-14
accepted: 2026-11-14
scope: suite/skills
---

# Eigentümerentscheidungen zu den offenen Befunden des Opus-Reviews

## Decision

Binding sections: complete

Der Eigentümer hat am 2026-11-14 über die Befunde entschieden, die PLAN-0067 offen gelassen hatte:

- **Plan, Decision-Vorlage:** Die Vorlage enthält den Vermerk `Binding sections: complete` nicht mehr vorausgefüllt. Der Vermerk bleibt möglich; wer ihn setzt, hat geprüft, dass die vier bindenden Abschnitte allein alles tragen.
- **Plan, Aufräumen von Decisions:** Das Anlegen eines Plans entfernt keine Decision und keinen Link. Decisions werden nur auf ausdrücklichen Pflegeauftrag nach repair.md aufgeräumt.
- **Plan, Zielprüfung beim Schreiben:** Die Regel verbietet weiter das Schreiben außerhalb des Projekts. Die Prüfung auf umgeleitete Pfade ist kein Schritt des Modells mehr; Selector und Validator melden sie.
- **Plan, geänderte Acceptance:** Mit ausdrücklicher Entscheidung des Nutzers wird die Acceptance eines begonnenen Work Items im Work Item geändert, und Evidence nennt, was der Nutzer wann geändert hat. Eine Decision entsteht nur, wenn die Änderung über das Work Item hinaus gilt.
- **Setup, Nachweis beim Umstieg:** Liegt ein nötiger Abschlussnachweis nur im flüchtigen Zustand des Hosts, wird das Work Item vor dem Umstieg mit der alten Version beendet. Setup legt keine Nachweisdatei in einem ignorierten Ordner an.
- **Ask, Inhalt einer Antwort:** Die Antwort eines nativen Beraters nennt die Referenz der Anfrage und die wesentlichen Grenzen der Belege. Kennung des Beraters und Auftragsumfang werden nicht wiederholt und nicht verglichen.
- **Code, Regeldateien:** Im allgemeinen Profil gilt eine Regel aus AGENTS.md wie aus CLAUDE.md als Projektregel. Widersprechen sich gleichrangige Regeln, fragt das Modell vor der davon abhängigen Arbeit.
- **UI, Textkorrektur:** Eine Korrektur an bestehendem Oberflächentext liest nur die Wording-Referenz.
- **UI, WordPress-Version:** Das PHP-Beispiel nimmt den Token-Zweig ab WordPress 7.1 aufwärts. Dass spätere Versionen ungeprüft sind, steht im Beispiel.
- **Testmodelle:** Modelltests nutzen gpt-6.1-sol und Claude Opus 5.5, beide mit Reasoning-Aufwand medium.

Unverändert bleiben auf Entscheidung des Eigentümers: Setup darf eine einmalige Wahl in der Anfrage oder im Plan-Step festhalten, und in Ask erledigt eine unbegründete Zustimmung des Beraters einen Befund nicht.

## Problem

Ein Review der Skills mit Opus 5.5 am 2026-11-13 hinterließ zwölf Befunde, die Verhalten ändern und deshalb nicht ohne den Eigentümer zu entscheiden waren. Zwei davon hingen an WordPress-Fakten: Das Versionsmuster ist oben entschieden, das Beispiel `submit_button( esc_html__( … ) )` wurde ohne Entscheidung auf die von WordPress dokumentierte Form `submit_button( __( … ) )` gestellt.

## Drivers

- Der Eigentümer will keine Schritte, die ein Modell nur um des Ablaufs willen ausführt.
- Ein Auftrag soll nichts auslösen, was der Nutzer nicht bestellt hat.
- Records sollen aus dem Repository allein lesbar bleiben.

## Considered alternatives

- Den Vermerk `Binding sections: complete` ganz abschaffen: einfacher, kostet aber Kontext bei jeder gelieferten Decision und eine Änderung am Helfer.
- In einem Projekt mit beiden Regeldateien nur die Datei des eigenen Hosts binden lassen: entspricht dem, was der Host lädt, lässt aber unterschiedliches Verhalten je Host zu.
- Das WordPress-Beispiel auf 7.1 beschränkt lassen: sicher gegen ungeprüfte Änderungen, aber ein Plugin verliert die Tokens beim nächsten WordPress-Update.

## Consequences

- Erledigte befristete und ersetzte Decisions bleiben liegen, bis der Nutzer Pflege verlangt.
- Eine geänderte Acceptance ist im Work Item und in dessen Evidence nachvollziehbar, nicht mehr in einer eigenen Decision.
- Ein natives Berater-Final ohne Kennung wird allein über den Absender des Hosts und die Referenz zugeordnet.
- Ein WordPress-Release nach 7.1, das die Tokens ändert, trifft Plugins, die das Beispiel übernommen haben.

## Confirmation

Die genannten Stellen in den Skills Plan, Setup, Ask, Code und UI sowie die Freigaberegeln nennen die Entscheidungen. Die Gesamtprüfung der Suite besteht.

## Revisit when

Ein Modell setzt den Vermerk ohne Prüfung, ein Projekt sammelt veraltete Decisions an, eine Antwort eines Beraters wird falsch zugeordnet, ein WordPress-Release ändert die Tokens, oder der Eigentümer entscheidet einen der Punkte neu.
