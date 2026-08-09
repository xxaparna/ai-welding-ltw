from pathlib import Path

# ==========================================================
# PROJECT ROOT
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

# ==========================================================
# DIRECTORIES
# ==========================================================

DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"

MODEL_DIR = BASE_DIR / "models"

OUTPUT_DIR = BASE_DIR / "outputs"

FIGURE_DIR = OUTPUT_DIR / "figures"
REPORT_DIR = OUTPUT_DIR / "reports"
PREDICTION_DIR = OUTPUT_DIR / "predictions"

# Create folders automatically
MODEL_DIR.mkdir(exist_ok=True)

OUTPUT_DIR.mkdir(exist_ok=True)
FIGURE_DIR.mkdir(exist_ok=True)
REPORT_DIR.mkdir(exist_ok=True)
PREDICTION_DIR.mkdir(exist_ok=True)

# ==========================================================
# DATASET FILES
# ==========================================================

ABSORPTIVITY_DATASET = RAW_DATA_DIR / "absorptivity_dataset.csv"

INTERFACE_TEMP_DATASET = RAW_DATA_DIR / "interface_temp_dataset.csv"

# ==========================================================
# FEATURE LISTS
# ==========================================================

ABSORPTIVITY_FEATURES = [

    "P_W",
    "V_mm_min",
    "line_energy_J_mm",
    "power_squared",
    "speed_squared",
    "power_speed_interaction",
    "specific_energy"

]

TEMPERATURE_FEATURES = [

    "P_W",
    "V_mm_min",
    "line_energy_J_mm",
    "power_squared",
    "speed_squared",
    "power_speed_interaction",
    "specific_energy"

]

# ==========================================================
# TARGET COLUMNS
# ==========================================================

ABSORPTIVITY_TARGET = "absorptivity_pct"

TEMPERATURE_TARGET = "interface_temp_C"

# ==========================================================
# TRAIN / TEST SPLIT
# ==========================================================

TEST_SIZE = 0.20

RANDOM_STATE = 42

# ==========================================================
# EDA SETTINGS
# ==========================================================

SHOW_PLOTS = False

# ==========================================================
# MODEL FILES
# ==========================================================

ABSORPTIVITY_MODEL = MODEL_DIR / "absorptivity_model.pkl"

TEMPERATURE_MODEL = MODEL_DIR / "temperature_model.pkl"

# ==========================================================
# SYNTHETIC DATASET
# ==========================================================

# ==========================================================
# SYNTHETIC DATA GENERATION
# ==========================================================

SYNTHETIC_DATASET_SIZE = 5000

POWER_MIN = 80
POWER_MAX = 150

SPEED_MIN = 200
SPEED_MAX = 600

ABSORPTIVITY_NOISE_STD = 0.50

TEMPERATURE_NOISE_STD = 20

SYNTHETIC_DATA_DIR = DATA_DIR / "synthetic"

SYNTHETIC_DATA_DIR.mkdir(exist_ok=True)

SYNTHETIC_DATASET = SYNTHETIC_DATA_DIR / "synthetic_dataset.csv"

# ==========================================================
# SCALER FILES
# ==========================================================

ABSORPTIVITY_SCALER = MODEL_DIR / "absorptivity_scaler.pkl"

TEMPERATURE_SCALER = MODEL_DIR / "temperature_scaler.pkl"
# ==========================================================
# FEATURE METADATA
# ==========================================================

FEATURE_METADATA = MODEL_DIR / "feature_metadata.json"

# ==========================================================
# MODEL METRICS
# ==========================================================

MODEL_METRICS = MODEL_DIR / "model_metrics.json"