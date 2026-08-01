# Crestline AI Project Template

The standard starting point for production-minded AI automation projects at Crestline Partners. It keeps MVP delivery lightweight while establishing consistent documentation, testing, logging, health checks, and release discipline.

## Engineering principles

- Ship small, iterative releases.
- Test before merge.
- Never allow silent failures; surface actionable errors.
- Use clear, structured logging.
- Provide health checks for deployed services.
- Preserve backwards compatibility where practical.
- Treat documentation as mandatory.
- Add regression tests for every feature.

## Development workflow

1. Define the project in `PROJECT.md` and the sprint in `TASK.md`.
2. Select prioritized work from `BACKLOG.md`.
3. Create a focused branch, implement the smallest useful change, and add tests.
4. Run tests and linting locally, then open a pull request.
5. Merge only after the CI health summary passes and CTO review is complete.
6. Record the completed sprint in `REVIEW.md` and update `CHANGELOG.md`.

## Chrome Agent workflow

1. Give the Chrome Agent a sprint objective and the relevant acceptance criteria from `TASK.md`.
2. Ask it to inspect the current GitHub Action, issue, or pull request in the active tab.
3. Keep changes small and require the agent to run tests, inspect the workflow result, and fix failures.
4. Require a handoff containing the repository URL, commit hash, workflow run, verification results, and remaining recommendations.

Never paste secrets into prompts, logs, source files, or screenshots.

## CTO review workflow

The CTO reviews business alignment, architecture, security, operational readiness, test coverage, backwards compatibility, and the CI health summary. Decisions and follow-up work are recorded in `REVIEW.md` and `BACKLOG.md` before approval.

## Start a new project

1. On GitHub, select **Use this template** and create a repository.
2. Clone the new repository and create a feature branch.
3. Replace the placeholders in `PROJECT.md`, `TASK.md`, and `BACKLOG.md`.
4. Add implementation code under `src/` and regression tests under `tests/`.
5. Configure deployment secrets in the repository or environment settings, never in source control.

## Run tests

```bash
python -m unittest discover -s tests -v
python -m pip install ruff
ruff check src tests
```

## Deploy

Deployment is intentionally platform-neutral. Document the target, environments, release command, rollback procedure, health endpoint, and required approvals in `PROJECT.md`. Deploy immutable, tested commits through CI/CD and verify health checks immediately after release.

