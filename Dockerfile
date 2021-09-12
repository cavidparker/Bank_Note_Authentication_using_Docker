FROM continuumio/miniconda3

RUN apt-get update -y && apt-get install
WORKDIR /app
COPY . /app


RUN conda install scikit-learn
RUN pip install -r requirements.txt

EXPOSE 8080

ENTRYPOINT [ "python" ]
CMD [ "app.py" ]

