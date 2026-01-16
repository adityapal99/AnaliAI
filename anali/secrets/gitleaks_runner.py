'''gitleaks runner (stub).'''

from anali.core.executor import run_command

def scan_secrets():
    return {"gitleaks": run_command("gitleaks detect --report-format json --no-git || true")}
