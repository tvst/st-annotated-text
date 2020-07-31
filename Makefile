.PHONY: help
help:
	@# Magic line used to create self-documenting makefiles.
	@# See https://stackoverflow.com/a/35730928
	@awk '/^#/{c=substr($$0,3);next}c&&/^[[:alpha:]][[:alnum:]_-]+:/{print substr($$1,1,index($$1,":")),c}1{c=0}' Makefile | column -s: -t

.PHONY: develop
# Set up development environment
develop:
	pipenv install --dev
	pipenv run python setup.py develop
	pipenv shell

.PHONY: install
# Install in your current Python environment
install:
	pipenv run python setup.py install

.PHONY: test
# Run unit tests
test:
	pytest tests/

.PHONY: clean
# Remove temporary files
clean:
	rm -rf dist
	rm -rf build
	rm -rf *.egg-info
	rm -f Pipfile.lock

.PHONY: distribute
# Distributes the package to PyPI
distribute:
	rm -rf dist
	python setup.py sdist
	twine upload dist/*
