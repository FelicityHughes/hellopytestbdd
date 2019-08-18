# HelloWorld Python & pytest-bdd Demonstration

## About
This is a simple HelloWorld project that demonstrates how to set up a small
Python project with pytest-bdd tests.

## Dependencies
The program uses `pipenv` to manage its virtual environment.

## Execution
1. Go to the root of the project and launch a virtual environment with `pipenv shell`.
2. Type `PYTHONPATH="src" pytest --gherkin-terminal-reporter-expanded -v --cov=src` to run BDD tests.

Feature files are expected to live under the `features` directory with a `steps` subdirectory for step definitions.  The program itself lives in `src/hello`.