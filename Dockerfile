FROM python:3.11-alpine

ENV LIBRARY_PATH=/lib:/usr/lib \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  PATH="/root/.local/bin:$PATH" \
  POETRY_VERSION=1.3.1

# System deps:
RUN apk update \
    && apk --no-cache add curl bash

# Project initialization:
RUN curl -sSL https://install.python-poetry.org | python3 -

WORKDIR /code

RUN curl -O https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh \
    && chmod +x wait-for-it.sh

COPY poetry.lock pyproject.toml /code/
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

# Creating folders, and files for a project:
COPY . /code

RUN chmod -R +x /code/docker/django/