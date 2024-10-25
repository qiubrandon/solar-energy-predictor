import pandas as pd
import pytest
from src.training import train_model

@pytest.fixture

def test_data(tempDir):
    data = {
        'irradiance': [500,600,700,800],
        'temperature': [25,30,28,26],
        'humidity': [40,50,45,60],
        'energy_output':[75,85,95,105],
    }
    df = pd.DataFrame(data)
    file_path = tempDir.join("test_data.csv")
    df.to_csv(file_path, index=False)
    return file_path

def test_train_model(mock_data):
    model, mae = train_model(mock_data)
    assert mae < 10