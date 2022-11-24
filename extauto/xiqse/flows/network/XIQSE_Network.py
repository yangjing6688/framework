from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.elements.network.NetworkWebElements import NetworkWebElements


class XIQSE_Network(NetworkWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()

    def xiqse_network_select_tab(self, tab_name):
        """
        - This keyword selects the specified tab of the Network page
        - Keyword Usage
        - ``XIQSE Network Select Tab    Dashboard``
        - ``XIQSE Network Select Tab    Devices``
        - ``XIQSE Network Select Tab    Discovered``
        - ``XIQSE Network Select Tab    Firmware``
        - ``XIQSE Network Select Tab    Archives``
        - ``XIQSE Network Select Tab    Configuration Templates``
        - ``XIQSE Network Select Tab    Reports``

        :param tab_name: name of the sub tab to select
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        if tab_name == "Dashboard":
            the_tab = self.get_dashboard_tab()
        elif tab_name == "Devices":
            the_tab = self.get_devices_tab()
        elif tab_name == "Discovered":
            the_tab = self.get_discovered_tab()
        elif tab_name == "Firmware":
            the_tab = self.get_firmware_tab()
        elif tab_name == "Archives":
            the_tab = self.get_archives_tab()
        elif tab_name == "Configuration Templates":
            the_tab = self.get_configuration_templates_tab()
        elif tab_name == "Reports":
            the_tab = self.get_reports_tab()
        else:
            the_tab = None
        if the_tab:
            self.utils.print_info(f"Selecting '{tab_name}' tab on Network page")
            self.auto_actions.click(the_tab)
            ret_val = 1
            sleep(2)
        else:
            self.utils.print_info(f"Unable to select tab with name '{tab_name}' on Network page")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_network_select_dashboard_tab(self):
        """
        - This keyword selects the Dashboard tab of the Network page
        - Keyword Usage
        - ``XIQSE Network Select Dashboard Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_network_select_tab("Dashboard")

    def xiqse_network_select_devices_tab(self):
        """
        - This keyword selects the Devices tab of the Network page
        - Keyword Usage
        - ``XIQSE Network Select Devices Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_network_select_tab("Devices")

    def xiqse_network_select_discovered_tab(self):
        """
        - This keyword selects the Discovered tab of the Network page
        - Keyword Usage
        - ``XIQSE Network Select Discovered Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_network_select_tab("Discovered")

    def xiqse_network_select_firmware_tab(self):
        """
        - This keyword selects the Firmware tab of the Network page
        - Keyword Usage
        - ``XIQSE Network Select Firmware Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_network_select_tab("Firmware")

    def xiqse_network_select_archives_tab(self):
        """
        - This keyword selects the Archives tab of the Network page
        - Keyword Usage
        - ``XIQSE Network Select Archives Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_network_select_tab("Archives")

    def xiqse_network_select_configuration_templates_tab(self):
        """
        - This keyword selects the Configuration Templates tab of the Network page
        - Keyword Usage
        - ``XIQSE Network Select Configuration Templates Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_network_select_tab("Configuration Templates")

    def xiqse_network_select_reports_tab(self):
        """
        - This keyword selects the Reports tab of the Network page
        - Keyword Usage
        - ``XIQSE Network Select Reports Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_network_select_tab("Reports")
