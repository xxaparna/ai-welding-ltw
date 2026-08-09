import joblib
import pandas as pd

from src.model_metadata import ModelMetadata

from src.config import (
    ABSORPTIVITY_MODEL,
    TEMPERATURE_MODEL,
    ABSORPTIVITY_SCALER,
    TEMPERATURE_SCALER,
)


class Predictor:

    def __init__(self):

        # =====================================================
        # Load Models
        # =====================================================

        self.abs_model = joblib.load(
            ABSORPTIVITY_MODEL
        )

        self.temp_model = joblib.load(
            TEMPERATURE_MODEL
        )

        # =====================================================
        # Load Scalers
        # =====================================================

        self.abs_scaler = joblib.load(
            ABSORPTIVITY_SCALER
        )

        self.temp_scaler = joblib.load(
            TEMPERATURE_SCALER
        )

        # =====================================================
        # Load Feature Metadata
        # =====================================================

        self.metadata = ModelMetadata.load()

        self.abs_features = self.metadata[
            "absorptivity_features"
        ]

        self.temp_features = self.metadata[
            "temperature_features"
        ]

    # =====================================================
    # Feature Engineering
    # =====================================================

    def create_features(
        self,
        power,
        speed
    ):

        line_energy = (
            60 * power / speed
        )

        power_squared = power ** 2

        speed_squared = speed ** 2

        power_speed_interaction = (
            power * speed
        )

        specific_energy = (
            power / (speed ** 0.5)
        )

        features = pd.DataFrame({

            "P_W": [power],

            "V_mm_min": [speed],

            "line_energy_J_mm": [line_energy],

            "power_squared": [power_squared],

            "speed_squared": [speed_squared],

            "power_speed_interaction": [
                power_speed_interaction
            ],

            "specific_energy": [
                specific_energy
            ]

        })

        return features

    # =====================================================
    # Prediction
    # =====================================================

    def predict(
        self,
        power,
        speed
    ):

        features = self.create_features(
            power,
            speed
        )

        # Arrange columns exactly as used during training

        abs_features = features[
            self.abs_features
        ]

        temp_features = features[
            self.temp_features
        ]

        # Scale features

        abs_scaled = self.abs_scaler.transform(
            abs_features
        )

        temp_scaled = self.temp_scaler.transform(
            temp_features
        )

        # Predictions

        absorptivity = self.abs_model.predict(
            abs_scaled
        )[0]

        temperature = self.temp_model.predict(
            temp_scaled
        )[0]

        return {

            "power": round(power, 2),

            "speed": round(speed, 2),

            "line_energy": round(
                features["line_energy_J_mm"].iloc[0],
                2
            ),

            "absorptivity": round(
                absorptivity,
                2
            ),

            "interface_temperature": round(
                temperature,
                2
            )

        }