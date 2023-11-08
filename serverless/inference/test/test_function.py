import json

from inference.lambda_function import lambda_handler


# Loading input data
with open("./inference/sample_data/single-dp.json", "r", encoding="utf-8") as f_in:
    single_data_point = json.load(f_in)

# Declaring expected output data
expected_output = {"prediction": 0}


def test_predict_single_data_point(lambda_context):
    response = lambda_handler(single_data_point, lambda_context)
    assert response == expected_output
