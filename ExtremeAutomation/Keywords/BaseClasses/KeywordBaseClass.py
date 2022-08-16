import re
import abc
import inspect
import sys
from ExtremeAutomation.Library.Logger.Logger import Logger
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils
from ExtremeAutomation.Library.Device.Common.Agents.AgentConstants import AgentConstants
from ExtremeAutomation.Keywords.Utils.DeviceCollectionManager import DeviceCollectionManager
from ExtremeAutomation.Library.Device.Common.PlatformVariables.Library.PlatformVariables import PlatformVariables


class KeywordBaseClass(object):
    __metaclass__ = abc.ABCMeta

    DEBUG = False

    def __init__(self):
        self.logger = Logger()
        self.constants = None
        self.agent_constants = AgentConstants()
        self.device_collection = DeviceCollectionManager()
        self.robot_running = self._check_robot_running()

    def _pause(self):
        """
        This function will pause the current test if a failure occurs with the debug flag enabled.
        
        todo (jhall) - Need to find out if failed keyword injection is needed.
        """
        # if self.robot_running:
            # pause_execution("Keyword failed while in debug mode, pausing execution.")
            # self.built_in.run_keyword_and_continue_on_failure("fail", "Injecting a failed keyword to "
                                                                      # "show the test failed.")
                                                                      
    def _check_robot_running(self):
        return True
        # try:
            # self..get_variables()
            # return True
        # except RobotNotRunningError:
            # return False

    def _init_keyword(self, disable_strict_host_key_checking=False, **kwargs):
        """
        Initializes a given keyword.

        Supported kwargs:
            [device_name]          - A string name of a device.
            [check_initial_prompt] - A boolean indicating whether or not the device should be initialized
                                     after grabbing it from the device collection.
        """
        kw_name = self.get_keyword_name()
        device_name = kwargs.get("device_name", None)
        device = None

        if device_name:
            do_init = StringUtils.string_to_boolean(kwargs.get("check_initial_prompt", True))
            device = self.device_collection.get_device(device_name, init=do_init, disable_strict_host_key_checking=disable_strict_host_key_checking)

            if not device:
                self.logger.log_info("ERROR - Device not found, verify it was created.")

        #if kwargs.get("log_keyword", True):
        self.log_keyword(kw_name, device_name=device_name)

        return device

    def log_keyword_result(self, keyword_failed):
        # Log the results
        if not keyword_failed:
            keyword_value = 'Passed'
        else:
            keyword_value = "Failed"
        endOfLine = "\n\n"
        start = "****************************************************  "
        msg = "Keyword Results: {0} -> {1}".format(KeywordBaseClass.get_keyword_name(), keyword_value)
        end = "  ****************************************************"
        self.logger.log_info(endOfLine + start + msg + end + endOfLine)

    # +--------------------+
    # | Abstract Functions |
    # +--------------------+
    @abc.abstractmethod
    def _parse_kwargs(self, dev, **kwargs):
        pass

    # +------------------+
    # | Helper Functions |
    # +------------------+
    def _get_platform_variables(self, device_name):
        if self.robot_running:
            plat_var_gen = PlatformVariables()
            plat_var_gen.get_variables(device_name)

    def log_keyword(self, keyword_name, message="", log_level=Logger.INFO, device_name=""):
        """Logs the running keyword."""
        endOfLine = "\n\n"
        start = "****************************************************  "
        msg = "Running Keyword: {0} {1}".format(keyword_name, message)
        end = "  ****************************************************"
        if device_name:
            msg = "{0} on {1}".format(msg, device_name)

        self.logger.log_info(endOfLine + start + msg + end + endOfLine)
        self.logger.log_info(f"[+] {inspect.currentframe().f_code.co_name}()  Line: {sys._getframe().f_lineno}")

    @staticmethod
    def get_keyword_name():
        """Looks through the current stack trace and tries to find the currently running keyword name."""
        keyword = inspect.currentframe().f_back

        while keyword.f_code.co_name.lower() == "_init_keyword" or keyword.f_code.co_name.lower() == "_keyword_cleanup" or keyword.f_code.co_name.lower() == "log_keyword_result":
            keyword = keyword.f_back
        if len(re.findall("^execute_.*keyword$", keyword.f_code.co_name.lower())) == 1:
            keyword = keyword.f_back

        return keyword.f_code.co_name.replace("_", " ").title()

    @staticmethod
    def add_agent_kwarg(device, kwarg_key, kwargs):
        """
        Keyword Arguments:
        [device]    - The Network Element to add agent kwargs to.
        [kwarg_key] - The new agent kwarg to add.

        Checks to see if <kwarg_key> is present in <kwargs>. If it is, the value will be added to the
        device's agent dict with key <kwarg_key> and the retrieved value. If no value is found it is ignored.
        """
        kwarg_val = kwargs.get(kwarg_key, None)

        if kwarg_val is not None:
            device.agent_kwargs[kwarg_key] = kwarg_val

    @staticmethod
    def get_kwarg_bool(kwargs, key, def_val):
        """Returns a normalized boolean from the kwarg."""
        return StringUtils.string_to_boolean(kwargs.get(key, def_val))
