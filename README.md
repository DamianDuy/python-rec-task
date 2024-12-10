# Currency App
A simple application for retrieving currency rates from the Yahoo API.

## Prerequisites
For project development [uv](https://docs.astral.sh/uv/) package manager was used.
To initialize the project make sure to have it installed (preferably the latest version),
and then run `uv sync`.

## Running application
To start the application run `uv run manage.py runserver`.

## Admin interface
To access admin interface first create superuser with `uv run manage.py createsuperuser`.
Then you can log in with provided credentials in the `http://127.0.0.1:8000/admin/`.

## Running tests
To run tests do: `uv run manage.py test`

## Additional features
Additionaly to required features the app allows ordering and filtering of the currency list:
- to sort the list in the ascending/descending order pass `asc`/`desc` respectively as query parameters
- to filter the list to currency codes that start/end with a chosen string pass `startsWith`/`endsWith` respectively as query parameters