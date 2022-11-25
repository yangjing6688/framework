from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.elements.wireless.threats.WirelessThreatsWebElements import WirelessThreatsWebElements


class XIQSE_WirelessThreats(WirelessThreatsWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()

    def xiqse_wireless_threats_select_tab(self, tab_name):
        """
        - This keyword selects the specified tab of the Wireless> Threats page
        - Keyword Usage
        - ``XIQSE Wireless Threats Select Tab    Threats``
        - ``XIQSE Wireless Threats Select Tab    Threat Events``
        - ``XIQSE Wireless Threats Select Tab    Interference``
        - ``XIQSE Wireless Threats Select Tab    Interference Events``

        :param tab_name: name of the sub tab to select
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        if tab_name == "Threats":
            the_tab = self.get_threats_tab()
        elif tab_name == "Threat Events":
            the_tab = self.get_threat_events_tab()
        elif tab_name == "Interference":
            the_tab = self.get_interference_tab()
        elif tab_name == "Interference Events":
            the_tab = self.get_interference_events_tab()
        else:
            the_tab = None
        if the_tab:
            self.utils.print_info(f"Selecting '{tab_name}' tab on Wireless> Threats page")
            self.auto_actions.click(the_tab)
            ret_val = 1
            sleep(2)
        else:
            self.utils.print_info(f"Unable to select tab with name '{tab_name}' on Wireless> Threats page")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_wireless_threats_select_threats_tab(self):
        """
        - This keyword selects the Threats tab on the Wireless> Threats Tab
        - Keyword Usage
        - ``XIQSE Wireless Threats Select Threats Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_wireless_threats_select_tab("Threats")

    def xiqse_wireless_threats_select_threat_events_tab(self):
        """
        - This keyword selects the Threat Events tab on the Wireless> Threats Tab
        - Keyword Usage
        - ``XIQSE Wireless Threats Select Threat Events Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_wireless_threats_select_tab("Threat Events")

    def xiqse_wireless_threats_select_interference_tab(self):
        """
        - This keyword selects the Interference tab on the Wireless> Threats Tab
        - Keyword Usage
        - ``XIQSE Wireless Threats Select Interference Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_wireless_threats_select_tab("Interference")

    def xiqse_wireless_threats_select_interference_events_tab(self):
        """
        - This keyword selects the Interference Events tab on the Wireless> Threats Tab
        - Keyword Usage
        - ``XIQSE Wireless Threats Select Interference Events Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_wireless_threats_select_tab("Interference Events")
