# AGENTS.md

Guidance for Codex when working in this repo.

## Role

`pomodoro-timer` is a small public utility project for the CSolutions portfolio. It is not a primary business lane, but it should stay clean, usable, and easy to explain as a lightweight Python CLI showcase.

## Project Shape

- `pomodoro.py` is the app entry point.
- `data/sessions.json` stores local session history.
- `pomodoro-timer.gif` is the demo asset used by the README.
- There is no package manager, build step, or runtime dependency.

## Commands

```bash
python3 pomodoro.py
python3 -m py_compile pomodoro.py
```

## Working Rules

- Keep the CLI dependency-free unless the owner explicitly asks for a larger product direction.
- Do not commit personal session history or generated cache folders.
- Keep copied `.agents/skills/` and `.claude/skills/` folders local-only.
- Commit `.mcp.example.json`, `.env.ai.example`, and workflow docs when they define portable setup.
- Keep `.mcp.json` and `.env.ai.local` local-only.

## Verification

Before pushing, run:

```bash
python3 -m py_compile pomodoro.py
git diff --check
```
