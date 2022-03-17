import os
import re
import time
import logging
import inspect
import uuid
import subprocess
from datetime import datetime
from ExtremeAutomation.Library.Utils.StatsUtils import MicroserviceInterface
from ExtremeAutomation.Library.Utils.ListUtils import ListUtils
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils
from ExtremeAutomation.Keywords.FailureException import FailureException
from ExtremeAutomation.Keywords.BreakFailureException import BreakFailureException
from ExtremeAutomation.Keywords.BaseClasses.KeywordResult import KeywordResult
from ExtremeAutomation.Keywords.Utils.DeviceValueStorage import DeviceValueStorage
from ExtremeAutomation.Keywords.BaseClasses.KeywordBaseClass import KeywordBaseClass
from ExtremeAutomation.Library.Device.Common.Agents.LoginManagementAgent import LoginManagementAgent
from ExtremeAutomation.Library.Device.Common.CommandObjects.CommandObjectConstants import CommandObjectConstants
from ExtremeAutomation.Library.Device.NetworkElement.Constants.NetworkElementConstants import NetworkElementConstants


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class NetworkElementKeywordBaseClass(KeywordBaseClass):

    def __init__(self):

        super(NetworkElementKeywordBaseClass, self).__init__()

        self.constants = NetworkElementConstants()
        self.cmd_obj_constants = CommandObjectConstants()
        self.api_const = None
        self.value_storage = DeviceValueStorage()
        self.continue_on_failure = None

    def execute_keyword(self, device_name, args, api_str, **kwargs):
        """
        Executes a configuration keyword. Gets the device and API then runs the given <api_func> and
        returns the results.

        Function Args:
            device_name - The name of the device that should be retrieved from the device collection.
            api_func - The name of the function within the API to execute. This should (almost)
                       always be from a constants file.
            *args - The non-named args to pass to the keyword.
            **kwargs - The named args to pass to the keyword.
        """
        # Create a list of keyword results
        kw_results = []

        # If no API constant is passed use the class api_const attribute.
        # This MUST be set by child classes.
        api_const = kwargs.get("command_api_const", self.api_const)

        # Generate a list of arguments based on the passed args dictionary.
        if kwargs.get("list_value_arg", False):
            arg_list = [args]
        else:
            arg_list = ListUtils.generate_arg_list(**args)

        for arg_dict in arg_list:
            # Initialize the keyword by getting the device and API. Ignore the
            # returned parse API as it will be None.
            dev, api, _ = self._init_keyword(device_name, api_const, None, **kwargs)

            if dev is not None:
                # Get the command object from the API and send it to the device.
                # Then return the commando object that is returned by the device.
                cmd_obj = getattr(api, api_str)(arg_dict, **kwargs)
                # If the command object returned is supported, have the device execute it.
                if not cmd_obj.not_supported:
                    cmd_obj = dev.send_command_object(cmd_obj)
                    try:
                        self._parse_microservice_input(cmd_obj=cmd_obj,dev_obj=dev)
                    except Exception as e:
                        self.logger.log_info("Unable to record keyword stats for " + str(cmd_obj.uuid))
                kw_results.append(self._determine_result(dev, cmd_obj, **kwargs))

                self._init_keyword(device_name, api_const, None, **kwargs)
            else:
                kw_results.append(KeywordResult(device_name, False, "", "Device \"" + device_name +"\" does not exist!", None))
                break

        return self._keyword_cleanup(kw_results)

    def execute_verify_keyword(self, device_name, args, cmd_str, parse_str, expected_result, pass_str, fail_str,
                               **kwargs):
        """
        Executes a verification keyword. Gets the device, command API, and parse API then runs the
        give <cmd_func> before passing it's output to <parse_func>. Returns result == expected_result.

        Function Args:
            name            - The name of the device this keyword will be run against.
            cmd_str         - The string name of a function within the command API to execute.
                              This should (almost) always be from a constants file.
            parse_str       - The string name of a function within the parse API to execute.
                              This should (almost) always be from a constants file.
            expected_result - A boolean that represents the expected return from the parse function.
            pass_str        - The string that should be added to the log if the keyword passes.
            fail_str        - The string that should be added to the log if the keyword fails.
            **kwargs        - The named args to pass to the keyword.
        """

        # Create a list for keyword results.
        kw_results = []

        # Set the command and parse API constants if they were passed, otherwise use
        # the class attribute api_const.
        cmd_api_const = kwargs.get("command_api_const", self.api_const)
        parse_api_const = kwargs.get("parse_api_const", self.api_const)
        arg_list = ListUtils.generate_arg_list(**args)

        return_value = []
        for arg_dict in arg_list:
            # Initialize the keyword by getting the device, command API, and parse API.
            dev, cmd_api, parse_api = self._init_keyword(device_name, cmd_api_const, parse_api_const, **kwargs)

            if dev is not None:
                # Get the show and parse functions from their respective APIs.
                show_func = getattr(cmd_api, cmd_str)
                parse_func = getattr(parse_api, parse_str)
                ret_dict = {}

                # If we are doing a wait for verification gather the required arguments.
                # Then perform the wait for keyword.
                if self.get_kwarg_bool(kwargs, "wait_for", False):
                    message = kwargs.get("message", "Waiting for {0}...".format(pass_str))
                    kwargs["message"] = self._format_string(device_name, arg_dict, message, ret_dict)
                    cmd_obj, result, ret_dict = self._wait_for(dev, show_func, parse_func, expected_result, arg_dict,
                                                               **kwargs)
                # Otherwise perform the keyword normally. Execute the show function
                # then pass the output to the parser and get the result.
                else:
                    result = None
                    cmd_obj = show_func(arg_dict, **kwargs)
                    if not cmd_obj.not_supported:
                        # Check if the user wants to use show cmd return text from history and that it exists in
                        # the history. Otherwise send the cmd and use that return text.
                        # try:
                        if self.get_kwarg_bool(kwargs, "use_cached", False) and \
                                dev.show_command_history.get(cmd_obj.command):
                            result, ret_dict = parse_func(dev.show_command_history.get(cmd_obj.command), arg_dict,
                                                          **kwargs)
                            return_value.append(ret_dict)
                        else:
                            cmd_obj = dev.send_command_object(cmd_obj)
                            dev.show_command_history[cmd_obj.command] = cmd_obj.return_text
                            result, ret_dict = parse_func(cmd_obj.return_text, arg_dict, **kwargs)
                            return_value.append(ret_dict)
                        # except TypeError as e:
                        #     self.logger.log_error(e)
                        #     self.logger.log_error("ParseAPI did not return a Tuple! Defaulting to 'None'.")

                # Format the pass and fail strings converting an values with {} around them.
                # Then call determine_result with the parse result, expected result, and the
                # formatted pass/fail strings. Finally call the keyword cleanup and return
                # the result.
                format_pass = self._format_string(device_name, arg_dict, pass_str, ret_dict)
                format_fail = self._format_string(device_name, arg_dict, fail_str, ret_dict)
                kw_results.append(self._determine_result(dev, cmd_obj, result, expected_result,
                                                         format_pass, format_fail, **kwargs))
            else:
                kw_results.append(KeywordResult(device_name, False, "", "Device \"" + device_name +
                                                "\" does not exist!", None))
                break

        cmd_obj = self._keyword_cleanup(kw_results, return_value)

        if len(return_value) > 1:
            return cmd_obj, return_value
        elif len(return_value) == 1:
            return cmd_obj, return_value[0]
        else:
            return cmd_obj, None

    # +-----------------+
    # | Private Methods |
    # +-----------------+
    def _init_keyword(self, device_name=None, cmd_const=None, parse_const=None, **kwargs):
        """
        Runs the needed initialization before executing a keyword. Gets the device object and API
        requested by the keyword.

        Function Args:
            [device_name] - The name of the device that should be retrieved from the device collection.
            [cmd_const] - A string indicating which command API should be used.
            [parse_const] - A string indicating which parse API should be used.
        """
        dev = super(NetworkElementKeywordBaseClass, self)._init_keyword(device_name=device_name, **kwargs)
        cmd_api, parse_api = None, None
        self._parse_kwargs(dev, **kwargs)

        if dev:
            if cmd_const:
                cmd_api = dev.get_api(cmd_const)

                if not cmd_api:
                    self.logger.log_error("ERROR - Command API not found, verify it exists.")
            if parse_const:
                parse_api = dev.get_parse_api(parse_const)

                if not parse_api:
                    self.logger.log_error("ERROR - Parse API not found, verify it exists.")
        else:
            return None, None, None

        return dev, cmd_api, parse_api

    def _determine_result(self, dev, cmd_obj, result=None, expected_result=None, pass_string="Keyword Passed",
                          fail_string="Keyword Failed", **kwargs):
        cmd_result = True
        parse_result = True

        # Clear the temporary error lists on the device.
        if dev:
            dev.error_checker.clear_temp_error_list()
            dev.error_checker.clear_ignore_error_list()

        # First check if the command object is marked as not supported or the passed result
        # is equal to "METHOD_NOT_SUPPORTED". In either case pass the keyword and make a note
        # that it only passed because it's not supported.
        if cmd_obj.not_supported or result == self.cmd_obj_constants.METHOD_NOT_SUPPORTED:
            # todo - Create a better method for marking unsupported keywords.
            kw_result = KeywordResult(dev.name, True,
                                      "Pass, but only due to the fact that the method is not supported", "",
                                      cmd_obj)
        else:
            # If the keyword is supported check for the existence of two kwargs.
            # ignore_cli_feedback, which ignores any errors or output from the CLI when
            # determining keyword pass/fail. expect_error, which verifies that an error
            # was returned by the keyword.
            ignore_cli = self.get_kwarg_bool(kwargs, "ignore_cli_feedback", False)
            expect_error = self.get_kwarg_bool(kwargs, "expect_error", False)
            get_only = self.get_kwarg_bool(kwargs, "get_only", False)

            if ignore_cli and expect_error:
                raise ValueError("Both ignore_cli_feedback and expect_error cannot be enabled.")

            # First check if there was a cli error.
            if cmd_obj.error_state and not ignore_cli:
                cmd_result = False
                fail_string = "Error in command: " + cmd_obj.error_text

            # If result was supplied to the function check if the result
            # is equal to the expected result.
            if result is not None:
                parse_result = result == expected_result

            # and the cmd and parse results to the get the test result.
            test_result = cmd_result and parse_result

            # If expect error is set to true make sure an error occurred.
            if expect_error and not test_result:
                test_result = True
            elif expect_error and test_result:
                test_result = False

            # Finally create a KeywordResult object based on all the information gathered and append it
            # to the kw_results list.
            if not get_only:
                kw_result = KeywordResult(dev.name, test_result, pass_string, fail_string, cmd_obj)
            else:
                kw_result = KeywordResult(dev.name, True, "Returning parse values.", fail_string, cmd_obj)

        return kw_result

    def _keyword_cleanup(self, kw_results, ret_vals=None):
        keyword_failed = False
        
        # error_information = ""

        # Iterate over each result in the keyword result list and log it.
        # Check each result to see if it failed, if a keyword has failed
        # change the keyword failed flag to True.
        for result in kw_results:
            error_results = result.print_kw_result()
            if not result.test_result and not keyword_failed:
                keyword_failed = True
                # error_information =  error_information + "DUT:" +  result.device_name + "\n " + "Command: " + result.command + "\n Result: " + result.cmd_obj.return_text.replace("r\r\n","\n ") + "\n\n"

        # Check the keyword failed flag, if it's True check if we are debugging a robot
        # execution, if yes pause the test otherwise raise a Failure exception.
        if keyword_failed:
            if self.robot_running:
                if self.DEBUG:
                    self._pause()
                else:
                    err_msg = "Keyword Failed!\n Returned Values: " + str(ret_vals) + " \n " + error_results
                    fail_excep = FailureException(err_msg) if self.continue_on_failure \
                        else BreakFailureException(err_msg)
                    raise fail_excep

        super(NetworkElementKeywordBaseClass, self).log_keyword_result(keyword_failed)

        return kw_results

    def _wait_for(self, dev, show_func, parse_func, expected_result, args, **kwargs):
        """
        This function executes a wait for validation. It checks the result of the passed parse function
        every <interval> until it matches the expected result or <max_wait> seconds have passed.

        Arguments:
            [max_wait] - The maximum amount of time the function wait before stopping.
            [interval] - The amount of time to wait between each check.
            [msg] - The message to print after each execution.
            [show_func] - The command API function which gets the data needed by the parser.
            [parse_func] - The parse API function which parse the retrieved data.
            [**kwargs] - Arguments that should be passed to show_func and parse_func.
        """
        # Get the max wait, interval, and message vars from the keyword arguments.
        max_wait = int(kwargs.get("max_wait", 60))
        interval = int(kwargs.get("interval", 1))
        msg = kwargs["message"]

        # Execute the show function and get an initial result from the parse function.
        # If the result == expected result the while loop will be bypassed as the
        # pass condition has already been met.
        cmd_obj = show_func(args, **kwargs)
        cmd_obj = dev.send_command_object(cmd_obj)
        result, ret_dict = parse_func(cmd_obj.return_text, args, **kwargs)

        # If the parse_func returns N/S return it, no need to loop if the
        # parser isn't supported.
        if result == self.cmd_obj_constants.METHOD_NOT_SUPPORTED:
            return cmd_obj, result

        start = time.time()

        # Loop while < max_wait seconds have passed and the result doesn't equal the expected result.
        # First delay for <interval> seconds then print the msg (if applicable) then re-execute the
        # show and parse functions.
        while time.time() - start < max_wait and result != expected_result:
            time.sleep(interval)
            if msg:
                self.logger.log_info(msg + " [Elapsed Time: " + str(int(time.time() - start)) + " seconds]")

            cmd_obj = show_func(args, **kwargs)
            cmd_obj = dev.send_command_object(cmd_obj)
            result, ret_dict = parse_func(cmd_obj.return_text, args, **kwargs)
        return cmd_obj, result, ret_dict

    @staticmethod
    def _format_string(name, args, string, parse_return):
        """
        Formats a pass/fail string with the following format.

        s = "Example string on {device_name} using args: {arg1} and {arg2}."

        Give the args the string would be formatted as follows.

        args = {"arg1": "myFirstArg", "arg2": "mySecondArg"}

        _format_string("myDevice", args, s) = "Example string on myDevice using args: myFirstArg and mySecondArg."

        Function Args:
            name - The name of the device.
            args - A dictionary of the arguments passed to the keyword.
            string - The string to be formatted.
        """
        format_string = string

        # Use regex to find all instances of {<str>} within the <string>.
        string_vars = re.findall("{.*?}", string)

        # Iterate over each variables located by the above regex.
        for string_var in string_vars:
            # If {device_name} was found, replace it with the passed name.
            # This is a special case all other {<str>} vars MUST be present
            # in the passed <args> dictionary.
            if "device_name" in string_var:
                format_string = format_string.replace(string_var, name)
            elif "ret_dict" in string_var:
                format_string = format_string.replace(string_var, str(parse_return))
            else:
                # Format the current variable by removing its surrounding {} chars.
                # Then, if the formatted variable is in the <args> dictionary replace
                # all instances of it with with it's corresponding value.
                format_var = string_var.strip("{}")
                if format_var in args:
                    format_string = format_string.replace(string_var, args[format_var])
                elif format_var in parse_return:
                    format_string = format_string.replace(string_var, parse_return[format_var])
        return format_string

    def _parse_kwargs(self, dev, **kwargs):
        """
        This function checks the passed kwargs for the following kwargs and sets attributes as needed.

        Supported kwargs:
            [wait_for_prompt] - This is used to disable (it's enabled by default) wait for prompt functionality
                                on a given device. If set it will be disabled on the next keyword call.
            [cmd_delay] - This sets the time in milliseconds to wait between each command sent.
            [add_error] - This adds errors to the devices error checker to check for the given keyword.
            [ignore_error] - This adds errors to the devices error checker to ignore for the given keyword.
        """
        super(NetworkElementKeywordBaseClass, self)._parse_kwargs(dev, **kwargs)
        wait_for_prompt = kwargs.get("wait_for_prompt", True)
        cmd_delay = kwargs.get("cmd_delay", self.constants.DEFAULT_SLEEP_BETWEEN_COMMANDS)
        add_errors = kwargs.get("add_error", [])
        ignore_errors = kwargs.get("ignore_error", [])
        if dev is None or dev.continue_on_failure is None:
            self.continue_on_failure = self.get_kwarg_bool(kwargs, 'continue_on_failure', True)
        else:
            self.continue_on_failure = StringUtils.string_to_boolean(dev.continue_on_failure)
        if dev and StringUtils.string_to_boolean(wait_for_prompt):
            dev.wait_for_prompt = StringUtils.string_to_boolean(wait_for_prompt)
        elif dev:
            dev.wait_for_prompt = False

        if isinstance(cmd_delay, int):
            try:
                dev.current_agent.default_sleep_between_commands = cmd_delay
            except AttributeError:
                LoginManagementAgent.default_sleep_between_commands = cmd_delay
        elif isinstance(cmd_delay, str) and cmd_delay.isdigit():
            try:
                dev.current_agent.default_sleep_between_commands = int(cmd_delay)
            except AttributeError:
                LoginManagementAgent.default_sleep_between_commands = int(cmd_delay)
        else:
            try:
                dev.current_agent.default_sleep_between_commands = self.constants.DEFAULT_SLEEP_BETWEEN_COMMANDS
            except AttributeError:
                LoginManagementAgent.default_sleep_between_commands = self.constants.DEFAULT_SLEEP_BETWEEN_COMMANDS

        if add_errors:
            errs = ListUtils.convert_to_list(add_errors)
            for err in errs:
                dev.error_checker.add_error_to_temp_list(err)

        if ignore_errors:
            errs = ListUtils.convert_to_list(ignore_errors)
            for err in errs:
                dev.error_checker.add_error_to_ignore_list(err)


    
    @staticmethod
    def _parse_microservice_input(**kwargs):

        """
        This static method expects kwargs to contain the following objects:

            cmd_obj 
            dev_obj 
        
        Data is managed in the 'econ-stats' microservice as follows:

        #1. First, add the testfile name and repo info into the 'testFiles' 
            table. If the testfile entry already exists, we retrieve and
            re-use that entry's UUID.
            If it's a new testfile entry, we generate a new UUID and use that 
            gong forward.
    
        #2  Next, add data into the 'keywordTiming' table. The data is defined
            in the postThis dictionary below. (includes the testfile UUID from
            the first step (tfUuid))

        #3  Finally, add the kwUuid & kwName data into the 'kwEvent' table.

        """
        this_function_name = inspect.currentframe().f_code.co_name
        callingfunction_name = inspect.currentframe().f_back.f_code.co_name
        logger.info("[+] Entering function   : %s()", this_function_name)
        logger.info("[+] Called from function: %s()", callingfunction_name)
   
        cmd_obj = kwargs.get("cmd_obj", False)
        dev_obj = kwargs.get("dev_obj", False)
  
        assert cmd_obj is not False and dev_obj is not False
 
        statsObj  = MicroserviceInterface()
        startTime = datetime.fromtimestamp(cmd_obj.start_time).strftime("%Y-%m-%d %H:%M:%S.%f")
        endTime   = datetime.fromtimestamp(cmd_obj.end_time).strftime("%Y-%m-%d %H:%M:%S.%f")
        end       = datetime.strptime(endTime,"%Y-%m-%d %H:%M:%S.%f")
        start     = datetime.strptime(startTime,"%Y-%m-%d %H:%M:%S.%f")

        # Informational/logging only ... the stats microservice 
        # calculates elapsed time, so no need to post
        #
        elapsedTime = end - start

        # Step #1:
        #
        logger.info(" [+] Step #1: Update testFiles table data")
        
        # If we have a problem running the git command, set a default value. 
        # This is for information logging only, so it's not worth failing over. 
        #
        try:
            gitRepo   = os.path.basename(subprocess.check_output(["git", "rev-parse", "--show-toplevel"]).decode().strip())
        except:
             gitRepo = 'extreme_automation_tests'

        tfileName = re.split(r':', os.getenv('PYTEST_CURRENT_TEST'))[0]
        tfileData = {
                "testfileName": str(tfileName),
                "testfileRepo": str(gitRepo)
                    }

        tfUuid = statsObj.postTfile(tfileData)

        logger.info(" [+] testfileUuid  : %s", tfUuid)
        logger.info(" [+] testfileName  : %s", tfileName)
        logger.info(" [+] testfileRepo  : %s", gitRepo)

        # Step #2:
        #
        logger.info(" [+] Step #2: Update keywordTiming table data")

        postThis = { 
                "startTime":str(startTime),
                "endTime":str(endTime),
                "os":dev_obj._oper_sys,
                "connectionType":dev_obj.connection_method,
                "hwType":dev_obj.platform,
                "keywordUuid":cmd_obj.uuid,
                "testCaseUuid":str(tfUuid)
                   }
         
        status = statsObj.postStats(postThis)

        logger.info(" [+] Start Time    : %s", startTime)
        logger.info(" [+] End Time      : %s", endTime)
        logger.info(" [+] Elapsed Time  : %s", elapsedTime)
        logger.info(" [+] os            : %s", dev_obj._oper_sys)
        logger.info(" [+] connectionType: %s", dev_obj.connection_method)
        logger.info(" [+] hwType        : %s", dev_obj.platform)
        logger.info(" [+] keywordUuid   : %s", postThis['testCaseUuid'])
        logger.info(" [+] testCaseUuid  : %s", postThis['testCaseUuid'])
        logger.info(" [+] Status        : %s", status)

        # Step #2:
        #
        logger.info(" [+] Step #3: Update kwEvent table data")
        eventData = {
                "keywordUuid": postThis['keywordUuid'],
                "keywordName": str(cmd_obj._command)
                    }

        logger.info(" [+] keywordUuid   : %s", postThis['keywordUuid'])
        logger.info(" [+] keywordName   : %s", cmd_obj._command)

        eventStat = statsObj.postEvent(eventData)
        logger.info(" [+] eventStat     : %s", eventStat)

        logger.info("[+] Leaving function     : %s()", this_function_name)
        logger.info("[+] Returning to function: %s()", callingfunction_name)
