install:
	poetry install

lint: black flake isort

lint-fix: isort black-fix

isort:
	isort .

black:
	black -l 120 -t py37 --check rio_discord_bot/ tests/

black-fix:
	black -l 120 -t py37 rio_discord_bot/ tests/

flake:
	flake8 rio_discord_bot/ tests/

unit:
	pytest -sv tests

unit-html:
	pytest --html=tests/reports/unit-test-report.html --self-contained-html -sv tests || true
	open tests/reports/unit-test-report.html

coverage:
	coverage run --source=jobs -m pytest tests/unit --junitxml=build/test.xml -v
	coverage report
	coverage xml -i -o build/coverage.xml

coverage-html:
	pytest --cov-report html --cov=jobs tests/unit || true
	open tests/reports/coverage/index.html

test: lint unit

.PHONY: install lint unit unit-html coverage coverage-html test