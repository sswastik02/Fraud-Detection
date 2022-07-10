from pathlib import Path
import os

ML_DIR = Path(__file__).resolve().parent
PIPES_DIR = os.path.join(ML_DIR, "pipes")
MODELS_DIR = os.path.join(ML_DIR,"models")
