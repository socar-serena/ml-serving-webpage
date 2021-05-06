from abc import abstractmethod, ABC
from typing import List

from domain.model import Prediction


class PredictionRepository(ABC):
    @abstractmethod
    def find_all(self) -> List[Prediction]:
        pass

    @abstractmethod
    def save(cls, prediction_output: Prediction) -> None:
        pass

    @property
    @abstractmethod
    def current_items_num(self) -> int:
        pass

    @abstractmethod
    def get_next_id(self) -> str:
        pass
