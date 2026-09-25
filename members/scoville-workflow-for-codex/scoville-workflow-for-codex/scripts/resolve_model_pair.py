#!/usr/bin/env python3
"""Resolve Workflow task model and thinking from the installed route table."""
from __future__ import annotations

import argparse
import json
import sys
if sys.version_info < (3, 11):
    raise SystemExit("Python 3.11 or newer is required for Workflow helpers")
import tomllib
from pathlib import Path


from workflow_settings import ROUTES, EFFORTS, load_config


def resolve(config: dict, role: str, route: str | None = None,
            override_model: str | None = None, override_reasoning: str | None = None,
            original_model: str | None = None, original_reasoning: str | None = None,
            repair_number: int | None = None) -> dict:
    if role in {"executor", "reviewer"}:
        if route not in ROUTES or original_model is not None or original_reasoning is not None or repair_number is not None:
            raise ValueError("executor or reviewer requires only a route and optional executor overrides")
        if role == "reviewer" and (override_model is not None or override_reasoning is not None):
            raise ValueError("reviewer overrides are not allowed")
        pair = dict(config["execute" if role == "executor" else "review"][route])
        if override_model is not None:
            pair["model"] = override_model
        if override_reasoning is not None:
            pair["reasoning"] = override_reasoning
        if not pair["model"] or pair["reasoning"] not in EFFORTS:
            raise ValueError("invalid executor override")
        return {"model": pair["model"], "thinking": pair["reasoning"], "route": route}

    if role != "repair" or route is not None or override_model is not None or override_reasoning is not None:
        raise ValueError("repair requires the original launched pair and repair number")
    if not original_model or original_reasoning not in EFFORTS or repair_number not in (1, 2, 3):
        raise ValueError("invalid original pair or repair number")
    if repair_number == 1:
        return {"model": original_model, "thinking": original_reasoning}
    matches = [index for index, name in enumerate(ROUTES)
               if config["execute"][name] == {"model": original_model, "reasoning": original_reasoning}]
    if not matches:
        raise ValueError("original launched pair is not in the current execute route table; repair 2/3 cannot select a higher route. Check the original override and current configuration")
    target = ROUTES[min(max(matches) + repair_number - 1, len(ROUTES) - 1)]
    pair = config["execute"][target]
    return {"model": pair["model"], "thinking": pair["reasoning"], "route": target}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--role", choices=("executor", "reviewer", "repair"), required=True)
    parser.add_argument("--route", choices=ROUTES)
    parser.add_argument("--override-model")
    parser.add_argument("--override-reasoning")
    parser.add_argument("--original-model")
    parser.add_argument("--original-reasoning")
    parser.add_argument("--repair-number", type=int)
    parser.add_argument("--project-root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    try:
        config = load_config(Path(__file__).resolve().parents[1] / "assets" / "workflow.toml", args.project_root)
        result = resolve(config, args.role, args.route, args.override_model,
                         args.override_reasoning, args.original_model,
                         args.original_reasoning, args.repair_number)
    except (OSError, ValueError, tomllib.TOMLDecodeError) as error:
        print(json.dumps({"valid": False, "diagnostic": str(error)}, ensure_ascii=False))
        return 1
    print(json.dumps({"valid": True, **result}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    for stream in (sys.stdin, sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="strict")
    raise SystemExit(main())
