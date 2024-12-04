import math
import numpy as np
from datetime import datetime

def solarIrr(constant=1361, incidenceAngle=0.0):
    # how is irradiance calculated? 
    # some assumptions: no cloud coverage, direct sunlight
    #

    # irradiance is the power per unit area received from the sun
    # at a given time
    return max(constant * math.cos(math.radians(incidenceAngle)), 0)

def energyOutput(irradiance, area=1.0, efficiency=0.15):
    return irradiance * area * efficiency

SOLAR_CONSTANT = 1361  

def calculate_solar_declination(day_of_year):
    return 23.45 * np.sin(np.radians(360 * (284 + day_of_year) / 365))

def calculate_hour_angle(hour):
    return 15 * (hour - 12)

from math import cos, sin, acos, radians, degrees
from datetime import datetime, timedelta

def calculate_solar_zenith_angle(lat, lon, date_time):
    """
    Calculate the Solar Zenith Angle given latitude, longitude, and datetime.
    :param lat: Latitude in degrees
    :param lon: Longitude in degrees
    :param date_time: Datetime object
    :return: Solar Zenith Angle in degrees
    """
    utc_time = date_time - timedelta(minutes=date_time.utcoffset().total_seconds() / 60) if date_time.utcoffset() else date_time
    day_of_year = utc_time.timetuple().tm_yday
    
    declination = 23.45 * sin(radians(360 * (284 + day_of_year) / 365))
    
    time_correction = 4 * lon + 60 * utc_time.utcoffset().total_seconds() / 3600 if utc_time.utcoffset() else 4 * lon
    
    solar_noon = 12 - time_correction / 60
    
    current_time = utc_time.hour + utc_time.minute / 60
    hour_angle = 15 * (current_time - solar_noon)
    
    zenith_angle = acos(
        sin(radians(lat)) * sin(radians(declination)) +
        cos(radians(lat)) * cos(radians(declination)) * cos(radians(hour_angle))
    )
    
    return degrees(zenith_angle)


def calculate_clear_sky_ghi(latitude, day_of_year, hour):
    zenith_angle = calculate_solar_zenith_angle(latitude, day_of_year, hour)
    
    clear_sky_ghi = SOLAR_CONSTANT * np.cos(np.radians(zenith_angle))
    return max(clear_sky_ghi, 0)  