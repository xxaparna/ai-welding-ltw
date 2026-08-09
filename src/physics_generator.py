import numpy as np
from sklearn.linear_model import LinearRegression


class PhysicsGenerator:

    def __init__(self, absorptivity_df, temperature_df):

        self.abs_df = absorptivity_df.copy()
        self.temp_df = temperature_df.copy()

        self.abs_model = LinearRegression()
        self.temp_model = LinearRegression()

    # =====================================================
    # Absorptivity Physics Model
    # =====================================================

    def fit_absorptivity_model(self):

        X = self.abs_df[
            [
                "P_W",
                "V_mm_min"
            ]
        ]

        y = self.abs_df["absorptivity_pct"]

        self.abs_model.fit(X, y)

        intercept = self.abs_model.intercept_

        power_coef = self.abs_model.coef_[0]

        speed_coef = self.abs_model.coef_[1]

        print("\n")
        print("=" * 70)
        print("ABSORPTIVITY PHYSICS MODEL")
        print("=" * 70)

        print(
            f"Absorptivity = "
            f"{intercept:.4f} "
            f"+ ({power_coef:.4f} × Power)"
            f" + ({speed_coef:.4f} × Speed)"
        )

    # =====================================================
    # Temperature Physics Model
    # =====================================================

    def fit_temperature_model(self):

        X = self.temp_df[
            [
                "line_energy_J_mm"
            ]
        ]

        y = self.temp_df["interface_temp_C"]

        self.temp_model.fit(X, y)

        intercept = self.temp_model.intercept_

        energy_coef = self.temp_model.coef_[0]

        print("\n")
        print("=" * 70)
        print("TEMPERATURE PHYSICS MODEL")
        print("=" * 70)

        print(
            f"Temperature = "
            f"{intercept:.4f} "
            f"+ ({energy_coef:.4f} × Line Energy)"
        )

    # =====================================================
    # Train Physics Models
    # =====================================================

    def fit(self):

        self.fit_absorptivity_model()

        self.fit_temperature_model()