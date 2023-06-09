"""
    This Robot test library is used by:
    - TUT.robot in RobotLoggerTests.robot
    - TUTSetupTeardown.robot in RobotLoggerTests.robot
"""
from ExtremeAutomation.Library.Logger.RobotLogger import RobotLogger as Logging


class TUTLibrary:
    def __init__(self):
        self.logger = Logging()

    def print_trace(self, message):
        self.logger.trace(message)

    def print_debug(self, message):
        self.logger.debug(message)

    def print_info(self, message):
        self.logger.info(message)

    def print_warning(self, message):
        self.logger.warning(message)

    def print_error(self, message):
        self.logger.error(message)

    def print_suite_setup(self, message):
        self.logger.info(message)

    def print_suite_teardown(self, message):
        self.logger.info(message)

