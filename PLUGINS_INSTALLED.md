# Claude Code plugins set up in this session

Compiled from conversation history (container was reset, so `claude plugin list` shows nothing locally). To reuse in another chat: re-run the `claude plugin marketplace add` / `claude plugin install` commands below.

## Marketplaces added

| Marketplace name | Source |
|---|---|
| ponytail | https://github.com/DietrichGebert/ponytail |
| superpowers-marketplace | obra/superpowers-marketplace |
| addy-agent-skills | https://github.com/addyosmani/agent-skills |
| ui-ux-pro-max-skill | https://github.com/nextlevelbuilder/ui-ux-pro-max-skill |
| caveman | https://github.com/JuliusBrussee/caveman |
| open-design | https://github.com/nexu-io/open-design |
| mattpocock | https://github.com/mattpocock/skills |
| ecc | https://github.com/affaan-m/ECC |
| storybook | https://github.com/storybookjs/storybook |
| taste-skill | https://github.com/Leonxlnx/taste-skill |
| career-ops | https://github.com/career-ops-hq/career-ops |
| impeccable | https://github.com/pbakaus/impeccable |
| ppt-master | https://github.com/hugohe3/ppt-master |
| humanizer | https://github.com/blader/humanizer |
| marketingskills | https://github.com/coreyhaines31/marketingskills |
| academic-research-skills | https://github.com/Imbad0202/academic-research-skills |
| slidev-plugins | https://github.com/slidevjs/slidev |
| headroom-marketplace | https://github.com/headroomlabs-ai/headroom |
| agentic-awesome-skills | https://github.com/sickn33/agentic-awesome-skills |
| mempalace | https://github.com/MemPalace/mempalace |
| diffusers-skills | https://github.com/huggingface/diffusers |
| claude-for-financial-services | https://github.com/anthropics/financial-services |
| claude-plugins-official | https://github.com/anthropics/claude-plugins-official |
| anthropic-cybersecurity-skills | https://github.com/mukul975/Anthropic-Cybersecurity-Skills |
| claude-video | https://github.com/bradautomates/claude-video |

`anthropic-agent-skills` (source of `document-skills`) was already present before this session — not added by us.

## Plugins installed (`plugin@marketplace`)

All below installed successfully unless noted.

