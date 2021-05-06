import datetime

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, File
from starlette import status

from application.service import PredictionService
from container import Container
from presentation.req_res_objects import GetPredictionsResponse, PredictResponse

router = APIRouter()


@router.get("/health", status_code=status.HTTP_200_OK)
def health():
    return {"message": "I'm healthy!", "current_time": datetime.datetime.now()}


@router.get("/predictions", status_code=status.HTTP_200_OK, response_model=GetPredictionsResponse)
@inject
def get_predictions(
    prediction_service: PredictionService = Depends(Provide[Container.prediction_service]),
):
    predictions = prediction_service.get_predictions()
    return GetPredictionsResponse.from_predictions(predictions)


@router.post("/predict", status_code=status.HTTP_200_OK, response_model=PredictResponse)
@inject
def predict(
    review: str,
    prediction_service: PredictionService = Depends(Provide[Container.prediction_service]),
):
    prediction = prediction_service.predict(review)
    return PredictResponse.from_prediction(prediction)
