# ApatoScraper
> Scrap listing items from sewa-apartemen.net & jual-apartemen.com 

## Table of contents
* [Technologies](#technologies)
* [Setup](#setup)
* [Run Program](#run-program)

## Technologies
* Python - version 2.7
* Scrapy - version 1.8
* SQLAlchemy - version 1.3
* PostgreSQL - version 9

## Setup
Clone the project:
```commandline
> git clone https://github.com/matrachma/apato-scraper.git
> cd apato-scraper
```

Create and start a virtual environment:
```commandline
> virtualenv venv --no-site-packages
> source venv/bin/activate
```

Install the project dependencies:
```commandline
> pip install -r requirements.txt
```

Prepare postgresql database for this project on your localhost, and change db connection setting according to your configs:
``` python
# ./apatoScraper/settings.py
# PostgreSQL Connection Settings
DB_DRIVER = 'postgresql'
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_UNAME = 'postgres'
DB_PASSWORD = 'd0ck3r'
DB_NAME = 'apato_scraper'
CONNECTION_STRING = "{drivername}://{user}:{passwd}@{host}:{port}/{db_name}".format(
     drivername=DB_DRIVER,
     user=DB_UNAME,
     passwd=DB_PASSWORD,
     host=DB_HOST,
     port=DB_PORT,
     db_name=DB_NAME,
)
```

For storing raw HTML listing item, set `STORE_RAW` to `True`
```python
# Store raw HTML
STORE_RAW = True
```
Warning! It will store a huge data.

## Run Program
Scrap sewa-apartemen.net:
```commandline
> scrapy crawl sewa-apartemen
```

Scrap sewa-apartemen.net:
```commandline
> scrapy crawl jual-apartemen
```

All result will be stored in database & result file (json/csv). If you prefer not to store into database, just put comment
on `ITEM_PIPELINES` line in `settings.py`
