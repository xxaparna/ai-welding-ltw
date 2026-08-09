import json
import numpy as np

from sklearn.metrics import (
    r2_score,
    mean_absolute_error,
    mean_squared_error,
)

from src.config import MODEL_METRICS


class ModelEvaluator:

    def __init__(
        self,
        model,
        X_test,
        y_test,
        model_name,
    ):

        self.model = model
        self.X_test = X_test
        self.y_test = y_test
        self.model_name = model_name

    def evaluate(self):

        predictions = self.model.predict(
            self.X_test
        )

        r2 = r2_score(
            self.y_test,
            predictions
        )

        mae = mean_absolute_error(
            self.y_test,
            predictions
        )

        rmse = np.sqrt(
            mean_squared_error(
                self.y_test,
                predictions
            )
        )

        metrics = {

            "r2": round(float(r2), 4),

            "mae": round(float(mae), 4),

            "rmse": round(float(rmse), 4),

            "testing_samples": len(self.y_test)

        }

        # ----------------------------------------
        # Save metrics
        # ----------------------------------------

        try:

            with open(
                MODEL_METRICS,
                "r"
            ) as file:

                all_metrics = json.load(file)

        except FileNotFoundError:

            all_metrics = {}

        all_metrics[self.model_name] = metrics

        with open(
            MODEL_METRICS,
            "w"
        ) as file:

            json.dump(
                all_metrics,
                file,
                indent=4
            )

        print("\nModel Evaluation")
        print("-" * 40)

        print(f"R² Score : {r2:.4f}")
        print(f"MAE      : {mae:.4f}")
        print(f"RMSE     : {rmse:.4f}")

        print(
            f"\nMetrics saved -> {MODEL_METRICS}"
        )

        return metrics