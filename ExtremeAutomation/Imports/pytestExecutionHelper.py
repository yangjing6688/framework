from pytest import skip, fail
import traceback
from ExtremeAutomation.Library.Logger.Logger import Logger


class PytestExecutionHelper():
    def __init__(self, defaultAction="skip"):
        """
        The pytest execution helper class will allow users to be able to set the action for all test cases when the setup fails.

        :param defaultAction: skip or fail are the allowed actions
        """
        self.logger = Logger()

        if defaultAction != "skip" and defaultAction != "fail":
            fail("Unable to create the PytestExecutionHelper class, the defaultAction must be set to 'skip' or 'fail'. the value " + defaultAction + " is not valid")

        self.logger.log_info("PytestExecutionHelper: setting default action for test cases as: [" + defaultAction + "]")
        self.action = defaultAction
        self.setup_failure = False
        
    def setSetupFailure(self, value):
        self.setup_failure = value
        self.__printException()
         
    def testSkipCheck(self):
        if self.setup_failure:
            if self.action == "skip":
                skip("Setup failed, so skipping the test")
            elif self.action == "fail":
                fail("Setup failed, so failing the test")
            
    def __printException(self):
        tb = traceback.format_exc()
        self.logger.log_error("Detected Exception: " + tb)
            
