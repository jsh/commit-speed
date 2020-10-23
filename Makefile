# The usual

SOURCES=$(wildcard *.py */*.py)

all: lint test

lint: black mypy pylint pylama

black: isort
	black -q ${SOURCES}

clean:
	git clean -dfx --exclude=bin --exclude=problems --exclude=results

coverage:
	- pytest --cov --cov-report=html
	open htmlcov/index.html

fixme:
	pylint -rn ${SOURCES} | sort -t: -k2 -n -r

isort:
	isort ${SOURCES}

mypy:
	mypy ${PWD}

pylama:
	pylama -o .config/pylama ${SOURCES}

pylint:
	pylint --disable=fixme -rn ${SOURCES} | sort -t: -k2 -n -r

test:
	pytest


.PHONY: all black clean fixme lint mypy pylint pylama isort test
