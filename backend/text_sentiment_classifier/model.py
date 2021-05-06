import numpy as np
from joblib import load


class TextSentimentClassifier(object):
    def __init__(self, weights_path):
        self.model = load(weights_path)
        self.cls_dict = {0: "negative", 1: "positive"}

    def predict(self, review):
        review = [str(review)]
        probs = self.model.predict_proba(review)
        cls = np.argmax(probs, 1)[0]
        proba = round(probs[0][cls] * 100, 1)
        cls = self.cls_dict[np.argmax(probs, 1)[0]]
        result = {"class": cls, "proba": proba}
        return result
