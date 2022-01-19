from time import sleep
from common.Utils import Utils
from common.Screen import Screen
from common.AutoActions import AutoActions
from xiqse.elements.network.devices.NetworkDevicesWebElements import NetworkDevicesWebElements


class XIQSE_NetworkDevices(NetworkDevicesWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()

    def xiqse_devices_select_tab(self, tab_name, site="World"):
        """
         - This keyword selects the specified tab of the Network> Devices page
         - Keyword Usage
          - ``XIQSE Devices Select Tab    Devices``
          - ``XIQSE Devices Select Tab    Site Summary``
          - ``XIQSE Devices Select Tab    Endpoint Locations``
          - ``XIQSE Devices Select Tab    FlexReports``

        :param tab_name: name of the sub tab to select
        :param site:     name of site tab to select, if tab to select is Site (it changes name based on tree selection)
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        if tab_name == "Devices":
            the_tab = self.get_devices_tab()
        elif tab_name == "Site":
            the_tab = self.get_site_tab(site)
        elif tab_name == "Site Summary":
            the_tab = self.get_site_summary_tab()
        elif tab_name == "Endpoint Locations":
            the_tab = self.get_endpoint_locations_tab()
        elif tab_name == "FlexReports":
            the_tab = self.get_flexreports_tab()
        else:
            the_tab = None
        if the_tab:
            if tab_name == "Site":
                self.utils.print_info(f"Selecting '{site}' tab on Network> Devices page")
            else:
                self.utils.print_info(f"Selecting '{tab_name}' tab on Network> Devices page")
            self.auto_actions.click(the_tab)
            ret_val = 1
            sleep(2)
        else:
            if tab_name == "Site":
                self.utils.print_info(f"Unable to select tab with name '{site}' on Network> Devices page")
            else:
                self.utils.print_info(f"Unable to select tab with name '{tab_name}' on Network> Devices page")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_devices_select_devices_tab(self):
        """
         - This keyword selects the Devices tab on the Network> Devices Tab
         - Keyword Usage
          - ``XIQSE Devices Select Devices Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_devices_select_tab("Devices")

    def xiqse_devices_select_site_tab(self, site="World"):
        """
         - This keyword selects the specified site tab on the Network> Devices Tab
         - Keyword Usage
          - ``XIQSE Devices Select Site Tab   ${SITE}``

        :param site: name of site tab to select (it changes name based on tree selection)
        :return: 1 if action was successful, else -1
        """

        return self.xiqse_devices_select_tab("Site", site)

    def xiqse_devices_select_site_summary_tab(self):
        """
         - This keyword selects the Site Summary tab on the Network> Devices Tab
         - Keyword Usage
          - ``XIQSE Devices Select Site Summary Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_devices_select_tab("Site Summary")

    def xiqse_devices_select_endpoint_locations_tab(self):
        """
         - This keyword selects the Endpoint Locations tab on the Network> Devices Tab
         - Keyword Usage
          - ``XIQSE Devices Select Endpoint Locations Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_devices_select_tab("Endpoint Locations")

    def xiqse_devices_select_flexreports_tab(self):
        """
         - This keyword selects the FlexReports tab on the Network> Devices Tab
         - Keyword Usage
          - ``XIQSE Devices Select FlexReports Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_devices_select_tab("FlexReports")
