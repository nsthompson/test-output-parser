from pydantic import BaseSettings


class Settings(BaseSettings):
    # Configuration Options
    IGNORE_LIBRARIES: list = [
        "OperatingSystem",
        "yaml",
        "Collections",
        "BuiltIn"
        ]
    IGNORE_TYPES: list = []


config = Settings()
