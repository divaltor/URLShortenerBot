## Development

### System dependencies
* Python 3.7+ (Python 3.8 with Docker)
* poetry
* Docker
* docker-compose

### Setup environment
* Copy .env.sample to .env file and change values in this file

## Deployment

### docker-compose

Pre-requirements:
* Docker
* docker-compose

Steps:
* Prepare .env file
* Run `docker-compose build && docker-compose up -d`
* Enjoy

Stopping:
* `docker-compose stop`

Destroying:
* `docker-compose down`

### Without docker

Install dependencies with [**Poetry**](https://python-poetry.org/docs/)
```cmd
$ poetry install
```
or via pip
```cmd
$ pip install -r requirements.txt
```

Setup `.env` file and compile translates (enter `url_shortener` directory)
```cmd
$ pybabel compile -d locales -D mybot
```