import pandas as pd
#import numpy as np
import random
from datetime import datetime, timedelta

# Define equipment types, their sensors, and units of measurement
equipment_sensors = {
    "Aseptic Filling Equipment": [("Temperature", "°C"), ("Pressure", "hPa"), ("Fill Volume", "mL"), ("Flow Rate", "L/min"), ("Vibration", "g")],
    "Lyophilization Systems": [("Chamber Temperature", "°C"), ("Vacuum Pressure", "hPa"), ("Condenser Temperature", "°C")],
    "Sterilization Equipment": [("Chamber Pressure", "hPa"), ("Steam Temperature", "°C"), ("Cycle Duration", "minutes")],
    "Isolator Systems": [("Particle Count", "particles/m³"), ("Air Pressure", "hPa"), ("Temperature", "°C"), ("Humidity", "%")],
    "Bioreactors": [("pH", "pH units"), ("Dissolved Oxygen", "mg/L"), ("Agitation Speed", "rpm"), ("Temperature", "°C")],
    "Inspection Systems": [("Fill Volume Accuracy", "mL"), ("Particle Detection Count", "count")],
    "Environmental Monitoring": [("Particle Count", "particles/m³"), ("Room Temperature", "°C"), ("Humidity", "%")],
    "PAT Tools": [("pH", "pH units"), ("Conductivity", "µS/cm"), ("Oxygen Levels", "ppm")],
    "CIP/SIP Systems": [("Fluid Temperature", "°C"), ("Flow Rate", "L/min"), ("Pressure", "hPa")],
    "Balances": [("Weight", "g"), ("Stability Status", "binary")],
    "Automation Software": [("System Health Status", "binary"), ("Throughput", "units/hour"), ("Error Rates", "%")]
}

# Define possible error messages for each sensor type
sensor_error_messages = {
    "Temperature": ["Overheating", "Temperature Sensor Failure", "Calibration Needed"],
    "Pressure": ["Low Pressure", "High Pressure", "Pressure Sensor Fault"],
    "Fill Volume": ["Inconsistent Fill Volume", "Overflow Detected", "Calibration Needed"],
    "Flow Rate": ["Flow Rate Too High", "Flow Blockage Detected"],
    "Vibration": ["Vibration Sensor Fault", "Excessive Vibration"],
    "Particle Count": ["High Particle Count", "Sensor Malfunction"],
    "pH": ["pH Out of Range", "pH Sensor Fault"],
    "Dissolved Oxygen": ["Low Oxygen Levels", "Sensor Calibration Needed"],
    "Agitation Speed": ["Agitation Speed Too High", "Motor Failure"],
    "Humidity": ["Humidity Sensor Fault", "High Humidity Detected"],
    "Conductivity": ["Conductivity Out of Range", "Calibration Required"],
    "Weight": ["Weight Inconsistency", "Scale Calibration Error"],
    "Cycle Duration": ["Cycle Time Exceeded", "Process Timeout"],
    "Oxygen Levels": ["Low Oxygen Levels", "Oxygen Sensor Fault"],
    "System Health Status": ["System Overload", "CPU Failure", "Memory Leak Detected"],
    "Throughput": ["Low Throughput", "Output Inconsistency"],
    "Error Rates": ["High Error Rate Detected"],
    "Stability Status": ["Unstable Operation", "Control System Failure"],
}

# Number of sensors to simulate (100 sensors)
total_sensors = 100

# Simulation parameters
start_date = datetime.now() - timedelta(days=90)  # 90 days of data
end_date = datetime.now()

# Generate a list of random timestamps within the 90-day period
def generate_random_timestamps(num_timestamps):
    return [start_date + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds()))) for _ in range(num_timestamps)]

