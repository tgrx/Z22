pipenv run pytest .
pipenv run black --check .
pipenv run flake8
pipenv run pylint run_hw_tests.py homeworks/ lessons/
