# Automatic activation

`overengineer` is designed to trigger implicitly from its `description`. The adapters below are optional when you want a stronger, always-on guarantee.

## Cursor

Cursor can auto-select Agent Skills, but its `sessionStart` hook context injection has had reliability issues. For a static guardrail, use the included Always rule adapter instead.

After a project install:

```sh
mkdir -p .cursor/rules
cp -n .agents/skills/overengineer/adapters/cursor/overengineer.mdc .cursor/rules/overengineer.mdc
```

This rule does not duplicate the skill. It only tells Cursor to load `overengineer` automatically for implementation and complexity decisions.

## Codex

Codex already supports implicit skill invocation and this skill explicitly sets `policy.allow_implicit_invocation: true` in `agents/openai.yaml`.

For deterministic session and subagent activation, merge the entries from:

```text
.agents/skills/overengineer/adapters/codex/hooks.json
```

into your project:

```text
.codex/hooks.json
```

Do not overwrite an existing hooks file. Codex requires review/trust for non-managed command hooks.

## Claude Code

Claude Code can invoke skills automatically by default based on their description.

For deterministic session and subagent activation, merge the entries from:

```text
.claude/skills/overengineer/adapters/claude/settings.json
```

into:

```text
.claude/settings.json
```

Do not overwrite existing settings. The hook uses `SessionStart` and `SubagentStart` to remind Claude to load the skill automatically.

## Why not one universal hook file?

The three hosts do not share one hook configuration format or installation location. Keeping one portable `SKILL.md` as the source of truth and thin host adapters avoids coupling the skill to one agent.
