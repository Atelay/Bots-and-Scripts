import logging
import logging.handlers
import datetime


# Set up the logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Define the log file path
log_file = f"log_{datetime.datetime.now().strftime('%Y-%m-%d')}.log"

# Create a file handler
file_handler = logging.handlers.TimedRotatingFileHandler(log_file, when='midnight', backupCount=1)
file_handler.setLevel(logging.INFO)

# Create a console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Define the log format
log_format = '%(filename)-20s:%(lineno)-4d #%(levelname)-7s [%(asctime)s] - %(name)s - %(message)s'
formatter = logging.Formatter(log_format)

# Set the formatters for the handlers
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)
