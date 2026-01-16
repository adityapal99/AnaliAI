'''Framework detection logic (stub).'''

import os, json

FRAMEWORK_MAP = {
    ".NET": ["Program.cs", "appsettings.json"],
    "NodeJS": ["package.json"],
    "Python-Django": ["manage.py", "requirements.txt"],
    "Python-Flask": ["app.py", "requirements.txt"],
    "Java-SpringBoot": ["pom.xml"],
    "Flutter": ["pubspec.yaml"],
    "Android": ["AndroidManifest.xml"],
    "C++": ["main.cpp", "CMakeLists.txt"],
    "Go": ["go.mod"],
}

def detect_framework(root="."):
    detected = []
    files = os.listdir(root)
    for fw, indicators in FRAMEWORK_MAP.items():
        if any(f in files for f in indicators):
            detected.append(fw)
    return detected or ["Unknown"]

if __name__ == "__main__":
    print(json.dumps({"detected": detect_framework()}))
