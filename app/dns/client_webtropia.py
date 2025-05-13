from requests import Response

from app.dns.api_client import ApiClient
from app.dns.api_provider import ApiProvider
from app.dns.dns_record import DNSRecord
from app.logging_config import setup_logger
from os import getenv
import requests

logger = setup_logger(__name__)

class ClientWebtropia(ApiClient):

    api_url = ApiProvider.WEBTROPIA.value["api_url"]
    api_token = getenv(ApiProvider.WEBTROPIA.value["env_token_name"], "")

    def get_records(self, zone_name: str) -> list[DNSRecord]:
        logger.debug(f"requesting records for zone {zone_name}...")
        url = f"{self.api_url}/dns/zone/{zone_name}"
        headers = {
            "Authorization": f"Bearer {self.api_token}"
        }
        response = requests.get(url, headers=headers)

        ApiClient.validate_get_response(response)

        return self._extract_records(response)

    def update_record(self, zone_name: str, record_name: str, record_type: str, record_content: str) -> dict:
        logger.debug(f"updating record {record_name} of type {record_type} for zone {zone_name} with content {record_content}...")
        return {"success": True}

    def _extract_records(self, response: Response) -> list[DNSRecord]:
        records = response.json().get("content", {}).get("records", [])
        return [DNSRecord(record["name"], record["type"], record["ttl"], record["content"]) for record in records]