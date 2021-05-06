import time
from typing import List

from text_sentiment_classifier.model import TextSentimentClassifier

from domain.model import Prediction
from domain.repository import PredictionRepository


class PredictionService:
    def __init__(
        self,
        prediction_repository: PredictionRepository,
        sentiment_classifier: TextSentimentClassifier,
    ) -> None:
        self.prediction_repository = prediction_repository
        self.text_classifier = sentiment_classifier

    def get_predictions(self) -> List[Prediction]:
        return self.prediction_repository.find_all()

    def predict(self, review: str) -> Prediction:
        start_time = time.time()
        print("in predict():", review)
        predicted_result = self.text_classifier.predict(review)
        print(predicted_result)
        prediction = Prediction(
            id=self.prediction_repository.get_next_id(),
            predicted_result=predicted_result,
            prediction_time=time.time() - start_time,
        )
        self.prediction_repository.save(prediction)
        return prediction
