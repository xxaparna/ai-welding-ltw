import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from app.routes import router

app = FastAPI(
    title="AI Laser Transmission Welding",
    version="1.0.0"
)

# -----------------------------
# CORS Configuration (Production & Development)
# -----------------------------
origins_env = os.getenv("CORS_ORIGINS", "")
if origins_env:
    origins = [origin.strip() for origin in origins_env.split(",") if origin.strip()]
else:
    origins = [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "*"
    ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

# Serve saved plots
app.mount(
    "/figures",
    StaticFiles(directory="outputs/figures"),
    name="figures",
)