from ExtremeAutomation.Library.Logger.Logger import Logger
from ExtremeAutomation.Library.Device.Common.Agents.BaseSeleniumAgent import BaseSeleniumAgent
from ExtremeAutomation.Library.Device.Common.Agents.SeleniumAgent import SeleniumAgent
from ExtremeAutomation.Library.Device.Common.Agents.ExtjsSeleniumAgent import ExtjsSeleniumAgent
from ExtremeAutomation.Library.Device.Common.ManagedDeviceObject import ManagedDeviceObject
from ExtremeAutomation.Library.Device.UiElement.Constants.UiElementConstants import UiElementConstants
from ExtremeAutomation.Library.Device.Common.Factories.UiElementCommandApiFactory import UiElementCommandApiFactory


class UiElement(ManagedDeviceObject):
    def __init__(self, application, app_version):
        super(UiElement, self).__init__()
        self.current_agent = None
        self.hostname = ""
        self.port = ""
        self.connection_method = ""
        self.application = application
        self.oper_sys = self.application
        self.app_version = app_version
        self.max_connection_retries = 3
        self.logger = Logger()
        self.constants = UiElementConstants()
        self.api_factory = UiElementCommandApiFactory()
        self.element_data = None

        # Valid agents for UI elements.
        self.agent_dict = {self.agent_constants.TYPE_SELENIUM: SeleniumAgent,
                           self.agent_constants.TYPE_EXT_SELENIUM: ExtjsSeleniumAgent,
                           self.agent_constants.TYPE_BASE_SELENIUM: BaseSeleniumAgent}

    def init_current_agent(self, agent_type=None):
        """
        This function initializes whichever agent is assigned to the UI element device.
        If it is a supported agent it creates an instance of that agent otherwise a
        ValueError is raised.
        """
        if agent_type is None:
            agent_type = self.connection_method

        if self.current_agent is None:
            if agent_type in self.agent_dict:
                self.current_agent = self.agent_dict[agent_type](self)
                return True
            else:
                raise ValueError(agent_type + " is not a valid agent type for UI elements.")
        return self.check_current_agent(agent_type)

    def check_current_agent(self, agent_type):
        """
        This function checks to make sure the current agent matches the passed <agent_type>.
        If the agent_type is a known good agent type it attempts the comparison and returns the
        result, if the agent_type is unknown False is returned.
        """
        if agent_type == self.agent_constants.TYPE_SELENIUM:
            return isinstance(self.current_agent, SeleniumAgent)
        elif agent_type == self.agent_constants.TYPE_EXT_SELENIUM:
            return isinstance(self.current_agent, ExtjsSeleniumAgent)
        elif agent_type == self.agent_constants.TYPE_BASE_SELENIUM:
            return isinstance(self.current_agent, BaseSeleniumAgent)
        else:
            return False

    def send_command_object(self, command, **kwargs):
        """
        This function calls the send_command_object function of the current agent.
        """
        return self.current_agent.send_command_object(command, **kwargs)

    def get_base_attrs(self):
        """
        This function returns a list of base attributes. The API factory needs this information
        in order to know what to grab if it can't find a match based on the devices attributes.
        """
        base_attrs = [self.constants.APP_VER_BASE]

        return base_attrs

    def connect(self, *args, **kwargs):
        """
        Function required because of abstract parent class. Not needed for UI elements.
        """
        pass

    def disconnect(self):
        """
        This function calls the disconnect method of the current agent.
        """
        if self.current_agent:
            self.logger.log_debug("Disconnecting...")
            self.current_agent.disconnect()

    def login(self):
        """
        Function required because of abstract parent class. Not needed for UI elements.
        """
        pass
