from abc import ABC


class AbstractSentimentClassifier(ABC):
    def predict(cls, review: str) -> dict:
        """ 영화 리뷰를 입력받아, 감정 분석 결과를 출력한다 """
        pass
