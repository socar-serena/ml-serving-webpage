from constants import ROOT_PATH
from domain.ab_sentiment_classifier import AbstractSentimentClassifier
from text_sentiment_classifier.model import TextSentimentClassifier


class SentimentClassifier(AbstractSentimentClassifier):
    def __init__(self, weights_path: str) -> None:
        self.classifier = TextSentimentClassifier(weights_path=f"{ROOT_PATH}/{weights_path}")

    def predict(self, review: str) -> dict:
        return self.classifier.predict(review)
