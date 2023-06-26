from pandas import DataFrame
from sklearn.ensemble import RandomForestClassifier
import datetime
import joblib


class Machine:

    def __init__(self, df: DataFrame):
        self.name = "Random Forest Classifier"
        target = df["Rarity"]
        features = df.drop(columns=["Rarity"])
        self.model = RandomForestClassifier()
        self.model.fit(features, target)
        self.timestamp = '%s' % datetime.datetime.now()

    def __call__(self, pred_basis: DataFrame):
        prediction, *_ = self.model.predict(pred_basis)
        confidence, *_ = self.model.predict_proba(pred_basis)
        return prediction, max(confidence)

    def save(self, filepath):
        joblib.dump(self.model, filepath)

    @staticmethod
    def open(filepath):
        joblib.load(filepath)

    def info(self):
        return f'Model: {self.name} <br>Initialized: {self.timestamp}'
