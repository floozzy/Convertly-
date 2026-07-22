#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

python -m pip install --upgrade pip
pip install -r requirements.txt

if [ -f .env ]; then
  set -a
  source .env
  set +a
fi

python -m app.clients.telegram.bot
