import json
from fastapi.testclient import TestClient

from inference.main import app

client = TestClient(app)

# Loading input data
with open("./inference/sample_data/single-dp.json", "r", encoding="utf-8") as f_in:
    single_data_point = json.load(f_in)

# Declaring expected output data
expected_output = {"prediction": 0}


def test_predict_single_data_point():
    response = client.post("/predict", json=single_data_point)
    assert response.status_code == 200
    assert response.json() == expected_output
