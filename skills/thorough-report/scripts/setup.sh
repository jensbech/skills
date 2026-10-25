#!/usr/bin/env bash
# One-time setup per session: Playwright + Chromium for rendering, and the avoid-ai-writing rules.
# Usage: bash setup.sh <scratch-dir>
# Prints the PW_PATH to use with build.js and contact-sheet.js.
set -euo pipefail
SCRATCH="${1:?usage: setup.sh <scratch-dir>}"
mkdir -p "$SCRATCH/render" "$SCRATCH/aiw"

if [ ! -d "$SCRATCH/render/node_modules/playwright" ]; then
  (cd "$SCRATCH/render" && npm init -y >/dev/null && npm i playwright@latest >/dev/null 2>&1)
fi
(cd "$SCRATCH/render" && npx playwright install chromium >/dev/null 2>&1 || true)

if [ ! -d "$SCRATCH/aiw/avoid-ai-writing" ]; then
  git clone --depth 1 https://github.com/conorbronsdon/avoid-ai-writing.git "$SCRATCH/aiw/avoid-ai-writing" >/dev/null 2>&1 \
    || echo "WARN: could not clone avoid-ai-writing; use the lists in references/writing-guide-template.md"
fi

SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DESIGN_LOG="$SKILL_DIR/artifacts/design-log.md"
if [ ! -f "$DESIGN_LOG" ]; then
  mkdir -p "$SKILL_DIR/artifacts"
  printf '# Design log

One entry per delivered report. New designs must differ from every entry on at least 5 of the 8 dials.
This folder is gitignored: it holds per-user data, never published with the skill.
' > "$DESIGN_LOG"
fi

for tool in pdftotext pdftoppm pdfinfo; do
  command -v "$tool" >/dev/null || echo "WARN: $tool missing (install poppler: brew install poppler / apt install poppler-utils)"
done

echo "PW_PATH=$SCRATCH/render/node_modules/playwright"
echo "AIW=$SCRATCH/aiw/avoid-ai-writing"
echo "DESIGN_LOG=$DESIGN_LOG"
