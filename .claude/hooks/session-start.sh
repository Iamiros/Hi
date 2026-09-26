#!/bin/bash
# Installs the plugin set and document build tools in every Claude Code on the web session.
set -uo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

MARKETPLACES=(
  "anthropics/skills"
  "Leonxlnx/taste-skill"
  "JuliusBrussee/caveman"
  "DietrichGebert/ponytail"
  "anthropics/life-sciences"
  "hugohe3/ppt-master"
  "nextlevelbuilder/ui-ux-pro-max-skill"
  "blader/humanizer"
  "bradautomates/claude-video"
)
PLUGINS=(
  "document-skills@anthropic-agent-skills"
  "taste-skill@taste-skill"
  "caveman@caveman"
  "ponytail@ponytail"
  "pubmed@life-sciences"
  "ppt-master@ppt-master"
  "ui-ux-pro-max@ui-ux-pro-max-skill"
  "humanizer@humanizer"
  "watch@claude-video"
)

if command -v claude >/dev/null 2>&1; then
  known=$(claude plugin marketplace list 2>/dev/null || true)
  for repo in "${MARKETPLACES[@]}"; do
    grep -qF "($repo)" <<<"$known" || claude plugin marketplace add "$repo" >/dev/null 2>&1 || echo "marketplace add failed: $repo" >&2
  done
  installed=$(claude plugin list 2>/dev/null || true)
  for p in "${PLUGINS[@]}"; do
    grep -qF "$p" <<<"$installed" || claude plugin install "$p" >/dev/null 2>&1 || echo "plugin install failed: $p" >&2
  done
fi

# Slow system and Python tools install in the background so the session starts immediately.
setsid nohup bash -c '
  if ! command -v pdftoppm >/dev/null || ! command -v ffmpeg >/dev/null || ! fc-list | grep -qi "noto.*cjk"; then
    apt-get update -qq && DEBIAN_FRONTEND=noninteractive apt-get install -y -qq poppler-utils ffmpeg fonts-noto-cjk
  fi
  pip install -q --disable-pip-version-check pymupdf playwright weasyprint beautifulsoup4 \
    python-pptx PyYAML "markitdown[pptx]" defusedxml lxml Pillow reportlab yt-dlp
  echo done > /tmp/session-setup.done
' >/tmp/session-setup.log 2>&1 < /dev/null &

exit 0
