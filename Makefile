# Makefile

# Define the Python interpreter
PYTHON=python3

# Define the source and test files
SRC=calculator.py
TEST=test_calculator.py

# Default target
all: test package

# Test target
test:
	$(PYTHON) -m unittest $(TEST) || (echo "Tests failed" && exit 1)

# Package target
package:
	@echo "Creating deployable package..."
	tar -czvf calculator_app.tar.gz $(SRC) $(TEST) Makefile Readme.txt
	@echo "Package created: calculator_app.tar.gz"

# Clean target
clean:
	@echo "Cleaning up..."
	rm -f calculator_app.tar.gz
	@echo "Clean up complete"
