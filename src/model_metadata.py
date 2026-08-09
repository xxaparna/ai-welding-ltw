import json

from src.config import FEATURE_METADATA


class ModelMetadata:

    @staticmethod
    def save(abs_features, temp_features):

        metadata = {

            "absorptivity_features": abs_features,

            "temperature_features": temp_features

        }

        with open(
            FEATURE_METADATA,
            "w"
        ) as file:

            json.dump(
                metadata,
                file,
                indent=4
            )

        print(
            f"\nFeature metadata saved -> {FEATURE_METADATA}"
        )

    @staticmethod
    def load():

        with open(
            FEATURE_METADATA,
            "r"
        ) as file:

            return json.load(file)