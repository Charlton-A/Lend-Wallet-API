init:
	pip install -r requirements.txt

unit_tests:
	python -m pytest -v -m unit --cov=.
