from logging_config import setup_logger
import ip_resolver

logger = setup_logger(__name__)

def update_dns_entry(provider: str, domain: str):
    logger.info(f"updating dns entry {domain} for {provider}...")
    ipv4 = ip_resolver.resolve_ip()
    logger.info(f"dns entry {domain} for {provider} successfully updated")