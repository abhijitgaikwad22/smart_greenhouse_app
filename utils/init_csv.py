"""
Initialize CSV file with headers and sample data
Run this script once to create the CSV file properly
"""

import os
import csv
from datetime import datetime, timedelta

def init_history_csv():
    """Initialize history.csv with headers and sample data"""
    csv_file = 'data/history.csv'
    
    # Create data directory if it doesn't exist
    os.makedirs('data', exist_ok=True)
    
    # Sample data
    sample_data = [
        {
            'Timestamp': (datetime.now() - timedelta(days=2)).strftime('%Y-%m-%d %H:%M:%S'),
            'Crop': 'Tomato',
            'Temperature': 24.5,
            'Humidity': 65,
            'Soil_Moisture': 55,
            'Light': 70,
            'Status': 'GOOD',
            'Score': 85
        },
        {
            'Timestamp': (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S'),
            'Crop': 'Lettuce',
            'Temperature': 22.0,
            'Humidity': 70,
            'Soil_Moisture': 45,
            'Light': 60,
            'Status': 'ATTENTION REQUIRED',
            'Score': 65
        },
        {
            'Timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'Crop': 'Capsicum',
            'Temperature': 28.0,
            'Humidity': 55,
            'Soil_Moisture': 35,
            'Light': 75,
            'Status': 'CRITICAL',
            'Score': 45
        }
    ]
    
    # Write to CSV
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['Timestamp', 'Crop', 'Temperature', 
                                              'Humidity', 'Soil_Moisture', 'Light', 
                                              'Status', 'Score'])
        writer.writeheader()
        writer.writerows(sample_data)
    
    print(f"✅ CSV file initialized with sample data at: {csv_file}")
    print(f"📊 Total records: {len(sample_data)}")

if __name__ == '__main__':
    init_history_csv()