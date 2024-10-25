import math

def solarIrr(constant=1361, incidenceAngle=0.0):
    # how is irradiance calculated? 
    # some assumptions: no cloud coverage, direct sunlight
    #

    # irradiance is the power per unit area received from the sun
    # at a given time
    return max(constant * math.cos(math.radians(incidenceAngle)), 0)

def energyOutput(irradiance, area=1.0, efficiency=0.15):
    return irradiance * area * efficiency