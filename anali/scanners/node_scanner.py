'''Scanner: node_scanner.py (stub).'''

from anali.core.executor import run_command

def run():
    return {
        "eslint-security": run_command("npx eslint . -f json || true"),
        "semgrep": run_command("semgrep --config=auto --json || true"),
    }
