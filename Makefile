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

fmt:
	@.venv/bin/isort dundie tests integration
	@.venv/bin/black dundie tests integration

test:
	@.venv/bin/pytest -s --forked
testci:
	@pytest -v --junitxml=test-result.xml -s --forked

watch:
	# @.venv/bin/ptw
	@ls **/*.py | entr pytest --forked

clean:
	@find ./ -name '*.pyc' -exec rm -rf {} \;
	@find ./ -name '__pycache__' -exec rm -rf {} \;
	@find ./ -name 'Thumbs.db' -exec rm -rf {} \;
	@find ./ -name '*~' -exec rm -rf {} \;
	@rm -rf .cache
	@rm -rf .pytest_cache
	@rm -rf .mypy_cache
	@rm -rf build
	@rm -rf dist
	@rm -rf *.egg-info
	@rm -rf htmlcov
	@rm -rf .tox/
	@rm -rf docs/_build

build:
	@python3 setup.py sdist bdist_wheel

publish-test:
	@twine upload --repository testpypi dist/*

publish:
	twine upload  dist/*
	