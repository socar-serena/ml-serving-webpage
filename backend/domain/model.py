import time

from pydantic import BaseModel, Field


class Prediction(BaseModel):
    id: str
    predicted_result: dict
    prediction_time: float
    created_at: int = Field(default_factory=lambda: int(time.time()))
