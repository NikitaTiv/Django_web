style:
	flake8 .

types:
	mypy learndjango
	
test:
	python -m pytest
	
check:
	make style types test
