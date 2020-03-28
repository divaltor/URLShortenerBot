FROM python:3.8.2-slim-buster

WORKDIR /code

RUN pip install poetry

COPY poetry.lock pyproject.toml /code/

RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

COPY . /code/