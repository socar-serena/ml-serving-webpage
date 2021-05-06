from dependency_injector import containers, providers

from application.service import PredictionService
from infrastructure.classifier.sentiment_classifier import SentimentClassifier
from infrastructure.repository.in_mem_repository import InMemPredictionRepository


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    prediction_repository = providers.Singleton(
        InMemPredictionRepository, max_item_size=config.in_mem_repository.max_item_size
    )
    sentiment_classifier = providers.Singleton(
        SentimentClassifier,
        weights_path=config.model.weight_file_name,
    )
    prediction_service = providers.Singleton(
        PredictionService, prediction_repository=prediction_repository, sentiment_classifier=sentiment_classifier
    )
