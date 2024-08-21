# Define the Python interpreter
PYTHON=python3

# Define the source and test files
SRC=calculator.py
TEST=test_calculator.py

# Compile target
compile:
	@echo "Compiling the Python script into a standalone executable..."
	pip3 install pyinstaller
	pyinstaller --onefile calculator.py

# Build target
build: compile
	@echo "Building the application..."
	# Placeholder for additional build steps

# Test target
test: build
	@echo "Running unit tests on the compiled executable..."
	$(PYTHON) -m unittest $(TEST) || (echo "Tests failed" && exit 1)

# Package target
package: 
	@echo "Creating deployable package..."
	tar -czvf calculator_app.tar.gz $(SRC) $(TEST) Makefile Readme.txt dist/calculator
	@echo "Package created: calculator_app.tar.gz"

# Clean target
clean:
	@echo "Cleaning up..."
	rm -f calculator_app.tar.gz
	rm -rf __pycache__ build dist *.spec
	@echo "Clean up complete"
