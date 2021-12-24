.DEFAULT_GOAL := default

default:
	@echo "The following commands are supported:"
	@echo "clean \t\t # Clean the project"
	@echo "install \t # Install project dependencies"
	@echo "reinstall \t # Clean the project and install from scratch"
	@echo "test \t\t # Test the project"

reinstall: clean install

clean:
	pipenv --rm

install:
	pipenv install


test: tox sfilter

tox:
	@echo "Run tox"
	pip3 install tox tox-pyenv
	pyenv local 3.7.12 3.8.12 3.9.1
	tox

pytest:
	@echo "Run tests"
	PIPENV_IGNORE_VIRTUALENVS=1 pipenv run pytest -v

sfilter:
	@echo "Run sfilter"
	PIPENV_IGNORE_VIRTUALENVS=1 pipenv run python -c'import src.sfilter.main as sf;sf.run_all("./src")'

