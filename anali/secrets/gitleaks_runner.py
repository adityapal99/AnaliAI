'''gitleaks runner (stub).'''

from anali.core.executor import run_command

def scan_secrets():
    output = run_command("gitleaks detect --report-format json --no-git")
    return {"gitleaks": output}
