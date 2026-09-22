#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import posixpath
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path, PurePosixPath
from typing import Any

import yaml


from generate_module_index import END, GENERATED, INDEX_PATH, START, load_registry, render_index, replace_index


SUCCESSOR_SCHEMA = "successor-v1"
CURRENT_SCHEMA = "successor-v2"
LEGACY_SCHEMA = "legacy-rc7"
SCHEMAS = (CURRENT_SCHEMA, SUCCESSOR_SCHEMA, LEGACY_SCHEMA)

SUCCESSOR_CANONICAL_IDS = [
    "brief-framing-and-criteria",
    "concept-development-and-selection",
    "composition-and-layout",
    "typography-and-typesetting",
    "font-technology-and-script-safety",
    "colour-and-reproduction",
    "imagery-and-art-direction",
    "information-design-and-data-visualization",
    "cartography-and-spatial-data",
    "diagrams-and-relational-information",
    "brand-and-visual-systems",
    "logo-and-identity-mark-design",
    "instructional-and-explanatory-design",
    "advertising-and-campaign-art-direction",
    "ui-workflow-and-interaction-design",
    "web-and-responsive-design",
    "editorial-and-fixed-media-design",
    "packaging-graphics-and-sku-systems",
    "physical-wayfinding-and-signage-systems",
    "motion-and-sequence",
    "media-production-and-handoff",
    "critique-and-validation",
    "culture-and-representation",
    "people-privacy-and-media-integrity",
    "sustainability-claims",
    "source-verification-and-evidence",
    "asset-rights-and-attribution",
    "style-direction",
]

CURRENT_CANONICAL_IDS = SUCCESSOR_CANONICAL_IDS + [
    "generic-signatures-and-subject-specificity",
    "coordination-with-sibling-skills",
]

LEGACY_CANONICAL_IDS = [
    "brief-and-concept",
    "composition-and-layout",
    "typography-and-writing-systems",
    "colour-and-reproduction",
    "imagery-and-art-direction",
    "information-and-data",
    "brand-and-visual-systems",
    "ui-and-interaction-design",
    "motion-and-sequence",
    "media-production-and-handoff",
    "critique-and-validation",
    "culture-ethics-and-provenance",
    "sources-and-attribution",
    "style-direction",
]

STATUSES = {"admitted", "retained-floor", "stub", "withheld"}
INTERVENTIONS = {"focus", "correction", "teaching", "external-verification"}

# Source identifiers are intentionally prefix-agnostic. At least one separator
# keeps ordinary prose headings from being mistaken for source records.
SOURCE_ID_TEXT = r"[A-Za-z0-9]+(?:[-_.:][A-Za-z0-9]+)+"
SOURCE_ID = re.compile(rf"^{SOURCE_ID_TEXT}$")
SOURCE_HEADING = re.compile(
    rf"^###\s+`?({SOURCE_ID_TEXT})`?(?:\s|$)", re.MULTILINE
)
SOURCE_HEADER = re.compile(r"^Sources:\s*(.*?)\s*$", re.MULTILINE)
MARKDOWN_LINK = re.compile(r"\]\(([^)]+)\)")
DIRECT_MODULE_LINK = re.compile(r"\]\(([^)#?]+\.md)(?:#[^)]+)?\)")


@dataclass
class Result:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    metrics: dict[str, int] = field(default_factory=dict)

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warning(self, message: str) -> None:
        self.warnings.append(message)


def tokens(text: str) -> int:
    # Optional descriptive measurement; structural validation never calls this.
    import tiktoken
    return len(tiktoken.get_encoding("o200k_base").encode(text))


def successor_core_text(skill_text: str) -> str:
    """Return Core with generated index entries excluded from its measured size.

    The exact successor metric retains the index boundary markers and replaces
    everything from START through END with ``START + newline + END``. The
    generated comment and every generated module entry therefore count only
    toward the separate index measurement.
    """
    start = skill_text.find(START)
    end = skill_text.find(END)
    if start < 0 or end < 0 or end < start:
        return skill_text
    end += len(END)
    return skill_text[:start] + START + "\n" + END + skill_text[end:]


def _normal_path(value: Any) -> str:
    return str(value).replace("\\", "/")


def _source_ids_from_header(
    content: str, module_id: str, result: Result
) -> list[str]:
    matches = SOURCE_HEADER.findall(content)
    if len(matches) != 1:
        result.error(f"{module_id}: expected exactly one Sources: header")
        return []
    raw_parts = [part.strip().strip("`") for part in matches[0].split(",")]
    if not raw_parts or any(not part for part in raw_parts):
        result.error(f"{module_id}: Sources: header must list source IDs")
        return []
    invalid = [part for part in raw_parts if not SOURCE_ID.fullmatch(part)]
    if invalid:
        result.error(
            f"{module_id}: invalid source ID(s) in Sources: header: "
            + ", ".join(invalid)
        )
    if len(raw_parts) != len(set(raw_parts)):
        result.error(f"{module_id}: duplicate source ID in Sources: header")
    return raw_parts


def _source_headings(source_text: str, result: Result) -> set[str]:
    headings = SOURCE_HEADING.findall(source_text)
    if not headings:
        result.error("source index has no level-three source ID headings")
        return set()
    duplicates = sorted({item for item in headings if headings.count(item) > 1})
    if duplicates:
        result.error("duplicate source index headings: " + ", ".join(duplicates))
    return set(headings)


def _is_sibling_reference_link(target: str) -> bool:
    target = target.split("#", 1)[0].split("?", 1)[0].strip()
    if not target or "://" in target or target.startswith(("mailto:", "#", "/")):
        return False
    normalized_target = target.replace("\\", "/")
    normalized = PurePosixPath(normalized_target)
    if normalized.suffix.lower() != ".md":
        return False
    # Resolve relative to the routed leaf's references/ directory. This catches
    # `other.md`, `references/other.md`, and `../references/other.md` without
    # confusing a link to repository documentation with a sibling expert.
    resolved = posixpath.normpath(posixpath.join("references", normalized_target))
    return resolved.startswith("references/")


def _distribution_files(root: Path, registry: dict, result: Result) -> set[str]:
    values = registry.get("distribution_files", [])
    if not isinstance(values, list) or not all(isinstance(v, str) and v for v in values):
        result.error("distribution_files must be a list of non-empty paths")
        return set()
    declared: set[str] = set()
    for value in values:
        normalized = _normal_path(value)
        path = PurePosixPath(normalized)
        if path.is_absolute() or ".." in path.parts or ":" in normalized:
            result.error(f"invalid distribution path: {value}")
            continue
        target = root.joinpath(*path.parts)
        if not target.resolve().is_relative_to(root):
            result.error(f"distribution path escapes package: {value}")
            continue
        if path.as_posix() in declared:
            result.error(f"duplicate distribution path: {value}")
        declared.add(path.as_posix())
        if not target.is_file():
            result.error(f"missing distribution file: {value}")
    return declared


def _validate_script_links(content: str, relative: PurePosixPath,
                           distribution: set[str], result: Result) -> None:
    for link in MARKDOWN_LINK.findall(content):
        link = _normal_path(link.split("#", 1)[0].split("?", 1)[0])
        if "://" in link or "scripts" not in PurePosixPath(link).parts:
            continue
        target = posixpath.normpath(posixpath.join(str(relative.parent), link))
        if not target.startswith("scripts/") or target not in distribution:
            result.error(f"{relative}: script link is not a declared packaged tool: {link}")


def _validate_example_links(content: str, relative: PurePosixPath,
                            distribution: set[str], result: Result) -> None:
    for link in MARKDOWN_LINK.findall(content):
        link = _normal_path(link.split("#", 1)[0].split("?", 1)[0])
        if "://" in link or "examples" not in PurePosixPath(link).parts:
            continue
        target = posixpath.normpath(posixpath.join(str(relative.parent), link))
        if not target.startswith("examples/") or target not in distribution:
            result.error(f"{relative}: example link is not a declared packaged asset: {link}")


def _validate_example_manifest(root: Path, distribution: set[str], result: Result) -> None:
    manifest_name = "examples/spatial-proof/manifest.json"
    if manifest_name not in distribution:
        return
    try:
        payload = json.loads((root / manifest_name).read_text(encoding="utf-8"))
        entries = payload["entries"]
        if payload.get("schema_version") != 1 or len(entries) != 6:
            raise ValueError("expected schema 1 and six entries")
        for entry in entries:
            if entry.get("review") != "native-image-view-2026-09-07":
                raise ValueError(f"{entry.get('id')}: missing native image review")
            for field, hash_field in (("source", "source_sha256"), ("render", "render_sha256")):
                relative = f"examples/spatial-proof/{entry[field]}"
                if relative not in distribution:
                    raise ValueError(f"{entry['id']}: undeclared {field}")
                digest = hashlib.sha256((root / relative).read_bytes()).hexdigest()
                if digest != entry.get(hash_field):
                    raise ValueError(f"{entry['id']}: {field} hash mismatch")
            if entry.get("viewport") != [640, 400]:
                raise ValueError(f"{entry.get('id')}: unexpected viewport")
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
        result.error(f"invalid spatial teaching manifest: {exc}")


