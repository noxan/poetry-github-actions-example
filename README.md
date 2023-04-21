# Poetry Github Actions Example

This is an example of how to use [Poetry](https://python-poetry.org/) with Github Actions.

## Workflows

1. Linters
    1. Pyright: Static type checking which requires dependencies to be installed
    2. Flake8: Linting (no dependencies required)
    3. Black: Formatting (no dependencies required)
2. Tests: Unit tests with pytest which requires dependencies to be installed

## References

- https://github.com/actions/setup-python
- https://github.com/snok/install-poetry https://github.com/marketplace/actions/install-poetry-action
- https://github.com/liskin/gh-problem-matcher-wrap
- https://jacobian.org/til/github-actions-poetry/
- [Solution if shell and os are not compatible](https://github.com/orgs/community/discussions/27143)

## Open issues

1. Poetry caching does not work on macOS
    ```
          - name: Cache poetry
            id: poetry-cache
            uses: actions/cache@v3
            with:
              path: ~/.local
              key: poetry-${{runner.os}}
    ```
