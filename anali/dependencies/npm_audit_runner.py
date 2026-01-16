'''npm audit runner (stub).'''

from anali.core.executor import run_command

def run_npm_audit():
    output = run_command("npm audit --json || true")
    return {"npm_audit": output}
