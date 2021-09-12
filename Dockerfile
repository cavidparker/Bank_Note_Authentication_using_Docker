FROM continuumio/miniconda3

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

RUN apt-get update -y && apt-get install

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./


RUN conda install scikit-learn
RUN pip install -r requirements.txt




CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app

