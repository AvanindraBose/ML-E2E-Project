import os

# PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

DATASET_DIR = "Dataset"
DATA_FILE_NAME = "car-details.csv"
DATA_FILE_PATH = os.path.join(DATASET_DIR, DATA_FILE_NAME)

APP_DIR = 'app'
MODEL_DIR_NAME = 'models'
MODEL_NAME = 'model.joblib'
MODEL_DIR = os.path.join(APP_DIR,MODEL_DIR_NAME)
MODEL_FILE_PATH = os.path.join(MODEL_DIR,MODEL_NAME)
