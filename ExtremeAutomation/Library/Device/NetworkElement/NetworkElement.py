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
import sys

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logging.basicConfig(format='[%(asctime)s] %(levelname)s: [%(filename)s %(name)s %(funcName)s (Line#%(lineno)d)]: %(message)s')

class NetworkElement(ManagedDeviceObject):
    def __init__(self, oper_sys, platform, unit, version):
        super(NetworkElement, self).__init__()
        self.debug_password = ""
        self.oper_sys = oper_sys
        self.platform = platform
        self.unit = unit
        self.version = version
        self.login_prompt = []
        self.pass_prompt = []
        self.main_prompt = ''
        self.model = ""
        self.running_version = ""
        self.connection_method = ""
        self.last_connection_method = ""
        self.primary_connection = "console"
        self.current_agent = None
        self.session_key = None
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
                           self.agent_constants.TYPE_CONSOLE: ConsoleAgent,
                           self.agent_constants.TYPE_SLOT_1: ConsoleAgent,
                           self.agent_constants.TYPE_SLOT_2: ConsoleAgent}
        self.agent_track = {}

######################################################################################
    def track_named_agent(self, session_key, connection_method, hostname, port):
        logger.debug("[+]Current Agent Name: %s SessionKey: %s", self.agent_dict[connection_method], session_key)
        if connection_method in self.agent_track and session_key in self.agent_track[connection_method]:
            # already tracked/used.  Not need to add
            pass
        elif connection_method not in self.agent_track and (connection_method == 'console' or \
                connection_method == 'slot1'):
            self.add_tracked_named_agents(session_key, 'slot1', hostname, port)
            self.add_tracked_named_agents(session_key, 'console', hostname, port)
        elif connection_method in self.agent_track and (connection_method == 'console' or \
            connection_method == 'slot1' or connection_method == 'slot2') and \
                (hostname in self.agent_track and port in self.agent_track):
            logger.debug("[+]%s, %s only allows a single connection.  Reuse existing", connection_method, session_key)
            pass
        else:
            retVal = self.add_tracked_named_agents(session_key, connection_method, hostname, port)
            self.session_key = session_key
            # not in dict.  Add new session info

