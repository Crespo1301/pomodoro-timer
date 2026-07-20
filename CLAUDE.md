# CLAUDE.md

Repo role: active public showcase tool featured in Portfolio as `CLI Pomodoro Timer`, but low current priority.

## Business Context

- This repo is part of the public showcase list in `Portfolio/src/data/projects.ts`.
- Shared workflow rules live in `/home/cresp3/Portfolio/AI-WORKFLOW.md`.

## Claude Role Here

- Use Claude for UX wording, naming, and product framing if this tool is revisited.
- Let Codex handle Python implementation, CLI behavior, and GitHub closeout.

## Working Notes

- Simple Python CLI with session tracking.
- Treat this as a portfolio tool, not a main weekly business surface.

## Useful Commands

```bash
python pomodoro.py
bash ./scripts/stitch-doctor.sh
bash ./scripts/stitch-proxy.sh
bash ./scripts/magic-mcp.sh
```

## Shared AI Tooling

- Follow `AI-WORKFLOW.md` for the shared CSolutions AI stack.
- Copied skill packs under `.claude/skills/` are local-only and ignored by Git.
  Use them when present, but do not commit bulk skill directories.
- Use `.mcp.json` with `code-review-graph` after running `code-review-graph build` so exploration and reviews stay token-efficient.
- Use OpenSpec for larger changes that benefit from proposal, spec, and task artifacts.

## Visual QA

Use the workspace runner at `/home/cresp3/scripts/visual-check.sh` after any layout, responsive, spacing, animation, or visual-polish change. Start the local dev server, capture mobile and desktop screenshots into `.visual-checks/`, and inspect the rendered pixels before calling the work done. See `VISUAL-QA.md`.
