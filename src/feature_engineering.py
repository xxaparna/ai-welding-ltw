import numpy as np


class FeatureEngineer:

    def __init__(self, dataframe):

        self.df = dataframe.copy()

    # =====================================================
    # Line Energy
    # =====================================================

    def add_line_energy(self):

        # Always calculate using the physics formula
        self.df["line_energy_J_mm"] = (
            60 * self.df["P_W"] /
            self.df["V_mm_min"]
        )

        return self

    # =====================================================
    # Polynomial Features
    # =====================================================

    def add_polynomial_features(self):

        self.df["power_squared"] = self.df["P_W"] ** 2

        self.df["speed_squared"] = self.df["V_mm_min"] ** 2

        return self

    # =====================================================
    # Interaction Feature
    # =====================================================

    def add_interaction_feature(self):

        self.df["power_speed_interaction"] = (
            self.df["P_W"] *
            self.df["V_mm_min"]
        )

        return self

    # =====================================================
    # Experimental Physics Feature
    # =====================================================

    def add_specific_energy(self):

        self.df["specific_energy"] = (
            self.df["P_W"] /
            np.sqrt(self.df["V_mm_min"])
        )

        return self

    # =====================================================
    # Run All
    # =====================================================

    def engineer(self):

        self.add_line_energy()

        self.add_polynomial_features()

        self.add_interaction_feature()

        self.add_specific_energy()

        return self.df