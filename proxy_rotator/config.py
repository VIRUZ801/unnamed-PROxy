import os
from dotenv import load_dotenv

load_dotenv()

def _split(value: str):
    return [v.strip() for v in value.split(",") if v.strip()]

PROXY_LIST = _split(os.getenv("PROXY_LIST", ""))
ROTATION_MINUTES = int(os.getenv("ROTATION_MINUTES", "10"))
SELECTION_MODE = os.getenv("SELECTION_MODE", "random")
TIMEOUT = int(os.getenv("TIMEOUT", "10"))
ASYNC = os.getenv("ASYNC", "false").lower() == "true"
HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
