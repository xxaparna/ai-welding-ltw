import joblib

from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures

from src.config import (
    ABSORPTIVITY_MODEL,
    TEMPERATURE_MODEL,
)


class ModelTrainer:

    def __init__(
        self,
        X_train,
        y_train,
        model_name="linear"
    ):

        self.X_train = X_train
        self.y_train = y_train
        self.model_name = model_name

        self.model = None

    # =====================================================
    # Linear Regression
    # =====================================================

    def train_linear(self):

        self.model = LinearRegression()

        self.model.fit(
            self.X_train,
            self.y_train
        )

        return self.model

    # =====================================================
    # Polynomial Regression
    # =====================================================

    def train_polynomial(self, degree=2):

        self.model = Pipeline([

            (
                "poly",
                PolynomialFeatures(
                    degree=degree,
                    include_bias=False
                )
            ),

            (
                "linear",
                LinearRegression()
            )

        ])

        self.model.fit(
            self.X_train,
            self.y_train
        )

        return self.model

    # =====================================================
    # Select Model
    # =====================================================

    def train(self):

        if self.model_name == "linear":

            return self.train_linear()

        elif self.model_name == "polynomial":

            return self.train_polynomial()

        else:

            raise ValueError(
                "Unsupported model."
            )

    # =====================================================
    # Save Model
    # =====================================================

    def save(self, filepath):

        joblib.dump(
            self.model,
            filepath
        )

        print(f"Model saved -> {filepath}")