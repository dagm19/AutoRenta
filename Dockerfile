FROM python:3.12-slim-bullseye

# Setear variables de entorno
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /code

COPY poetry.lock pyproject.toml ./
RUN pip install --no-cache-dir poetry \
    && poetry install --no-root

COPY . .



