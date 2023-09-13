===========================

## Structure
- **ext_selenium** folder contains selenium extensions.
- **tests** folder with tests

## How to run
### Preconditions
- [Python 3.10+](https://www.python.org/downloads), <br>
- [Poetry](https://python-poetry.org/docs/#installation) <br>
- Allure for reports https://docs.qameta.io/allure/

### Installation
1. clone repo
2. Install required libraries. In project root perform:
```sh
poetry install --no-root
```

### Running tests
#### Locally
1. In project root perform
```sh
poetry run pytest --color=yes --alluredir=./tmp/allure_results TEST_DIRECTORY
```
`TEST_DIRECTORY` - path to tests you gonna run (e.g. `./tests` to run all tests in project)

To serve allure reports after run locally please do the following. The report will be opened automatically in the browser.
```sh
allure serve ./tmp/allure_results
```
