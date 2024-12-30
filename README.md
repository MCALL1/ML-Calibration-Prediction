Sensor Data Calibration Prediction Project

This project involves building a machine learning pipeline to predict whether sensor equipment requires calibration based on environmental and operational data. The code is split into two main scripts:

Model Training Script (train_model.py)
Prediction and Analysis Script (predict_and_analyze.py)

    Model Training Script (train_model.py)

This script is responsible for loading synthetic sensor data, performing feature engineering, training a classification model, and saving the trained model along with the scaler.

Data Processing: Loads and preprocesses sensor data from a CSV file. Creates synthetic features such as pressure_deviation, temperature, humidity, time_since_last_calibration, and stability_status (indicating stable or unstable sensor operation).
Feature Engineering: Adds new features and performs one-hot encoding for categorical variables.
Model Training: Uses a RandomForestClassifier from scikit-learn as the primary machine learning model. The classifier is trained to predict the needs_calibration label, indicating whether a sensor needs calibration.
Normalization: Scales the features using StandardScaler to improve model performance and ensure standardized input.
Model Saving: Serializes and saves the trained model and scaler using joblib for use in future predictions.

Key Processes 

Machine Learning Model: Random Forest Classifier
Data Processing Techniques: Feature Engineering, One-Hot Encoding, Data Scaling
File Handling: Model and scaler are saved as .pkl files for later use.

    Prediction and Analysis Script (predict_and_analyze.py)

This script loads the pre-trained model and scaler, processes new sensor data, generates predictions, and provides actionable insights based on the model's output.

Model and Scaler Loading: Loads the saved model and scaler to make predictions on new data.
Feature Engineering on New Data: Similar to the training process, it generates features (pressure_deviation, temperature, humidity, time_since_last_calibration, stability_status) for consistency with the model.
Prediction Generation: Uses the pre-trained Random Forest model to predict if calibration is needed for each sensor.
Detailed Analysis: Provides contextual descriptions and recommendations based on the prediction. For example:
    If pressure_deviation is high, a recommendation for sensor inspection is provided.
    If the temperature exceeds a threshold, it suggests cooling system checks.
Result Saving: Saves the predictions, descriptions, and recommendations to a CSV file for easy review.

Key Processes and Models

Machine Learning Prediction: Uses the loaded Random Forest model for predictions.
Data Processing and Feature Engineering: Ensures the new data is compatible with the model's input format.
Analysis and Recommendations: Generates actionable insights based on the model’s predictions.
File Handling: Saves results with predictions, descriptions, and recommendations as a .csv file.

Project Summary

This project demonstrates a full machine learning pipeline, from data processing and model training to real-time predictions and actionable insights. The use of synthetic sensor data highlights how machine learning can be applied in maintenance prediction and calibration recommendations for industrial applications. Both scripts work in tandem to create an end-to-end solution for predictive maintenance. 

Technical support - Michael Call
  317 439 5854 
