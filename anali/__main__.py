from anali.core.detector import detect_framework
from anali.core.scanner import run_scans, run_secrets_scan, run_dependency_scan
from anali.core.reporter import generate_report
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", type=str, default=".", help="Path to project root")
    args = parser.parse_args()

    print(f"🔍 Scanning project at: {args.path}")
    frameworks = detect_framework(args.path)
    print(f"Detected: {frameworks}")

    print("🧠 Running static + dynamic analysis...")
    scans = run_scans(frameworks)

    print("🔑 Scanning for secrets...")
    secrets = run_secrets_scan()

    print("📦 Auditing dependencies...")
    dependencies = run_dependency_scan(frameworks)

    print("🧾 Generating reports...")
    generate_report(scans, secrets, dependencies)

if __name__ == "__main__":
    main()
