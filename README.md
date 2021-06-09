# Performance API

performance metrics API shows impressions, clicks, installs, spend, revenue for a given date, advertising channel, country and operating system.

## Run Locally

Clone the project

```bash
  git clone https://github.com/Marlinekhavele/PerformanceAPI
```

Go to the project directory

```bash
  cd app
```

Create a virtualenv environment

```bash
 virtualenv env -p python3.6

 source env/bin/activate

```

Install dependencies

```bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

```

Start the server

```bash
  ./manage.py runsever
```

## Running Tests

To run tests, run the following command

```bash
  ./manage.py run test
```

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`DEBUG=True`

`SECRET_KEY = ( "django-insecure-@w=dkzvdvdh=wz0h++-e8yx@&xw3)o-9*wum07jtz#q)-*+1os" )`

DB Configuration

`DB_NAME=performance`

`DB_USER=postgres`

`DB_PASSWORD=password`

`DB_HOST=localhost`

## API Reference and documentation

```http
  http://localhost:8000/api/v1/docs
```

## Tech Stack

**Server:** Python version 3, Django, Djangorestframework

## Authors

- [@Marlinekhavele](https://github.com/Marlinekhavele/)

## License

[MIT](https://choosealicense.com/licenses/mit/)

Common API use-cases:

1. select channel, country, sum(impressions) as impressions, sum(clicks) as clicks from base_performance where date < '2017-06-01' group by channel, country order by clicks desc;
