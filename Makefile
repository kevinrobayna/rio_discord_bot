install:
	poetry install

lint: black flake isort

lint-fix: isort black-fix

isort:
	poetry run isort .

black:
	poetry run black -l 120 -t py37 --check rio_discord_bot/ tests/

black-fix:
	poetry run black -l 120 -t py37 rio_discord_bot/ tests/

flake:
	poetry run flake8 rio_discord_bot/ tests/

unit:
	poetry run pytest -sv tests

unit-html:
	poetry run pytest --html=tests/reports/unit-test-report.html --self-contained-html -sv tests || true
	open tests/reports/unit-test-report.html

coverage:
	poetry run coverage run --source=jobs -m pytest tests/unit --junitxml=build/test.xml -v
	poetry run coverage report
	poetry run coverage xml -i -o build/coverage.xml

coverage-html:
	poetry run pytest --cov-report html --cov=jobs tests/unit || true
	open tests/reports/coverage/index.html

test: lint unit

.PHONY: install lint unit unit-html coverage coverage-html test