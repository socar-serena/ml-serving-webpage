from typing import ClassVar, Dict, List, Optional

from domain.model import Prediction
from domain.repository import PredictionRepository


class InMemPredictionRepository(PredictionRepository):
    DEFAULT_MAX_ITEM_SIZE: ClassVar[int] = 100

    def __init__(self, max_item_size: Optional[int] = None) -> None:
        self.max_item_size = self.DEFAULT_MAX_ITEM_SIZE if max_item_size is None else max_item_size
        self._data: Dict[str, Prediction] = {}
        self.next_id = 1

    def find_all(self) -> List[Prediction]:
        return list(self._data.values())

    def find_by_id(self, prediction_id: str) -> Prediction:
        return self._data[prediction_id]

    def save(self, prediction: Prediction) -> None:
        if self.current_items_num >= self.max_item_size:
            raise Exception("Prediction을 저장할 수 있는 공간이 꽉 찼습니다!")
        self._data[prediction.id] = prediction

    @property
    def current_items_num(self):
        return len(self._data)

    def get_next_id(self) -> int:
        return_value = self.next_id
        self.next_id += 1

        return return_value
