from abc import ABC, abstractmethod

from requests import Response

from app.dns.dns_record import DNSRecord

class ApiClient(ABC):
    @abstractmethod
    def get_records(self, zone_name: str) -> list[DNSRecord]:
        pass

    @abstractmethod
    def update_record(self, zone_name: str, record_name: str, record_type: str, record_content: str) -> dict:
        pass

    @abstractmethod
    def _extract_records(self, response: Response) -> list[DNSRecord]:
        pass

    @staticmethod
    def validate_get_response(response: Response):
        if response.status_code != 200:
            raise Exception(f"API request failed with status code: {response.status_code}")