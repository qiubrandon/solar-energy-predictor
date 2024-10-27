import requests
import pandas as pd
import hashlib
from pathlib import Path
from io import StringIO
from config import API_KEY, URL, EMAIL

# check if coordinates already exist in hash table
def hash_check(lon, lat):
    unique = f'{lat}_{lon}'
    hash_id = hashlib.md5(unique.encode()).hexdigest()
    return f'data_{hash_id}.csv'
    

    

def fetch_data(lat, lon, year=2020):
    lo = round(lon, 1)
    la = round(lat, 1)
    params = {
        'api_key': API_KEY,
        'wkt': f'POINT({lo} {la})',
        'names': year,
        'interval': 60,
        'email': EMAIL,
        'utc': 'true',
    }

    # create a new csv file if it doesnt exist
    filename = f'data/solar_data/{hash_check(lo,la)}'
    if Path(filename).exists():
        return filename
    else:
        response = requests.get(URL, params=params)
        response.raise_for_status()
        data = pd.read_csv(StringIO(response.text), skiprows=2)
        data.to_csv(filename, index=False)
    return filename

if __name__ == "__main__":
    lat = 43.0006251
    lon = -78.7897144
    
    data = fetch_data(lat, lon)
    print(data.head())
