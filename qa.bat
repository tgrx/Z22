pipenv run python -m run_hw_tests

pipenv run black --check .
pipenv run flake8
pipenv run pylint run_hw_tests.py homeworks/ lessons/
