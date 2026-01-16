FROM python:3.11-slim

RUN apt-get update && apt-get install -y npm git curl wget libssl-dev tar
RUN pip install bandit semgrep pip-audit
RUN wget -qO gitleaks.tar.gz https://github.com/gitleaks/gitleaks/releases/latest/download/gitleaks_8.30.0_linux_x64.tar.gz
RUN tar xf gitleaks.tar.gz -C /usr/local/bin gitleaks
RUN rm gitleaks.tar.gz

WORKDIR /app
COPY . .

ENTRYPOINT ["python", "-m", "anali"]
