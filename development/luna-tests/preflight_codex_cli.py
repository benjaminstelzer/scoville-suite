"""Verify the pinned CLI's model/effort/tool projection on localhost; no backend."""
import argparse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import os
from pathlib import Path
import subprocess
import threading
from run_codex_cli_case import base_command, turn_command, verify_hash
from process_lifetime import WorkerProcess


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for key in ('codex', 'catalog', 'output'):
        parser.add_argument('--' + key, type=Path, required=True)
    parser.add_argument('--model', choices=('gpt-5.6-luna', 'gpt-5.6-terra'), required=True)
    args = parser.parse_args()
    hashes = {
        'codex': verify_hash(args.codex, 'bc45017e8239dc150258f69309ced9df6bbcdf5b8e4f346decf780ac0999e226', 'codex'),
        'catalog': verify_hash(args.catalog, '0a2bca132452338774a9c243e195095ad0b6400b17b2586306a69e8dcfade5f0', 'catalog'),
    }
    args.output.mkdir(parents=True, exist_ok=False)
    workspace = args.output / 'workspace'
    workspace.mkdir()
    observations = []

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *_args):
            pass

        def do_POST(self):
            length = int(self.headers.get('Content-Length', '-1'))
            if not 0 <= length <= 4 * 1024 * 1024:
                self.send_error(400)
                return
            request = json.loads(self.rfile.read(length))
            observations.append({'model': request.get('model'),
                'effort': request.get('reasoning', {}).get('effort'),
                'tools': request.get('tools', []), 'tools_present': 'tools' in request,
                'auth_present': 'Authorization' in self.headers})
            body = b'{"error":{"message":"intentional local preflight stop","type":"preflight"}}'
            self.send_response(400)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Content-Length', str(len(body)))
            self.end_headers()
            self.wfile.write(body)

    server = ThreadingHTTPServer(('127.0.0.1', 0), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    base = base_command(args.codex, args.catalog, args.model, 'medium')
    for config in ('model_provider="loopback"', 'model_providers.loopback.name="Local qualification"',
        f'model_providers.loopback.base_url="http://127.0.0.1:{server.server_port}/v1"',
        'model_providers.loopback.wire_api="responses"',
        'model_providers.loopback.requires_openai_auth=false',
        'model_providers.loopback.request_max_retries=0', 'model_providers.loopback.stream_max_retries=0'):
        base.extend(('-c', config))
    command = turn_command(base, workspace, None)
    command.insert(command.index('exec') + 1, '--ephemeral')
    names = ('APPDATA', 'COMSPEC', 'LOCALAPPDATA', 'NUMBER_OF_PROCESSORS', 'PATH', 'PATHEXT',
             'PROCESSOR_ARCHITECTURE', 'SystemRoot', 'TEMP', 'TMP', 'USERPROFILE', 'WINDIR')
    env = {k: os.environ[k] for k in names if k in os.environ}
    env.update(HTTP_PROXY='http://127.0.0.1:1', HTTPS_PROXY='http://127.0.0.1:1',
               ALL_PROXY='http://127.0.0.1:1', NO_PROXY='127.0.0.1,localhost')
    worker = None
    try:
        worker = WorkerProcess(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
            stderr=subprocess.PIPE, cwd=workspace, env=env)
        stdout, stderr = worker.communicate(b'Return PRECHECK without tools.\n', timeout=30)
    finally:
        if worker is not None:
            worker.close()
        server.shutdown()
        server.server_close()
        thread.join(timeout=5)
    expected = {'model': args.model, 'effort': 'medium', 'tools': [], 'auth_present': False}
    valid = (len(observations) == 1 and
             {k: observations[0][k] for k in expected} == expected and
             not stderr and worker.returncode != 0)
    result = {'valid': valid, 'hashes': hashes, 'observations': observations,
              'returncode': worker.returncode, 'worker_tree_stopped': True,
              'limit': 'Local serialized request only; intentional 400; no backend proof.'}
    (args.output / 'summary.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    (args.output / 'stdout.jsonl').write_bytes(stdout)
    (args.output / 'stderr.log').write_bytes(stderr)
    print(json.dumps(result))
    return 0 if valid else 1

if __name__ == '__main__':
    raise SystemExit(main())
