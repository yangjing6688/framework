import logging
from robot.libraries.BuiltIn import BuiltIn


class Logging:
    def __init__(self):
        self.logger = logging.getLogger('root')

    def set_log_level(self):
        log_level = BuiltIn().get_variable_value("${LOGLEVEL}")
        self.logger.setLevel(str(logging) + "." + log_level)

    def get_logger(self):
        return self.logger

    def log(self, message):
        _format = "[%(filename)s:%(lineno)s - %(funcName)s() ] %(message)s"
        logging.basicConfig(format=_format)
        self.logger.info("message:" + message)

