PYTHON=python

.PHONY
	install
	test
	clean
# run
# clean
# setup

.DEFAULT_GOAL test


install:
	$(PYTHON) -m pip install -r requirements.txt

test:
	$(PYTHON) -m tests

clean:
	find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf