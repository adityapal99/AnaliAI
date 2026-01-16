'''Scanner: python_scanner.py (stub).'''

from anali.core.executor import run_command

def run():
    results = {}
    results["bandit"] = run_command("bandit -r . -f json || true")
    results["semgrep"] = run_command("semgrep --config=auto --json || true")
    results["pip-audit"] = run_command("pip-audit --format json || true")
    return results
