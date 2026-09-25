#!/usr/bin/env python3
"""Resolve instruction depth from one Skill's independent configuration."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

PROFILES = {'low', 'medium', 'high'}
CLASSES = {'ultra_low': 'low', 'low': 'low', 'medium': 'medium',
           'high': 'high', 'ultra_high': 'high'}


def read_config(path: Path) -> dict:
    try:
        import tomllib
    except ImportError as error:
        raise ValueError('Python 3.11 or newer is required; do not use the no-Python route') from error
    with path.open('rb') as stream:
        data = tomllib.load(stream)
    config = data.get('prompting')
    if not isinstance(config, dict) or set(config) != {'profile', 'models'}:
        raise ValueError('prompting requires exactly profile and models')
    if not isinstance(config['profile'], str) or config['profile'] not in PROFILES | {'auto'}:
        raise ValueError('profile must be auto, low, medium or high')
    models = config['models']
    if not isinstance(models, dict) or any(
        not isinstance(key, str) or not key.strip() or not isinstance(value, str) or value not in PROFILES
        for key, value in models.items()
    ):
        raise ValueError('models must map exact nonempty model IDs to low, medium or high')
    return config


def resolve(config: dict, *, explicit: str | None = None,
            model: str | None = None, task_class: str | None = None) -> str:
    if explicit is not None:
        if explicit not in PROFILES:
            raise ValueError('explicit profile must be low, medium or high')
        return explicit
    if config['profile'] != 'auto':
        return config['profile']
    if model is not None:
        if not isinstance(model, str) or not model.strip():
            raise ValueError('target model must be a nonempty exact ID')
        return config['models'].get(model, 'medium')
    if task_class is not None and task_class not in CLASSES:
        raise ValueError('unknown task class')
    return CLASSES.get(task_class, 'medium')


def instructions(config_path: Path, *, explicit: str | None = None,
                 model: str | None = None, task_class: str | None = None) -> dict:
    profile = resolve(read_config(config_path), explicit=explicit,
                      model=model, task_class=task_class)
    references = Path(__file__).resolve().parent.parent / 'references' / 'prompting'
    texts = [(references / name).read_text(encoding='utf-8').strip()
             for name in ('common.md', profile + '.md')]
    return {'profile': profile, 'instructions': '\n\n'.join(texts)}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', type=Path, required=True)
    parser.add_argument('--profile', choices=sorted(PROFILES))
    parser.add_argument('--model')
    parser.add_argument('--task-class', choices=sorted(CLASSES))
    args = parser.parse_args()
    try:
        result = instructions(args.config, explicit=args.profile,
                              model=args.model, task_class=args.task_class)
    except (ValueError, OSError) as error:
        print(json.dumps({'error': str(error)}, ensure_ascii=False), file=sys.stderr)
        return 1
    print(json.dumps(result, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
