# Furkan Anter's Agent Skills

Small, practical guardrails for coding agents.

## Skills

### overengineer

Prevents unnecessary architecture, abstractions, dependencies, refactors, and scope creep. Pushes toward the smallest correct solution.

### test-guard

Prevents code changes from being completed while relevant tests or coverage impact are forgotten. Requires meaningful test consideration without chasing coverage for its own sake.

## Install

Cursor + Codex:

```sh
npx skills add furkananter/skills --skill overengineer --skill test-guard -a cursor -a codex
```

Only `test-guard`:

```sh
npx skills add furkananter/skills --skill test-guard -a cursor -a codex
```

## Cursor always-on rules

Cursor project rules live in `.cursor/rules`. Both skills include an `alwaysApply: true` adapter, but the Skills CLI does not copy adapters into `.cursor/rules` automatically.

After installing the skills for Cursor:

```sh
sh .agents/skills/overengineer/scripts/install-cursor-rule.sh
sh .agents/skills/test-guard/scripts/install-cursor-rule.sh
```

The resulting rules are:

```text
.cursor/rules/overengineer.mdc
.cursor/rules/test-guard.mdc
```

## Codex

Both skills include `agents/openai.yaml` with implicit invocation enabled.

## Repository structure

```text
skills/
├── overengineer/
│   ├── SKILL.md
│   ├── agents/
│   ├── adapters/
│   └── scripts/
└── test-guard/
    ├── SKILL.md
    ├── agents/
    ├── adapters/
    └── scripts/
```

Follows the open [Agent Skills specification](https://agentskills.io/specification).

## License

MIT License. Copyright (c) 2026 Furkan Anter.
