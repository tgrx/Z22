pipenv run pytest homeworks/
pipenv run pytest lessons/
pipenv run black --check .
pipenv run flake8
pipenv run pylint homeworks/ lessons/
