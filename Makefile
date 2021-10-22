.DEFAULT_GOAL := default

default:
	@echo "The following commands are supported:"
	@echo "install \t # Install pipenv"
	@echo "test \t # Test the project"

install:
	pipenv install

test: sfilter pytest

sfilter:
	@echo "Run sfilter"
	PIPENV_IGNORE_VIRTUALENVS=1 pipenv run python -c'import src.sfilter.main as sf;sf.run_all("./src")'
	PIPENV_IGNORE_VIRTUALENVS=1 pipenv run python -c'import src.sfilter.main as sf;sf.run_all("./tests")'

pytest:
	@echo "Run tests"
	PIPENV_IGNORE_VIRTUALENVS=1 pipenv run pytest -v
