import json

from src.config import MODEL_METRICS


def get_metrics():

    try:

        with open(
            MODEL_METRICS,
            "r"
        ) as file:

            return json.load(file)

    except FileNotFoundError:

        return {
            "message": "Metrics file not found."
        }