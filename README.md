# sfilter (Pre-Alpha)

Tool for filtering out stinky/smelling code

## Usage

### How to

```shell
python -c'import sfilter.main as sf;sf.run_all("<path_to_project>")'
```

### Run all checks example

```shell
PIPENV_IGNORE_VIRTUALENVS=1 pipenv run python -c'import sfilter.main as sf;sf.run_all("./sfilter")'
```

### Run step by step example

1. Clean before analysis:
    ```shell
    PIPENV_IGNORE_VIRTUALENVS=1 pipenv run python -c'import sfilter.main as sf;sf.clean_before_test()'
    ```
1. Run black:
    ```shell
    PIPENV_IGNORE_VIRTUALENVS=1 pipenv run python -c'import sfilter.main as sf;sf.run_black("./sfilter")'
    ```
1. Run isort:
    ```shell
    PIPENV_IGNORE_VIRTUALENVS=1 pipenv run python -c'import sfilter.main as sf;sf.run_isort("./sfilter")'
    ```
1. Run flake8:
    ```shell
    PIPENV_IGNORE_VIRTUALENVS=1 pipenv run python -c'import sfilter.main as sf;sf.run_flake8("./sfilter")'
    ```
1. Run radon:
    ```shell
    PIPENV_IGNORE_VIRTUALENVS=1 pipenv run python -c'import sfilter.main as sf;sf.run_radon("./sfilter")'
    ```
1. Run final checks:
    ```shell
    PIPENV_IGNORE_VIRTUALENVS=1 pipenv run python -c'import sfilter.main as sf;sf.check_quality()'
    ```

## Install and test the project

### Precondition

1. [make](https://www.gnu.org/software/make/) is installed
2. [pipenv](https://pipenv.pypa.io/en/latest/#install-pipenv-today) is installed
3. [pyenv](https://github.com/pyenv/pyenv#installation) 
   is installed with the following python versions:
     - 3.7.12
     - 3.8.12
     - 3.9.1 
4. Run make command:
   ```shell
   make install
   ```

### Test project

Test the project after each code change by running make:
```shell
make test
```

## Publish

### Prepare to publish the project

```shell
PIPENV_IGNORE_VIRTUALENVS=1 pipenv run python setup.py bdist_wheel
PIPENV_IGNORE_VIRTUALENVS=1 pipenv run pip install -e .
pipenv shell
python
```

```python
import src.sfilter.main as sf

sf.run_all("src/sfilter")
exit()
```

```shell
exit
PIPENV_IGNORE_VIRTUALENVS=1 pipenv run python setup.py sdist
tar tzf dist/sfilter-<version>.tar.gz 
```

### Upload to pypi

```shell
twine upload dist/*
```
