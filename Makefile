.PHONY: install virtualenv ipython clean test pflake8

install:
	@echo "Installing for dev environment"
	@.venv/bin/python -m pip install -e '.[dev]'

virtualenv:
	@.venv/bin/python -m pip -m venv .venv


ipython:
	@.venv/bin/ipython

lint:
	@.venv/bin/pflake8

test:
	@.venv/bin/pytest -s 

testci:
	@pytest -v --junitxml=test-result.xml

watch:
	#@@.venv/bin/ptw -- -vv -s
	@ls **/*.py | entr pytest
