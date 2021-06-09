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

#### Get all performances

```http
  GET /api/v1/performances

```

#### Common API use-cases:

```

1. => select channel, country, sum(impressions) as impressions, sum(clicks) as clicks from base_performance where date < '2017-06-01' group by channel, country order by clicks desc;
channel | country | impressions | clicks
------------------+---------+-------------+--------
adcolony | US | 532608 | 13089
apple_search_ads | US | 369993 | 11457
vungle | GB | 266470 | 9430
vungle | US | 266976 | 7937
...



2. select os,sum(installs) as installs from base_performance where date > '2017-05-01' and os = 'ios' group by date,os order by date ASC;

3. select os,sum(revenue) as revenue from base_performance where date > '2017-06-01' and country = 'US' group by os order by revenue desc;

4.

```

## Tech Stack

**Server:** Python version 3, Django, Djangorestframework

## Authors

- [@Marlinekhavele](https://github.com/Marlinekhavele/)

## License

MIT License

Copyright (c) 2021 Marline Khavele

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
