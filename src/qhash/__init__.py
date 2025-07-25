__version__ = "0.9.4"
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from loguru import logger
import sys

# Remove default handler
logger.remove()

# Add custom handler with clean format including module and line number
logger.add(
    sys.stderr,
    format="<green>{time:HH:mm:ss}</green> | <cyan>{module:>16}:{line}</cyan> | <level>{level: >8}</level> | <level>{message}</level>",
    colorize=True,
    level="INFO",  # "DEBUG" to enable logger.debug("message") and up prints
    # "ERROR" to enable only logger.error("message") prints
    # etc
)

# Disable before release or as needed
logger.disable("qhash")

from qhash.model import QModel
from qhash.pipeline import QPipeline
