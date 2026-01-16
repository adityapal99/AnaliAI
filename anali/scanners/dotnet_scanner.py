'''Scanner: dotnet_scanner.py (stub).'''

from anali.core.executor import run_command

def run():
    return {
        "roslyn-analyzers": run_command("dotnet build --no-incremental || true"),
        "devskim": run_command("devskim analyze . --json || true"),
    }
