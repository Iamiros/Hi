# Tooling inventory

Collected at session start with `claude plugin list`, the skills listing, the agent list and the MCP servers connected in this session.

## Plugins (user + project scope)
| Plugin | Used | For what / why skipped |
|---|---|---|
| taste-skill (taste-skill, minimalist-skill, soft-skill, brutalist-skill, redesign-skill, stitch-skill, brandkit, output-skill, image skills) | **taste-skill:taste-skill read in full** | Anti-slop rules applied to the product UI: one accent, one radius system (10 px), no gradients, no em or en dashes, no eyebrow labels, light and dark tokens, reduced motion, one hero element. Marketing-page rules (hero stack, logo walls) do not apply to a tracker and were not used. Others skipped: they target landing pages or image generation. |
| ui-ux-pro-max | **Used (redesign)** | `--design-system` search for a fitness tracker; kept its Barlow Condensed numerals and UX checklist (44 px targets, focus, reduced motion), rejected its orange and green palette. |
| document-skills (pdf, docx, pptx, xlsx) | pdf approach only | The guide PDF is produced by Chromium print (Playwright) from the same HTML, so the Persian shaping and fonts match the screen version. docx, pptx, xlsx not requested. |
| humanizer | Skipped | Persian prose written directly; the plugin targets English AI-isms. |
| pubmed (MCP) | **Used** | Verified every citation (title, year, journal, PMID, DOI) and checked creatine and caffeine claims against abstracts and full text. See DECISIONS.md. |
| caveman, ponytail | Used as style | Terse replies; no extra abstraction layers or dependencies in the tracker (vanilla JS, no build chain). |
| ppt-master | Skipped | No presentation requested. |
| watch | Skipped | No video material. |

## Skills (standalone)
| Skill | Used |
|---|---|
| dataviz | **Read in full.** Weight line (daily dots + 7-day line + target), comparison bars (single hue steps, no dual axis, no track), heatmap with 5 validated steps (text colour chosen per step for 4.5:1). |
| taste-skill:output-skill | Applied: no placeholders, nothing truncated. |
| literature-review, pubmed-database, medical-image-search, token-budget-advisor, context-budget | Not needed (no images, short context). |
| artifact-design, artifact-capabilities, artifact-diagramming | Skipped: files are delivered in the repo, not published as an Artifact. |
| session-start-hook, update-config, loop, claude-api, security-review, code-review, simplify | Not applicable. |

## Agents
| Agent | Used |
|---|---|
| general-purpose (x2, parallel) | One sports-science and Persian wording review of `tools/program.py` and `tools/build_guide.py`. One code, accessibility, RTL, security and offline review of the tracker (with Playwright repro). Findings were applied, see DECISIONS.md. |
| Explore, Plan, caveman cavecrew-*, claude-code-guide, statusline-setup | Not needed. |

## MCP servers
| Server | Used |
|---|---|
| pubmed (plugin) | Yes, citation checks. |
| github (mcp__github__*) | No PR requested. |
| claude-code-remote, Claude_Docs | No. |

## Local tools
Playwright + Chromium (`/opt/pw-browsers/chromium-1194`): screenshots at 375, 430 and 1280 px in light and dark, rule verification across all 56 days, persistence/import/export tests, PDF export. PyMuPDF to inspect the PDF. Fonts Vazirmatn 33.0.3 and Barlow Condensed 5.0.8 (SIL OFL 1.1) from jsDelivr, embedded as base64 in both HTML files.
