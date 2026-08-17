---
name: test-guard
description: Automatic test and coverage guardrail for code changes. Use whenever implementation, bug fixes, refactors, API changes, code deletion, or other changes affect executable or observable behavior. Ensure changed behavior is meaningfully tested, existing test patterns are followed, coverage stays at or above 80%, and verification status is reported honestly before completion.
license: MIT
metadata:
  author: furkananter
  version: "1.1.0"
---

# Test Guard

Do not complete a code-changing task without considering tests and coverage.

## Trigger

Apply automatically whenever executable or observable behavior changes.

This includes:

- features,
- bug fixes,
- refactors,
- API changes,
- code deletion,
- behavior-preserving rewrites.

Do not wait for the user to mention tests or coverage.

Skip only changes that cannot affect behavior, such as documentation, comments, or formatting.

## Core rule

Before completion, determine:

1. What behavior changed or could regress?
2. Do existing tests cover it?
3. Are new or updated tests required?
4. Is coverage still at or above 80%?
5. What verification actually ran?

If a meaningful test is required, add it.

## Test discipline

Prefer tests that:

- verify observable behavior,
- protect the changed or fixed behavior,
- cover relevant branches and failure paths,
- follow existing repository patterns,
- survive harmless implementation refactors.

Do not:

- add meaningless tests only to increase coverage,
- duplicate existing tests without reason,
- test implementation details without behavioral value,
- introduce a new testing framework or dependency unless required.

## Coverage

Maintain test coverage at or above 80% for code changes.

- Do not consider the task complete if coverage drops below 80%.
- Preserve or improve coverage when it is already above 80%.
- Use the repository's existing coverage tooling and calculation as the source of truth.
- Do not lower, bypass, or game coverage thresholds.
- Do not chase coverage numbers with low-value tests.

## Refactors

For behavior-preserving refactors, existing tests may be sufficient.

Add new tests only when touched behavior is insufficiently protected or a concrete regression risk is uncovered.

## Verification

Run the narrowest relevant verification allowed by repository and user instructions.

If the agent must not run tests or coverage:

- still add or update required tests,
- do not claim verification ran,
- provide the exact command the user should run.

## Completion

A code-changing task is complete only when:

- changed behavior is meaningfully covered, or there is a concrete reason no test is needed,
- coverage is at or above 80%,
- unrelated test work was not added,
- verification status is stated honestly.

Compilation alone is not sufficient verification.
