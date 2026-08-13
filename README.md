# Furkan Anter's Agent Skills

Open Agent Skills focused on practical software work.

## overengineer

A default anti-overengineering guardrail. It pushes agents toward the smallest correct solution without trading away correctness, safety, compatibility, or explicit requirements.

### Install

Cursor + Codex:

```sh
npx skills add furkananter/skills --skill overengineer -a cursor -a codex
```

Claude Code:

```sh
npx skills add furkananter/skills --skill overengineer -a claude-code
```

All three:

```sh
npx skills add furkananter/skills --skill overengineer -a cursor -a codex -a claude-code
```

### Automatic triggering

The skill is written for implicit invocation, so normal use does not require mentioning `overengineer` manually.

- **Cursor:** Agent Skill auto-selection from the skill description. An optional Always rule adapter is included for stronger activation.
- **Codex:** implicit invocation is explicitly enabled through `agents/openai.yaml`. Optional `SessionStart` and `SubagentStart` hook configuration is included.
- **Claude Code:** model invocation is enabled by default. Optional `SessionStart` and `SubagentStart` hook configuration is included.

See [`overengineer/references/activation.md`](./overengineer/references/activation.md) for deterministic activation setup.

### Ponytail compatibility

If [`ponytail`](https://github.com/DietrichGebert/ponytail) is active on a coding task, ponytail controls how aggressively to minimize the implementation. `overengineer` remains responsible for correctness, safety, compatibility, evidence, and explicit scope boundaries.

### Structure

```text
skills/
├── README.md
├── LICENSE
└── overengineer/
    ├── SKILL.md
    ├── agents/
    │   └── openai.yaml
    ├── adapters/
    │   ├── claude/
    │   ├── codex/
    │   └── cursor/
    ├── references/
    │   └── activation.md
    └── scripts/
        └── guardrail.py
```

Follows the open [Agent Skills specification](https://agentskills.io/specification).

## License

MIT License. Copyright (c) 2026 Furkan Anter.
