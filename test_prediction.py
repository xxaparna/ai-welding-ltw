from src.predictor import Predictor

predictor = Predictor()

result = predictor.predict(

    power=120,

    speed=350

)

print(result)