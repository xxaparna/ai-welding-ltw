from pydantic import BaseModel


class PredictionRequest(BaseModel):

    power: float

    speed: float


class PredictionResponse(BaseModel):

    power: float

    speed: float

    line_energy: float

    absorptivity: float

    interface_temperature: float