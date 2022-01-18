from robot.libraries.BuiltIn import BuiltIn
from ExtremeAutomation.Keywords.BaseClasses.KeywordBaseClass import KeywordBaseClass
from ExtremeAutomation.Keywords.Utils.GlobalVariableCache import GlobalVariableCache, GlobalVariableCacheConstants


class ExecutionKeywords(KeywordBaseClass):
    def __init__(self):
        super(ExecutionKeywords, self).__init__()
        self.robot_built_in = BuiltIn()
        self.var_cache = GlobalVariableCache()

    def run_keyword_if_previous_keyword_passed(self, keyword, *args, **kwargs):
        """
        This function checks the result of the last keyword run and only executes the included keyword if it passed.
        """
        execute_keyword = True
        previous_kw_result = self.var_cache.get_global_value(GlobalVariableCacheConstants.PREVIOUS_KW_RESULT)

        if previous_kw_result is not None:
            if previous_kw_result == ExecutionKeywordConstants.KW_RESULT_FAIL:
                execute_keyword = False
        else:
            self.logger.log_info("No previous keyword result found, executing keyword normally...")

        if execute_keyword:
            self.robot_built_in.run_keyword(keyword, *args, **kwargs)

    def run_keyword_if_previous_keyword_failed(self, keyword, *args, **kwargs):
        """
        This function checks the result of the last keyword run and only executes the included keyword if it failed.
        """
        execute_keyword = True
        previous_kw_result = self.var_cache.get_global_value(GlobalVariableCacheConstants.PREVIOUS_KW_RESULT)

        if previous_kw_result is not None:
            if previous_kw_result == ExecutionKeywordConstants.KW_RESULT_PASS:
                execute_keyword = False
        else:
            self.logger.log_info("No previous keyword result found, executing keyword normally...")

        if execute_keyword:
            self.robot_built_in.run_keyword(keyword, *args, **kwargs)

    def loop_keyword_on_device(self, keyword, device_names, *args, **kwargs):
        """
        This function executes the given keyword on all devices in the device_names list.
        """
        for device_name in device_names:
            self.robot_built_in.run_keyword(keyword, device_name, *args, **kwargs)


class ExecutionKeywordConstants(object):
    KW_RESULT_PASS = "PASS"
    KW_RESULT_FAIL = "FAIL"
