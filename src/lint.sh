#!/bin/bash

set -o errexit -o nounset -o xtrace

ERROR=0
# Lint the entire project using flake8 and mypy with settings defined in setup.cfg.
flake8 --count "panel/" || ERROR=1
black --check "panel/" || ERROR=1
mypy --show-error-codes "panel/" || ERROR=1

exit $ERROR
