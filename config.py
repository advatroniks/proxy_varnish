from dotenv import load_dotenv

from pydantic_settings import BaseSettings

from constants import ENV_PATH


load_dotenv(dotenv_path=ENV_PATH)


class MainSettings(BaseSettings):
    ACCESS_KEY: str
    SECRET_KEY: str
    S3_ENDPOINT_NAME: str


main_config = MainSettings()
