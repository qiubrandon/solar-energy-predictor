import pytest
from src.solar_calc import energyOutput, solarIrr

def test_solarIrr():
    assert solarIrr(1361,0) == 1361
    assert solarIrr(1361,90) == 0

def test_calculate_energy_output():
    irradiance = 1000  # Example irradiance value in W/m^2
    area = 1.5         # Example panel area in m^2
    efficiency = 0.2   # 20% efficiency
    expected_output = irradiance * area * efficiency
    assert energyOutput(irradiance, area, efficiency) == expected_output