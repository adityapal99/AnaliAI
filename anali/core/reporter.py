'''Builds unified report (stub).'''

import json
from datetime import datetime

def generate_report(scan_results, secrets_results, dependency_results):
    final = {
        "timestamp": str(datetime.utcnow()),
        "scans": scan_results,
        "secrets": secrets_results,
        "dependencies": dependency_results,
    }

    with open("reports/report.json", "w") as f:
        json.dump(final, f, indent=2)

    with open("reports/report.md", "w") as f:
        f.write(f"# 🛡️ Anali Security Report\n")
        f.write(f"**Generated:** {final['timestamp']}\n\n")
        for section, data in final.items():
            if section != "timestamp":
                f.write(f"## {section.title()}\n```\n{json.dumps(data, indent=2)[:3000]}\n```\n\n")
