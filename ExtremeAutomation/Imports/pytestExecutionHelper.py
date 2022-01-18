from pytest import skip
import traceback
from ExtremeAutomation.Library.Logger.Logger import Logger


class PytestExecutionHelper():
    def __init__(self):
        self.setup_failure = False
        self.logger = Logger()
        
    def setSetupFailure(self, value):
        self.setup_failure = value
        self.__printException()
         
    def testSkipCheck(self):
        if self.setup_failure:
            skip()
            
    def __printException(self):
        tb = traceback.format_exc()
        self.logger.log_error("Detected Exception: " + tb)
            