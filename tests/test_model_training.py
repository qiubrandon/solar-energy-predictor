import pytest
from src.training import train_model
from config import PATH

@pytest.fixture
def real_dataset():
    # Provide the path to your real dataset CSV file
    return PATH # Replace this with the actual file path

def test_train_model_real_dataset(real_dataset):
    # Train the model using the real dataset
    model, mae = train_model(datapath=real_dataset)

    # Assertions to validate the training process
    assert model is not None, "Model should be trained successfully"
    assert mae < 50, f"Model MAE too high: {mae}"  # Adjust threshold based on your expectations
