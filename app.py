#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 17:51:02 2021

@author: cavid
"""
from flask import Flask,request
import pandas as pd
import numpy as np
import pickle
import flasgger
from flasgger import Swagger



app = Flask(__name__)
Swagger(app)


pickle_in = open("classifier.pkl", "rb")
classifier = pickle.load(pickle_in)


@app.route('/')
def welcome():
    return "welcome all"

@app.route('/predict')
def predict_note_authentication():
    """Example endpoint returning a list of colors by palette
    This is using docstrings for specifications.
    ---
    parameters:
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
        
    responses:
        200:
            description: The output values
    """            
    
    variance = request.args.get("variance")
    skewness = request.args.get("skewness")
    curtosis = request.args.get("curtosis")
    entropy = request.args.get("entropy")
    prediction = classifier.predict([[variance,skewness,curtosis,entropy]])
    return "The predicted value is : " + str(prediction)

# input url: http://127.0.0.1:5000/predict?variance=2&skewness=3&curtosis=2&entropy=1
# http://127.0.0.1:5000/apidocs
# sudo docker build -t money_api .


@app.route('/predict_file', methods=["POST"])
def predict_note_file():
    
    """Let's Authenticate the Banks Note
    This is Using docstrings for specifications.
    ---
    parameters:
        
        - name: file
          in: formData
          type: file
          required: true
        
    responses:
        200:
            description: The Output Value
    """

    df_test = pd.read_csv(request.files.get("file"))
    prediction = classifier.predict(df_test)
    return "The predicted values for the csv is" + str(list(prediction))



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
