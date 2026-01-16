'''pip-audit runner (stub).'''

from anali.core.executor import run_command

def run():
    return {"pip-audit": run_command("pip-audit --format json || true")}
