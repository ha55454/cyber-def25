import pandas as pd
import joblib
import os

# Load trained model
model = joblib.load("model.pkl")

# Define paths
input_file = "/input/logs/sample_log.csv"
output_file = "/output/alerts.csv"

# Read network logs
data = pd.read_csv(input_file)

# Run prediction
predictions = model.predict(data)

# Add prediction column
data['prediction'] = predictions

# Save alerts
data.to_csv(output_file, index=False)

print("Threat detection completed successfully!")
print("alerts.csv generated in /output folder")
