from extauto.common.Utils import Utils
from extauto.common.Logging import Logging
import traceback
import abc
import os
import pytest
"""  A JIRA AIQ-1403 was raised to track the following problem
    [ ERROR ] Unexpected error: ModuleNotFoundError: No module named 'robot.utils'
    We trace the issue back to when the CommonValidation.py was added to the system.
    When this file was added the __int__.py in root of the extreme_automation_framework
    was used and this caused all the robot libraries to be unloaded.
    If we comment out the 'import pytest' the issue is no longer seen.
    Since we do not know the intent of the pytest import we just disabled the validation in Login.py
"""

class FailureException(AssertionError):
    ROBOT_CONTINUE_ON_FAILURE = True
    pass

class CommonValidation():
    
    def __init__(self):
        self.logger = Logging().get_logger()
        self.utils = Utils()
    
    def validate(self, value, expectedValue, **kwargs):
        """
        Description: Validate the input values for framework
        
        kwargs:
            IRV = Internal Result verification flag, will be set to true by default
            fail_msg = The message to print on failure
            pass_msg = The message to print on success
            ignore_cli_feedback = which ignores any errors or output from the keyword
            expect_error = verifies that an error was returned by the keyword
        """
        test_result = False
        ivr_flag = self.get_kwarg(kwargs, "IRV", True)
        if ivr_flag:
            self.logger.info("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            self.logger.info("Internal Result Verification is Enabled")
            self.logger.info("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            default_fail_msg = "The keyword had a result of fail"
            fail_msg = self.get_kwarg(kwargs, "fail_msg", default_fail_msg)
            pass_msg = self.get_kwarg(kwargs, "pass_msg")

            # If the keyword is supported check for the existence of two kwargs.
            # ignore_cli_feedback, which ignores any errors or output from the keyword when
            # determining keyword pass/fail. expect_error, which verifies that an error
            # was returned by the keyword.
            ignore_cli = self.get_kwarg_bool(kwargs, "ignore_cli_feedback", False)
            expect_error = self.get_kwarg_bool(kwargs, "expect_error", False)

            # Get the expected value test result
            if value == expectedValue:
                test_result = True

            # If we are enabling both of this options that isn't allowed!
            if ignore_cli and expect_error:
                raise ValueError("Both ignore_cli_feedback and expect_error cannot be enabled.")

            # First check if there was a cli error.
            if not test_result and ignore_cli:
                self.logger.warning("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                self.logger.warning("kwarg - ignore_cli is Enabled return True")
                self.logger.warning("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                test_result = True

            if expect_error and not test_result:
                self.logger.warning("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                self.logger.warning("kwarg - expect_error is Enabled return True")
                self.logger.warning("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                test_result = True
            elif expect_error and test_result:
                self.logger.warning("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                self.logger.warning("kwarg - expect_error is Enabled return False")
                self.logger.warning("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                test_result = False

            # print the output
            if test_result:
                self.utils.print_info(pass_msg)
            else:
                # Print the error message
                full_error_msg = fail_msg + " Expected Value: " + str(expectedValue) + " Value: " + str(value)
                pytest.fail(full_error_msg, pytrace=False)
                assert value == expectedValue, full_error_msg
        else:
            test_result = True

        return test_result


    def get_kwarg_bool(self, kwargs, key, def_val):
        """Returns a normalized boolean from the kwarg."""
        return self.string_to_boolean(kwargs.get(key, def_val))

    def get_kwarg(self, kwargs, key, default=""):
        value = ''
        if key in kwargs:
            value = kwargs[key]
        else:
            value = default
        return value


    def string_to_boolean(self, boolean_string, default=True):
        """
        Converts boolean strings to a python boolean.
        Example "True" and "true" would be converted to True.
        The default option is used to set the boolean value when the passed string
        does not contain "True", "true", "False", or "false".

        """
        if str(type(boolean_string)) == "<type 'unicode'>":
            boolean_string = boolean_string.encode('utf8')

        if isinstance(boolean_string, str):
            if boolean_string.lower() == "true":
                boolean = True
            elif boolean_string.lower() == "false":
                boolean = False
            else:
                boolean = default
        elif isinstance(boolean_string, bool):
            boolean = boolean_string
        else:
            boolean = default

        return boolean

    def passed(self, **kwargs):
        """Description: This method will print the passing message and return 1"""
        return self.validate(1, 1, **kwargs)

    def failed(self, **kwargs):
        """Description: This method will print the failing message and raise an error if IRV is enabled"""
        return self.validate(-1, 1, **kwargs)