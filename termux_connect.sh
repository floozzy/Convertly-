#!/usr/bin/env bash
set -euo pipefail

REPO_URL="${REPO_URL:-https://github.com/floozzy/Convertly-.git}"
TARGET_DIR="${TARGET_DIR:-$HOME/Convertly-}"
BRANCH="${BRANCH:-main}"

echo "[Termux] Preparing environment..."
pkg update -y >/dev/null 2>&1 || true
pkg install -y git python >/dev/null 2>&1 || true

mkdir -p "$HOME"

if [ ! -d "$TARGET_DIR/.git" ]; then
  echo "[Termux] Cloning repository into $TARGET_DIR"
  rm -rf "$TARGET_DIR"
  git clone "$REPO_URL" "$TARGET_DIR"
else
  echo "[Termux] Updating existing repository"
  cd "$TARGET_DIR"
  git remote set-url origin "$REPO_URL" 2>/dev/null || true
  git fetch origin >/dev/null 2>&1 || true
  if git show-ref --verify --quiet refs/heads/$BRANCH; then
    git checkout "$BRANCH" >/dev/null 2>&1 || true
  elif git show-ref --verify --quiet refs/heads/master; then
    git checkout master >/dev/null 2>&1 || true
  fi
  git reset --hard "origin/$BRANCH" >/dev/null 2>&1 || git reset --hard origin/master >/dev/null 2>&1 || true
fi

cd "$TARGET_DIR"

echo "[Termux] Installing Python dependencies..."
python3 -m pip install --upgrade pip >/dev/null 2>&1 || true
python3 -m pip install -r requirements.txt

if [ ! -f .env ]; then
  cat > .env <<'EOF'
BOT_TOKEN=your_token_here
EOF
  echo "[Termux] Created .env. Edit it and put your Telegram token."
fi

echo "[Termux] Done. Run this next:"
echo "  cd $TARGET_DIR && bash start.sh"
