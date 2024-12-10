# python-rec-task
A simple application for retrieving currency rates.

# Requirments
- uv=0.5.1
- python>=3.13
- django>=5.1.4 
- yfinance>=0.2.50

For development:
- code formatter ruff>=0.8.2

# Running application
To start the application run `uv manage.py runserver`.

# Admin interface
To access admin interface first create superuser with `uv run manage.py createsuperuser`.
Then you can log in with provided credentials.

# Running tests
To run tests do: `uv run manage.py test`

# Additional features
Additionaly to required features the app provides ordering and filtering results:
- to sort the results in the ascending/descending order pass "asc"/"desc" as query parameters
- to filter the results to ones that start/end with chosen letter pass "starting letter/"ending letter" as query parameters