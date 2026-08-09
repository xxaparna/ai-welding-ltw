from src.predictor import Predictor


predictor = Predictor()


def predict(power, speed):

    return predictor.predict(
        power,
        speed
    )