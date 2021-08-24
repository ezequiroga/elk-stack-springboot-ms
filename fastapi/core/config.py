from starlette.config import Config
from starlette.datastructures import Secret

APP_NAME = "LogApp"
API_PREFIX = "/api"

config = Config("drenv.env")

APP_VERSION = config("APP_VERSION")
PATH_BASE = config("PATH_BASE")

# API_KEY: Secret = config("API_KEY", cast=Secret)