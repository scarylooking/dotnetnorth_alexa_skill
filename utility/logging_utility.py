import logging


def configure_logger():
    if logging.getLogger().hasHandlers():
        logging.getLogger().setLevel(logging.INFO)
    else:
        logging.basicConfig(level=logging.INFO)
