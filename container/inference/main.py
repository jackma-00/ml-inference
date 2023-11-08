import pickle
from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.encoders import jsonable_encoder

from inference.models import SingleDataPoint


app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
    )


@app.exception_handler(Exception)
async def unhandled_exception_handler(request: Request, exc: Exception):
    return PlainTextResponse(
        f"Unexpected {exc=}, {type(exc)=}",
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )


# Loading ML model
with open("./inference/ml_models/classifier.pkl", "rb") as model_pickle:
    classifier = pickle.load(model_pickle)


@app.get("/")
async def root():
    return {"message": "Call /predict for inference"}


@app.post("/predict")
async def predict(request: SingleDataPoint):
    """This method performs prediction on a single data point"""

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
