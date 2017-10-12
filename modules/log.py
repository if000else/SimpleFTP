import logging
from conf import settings

def logger(log_type):
    # create logger
    logger = logging.getLogger(log_type)
    logger.setLevel(settings.LOG_LEVEL)

    # create console handler and set level to debug

    if not logger.handlers:
        ch = logging.StreamHandler()  # print to screen
        ch.setLevel(settings.LOG_LEVEL)
        # create file handler and set level to warning
        log_file = "%s/%s.log"%(settings.LOG_PATH,log_type)
        fh = logging.FileHandler(log_file)#print to file
        fh.setLevel(settings.LOG_LEVEL)
        # create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # add formatter to ch and fh
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)

        # add ch and fh to logger
        logger.addHandler(ch)
        logger.addHandler(fh)

    return logger