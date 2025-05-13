from app.dns.api_client import ApiClient
from app.dns.api_provider import ApiProvider
from app.dns.client_webtropia import ClientWebtropia

def get_api_client(api_provider: ApiProvider) -> ApiClient:
    if api_provider == ApiProvider.WEBTROPIA:
        return ClientWebtropia()
    else:
        raise Exception(f"api provider {api_provider} not found")