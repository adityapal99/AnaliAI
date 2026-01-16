'''Scanner: cpp_scanner.py (stub).'''

from anali.core.executor import run_command

def run():
    return {
        "flawfinder": run_command("flawfinder . || true"),
        "cppcheck": run_command("cppcheck --enable=all --inconclusive --xml . || true"),
    }
