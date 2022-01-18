import socket
from ExtremeAutomation.Library.Device.Common.Agents.SnmpAgent import SnmpAgent
from ExtremeAutomation.Library.Device.Common.Agents.RestAgent import RestAgent
from ExtremeAutomation.Library.Device.Common.Agents.XmcAgent import XmcAgent
from ExtremeAutomation.Library.Device.Common.Agents.SshAgent import SshAgent
from ExtremeAutomation.Library.Device.Common.Agents.SerialAgent import SerialAgent
from ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent import TelnetAgent
from ExtremeAutomation.Library.Device.Common.Agents.ConsoleAgent import ConsoleAgent
from ExtremeAutomation.Library.Device.Common.Agents.JsonRpcAgent import JsonRpcAgent
from ExtremeAutomation.Library.ParsingHelper.InspectionToolkit import InspectionToolkit
from ExtremeAutomation.Library.Device.Common.ManagedDeviceObject import ManagedDeviceObject
from ExtremeAutomation.Library.Device.Common.Factories.PromptFactory import PromptFactory
from ExtremeAutomation.Library.Device.Common.Factories.ErrorCheckerFactory import ErrorCheckerFactory
from ExtremeAutomation.Library.Device.NetworkElement.Constants.NetworkElementConstants import NetworkElementConstants
from ExtremeAutomation.Library.Device.Common.CommandObjects.RestCommandObject import RestCommandObject
from ExtremeAutomation.Library.Device.Common.Agents.DeviceAgent import DeviceAgent
from ExtremeAutomation.Library.Device.Common.CommandObjects.CliCommandObject import CliCommandObject



import inspect
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logging.basicConfig(format='[%(asctime)s] %(levelname)s: [%(filename)s %(name)s %(funcName)s (Line#%(lineno)d)]: %(message)s')

class NetworkElement(ManagedDeviceObject):
    def __init__(self, oper_sys, platform, unit, version):
        super(NetworkElement, self).__init__()
        self.debug_password = ""
        self.oper_sys = oper_sys
        self.platform = platform
        self.unit = unit
        self.version = version
        self.login_prompt = ""
        self.pass_prompt = ""
        self.main_prompt = ""
        self.model = ""
        self.running_version = ""
        self.current_agent = None
        self.wait_for_prompt = True
        self.max_connection_retries = 3
        self.eol = None
        self.show_command_history = dict()

        # Set attributes with factories.
        self.error_checker = ErrorCheckerFactory().get_api(self)
        self.inspection_toolkit = InspectionToolkit(self)

        # Valid agents for NetworkElements.
        self.agent_dict = {self.agent_constants.TYPE_TELNET: TelnetAgent,
                           self.agent_constants.TYPE_SSH: SshAgent,
                           self.agent_constants.TYPE_REST: RestAgent,
                           self.agent_constants.TYPE_SNMP: SnmpAgent,
                           self.agent_constants.TYPE_SERIAL: SerialAgent,
                           self.agent_constants.TYPE_XMC_REST: XmcAgent,
                           self.agent_constants.TYPE_JSON_RPC: JsonRpcAgent,
                           self.agent_constants.TYPE_CONSOLE: ConsoleAgent}
        self.agent_sessions = {}

######################################################################################
    def get_named_agent(self):
        logger.info("[+]Current Agent: %s", self.agent_dict[self.connection_method])

    def set_named_agent(self, name, agent_type, port):

        """ Switch to new connection """

        # If name not in agent_sessions,  create it, otherwise set the agent

        device = self
        if name not in self.agent_sessions:
            if agent_type == self.agent_constants.TYPE_TELNET:
                new_agent = TelnetAgent(device)
                self.agent_sessions[name] = new_agent
                self.current_agent = self.agent_sessions[name]
                self.current_agent.login()
            elif agent_type == self.agent_constants.TYPE_REST:
                 new_agent = RestAgent(device)
                 self.agent_sessions[name] = new_agent
                 self.current_agent = self.agent_sessions[name]
                 self.current_agent.login()
            elif agent_type == self.agent_constants.TYPE_SNMP:
                 new_agent = SnmpAgent(device)
                 self.agent_sessions[name] = new_agent
                 self.current_agent = self.agent_sessions[name]
                 self.current_agent.login()
            elif agent_type == self.agent_constants.TYPE_SSH:
                new_agent = SshAgent(device)
                self.agent_sessions[name] = new_agent
                self.current_agent = self.agent_sessions[name]
                self.current_agent.login()
            elif agent_type == self.agent_constants.TYPE_SERIAL:
                new_agent = SerialAgent(device)
                self.agent_sessions[name] = new_agent
                self.current_agent = self.agent_sessions[name]
                self.current_agent.login()
            elif agent_type == self.agent_constants.TYPE_XMC_REST:
                new_agent = XmcAgent(device)
                self.agent_sessions[name] = new_agent
                self.current_agent = self.agent_sessions[name]
                self.current_agent.login()
            elif agent_type == self.agent_constants.TYPE_JSON_RPC:
                new_agent = JsonRpcAgent(device)
                self.agent_sessions[name] = new_agent
                self.current_agent = self.agent_sessions[name]
                self.current_agent.login()
            elif agent_type == self.agent_constants.TYPE_CONSOLE:
                new_agent = ConsoleAgent(device)
                self.agent_sessions[name] = new_agent
                self.current_agent = self.agent_sessions[name]
                self.current_agent.login()
        else:
            self.current_agent = self.agent_sessions[name]  # get the connect based on the name

        logger.info("[+] NetworkElement:: self.current_agent            : %s", self.current_agent)
        logger.info("[+] NetworkElement:: new agent                      : %s", new_agent)
        logger.info("[+] NetworkElement:: session                       : %s", name)
        logger.info("[+] NetworkElement:: self.agent_sessions[name] : %s", self.agent_sessions[name])

