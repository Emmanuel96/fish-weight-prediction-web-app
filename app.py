#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 08:46:21 2022

@author: emmanuelaudu
"""

import pickle
import numpy as np
import pandas as pd
from flask import Flask, request
from flask import Flask, render_template
import sys

app=Flask(__name__)
 
pickle_in = open("model.pkl",'rb')
classifier=pickle.load(pickle_in)

@app.route('/')
def home():
    return render_template("model_test.html")


@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [x for x in request.form.getlist('data[]')]
    print(request.form.getlist('data[]'), flush = True)
    
    final_features = [np.array(int_features)]

    prediction = classifier.predict(final_features)

    prediction_text='The close price of bitcoin on this day will be {}'.format(prediction)

    return prediction_text


if __name__=='__main__':
    app.run(debug=True)
    
    
    
    
    
    
    
    
    
    
    
    