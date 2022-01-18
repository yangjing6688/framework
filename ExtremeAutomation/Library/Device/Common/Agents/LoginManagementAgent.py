import abc
from ExtremeAutomation.Library.Device.Common.Agents.DeviceAgent import DeviceAgent


class LoginManagementAgent(DeviceAgent, metaclass=abc.ABCMeta):
    def __init__(self, device):
        super(LoginManagementAgent, self).__init__(device)
        self.connected = False
        self.logged_in = False
        self.slow_login_time = 0
        self.main_session = None
        self.debug = False
        self.type = ""
        self.default_sleep_between_commands = self.constants.DEFAULT_SLEEP_BETWEEN_COMMANDS
        self.wait_for_sleep = self.constants.WAIT_FOR_SLEEP
        self.wait_for_retries = self.constants.WAIT_FOR_RETRIES

    @abc.abstractmethod
    def login(self):
        """
        Login function, any child class should override this with the means to log in via
        the given agent.
        """
        pass

    @abc.abstractmethod
    def connect(self):
        """
        Connect function, any child class should override this with the means to connect
        via the given agent.
        """
        pass

    @abc.abstractmethod
    def disconnect(self):
        """
        Disconnect function, any child class should override this with the means to disconnect
        via the given agent.
        """
        pass

    @abc.abstractmethod
    def logout(self):
        """
        Logout function, any child class should override this with the means to logout via
        the given agent.
        """
        pass

    @abc.abstractmethod
    def send_command_object(self, cmd_obj, **kwargs):
        """
        This function handles sending the given command object. The command object depends on the agent
        type being used. Any child class should override this with the code needed to handle any supported
        command objects.
        """
        pass

    def debug_print(self, msg):
        """
        This function checks the debug flag, if it's set it will log the given <msg> at info level.
        """
        if self.debug:
            self.logger.log_info(msg)
