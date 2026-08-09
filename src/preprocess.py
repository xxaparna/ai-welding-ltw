import pandas as pd


class DataPreprocessor:

    def __init__(self, dataframe):

        self.df = dataframe.copy()

    ############################################################

    def dataset_information(self):

        print("\nDataset Shape")
        print("-"*50)
        print(self.df.shape)

        print("\nColumns")
        print("-"*50)
        print(self.df.columns.tolist())

        print("\nData Types")
        print("-"*50)
        print(self.df.dtypes)

    ############################################################

    def missing_values(self):

        print("\nMissing Values")
        print("-"*50)

        print(self.df.isnull().sum())

    ############################################################

    def duplicate_rows(self):

        print("\nDuplicate Rows")
        print("-"*50)

        print(self.df.duplicated().sum())

    ############################################################

    def descriptive_statistics(self):

        print("\nStatistics")
        print("-"*50)

        print(self.df.describe(include="all"))

    ############################################################

    def validate_ranges(self):

        print("\nPhysics Validation")
        print("-"*50)

        if "P_W" in self.df.columns:

            if (self.df["P_W"] <= 0).any():

                print("❌ Invalid Laser Power Found")

            else:

                print("✅ Laser Power OK")

        if "V_mm_min" in self.df.columns:

            if (self.df["V_mm_min"] <= 0).any():

                print("❌ Invalid Welding Speed")

            else:

                print("✅ Welding Speed OK")

        if "absorptivity_pct" in self.df.columns:

            if ((self.df["absorptivity_pct"] < 0) |
                    (self.df["absorptivity_pct"] > 100)).any():

                print("❌ Invalid Absorptivity")

            else:

                print("✅ Absorptivity OK")

        if "interface_temp_C" in self.df.columns:

            if (self.df["interface_temp_C"] < 25).any():

                print("❌ Impossible Temperature")

            else:

                print("✅ Interface Temperature OK")

    ############################################################

    def report(self):

        self.dataset_information()

        self.missing_values()

        self.duplicate_rows()

        self.descriptive_statistics()

        self.validate_ranges()