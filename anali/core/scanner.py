'''Orchestrates all scans (stub).'''

from anali.core.executor import run_command
from anali.dependencies import generic_audit_runner, npm_audit_runner, pip_audit_runner
from anali.scanners import (
    python_scanner, node_scanner, dotnet_scanner,
    java_scanner, cpp_scanner, generic_scanner
)
from anali.secrets.gitleaks_runner import scan_secrets

def run_scans(frameworks):
    results = {}
    for fw in frameworks:
        if "Python" in fw:
            results[fw] = python_scanner.run()
        elif fw == "NodeJS":
            results[fw] = node_scanner.run()
        elif fw == ".NET":
            results[fw] = dotnet_scanner.run()
        elif fw == "Java-SpringBoot":
            results[fw] = java_scanner.run()
        elif fw == "C++":
            results[fw] = cpp_scanner.run()
        else:
            results[fw] = generic_scanner.run()
    return results

def run_secrets_scan():
    return scan_secrets()

def run_dependency_scan(frameworks):
    if "NodeJS" in frameworks:
        return npm_audit_runner.run()
    elif any("Python" in f for f in frameworks):
        return pip_audit_runner.run()
    else:
        return generic_audit_runner.run()