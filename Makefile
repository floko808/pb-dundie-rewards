.PHONY: install virtualenv ipython

install:
	@echo "Installing for dev environment"
	@.venv/bin/python -m pip install -e '.[dev]'

virtualenv:
	@.venv/bin/python -m pip -m venv .venv


ipython:
	@.venv/bin/ipython

test:
	@.venv/bin/pytest -s 

testci:
	@.venv/bin/pytest -v --junitxml=test-result.xml

watch:
	#@@.venv/bin/ptw -- -vv -s
	@ls **/*.py | entr pytest
