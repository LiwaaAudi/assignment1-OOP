.PHONY: venv
venv:
	: # Create venv (One time only)
	: test -d venv || virtualenv -p --nostite-packages venv;
	test -d venv || python3 -m venv venv;
	@echo "To activate the virtual environment run following command:"
	@echo "source venv/bin/activate"