"""Ask configuration validation shared by Ask and suite Setup."""
from pathlib import Path
import json
import math
import re
from scoville_config import merge, section

REASONING_LEVELS = {"none", "minimal", "low", "medium", "high", "xhigh", "max", "ultra"}
EFFORT_LEVELS = ("low", "medium", "high", "xhigh", "max")
MODEL_PATTERN = re.compile(r"^[A-Za-z0-9._:-]+$")


def validate_claude_pair(settings):
    if settings['route'] == 'claude-cli':
        require(MODEL_PATTERN.fullmatch(settings['model']), 'invalid Claude model')
        require(settings['effort'] in EFFORT_LEVELS, 'unsupported Claude CLI effort')


def require(condition, message):
    if not condition:
        raise ValueError(message)


def text(value, name):
    require(isinstance(value, str) and bool(value.strip()), f'{name} must be nonempty text')
    return value


def merge_config_layer(base, overlay):
    result = merge(base, overlay)
    # A newer preset also overrides inline fields inherited from older layers.
    # Inline advisers supplied in this same layer retain their local precedence.
    if 'advisers' not in overlay and isinstance(overlay.get('presets'), dict):
        advisers = result.get('advisers')
        if isinstance(advisers, list):
            for index, adviser in enumerate(advisers):
                if isinstance(adviser, dict):
                    preset = overlay['presets'].get(adviser.get('id'))
                    if isinstance(preset, dict):
                        advisers[index] = merge(adviser, preset)
    return result

def resolve_settings(defaults: Path, request: dict):
    config = json.loads(defaults.read_text(encoding='utf-8'))
    require('project_config' not in request,
            'project_config is no longer an input; use project_root for .scoville/config.json or overrides for this request')
    config = merge_config_layer(config, section('ask', request.get('project_root', request.get('cwd'))))
    config = merge_config_layer(config, request.get('overrides', {}))
    require(set(config) <= {'schema_version', 'advisers', 'presets', 'claude'}, 'unknown configuration keys')
    require(type(config.get('schema_version')) is int and config['schema_version'] == 1, 'unsupported config version')
    advisers = config.get('advisers')
    require(isinstance(advisers, list) and advisers, 'select at least one adviser')
    presets = config.get('presets')
    require(isinstance(presets, dict), 'presets must be an object')
    for identifier, preset in presets.items():
        require(re.fullmatch(r'[a-z0-9][a-z0-9-]*', identifier), 'invalid preset id')
        require(isinstance(preset, dict) and set(preset) <= {'name', 'route', 'model', 'effort'}, 'invalid adviser preset')
        require(preset.get('route') in {'native', 'claude-cli'}, 'unknown adviser route')
        text(preset.get('model'), 'preset model')
        require(preset.get('effort') in REASONING_LEVELS, 'invalid preset reasoning level')
        validate_claude_pair(preset)
        if 'name' in preset:
            text(preset['name'], 'preset name')
    expanded = []
    for item in advisers:
        if isinstance(item, str):
            require(item in presets, f'unknown adviser preset: {item}')
            item = {'id': item}
        require(isinstance(item, dict), 'adviser must be a preset name or object')
        preset = presets.get(item.get('id'), {})
        require(isinstance(preset, dict) and set(preset) <= {'name', 'route', 'model', 'effort'}, 'invalid adviser preset')
        expanded.append(merge(preset, item))
    advisers = config['advisers'] = expanded
    claude = config.get('claude')
    require(isinstance(claude, dict), 'invalid Claude settings')
    seen = set()
    for adviser in advisers:
        require(isinstance(adviser, dict), 'adviser must be an object')
        require(set(adviser) <= {'id', 'name', 'route', 'model', 'effort'}, 'unknown adviser keys')
        identifier = text(adviser.get('id'), 'adviser id')
        require(re.fullmatch(r'[a-z0-9][a-z0-9-]*', identifier) and identifier not in seen, 'invalid or duplicate adviser id')
        seen.add(identifier)
        require(adviser.get('route') in {'native', 'claude-cli'}, 'unknown adviser route')
        text(adviser.get('model'), 'model')
        require(adviser.get('effort') in REASONING_LEVELS, 'invalid reasoning level')
        validate_claude_pair(adviser)
        if 'name' in adviser:
            text(adviser['name'], 'adviser name')
    claude = config.get('claude')
    require(set(claude) == {'max_budget_usd', 'session_persistence', 'customizations', 'timeout_seconds', 'web_tools'}, 'invalid Claude settings')
    deadline = claude['timeout_seconds']
    require(type(deadline) in (int, float) and math.isfinite(deadline) and deadline > 0, 'Claude timeout_seconds must be positive and finite')
    budget = claude['max_budget_usd']
    require(type(budget) in (int, float) and math.isfinite(budget) and budget > 0, 'Claude budget must be positive and finite')
    require(all(type(claude[k]) is bool for k in ('session_persistence', 'customizations', 'web_tools')), 'Claude flags must be boolean')
    return config