def _validate_common_loads(registry: dict, modules: list[dict], result: Result) -> None:
    planned = registry.get("planned_common_loads")
    if not isinstance(planned, list) or not planned:
        result.error("planned_common_loads must be a non-empty list")
        planned = []
    known_ids = {item.get("id") for item in modules if isinstance(item, dict)}
    load_ids: set[str] = set()
    for load in planned:
        if not isinstance(load, dict):
            result.error("planned_common_loads entries must be mappings")
            continue
        load_id = load.get("id")
        selected = load.get("modules")
        if not isinstance(load_id, str) or not load_id.strip():
            result.error("planned common load requires a non-empty id")
            load_id = "<missing>"
        elif load_id in load_ids:
            result.error(f"duplicate planned common load id: {load_id}")
        load_ids.add(load_id)
        if (
            not isinstance(selected, list)
            or not selected
            or not all(isinstance(module_id, str) and module_id for module_id in selected)
        ):
            result.error(
                f"planned common load {load_id}: modules must be a non-empty string list"
            )
            continue
        if len(selected) != len(set(selected)):
            result.error(f"planned common load {load_id}: duplicate module IDs")
        unknown = sorted(set(selected) - known_ids)
        if unknown:
            result.error(
                f"planned common load {load_id}: unknown module IDs "
                + ", ".join(unknown)
            )


