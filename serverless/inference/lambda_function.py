import pickle
from inference.models import SingleDataPoint


# Loading ML model
with open("./inference/ml_models/classifier.pkl", "rb") as model_pickle:
    classifier = pickle.load(model_pickle)


def lambda_handler(event, context):
    """This functions performs prediction on a single data point"""

    # Parse the event payload
    request = SingleDataPoint.model_validate(event)

    # Logging received features
    print(
        "variance: {},\nskewness: {},\ncurtosis: {},\nentropy: {},".format(
            request.variance, request.skewness, request.curtosis, request.entropy
        )
    )

    # Performing prediction
    prediction = classifier.predict(
        [[request.variance, request.skewness, request.curtosis, request.entropy]]
    )

    # Logging prediction
    print(f"prediction: {int(prediction[0])}")

    # Returning prediction
    return {"prediction": int(prediction[0])}
