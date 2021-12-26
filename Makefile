gendiff:
	poetry run gendiff
install:
	poetry install
build: check
	@poetry build
package-install:
	python3 -m pip install --user dist/*.whl
publish:
	poetry publish --dry-run
force:
	python3 -m pip install --user --force-reinstall dist/*.whl
lint:
	poetry run flake8 .
coverage:
	poetry run pytest --cov=gendiff --cov-report xml tests/
selfcheck:
	poetry check
check: selfcheck lint
rec:
	asciinema rec




