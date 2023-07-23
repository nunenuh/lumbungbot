.PHONY: venv

venv:
	@echo "Activating virtual environment"
	@source venv/bin/activate

run:
	PYTHONAPP=.:src python src/lumbungbot/main.py

run-test:
ifdef dst
	PYTHONPATH=.:src python -m pytest $(dst) -v
else
	PYTHONPATH=.:src python -m pytest -v
endif

run-test-cov:
	@PYTHONPATH=.:src:$PYTHONPATH pytest --cov=src --cov-report=xml

precommit:
	pre-commit run --all-files
