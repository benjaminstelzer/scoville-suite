---
format_version: 1
id: ADR-0238
status: accepted
created: 2026-11-16
accepted: 2026-11-16
scope: suite/skills
---

# Eigentümerentscheidungen zu drei offenen Punkten der Widerspruchsprüfung

## Decision

Binding sections: complete

Der Eigentümer hat am 2026-11-16 über die drei Befunde entschieden, die die Widerspruchsprüfung aller Skills vom 2026-11-15 offen gelassen hatte:

- **Cleanup ohne Plan-Profil:** Cleanup legt keine fehlende `PROJECT_INDEX.md` an, auch wenn die Anfrage die Datei nennt. Plan legt den Index zusammen mit seinem Profil an. Der gewünschte Projektkontext kommt bis dahin in die zuständige Regeldatei, und Cleanup sagt das.
- **Kein Modell je Step:** Workflow kennt keine Modellwahl je Step. Das gespeicherte Hauptpaar gilt für jeden Step. Eine vorhandene `[execute: ...]`-Angabe, die abweicht, gilt nicht; sie wird auf das Wort des Nutzers über Plan ersetzt. Setup verweist für eine einmalige Wahl nicht mehr auf den Plan-Step. Das ersetzt den letzten Satz der Decision in ADR-0235, soweit er die einmalige Wahl im Plan-Step erlaubte.
- **Wechsel gespeicherter Paare:** Gespeicherte Workflow-Paare werden nur zwischen Läufen über Setup geändert, nie für einen Step und nie innerhalb eines Laufs.

Am selben Tag hat der Eigentümer zum weiteren Vorgehen in PLAN-0067/W-005 entschieden: Nach Runde v33 wird zuerst die Ursache der verbliebenen Opus-Fehlläufe isoliert und erst dann gezielt korrigiert und nachgemessen. Die frische unabhängige Aufgabe läuft einmal am Endkandidaten.

## Problem

Die Widerspruchsprüfung fand drei Paare von Textstellen, hinter denen zwei verschiedene Absichten standen. Cleanup durfte auf Wunsch einen frei formulierten Index anlegen, während Plan nur ein vollständig fehlendes Profil initialisiert. Setup verwies für eine einmalige Modellwahl auf den Plan-Step, während Workflow und sein Helfer eine abweichende Angabe nie ausführten. Setup ließ Paare nur zwischen Läufen ändern, während Workflow bei einer abweichenden Angabe anbot, mitten im Lauf ein neues Hauptpaar zu speichern.

## Drivers

- Ein frei formulierter Index lässt das Plan-Profil unvollständig zurück und blockiert die spätere Initialisierung.
- Ein Lauf mit einem festen Paar bleibt vergleichbar und braucht keine Auswahl je Step.
- Die Skills sollen einfach bleiben; eine Funktion ohne Wirkung wird weggelassen statt ausgebaut.

## Considered alternatives

- Cleanup legt den Index frei an, und Plan übernimmt ihn später: verlangt eine Änderung am Plan-Helfer.
- Ein abweichendes Paar je Step zulassen: verlangt einen neuen Laufzeit-Mechanismus im Workflow-Helfer. Der Eigentümer hat diese Wahl zunächst getroffen und am selben Tag zurückgenommen.
- Paarwechsel ab dem nächsten Step: ein Lauf bestünde dann aus gemischten Paaren.

## Consequences

- Das Step-Format von Plan bleibt unverändert: Plan liest und prüft `[execute: ...]` weiter, damit bestehende Pläne gültig bleiben. Ob Plan die Angabe künftig nicht mehr neu schreiben soll, ist nicht entschieden.
- Der Workflow-Helfer hält bei einer abweichenden Angabe weiter an. Geändert ist nur seine Meldung: Sie nennt das Ersetzen über Plan und den Wechsel des Hauptpaars zwischen Läufen.
- Wer ohne Plan einen Index wünscht, bekommt den Kontext in der Regeldatei und den Hinweis auf Plan.

## Confirmation

Die Texte von Cleanup, Workflow und Setup, die Meldung des Workflow-Helfers und die README-Bausteine stimmen mit den drei Entscheidungen überein. Die Gesamtprüfung der Suite besteht.

## Revisit when

Ein Projekt braucht einen Index ohne Plan, ein Lauf braucht nachweislich verschiedene Modelle für einzelne Steps, oder bestehende `[execute: ...]`-Angaben halten Läufe wiederholt an.