def validate_package(root: Path, schema: str, *, runtime: bool = False, development_root: Path | None = None) -> Result:
    root = root.resolve()
    result = Result()
    if schema not in SCHEMAS:
        result.error(f"unknown validation schema: {schema}")
        return result
    successor = schema in (SUCCESSOR_SCHEMA, CURRENT_SCHEMA)
    if runtime and schema != CURRENT_SCHEMA:
        result.error("runtime derivative validation requires successor-v2")
        return result

    registry_path = root / "modules.yaml"
    skill_path = root / "SKILL.md"
    agent_path = root / "agents" / "openai.yaml"
    for required in (registry_path, skill_path, agent_path):
        if not required.is_file():
            result.error(f"missing required file: {required.relative_to(root)}")
    if result.errors:
        return result

    try:
        registry = load_registry(registry_path)
    except (OSError, ValueError, yaml.YAMLError) as exc:
        result.error(f"invalid modules.yaml: {exc}")
        return result

    declared_schema = registry.get("package_schema")
    distribution = _distribution_files(root, registry, result)
    _validate_example_manifest(root, distribution, result)
    if successor:
        if declared_schema != schema:
            result.error(
                f"modules.yaml package_schema must be {schema!r}"
            )
        canonical_ids = CURRENT_CANONICAL_IDS if schema == CURRENT_SCHEMA else SUCCESSOR_CANONICAL_IDS
    else:
        if declared_schema not in (None, LEGACY_SCHEMA):
            result.error(
                f"modules.yaml package_schema is incompatible with {LEGACY_SCHEMA!r}"
            )
        canonical_ids = LEGACY_CANONICAL_IDS

    modules = registry["modules"]
    ids = [item.get("id") if isinstance(item, dict) else None for item in modules]
    if ids != canonical_ids:
        result.error(f"canonical module IDs/order differ: {ids}")
    if len(ids) != len(set(ids)):
        result.error("duplicate module IDs")

    signals = registry.get("signal_enum")
    if not isinstance(signals, list) or not all(
        isinstance(signal, str) and signal for signal in signals
    ):
        result.error("signal_enum must be a list of non-empty strings")
        signals = []
    elif len(signals) != len(set(signals)):
        result.error("signal_enum must be unique")
    signal_set = set(signals)
    signal_owner: dict[str, str] = {}
    owned: dict[str, str] = {}
    referenced_paths: set[Path] = set()
    module_sources: dict[str, set[str]] = {}

    if successor:
        non_routed = registry.get("non_routed_references")
        if non_routed != ["references/source-index.md"]:
            result.error(
                "non_routed_references must contain exactly references/source-index.md"
            )
        source_path = root / "references" / "source-index.md"
    else:
        if "non_routed_references" in registry:
            result.error("legacy-rc7 must not declare non_routed_references")
        source_path = root / "references" / "sources-and-attribution.md"

    if not source_path.is_file():
        result.error(f"missing required file: {source_path.relative_to(root)}")
        registered_sources: set[str] = set()
    else:
        source_text = source_path.read_text(encoding="utf-8")
        registered_sources = _source_headings(source_text, result)
        if schema == CURRENT_SCHEMA:
            local_entry = re.search(
                r"^### SRC-PACKAGE-LOCAL-SYNTHESIS\s*\n(.*?)(?=^### |\Z)",
                source_text, re.MULTILINE | re.DOTALL,
            )
            if not local_entry or not re.search(r"^Class: local-synthesis\s*$", local_entry[1], re.MULTILINE):
                result.error("successor-v2 requires the registered local-synthesis entry and class")

    for item in modules:
        if not isinstance(item, dict):
            result.error("modules entries must be mappings")
            continue
        module_id = item.get("id", "<missing>")
        status = item.get("status")
        intervention = item.get("intervention")
        allowed_statuses = {"draft"} if schema == CURRENT_SCHEMA else STATUSES
        if status not in allowed_statuses:
            result.error(f"{module_id}: invalid status {status!r}")
        if intervention not in INTERVENTIONS:
            result.error(f"{module_id}: invalid intervention {intervention!r}")
        if item.get("requires") != [] or item.get("conflicts") != []:
            result.error(f"{module_id}: requires/conflicts must be explicit empty lists")

        for field_name in ("when_any", "unless"):
            values = item.get(field_name)
            if not isinstance(values, list) or not all(
                isinstance(value, str) and value for value in values
            ):
                result.error(
                    f"{module_id}: {field_name} must be a list of non-empty strings"
                )
                continue
            unknown = sorted(set(values) - signal_set)
            if unknown:
                result.error(
                    f"{module_id}: {field_name} contains unknown signals "
                    + ", ".join(unknown)
                )
        for signal in item.get("when_any", []):
            if not isinstance(signal, str):
                continue
            previous = signal_owner.get(signal)
            if previous:
                result.error(
                    f"signal ownership collision: {signal} in {previous} and {module_id}"
                )
            else:
                signal_owner[signal] = module_id

        concerns = item.get("owns")
        if (
            not isinstance(concerns, list)
            or not concerns
            or not all(isinstance(concern, str) and concern for concern in concerns)
        ):
            result.error(f"{module_id}: owns must be a non-empty string list")
            concerns = []
        for concern in concerns:
            previous = owned.get(concern)
            if previous:
                result.error(
                    f"ownership collision: {concern} in {previous} and {module_id}"
                )
            else:
                owned[concern] = module_id

        relative_text = _normal_path(item.get("path", ""))
        relative = PurePosixPath(relative_text)
        if (
            len(relative.parts) != 2
            or relative.parts[0] != "references"
            or relative.suffix != ".md"
        ):
            result.error(
                f"{module_id}: path must be a Markdown file directly under references/"
            )
            continue
        target = root.joinpath(*relative.parts)
        resolved_target = target.resolve()
        if resolved_target in referenced_paths:
            result.error(f"{module_id}: duplicate module path {relative_text}")
        referenced_paths.add(resolved_target)
        if successor and relative_text == "references/source-index.md":
            result.error(f"{module_id}: source-index.md must remain non-routed")
        if not target.is_file():
            result.error(f"{module_id}: missing reference {relative_text}")
            continue

        content = target.read_text(encoding="utf-8")
        if schema == CURRENT_SCHEMA:
            for label, value in (("Status", status), ("Intervention", intervention)):
                if re.findall(rf"^{label}: `(.*?)`  $", content, re.MULTILINE) != [value]:
                    result.error(f"{module_id}: {label} header must match registry with standard formatting")
            if item.get("evidence") != []:
                result.error(f"{module_id}: evidence must be empty; raw receipt registries are not retained")
        _validate_script_links(content, relative, distribution, result)
        _validate_example_links(content, relative, distribution, result)
        sibling_links = [
            link for link in MARKDOWN_LINK.findall(content) if _is_sibling_reference_link(link)
        ]
        if sibling_links:
            result.error(
                f"{module_id}: sibling reference link found: {sibling_links[0]}"
            )

        declared = item.get("sources")
        if (
            not isinstance(declared, list)
            or not declared
            or not all(isinstance(source_id, str) for source_id in declared)
        ):
            result.error(f"{module_id}: sources must be a non-empty string list")
            declared = []
        if len(declared) != len(set(declared)):
            result.error(f"{module_id}: duplicate declared source ID")
        for source_id in declared:
            if not SOURCE_ID.fullmatch(source_id):
                result.error(f"{module_id}: invalid source ID {source_id}")
            elif source_id not in registered_sources:
                result.error(f"{module_id}: unresolved source ID {source_id}")
        header_sources = _source_ids_from_header(content, module_id, result)
        if header_sources != declared:
            result.error(
                f"{module_id}: Sources: header must equal modules.yaml sources in order"
            )
        module_sources[module_id] = set(declared)

    unused_signals = sorted(signal_set - set(signal_owner))
    if unused_signals:
        result.error("signal_enum contains unowned signals: " + ", ".join(unused_signals))

    actual_reference_files = {
        path.resolve() for path in (root / "references").glob("*.md")
    }
    allowed_non_routed = {source_path.resolve()} if successor else set()
    allowed_non_routed.update(
        (root / path).resolve()
        for path in distribution
        if PurePosixPath(path).parts[:1] == ("references",)
    )
    expected_reference_files = referenced_paths | allowed_non_routed
    orphans = sorted(actual_reference_files - expected_reference_files)
    missing_expected = sorted(expected_reference_files - actual_reference_files)
    if orphans:
        result.error("orphan references: " + ", ".join(path.name for path in orphans))
    if missing_expected:
        result.error(
            "declared reference files missing: "
            + ", ".join(path.name for path in missing_expected)
        )

    skill_text = skill_path.read_text(encoding="utf-8")
    index_path = root / INDEX_PATH if (root / INDEX_PATH).is_file() else skill_path
    current_index = index_path.read_text(encoding="utf-8")
    try:
        index_text = render_index(
            registry,
            relative_to_references=index_path != skill_path,
        )
        if runtime or (schema == CURRENT_SCHEMA and GENERATED not in current_index):
            index_text = index_text.replace(GENERATED + "\n", "")
        expected_index = replace_index(current_index, index_text)
    except (KeyError, TypeError, ValueError) as exc:
        result.error(f"cannot render generated module index: {exc}")
        index_text = ""
        expected_index = current_index
    if current_index != expected_index:
        result.error("generated module index drift")
    result.metrics["modules"] = len(modules)

    linked = {
        path if path.startswith("references/") else f"references/{path}"
        for path in DIRECT_MODULE_LINK.findall(current_index)
    }
    expected_links = {
        _normal_path(item.get("path", ""))
        for item in modules
        if isinstance(item, dict)
    }
    if linked != expected_links:
        result.error("direct expert index links do not equal modules.yaml paths")

    if successor:
        _validate_common_loads(registry, modules, result)

    try:
        agent = yaml.safe_load(agent_path.read_text(encoding="utf-8"))
        default_prompt = agent["interface"]["default_prompt"]
        short_description = agent["interface"]["short_description"]
        if "$scoville-design-anti-ai-slop" not in default_prompt:
            result.error("agents/openai.yaml default_prompt must name the skill")
        if not 25 <= len(short_description) <= 64:
            result.error("agents/openai.yaml short_description must be 25-64 characters")
    except (KeyError, TypeError, yaml.YAMLError) as exc:
        result.error(f"invalid agents/openai.yaml: {exc}")

    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the Scoville Design package")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2] / "scoville-design-anti-ai-slop")
    parser.add_argument("--development-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument(
        "--schema",
        choices=SCHEMAS,
        default=CURRENT_SCHEMA,
        help=(
            "Validation contract. successor-v2 is current; select successor-v1 "
            "or legacy-rc7 explicitly for historical packages."
        ),
    )
    parser.add_argument("--runtime", action="store_true", help="Validate the comment-stripped v2 derivative without repository-only source-map checks")
    args = parser.parse_args()
    result = validate_package(args.root, args.schema, runtime=args.runtime, development_root=args.development_root)

    for warning in result.warnings:
        print(f"WARNING {warning}")
    if result.errors:
        print(f"INVALID errors={len(result.errors)} warnings={len(result.warnings)}")
        for error in result.errors:
            print(f"ERROR {error}")
        return 1

    metrics = " ".join(f"{key}={value}" for key, value in result.metrics.items())
    print(f"VALID schema={args.schema} warnings={len(result.warnings)} {metrics}".rstrip())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
