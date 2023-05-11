style:
	flake8 .

types:
	mypy learndjango --explicit-package-bases
	
test:
	python -m pytest
	
check:
	make style types test
