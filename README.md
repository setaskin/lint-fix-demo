# lint-fix-demo

A small Python module used as a target repository for an automated
lint-fixing agent ([dev-tool-agent](https://github.com/setaskin/dev-tool-agent)).

`inventory.py` intentionally contains real `flake8` violations (unused
imports, bare `except`, `== None` comparisons, an unused variable, and
overlong lines). The agent clones this repo, fixes the violations, and
opens a pull request with the changes.
