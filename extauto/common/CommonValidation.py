from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.Logging import Logging


class FailureException(AssertionError):
    ROBOT_CONTINUE_ON_FAILURE = True
    pass

class CommonValidation():

    def __init__(self):
        self.logger = Logging().get_logger()
        self.utils = Utils()
        self.screen = Screen()

    def fault(self, **kwargs):
        """
        Description: This method is used to raise an error and fail a test unconditionally.  This method should be
           called whenever there is an error in a keyword that cannot be worked around.  For example if as part of
           a keyword implementation we need to navigate to a page but were unable to navigate.

           A keyword fault differs from a failure in that the fault means the keyword was unable perform an action that
           is required to be performed before the ultimate keyword does its job.  For example:  For a "login user"
           keyword a fault would occur if the test could not enter the login credentials.  It would be considered a
           failure if the test could enter the credentials but was unable to log in.

        :param kwargs: A dictionary that contains the message to print when raising an error due to a keyword fault
        :return: This method does not return because it will raise an error causing the test to fail.
        """

        # Get the message that will be printed
        default_fail_msg = "[IRV] A fault occurred while running the keyword"
        fail_msg = self.get_kwarg(kwargs, "fail_msg", default_fail_msg)

        # Raise an error to cause the test to fail
        self._raise_error(fail_msg)
    def _raise_error(self, fail_msg):
        """
        Description:  The method raises an error causing the test to fail.  It also prints a failure message
            and captures a screenshot.

        :param fail_msg: The message to print to the test log before raising an error
        :return: This method causes an error and does not return
        """
        # Print the error message
        # Added screen capture in case of errors or problems
        self.screen.save_screen_shot()

        # todo psadej test this
        # Raise an exception for pytest and robot
        raise Exception(fail_msg)

    def validate(self, value, expectedValue, **kwargs):
        """
        Description: Validate the input values for framework

        kwargs:
            IRV = Internal Result verification flag, will be set to true by default
            fail_msg = The message to print on failure
            pass_msg = The message to print on success
            ignore_cli_feedback = ignores any errors or output from the keyword
            ignore_failure = Same as 'ignore_cli_feedback'
            expect_error = verifies that a failure was returned by the keyword
            expect_failure = Same as 'expect_error'
        """
        test_result = False
        ivr_flag = self.get_kwarg(kwargs, "IRV", True)

        if ivr_flag:
            self.logger.info("Internal Result Verification [IRV] is: Enabled")
            default_fail_msg = "[IRV] The keyword failed expectations"
            default_pass_msg = "[IRV] The keyword passed expectations"
            fail_msg = self.get_kwarg(kwargs, "fail_msg", default_fail_msg)
            pass_msg = self.get_kwarg(kwargs, "pass_msg", default_pass_msg)

            # If the keyword is supported, check for the existence of kwargs that manipulate how keyword results
            # should be interpreted.
            #
            #  ignore_cli_feedback or ignore_failure:
            #    - These kwargs indicate that we don't care whether the keyword failed or not.  We'll just print
            #      a message and return.  This is used primarily during cleanup.  For example, when deleting a
            #      device that may not exist.  If the test failed before adding the device then when trying to the
            #      delete the device it won't be there and we woudln't want to raise an error in that case.
            #
            #      The default for this is: False
            #
            #  expect_error or expect_failure:
            #    - These kwargs indicate that the keyword is expected to fail so if it does fail we should not raise
            #      an error; however, if it doesn't fail we should raise an error.   This is primarily used for negative
            #      testing.  For example, logging into an account with an invalid username or password.
            #
            #      The default for this is: False
            ignore_cli = False
            expect_error = False
            if 'ignore_cli_feedback' in kwargs:
                ignore_cli = self.get_kwarg_bool(kwargs, "ignore_cli_feedback", False)
            elif 'ignore_failure' in kwargs:
                ignore_cli = self.get_kwarg_bool(kwargs, "ignore_failure", False)
            if 'expect_error' in kwargs:
                expect_error = self.get_kwarg_bool(kwargs, "expect_error", False)
            elif 'expect_failure' in kwargs:
                expect_error = self.get_kwarg_bool(kwargs, "expect_failure", False)


            # Get the expected value test result
            if value == expectedValue:
                test_result = True

            # Ignoring errors and expected errors at the same time isn't allowed!
            if ignore_cli and expect_error:
                raise ValueError("[IRV] Expecting a failure and ignoring failures cannot be configured simultaneously")

            # If the test result failed and we're ignoring failures then we'll return true
            if not test_result and ignore_cli:
                self.logger.info("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                self.logger.info("[IRV] IRV is configured to ignore failures but a failure occurred!")
                self.logger.info("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                test_result = True

            if expect_error and not test_result:
                self.logger.info("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                self.logger.info("[IRV] IRV is configured to expect a failure and the keyword failed!")
                self.logger.info("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                test_result = True

            elif expect_error and test_result:
                self.logger.info("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                self.logger.info("[IRV] IRV is configured to expect a failure and the keyword did not fail")
                self.logger.info("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                test_result = False

            # Print the output
            if test_result:
                self.utils.print_info(pass_msg)
            else:
                self._raise_error(fail_msg)
        else:
            test_result = True

        return test_result


    def get_kwarg_bool(self, kwargs, key, def_val):
        """
        Returns a normalized boolean from the kwarg.
        """
        return self.string_to_boolean(kwargs.get(key, def_val))

    def get_kwarg(self, kwargs, key, default=""):
        """
        Description: Get a key from the kwargs dictionary.  Return the default value if the key is not found.

        :param kwargs: A dictionary passed into keywords that contains keys used to modify how the keyword shoudl run
        :param key: The key in the 'kwargs' dictionary that the caller is trying to extract
        :param default: The default value to be returned if the key is not found in the 'kwargs' dictionary
        :return:  The value for the kwarg or the default value if the key is not present in the 'kwargs' dictionary
        """
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
        """
        Description: This method will print the passing message and return 1 unless a failure is expected.  If
        a failure is expected (determined by kwargs) then an error will be raised

        """
        return self.validate(1, 1, **kwargs)

    def failed(self, **kwargs):
        """
        Description: This method will print the failing message and raise an error if IRV is enabled and
        a failure is not expected

        """
        return self.validate(-1, 1, **kwargs)