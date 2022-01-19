from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.elements.connect.configuration.ConnectConfigWebElements import ConnectConfigWebElements


class XIQSE_ConnectConfiguration(ConnectConfigWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()

    def xiqse_connect_configuration_select_tab(self, tab_name):
        """
         - This keyword selects the specified tab of the Connect> Configuration page
         - Keyword Usage
          - ``XIQSE Connect Configuration Select Tab    Services``
          - ``XIQSE Connect Configuration Select Tab    Options``

        :param tab_name: name of the sub tab to select
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        # These tabs are within an iframe, so switch to the iframe
        self.utils.switch_to_iframe(self.auto_actions.driver)

        if tab_name == "Services":
            the_tab = self.get_services_tab()
        elif tab_name == "Options":
            the_tab = self.get_options_tab()
        else:
            the_tab = None
        if the_tab:
            self.utils.print_info(f"Selecting '{tab_name}' tab on Connect> Configuration page")
            self.auto_actions.click(the_tab)
            ret_val = 1
            sleep(2)
        else:
            self.utils.print_info(f"Unable to select tab with name '{tab_name}' on Connect> Configuration page")
            self.screen.save_screen_shot()

        # Switch out of the iframe
        self.utils.switch_to_default(self.auto_actions.driver)

        return ret_val

    def xiqse_connect_configuration_select_services_tab(self):
        """
         - This keyword selects the Services tab on the Connect> Configuration Tab
         - Keyword Usage
          - ``XIQSE Connect Configuration Select Services Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_connect_configuration_select_tab("Services")

    def xiqse_connect_configuration_select_options_tab(self):
        """
         - This keyword selects the Options tab on the Connect> Configuration Tab
         - Keyword Usage
          - ``XIQSE Connect Configuration Select Options Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_connect_configuration_select_tab("Options")
