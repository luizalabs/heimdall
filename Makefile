SOURCE=heimdall

VERSION := 1.0.0

install-test:
	pip install -r requirements_test.txt

test:
	coverage run -m unittest
	coverage report
	