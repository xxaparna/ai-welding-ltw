import numpy as np
import pandas as pd

from src.config import (
    SYNTHETIC_DATASET_SIZE,
    SYNTHETIC_DATASET,
    POWER_MIN,
    POWER_MAX,
    SPEED_MIN,
    SPEED_MAX,
    ABSORPTIVITY_NOISE_STD,
    TEMPERATURE_NOISE_STD,
)


class SyntheticDataGenerator:

    def __init__(self, physics):

        self.physics = physics

    # =====================================================
    # Generate Synthetic Dataset
    # =====================================================

    def generate(self):

        np.random.seed(42)

        # ---------------------------------------------
        # Generate Process Parameters
        # ---------------------------------------------

        power = np.random.uniform(
            POWER_MIN,
            POWER_MAX,
            SYNTHETIC_DATASET_SIZE
        )

        speed = np.random.uniform(
            SPEED_MIN,
            SPEED_MAX,
            SYNTHETIC_DATASET_SIZE
        )

        # ---------------------------------------------
        # Calculate Line Energy
        # ---------------------------------------------

        line_energy = (
            60 * power / speed
        )

        # ---------------------------------------------
        # Predict Absorptivity
        # ---------------------------------------------

        X_abs = pd.DataFrame({
            "P_W": power,
            "V_mm_min": speed
        })

        abs_pred = self.physics.abs_model.predict(
            X_abs
        )

        # ---------------------------------------------
        # Predict Interface Temperature
        # ---------------------------------------------

        X_temp = pd.DataFrame({
            "line_energy_J_mm": line_energy
        })

        temp_pred = self.physics.temp_model.predict(
            X_temp
        )

        # ---------------------------------------------
        # Add Experimental Noise
        # ---------------------------------------------

        absorptivity = (
            abs_pred +
            np.random.normal(
                0,
                ABSORPTIVITY_NOISE_STD,
                SYNTHETIC_DATASET_SIZE
            )
        )

        temperature = (
            temp_pred +
            np.random.normal(
                0,
                TEMPERATURE_NOISE_STD,
                SYNTHETIC_DATASET_SIZE
            )
        )

        # ---------------------------------------------
        # Clip to Physical Limits
        # ---------------------------------------------

        absorptivity = np.clip(
            absorptivity,
            8,
            30
        )

        temperature = np.clip(
            temperature,
            200,
            1350
        )

        # ---------------------------------------------
        # Create Dataset
        # ---------------------------------------------

        synthetic_df = pd.DataFrame({

            "P_W": power,

            "V_mm_min": speed,

            "line_energy_J_mm": line_energy,

            "absorptivity_pct": absorptivity,

            "interface_temp_C": temperature

        })

        return synthetic_df

    # =====================================================
    # Save Dataset
    # =====================================================

    def save(self):

        df = self.generate()

        df.to_csv(
            SYNTHETIC_DATASET,
            index=False
        )

        print("\nSynthetic Dataset Generated Successfully.")
        print(f"Saved at : {SYNTHETIC_DATASET}")
        print()
        print(df.head())

        return df