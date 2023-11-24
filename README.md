
# currency-exchange-django

Basic Django application used to view currency exchange rates, created using mySQL database, Yahoo! dataset and Django

## Run Locally

Clone the project

```bash
  git clone https://link-to-project
```

Go to the project directory and then to server directory containing manage.py file

```bash
  cd my-project
  cd server
```

Install my-project with python 3.8+, and then install dependencies listed below.

```bash
  pip install django
  pip install django-admin-interface
  pip install djangorestfreamwork
  pip install pandas
  pip install PyMySQL
  pip install sqlparse
  pip install yfinance
```
    
Prepare migration and load initial data.

```bash
  py manage.py migrate

  py manage.py loaddata fixtures/currencies.json
```

Create superuser

```bash
  python manage.py createsuperuser
```

Start the server

```bash
  py manage.py runserver
```


Go to http://127.0.0.1:8000/loadstock/ for loading leatest data


## Running Tests

To run tests, run the following command

```bash
  py manage.py test
```

