# Bengaluru_House_price_Prediction_deploy
it is whole project of ml prediction then Deploy
Bengaluru House Price Prediction
Project Overview
This project aims to predict house prices in Bengaluru using various regression models. The process involves data cleaning, feature engineering, model training, evaluation, and deployment through a web interface.

Table of Contents
Installation
Data Description
Data Preprocessing
Model Training
Model Evaluation
Model Deployment
Usage
Contributing
License
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/baengaluru_house_price_prediction.git
Navigate to the project directory:

bash
Copy code
cd baengaluru_house_price_prediction
Install the required packages:

bash
Copy code
pip install -r requirements.txt
Data Description
The dataset contains the following columns:

Number of bedrooms
Number of bathrooms
Living area
Lot area
Number of floors
Waterfront presence
Number of views
House condition
House grade
House area (excluding basement)
Basement area
Built year
Renovation year
Postal code
Latitude
Longitude
Living area renovation
Lot area renovation
Number of schools nearby
Distance from the airport
Price
Data Preprocessing
Loading Data:

Load the dataset using pandas.
Cleaning Data:

Remove duplicates.
Handle missing values.
Treat outliers, specifically in the price_per_sqft column.
Feature Engineering:

One-Hot Encode categorical features.
Scale numerical features using a standard scaler.
Pipeline:

Apply a pipeline to streamline preprocessing steps.
Model Training
Train different regression models to predict house prices:

Linear Regression
Lasso Regression
Ridge Regression
Model Evaluation
Evaluate the models using the following metrics:

Mean Squared Error (MSE)
Mean Absolute Error (MAE)
R-squared (R²) Score
Model Deployment
Save the best-performing model and deploy it using a web interface.

Save the Model:

python
Copy code
import joblib
joblib.dump(model, 'best_model.pkl')
Create a Web Interface:

Use PyCharm to create a Python script to load the saved model and handle user input.
Develop an index.html file for the web interface to take user inputs and display predictions.
Python Code Skeleton
python
Copy code
# app.py
from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)
model = joblib.load('best_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [float(x) for x in request.form.values()]
    prediction = model.predict([features])
    return render_template('index.html', prediction_text='Predicted House Price: ${:.2f}'.format(prediction[0]))

if __name__ == "__main__":
    app.run(debug=True)
HTML File
html
Copy code
<!-- index.html -->
<!DOCTYPE html>
<html>
<head>
    <title>House Price Prediction</title>
</head>
<body>
    <div>
        <h2>Enter House Features</h2>
        <form action="/predict" method="post">
            <!-- Add input fields for each feature -->
            <input type="text" name="feature1" placeholder="Feature 1">
            <input type="text" name="feature2" placeholder="Feature 2">
            <!-- Add more input fields as required -->
            <button type="submit">Predict</button>
        </form>
        <h2>{{ prediction_text }}</h2>
    </div>
</body>
</html>
Usage
Run the Flask app:

bash
Copy code
python app.py
Access the web interface at http://127.0.0.1:5000/.

Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.