# Function to generate synthetic sensor data (integers only)
def generate_sensor_data(sensor_type):
    if sensor_type in ["Temperature", "Chamber Temperature", "Condenser Temperature", "Fluid Temperature", "Room Temperature"]:
        return random.randint(20, 30)
    elif sensor_type in ["Pressure", "Vacuum Pressure", "Chamber Pressure", "Air Pressure"]:
        return random.randint(950, 1050)
    elif sensor_type in ["Fill Volume", "Fill Volume Accuracy"]:
        return random.randint(95, 105)
    elif sensor_type in ["Vibration"]:
        return random.randint(0, 1)
    elif sensor_type in ["Particle Count", "Particle Detection Count"]:
        return random.randint(0, 100)
    elif sensor_type in ["pH"]:
        return random.randint(6, 8)
    elif sensor_type in ["Dissolved Oxygen"]:
        return random.randint(4, 8)
    elif sensor_type in ["Flow Rate"]:
        return random.randint(1, 5)
    elif sensor_type in ["Weight"]:
        return random.randint(50, 200)
    elif sensor_type in ["Stability Status", "System Health Status"]:
        return random.choice([0, 1])
    elif sensor_type in ["Throughput"]:
        return random.randint(100, 1000)
    elif sensor_type in ["Error Rates"]:
        return random.randint(0, 5)
    elif sensor_type in ["Cycle Duration"]:
        return random.randint(30, 120)
    elif sensor_type in ["Conductivity"]:
        return random.randint(10, 100)
    elif sensor_type in ["Oxygen Levels"]:
        return random.randint(5, 20)
    else:
        return 0

# Generate synthetic data for 100 sensors
sensor_data_list = []

for i in range(total_sensors):
    equipment_type = random.choice(list(equipment_sensors.keys()))
    sensor_type, unit = random.choice(equipment_sensors[equipment_type])
    
    # Generate a random number of timestamps for each sensor (to vary data points per sensor)
    num_timestamps = random.randint(100, 200)  # Each sensor will have 100 to 200 readings
    random_timestamps = generate_random_timestamps(num_timestamps)
    
    for timestamp in random_timestamps:
        sensor_reading = generate_sensor_data(sensor_type)

        # Introduce random anomalies (5% chance for each data point)
        if random.random() < 0.05:
            sensor_reading = sensor_reading * random.randint(2, 5)
            is_anomaly = 1
            error_message = random.choice(sensor_error_messages.get(sensor_type, ["Unknown Error"]))
        else:
            is_anomaly = 0
            error_message = "No Error"

        # Add other columns
        sensor_status = random.choice(["Operational", "Faulty"])
        days_since_last_maintenance = random.randint(0, 180)
        operational_mode = random.choice(["Idle", "Running", "Cleaning", "Maintenance"])
        equipment_age = random.randint(1, 15)
        calibration_drift = round(random.uniform(-0.5, 0.5), 2)
        alarm_triggered = 1 if random.random() < 0.1 else 0

        # Determine the shift based on the timestamp
        if 6 <= timestamp.hour < 14:
            shift = "Morning"
        elif 14 <= timestamp.hour < 22:
            shift = "Evening"
        else:
            shift = "Night"

        sensor_data_list.append({
            "Timestamp": timestamp,
            "Day_of_Week": timestamp.strftime('%A'),
            "Shift": shift,
            "Sensor_ID": f"Sensor_{i+1}",
            "Equipment_Type": equipment_type,
            "Sensor_Type": sensor_type,
            "Reading": sensor_reading,
            "Unit": unit,
            "Anomaly": is_anomaly,
            "Error_Message": error_message,  # Add error message column
            "Sensor_Status": sensor_status,
            "Days_Since_Last_Maintenance": days_since_last_maintenance,
            "Operational_Mode": operational_mode,
            "Equipment_Age": equipment_age,
            "Calibration_Drift": calibration_drift,
            "Alarm_Triggered": alarm_triggered
        })

# Create a DataFrame to hold the generated data
sensor_data_df = pd.DataFrame(sensor_data_list)

# Save the generated data to a CSV file in the specified location
sensor_data_df.to_csv('C:/Users/mcall/synthetic_sensor_data_90_days.csv', index=False)

print("Synthetic sensor data with error messages generated and saved successfully.")



