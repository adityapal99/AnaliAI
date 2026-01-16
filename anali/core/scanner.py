'''Orchestrates all scans (stub).'''

from anali.core.executor import run_command
from anali.scanners import (
    python_scanner, node_scanner, dotnet_scanner,
    java_scanner, cpp_scanner, generic_scanner
)

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
