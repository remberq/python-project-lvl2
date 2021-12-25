gendiff:
	poetry run gendiff
install:
	poetry install
build:
	poetry build
package-install:
	python3 -m pip install --user dist/*.whl
publish:
	poetry publish --dry-run
force:
	python3 -m pip install --user --force-reinstall dist/*.whl
lint:
	poetry run flake8 gendiff
pytest:
	poetry run pytest --cov tests/