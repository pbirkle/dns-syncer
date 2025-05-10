from logging_config import setup_logger
from scheduler import start_scheduler

logger = setup_logger("main")

if __name__ == '__main__':
    logger.info("dns-syncer successfully started!")
    start_scheduler()