from typing import List

from pydantic import BaseModel

from domain.model import Prediction


class GetPredictionResponse(BaseModel):
    id: str
    predicted_result: dict
    prediction_time: float
    created_at: int

    @classmethod
    def from_prediction(cls, prediction: Prediction) -> "GetPredictionResponse":
        return cls(
            id=prediction.id,
            predicted_result=prediction.predicted_result,
            prediction_time=prediction.prediction_time,
            created_at=prediction.created_at,
        )


class GetPredictionsResponse(BaseModel):
    items: List[GetPredictionResponse]

    @classmethod
    def from_predictions(cls, predictions: List[Prediction]) -> "GetPredictionsResponse":
        return cls(items=[GetPredictionResponse.from_prediction(prediction) for prediction in predictions])


class PredictReqeust(BaseModel):
    pass


class PredictResponse(BaseModel):
    id: str
    predicted_result: dict
    prediction_time: float

    @classmethod
    def from_prediction(cls, prediction: Prediction) -> "PredictResponse":
        return cls(
            id=prediction.id,
            predicted_result=prediction.predicted_result,
            prediction_time=prediction.prediction_time,
        )
