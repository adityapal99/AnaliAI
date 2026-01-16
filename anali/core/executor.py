'''Subprocess wrappers for scanners (stub).'''

import subprocess, json

def run_command(cmd):
    try:
        result = subprocess.run(cmd, shell=True, text=True, capture_output=True)
        return json.loads(result.stdout) if result.stdout.strip().startswith("{") else result.stdout
    except Exception as e:
        return {"error": str(e)}
