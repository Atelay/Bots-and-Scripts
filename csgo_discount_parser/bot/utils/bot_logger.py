import logging
import logging.handlers
import datetime


logger = logging.getLogger()
logger.setLevel(logging.INFO)

log_file = f"log_{datetime.datetime.now().strftime('%Y-%m-%d')}.log"

file_handler = logging.handlers.TimedRotatingFileHandler(
    log_file, when="midnight", backupCount=1
)
file_handler.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

log_format = "%(filename)-20s:%(lineno)-4d #%(levelname)-7s [%(asctime)s] - %(name)s - %(message)s"
formatter = logging.Formatter(log_format)

file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)
