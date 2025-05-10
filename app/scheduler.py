from logging_config import setup_logger
from apscheduler.schedulers.blocking import BlockingScheduler

logger = setup_logger(__name__)

def start_scheduler():
    scheduler = BlockingScheduler()
    logger.info("configuring schedulers...")
    scheduler.add_job(_create_job, 'interval', seconds=5, kwargs={'job': 'job-1'})
    scheduler.add_job(_create_job, 'interval', seconds=10, kwargs={'job': 'job-2'})
    logger.info("schedulers successfully configured")
    scheduler.start()

def _create_job(job: str):
    logger.info("testing " + job)