| Plugin | What it does |
|---|---|
| ponytail@ponytail | Lazy/YAGNI code-writing mode, active every session |
| caveman@caveman | Terse-prose reply mode, active every session |
| superpowers@superpowers-marketplace | TDD, debugging, collaboration-pattern skills |
| superpowers-chrome@superpowers-marketplace | Chrome DevTools Protocol access (`browsing` skill) |
| double-shot-latte@superpowers-marketplace | Stops unnecessary "should I continue?" interruptions |
| agent-skills@addy-agent-skills | SDLC engineering skills (spec/plan/build/verify/ship) |
| ui-ux-pro-max@ui-ux-pro-max-skill | 79 UI styles, 192 color palettes, 74 font pairings, design-system data |
| open-design@open-design | MCP client for local OpenDesign app; needs `od` daemon on PATH — **not running in this container, MCP connection failed (CONNECTION_CLOSED)** |
| mattpocock-skills@mattpocock | TDD, "grilling", domain-modeling, code-review skills |
| ecc@ecc | 68 agents / 292 skills + Bash/Write safety-gating hooks (heaviest, behavior-changing plugin installed) |
| storybook@storybook | Official Storybook init/setup/upgrade/stories skills |
| taste-skill@taste-skill | Frontend design-taste skills (brutalist, minimalist, soft, redesign, image-to-code) |
| career-ops@career-ops | Personal job-search automation (scan boards, tailor CV, track applications) |
| impeccable@impeccable | Design fluency, 24 `/impeccable` commands, anti-pattern detection |
| ppt-master@ppt-master | Natively-editable PPTX generation from PDF/DOCX/URL/Markdown |
| humanizer@humanizer | Strips AI-sounding prose patterns |
| marketing-skills@marketingskills | 50 marketing skills (CRO, SEO, copywriting, paid ads, etc.) |
| academic-research-skills@academic-research-skills | Research→write→review pipeline; **license CC-BY-NC-4.0 (non-commercial)** |
| slidev@slidev-plugins | Slidev markdown slide decks (official, Anthony Fu) |
| headroom@headroom-marketplace | Local context-compression hooks; needed CLI installed separately (see below) |
| agentic-awesome-skills@agentic-awesome-skills | Full plugin-safe skill catalog (skipped ~50 narrower role-bundle variants) |
| mempalace@mempalace | Local AI memory system via MCP; value limited here since this container is ephemeral |
| diffusers@diffusers-skills | Contribution conventions for the HuggingFace `diffusers` repo itself |
| financial-analysis@claude-for-financial-services | DCF/comps/LBO/3-statement modeling (skipped 18 other narrow finance verticals) |
| code-review@claude-plugins-official | Official: automated PR code review |
| pr-review-toolkit@claude-plugins-official | Official: PR review agents |
| commit-commands@claude-plugins-official | Official: git commit/push/PR workflow commands |
| feature-dev@claude-plugins-official | Official: feature-development workflow |
| code-modernization@claude-plugins-official | Official: legacy-codebase modernization |
| code-simplifier@claude-plugins-official | Official: code simplification agent |
| claude-md-management@claude-plugins-official | Official: CLAUDE.md maintenance |
| claude-code-setup@claude-plugins-official | Official: recommends hooks/skills/MCP setup for a codebase |
| skill-creator@claude-plugins-official | Official: create/improve skills |
| plugin-dev@claude-plugins-official | Official: Claude Code plugin development toolkit |
| agent-sdk-dev@claude-plugins-official | Official: Claude Agent SDK dev kit |
| mcp-server-dev@claude-plugins-official | Official: MCP server development skills |
| hookify@claude-plugins-official | Official: create custom hooks from conversation patterns |
| security-guidance@claude-plugins-official | Official: security review for Claude-generated code |
| claude-security@claude-plugins-official | Official: deep vulnerability scanning |
| frontend-design@claude-plugins-official | Official: high-design-quality frontend generation |
| explanatory-output-style@claude-plugins-official | Official: educational-insight output style |
| learning-output-style@claude-plugins-official | Official: interactive learning-mode output style |
| typescript-lsp@claude-plugins-official | Official: TypeScript/JS language server |
| pyright-lsp@claude-plugins-official | Official: Python language server (Pyright) |
| rust-analyzer-lsp@claude-plugins-official | Official: Rust language server |
| gopls-lsp@claude-plugins-official | Official: Go language server |
| cybersecurity-skills@anthropic-cybersecurity-skills | 818 skills mapped to MITRE ATT&CK / NIST CSF / ATLAS / D3FEND / F3 |
| watch@claude-video | `/watch` command: video → frames (ffmpeg) + transcript (yt-dlp, Whisper) |

`document-skills@anthropic-agent-skills` (xlsx/docx/pptx/pdf) was already installed before this session.

`claude-plugins-official` and `claude-for-financial-services` are large marketplaces with hundreds/dozens more entries not installed (mostly third-party SaaS integrations needing credentials, e.g. GitHub, Linear, AWS, MongoDB, Zapier, or narrow finance verticals like kyc-screener, lseg, sp-global) — install any specific one with `claude plugin install <name>@<marketplace>`.

## MCP servers / CLI tools / config changes for the above

- `poppler-utils` (apt) — PDF page rendering, needed to read uploaded PDFs
- `fonts-noto-cjk` (apt) — Noto Sans/Serif CJK fonts, for proper Chinese-language PDF/PPTX rendering
- `libreoffice-impress` (apt) — needed by the `document-skills:pptx` skill's QA scripts (soffice → PDF → image render)
- `reportlab`, `weasyprint`, `python-pptx`, `defusedxml`, `lxml`, `Pillow`, `markitdown[pptx]` (pip) — PDF/PPTX generation and the pptx skill's validate/thumbnail tooling
- `uv tool install "headroom-ai[all]"` — installs the `headroom` CLI so the `headroom` plugin's hooks work (plain `pip install` failed on a system PyJWT conflict; `uv tool` sandboxes around it)
- `uv tool install mempalace` — installs `mempalace-mcp` so the `mempalace` plugin's MCP server works
- `npm install pptxgenjs react-icons react react-dom sharp` (in `scratchpad/medchinese/`) — used to generate a custom-graphics PPTX deck with rendered icons
- No `settings.json` / permission config changes were made.