# #################################################################################
    def add_tracked_named_agents(self, session_key, connection_method, hostname, port):

        device = self
        if connection_method not in device.agent_track:
            device.agent_track[connection_method] = {}
            device.agent_track[connection_method][session_key] = {}
            device.agent_track[connection_method][session_key]['hostname'] = hostname
            device.agent_track[connection_method][session_key]['port'] = port
            device.agent_track[connection_method][session_key]['agent'] = self.current_agent
            return None
        elif session_key not in device.agent_track[connection_method]:
            device.agent_track[connection_method][session_key] = {}
            device.agent_track[connection_method][session_key]['hostname'] = hostname
            device.agent_track[connection_method][session_key]['port'] = port
            device.agent_track[connection_method][session_key]['agent'] = self.current_agent
            return None
        elif connection_method in device.agent_track and session_key in device.agent_track[connection_method]:
            logger.debug("[+] %s session_key %s exists            ", connection_method, session_key)
            # return the agent object
            return device.agent_track[connection_method][session_key]['agent']

    # #################################################################################
    def check_tracked_named_agents(self, session_key, connection_method, hostname, port):
        device = self

        if connection_method in device.agent_track and session_key in device.agent_track[connection_method]:
            device.session_key = session_key
            device.connection_method = connection_method
            device.hostname = hostname
            device.port = port
            return True
        elif connection_method in self.agent_track and (connection_method == 'console' or \
            connection_method == 'slot1') and \
                (hostname in self.agent_track and port in self.agent_track):
            if 'console' in self.agent_track and 'slot1' not in self.agent_track and connection_method == 'slot1':
                self.add_tracked_named_agents(session_key, 'slot1', hostname, port)
                self.agent_track['slot1'][session_key]['agent'] = self.agent_track['console']['default']['agent']
            elif 'slot1' in self.agent_track and 'console' not in self.agent_track and connection_method == 'console':
                self.add_tracked_named_agents(session_key, 'console', hostname, port)
                self.agent_track['console'][session_key]['agent'] = self.agent_track['slot1']['default']['agent']
            device.session_key = session_key
            device.connection_method = connection_method
            device.hostname = hostname
            device.port = port
            return True
        elif connection_method in self.agent_track and connection_method == 'slot2':
            device.session_key = session_key
            device.connection_method = connection_method
            device.hostname = hostname
            device.port = port
            return True
        else:
            return None

    # #################################################################################
    def remove_tracked_named_agent(self, session_key, connection_method, hostname, port):

        device = self
        try:
            device.agent_track[connection_method].pop(session_key, None)
            logger.debug("POP session_key %s", session_key)
        except:
            pass
        try:
            if len(device.agent_track[connection_method]) == 0:
                device.agent_track.pop(connection_method, None)
                logger.debug("POP connect meth %s", connection_method)
        except:
            logger.debug("POP error connect meth %s", connection_method)
            pass
        else:
            logger.debug("LEAVE connect meth %s", connection_method)

    def set_and_connect_named_agent(self, session_key, agent_type, hostname, port=None):

        """ Switch to new connection  """

        if port:
            self.port = port  # sets the device.port
        # If session_key not in agent_track,  create it, otherwise set the agent
        new_agent = None
        device = self
        if agent_type in device.agent_track and session_key in device.agent_track[agent_type]:
            self.current_agent = device.agent_track[agent_type][session_key]['agent']
            self.current_agent.login()
        else:
            if agent_type == self.agent_constants.TYPE_TELNET:
                try:
                    if self.port == 0:
                        self.port = self.agent_constants.TELNET_PORT
                except:
                    self.port = self.agent_constants.TELNET_PORT
                new_agent = TelnetAgent(device)
                self.current_agent = new_agent
                self.current_agent.login()
            elif agent_type == self.agent_constants.TYPE_REST:
                try:
                    if self.port == 0:
                        self.port = self.agent_constants.REST_PORT
                except:
                    self.port = self.agent_constants.REST_PORT
                new_agent = RestAgent(device)
                self.current_agent = new_agent
                self.current_agent.login()
            elif agent_type == self.agent_constants.TYPE_SNMP:
                try:
                    if self.port == 0:
                        self.port = self.agent_constants.REST_PORT
                except:
                    self.port = self.agent_constants.REST_PORT
                new_agent = SnmpAgent(device)
                self.current_agent = new_agent
                self.current_agent.login()
            elif agent_type == self.agent_constants.TYPE_SSH:
                try:
                    if self.port == 0:
                        self.port = self.agent_constants.SSH_PORT
                except:
                    self.port = self.agent_constants.SSH_PORT
                new_agent = SshAgent(device)
                self.current_agent = new_agent
                self.current_agent.login()
            elif agent_type == self.agent_constants.TYPE_SERIAL:
                new_agent = SerialAgent(device)
                self.current_agent = new_agent
                self.current_agent.login()
            elif agent_type == self.agent_constants.TYPE_XMC_REST:
                try:
                    if self.port == 0:
                        self.port = self.agent_constants.XMC_REST_PORT
                except:
                    self.port = self.agent_constants.XMC_REST_PORT
                new_agent = XmcAgent(device)
                self.current_agent = new_agent
                self.current_agent.login()
            elif agent_type == self.agent_constants.TYPE_JSON_RPC:
                new_agent = JsonRpcAgent(device)
                self.current_agent = new_agent
                self.current_agent.login()
            elif agent_type == self.agent_constants.TYPE_CONSOLE or agent_type == self.agent_constants.TYPE_SLOT_1:
                if not port:
                    port = self.port
                if self.check_tracked_named_agents(session_key, agent_type, hostname, port):
                    self.current_agent = device.agent_track[agent_type][session_key]['agent']
                    self.current_agent.login()
                else:
                    new_agent = ConsoleAgent(device)
                    self.current_agent = new_agent
                    self.current_agent.login()
            elif agent_type == self.agent_constants.TYPE_SLOT_2:
                if not port:
                    port = self.port
                if self.check_tracked_named_agents(session_key, agent_type, hostname, port):
                    self.current_agent = device.agent_track[agent_type][session_key]['agent']
                    self.current_agent.login()
                else:
                    new_agent = ConsoleAgent(device)
                    self.current_agent = new_agent
                    self.current_agent.login()
            self.track_named_agent(session_key, agent_type, hostname, self.port)


        logger.debug("[+] NetworkElement:: self.current_agent      : %s", self.current_agent)
        logger.debug("[+] NetworkElement:: new agent               : %s", new_agent)
        logger.debug("[+] NetworkElement:: session key             : %s", session_key)
        logger.debug("[+] NetworkElement:: device.agent_track[agent_type][session_key] : %s", device.__dict__['agent_track'])

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
                self.logger.log_debug("    Login Prompt: " + ",".join(self.login_prompt))
                self.logger.log_debug("    Password Prompt: " + ",".join(self.pass_prompt))
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
            self.logger.log_debug(f"Agent {self.current_agent.type} is not connected. Attempting to connect...")
            try:
                self.current_agent.connect()
                if not self.current_agent.logged_in:
                    self.logger.log_debug(f"Agent {self.current_agent.type} is not logged in. Attempting to log in...")
                    logged_in = self.login()
                    if not logged_in:
                        self.disconnect()
            except Exception as e:
                self.logger.log_error(f"Agent {self.current_agent.type} failed to connect or login: {e}")

    def disconnect(self):
        """
        Disconnects from the current agent, if a current agent has been set.
        """
        if self.current_agent is not None:
            self.logger.log_debug("Netelem Agent disconnect...")
            self.current_agent.disconnect()
            self.remove_tracked_named_agent(self.session_key, self.connection_method, self.hostname, self.port)

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
                if not logged_in and self.oper_sys == NetworkElementConstants.OS_AHAP and \
                        not self.current_agent.get_enable_default_password_mode():
                    self.current_agent.enable_default_password_mode(True)
                    logged_in = self.current_agent.login()
                    self.current_agent.enable_default_password_mode(False)
                if not logged_in:
                    self.logger.log_debug("Attempt Connection failed, retry attempt " + str(retries))
            except (EOFError, socket.error):
                logged_in = False
                self.current_agent.connected = False
                self.logger.log_debug("Error Connection failed, retry attempt " + str(retries))

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
        except AttributeError as e:
            base_attrs = [NetworkElementConstants.PLATFORM_BASE,
                          NetworkElementConstants.VERSION_BASE,
                          NetworkElementConstants.UNIT_BASE
                          ]

        return base_attrs
