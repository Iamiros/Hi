#!/bin/bash
# Installs the plugin set and PDF build tools in every Claude Code on the web session.
set -uo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

MARKETPLACES=(
  "anthropics/skills"
  "Leonxlnx/taste-skill"
  "JuliusBrussee/caveman"
  "DietrichGebert/ponytail"
  "affaan-m/everything-claude-code"
  "storybookjs/storybook"
)
PLUGINS=(
  "document-skills@anthropic-agent-skills"
  "taste-skill@taste-skill"
  "caveman@caveman"
  "ponytail@ponytail"
  "ecc@ecc"
  "storybook@storybook"
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

pip install -q --disable-pip-version-check pymupdf playwright weasyprint beautifulsoup4 >/dev/null 2>&1 \
  || echo "pip install of PDF build tools failed" >&2

exit 0
