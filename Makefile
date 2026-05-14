.PHONY: install install-full dev test demo clean

install:
	pip install -e .

install-full:
	pip install -e ".[full]"

dev:
	pip install -e ".[full,dev]"

test:
	python -m pytest tests/ -v

demo:
	python -c "from scipub import demo; demo()"

clean:
	rm -rf figures/*.pdf figures/*.png
	rm -rf __pycache__ src/scipub/__pycache__
	rm -rf *.egg-info dist build
	rm -rf .pytest_cache
	rm -rf .venv
