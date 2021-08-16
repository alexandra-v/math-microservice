FROM python:3.6
RUN pip install pipenv
RUN apt-get update
WORKDIR /code
COPY Pipfile .
COPY Pipfile.lock .
RUN pipenv install --deploy --system
COPY . /code