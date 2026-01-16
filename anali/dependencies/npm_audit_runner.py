'''npm audit runner (stub).'''

from anali.core.executor import run_command

def run():
    return {"npm-audit": run_command("npm audit --json || true")}

