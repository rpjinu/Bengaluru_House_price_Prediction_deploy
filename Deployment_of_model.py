#flask, scikit-learn,pandas,pickle-mixin
import pandas as pd
import numpy as  np
from flask import Flask,render_template,request
import pickle

app=Flask(__name__)
data=pd.read_csv("Bengaluru_house_price_cleaned.csv")
pipe=pickle.load(open("final_ridge_model.pkl",'rb'))

@app.route('/')
def index():
    locations = sorted(data["location"].unique())
    return render_template('index.html',locations=locations)

@app.route('/predict',methods=['POST'])
def predict():
    location=request.form.get('location')
    bhk=request.form.get('bhk')
    bath=request.form.get('bath')
    sqft=request.form.get('sqft')

    print(location,bhk,bath,sqft)
    input=pd.DataFrame([[location,sqft,bath,bhk]],columns=['location','sqft','bath','bhk'])
    prediction=pipe.predict(input)[0]*100000


    return str(prediction,2)

if __name__=="__main__":
    app.run(debug=True,port=5001)

