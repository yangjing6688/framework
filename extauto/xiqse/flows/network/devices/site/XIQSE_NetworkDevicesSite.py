from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.elements.network.devices.site.NetworkDevicesSiteWebElements import NetworkDevicesSiteWebElements
from xiqse.flows.network.devices.site.discover.XIQSE_NetworkDevicesSiteDiscover import XIQSE_NetworkDevicesSiteDiscover
from xiqse.flows.network.devices.site.actions.XIQSE_NetworkDevicesSiteActions import XIQSE_NetworkDevicesSiteActions
from xiqse.flows.common.XIQSE_CommonOperationsPanel import XIQSE_CommonOperationsPanel


class XIQSE_NetworkDevicesSite(NetworkDevicesSiteWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.site_discover = XIQSE_NetworkDevicesSiteDiscover()
        self.site_actions = XIQSE_NetworkDevicesSiteActions()
        self.operations_panel = XIQSE_CommonOperationsPanel()

    def xiqse_site_select_tab(self, tab_name):
        """
         - This keyword selects the specified tab of the Network> Devices> Site page
         - Keyword Usage
          - ``XIQSE Site Select Tab    Discover``
          - ``XIQSE Site Select Tab    Actions``
          - ``XIQSE Site Select Tab    VRF/VLAN``
          - ``XIQSE Site Select Tab    Topologies``
          - ``XIQSE Site Select Tab    Services``
          - ``XIQSE Site Select Tab    Port Templates``
          - ``XIQSE Site Select Tab    ZTP+ Device Defaults``
          - ``XIQSE Site Select Tab    Endpoint Locations``
          - ``XIQSE Site Select Tab    Analytics``
          - ``XIQSE Site Select Tab    Custom Variables``

        :param tab_name: name of the sub tab to select
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        if tab_name == "Discover":
            the_tab = self.get_discover_tab()
        elif tab_name == "Actions":
            the_tab = self.get_actions_tab()
        elif tab_name == "VRF/VLAN":
            the_tab = self.get_vrf_vlan_tab()
        elif tab_name == "Topologies":
            the_tab = self.get_topologies_tab()
        elif tab_name == "Services":
            the_tab = self.get_services_tab()
        elif tab_name == "Port Templates":
            the_tab = self.get_port_templates_tab()
        elif tab_name == "ZTP+ Device Defaults":
            the_tab = self.get_ztp_device_defaults_tab()
        elif tab_name == "Endpoint Locations":
            the_tab = self.get_endpoint_locations_tab()
        elif tab_name == "Analytics":
            the_tab = self.get_analytics_tab()
        elif tab_name == "Custom Variables":
            the_tab = self.get_custom_variables_tab()
        else:
            the_tab = None
        if the_tab:
            self.utils.print_info(f"Selecting '{tab_name}' tab on Network> Devices> Site page")
            self.auto_actions.click(the_tab)
            ret_val = 1
            sleep(2)
        else:
            self.utils.print_info(f"Unable to select tab with name '{tab_name}' on Network> Devices> Site page")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_site_select_discover_tab(self):
        """
         - This keyword selects the Discover tab on the Network> Devices> Site Tab
         - It is assumed the view is already navigated to the Site tab.
         - Keyword Usage
          - ``XIQSE Site Select Discover Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_site_select_tab("Discover")

    def xiqse_site_select_actions_tab(self):
        """
         - This keyword selects the Actions tab on the Network> Devices> Site Tab
         - It is assumed the view is already navigated to the Site tab.
         - Keyword Usage
          - ``XIQSE Site Select Actions Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_site_select_tab("Actions")

    def xiqse_site_select_vrf_vlan_tab(self):
        """
         - This keyword selects the VRF/VLAN tab on the Network> Devices> Site Tab
         - It is assumed the view is already navigated to the Site tab.
         - Keyword Usage
          - ``XIQSE Site Select VRF/VLAN Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_site_select_tab("VRF/VLAN")

    def xiqse_site_select_topologies_tab(self):
        """
         - This keyword selects the Topologies tab on the Network> Devices> Site Tab
         - It is assumed the view is already navigated to the Site tab.
         - Keyword Usage
          - ``XIQSE Site Select Topologies Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_site_select_tab("Topologies")

    def xiqse_site_select_services_tab(self):
        """
         - This keyword selects the Services tab on the Network> Devices> Site Tab
         - It is assumed the view is already navigated to the Site tab.
         - Keyword Usage
          - ``XIQSE Site Select Services Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_site_select_tab("Services")

    def xiqse_site_select_port_templates_tab(self):
        """
         - This keyword selects the Port Templates tab on the Network> Devices> Site Tab
         - It is assumed the view is already navigated to the Site tab.
         - Keyword Usage
          - ``XIQSE Site Select Port Templates Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_site_select_tab("Port Templates")

    def xiqse_site_select_ztp_device_defaults_tab(self):
        """
         - This keyword selects the ZTP+ Device Defaults tab on the Network> Devices> Site Tab
         - It is assumed the view is already navigated to the Site tab.
         - Keyword Usage
          - ``XIQSE Site Select ZTP Device Defaults Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_site_select_tab("ZTP+ Device Defaults")

    def xiqse_site_select_endpoint_locations_tab(self):
        """
         - This keyword selects the Endpoint Locations tab on the Network> Devices> Site Tab
         - It is assumed the view is already navigated to the Site tab.
         - Keyword Usage
          - ``XIQSE Site Select Endpoint Locations Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_site_select_tab("Endpoint Locations")

    def xiqse_site_select_analytics_tab(self):
        """
         - This keyword selects the Analytics tab on the Network> Devices> Site Tab
         - It is assumed the view is already navigated to the Site tab.
         - Keyword Usage
          - ``XIQSE Site Select Analytics Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_site_select_tab("Analytics")

    def xiqse_site_select_custom_variables_tab(self):
        """
         - This keyword selects the Custom Variables tab on the Network> Devices> Site Tab
         - It is assumed the view is already navigated to the Site tab.
         - Keyword Usage
          - ``XIQSE Site Select Custom Variables Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_site_select_tab("Custom Variables")

    def xiqse_site_click_discover(self):
        """
         - This keyword clicks the Discover button on the Network> Devices> Site Tab
         - It is assumed the view is already navigated to the Site tab.
         - Keyword Usage
          - ``XIQSE Site Click Discover``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        the_button = self.get_discover_button()
        if the_button:
            self.utils.print_info("Clicking Discover Button")
            self.auto_actions.click(the_button)
            ret_val = 1
            sleep(2)
        else:
            self.utils.print_info("Unable to find the Discover button")
            self.screen.save_screen_shot()
        return ret_val

    def xiqse_site_click_save(self):
        """
         - This keyword clicks the Save button on the Network> Devices> Site Tab
         - It is assumed the view is already navigated to the Site tab.
         - Keyword Usage
          - ``XIQSE Site Click Save``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        the_button = self.get_save_button()
        if the_button:
            self.utils.print_info("Clicking Save Button")
            self.auto_actions.click(the_button)
            ret_val = 1
            sleep(2)
        else:
            self.utils.print_info("Unable to find the Save button")
            self.screen.save_screen_shot()
        return ret_val

    def xiqse_site_click_cancel(self):
        """
         - This keyword clicks the Cancel button on the Network> Devices> Site Tab
         - It is assumed the view is already navigated to the Site tab.
         - Keyword Usage
          - ``XIQSE Site Click Cancel``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        the_button = self.get_cancel_button()
        if the_button:
            self.utils.print_info("Clicking Cancel Button")
            self.auto_actions.click(the_button)
            ret_val = 1
            sleep(2)
        else:
            self.utils.print_info("Unable to find the Cancel button")
            self.screen.save_screen_shot()
        return ret_val

    def xiqse_site_perform_subnet_discovery(self, subnet_values, profile_names, auto_add="true", trap="false", syslog="false", archive="false"):
        """
         - This keyword configures and performs a subnet discovery.
         - It is assumed the view is already navigated to the Site tab.
         - Keyword Usage
          - ``XIQSE Site Perform Subnet Discovery  1.1.1.1/24  public_v1_Profile  true  true  true  true``
          - ``XIQSE Site Perform Subnet Discovery  1.1.1.1/24,2.2.2.1/24  public_v1_Profile,public_v2_Profile``

        :param subnet_values:  comma-separated list of subnet/mask values to use in the discovery
        :param profile_names:  comma-separated list of profile names to use in the discovery
        :param auto_add:       specifies value of Automatically Add Devices checkbox on the Actions tab  (true/false)
        :param trap:           specifies value of Add Trap Receiver checkbox on the Actions tab  (true/false)
        :param syslog:         specifies value of Add Syslog Receiver checkbox on the Actions tab  (true/false)
        :param archive:        specifies value of Add to Archive checkbox on the Actions tab  (true/false)
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        if self.xiqse_site_select_actions_tab():
            # Configure the Actions tab
            self.site_actions.xiqse_actions_set_automatically_add_devices(auto_add)
            self.site_actions.xiqse_actions_set_add_trap_receiver(trap)
            self.site_actions.xiqse_actions_set_add_syslog_receiver(syslog)
            self.site_actions.xiqse_actions_set_add_to_archive(archive)
            self.xiqse_site_click_save()

            # Configure the Discover tab
            if self.xiqse_site_select_discover_tab():
                error_occurred = False
                subnet_list = subnet_values.split(',')
                for subnet_mask in subnet_list:
                    if self.site_discover.xiqse_discover_addresses_add_subnet(subnet_mask) == -1:
                        error_occurred = True
                        break

                self.site_discover.xiqse_discover_clear_all_profile_selections()
                profile_list = profile_names.split(',')
                for profile in profile_list:
                    if self.site_discover.xiqse_discover_set_accept_profile(profile) == -1:
                        error_occurred = True
                        break

                # Perform the discovery
                if not error_occurred:
                    if self.xiqse_site_click_save() != -1:
                        ret_val = self.xiqse_site_click_discover()

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_site_perform_ip_range_discovery(self, ip_start, ip_end, profile_names, auto_add="true", trap="false", syslog="false", archive="false"):
        """
         - This keyword configures and performs an IP range discovery.
         - It is assumed the view is already navigated to the Site tab.
         - Keyword Usage
          - ``XIQSE Site Perform IP Range Discovery  1.1.1.1  1.1.1.5  public_v1_Profile  true  true  true  true``
          - ``XIQSE Site Perform IP Range Discovery  2.2.2.1  2.2.2.250  public_v1_Profile,public_v2_Profile''

        :param ip_start:       IP starting value to use in the discovery
        :param ip_end:         IP ending value to use in the discovery
        :param profile_names:  comma-separated list of profile names to use in the discovery
        :param auto_add:       specifies value of Automatically Add Devices checkbox on the Actions tab  (true/false)
        :param trap:           specifies value of Add Trap Receiver checkbox on the Actions tab  (true/false)
        :param syslog:         specifies value of Add Syslog Receiver checkbox on the Actions tab  (true/false)
        :param archive:        specifies value of Add to Archive checkbox on the Actions tab  (true/false)
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        if self.xiqse_site_select_actions_tab():
            # Configure the Actions tab
            self.site_actions.xiqse_actions_set_automatically_add_devices(auto_add)
            self.site_actions.xiqse_actions_set_add_trap_receiver(trap)
            self.site_actions.xiqse_actions_set_add_syslog_receiver(syslog)
            self.site_actions.xiqse_actions_set_add_to_archive(archive)
            self.xiqse_site_click_save()

            # Configure the Discover tab
            if self.xiqse_site_select_discover_tab():
                error_occurred = False
                if self.site_discover.xiqse_discover_addresses_add_address_range(ip_start, ip_end) == -1:
                    error_occurred = True

                self.site_discover.xiqse_discover_clear_all_profile_selections()
                profile_list = profile_names.split(',')
                for profile in profile_list:
                    if self.site_discover.xiqse_discover_set_accept_profile(profile) == -1:
                        error_occurred = True
                        break

                # Perform the discovery
                if not error_occurred:
                    if self.xiqse_site_click_save() != -1:
                        ret_val = self.xiqse_site_click_discover()

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_site_wait_until_discovery_complete(self, retry_duration=30, retry_count=10):
        """
         - This keyword waits until the discovery has completed by checking the Discover Site entry in the
         - Operations panel for progress value of 100%.
         - It is assumed the view is already navigated to the Site tab.
         - Keyword Usage
          - ``XIQSE Wait Until Discovery Complete``
          - ``XIQSE Wait Until Discovery Complete    retry_duration=10  retry_count=60``

        :param retry_duration: duration between each retry
        :param retry_count: retry count
        :return: 1 if action was successful, else -1
        """
        return self.operations_panel.xiqse_operations_wait_until_operation_complete("Discover Site",
                                                                                    retry_duration, retry_count)

    def xiqse_site_save_changes(self):
        """
         - This keyword saves the changes on the Site tab.
         - It is assumed the view is already navigated to the Site tab.
         - Keyword Usage
          - ``XIQSE Site Save Changes``

        :return: 1 if action was successful, else -1
        """
        return self.xiqse_site_click_save()

    def xiqse_site_cancel_changes(self):
        """
         - This keyword cancels the changes on the Site tab.
         - It is assumed the view is already navigated to the Site tab.
         - Keyword Usage
          - ``XIQSE Site Cancel Changes``

        :return: 1 if action was successful, else -1
        """
        return self.xiqse_site_click_cancel()

    def xiqse_site_unsaved_changes_dialog(self, the_answer="No"):
        """
         - This keyword clicks the Yes, No, or Cancel button in the 'Site - Unsaved Changes' dialog.
         - This panel is displayed when moving away from a site that has unsaved changes.
         - Keyword Usage
          - ``XIQSE Site Unsaved Changes Dialog    No``

        :param the_answer:  Specifies how to answer the question in the dialog - Yes, No, or Cancel
        :return: 1 if action was successful, 2 if dialog was not displayed, else -1
        """
        ret_val = -1

        save_dlg = self.get_site_unsaved_changes_dialog()
        if save_dlg:
            self.utils.print_info(f"'Site - Unsaved Changes' dialog was displayed; answer with '{the_answer}'")
            if the_answer.upper() == "NO":
                ret_val = self.xiqse_site_unsaved_changes_dialog_click_no()
            elif the_answer.upper() == "YES":
                ret_val = self.xiqse_site_unsaved_changes_dialog_click_yes()
            elif the_answer.upper() == "CANCEL":
                ret_val = self.xiqse_site_unsaved_changes_dialog_click_cancel()
            else:
                self.utils.print_info(f"Unknown 'Site - Unsaved Changes' answer '{the_answer}'")
        else:
            self.utils.print_info("'Site - Unsaved Changes' dialog was not displayed")
            ret_val = 2

        return ret_val

    def xiqse_site_unsaved_changes_dialog_click_yes(self):
        """
         - This keyword clicks 'Yes' in the 'Site - Unsaved Changes' dialog panel.
         - This panel is displayed when moving away from a site that has unsaved changes.
         - It is assumed the 'Site - Unsaved Changes' dialog panel is already open.
         - Keyword Usage
          - ``XIQSE Site Unsaved Changes Dialog Click Yes``

        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        the_btn = self.get_site_unsaved_changes_yes_button()
        if the_btn:
            self.utils.print_info("Clicking 'Yes'")
            self.auto_actions.click(the_btn)
        else:
            self.utils.print_info("Could not find 'Yes' button in the 'Site - Unsaved Changes' dialog")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val

    def xiqse_site_unsaved_changes_dialog_click_no(self):
        """
         - This keyword clicks 'No' in the 'Site - Unsaved Changes' dialog panel.
         - This panel is displayed when moving away from a site that has unsaved changes.
         - It is assumed the 'Site - Unsaved Changes' dialog panel is already open.
         - Keyword Usage
          - ``XIQSE Site Unsaved Changes Dialog Click No``

        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        the_btn = self.get_site_unsaved_changes_no_button()
        if the_btn:
            self.utils.print_info("Clicking 'No'")
            self.auto_actions.click(the_btn)
        else:
            self.utils.print_info("Could not find 'No' button in the 'Site - Unsaved Changes' dialog")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val

    def xiqse_site_unsaved_changes_dialog_click_cancel(self):
        """
         - This keyword clicks 'Cancel' in the 'Site - Unsaved Changes' dialog panel.
         - This panel is displayed when moving away from a site that has unsaved changes.
         - It is assumed the 'Site - Unsaved Changes' dialog panel is already open.
         - Keyword Usage
          - ``XIQSE Site Unsaved Changes Dialog Click Cancel``

        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        the_btn = self.get_site_unsaved_changes_cancel_button()
        if the_btn:
            self.utils.print_info("Clicking 'Cancel'")
            self.auto_actions.click(the_btn)
        else:
            self.utils.print_info("Could not find 'Cancel' button in the 'Site - Unsaved Changes' dialog")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val
