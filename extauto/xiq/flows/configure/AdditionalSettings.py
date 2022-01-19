from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions

from xiq.flows.common.Navigator import Navigator
from xiq.flows.configure.NetworkPolicy import NetworkPolicy

from xiq.elements.AdditionalSettingsWebElements import AdditionalSettingsWebElements


class AdditionalSettings(AdditionalSettingsWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.navigator = Navigator()
        self.network_policy = NetworkPolicy()
        self.screen = Screen()

    def search_ntp_server_classification_entry(self, nw_policy, ntp_server_name):
        """
        - This keyword will check Single NTP server Classification Entry in Network Policy's NTP Server configuration page.
        - Flow: Configure --> Edit Network Policy->Additional Settings --> NTP Server
        - Keyword Usage
         - ``Search Ntp Server Classification Entry     ${NETWORK_POLICY_NAME}     ${NTP_SERVER_NAME}``

        :param nw_policy:  Network Policy Name to check ntp server classification entry
        :param ntp_server_name: NTP Server Name for classification entry
        :return: 1 if NTP server Classification Entry found on Network Policy else -1
        """
        self.navigator.navigate_to_devices()
        self.network_policy.navigate_to_np_edit_tab(nw_policy)
        sleep(2)

        self.utils.print_info("Click on network policy Additional Settings Tab")
        self.auto_actions.click(self.get_nw_policy_additional_settings_tab())

        self.utils.print_info("Click on NTP Server Tab")
        self.auto_actions.click(self.get_nw_policy_additional_settings_ntp_server_tab())
        sleep(2)

        self.auto_actions.scroll_down()
        self.screen.save_screen_shot()

        rows = self.get_ntp_server_classification_rule_grid_rows()
        for row in rows:
            if ntp_server_name in row.text:
                self.utils.print_info("Found NTP Server Classification Entry with Name: ", ntp_server_name)
                return 1
        return -1

    def search_ntp_server_classification_entries(self, nw_policy, *ntp_server_names):
        """
        - This keyword will check Multiple NTP server Classification Entries in Network Policy's NTP Server
          configuration page.
        - Flow: Configure --> Edit Network Policy->Additional Settings --> NTP Server
        - Keyword Usage
         - ``Search Ntp Server Classification Entry  ${NETWORK_POLICY_NAME}   ${NTP_SERVER_NAME}``
         - ``Search Ntp Server Classification Entry  ${NETWORK_POLICY_NAME}   ${NTP_SERVER_NAME}   ${NTP_SERVER_NAME2}``

        :param nw_policy:  Network Policy Name to check ntp server classification entry
        :param ntp_server_names: NTP Server Names for classification entry
        :return: 1 if NTP server Classification Entries found on Network Policy else -1
        """
        self.navigator.navigate_to_devices()
        self.network_policy.navigate_to_np_edit_tab(nw_policy)
        sleep(2)

        self.utils.print_info("Click on network policy Additional Settings Tab")
        self.auto_actions.click(self.get_nw_policy_additional_settings_tab())

        self.utils.print_info("Click on NTP Server Tab")
        self.auto_actions.click(self.get_nw_policy_additional_settings_ntp_server_tab())
        sleep(2)

        self.auto_actions.scroll_down()
        self.screen.save_screen_shot()

        ntp_flag = None
        for ntp_server_name in ntp_server_names:
            rows = self.get_ntp_server_classification_rule_grid_rows()
            for row in rows:
                if ntp_server_name in row.text:
                    self.utils.print_info("Found NTP Server Classification Entry with Name: ", ntp_server_name)
                    ntp_flag = True
                else:
                    self.utils.print_info(f"NTP Server Name {ntp_server_name} does't exists in the list")
                    ntp_flag = False

        if ntp_flag:
            return 1
        else:
            return -1

    def get_total_counts_of_ntp_server_classification_entry(self, nw_policy):
        """
        - This keyword will check Total counts of NTP server Classification Entry in Network Policy's NTP Server configuration page.
        - Flow: Configure --> Edit Network Policy->Additional Settings --> NTP Server
        - Keyword Usage
         - ``get total counts of ntp server classification entry     ${NETWORK_POLICY_NAME}``

        :param nw_policy:  Network Policy Name to check total ntp server classification entry
        :return: total number of rows if NTP server Classification Entry rows found on Network Policy else -1
        """
        self.navigator.navigate_to_devices()
        self.network_policy.navigate_to_np_edit_tab(nw_policy)
        sleep(2)

        self.utils.print_info("Click on network policy Additional Settings Tab")
        self.auto_actions.click(self.get_nw_policy_additional_settings_tab())

        self.utils.print_info("Click on NTP Server Tab")
        self.auto_actions.click(self.get_nw_policy_additional_settings_ntp_server_tab())
        sleep(10)

        self.auto_actions.scroll_down()
        self.screen.save_screen_shot()

        self.utils.print_info('Getting all NTP Server Classification Entries rows...')
        rows = self.get_ntp_server_classification_rule_grid_rows()

        if rows:
            ntp_count = len(rows) - 1
            self.utils.print_info("Total NTP Server Classification Entries on Network Policy is : ", ntp_count)
            return ntp_count
        else:
            self.utils.print_info("NTP Server Classification Entries Not Found on Network Policy")
            return -1
