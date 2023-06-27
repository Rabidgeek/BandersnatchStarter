from pandas import DataFrame
from sklearn.ensemble import RandomForestClassifier
import datetime
import joblib


class Machine:
    """
    A class representing a Random Forest Classifier model.

    Parameters:
    - df (pandas.DataFrame): The input DataFrame containing the training data.

    Attributes:
    - name (str): The name of the model ("Random Forest Classifier").
    - model (RandomForestClassifier): The trained Random Forest Classifier
      model.
    - timestamp (str): The timestamp indicating when the model was initialized.

    Methods:
    - __call__(self, pred_basis: DataFrame) -> Tuple: Makes predictions on the
      provided DataFrame.
    - save(self, filepath: str): Saves the model to a file.
    - open(filepath: str) -> Machine: Loads a saved model from a file.
    - info(self) -> str: Returns information about the model.

    """
    def __init__(self, df: DataFrame):
        """
        Initializes the Machine object with the given DataFrame.

        Parameters:
        - df (pandas.DataFrame): The input DataFrame containing the training
          data.

        """
        self.name = "Random Forest Classifier"
        target = df["Rarity"]
        features = df.drop(columns=["Rarity"])
        self.model = RandomForestClassifier(
            n_estimators=300,
            max_depth=10,
            min_samples_leaf=1,
            min_samples_split=2,
            random_state=42
        )
        self.model.fit(features, target)
        self.timestamp = '%s' % datetime.datetime.now()

    def __call__(self, pred_basis: DataFrame):
        """
        Makes predictions on the provided DataFrame.

        Parameters:
        - pred_basis (pandas.DataFrame): The DataFrame to make predictions on.

        Returns:
        - prediction (Any): The predicted value.
        - confidence (float): The confidence score associated with the
          prediction.

        """
        prediction, *_ = self.model.predict(pred_basis)
        confidence, *_ = self.model.predict_proba(pred_basis)
        return prediction, max(confidence)

    def save(self, filepath):
        """
        Saves the model to a file.

        Parameters:
        - filepath (str): The path to save the model.

        """
        joblib.dump(self.model, filepath)

    @staticmethod
    def open(filepath):
        """
        Loads a saved model from a file.

        Parameters:
        - filepath (str): The path to the saved model file.

        Returns:
        - machine (Machine): The loaded Machine object.

        """
        return joblib.load(filepath)

    def info(self):
        """
        Returns information about the model.

        Returns:
        - info (str): Information about the model, including its name and
          initialization timestamp.

        """
        return f'Model: {self.name} <br>Initialized: {self.timestamp}'
