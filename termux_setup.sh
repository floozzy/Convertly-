#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

if ! command -v git >/dev/null 2>&1; then
  echo "Git is not installed. Run: pkg install git" >&2
  exit 1
fi

if ! command -v python3 >/dev/null 2>&1; then
  echo "Python 3 is not installed. Run: pkg install python" >&2
  exit 1
fi

python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

if [ ! -f .env ]; then
  echo "BOT_TOKEN=your_token_here" > .env
  echo "Created .env. Please edit it and set your token." >&2
  exit 0
fi

echo "Environment looks ready. Run: bash start.sh"
