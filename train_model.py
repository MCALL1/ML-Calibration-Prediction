# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 11:17:01 2024

@author: mcall
"""

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib
import numpy as np

# Load the synthetic data
data = pd.read_csv('C:/Users//synthetic_sensor_data_90_days.csv')

# Feature engineering: Create new features
data['pressure_deviation'] = data['Reading']
data['time_since_last_calibration'] = np.random.randint(1, 100, size=len(data))
data['temperature'] = np.random.randint(20, 30, size=len(data))
data['humidity'] = np.random.randint(30, 70, size=len(data))
data['stability_status'] = np.random.choice([0, 1], size=len(data))  # 0 for Stable, 1 for Unstable

# One-hot encode the 'stability_status' column
data['stability_status_Unstable'] = data['stability_status']

# Assuming 'needs_calibration' is a binary label column for demonstration
data['needs_calibration'] = np.random.choice([0, 1], size=len(data))

# Select features and labels for training
features = data[['pressure_deviation', 'temperature', 'humidity', 'time_since_last_calibration', 'stability_status_Unstable']]
labels = data['needs_calibration']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.3, random_state=42)

# Normalize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# Save the trained model and the scaler
joblib.dump(model, 'C:/Users//trained_model_rf.pkl')
joblib.dump(scaler, 'C:/Users//scaler.pkl')

print("Model and scaler saved successfully.")
