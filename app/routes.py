from fastapi import APIRouter

from app.schemas import (
    PredictionRequest,
    PredictionResponse,
)

from app.predictor_service import predict
from app.metrics_service import get_metrics
from app.physics_service import get_physics


router = APIRouter()


# =====================================================
# Prediction API
# =====================================================

@router.post(
    "/predict",
    response_model=PredictionResponse
)
def predict_welding(request: PredictionRequest):

    return predict(
        request.power,
        request.speed
    )


# =====================================================
# Model Metrics API
# =====================================================

@router.get("/metrics")
def metrics():

    return get_metrics()


# =====================================================
# Physics Equations API
# =====================================================

@router.get("/physics")
def physics():

    return get_physics()