FROM python:3.12-slim

LABEL author="drwn03gm@gmail.com"
# Darwin Godoy

# Set enveronment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

#Install poetry and dependencies
COPY poetry.lock pyproject.toml /app/
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --only main --no-root

#Copy all files
COPY ./autorenta_project /app

#Run the application
ENTRYPOINT ["python", "main.py"]
CMD ["runserver", "0.0.0.0:80", "--noreload"]

