from app.logging_config import setup_logger
import requests

logger = setup_logger(__name__)

def resolve_ip() -> str:
    request_url = "https://ipapi.co/json"
    request_headers = {
        "User-Agent": "curl/7.79.1"
    }
    logger.info(f"Requesting ipv4...")
    response = requests.get(request_url, headers=request_headers)
    logger.info("Request successful, ipv4=%s", response.json()["ip"])
    logger.debug(f"Response from request: {response.json()}")
    return response.json()["ip"]