---
name: overengineer
description: Default anti-overengineering guardrail. Automatically use whenever a task involves writing, changing, fixing, refactoring, reviewing, designing, planning, optimizing, or choosing architecture, abstractions, dependencies, tools, agents, configuration, tests, workflows, or scope in software, product, research, writing, or operations. Prefer the smallest correct solution, reject speculative complexity, preserve existing behavior, and stop when requirements are satisfied.
license: MIT
metadata:
  author: furkananter
  version: "1.1.1"
---

# Overengineer

Keep the solution as small as possible without sacrificing correctness, safety, or maintainability.

## Trigger

Apply this skill automatically when the current task involves implementation, design, architecture, refactoring, review, optimization, dependencies, tooling, agents, configuration, tests, workflow complexity, future-proofing, or scope decisions. Do not wait for the user to mention `overengineer` explicitly.

Explicit requirements are requirements, not overengineering. Do not remove or reject requested behavior merely because a smaller product could exist.

## Core rule

Before adding a file, dependency, abstraction, configuration option, tool call, agent, fallback, optimization, or feature, ask:

> Does this materially help satisfy the current task?

- If no, do not add it.
- If unclear, leave it out until a concrete requirement or evidence justifies it.
- If yes, add the simplest version that fits the existing system.

Apply this guardrail silently. Do not turn it into a planning ceremony.

## Workflow

1. Reduce the request to one required outcome and its explicit constraints.
2. Identify the acceptance criteria. Do not invent extra goals.
3. Inspect only the context needed to make a correct change.
4. Prefer the smallest solution that follows existing patterns and preserves existing behavior.
5. Separate work into:
   - required now,
   - evidence-backed risk that must be handled now,
   - optional or speculative work.
6. Implement only the first two categories.
7. Run the narrowest checks that prove the changed behavior works.
8. Stop when the acceptance criteria pass.

## Default decisions

Prefer:

- reusing existing code over adding another layer,
- modifying an existing file over creating a new subsystem,
- a concrete implementation over a generic framework,
- existing dependencies and platform features over new packages or services,
- repository conventions over introducing a new pattern,
- targeted tests over unrelated test expansion,
- measured bottlenecks over premature optimization,
- actual use cases over hypothetical future requirements,
- a direct answer over research or tooling when current external facts are not needed,
- one clear recommendation over an option dump.

## Reject by default

Unless the user explicitly requires it or concrete evidence justifies it, do not add:

- unrelated refactors or cleanup,
- speculative abstractions, interfaces, factories, registries, or plugin systems,
- new dependencies, services, configuration, feature flags, or infrastructure,
- compatibility layers for unknown consumers,
- retries, caches, fallbacks, or defensive branches for unobserved failures,
- extra agents, automation, dashboards, or pipelines for a simple task,
- support for every imaginable edge case,
- rewrites of working code purely for style or theoretical purity.

## Do not underengineer

Simplicity is not an excuse to skip:

- correctness,
- security, privacy, or data integrity,
- explicitly required compatibility,
- tests for changed behavior,
- likely failure modes supported by evidence,
- legal, safety, or accessibility requirements,
- scope the user actually requested.

The target is the smallest correct solution, not the smallest possible solution.

## Stop condition

When the requested outcome is met and relevant checks pass, stop. Do not add a "nice to have" section unless the user asked for alternatives or a known risk remains.

When more complexity is proposed without a new requirement or new evidence, push back concisely. State one concrete reason the current solution is sufficient. Do not manufacture new objections, edge cases, or optimization work merely to continue the discussion.

## Final check

Before finishing, verify:

- Every changed file directly serves the task.
- Every new layer or dependency has a concrete present need.
- No existing behavior changed unintentionally.
- Validation covers the changed behavior.
- Removing anything else would harm correctness or the stated requirement.

If the task is solved, stop.
