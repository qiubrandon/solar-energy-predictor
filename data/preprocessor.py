import pandas as pd
from src.solar_calc import calculate_solar_zenith_angle

def preprocess_api_data(api_data):
    # Convert API data into a DataFrame
    features = pd.DataFrame([{
        'Temperature': api_data['temperature'],
        'Relative Humidity': api_data['humidity'],
        'Cloud Type': api_data['cloud_type'],  # Map to categorical index
        'Solar Zenith Angle': calculate_solar_zenith_angle(api_data['lat'], api_data['lon'], api_data['time']),
        'Wind Speed': api_data['wind_speed'],
        'Pressure': api_data['pressure']
    }])