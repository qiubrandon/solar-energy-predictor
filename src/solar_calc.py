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

def calculate_solar_zenith_angle(latitude, day_of_year, hour):
    declination = calculate_solar_declination(day_of_year)
    hour_angle = calculate_hour_angle(hour)
    
    latitude_rad = np.radians(latitude)
    declination_rad = np.radians(declination)
    hour_angle_rad = np.radians(hour_angle)

    cos_theta = (np.sin(declination_rad) * np.sin(latitude_rad) +
                 np.cos(declination_rad) * np.cos(latitude_rad) * np.cos(hour_angle_rad))
    
    zenith_angle = np.degrees(np.arccos(cos_theta))
    return zenith_angle

def calculate_clear_sky_ghi(latitude, day_of_year, hour):
    zenith_angle = calculate_solar_zenith_angle(latitude, day_of_year, hour)
    
    clear_sky_ghi = SOLAR_CONSTANT * np.cos(np.radians(zenith_angle))
    return max(clear_sky_ghi, 0)  