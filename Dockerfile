FROM continuumio/miniconda3

RUN apt-get update -y && apt-get install
WORKDIR /app
COPY . /app


RUN conda install scikit-learn
RUN pip install -r requirements.txt

# Expose port 
ENV PORT 8080

ENTRYPOINT [ "python" ]
CMD [ "flask_api_using_flasgger.py" ]

