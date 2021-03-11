# Groot

Groot can generate all kinds of test data, fast, in large quantities and in multiple formats.

* Create custom JSON formatted schemas and generate data
* Output large amounts of data to storage quickly

## Setup 

Install [pipenv](https://pipenv-fork.readthedocs.io/en/latest/basics.html) to setup virtual environment and manage package dependencies (run and dev) for the project.

#### Installing pipenv
```shell
# homebrew
brew install pipenv

#pip
pip3 install pipenv
```

#### Starting the virtual environment
```shell
pipenv shell
```

#### Installing new dependencies
```shell
# dependencies for running the app
pipenv install boto3

# dependencies for developing the app
pipenv install --dev pytest
```
#### Locking currently installed packages
```shell
pipenv lock
```

## Tests
```shell
make test
```

## Running the application
#### Example 1:  Output 5000 records in csv format using the character schema
```shell
python3 -m groot --schema character --records 5000 --output-format csv
```

