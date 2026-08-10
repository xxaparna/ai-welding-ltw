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
allowed_origins = [
    "https://ai-welding-ltw.vercel.app",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:3000",
]

origins_env = os.getenv("CORS_ORIGINS", "")
if origins_env:
    for origin in origins_env.split(","):
        cleaned = origin.strip()
        if cleaned and cleaned not in allowed_origins:
            allowed_origins.append(cleaned)

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_origin_regex=r"https://.*\.vercel\.app",
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