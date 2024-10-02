import logging
from .sheetauto import pandas2excel, excel2img

# Configure logging for the package
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # Set default logging level

# Console handler for logging output
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)  # Adjust logging level as needed
formatter = logging.Formatter('%(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Add the handler to the logger
if not logger.hasHandlers():  # Ensure the logger isn't set up multiple times
    logger.addHandler(console_handler)

# Expose functions at package level
__all__ = ['pandas2excel', 'excel2img']
