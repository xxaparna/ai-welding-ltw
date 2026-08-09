import pandas as pd

from src.config import (
    ABSORPTIVITY_DATASET,
    INTERFACE_TEMP_DATASET,
)

def load_absorptivity_data():

    return pd.read_csv(ABSORPTIVITY_DATASET)


def load_interface_temperature_data():

    return pd.read_csv(INTERFACE_TEMP_DATASET)