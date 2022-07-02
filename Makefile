init:
	pip install -r requirements.txt

unit_tests:
	python -m pytest -v -m unit
integration_tests:
	python -m pytest -v -m integration
all_tests:
	python -m pytest -v --cov=.
