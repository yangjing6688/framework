from ExtremeAutomation.Library.Utils.Time import get_timestamp
from ExtremeAutomation.Library.Utils.ListUtils import ListUtils
from ExtremeAutomation.Keywords.BaseClasses.KeywordResult import KeywordResult
from ExtremeAutomation.Keywords.FailureException import FailureException
from ExtremeAutomation.Keywords.BreakFailureException import BreakFailureException
from ExtremeAutomation.Keywords.BaseClasses.KeywordBaseClass import KeywordBaseClass
from ExtremeAutomation.Library.Device.Common.CommandObjects.UiCommandObject import UiCommandObject
from ExtremeAutomation.Library.Device.UiElement.Constants.UiElementConstants import UiElementConstants
from ExtremeAutomation.Library.Device.NetworkElement.Constants.NetworkElementConstants import NetworkElementConstants
from ExtremeAutomation.Library.Device.UiElement.Commands.ApiUtils.UiApiBuilder import UiApiBuilder


class UiKeywordBaseClass(KeywordBaseClass):
    def __init__(self):
        super(UiKeywordBaseClass, self).__init__()
        self.constants = UiElementConstants()
        self.api_const = None
        self.continue_on_fail = True
        self.ne_const = NetworkElementConstants()

    def _init_keyword(self, device_name=None, cmd_const=None, **kwargs):
        dev = super(UiKeywordBaseClass, self)._init_keyword(device_name=device_name, **kwargs)
        cmd_api = None

        if dev:
            if cmd_const:
                cmd_api = dev.get_api(cmd_const)

                if not cmd_api:
                    self.logger.log_error("ERROR - API not found, verify it exists")
        else:
            return None, None

        return dev, cmd_api

    def _determine_results(self, dev, cmd_obj, result=None, expected_result=None, pass_string="Keyword Passed",
                           fail_string="Keyword Failed", **kwargs):
        if cmd_obj and cmd_obj.not_supported:
            pass_string = "Pass, but only due to the fact that the method is not supported."
            kw_result = KeywordResult(dev.name, True, pass_string, fail_string, cmd_obj)
        else:
            cmd_result = True
            verify_result = True
            expect_error = self.get_kwarg_bool(kwargs, "expect_error", False)

            if cmd_obj.error_state:
                cmd_result = False

            if result is not None:
                verify_result = result == expected_result

            test_result = cmd_result and verify_result

            if expect_error and not test_result:
                test_result = True
            elif expect_error and test_result:
                test_result = False

            kw_result = KeywordResult(dev.name, test_result, pass_string, fail_string, cmd_obj)
        return kw_result

    def _keyword_cleanup(self, dev, kw_results):
        keyword_failed = False
        cmd_obj = None

        # Iterate over each result in the keyword result list and log it.
        # Check each result to see if it failed, if a keyword has failed
        # change the keyword_failed flag to True.
        for result in kw_results:
            result.print_kw_result()
            cmd_obj = result.cmd_obj
            if not result.test_result and not keyword_failed:
                keyword_failed = True

        if keyword_failed:
            if self.DEBUG:
                self._pause()
            else:
                # Take a screen shot when a failure occurs.
                file_name = "{0}_{1}.png".format(get_timestamp(), self.get_keyword_name())
                builder = UiApiBuilder(dev)
                builder.screen_shot(cmd_obj, file_name)

                err_msg = "Keyword Failed!"
                fail_excep = FailureException(err_msg) if self.continue_on_fail else BreakFailureException(err_msg)
                raise fail_excep

        return kw_results

    def execute_keyword(self, device_name, arg_dict, api_function, **kwargs):
        """
        [device_name]       - The name of the device the keyword should be run against.
        [arg_dict]          - This must be a dictionary of the arguments passed to the keyword. The key should be the
                              value specified in the CSV and the value should be argument passed to the keyword.
                              For Example: CSV args = "arg1", "arg2", "arg3". Keyword args = val1, val2, val3.
                              arg_dict = {"arg1": val1, "arg2": val2, "arg3": val3}
        [api_function]      - This should be a string with the same name as the interface_method in the CSV.
        [command_api_const] - Used when a non-default command_api should be used. The default is specified in the
                              __init__ for each keyword class.
        """
        kw_results = []
        api_const = kwargs.get("command_api_const", self.api_const)
        arg_list = ListUtils.generate_arg_list(**arg_dict)
        dev = None

        for args in arg_list:
            dev, cmd_api = self._init_keyword(device_name, api_const, **kwargs)
            cmd_obj = getattr(cmd_api, api_function)(UiCommandObject(), args)

            kw_results.append(self._determine_results(dev, cmd_obj, **kwargs))
        return self._keyword_cleanup(dev, kw_results)

    def _parse_kwargs(self, dev, **kwargs):
        super(UiKeywordBaseClass, self)._parse_kwargs(dev, **kwargs)

        self.continue_on_fail = self.get_kwarg_bool(kwargs, "continue_on_fail", True)
