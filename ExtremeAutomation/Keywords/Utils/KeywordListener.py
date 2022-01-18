from ExtremeAutomation.Library.Logger.Logger import Logger
from ExtremeAutomation.Keywords.Utils.GlobalVariableCache import GlobalVariableCache, GlobalVariableCacheConstants


class KeywordListener:
    ROBOT_LISTENER_API_VERSION = 2

    def __init__(self):
        self.step_manager = StepManager()
        self.logger = Logger()

    def start_suite(self, name, attrs):
        """
        This function currently does nothing.
        """
        pass

    def end_suite(self, name, attrs):
        """
        This function currently does nothing.
        """
        pass

    def start_test(self, name, attrs):
        """
        This function currently does nothing.
        """
        pass

    def end_test(self, name, attrs):
        """
        This function currently does nothing.
        """
        pass

    def start_keyword(self, name, attrs):
        """
        This function calls the StepManager.start_keyword.
        """
        self.step_manager.start_keyword(attrs["starttime"])

    def end_keyword(self, name, attrs):
        """
        This function calls the StepManager.end_keyword.
        """
        self.step_manager.end_keyword(attrs["starttime"], attrs["status"])


class StepManager(object):
    def __init__(self):
        self.logger = Logger()
        self.kw_started = False
        self.kw_start_time = None
        self.global_variable_cache = GlobalVariableCache()

    def start_keyword(self, start_time):
        """
        This function sets the Keyword Started flag and marks the start_time.
        """
        if not self.kw_started:
            self.kw_started = True
            self.kw_start_time = start_time

    def end_keyword(self, start_time, status):
        """
        This function resets the Keyword Started flag and saves the Keyword result.
        """
        if self.kw_started:
            if start_time == self.kw_start_time:
                self.kw_started = False
                self.global_variable_cache.add_global_value(GlobalVariableCacheConstants.PREVIOUS_KW_RESULT,
                                                            status, log=False)
