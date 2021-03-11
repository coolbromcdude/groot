
.PHONY: help clean lint test
.DEFAULT: help
help:
	@echo  "  clean - Remove generated files from tests"
	@echo  "  lint 	- Lint code and run security scan"
	@echo  "  test  - Run app tests"
	@echo  ""

clean:
	@rm -rf .pytest_cache .coverage .pytest_cache

lint:
	@echo "\nRunning Pylint against source and test files...\n"
	@pylint --rcfile=setup.cfg **/*.py
	@echo "\nRunning YAML lint \n"
	@yamllint groot/

test:lint
	@pytest
