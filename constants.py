from pathlib import Path


BASE_PATH = str(Path(__file__).resolve().parent)

ENV_PATH = f"{BASE_PATH}/.env"

PATH_TO_TEMPORARY_STORAGE = f"{BASE_PATH}/temporary_storage"
