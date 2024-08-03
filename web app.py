from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model and feature selector
model = joblib.load('model/RUL_random_forest_model1.pkl')
selector = joblib.load('model/selector1.pkl')


# Route for the home page
@app.route('/')
def home():
    return render_template('index2.html')


# Route to handle form submission and make predictions
@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve data from form
    features = [float(request.form.get('cycle_index')),
                float(request.form.get('voltage')),
                float(request.form.get('time_at_4_15v'))]

    # Preprocess the features
    features_scaled = np.array(features).reshape(1, -1)
    features_selected = selector.transform(features_scaled)

    # Make prediction
    prediction = model.predict(features_selected)

    # Return prediction as JSON
    return jsonify({'prediction': prediction[0]})


if __name__ == '__main__':
    app.run(debug=True)
