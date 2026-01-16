from anali.core.detector import detect_framework
from anali.core.scanner import run_scans
from anali.secrets.gitleaks_runner import scan_secrets
from anali.dependencies.npm_audit_runner import run_npm_audit
from anali.core.reporter import generate_report

if __name__ == "__main__":
    print("🔍 Detecting frameworks...")
    frameworks = detect_framework()
    print("Detected:", frameworks)

    print("🧠 Running static + dynamic analysis...")
    scans = run_scans(frameworks)

    print("🔑 Running secrets scan...")
    secrets = scan_secrets()

    print("📦 Running dependency audit...")
    dependencies = run_npm_audit()

    print("🧾 Generating unified report...")
    generate_report(scans, secrets, dependencies)
    print("✅ Aegis Layer 1 completed successfully.")
