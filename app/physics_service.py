import json

from src.config import MODEL_DIR

PHYSICS_FILE = MODEL_DIR / "physics_equations.json"

print("Looking for physics file:", PHYSICS_FILE)


def get_physics():

    try:

        with open(PHYSICS_FILE, "r") as file:

            return json.load(file)

    except FileNotFoundError:

        return {
            "message": f"Physics file not found at {PHYSICS_FILE}"
        }