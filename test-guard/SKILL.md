---
name: test-guard
description: Automatic testing and coverage guardrail for code changes. Use whenever implementation, bug fixes, refactors, behavior changes, API changes, or code deletion modifies executable behavior. Before completion, determine affected behavior, add or update focused tests when needed, consider coverage impact, follow existing test patterns, and report unrun verification honestly. Do not add meaningless tests solely to inflate coverage.
license: MIT
metadata:
  author: furkananter
  version: "1.0.0"
---

# Test Guard

Prevent code changes from being completed while relevant tests or coverage impact are forgotten.

## Trigger

Apply this skill automatically to any task that changes executable code or externally observable behavior, including features, bug fixes, refactors, API changes, behavior-preserving rewrites, and code deletion.

Do not wait for the user to mention tests, coverage, or `test-guard` explicitly.

Documentation-only, comment-only, formatting-only, and other non-behavioral changes do not require new tests unless they affect executable behavior.

## Core rule

Before completing a code-changing task, answer these questions:

1. What behavior changed or could regress?
2. Which existing tests cover it?
3. Do tests need to be added or updated?
4. What is the coverage impact?
5. What verification was actually run?

A code change is not complete until these questions have been considered.

## Workflow

1. Identify the changed behavior and likely regression surface.
2. Find the nearest existing test patterns. Reuse the project's framework, helpers, naming, and structure.
3. Decide whether existing tests are sufficient.
4. Add or update the smallest meaningful tests needed for the changed behavior.
5. Cover important branches, failure paths, and regressions when they are relevant to the change.
6. Consider coverage impact using the project's existing coverage tooling when available.
7. Run the narrowest useful verification allowed by the project and user instructions.
8. State clearly what was tested, what was not run, and why.

## Test quality

Prefer tests that:

- verify observable behavior,
- reproduce the bug before proving the fix when practical,
- protect changed branches and edge cases that can realistically regress,
- follow existing repository patterns,
- remain stable across harmless implementation refactors.

Avoid tests that:

- exist only to increase a coverage percentage,
- assert implementation details without behavioral value,
- duplicate existing coverage without a concrete reason,
- use giant snapshots when a focused assertion is clearer,
- introduce a new testing framework or dependency without a current requirement.

## Coverage

Coverage is a regression signal, not a vanity target.

- Use existing coverage tooling if the repository already has it.
- Do not introduce new coverage infrastructure unless requested or clearly required.
- Do not chase 100% coverage for its own sake.
- Do not knowingly reduce meaningful coverage of changed behavior without explaining why.
- Prefer covering important logic, branches, errors, and regressions over trivial lines.

If the project has an explicit coverage threshold, preserve it unless the user explicitly approves a change.

## Refactors

Behavior-preserving refactors usually need existing tests to prove behavior stayed intact. Add new tests only when the refactor exposes an uncovered regression risk or existing coverage is insufficient for the touched behavior.

## Execution policy

Respect repository and user instructions about who may run tests or scripts.

If agent-side execution is disallowed or unavailable:

- still add or update the required tests,
- do not pretend verification ran,
- provide the exact targeted command the user should run.

## Completion check

Before finishing a code-changing task, verify:

- changed behavior is covered by an existing or new meaningful test, or there is a concrete reason a test is not needed,
- relevant coverage impact was considered,
- no unrelated test expansion was introduced,
- verification status is stated honestly.

Do not mark the task complete merely because the implementation compiles or looks correct.
