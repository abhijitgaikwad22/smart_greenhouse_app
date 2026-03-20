# Smart Greenhouse App

A Flask-based smart agriculture web application for monitoring greenhouse conditions, analyzing crop suitability, and generating recommendations for Maharashtra-specific crops.

## Overview

This project lets users enter greenhouse/environment values manually and analyze them against crop-specific rules. It provides:

- crop-wise environmental analysis
- condition scoring and health status
- English and Marathi alerts/recommendations
- CSV-based history tracking
- dashboard analytics
- PDF and CSV export

## Features

- User login with session-based access control
- Environment analysis using temperature, humidity, soil moisture, and light inputs
- Crop rules tailored to Maharashtra regions and seasons
- Bilingual result output with Marathi support
- Detection history stored in `data/history.csv`
- Dashboard with totals, average score, and recent alerts
- Export current report as PDF
- Export historical records as CSV

## Tech Stack

- Python
- Flask
- pandas
- reportlab
- matplotlib
- numpy
- python-dotenv

## Project Structure

```text
smart_greenhouse_app/
|-- app.py
|-- requirements.txt
|-- data/
|   `-- history.csv
|-- routes/
|   |-- auth_routes.py
|   |-- dashboard_routes.py
|   `-- detection_routes.py
|-- services/
|   |-- crop_rules.py
|   |-- decision_engine.py
|   |-- export_service.py
|   `-- suggestion_engine.py
|-- static/
|   |-- script.js
|   `-- style.css
|-- templates/
|   |-- about.html
|   |-- crop_comparison.html
|   |-- crop_recommendation.html
|   |-- dashboard.html
|   |-- detect.html
|   |-- fertilizer_guide.html
|   |-- index.html
|   `-- login.html
`-- utils/
    |-- csv_logger.py
    `-- init_csv.py
```

## Installation

1. Clone or download the project.
2. Open a terminal in the project folder.
3. Create and activate a virtual environment.
4. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the App

Use:

```bash
python app.py
```

The Flask app starts in debug mode by default.

Open in your browser:

```text
http://127.0.0.1:5000/
```

## Default Login

- Username: `admin`
- Password: `admin123`

These credentials are currently hardcoded in `routes/auth_routes.py`.

## Main Pages

- `/` - Landing page
- `/login` - Login page
- `/detect` - Environment detection form and analysis
- `/dashboard` - Analytics dashboard
- `/about` - About page
- `/crop-comparison` - Crop comparison page
- `/crop-recommendation` - Crop recommendation page
- `/fertilizer-guide` - Fertilizer guide page
- `/export/pdf` - Export current detection result as PDF
- `/export/csv` - Export detection history as CSV

## How It Works

1. The user logs in.
2. The user enters crop and environment values.
3. The app compares those values against crop ranges from `services/crop_rules.py`.
4. `services/decision_engine.py` generates:
   - status (`GOOD`, `ATTENTION REQUIRED`, or `CRITICAL`)
   - score
   - alerts
   - recommendations
   - Marathi guidance
   - crop-specific regional information
5. The result is saved to `data/history.csv`.
6. The dashboard reads the CSV and shows analytics.

## Data Storage

The app stores detection history in:

```text
data/history.csv
```

If the file does not exist, it is created automatically with headers.

You can also initialize sample history data with:

```bash
python utils/init_csv.py
```

## Notes

- The project currently uses manual input values, not live IoT sensor integration.
- Authentication is basic and intended for demo or academic-project use.
- A `SECRET_KEY` can be provided through environment variables for better security.

## Future Improvements

- Add real sensor integration
- Store users and records in a database
- Replace hardcoded credentials with secure authentication
- Add charts and richer analytics
- Improve export formatting and multilingual rendering

## License

This project is intended for educational and academic use unless you add your own license.
