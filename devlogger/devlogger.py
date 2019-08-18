import logging


class Logger:
    def __init__(self, logger):
        # self.logger = logging.getLogger(__name__)
        self.logger = logger
        logging.basicConfig(filename='application.log', filemode='w',
                            format='%(levelname)s : %(name)s : %(message)s',
                            level=logging.INFO)
        self.logger.info("Logger setup successful")

    def log_i(self, message):
        self.logger.info(message)

    def log_w(self, message):
        self.logger.warning(message)

    def log_e(self, message):
        self.logger.error(message)
