import os
import socket
from ExtremeAutomation.Library.Device.Common.Agents.SshAgent import SshAgent
from ExtremeAutomation.Library.Device.Common.Agents.RestAgent import RestAgent
from ExtremeAutomation.Library.Device.Common.Factories.PromptFactory import PromptFactory
from ExtremeAutomation.Library.Device.Common.ManagedDeviceObject import ManagedDeviceObject
from ExtremeAutomation.Library.Device.EndsystemElement.Constants.EndsystemElementConstants import \
    EndsystemElementConstants
from ExtremeAutomation.Library.Device.VirtualEnvironment.Constants.VirtualConstants import VirtualConstants
from ExtremeAutomation.Library.Device.VirtualEnvironment.VirtualEnvironmentFactory import VirtualMachineFactory
from ExtremeAutomation.Library.Logger.Logger import Logger


class VirtualMachineDevice(ManagedDeviceObject):
    def __init__(self, vm_type, ip_address, port, username, password, vm_api_version=VirtualConstants.BASE_VIRTUAL_API,
                 vm_unit=VirtualConstants.UNIT_BASE, vm_version=VirtualConstants.VERSION_BASE):
        ManagedDeviceObject.__init__(self)
        self.api_factory = VirtualMachineFactory()
        self.hostname = ip_address
        self.port = port
        self.platform = vm_api_version
        self.unit = vm_unit
        self.version = vm_version
        self.vm_type = vm_type
        self.username = username
        self.password = password
        self.image_id = None
        self.instance_id = None
        self.current_agent = None
        self.connection_method = None
        self.login_prompt = ""
        self.pass_prompt = ""
        self.main_prompt = ""
        self.end_of_line = b'\n'
        self.logger = Logger()
        self.STATUS_PREFIX = vm_type + " Status: "

        # Valid agents for VM Servers.
        self.agent_dict = {self.agent_constants.TYPE_SSH: SshAgent,
                           self.agent_constants.TYPE_REST: RestAgent}

    def init_current_agent(self, login=True, agent_type=None):
        """
        Function Args:
        [login] - A boolean that dictates whether we attempt to login with the current agent.
        [agent_type] - The type of agent we should initialize. If none is provided the value in self.connection_method
                       will be used.

        Initializes the given agent and attempts to log in if login=True.
        """
        if agent_type is None and self.connection_method is None:
            # TODO: Remove once deprecated 'Connect to Vm' is removed.
            agent_type = self.agent_constants.TYPE_REST
        elif agent_type is None:
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

                if self.end_of_line is not None:
                    try:
                        self.current_agent.eol = self.end_of_line
                    except AttributeError:
                        pass  # Current agent does not have an eol attribute.
            else:
                raise ValueError(agent_type + " is not a valid agent type for Virtual Machines.")

        if self.prompt_handler is None:
            self.prompt_handler = PromptFactory().get_api(self)

        if login:
            return self.login()

        # We didn't try to log in, so the agent is not logged in, return False.
        return False

    def connect(self, arg_list):
        """
        Virtual Machine control does not need to connect.
        This function logs the connection information.
        """
        self.logger.log_info(arg_list)

    def get_path(self, api_name):
        """
        Gets the API path for the given API name.
        """
        if self.connection_method == "ssh":
            agent = "CLI"
        else:
            agent = "REST"
        return "Apis" + os.path.sep + agent + os.path.sep + self.vm_type + \
               os.path.sep + api_name + \
               os.path.sep + self.unit + \
               os.path.sep + self.version + \
               os.path.sep + "VirtualBaseApi.py"

    def disconnect(self, *args, **kwargs):
        """
        :return:
        """
        pass

    def login(self, *args, **kwargs):
        """
        :return:
        """
        retries = 0
        logged_in = False
        while not logged_in and retries < 3:
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

    def get_base_attrs(self):
        """
        This function creates the base_attrs list which is needed for the API factories. It first tries
        to find a matching PLATFORM_<OS>_BASE in the NetworkElementConstants. If it is unable
        to find a match PLATFORM_BASE is used instead.
        """
        try:
            base_attrs = [getattr(EndsystemElementConstants, "PLATFORM_" + self.oper_sys + "_BASE"),
                          EndsystemElementConstants.VERSION_BASE,
                          EndsystemElementConstants.UNIT_BASE
                          ]
        except AttributeError:
            base_attrs = [EndsystemElementConstants.PLATFORM_BASE,
                          EndsystemElementConstants.VERSION_BASE,
                          EndsystemElementConstants.UNIT_BASE
                          ]

        return base_attrs
