#!/usr/bin/env bash
set -euo pipefail

REPO_URL="${REPO_URL:-https://github.com/floozzy/Convertly-.git}"
PROJECT_DIR="${PROJECT_DIR:-$HOME/Convertly-}"
BRANCH="${BRANCH:-master}"
BOT_TOKEN="${BOT_TOKEN:-}"

mkdir -p "$HOME"

if ! command -v git >/dev/null 2>&1; then
  pkg update -y || true
  pkg install -y git python >/dev/null 2>&1 || true
fi

if [ ! -d "$PROJECT_DIR/.git" ]; then
  rm -rf "$PROJECT_DIR"
  git clone "$REPO_URL" "$PROJECT_DIR"
else
  cd "$PROJECT_DIR"
  git remote set-url origin "$REPO_URL" >/dev/null 2>&1 || true
  git fetch origin >/dev/null 2>&1 || true
  git checkout "$BRANCH" >/dev/null 2>&1 || true
  git reset --hard "origin/$BRANCH" >/dev/null 2>&1 || true
fi

cd "$PROJECT_DIR"

python3 -m pip install --upgrade pip >/dev/null 2>&1 || true
python3 -m pip install -r requirements.txt

if [ -n "$BOT_TOKEN" ]; then
  printf 'BOT_TOKEN=%s\n' "$BOT_TOKEN" > .env
else
  if [ ! -f .env ]; then
    printf 'BOT_TOKEN=your_token_here\n' > .env
  fi
fi

if [ ! -f .env ]; then
  printf 'BOT_TOKEN=your_token_here\n' > .env
fi

mkdir -p logs

if pgrep -f 'python3 -m app.clients.telegram.bot' >/dev/null 2>&1; then
  pkill -f 'python3 -m app.clients.telegram.bot' || true
fi

nohup python3 -m app.clients.telegram.bot > logs/bot.log 2>&1 &

echo "[deploy_termux] Bot started"
echo "[deploy_termux] Log file: $PROJECT_DIR/logs/bot.log"
echo "[deploy_termux] Project: $PROJECT_DIR"
