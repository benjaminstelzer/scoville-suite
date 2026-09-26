"""Read explicit rollout groups; count model input once per response ID.

This offline evidence tool never modifies sessions. Inputs and selection are
retained in a manifest; outputs contain metrics and source lines, not prompts.
"""
from __future__ import annotations

import argparse
import collections
from datetime import datetime
import json
from pathlib import Path
import re
import statistics


def median(values):
    return statistics.median(values) if values else None


def inspect(path):
    counts = collections.Counter()
    calls, waits, inputs, outputs, reads, dispatches = [], [], [], [], [], []
    seen = set()
    parent = None
    role = None
    prompt_size = None
    comments = finals = errors = 0
    for line_number, line in enumerate(path.open(encoding="utf-8"), 1):
        event = json.loads(line)
        data = event.get("payload", {})
        kind = event.get("type")
        timestamp = event.get("timestamp")
        if kind == "token_usage_record":
            identity = data.get("response_id")
            if identity and identity in seen:
                continue
            if identity:
                seen.add(identity)
            usage = data.get("usage", {})
            inputs.append(usage.get("input_tokens", 0))
        if kind != "response_item":
            continue
        item = data.get("type")
        if item == "message" and data.get("role") == "assistant":
            comments += data.get("phase") == "commentary"
            finals += data.get("phase") in ("final_answer", "final")
        if item in ("function_call_output", "custom_tool_call_output"):
            raw = data.get("output", "")
            if not isinstance(raw, str):
                raw = json.dumps(raw, ensure_ascii=False)
            outputs.append(len(raw))
            if parent is None and "<codex_delegation>" in raw:
                match = re.search(r"<source_thread_id>(.*?)</source_thread_id>", raw)
                parent = match[1] if match else None
                assignment = re.search(r"<input>(.*?)</input>", raw, re.S)
                text = assignment[1] if assignment else raw
                match = re.search(r"scoville_role=(coordinator|executor|reviewer|repair)", text)
                role = match[1] if match else "coordinator"
                prompt_size = len(text)
            if re.search(r"unrecognized arguments|the following arguments are required|MAGIC_INVALID|wrong delivery reference|unrecognized terminal status", raw):
                errors += 1
        if item not in ("function_call", "custom_tool_call"):
            continue
        raw = data.get("input", data.get("arguments", ""))
        if not isinstance(raw, str):
            raw = json.dumps(raw)
        name = data.get("name", "")
        names = re.findall(r"tools\.([\w]+)\s*\(", raw) or [name]
        names = [n.split("__")[-1] for n in names]
        counts.update(names)
        calls.append({"line": line_number, "timestamp": timestamp, "tools": names})
        if "wait_threads" in names or name in ("wait", "functions.wait"):
            waits.append(timestamp)
        if any(n == "create_thread" for n in names):
            dispatches.append({"line": line_number, "timestamp": timestamp})
        reads.extend(re.findall(r"(?:Get-Content(?:\s+-LiteralPath)?|read_text)\s+[\"']([^\"']+)", raw))
    gaps = [(datetime.fromisoformat(b.replace("Z", "+00:00")) - datetime.fromisoformat(a.replace("Z", "+00:00"))).total_seconds()
            for a, b in zip(waits, waits[1:]) if a and b]
    return dict(parent=parent, role=role or "coordinator", model_calls=len(inputs),
                input_tokens=sum(inputs), input_median=median(inputs), input_max=max(inputs, default=0),
                tool_calls=dict(counts), waits=len(waits), wait_gaps=gaps,
                comments=comments, finals=finals, outputs_over_10k=sum(n > 10000 for n in outputs),
                repeated_literal_reads=sum(v > 1 for v in collections.Counter(reads).values()),
                helper_error_outputs=errors, prompt_chars=prompt_size, dispatches=dispatches,
                call_locations=calls)


def analyze(manifest):
    result = {}
    for group, entries in manifest["groups"].items():
        sessions = {entry["id"]: inspect(Path(entry["path"]).expanduser()) for entry in entries}
        coordinators = [s for s in sessions.values() if s["role"] == "coordinator"]
        workers = [s for s in sessions.values() if s["role"] == "executor"]
        result[group] = {
            "summary": {"coordinators": len(coordinators), "workers": len(workers),
                        **{key: sum(s[key] for s in coordinators) for key in
                           ("model_calls", "input_tokens", "waits", "comments", "finals", "outputs_over_10k", "repeated_literal_reads", "helper_error_outputs")},
                        "wait_gap_median_seconds": median([n for s in coordinators for n in s["wait_gaps"]]),
                        "worker_prompt_chars": [s["prompt_chars"] for s in workers]},
            "sessions": sessions,
        }
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    result = analyze(manifest)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({k: v["summary"] for k, v in result.items()}, ensure_ascii=False))


if __name__ == "__main__":
    main()
