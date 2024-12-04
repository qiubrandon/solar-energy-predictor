from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.encoders import jsonable_encoder
from datetime import datetime
import joblib
import pandas as pd
import requests
from config import KEY, URL, MODEL_PATH

# Load the trained model
MODEL_PATH = MODEL_PATH
try:
    model = joblib.load(MODEL_PATH)
except FileNotFoundError:
    model = None  # Handle the case where the model isn't trained yet

WEATHER_API_KEY = KEY
WEATHER_API_URL = URL

app = FastAPI()

def calculate_solar_zenith_angle(lat, lon, date_time):
    from math import cos, sin, acos, radians, degrees
    day_of_year = date_time.timetuple().tm_yday
    declination = 23.45 * sin(radians(360 * (284 + day_of_year) / 365))
    time_correction = 4 * lon
    solar_noon = 12 - time_correction / 60
    current_time = date_time.hour + date_time.minute / 60
    hour_angle = 15 * (current_time - solar_noon)
    zenith_angle = acos(
        sin(radians(lat)) * sin(radians(declination)) +
        cos(radians(lat)) * cos(radians(declination)) * cos(radians(hour_angle))
    )
    return degrees(zenith_angle)

@app.get("/predict")
async def predict(lat: float, lon: float, days: int = Query(1, ge=1, le=7)):
    if model is None:
        raise HTTPException(status_code=500, detail="Model not found or not trained.")

    response = requests.get(
        WEATHER_API_URL,
        params={"key": WEATHER_API_KEY, "q": f"{lat},{lon}", "days": days}
    )
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Failed to fetch weather data.")
    weather_data = response.json()

    # Preprocess the data
    rows = []
    for day in weather_data['forecast']['forecastday']:
        for hour in day['hour']:
            date_time = datetime.strptime(hour['time'], "%Y-%m-%d %H:%M")
            zenith_angle = calculate_solar_zenith_angle(lat, lon, date_time)
            row = {
                "date_time": hour['time'],  # Include the original date_time string
                "Temperature": hour['temp_c'],
                "Relative Humidity": hour['humidity'],
                "Cloud Type": hour['cloud'],
                "Solar Zenith Angle": zenith_angle,
                "Pressure": hour['pressure_mb'],
                "Wind Speed": hour['wind_kph']
            }
            rows.append(row)
    
    features = pd.DataFrame(rows)


    features['hour'] = pd.to_datetime(features['date_time']).dt.hour
    features = features[features['hour'] % 6 == 0]

    features_for_model = features.drop(columns=["date_time", "hour"])

    predictions = model.predict(features_for_model)
    features['predicted_GHI'] = predictions

    features = features.drop(columns=["hour"])


    return JSONResponse(content={"location": f"{lat},{lon}", "predictions": features.to_dict(orient="records")})

@app.post("/train")
async def train_model():
    return {"message": "Training endpoint not implemented yet."}

app.mount("/", StaticFiles(directory="templates", html=True), name="static")
