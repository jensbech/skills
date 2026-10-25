# Skills

Agent skills for Claude Code (and other runtimes that read `SKILL.md` folders). Each skill lives in `skills/<name>/` with a `SKILL.md` and any references, scripts and assets it needs.

| Skill | What it's for |
|---|---|
| [thorough-report](skills/thorough-report/SKILL.md) | A researched, designed PDF report on any subject, in any language, from a 10-page briefing to a 150-page handbook. Subagents research, design, write and review; every report gets its own design system; cross-chapter repetition is measured and gated. |

## Install

As a Claude Code plugin marketplace:

```
/plugin marketplace add <path-or-git-url-of-this-repo>
/plugin install report-skills@pers-skills
```

Or link a single skill into your personal skills folder:

```bash
ln -s "$PWD/skills/thorough-report" ~/.claude/skills/thorough-report
```

## Requirements per skill

**thorough-report**: Node.js, Python 3, poppler (`pdftoppm`, `pdftotext`) and git. `scripts/setup.sh` installs Playwright with Chromium into a scratch folder and fetches the [avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) rules. It needs an agent runtime with subagents for the full pipeline; without them it runs the phases sequentially.

## Adding a skill

- One folder per skill under `skills/`, named in lowercase with hyphens.
- `SKILL.md` frontmatter has `name` and `description`. The description says when to use the skill, not how it works.
- Heavy reference material goes in `references/`, runnable tools in `scripts/` (invoked through their interpreter, e.g. `python3 scripts/x.py`), templates in `assets/`.
- Only skills that are useful to anyone go here. No absolute paths, personal data or employer details in skill files.
- A skill that keeps per-user data (logs, history, generated output) writes it to its own `artifacts/` folder, which is gitignored.
- Add the folder to `skills` in `.claude-plugin/marketplace.json` and a row to the table above.

## Licence

[CC0 1.0](LICENSE): public domain dedication. Use, copy, modify and redistribute without asking or crediting.
