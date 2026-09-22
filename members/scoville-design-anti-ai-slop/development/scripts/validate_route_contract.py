#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

import yaml


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2] / "scoville-design-anti-ai-slop")
    args = parser.parse_args()
    root = args.root.resolve()
    registry = yaml.safe_load((root / "modules.yaml").read_text(encoding="utf-8"))
    fixtures = yaml.safe_load(
        (root.parent / "development" / "docs" / "evaluation" / "successor-route-fixtures.yaml").read_text(encoding="utf-8")
    )
    modules = registry["modules"]
    known_signals = set(registry["signal_enum"])
    module_ids = [module["id"] for module in modules]
    owner = {
        signal: module["id"]
        for module in modules
        for signal in module["when_any"]
    }
    errors: list[str] = []
    seen: set[str] = set()
    for case in fixtures.get("cases", []):
        case_id = case.get("id")
        if not isinstance(case_id, str) or not case_id or case_id in seen:
            errors.append(f"invalid or duplicate case id: {case_id!r}")
            continue
        seen.add(case_id)
        signals = case.get("signals")
        modifiers = case.get("modifiers")
        expected = case.get("expected")
        forbidden = case.get("forbidden")
        if not all(isinstance(value, list) for value in (signals, modifiers, expected, forbidden)):
            errors.append(f"{case_id}: signals/modifiers/expected/forbidden must be lists")
            continue
        unknown_signals = sorted(set(signals) - known_signals)
        unknown_modules = sorted((set(expected) | set(forbidden)) - set(module_ids))
        if unknown_signals:
            errors.append(f"{case_id}: unknown signals {unknown_signals}")
        if unknown_modules:
            errors.append(f"{case_id}: unknown modules {unknown_modules}")
        selected = [module_id for module_id in module_ids if module_id in {owner[s] for s in signals if s in owner}]
        if selected != expected:
            errors.append(f"{case_id}: selected {selected}, expected {expected}")
        collisions = sorted(set(selected) & set(forbidden))
        if collisions:
            errors.append(f"{case_id}: forbidden selected {collisions}")
        if any(modifier in known_signals for modifier in modifiers):
            errors.append(f"{case_id}: modifier duplicates a routing signal")
    if errors:
        for error in errors:
            print(f"ERROR {error}")
        print(f"INVALID cases={len(seen)} errors={len(errors)}")
        return 1
    print(f"VALID route_cases={len(seen)} signals={len(known_signals)} modules={len(module_ids)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
