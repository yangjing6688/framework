from ExtremeAutomation.Library.Device.UiElement.UiElement import UiElement
from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass


class UiElementConnectionManager(UiKeywordBaseClass):
    def connect_to_ui_element(self, element_name, remote_ip, agent, application, port=None, app_version=None,
                              remote=None, **kwargs):
        """Returns the UiElement device object after attempting to initialize and connect."""
        valid_agents = [getattr(self.constants, i) for i in dir(self.constants) if i.startswith("TYPE_")]
        valid_applications = [getattr(self.constants, i)
                              for i in dir(self.constants) if i.startswith("APP_") and not i.startswith("APP_VER_")]

        if agent not in valid_agents:
            raise ValueError(agent + " is not a valid agent type for UI elements.\n" + "Valid agents: " +
                             ",".join(valid_agents))
        if application.lower() not in valid_applications:
            raise ValueError(application + " is not a valid application for UI elements.\n" + "Valid applications: " +
                             ",".join(valid_applications))

        if app_version is None:
            app_version = self.constants.APP_VER_BASE

        ui_element = UiElement(application.upper(), app_version)
        ui_element.name = element_name
        ui_element.hostname = remote_ip
        ui_element.connection_method = agent
        ui_element.port = port
        ui_element.app_version = app_version
        ui_element.remote = remote

        self.set_agent_kwargs(ui_element, **kwargs)
        self.device_collection.add_device(element_name, ui_element)
        self._init_keyword(element_name, **kwargs)
        self._get_platform_variables(element_name)

        return ui_element

    def close_connection_to_ui_element(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The name of the UI element that robot should disconnect from.

        Closes the connection to a given UI element.
        """
        dev, _ = self._init_keyword(element_name, **kwargs)
        dev.disconnect()
        self.device_collection.remove_device(element_name)

    def set_agent_kwargs(self, device, **kwargs):
        """Returns the result of set_agent_kwargs."""
        self.add_agent_kwarg(device, "action_screen_shot", kwargs)
