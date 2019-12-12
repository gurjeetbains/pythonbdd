import logging


def custom_logger(log_level, logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler("Report.log")
    file_handler.setLevel(log_level)
    formatter = logging.Formatter("%(asctime)s -%(name)s %(levelname)s: %(message)s",
                                  datefmt="%m-%d-%Y %I:%M:%S %p")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger
