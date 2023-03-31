style:
	flake8 .

types:
	mypy learndjango
	
check:
	make style types
