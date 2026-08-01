# Sprint Template

## Sprint objective

State one clear, measurable outcome.

## Requirements

- R-001: TBD

## Constraints

- Time, budget, platform, privacy, compatibility, and dependency constraints: TBD

## Acceptance criteria

- [ ] Observable behavior is defined.
- [ ] Unit and regression tests pass.
- [ ] Linting passes.
- [ ] Errors are logged and no failure is silent.
- [ ] Documentation is updated.
- [ ] Health and rollback behavior are verified where applicable.

## Deliverables

- Source changes
- Tests
- Documentation
- Review log entry

## Verification steps

1. Run `python -m unittest discover -s tests -v`.
2. Run `ruff check src tests`.
3. Review the GitHub Actions health summary.
4. Exercise acceptance criteria in the target environment.
5. Record evidence and remaining issues in `REVIEW.md`.

