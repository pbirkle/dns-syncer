from enum import Enum

class ApiProvider(Enum):
    WEBTROPIA = {
        "name": "Webtropia",
        "api_url": "https://zkm.webtropia.com/api",
        "env_token_name": "WEBTROPIA_TOKEN"
    }