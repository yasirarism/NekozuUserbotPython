import os

class Config:
    api_id = int(os.environ.get("api_id", 12345))
    api_hash = os.environ.get("API_HASH", None)
    session = os.environ.get("STRING_SESSION", None)
    prefix = os.environ.get(".", None)
    alive_img = os.environ.get("alive img", None)
