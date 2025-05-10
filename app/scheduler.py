from logging_config import setup_logger
from apscheduler.schedulers.blocking import BlockingScheduler
from dns_updater import update_dns_entry

logger = setup_logger(__name__)

def start_scheduler():
    logger.info("configuring schedulers...")
    scheduler = BlockingScheduler()
    scheduler.add_job(update_dns_entry, 'interval', seconds=10, kwargs={'provider': 'provider-1', 'domain': 'domain-1'})
    logger.info("schedulers successfully configured")
    scheduler.start()