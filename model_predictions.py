# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 14:13:40 2024

@author: mcall
"""
import pandas as pd
import numpy as np
import joblib
from datetime import datetime

# Load the trained model and scaler
try:
    model = joblib.load('C:/Users////trained_model_rf.pkl')
    scaler = joblib.load('C:/Users////scaler.pkl')
    
    # Load new data for predictions
    new_data = pd.read_csv('C:/Users////synthetic_sensor_data_90_days.csv')
except FileNotFoundError as e:
    print(f"File not found: {e}")
    exit()
except Exception as e:
    print(f"An error occurred: {e}")
    exit()

# Feature engineering for new data
new_data['pressure_deviation'] = new_data['Reading']
new_data['time_since_last_calibration'] = np.random.randint(1, 100, size=len(new_data))
new_data['temperature'] = np.random.randint(20, 30, size=len(new_data))
new_data['humidity'] = np.random.randint(30, 70, size=len(new_data))
new_data['stability_status'] = np.random.choice([0, 1], size=len(new_data))  # 0 for Stable, 1 for Unstable
new_data['stability_status_Unstable'] = new_data['stability_status']

# Select features for prediction
features = new_data[['pressure_deviation', 'temperature', 'humidity', 'time_since_last_calibration', 'stability_status_Unstable']]

# Normalize the new data using the saved scaler
features_scaled = scaler.transform(features)

# Generate predictions
predictions = model.predict(features_scaled)

# Add predictions and timestamp to the DataFrame
new_data['Calibration_Needed'] = predictions
new_data['Prediction_Timestamp'] = datetime.now()

# Add descriptions and recommendations based on predictions
descriptions = []
recommendations = []

for index, row in new_data.iterrows():
    if row['Calibration_Needed'] == 1:
        if row['pressure_deviation'] > 30:
            description = "High pressure deviation detected."
            recommendation = "Schedule calibration and inspect pressure sensors for potential leaks."
        elif row['temperature'] > 28:
            description = "Temperature exceeds normal operating range."
            recommendation = "Schedule calibration and check cooling systems."
        else:
            description = "Unstable operating conditions detected."
            recommendation = "Perform a detailed equipment check and recalibrate as needed."
    else:
        description = "Operating within normal parameters."
        recommendation = "Continue routine monitoring."

    descriptions.append(description)
    recommendations.append(recommendation)

# Add the descriptions and recommendations to the DataFrame
new_data['Description'] = descriptions
new_data['Recommendation'] = recommendations

# Save predictions to a new CSV file
output_path = 'C:/Users////model_predictions_output.csv'
new_data.to_csv(output_path, index=False)

# Output success message and show a summary
print(f"Predictions generated and saved successfully to {output_path}")
print(f"Number of calibration needs detected: {new_data['Calibration_Needed'].sum()}")
print(new_data[['Timestamp', 'Sensor_ID', 'Calibration_Needed', 'Description', 'Recommendation']].head())

