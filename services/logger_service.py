"""
logger_service.py

Provides application logging.
"""

from loguru import logger


class LoggerService:
    """
    Central logging service.
    """

    def __init__(self):
        logger.remove()

        logger.add(
            "logs/application.log",
            rotation="5 MB",
            retention="10 days",
            level="INFO",
        )

    def get_logger(self):
        return logger