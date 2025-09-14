from pydantic import ValidationError
from pydantic_settings import BaseSettings
from pydantic import Field

class settings(BaseSettings):
    bucket_name: str = Field(default="formula-one-data")

Settings = settings()