######################################################################################

    def init_current_agent(self, login=True, agent_type=None):
        """
        Function Args:
        [login] - A boolean that dictates whether we attempt to login with the current agent.
        [agent_type] - The type of agent we should initialize. If none is provided the value in self.connection_method
                       will be used.

        Initializes the given agent and attempts to log in if login=True.
        """
        if agent_type is None:
            agent_type = self.connection_method

        if self.current_agent is None:
            if agent_type in self.agent_dict:
                self.logger.log_debug("Initializing current agent with type " + agent_type)
                self.logger.log_debug("    Username: " + self.username)
                self.logger.log_debug("    Password: " + self.password)
                self.logger.log_debug("    Login Prompt: " + self.login_prompt)
                self.logger.log_debug("    Password Prompt: " + self.pass_prompt)
                self.logger.log_debug("    Main Prompt: " + self.main_prompt)
                self.logger.log_debug("    Hostname: " + self.hostname)
                self.logger.log_debug("    Port: " + str(self.port))

                self.current_agent = self.agent_dict[agent_type](self)

                if self.eol is not None:
                    try:
                        self.current_agent.eol = self.eol
                    except AttributeError:
                        pass  # Current agent does not have an eol attribute.
            else:
                raise ValueError(agent_type + " is not a valid agent type for NetworkElements.")

        if self.prompt_handler is None:
            self.prompt_handler = PromptFactory().get_api(self)

        if login:
            return self.login()

        # We didn't try to log in, so the agent is not logged in, return False.
        return False

    def reload_apis(self):
        """
        Reloads API factory and prompt factory with the latest network element data.
        """
        self.apis = {}
        self.parse_apis = {}
        self.error_checker = ErrorCheckerFactory().get_api(self)
        self.prompt_handler = PromptFactory().get_api(self)
        self.inspection_toolkit = InspectionToolkit(self)

    def connect(self, *args):
        """
        Attempt to connect to the device using the current agent, if a current agent is set.
        """
        if not self.current_agent.connected:
            self.logger.log_debug("Agent is not connected. Attempting to connect...")
            self.current_agent.connect()
            if not self.current_agent.logged_in:
                self.logger.log_debug("Agent is not logged in. Attempting to log in...")
                logged_in = self.login()
                if not logged_in:
                    self.disconnect()

    def disconnect(self):
        """
        Disconnects from the current agent, if a current agent has been set.
        """
        if self.current_agent is not None:
            self.current_agent.disconnect()

    def login(self):
        """
        Attempts to log into the current agent using its login function.
        """
        retries = 0
        logged_in = False
        while not logged_in and retries < self.max_connection_retries:
            retries += 1
            try:
                logged_in = self.current_agent.login()
                if not logged_in:
                    self.logger.log_debug("Connection failed, retry attempt " + str(retries))
            except (EOFError, socket.error):
                logged_in = False
                self.current_agent.connected = False
                self.logger.log_debug("Connection failed, retry attempt " + str(retries))

        return logged_in

    def send_command(self, cmd):
        """
        This function calls the send command function of the current agent.
        """
        self.current_agent.send_command(cmd)

    def send_command_object(self, cmd_obj, **kwargs):
        """
        This function calls the send_command_object function of the current agent.
        """
        return self.current_agent.send_command_object(cmd_obj, **kwargs)

    def get_base_attrs(self):
        """
        This function creates the base_attrs list which is needed for the API factories. It first tries
        to find a matching PLATFORM_<OS>_BASE in the NetworkElementConstants. If it is unable
        to find a match PLATFORM_BASE is used instead.
        """
        try:
            base_attrs = [getattr(NetworkElementConstants, "PLATFORM_" + self.oper_sys + "_BASE"),
                          NetworkElementConstants.VERSION_BASE,
                          NetworkElementConstants.UNIT_BASE
                          ]
        except AttributeError:
            base_attrs = [NetworkElementConstants.PLATFORM_BASE,
                          NetworkElementConstants.VERSION_BASE,
                          NetworkElementConstants.UNIT_BASE
                          ]

        return base_attrs
