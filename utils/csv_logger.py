"""
CSV Logger module.
Handles saving detection records to CSV file.
"""

import csv
import os
from datetime import datetime

def init_csv_if_not_exists():
    """Initialize CSV file with headers if it doesn't exist"""
    csv_file = 'data/history.csv'
    os.makedirs('data', exist_ok=True)
    
    # Create file with headers if it doesn't exist or is empty
    if not os.path.exists(csv_file) or os.path.getsize(csv_file) == 0:
        with open(csv_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Timestamp', 'Crop', 'Temperature', 'Humidity', 
                           'Soil_Moisture', 'Light', 'Status', 'Score'])
        print(f"✅ CSV file initialized with headers at: {csv_file}")

def save_detection(crop, temperature, humidity, soil_moisture, light, status, score):
    """
    Save detection record to CSV file.
    
    Args:
        crop (str): Crop type
        temperature (float): Temperature in °C
        humidity (float): Humidity percentage
        soil_moisture (float): Soil moisture percentage
        light (float): Light intensity percentage
        status (str): Overall status (GOOD/ATTENTION REQUIRED/CRITICAL)
        score (float): Suitability score
    """
    csv_file = 'data/history.csv'
    
    # Ensure directory exists and file is initialized
    os.makedirs('data', exist_ok=True)
    
    # Check if file exists and has headers
    file_exists = os.path.exists(csv_file)
    file_has_content = file_exists and os.path.getsize(csv_file) > 0
    
    with open(csv_file, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        
        # Write headers if file is new or empty
        if not file_exists or not file_has_content:
            writer.writerow(['Timestamp', 'Crop', 'Temperature', 'Humidity', 
                           'Soil_Moisture', 'Light', 'Status', 'Score'])
        
        # Write data
        writer.writerow([
            datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            crop,
            temperature,
            humidity,
            soil_moisture,
            light,
            status,
            score
        ])
    
    print(f"✅ Detection saved: {crop} - {status} - {score}%")

def get_history(limit=None):
    """
    Retrieve detection history.
    
    Args:
        limit (int, optional): Number of records to return
        
    Returns:
        list: List of dictionaries containing history records
    """
    csv_file = 'data/history.csv'
    history = []
    
    if os.path.exists(csv_file) and os.path.getsize(csv_file) > 0:
        try:
            with open(csv_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    history.append(row)
        except Exception as e:
            print(f"Error reading CSV: {e}")
    
    # Return limited records if specified
    if limit and history:
        return history[-limit:]
    return history