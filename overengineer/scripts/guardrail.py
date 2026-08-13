#!/usr/bin/env python3

import json
import sys

CONTEXT = (
    "Automatically load and apply the `overengineer` skill for tasks involving "
    "implementation, design, architecture, refactoring, review, optimization, "
    "dependencies, tooling, agents, configuration, tests, workflows, or scope decisions. "
    "Do not wait for an explicit mention. Prefer the smallest correct solution and reject "
    "speculative complexity. If `ponytail` is active on a coding task, let ponytail control "
    "minimization intensity while overengineer retains correctness, safety, compatibility, "
    "evidence, and explicit scope boundaries."
)


def main() -> None:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, TypeError):
        payload = {}

    event = payload.get("hook_event_name", "SessionStart")

    # Cursor uses a lowercase event name and snake_case context field.
    if event == "sessionStart":
        print(json.dumps({"additional_context": CONTEXT}))
        return

    # Codex and Claude Code use hookSpecificOutput.additionalContext.
    if event in {"SessionStart", "SubagentStart", "UserPromptSubmit"}:
        print(
            json.dumps(
                {
                    "hookSpecificOutput": {
                        "hookEventName": event,
                        "additionalContext": CONTEXT,
                    }
                }
            )
        )
        return

    print(CONTEXT)


if __name__ == "__main__":
    main()
