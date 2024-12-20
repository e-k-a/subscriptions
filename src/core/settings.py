from pydantic import  PostgresDsn
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseSettings):
    postgres_dsn:str=os.getenv("POSTGRES_DB")

    project_name:str = 'API'


settings = Settings()