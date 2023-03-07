from ExtremeAutomation.Library.Logger.RobotLogger import Logging


class TUTLibrary:
    def __init__(self):
        self.logger = Logging().get_logger()

    def print_step(self, message):
        self.logger.step(message)

    def print_cli(self, message):
        self.logger.cli(message)

    def print_trace(self, message):
        self.logger.trace(message)

    def print_info(self, message):
        self.logger.info(message)

    def print_debug(self, message):
        self.logger.debug(message)

    def print_warning(self, message):
        self.logger.warning(message)

    def print_critical(self, message):
        self.logger.critical(message)

    def print_error(self, message):
        self.logger.error(message)
