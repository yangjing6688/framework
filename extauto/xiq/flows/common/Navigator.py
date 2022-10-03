from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.WebElementHandler import *
from extauto.common.AutoActions import AutoActions
from extauto.xiq.elements.NavigatorWebElements import NavigatorWebElements
from extauto.xiq.flows.common.DeviceCommon import DeviceCommon
from extauto.common.CommonValidation import CommonValidation

class Navigator(NavigatorWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.device_common = DeviceCommon()
        self.common_validation = CommonValidation()

    def navigate_to_manage_tab(self):
        """
         - This keyword Navigates to Manage Tab
         - Keyword Usage
          - ``Navigate To Manage Tab``

        :return: 1 if Navigation Successful to Monitor Tab else return -1
        """
        self.utils.print_info("Selecting Manage Tab...")
        if self.auto_actions.click_reference(self.get_manage_tab) == 1:
            sleep(2)
            if self.get_subtab_head_img_nav():
                self.utils.print_info("Subtab nav is already shown")
                return 1
            else:
                self.screen.save_screen_shot()
                self.utils.print_info("Even though already click manage tab, but can NOT go to subtab nav, stop NOT go to next step")
                return -1
        else:
            self.utils.print_info("Unable to navigate to Manage tab")
            self.screen.save_screen_shot()
            return -1

    def navigate_to_ml_insight_tab(self):
        """
         - This keyword Navigates to ML Insight tab
         - Keyword Usage
          - ``Navigate To ML Insight tab``

        :return: 1 if Navigation Successful to ML Insight tab else return -1
        """
        self.utils.print_info("Selecting ML Insight Tab....")
        if self.auto_actions.click_reference(self.get_ml_insight_tab) == 1:
            sleep(2)
            return 1
        else:
            self.utils.print_info("Unable to navigate to ML Insight tab")
            self.screen.save_screen_shot()
            return -1

    def navigate_to_configure_tab(self):
        """
         - This keyword Navigates to configure tab
         - Keyword Usage
          - ``Navigate To Configure tab``

        :return: 1 if Navigation Successful to configure tab else return -1
        """
        self.utils.print_info("Selecting Configure tab")
        if self.auto_actions.click_reference(self.get_configure_tab) == 1:
            sleep(2)
            return 1
        else:
            self.utils.print_info("Unable to navigate to Configure tab")
            self.screen.save_screen_shot()
            return -1

    def navigate_to_tools_sub_tab(self):
        """
         - This keyword Navigates to Tools Sub tab on Monitor Tab
         - Keyword Usage
          - ``Navigate To Tools Sub Tab``

        :return: 1 if Navigation Successful to Tools Sub tab on Monitor Tab else return -1
        """
        self.utils.print_info("Selecting Tools tab...")
        if self.auto_actions.click_reference(self.get_manage_tools_menu_item) == 1:
            sleep(2)
            return 1
        else:
            self.utils.print_info("Unable to navigate to Tools tab")
            self.screen.save_screen_shot()
            return -1

    def navigate_to_auto_provision(self):
        """
         - This keyword Navigates to Auto Provisioning on Common Objects
         - Flow Configure --> Common Objects --> Policy --> Auto Provisioning
         - Keyword Usage
          - ``Navigate To Auto Provision``

        :return: 1 if Navigation Successful
        """
        self.navigate_to_configure_tab()

        self.utils.print_info("Selecting Common Objects")
        self.auto_actions.click_reference(self.get_common_objects_sub_tab)
        sleep(2)

        if self.get_auto_provisioning_option() is None:
            self.utils.print_info("Auto Provisioning is Not visible. Clicking Policy...")
            self.auto_actions.click_reference(self.get_policy_toggle)
            sleep(2)

        self.utils.print_info("Auto Provision menu is visible. Selecting...")
        self.auto_actions.click_reference(self.get_auto_provisioning_option)
        sleep(2)

        return 1

    def navigate_to_devices(self, **kwargs):
        """
         - This keyword Navigates to Devices on Manage Menu
         - Flow Manage--> Devices
         - Keyword Usage
          - ``Navigate To Devices``

        :return: 1 if Navigation Successful to Devices Sub tab on Monitor Tab else return -1
        """
        if self.get_devices_page():
            self.utils.print_info("Already in Devices page")
            self.enable_page_size(page_size='100')
            return 1
        else:
            if self.navigate_to_manage_tab() == 1:
                self.utils.print_info("Manage page is present")
                if self.auto_actions.click(self.get_devices_nav()) == 1:
                    self.utils.print_info("Clicking Devices Tab...")
                    sleep(5)
                    self.enable_page_size(page_size='100')
                    return 1
                else:
                    self.utils.print_info("Unable to navigate to Devices tab")
                    self.screen.save_screen_shot()
                    return -1
            else:
                return -1

    def navigate_to_ssids(self):
        """
        - This keyword Navigates to SSIDs Menu on Common Objects
        - Flow Configure --> Common Objects --> Policy --> SSIDs
        - Keyword Usage
         - ``Navigate To SSIDs``

        :return: 1 if Navigation Successful
        """
        self.navigate_to_configure_tab()

        self.utils.print_info("Selecting Common Objects")
        self.auto_actions.click_reference(self.get_common_objects_sub_tab)
        sleep(2)

        if self.get_ssid_option() is None:
            self.utils.print_info("SSID menu is NOT visible. Clicking Policy...")
            self.auto_actions.click_reference(self.get_policy_toggle)
            sleep(2)
        self.utils.print_info("SSID menu is visible. Selecting...")
        self.auto_actions.click_reference(self.get_ssid_option)
        sleep(2)

        return 1

    def navigate_to_tools_page(self):
        """
        - This keyword Navigates to Tools Page on Monitor Menu
        - Flow MANAGE->Tools
        - Keyword Usage
         - ``Navigate To Tools Page``

        :return:  1 if Navigation Successful to Tools Sub tab on Monitor Tab else return -1
        """
        self.navigate_to_devices()
        self.navigate_to_device_utilities_tools()


    def navigate_configure_network_policies(self):
        """
         - This keyword Navigates to Network Policies On Configure Menu
         - Flow Configure--> Network Policies
         - Keyword Usage
          - ``Navigate Configure Network Policies``

        :return: 1 if Navigation Successful to Network Policies On Configure Menu else return -1
        """
        self.utils.print_info("Selecting Configure tab...")
        if self.get_configure_tab().is_displayed():
            self.navigate_to_configure_tab()
            sleep(2)
        else:
            return -2

        return self.navigate_to_network_policies_tab()

    def navigate_configure_common_objects(self):
        """
        - This keyword Navigates to Common Objects On Configure Menu
        - Flow: Configure --> Common Objects
        - Keyword Usage
         - ``Navigate Configure Common Objects``

        :return: -1 if Navigation Not Successful to Configure Menu else return None
        """
        self.navigate_to_configure_tab()

        self.utils.print_info("Selecting Common Objects")
        self.auto_actions.click_reference(self.get_common_objects_sub_tab)
        sleep(5)

    def navigate_to_network_policies_tab(self, **kwargs):
        """
         - This keyword Navigates to Network Policies
         - Keyword Usage
          - ``Navigate To Network Policies Tab``

        :return: 1 if Navigation Successful to Network Policies On Configure Menu else return -1
        """
        network_policy_tab_display = False
        try_cnt = 0
        while not network_policy_tab_display:
            self.utils.print_info("Navigate to Configure Tab first")
            self.navigate_to_configure_tab()
            if self.get_subtab_head_img_nav():
                self.utils.print_info("Selecting Network Policies Tab...")
                self.auto_actions.click(self.get_network_policies_sub_tab())
                sleep(2)
                network_policy_tab_display = True
            else:
                sleep(2)
                self.utils.print_info("Network Policy tab is NOT displayed, try to navigate to the tab again")
                self.screen.save_screen_shot()
                try_cnt += 1
                if try_cnt == 10:
                    self.utils.print_info(f"The MAX {try_cnt} times trying is reached, need figure out manually why the Network Policy tab can NOT be displayed")
                    return False
        if network_policy_tab_display:
            return 1
        else:
            return -1

    def navigate_to_clients_tab(self, **kwargs):
        """
         - This keyword Navigates to Client 360 Tab on Manage Menu
         - Keyword Usage
          - ``Navigate To Clients Tab``

        :return: 1 if Navigation Successful to Clients On Manage Menu else return -1
        """
        self.utils.print_info("Selecting Client 360 Tab...")
        if self.auto_actions.click_reference(self.get_clients_sub_tab) == 1:
            sleep(2)
            kwargs['pass_msg'] = "Navigated to Client 360 tab"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            self.utils.print_info("Unable to navigate to Client 360 tab")
            kwargs['fail_msg'] = "Unable to navigate to Client 360 tab"
            self.common_validation.failed(**kwargs)
            return -1

    def navigate_to_clients(self):
        """
        - This keyword Navigates to Clients On Manage Menu
        - Flow: Manage --> Client 360
        - Keyword Usage
         - ``Navigate To Clients``

        :return: 1 if Navigation Successful to Clients Tab on Monitor else return -1
        :return: -2 if Navigation Not Successful to Monitor Tab
        """
        if self.navigate_to_manage_tab() == 1:
            self.utils.print_info("Clicking Client 360 Tab...")
            if self.auto_actions.click_reference(self.get_clients_sub_tab) == 1:
                sleep(2)
                return 1
            else:
                self.utils.print_info("Unable to navigate to Client 360 tab")
                self.screen.save_screen_shot()
                return -1
        else:
            return -1

    def navigate_to_client_mode_profiles(self):
        """
        - This Keyword Navigate to Client Mode Profile on Common Objects
        - Flow: CONFIGURE-->COMMON OBJECTS-->Basic-->Client Mode Profiles
        - Keyword Usage:
         - ``Navigate To Client Mode Profiles``
        :return: 1 if Navigation Successful
        """
        self.navigate_configure_common_objects()
        self.utils.print_info("Click on Basic tab")
        self.navigate_to_common_object_basic_tab()
        self.utils.print_info("Click on Client Mode Profiles...")
        self.auto_actions.click_reference(self.get_common_object_basic_client_mode_profiles)
        return 1

    def navigate_to_user_account(self, **kwargs):
        """
        - This keyword Navigates to User Account Menu
        - Keyword Usage
         - ``Navigate To User Account``

        :return: 1 if Navigation Successful to User Account Menu else return -1
        """
        self.utils.print_info("Selecting user account...")
        if self.auto_actions.click_reference(self.get_user_account_nav) == 1:
            sleep(2)
            kwargs['pass_msg'] = "Navigated to user account"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            self.utils.print_info("Unable to navigate to user account")
            kwargs['fail_msg'] = "Failed: Unable to navigate to user account"
            self.common_validation.failed(**kwargs)
            return -1

    def _navigate_to_global_settings(self, **kwargs):
        """
        - This method is used to click on the global setting button
        """
        self.utils.print_info("Selecting global settings...")
        if self.auto_actions.click_reference(self.get_global_settings_nav) == 1:
            sleep(2)
            kwargs['pass_msg'] = "Navigated to global settings"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            self.utils.print_info("Unable to navigate to global settings")
            kwargs['fail_msg'] = "Unable to navigate to global settings"
            self.common_validation.passed(**kwargs)
            return -1

    def navigate_to_configure_user_sub_tab(self):
        """
        - This keyword Navigates to Global Settings on User Account Menu which is already Navigated
        - Keyword Usage
         - ``Navigate To Configure User Sub Tab``

        :return: 1 if Navigation Successful to Global Settings on User Account Menu else return -1
        """
        self.utils.print_info("Clicking on the Users Sub tab")
        if self.auto_actions.click_reference(self.get_configure_users_nav) == 1:
            sleep(2)
            return 1
        else:
            self.utils.print_info("Unable to navigate to the Configure Users sub tab")
            self.screen.save_screen_shot()
            return -1

    def navigate_to_global_settings_page(self):
        """
        - This keyword Navigates to Global Settings On User Account Menu
        - Flow: User Account Menu --> Global Settings
        - Keyword Usage
         - ``Navigate To Global Settings Page``

        :return: 1 if Navigation Successful to Clients Tab on Monitor else return -1
        :return: -2 if Navigation Not Successful to Monitor Tab
        """
        self.navigate_to_user_account()
        return self._navigate_to_global_settings()

    def navigate_to_configure_user_groups(self):
        """
        - This keyword Navigates to User Groups On Configure Menu
        - Flow: Configure --> Users --> User Management --> User Groups
        - Keyword Usage
         - ``Navigate To Configure User Groups``

        :return: 1 if Navigation Successful
        """
        self.navigate_to_configure_tab()
        self.navigate_to_configure_user_sub_tab()
        sleep(5)

        if self.get_configure_users_user_management_side_menu():
            self.auto_actions.click_reference(self.get_configure_users_user_management_side_menu)
            sleep(5)

        self.utils.print_info("Click on users group sub menu")
        self.auto_actions.click_reference(self.get_configure_user_group_side_nav_item)
        sleep(2)

        return 1

    def navigate_to_authentication_logs_menu(self):
        """
        - This keyword Navigate to the Authentication Logs Slider Menu
        - Flow: Authentication Logs
        - Keyword Usage
         - ``Navigate To Authentication Logs Menu``

        :return: 1 if Navigation Successful to Authentication Logs Slider Menu else return -1
        """
        self.utils.print_info("Selecting Authentication Logs...")

        if self.auto_actions.click_reference(self.get_global_settings_authentication_logs_slider) == 1:
            sleep(2)
            return 1
        else:
            self.utils.print_info("Unable to navigate to Authentication Logs")
            self.screen.save_screen_shot()
            return -1

    def navigate_to_accounting_logs_menu(self):
        """
        - This keyword Navigate to the Accounting Logs Slider Menu
        - Flow: Accounting Logs
        - Keyword Usage
         - ``Navigate To Accounting Logs Menu``

        :return: 1 if Navigation Successful to Accounting Logs Slider
        """
        self.utils.print_info("Selecting Accounting Logs...")
        if self.auto_actions.click_reference(self.get_global_settings_accounting_logs_slider) == 1:
            sleep(2)
            return 1
        else:
            self.utils.print_info("Unable to navigate to Accounting Logs")
            self.screen.save_screen_shot()
            return -1

    def navigate_to_authentication_logs(self):
        """
        - This keyword Navigate to the Authentication Logs Slider Menu
        - Flow: User account --> Global Settings --> LOGS--> Authentication Logs
        - Keyword Usage
         - ``Navigate To Authentication Logs Menu``

        :return: 1 if Navigation Successful to Authentication Logs Slider Menu else return -1
        """
        self.navigate_to_global_settings_page()
        self.navigate_to_authentication_logs_menu()

    def navigate_to_accounting_logs(self):
        """
        - This keyword Navigate to the Accounting Logs Slider Menu
        - Flow: User account --> Global Settings --> LOGS--> Accounting Logs
        - Keyword Usage
         - ``Navigate To Accounting Logs Menu``

        :return: 1 if Navigation Successful to Accounting Logs Slider else return -1
        """
        self.navigate_to_global_settings_page()
        self.navigate_to_accounting_logs_menu()

    def navigate_to_common_object_authentication_tab(self):
        """
        - This keyword Navigate to the Authentication Tab on common objects
        - Assumes that already navigated to the configure --> common object
        - Flow: Authentication
        - Keyword Usage
         - ``Navigate To Common Object Authentication Tab``

        :return: 1 if Navigation Successful
        """
        if not self.get_common_object_authentication_tab().is_selected():
            self.auto_actions.click_reference(self.get_common_object_authentication_tab)
            sleep(2)
            return 1

    def navigate_to_captive_web_portal(self):
        """
        - This keyword Navigate to the captive web portal tab on common objects
        - FLow: Configure --> Common Object --> Authentication --> Captive Web Portal
        - Keyword Usage
         - ``Navigate To Captive Web Portal``

        :return: 1 if Navigation Successful
        """
        self.navigate_configure_common_objects()
        self.utils.print_info("Click on common authentication tab")
        self.navigate_to_common_object_authentication_tab()
        self.utils.print_info("Click on captive web portal tab...")
        self.auto_actions.click_reference(self.get_common_object_authentication_captive_portal)
        sleep(5)

        return 1

    def navigate_to_aaa_server_settings(self):
        """
        - This Keyword Navigate to AAA server Settings on common objects
        - Flow: Configure --> Common Object --> Authentication --> AAA Server Settings
        - Keyword Usage
         - ``Navigate To AAA Server Settings``

        :return: 1 if Navigation Successful
        """
        self.navigate_configure_common_objects()
        self.utils.print_info("Click on common authentication tab")
        self.navigate_to_common_object_authentication_tab()
        self.utils.print_info("Click on AAA server Settings...")
        self.auto_actions.click_reference(self.get_common_object_authentication_aaa_server_settings)
        sleep(5)

        return 1

    def navigate_to_ad_servers(self):
        """
        - This Keyword Navigate to AD servers on common objects
        - Flow: Configure --> Common Object --> Authentication --> Ad Servers
        - Keyword Usage
         - ``Navigate To Ad Servers``

        :return: 1 if Navigation Successful
        """
        self.navigate_configure_common_objects()
        self.utils.print_info("Click on common authentication tab")
        self.navigate_to_common_object_authentication_tab()
        self.utils.print_info("Click on AAA server Settings...")
        self.auto_actions.click_reference(self.get_common_object_authentication_ad_servers)
        sleep(5)

        return 1

    def navigate_to_external_radius_server(self):
        """
        - This Keyword Navigate to External Radius Server on common objects
        - Flow: Configure --> Common Object --> Authentication --> External Radius Server
        - Keyword Usage
         - ``Navigate To External Radius Server``

        :return: 1 if Navigation Successful
        """
        self.navigate_configure_common_objects()
        self.utils.print_info("Click on common authentication tab")
        self.navigate_to_common_object_authentication_tab()
        self.utils.print_info("Click on  external radius server...")
        self.auto_actions.click_reference(self.get_common_object_authentication_external_radius_server)
        sleep(5)

        return 1

    def navigate_to_a3_menu(self):
        """
        - This Keyword Navigate to A3 menu
        - Keyword Usage
         - ``Navigate To A3 Menu``
        :return: 1 if Navigation Successful
        """
        self.utils.print_info("Clicking on A3 Icon")
        self.auto_actions.click_reference(self.get_a3_tab)
        sleep(2)
        return 1

    def navigate_to_extreme_networks_a3(self):
        """
        - This Keyword Navigate to Extreme Networks A3 on common objects
        - Flow: Configure --> Common Object --> Authentication --> Extreme Networks A3
        - Keyword Usage
         - ``Navigate To Extreme Networks A3``

        :return: 1 if Navigation Successful
        """
        self.navigate_configure_common_objects()
        self.utils.print_info("Click on common authentication tab")
        self.navigate_to_common_object_authentication_tab()
        self.utils.print_info("Click on External network A3...")
        self.auto_actions.click_reference(self.get_common_object_authentication_extreme_networks_a3)
        sleep(5)

        return 1

    def navigate_to_servers(self):
        """
        - This Keyword Navigate to Servers on common objects
        - Flow: Configure --> Common Object --> Authentication --> Servers
        - Keyword Usage
         - ``Navigate To Servers``

        :return: 1 if Navigation Successful
        """
        self.navigate_configure_common_objects()
        self.utils.print_info("Click on common authentication tab")
        self.navigate_to_common_object_authentication_tab()
        self.utils.print_info("Click on servers tab...")
        self.auto_actions.click_reference(self.get_common_object_authentication_servers)
        sleep(5)

        return 1

    def navigate_to_ldap_servers(self):
        """
        - This Keyword Navigate to LDAP Servers on common objects
        - Flow: Configure --> Common Object --> Authentication --> LDAP Servers
        - Keyword Usage
         - ``Navigate To Ldap Servers``

        :return: 1 if Navigation Successful
        """
        self.navigate_configure_common_objects()
        self.utils.print_info("Click on common authentication tab")
        self.navigate_to_common_object_authentication_tab()
        self.utils.print_info("Click on servers tab...")
        self.auto_actions.click_reference(self.get_common_object_authentication_ldap_servers)
        sleep(5)

        return 1

    def navigate_to_security_option(self):
        """
        - This Keyword Navigate to the Security option on Monitor Tab
        - Flow: Security
        - Keyword Usage
         - ``Navigate To Security Option``

        :return: 1 if Navigation Successful to Security tab on Monitor Menu else return -1
        """
        self.utils.print_info("Selecting Security on Monitor Page...")
        if self.auto_actions.click_reference(self.get_manage_security_nav) == 1:
            sleep(2)
            return 1
        else:
            self.utils.print_info("Unable to Security on Monitor Page")
            self.screen.save_screen_shot()
            return -1

    def navigate_manage_security(self):
        """
        - This Keyword Navigate to Manage --> Security
        - Flow: Manage--->Security
        - Keyword Usage
          - ``Navigate Manage Security``

        :return: 1 if Navigation Successful to Security tab on Monitor Menu else return -1
        """
        if self.navigate_to_manage_tab() == 1:
            return self.navigate_to_security_option()
        else:
            return -1

    def navigate_to_common_object_security_tab(self):
        """
        - This Keyword Navigate to Security Tab on Common Objects
        - Assumes that already navigated to the configure --> common object
        - Flow: Security
        - Keyword Usage
         - ``Navigate To Common Object Security Tab``

        :return: 1 if Navigation Successful to Security tab on common Objects else return -1
        :return:
        """
        if not self.get_common_object_security_tab().is_selected():
            self.auto_actions.click_reference(self.get_common_object_security_tab)
            sleep(2)

    def navigate_to_security_wips_policies(self):
        """
        - This Keyword Navigate to WIPS Policies on Common Objects
        - Flow: CONFIGURE-->COMMON OBJECTS-->SECURITY-->WIPS POLICIES
        - Keyword Usage:
         - ``Navigate To Security Wips Policies``

        :return: 1 if Navigation Successful
        """
        self.navigate_configure_common_objects()
        sleep(3)
        self.utils.print_info("Click on common Security tab")
        self.navigate_to_common_object_security_tab()
        self.utils.print_info("Click on WIPS Policies tab...")
        self.auto_actions.click_reference(self.get_common_object_security_wips_policies)
        sleep(5)

        return 1

    def navigate_to_common_object_policy_tab(self):
        """
        - This Keyword Navigate to Policies option Menu on Common Objects
        - Assumes that already navigated to the configure --> common object
        - Keyword Usage:
         - ``Navigate To Common Object Policy Tab``

        :return: 1 if Navigation Successful
        """

        if not self.get_subtab_common_object():
            self.auto_actions.click_reference(self.get_common_object_policy_tab)
            sleep(2)
            return 1

    def navigate_to_policy_ap_template(self):
        """
        - This Keyword Navigate to AP Templates on Common Objects
        - Flow: CONFIGURE-->COMMON OBJECTS-->AP Templates
        - Keyword Usage:
         - ``Navigate To Policy Ap Template``

        :return: 1 if Navigation Successful
        """
        self.navigate_configure_common_objects()
        sleep(3)
        self.utils.print_info("Click on common Policy tab")
        self.navigate_to_common_object_policy_tab()
        self.utils.print_info("Click on Ap Template tab...")
        self.auto_actions.click_reference(self.get_common_object_policy_ap_template)
        sleep(5)

        return 1

    def navigate_to_manage_reports(self):
        """
        - This Keyword Navigate to Reports on Manage Menu
        - Flow: Manage --> Reports
        - Keyword Usage:
         - ``Navigate To Manage Reports``

        :return: 1 if Navigation Successful
        """
        self.navigate_to_manage_tab()
        self.utils.print_info("Click on reports tab....")
        self.auto_actions.click_reference(self.get_manage_reports_nav)
        sleep(2)

        return 1

    def navigate_to_policy_port_types(self):
        """
        - This Keyword Navigate to Port Types On Common Objects
        - Flow: CONFIGURE-->COMMON OBJECTS-->POLICIES-->PORT TYPES
        - Keyword Usage:
         - ``Navigate To Policy Port Types``

        :return: 1 if Navigation Successful
        """
        self.navigate_configure_common_objects()
        sleep(3)
        self.utils.print_info("Click on common Policy tab")
        self.navigate_to_common_object_policy_tab()

        self.utils.print_info("Click on Port Types tab...")
        el = self.get_common_object_policy_port_types()
        if el is None:
            self.navigate_to_common_object_policy_tab()
            el = self.get_common_object_policy_port_types()

        self.auto_actions.click(el)
        sleep(5)

        return 1

    def navigate_to_common_object_network_tab(self):
        """
        - This Keyword Navigate to Network Tab On Common Objects
        - Assumes that already navigated to the configure --> common object
        - Flow: Networks
        - Keyword Usage:
          - ``Navigate To Common Object Network Tab``

        :return: 1 if Navigation Successful
        """
        if not self.get_common_object_network_tab().is_selected():
            self.auto_actions.click_reference(self.get_common_object_network_tab)
            sleep(2)
            return 1

    def navigate_to_network_subnetwork_space(self):
        """
        - This Keyword Navigate to SubNetwork Space Tab On Common Objects
        - Flow: CONFIGURE-->COMMON OBJECTS-->NETWORK-->Subnetwork Space
        - Keyword Usage:
         - ``Navigate To Network Subnetwork Space``

        :return: 1 if Navigation Successful
        """
        self.navigate_configure_common_objects()
        sleep(3)
        self.utils.print_info("Click on common object Network tab")
        self.navigate_to_common_object_network_tab()
        self.utils.print_info("Click on Subnetwork Space tab...")
        self.auto_actions.click_reference(self.get_common_object_network_sub_network_space)
        sleep(5)

        return 1

    def navigate_to_common_object_basic_tab(self):
        """
        - This Keyword Navigate to Basic Tab On Common Objects
        - Assumes that already navigated to the configure --> common object
        - Flow: Basic
        - Keyword Usage:
         - ``Navigate To Common Object Basic Tab``

        :return: 1 if Navigation Successful
        """
        if not self.get_common_object_basic_tab().is_selected():
            self.auto_actions.click_reference(self.get_common_object_basic_tab)
            sleep(2)
            return 1

    def navigate_to_basic_vlans_tab(self):
        """
        - This Keyword Navigate to Vlans Tabs On Common Objects
        - Flow: CONFIGURE-->COMMON OBJECTS-->BASIC-->VLAN's
        - Keyword Usage:
         - ``Navigate To Basic Vlans Tab``

        :return: 1 if Navigation Successful
        """
        self.navigate_configure_common_objects()
        sleep(3)
        self.utils.print_info("Click on common object Basic tab")
        self.navigate_to_common_object_basic_tab()
        self.utils.print_info("Click on Vlan tab...")
        self.auto_actions.click_reference(self.get_common_object_basic_vlans)
        sleep(5)
        return 1

    def navigate_to_manage_alarms(self):
        """
        - This Keyword Navigate to Alarms on manage Menu
        - Flow: Manage --> Alarms
        - Keyword Usage:
         - `` Navigate To Manage Alarms``

        :return: 1 if Navigation Successful
        """
        self.navigate_to_manage_tab()
        sleep(5)
        self.utils.print_info("Click on Alarms tab..")
        self.auto_actions.click_reference(self.get_manage_alarms_nav)
        sleep(5)
        return 1

    def navigate_to_client360(self):
        """
        - This Keyword Navigate to Client360 on ML Insights Menu
        - Flow: ML Insights --> Client 360
        - Keyword Usage:
         - ``Navigate To Client360``

        :return: 1 if Navigation Successful
        """
        self.navigate_to_ml_insight_tab()
        self.utils.print_info("Click on Client 360 tab..")
        self.auto_actions.click_reference(self.get_ml_insight_client360)
        sleep(5)
        return 1

    def navigate_to_network360plan(self):
        """
        - This Keyword Navigate to network360plan on Manage Menu
        - Flow: Manage --> Network360Plan
        - Keyword Usage:
         - ``Navigate To Network360Plan``

        :return: 1 if Navigation Successful
        """
        self.navigate_to_manage_tab()
        self.utils.print_info("Click on Network 360 tab..")
        self.auto_actions.click_reference(self.get_ml_insight_network360plan)
        sleep(5)
        return 1

    def navigate_to_network360monitor(self):
        """
        - This Keyword Navigate to network360monitor on ML Insights Menu
        - Flow: ML Insights --> Network360Monitor
        - Keyword Usage:
         - ``Navigate To Network360Monitor``

        :return: 1 if Navigation Successful
        """
        self.navigate_to_ml_insight_tab()
        self.utils.print_info("Click on Network 360 Monitor tab..")
        self.auto_actions.click_reference(self.get_ml_insight_network360monitor)
        sleep(5)
        return 1

    def navigate_to_network_scorecard(self):
        """
        - This Keyword Navigate to network scorecard on ML Insights Menu
        - Flow: ML Insights --> Network Scorecard
        - Keyword Usage:
         - ``Navigate To Network Scorecard``

        :return: 1 if Navigation Successful
        """
        self.navigate_to_ml_insight_tab()
        self.utils.print_info("Click on Network Scorecard tab..")
        self.auto_actions.click_reference(self.get_ml_insight_network_scorecard)
        sleep(5)
        return 1

    def navigate_to_retail_dashboard(self):
        """
        - This Keyword Navigate to retail dashboard on ML Insights Menu
        - Flow: ML Insights --> Retail Dashboard
        - Keyword Usage:
         - ``Navigate To Retail Dashboard``

        :return: 1 if Navigation Successful
        """
        self.navigate_to_ml_insight_tab()
        self.utils.print_info("Click on Retail Dashboard tab..")
        self.auto_actions.click_reference(self.get_ml_insight_retail)
        sleep(5)
        return 1

    def navigate_to_network_policies_list_view_page(self):
        """
        - This keyword Navigate to policies list view page
        - Flow: Configure --> Network Policies --> List View Tab
        - Keyword Usage:
         - ``Navigate To Network Policies List View Page``

        :return: 1
        """
        self.navigate_configure_network_policies()
        self.utils.print_info("click on list view button")
        self.auto_actions.click_reference(self.get_network_policy_list_view)
        self.utils.print_info("Click on network policy full size page")
        if self.get_network_policy_page_size():
            self.auto_actions.click_reference(self.get_network_policy_page_size)
            sleep(2)
        return 1

    def navigate_to_network_policies_card_view_page(self):
        """
        - This Keyword navigate to the policies card view page
        - Flow: Configure --> Network Policies --> Card View Tab
        - Keyword Usage:
         - ``Navigate To Network Policies Card View Page``
        :return: 1 in Navigated to network Policy Card View else None
        """
        self.navigate_configure_network_policies()
        self.utils.print_info("click on card view button")
        if self.auto_actions.click_reference(self.get_network_policy_card_view) == 1:
            return 1

    def navigate_to_multiple_device_configuration_page(self, device_serials=''):
        """
        - Flow: Manage --> Device --> Select Multiple Device --> Click on Edit button
        - This keyword is navigate to the devices configuration page
        - Keyword Usage:
         - Navigate To Multiple Device Configuration Page    device_serials=${DEVICE1_SER},${DEVICE2_SER}``

        :param device_serials: device serial number with comma separated
        :return: 1 if Navigation Successful
        """
        self.navigate_to_devices()
        device_serials_num = device_serials.split(',')
        if len(device_serials_num) == 1:
            self.utils.print_info("This keyword works with multiple device,pass devices serial number with comma sep")
            return -1
        self.device_common.edit_devices(device_serials)
        sleep(5)
        return 1

    def navigate_to_device360_page_with_mac(self, device_mac):
        """
        - This keyword is used to navigate to the device360 window
        - FLow: Manage --> Device --> Click on either device MAC hyper link
        - Keyword Usage:
         - ``Navigate To Device360 With MAC   ${DEVICE_MAC}``

        :param device_mac:  device MAC number
        :return: 1 if navigated else -1
        """
        self.navigate_to_devices()
        sleep(10)
        return self.device_common.go_to_device360_window(device_mac=device_mac)

    def navigate_to_device360_page_with_host_name(self, device_host):
        """
        - This keyword is used to navigate to the device360 window
        - FLow: Manage --> Device --> Click on either device host name hyper link
        - Keyword Usage:
         - ``Navigate To Device360 With MAC   ${DEVICE_MAC}``

        :param device_host:  device MAC number
        :return: 1 if navigated else -1
        """
        self.navigate_to_devices()
        sleep(6)
        return self.device_common.go_to_device360_window(device_host=device_host)

    def navigate_to_device360_with_client(self, device_serial=''):
        """
        - This keyword is used to navigate to the device360 window
        - FLow: Manage --> Device --> searches for the row with passed device serial and clicks on client hyperlink.
        - Keyword Usage:
         - ``Navigate To Device360 With Client   ${DEVICE_SERIAL}``

        :param device_serial:  device serial number
        :return: 1 if navigated else -1
        """
        self.navigate_to_devices()
        return self.device_common.goto_device360_with_client(device_serial)

    def navigate_to_device_cli_access(self, device_serials=''):
        """
        - This keyword is used to navigate to single/multiple device cli access window
        - Flow:
         - Navigate to Manage --> Device
         - Select the device/devices row based on the passed device serials
         - Click on Action --> Advanced --> CLI Access
        - Keyword Usage:
         - ``Navigate To Device Cli Access    ${DEVICE1_SERIAL}``
         - ``Navigate To Device Cli Access    device_serials=${DEVICE1_SERIAL},${DEVICE2_SERIAL}``

        :param device_serials: comma separated device serial numbers
        :return: 1 if Navigation Successful else -1
        """
        self.navigate_to_devices()
        if self.device_common.select_device_rows(device_serials) == -1:
            return -1

        self.utils.print_info("Click on Device Actions Button")
        self.auto_actions.click_reference(self.get_device_actions_button)

        self.utils.print_info("Hovering over Advanced button")
        self.auto_actions.move_to_element(self.weh.get_element(self.device_actions_advanced))
        sleep(2)

        self.utils.print_info("Clicking on Cli Access")
        if self.get_device_actions_advanced_cli_ap_access().is_displayed():
            self.auto_actions.click_reference(self.get_device_actions_advanced_cli_ap_access)
            sleep(5)
        else:
            self.auto_actions.click_reference(self.get_device_actions_advanced_cli_router_access)
            sleep(5)
        return 1

    def navigate_to_device_utilities_status(self):
        """
        - This keyword is used to navigate to utilities status menu
        - Assumes that already navigated to the Manage --> Device page
        - Keyword Usage:
         - ``Navigate To Device Utilities Status``
        :return: 1 if Navigation Successful else -1
        """
        if not self.get_device_utilities_status_menu_item().is_displayed():
            self.utils.print_info("Clicking on Utilities Button")
            if self.get_device_utilities_button().is_enabled():
                self.auto_actions.click_reference(self.get_device_utilities_button)
                sleep(2)
            else:
                self.utils.print_info("Unable to click on Utilities Button due to being disabled")
                return -1

        self.utils.print_info("Hovering over Status Menu Item")
        if self.get_device_utilities_status_menu_item().is_displayed():
            self.auto_actions.move_to_element(self.get_device_utilities_status_menu_item())
            sleep(2)
        else:
            self.utils.print_info("Unable to hover over Status Menu Item due to not being displayed")
            return -1

        return 1

    def navigate_to_status_interface(self, device_serial=''):
        """
        - This Keyword navigates to device Status Interface window
        - Navigate to Manage --> Device
        - Select the device row based on the passed device serial
        - Click on Utilities --> Status --> Interface
        - Keyword Usage:
         - ``Navigate To Status Interface    ${DEVICE1_SERIAL}``

        :param device_serial: serial number of the device
        :return: 1 if Navigation Successful
        """
        self.navigate_to_devices()
        self.device_common.select_device_row(device_serial)

        if self.navigate_to_device_utilities_status() == -1:
            return -1

        self.utils.print_info("Clicking on Interface")
        interface_access = self.weh.get_element(self.utilities_status_interface)
        self.auto_actions.click(interface_access)
        sleep(5)
        return 1

    def navigate_to_advance_channel_selection(self, device_serial=''):
        """
        - This Keyword navigates to device advanced channel selection window
        - Navigate to Manage --> Device
        - Select the device row based on the passed device serial
        - Click on Utilities --> Status --> Advanced Channel Selection
        - Keyword Usage:
         - ``Navigate To Advance Channel Selection   ${DEVICE_SERIAL}``

        :param device_serial: serial number of the device
        :return: 1 if Navigation Successful
        """
        self.navigate_to_devices()
        self.device_common.select_device_row(device_serial)

        if self.navigate_to_device_utilities_status() == -1:
            return -1

        self.utils.print_info("Clicking on Advance Channel Selection")
        adv_channel = self.weh.get_element(self.utilities_status_adv_channel_sel)
        self.auto_actions.click(adv_channel)
        sleep(5)
        return 1

    def navigate_to_wifi_status_summary(self, device_serial=''):
        """
        - This Keyword navigates to  device Status Interface window
        - Navigate to Manage --> Device
        - Select the device row based on the passed device serial
        - Click on Utilities --> Status --> Wifi Status Summary
        - Keyword Usage:
         - ``Navigate To Wifi Status Summary   ${DEVICE_SERIAL}``

        :param device_serial: serial number of the device
        :return: 1 if Navigation Successful
        """
        self.navigate_to_devices()
        self.device_common.select_device_row(device_serial)

        if self.navigate_to_device_utilities_status() == -1:
            return -1

        self.utils.print_info("Clicking on Wifi Status Summary")
        wifi = self.weh.get_element(self.utilities_status_wifi_status_summary)
        self.auto_actions.click(wifi)
        sleep(5)
        return 1

    def navigate_to_switch_templates(self):
        """
        - This keyword Navigates to Switch Templates Menu on Common Objects
        - Flow Configure --> Common Objects --> Policy --> Switch Templates
        - Keyword Usage
         - ``Navigate To Switch Templates``
        :return: 1 if Navigation Successful
        """
        self.navigate_to_configure_tab()

        self.utils.print_info("Selecting Common Objects")
        self.auto_actions.click_reference(self.get_common_objects_sub_tab)
        sleep(2)

        if self.get_switch_template_option() is None:
            self.utils.print_info("Switch Template menu is NOT visible. Clicking Policy...")
            self.auto_actions.click_reference(self.get_policy_toggle)
            sleep(2)
        self.utils.print_info("Switch Template menu is visible. Selecting...")
        self.auto_actions.click_reference(self.get_switch_template_option)
        sleep(5)
        return 1

    def navigate_to_api_token_mngment(self):
        """
        - This keyword is used to navigate the "API Token Management"
        - Flows XIQ User Menu(Account Info) --> Global Settings --> API Token Management
        - Keyword Usage:
         - ``Navigate To Api Token Mngment``

        :return: 1 if Navigation Successful
        """
        self.navigate_to_global_settings_page()
        self.utils.print_info("Click on api token management tab")
        self.auto_actions.click_reference(self.get_api_token_mgmt_tab())
        sleep(5)
        return 1

    def navigate_a3_inventory(self):
        """
        - This Keyword Navigate to A3 --> Inventory
        - Flow: A3--->Inventory
        - Keyword Usage
          - ``Navigate A3 Inventory``

        :return: 1 if Navigation Successful to Inventory tab on A3 Menu else None
        """
        self.navigate_to_a3_menu()
        self.utils.print_info("Selecting Inventory on A3 Page...")
        self.auto_actions.click_reference(self.get_a3_inventory_tab)
        sleep(2)
        return 1

    def navigate_a3_reporting(self):
        """
        - This Keyword Navigate to A3 --> Reporting
        - Flow: A3--->Reporting
        - Keyword Usage
          - ``Navigate A3 Reporting``

        :return: 1 if Navigation Successful to Reporting tab on A3 Menu else None
        """
        self.navigate_to_a3_menu()
        self.utils.print_info("Selecting Reporting on A3 Page...")
        self.auto_actions.click_reference(self.get_a3_reporting_tab)
        sleep(2)
        return 1

    def navigate_to_essentials_menu(self):
        """
        - This Keyword Navigate to Essentials Menu
        - Keyword Usage
          - ``Navigate To Essentials Menu``
        :return: 1 if Navigation Successful to Essentials Menu
        """
        self.utils.print_info("Clicking on Essentials Icon")
        self.auto_actions.click_reference(self.get_essentials_menu)
        sleep(2)
        return 1

    def navigate_to_extreme_airdefence(self):
        """
        - This Keyword Navigate to Extreme AirDefence Menu
        - Flow: Extreme AirDefence
        - Keyword Usage
          - ``Navigate To Extreme AirDefence``

        :return: 1 if Navigation Successful to Extreme AirDefence Menu
        """
        self.navigate_to_essentials_menu()
        self.utils.print_info("Selecting Extreme AirDefence Menu...")
        self.auto_actions.click_reference(self.get_air_defence_menu)
        sleep(5)
        return 1

    def navigate_to_onboard_tab(self):
        """
         - This keyword Navigates to Onboard Tab
         - Keyword Usage
          - ``Navigate To onboard Tab``

        :return: 1 if Navigation Successful to onboard Tab else return -1
        """
        self.utils.print_info("Selecting Onboard Tab...")
        if self.auto_actions.click_reference(self.get_onboard_tab) == 1:
            sleep(2)
            return 1
        else:
            self.utils.print_info("Unable to navigate to Onboard tab")
            self.screen.save_screen_shot()
            return -1

    def navigate_to_common_object_user_profile(self):
        """
        :return:
        """
        self.utils.print_info("Clicking Configure menu")
        element = self.weh.get_element(self.configure_nav)
        self.auto_actions.click(element)
        sleep(5)

        self.utils.print_info("Clicking common objects")
        common_object_element = self.weh.get_element(self.configure_common_objects_menu_item)
        self.auto_actions.click(common_object_element)
        sleep(5)
        self.utils.print_info("Clicking on policy")
        self.auto_actions.click(self.weh.get_element(self.common_objects_policy))

        sleep(5)
        self.utils.print_info("Clicking on user profile")
        self.auto_actions.click(self.weh.get_element(self.common_objects_policy_user_profile))
        return 1

    def navigate_to_communications_page(self):
        """
        - This Keyword Navigate to communications menu in Global settings page
        - Keyword Usage
          - ``Navigate To Communications Page``

        :return: 1 if Navigation Successful to Communications
        """
        self.utils.print_info("Clicking user account")
        user_account = self.weh.get_element(self.user_account_nav)
        sleep(2)
        self.auto_actions.move_to_element(user_account)
        sleep(2)

        self.utils.print_info("Navigating to communications page...")
        self.auto_actions.click_reference(self.get_communications_nav)
        return 1

    def navigate_to_extreme_iot_menu(self):
        """
        - This Keyword Navigate to Extreme IOT Essentials Page
        - Keyword Usage
          - ``Navigate To Extreme IOT Menu``

        :return: 1 if Navigation Successful to Extreme IOT Essentials Menu
        """
        self.navigate_to_essentials_menu()
        self.utils.print_info("Clicking Extreme IOT Essentials...")
        self.auto_actions.click_reference(self.get_extreme_iot_essentials_menu)
        sleep(2)

        return 1

    def navigate_to_extreme_iot_clients_page(self):
        """
        - This Keyword Navigate to Clients Page on Extreme IOT Essentials Page
        - Keyword Usage
          - ``Navigate To Extreme IOT Clients Page``

        :return: 1 if Navigation Successful to Clients Menu on Extreme IOT Essentials Menu
        """
        self.navigate_to_extreme_iot_menu()

        if self.get_extreme_iot_essentials_clients_submenu():
            self.utils.print_info("Extreme IOT Already Subscribed .Clicking Clients Menu on Extreme IOT...")
            self.auto_actions.click_reference(self.get_extreme_iot_essentials_clients_submenu)
            sleep(2)

        else:
            self.utils.print_info("Clicking Extreme IOT Subscribe button for New User Account")
            self.auto_actions.click_reference(self.get_extreme_iot_essentials_subscribe_button)
            sleep(3)

            self.navigate_to_extreme_iot_menu()
            sleep(2)

            self.utils.print_info("Clicking Clients Menu on Extreme IOT...")
            self.auto_actions.click_reference(self.get_extreme_iot_essentials_clients_submenu)
            sleep(2)
        return 1

    def navigate_to_extreme_iot_devices_page(self):
        """
        - This Keyword Navigate to Devices Page on Extreme IOT Essentials Page
        - Keyword Usage
          - ``Navigate To Extreme IOT Devices Page``

        :return: 1 if Navigation Successful to Devices Menu on Extreme IOT Essentials Menu
        """
        self.navigate_to_extreme_iot_menu()

        if self.get_extreme_iot_essentials_devices_submenu():
            self.utils.print_info("Extreme IOT Already Subscribed .Clicking Devices Menu on Extreme IOT...")
            self.auto_actions.click_reference(self.get_extreme_iot_essentials_devices_submenu)
            sleep(2)

        else:
            self.utils.print_info("Clicking Extreme IOT Subscribe button for New User Account")
            self.auto_actions.click_reference(self.get_extreme_iot_essentials_subscribe_button)
            sleep(3)

            self.navigate_to_extreme_iot_menu()
            sleep(2)

            self.utils.print_info("Clicking Devices Menu on Extreme IOT...")
            self.auto_actions.click_reference(self.get_extreme_iot_essentials_devices_submenu)
            sleep(2)
        return 1

    def navigate_to_extreme_iot_user_profiles_page(self):
        """
        - This Keyword Navigate to user profiles Page on Extreme IOT Essentials Page
        - Keyword Usage
          - ``Navigate To Extreme IOT User Profiles Page``

        :return: 1 if Navigation Successful to user profiles Menu on Extreme IOT Essentials Menu
        """
        self.navigate_to_extreme_iot_menu()

        if self.get_extreme_iot_essentials_user_profiles_submenu():
            self.utils.print_info("Extreme IOT Already Subscribed .Clicking User Profiles Menu on Extreme IOT...")
            self.auto_actions.click_reference(self.get_extreme_iot_essentials_user_profiles_submenu)
            sleep(2)

        else:
            self.utils.print_info("Clicking Extreme IOT Subscribe button for New User Account")
            self.auto_actions.click_reference(self.get_extreme_iot_essentials_subscribe_button)
            sleep(3)

            self.navigate_to_extreme_iot_menu()
            sleep(2)

            self.utils.print_info("Clicking User Profiles Menu on Extreme IOT...")
            self.auto_actions.click_reference(self.get_extreme_iot_essentials_user_profiles_submenu)
            sleep(2)
        return 1

    def navigate_to_extreme_iot_policy_groups_page(self):
        """
        - This Keyword Navigate to policy groups Page on Extreme IOT Essentials Page
        - Keyword Usage
          - ``Navigate To Extreme IOT Policy Groups Page``

        :return: 1 if Navigation Successful to policy groups Menu on Extreme IOT Essentials Menu
        """
        self.navigate_to_extreme_iot_menu()

        if self.get_extreme_iot_essentials_policy_groups_submenu():
            self.utils.print_info("Extreme IOT Already Subscribed .Clicking Policy Groups Menu on Extreme IOT...")
            self.auto_actions.click_reference(self.get_extreme_iot_essentials_policy_groups_submenu)
            sleep(2)

        else:
            self.utils.print_info("Clicking Extreme IOT Subscribe button for New User Account")
            self.auto_actions.click_reference(self.get_extreme_iot_essentials_subscribe_button)
            sleep(3)

            self.navigate_to_extreme_iot_menu()
            sleep(2)

            self.utils.print_info("Clicking Policy Groups Menu on Extreme IOT...")
            self.auto_actions.click_reference(self.get_extreme_iot_essentials_policy_groups_submenu)
            sleep(2)
        return 1

    def navigate_to_extreme_iot_dashboard_page(self):
        """
        - This Keyword Navigate to Dashboard Page on Extreme IOT Essentials Page
        - Keyword Usage
          - ``Navigate To Extreme IOT Dashboard Page``

        :return: 1 if Navigation Successful to Dashboard Menu on Extreme IOT Essentials Menu
        """
        self.navigate_to_extreme_iot_menu()

        if self.get_extreme_iot_essentials_dashboard_submenu():
            self.utils.print_info("Extreme IOT Already Subscribed .Clicking Dashboard Menu on Extreme IOT...")
            self.auto_actions.click_reference(self.get_extreme_iot_essentials_dashboard_submenu)
            sleep(2)

        else:
            self.utils.print_info("Clicking Extreme IOT Subscribe button for New User Account")
            self.auto_actions.click_reference(self.get_extreme_iot_essentials_subscribe_button)
            sleep(3)

            self.navigate_to_extreme_iot_menu()
            sleep(2)

            self.utils.print_info("Clicking Dashboard Menu on Extreme IOT...")
            self.auto_actions.click_reference(self.get_extreme_iot_essentials_policy_groups_submenu)
            sleep(2)
        return 1

    def navigate_to_extreme_guest_menu(self):
        """
        - This Keyword Navigate to Extreme guest Page
        - Keyword Usage
          - ``Navigate To Extreme Guest Menu``

        :return: 1 if Navigation Successful to Extreme Guest Menu
        """
        self.navigate_to_essentials_menu()
        self.utils.print_info("Clicking Extreme Guest  Menu...")
        self.auto_actions.click_reference(self.get_extreme_guest_menu)
        sleep(2)

        return 1

    def navigate_to_extreme_location_menu(self):
        """
        - This Keyword Navigate to Extreme Location Page
        - Keyword Usage
          - ``Navigate To Extreme Location Menu``

        :return: 1 if Navigation Successful to Extreme Location Menu
        """
        self.navigate_to_essentials_menu()
        self.utils.print_info("Clicking on Extreme location")
        self.auto_actions.click_reference(self.get_extreme_location_menu)
        sleep(2)

        return 1

    def navigate_to_extreme_location_dashboard_menu(self):
        """
        - This Keyword Navigate to Dashboard Menu on Extreme Location
        - Keyword Usage
          - ``Navigate To Extreme Location Dashboard Menu``

        :return: 1 if Navigation Successful to Dashboard Menu on Extreme Location
        """
        self.utils.print_info("Clicking Dashboard Menu on Extreme Location")
        self.auto_actions.click_reference(self.get_extreme_location_dashboard_menu)
        return 1

    def navigate_to_extreme_location_sites_menu(self):
        """
        - This Keyword Navigate to Sites Menu on Extreme Location
        - Keyword Usage
          - ``Navigate To Extreme Location Sites Menu``

        :return: 1 if Navigation Successful to Sites Menu on Extreme Location
        """
        self.utils.print_info("Clicking Sites Menu on Extreme Location")
        self.auto_actions.click_reference(self.get_extreme_location_sites_menu)
        return 1

    def navigate_to_extreme_location_category_menu(self):
        """
        - This Keyword Navigate to Category Menu on Extreme Location
        - Keyword Usage
          - ``Navigate To Extreme Location Category Menu``

        :return: 1 if Navigation Successful to Category Menu on Extreme Location
        """
        self.utils.print_info("Clicking Category Menu on Extreme Location")
        self.auto_actions.click_reference(self.get_extreme_location_category_menu)
        return 1

    def navigate_to_extreme_location_access_points_menu(self):
        """
        - This Keyword Navigate to Access Points Menu on Extreme Location
        - Keyword Usage
          - ``Navigate To Extreme Location Access Points Menu``

        :return: 1 if Navigation Successful to Access Points Menu on Extreme Location
        """
        self.utils.print_info("Clicking Access Points Menu on Extreme Location")
        self.auto_actions.click_reference(self.get_extreme_location_access_points_menu)
        return 1

    def navigate_to_extreme_location_beacons_menu(self):
        """
        - This Keyword Navigate to Beacons Menu on Extreme Location
        - Keyword Usage
          - ``Navigate To Extreme Location Beacons Menu``

        :return: 1 if Navigation Successful to Beacons Menu on Extreme Location
        """
        self.utils.print_info("Clicking Beacons Menu on Extreme Location")
        self.auto_actions.click_reference(self.get_extreme_location_beacons_menu)
        return 1

    def navigate_to_extreme_location_asset_management_menu(self):
        """
        - This Keyword Navigate to Beacons Menu on Extreme Location
        - Keyword Usage
          - ``Navigate To Extreme Location Asset Management Menu``

        :return: 1 if Navigation Successful to Asset Management Menu on Extreme Location
        """
        self.utils.print_info("Clicking Asset Management Menu on Extreme Location")
        self.auto_actions.click_reference(self.get_extreme_location_asset_management_menu)
        return 1

    def navigate_to_extreme_location_assets_submenu(self):
        """
        - This Keyword Navigate to Assets SubMenu on Extreme Location
        - Keyword Usage
          - ``Navigate To Extreme Location Assets Submenu``

        :return: 1 if Navigation Successful to Assets SubMenu on Extreme Location
        """
        self.utils.print_info("Clicking Assets SubMenu on Extreme Location")
        self.auto_actions.click_reference(self.get_extreme_location_asset_management_assets_menu)
        return 1

    def navigate_to_extreme_location_alarms_submenu(self):
        """
        - This Keyword Navigate to Alarms SubMenu on Extreme Location
        - Keyword Usage
          - ``Navigate To Extreme Location Alarms Submenu``

        :return: 1 if Navigation Successful to Alarms SubMenu on Extreme Location
        """
        self.utils.print_info("Clicking Alarms SubMenu on Extreme Location")
        self.auto_actions.click_reference(self.get_extreme_location_asset_management_alarms_menu)
        return 1

    def navigate_to_extreme_location_devices_menu(self):
        """
        - This Keyword Navigate to Devicess Menu on Extreme Location
        - Keyword Usage
          - ``Navigate To Extreme Location Devices Menu``

        :return: 1 if Navigation Successful to Devices Menu on Extreme Location
        """
        self.utils.print_info("Clicking Devices Menu on Extreme Location")
        self.auto_actions.click_reference(self.get_extreme_location_devices_menu)
        return 1

    def navigate_to_extreme_location_wireless_devices_submenu(self):
        """
        - This Keyword Navigate to Wireless Devices SubMenu on Extreme Location
        - Keyword Usage
         - ``Navigate To Extreme Location Wireless Devices Submenu``

        :return: 1 if Navigation Successful to Wireless Devices SubMenu on Extreme Location
        """
        self.utils.print_info("Clicking Wireless Devices SubMenu on Extreme Location")
        self.auto_actions.click_reference(self.get_extreme_location_devices_wireless_devices_menu)
        return 1

    def navigate_to_extreme_location_bss_devices_submenu(self):
        """
        - This Keyword Navigate to BSS Devices SubMenu on Extreme Location
        - Keyword Usage
          - ``Navigate To Extreme Location BSS Devices Submenu``

        :return: 1 if Navigation Successful to BSS Devices SubMenu on Extreme Location
        """
        self.utils.print_info("Clicking BSS Devices SubMenu on Extreme Location")
        self.auto_actions.click_reference(self.get_extreme_location_devices_bss_devices_menu)
        return 1

    def navigate_to_extreme_location_settings_menu(self):
        """
        - This Keyword Navigate to Settings Menu on Extreme Location
        - Keyword Usage
          - ``Navigate To Extreme Location Settings Menu``

        :return: 1 if Navigation Successful to Settings Menu on Extreme Location
        """
        self.utils.print_info("Clicking Settings Menu on Extreme Location")
        self.auto_actions.click_reference(self.get_extreme_location_settings_menu)
        return 1

    def navigate_to_extreme_location_device_classification_submenu(self):
        """
        - This Keyword Navigate to Device Classification SubMenu on Extreme Location
        - Keyword Usage
          - ``Navigate To Extreme Location Device Classification Submenu``

        :return: 1 if Navigation Successful to Device Classification SubMenu on Extreme Location
        """
        self.utils.print_info("Clicking Device Classification SubMenu on Extreme Location")
        self.auto_actions.click_reference(self.get_extreme_location_settings_device_classification_menu)
        return 1

    def navigate_to_extreme_location_threshold_submenu(self):
        """
        - This Keyword Navigate to Threshold SubMenu on Extreme Location
        - Keyword Usage
          - ``Navigate To Extreme Location Threshold Submenu``

        :return: 1 if Navigation Successful to Threshold SubMenu on Extreme Location
        """
        self.utils.print_info("Clicking Threshold SubMenu on Extreme Location")
        self.auto_actions.click_reference(self.get_extreme_location_settings_threshold_menu)
        return 1

    def navigate_to_extreme_location_third_party_config_submenu(self):
        """
        - This Keyword Navigate to Third Party Configuration SubMenu on Extreme Location
        - Keyword Usage
          - ``Navigate To Extreme Location Third Party Config Submenu``

        :return: 1 if Navigation Successful to Third Party Config SubMenu on Extreme Location
        """
        self.utils.print_info("Clicking Third Party Configuration SubMenu on Extreme Location")
        self.auto_actions.click_reference(self.get_extreme_location_settings_third_party_config_menu)
        return 1

    def navigate_to_extreme_location_settings_alarms_submenu(self):
        """
        - This Keyword Navigate to Settings Alarms SubMenu on Extreme Location
        - Keyword Usage
          - ``Navigate To Extreme Location Settings Alarms Submenu``

        :return: 1 if Navigation Successful to Settings Alarms SubMenu on Extreme Location
        """
        self.utils.print_info("Clicking Alarms SubMenu on Extreme Location Settings")
        self.auto_actions.click_reference(self.get_extreme_location_settings_alarms_menu)
        return 1

    def navigate_to_cloud_config_groups(self):
        """
        - This keyword Navigates to CCGs Menu on Common Objects
        - Flow Configure --> Common Objects --> Policy --> Cloud Config Groups
        - Keyword Usage
         - ``Navigate To Policy Cloud Config Group Submenu``

        :return: 1 if Navigation Successful
        """
        self.navigate_to_configure_tab()

        self.utils.print_info("Selecting Common Objects")
        self.auto_actions.click_reference(self.get_common_objects_sub_tab)
        sleep(2)

        if self.get_ccg_option() is None:
            self.utils.print_info("CCG menu is NOT visible. Clicking Policy...")
            self.auto_actions.click_reference(self.get_policy_toggle)
            sleep(2)
        self.utils.print_info("CCG menu is visible. Selecting...")
        self.auto_actions.click_reference(self.get_ccg_option)
        sleep(2)

        return 1

    def navigate_to_classification_rule(self):
        """
        - This keyword Navigates to ClassificationRule Menu on Common Objects
        - Flow Configure --> Common Objects --> Policy --> Classification Rule
        - Keyword Usage
         - ``Navigate To Policy Classification Rule Submenu``

        :return: 1 if Navigation Successful
        """
        self.navigate_to_configure_tab()

        self.utils.print_info("Selecting Common Objects")
        self.auto_actions.click_reference(self.get_common_objects_sub_tab)
        sleep(2)

        if self.get_classification_option() is None:
            self.utils.print_info("Classification rule menu is NOT visible. Clicking Policy...")
            self.auto_actions.click_reference(self.get_policy_toggle)
            sleep(2)
        self.utils.print_info("Classification Rule menu is visible. Selecting...")
        self.auto_actions.click_reference(self.get_classification_option)
        sleep(2)

        return 1

    def navigate_to_configure_ppsk_classification(self):
        """
        - This keyword Navigates to PPSK Classification On Configure Menu
        - Flow: Configure --> Users --> User Management --> PPSK Classification
        - Keyword Usage
         - ``Navigate To Configure User Management PPSK Classification Submenu``

        :return: 1 if Navigation Successful
        """
        self.navigate_to_configure_tab()
        self.navigate_to_configure_user_sub_tab()
        sleep(5)

        if self.get_configure_users_user_management_side_menu():
            self.auto_actions.click_reference(self.get_configure_users_user_management_side_menu)
            sleep(5)

        self.utils.print_info("Click on ppsk classification sub menu")
        self.auto_actions.click_reference(self.get_configure_ppsk_classification_side_nav_item)
        sleep(2)

        return 1

    def navigate_to_viq_management_page(self):
        """
        - This Keyword Navigate to VIQ Management Page
        - Flow: Global Settings --> VIQ Management
        - Keyword Usage:
         - ``Navigate To Viq Management Page``
        :return: 1 if Navigation Successful
        """
        self.navigate_to_global_settings_page()
        sleep(2)

        self.utils.print_info("Clicking VIQ Management Button")
        self.auto_actions.click_reference(self.get_viq_management_menu)
        sleep(2)

        return 1

    def navigate_manage_application(self):
        """
        - Navigate to the MANAGE->Application
        - Flow: Manage --> application
        - Keyword Usage:
         - ``Navigate Manage Application``
        :return: 1 If Navigated successfully else -1
        """
        self.utils.print_info("Clicking Manage Tab...")
        try:
            if self.get_manage_tab().is_displayed():
                self.auto_actions.click_reference(self.get_manage_tab)
            else:
                return -2

            self.utils.print_info("Clicking on Application Tab..")
            self.auto_actions.click_reference(self.get_manage_applications_menu_item)
            sleep(2)
            return 1
        except Exception as e:
            self.utils.print_info("Unable to Navigate to  Manage--> Application")
            return -1

    def navigate_manage_events(self):
        """
        - Navigate to the MANAGE->EVENTS
        - Flow: Manage --> Events
        - Keyword Usage:
         - ``Navigate Manage Events``

        :return: 1 If Navigated successfully else -1
        """
        self.utils.print_info("Clicking Manage Tab...")
        try:
            if self.get_manage_tab().is_displayed():
                self.auto_actions.click_reference(self.get_manage_tab)
            else:
                return -2

            self.utils.print_info("Clicking on Events Tab..")
            self.auto_actions.click_reference(self.get_manage_events_menu_item)
            sleep(2)
            return 1

        except Exception as e:
            self.utils.print_info("Unable to Navigate to Events ", e)
            return -1

    def navigate_configure_users(self):
        """
        - Navigate To CONFIGURE--->USERS
        - Flow: CONFIGURE--->USERS
        - Keyword Usage:
         - ``Navigate Configure Users``

        :return: 1 If Navigated successfully else -1
        """
        # Hover to Configure tool bar
        element = self.weh.get_element(self.configure_nav)
        self.auto_actions.move_to_element(element)
        sleep(2)

        # click on the users
        users_element = self.weh.get_element(self.configure_users_nav)
        self.auto_actions.click(users_element)
        sleep(2)
        return 1

    def navigate_to_account_mgmt(self):
        """
        - Navigate to the USER ACCOUNT-> Global settings > Account Management
        - Flow: USER ACCOUNT-> Global settings > Account Management
        - Keyword Usage:
         - ``Navigate To Account Mgmt``

        :return: 1 If Navigated successfully else -1
        """
        self.navigate_to_global_settings_page()
        sleep(2)
        self.utils.print_info("Clicking on account management...")
        account_mgmt_ele = self.weh.get_element(self.account_mgmt)
        sleep(2)
        if account_mgmt_ele.is_displayed():
            self.auto_actions.click(account_mgmt_ele)
            return 1
        else:
            return -2

    def navigate_to_license_mgmt(self):
        """
        - Navigate to the USER ACCOUNT-> Global settings > Account Management
        - Flow: USER ACCOUNT-> Global settings > Account Management
        - Keyword Usage:
         - ``Navigate To License Mgmt``

        :return: 1 If Navigated successfully else -1
        """
        self.navigate_to_global_settings_page()
        sleep(2)
        self.utils.print_info("Clicking on License Management...")
        license_mgmt_ele = self.weh.get_element(self.license_mgmt)
        if license_mgmt_ele.is_displayed():
            self.auto_actions.click(license_mgmt_ele)
            return 1
        else:
            return -2

    def navigate_to_accounts_organization_page(self):
        """
        - Navigate to the USER ACCOUNT-> Global settings > Account --> Organization
        - Flow: USER ACCOUNT-> Global settings > Account --> Organization
        - Keyword Usage:
         - ``Navigate To Accounts Organization Page``

        :return: 1 If Navigated successfully else -1
        """
        self.navigate_to_global_settings_page()
        sleep(2)
        self.utils.print_info("Clicking on organization Slider...")
        organization_ele = self.weh.get_element(self.global_settings_account_organizations_slider)
        sleep(2)
        if organization_ele.is_displayed():
            self.auto_actions.click(organization_ele)
            return 1
        else:
            return -1

    def navigate_to_account_details_page(self):
        """
        - Navigate to the USER ACCOUNT-> Global settings > Account Details
        - Flow: USER ACCOUNT-> Global settings > Account Details
        - Keyword Usage:
         - ``Navigate To Account Details Page``

        :return: 1 If Navigated successfully else -1
        """
        self.navigate_to_global_settings_page()
        sleep(2)
        self.utils.print_info("Clicking on account details...")
        account_details_ele = self.weh.get_element(self.global_settings_account_details)
        sleep(2)
        if account_details_ele.is_displayed():
            self.auto_actions.click(account_details_ele)
            return 1
        else:
            return -2

    def navigate_to_webhooks_page(self):
        """
        - Navigate to the USER ACCOUNT-> Global settings > Webhooks
        - Flow: USER ACCOUNT-> Global settings > Webhooks
        - Keyword Usage:
         - ``Navigate To Webhooks Page``

        :return: 1 If Navigated successfully else -1
        """
        self.navigate_to_global_settings_page()
        self.utils.print_info("Clicking on account details...")
        webhooks_ele = self.weh.get_element(self.global_settings_webhooks)
        if webhooks_ele.is_displayed():
            self.auto_actions.click(webhooks_ele)
            return 1
        else:
            return -1

    def navigate_to_dashboard_page(self):
        """
        - Navigate to dashboard page by clicking top left of UI
        - Flow: Dashboard Menu
        - Keyword Usage:
         - ``Navigate To Dashboard Page``

        :return: 1 If Navigated successfully else -1
        """
        dashboard_element = self.weh.get_element(self.dashboard)
        self.auto_actions.click(dashboard_element)
        sleep(2)

        report_ele = self.weh.get_element(self.create_report)
        if report_ele:
            if report_ele.text == "CREATE REPORT":
                return 1
        else:
            return -1

    def navigate_to_credential_dist_groups(self):
        """
        - Navigate to Global settings > Credential Distribution Groups
        - Flow: Global settings > Credential Distribution Groups
        - Keyword Usage:
         - ``Navigate To Credential Dist Groups``

        :return: 1 If Navigated successfully else -1
        """
        self.navigate_to_global_settings_page()
        sleep(2)
        self.utils.print_info("Clicking on Credentials distribution groups...")
        if self.weh.get_element(self.credential_dist_group).is_displayed():
            self.auto_actions.click(self.weh.get_element(self.credential_dist_group))
            sleep(2)
            return 1
        else:
            return -2

    def navigate_tool_utility(self):
        """
        - Navigate to the Tools->Utilities link
        - Flow: Tools->Utilities
        - Keyword Usage:
         - ``Navigate Tool Utility``

        :return: 1 If Navigated successfully else -1
        """
        sleep(5)
        utilities_element = self.weh.get_element(self.tool_utility_nav)
        sleep(5)
        self.auto_actions.click(utilities_element)

    def navigate_to_license_management(self):
        """
        Navigate to the USER ACCOUNT-> Global Settings > License Management
        :return:
        """
        return self.navigate_to_license_mgmt()

    def navigate_to_radio_profile(self):
        """
        - This keyword Navigates to SSIDs Menu on Common Objects
        - Flow Configure --> Common Objects --> Policy --> Radio Profile
        - Keyword Usage
         - ``Navigate To Radio Profile``

        :return: 1 if Navigation Successful
        """
        self.navigate_to_configure_tab()

        self.utils.print_info("Selecting Common Objects")
        self.auto_actions.click_reference(self.get_common_objects_sub_tab)
        sleep(2)

        if self.get_radio_profile() is None:
            self.utils.print_info("Radio Profile menu is NOT visible. Clicking Policy...")
            self.auto_actions.click_reference(self.get_policy_toggle)
            sleep(2)
        self.utils.print_info("Radio profile  menu is visible. Selecting...")
        self.auto_actions.click_reference(self.get_radio_profile)
        sleep(2)

        return 1

    def navigate_to_device_utilities(self, device_serial=''):
        """
        - This Keyword navigates to  device utilities
        - Navigate to Manage --> Device
        - Select the device row based on the passed device serial
        - Click on Utilities --> Status --> Wifi Status Summary
        - Keyword Usage:
         - ``Navigate To Wifi Status Summary   ${DEVICE_SERIAL}``

        :param device_serial: serial number of the device
        :return: 1 if Navigation Successful
        """
        self.navigate_to_devices()
        self.device_common.select_device_row(device_serial)

        self.utils.print_info("Clicking on Utilities")
        self.auto_actions.click_reference(self.get_device_utilities)
        sleep(2)

    def navigate_to_audit_logs_menu(self):
        """
        - This keyword Navigate to the Audit Logs Slider Menu
        - Flow: Authentication Logs
        - Keyword Usage
         - ``Navigate To Authentication Logs Menu``

        :return: 1 if Navigation Successful to Authentication Logs Slider Menu else return -1
        """

        self.navigate_to_global_settings_page()
        sleep(2)
        self.utils.print_info("Selecting Audit Logs...")
        if self.auto_actions.click_reference(self.get_global_settings_audit_logs_slider) == 1:
            sleep(2)
            return 1
        else:
            self.utils.print_info("Unable to navigate to Audit Logs")
            self.screen.save_screen_shot()
            return -1

    def navigate_to_copilot_menu(self):
        """
        - This Keyword navigates to Copilot Menu
        - Keyword Usage:
         - ``Navigate To Copilot Menu``
        :return: 1 if Navigation Successful
        """
        self.utils.print_info("selecting and clicking on Copilot Menu...")
        self.auto_actions.click_reference(self.get_copilot_tab)
        sleep(5)
        self.screen.save_screen_shot()
        return 1

    def navigate_to_copilot_anomaly_notification_icon(self):
        """
        - This Keyword navigates to Copilot Anomaly Notification Icon
        - Keyword Usage:
         - ``Navigate To Copilot Anomaly Notification Icon``
        :return: 1 if Navigation Successful
        """
        self.utils.print_info("Navigating to Anomaly Notification Icon menu..")
        self.auto_actions.move_to_element(self.get_copilot_anomaly_notification_icon())
        sleep(2)
        self.screen.save_screen_shot()
        return 1
    
    def rbac_user_navigate_to_extreme_airdefence_helpdesk(self):
        """
        - This Keyword is used to check if Extreme Airdefence menu is available for RBAC helpdesk user
        - Flow: Extreme AirDefence
        - Keyword Usage
          - ``Check for Extreme AirDefence menu ``

        :return: 1 if Navigation is not Successful to Extreme AirDefence Menu
        """
        self.utils.print_info("Selecting Extreme AirDefence Menu...")
        if self.auto_actions.click_reference(self.get_essentials_menu):
            self.utils.print_info("Clicked Extreme Airdefense Menu")
            return -1
        else:
            self.utils.print_info("Did not find Extreme AirDefence Menu...")
            sleep(5)
            return 1

    def navigate_to_configure_users_subtab_users(self):
        """
        - This keyword Navigates to PPSK Classification On Configure Menu
        - Flow: Configure --> Users --> User Management --> Users
        - Keyword Usage
         - ``Navigate To Configure User Management Users Submenu``

        :return: 1 if Navigation Successful
        """
        self.navigate_to_configure_tab()
        self.navigate_to_configure_user_sub_tab()
        sleep(5)

        if self.get_configure_users_user_management_side_menu():
            self.auto_actions.click_reference(self.get_configure_users_user_management_side_menu)
            sleep(5)

        self.utils.print_info("Click on Users sub menu")
        self.auto_actions.click_reference(self.get_configure_users_subtab_users_side_nav_item)
        sleep(2)

        return 1

    def navigate_to_policy_imago_tag_profiles(self):
        """
        - This Keyword Navigate to Imago Tag Profile on Common Objects
        - Flow: CONFIGURE-->COMMON OBJECTS-->Imago Tag Profiles
        - Keyword Usage:
         - ``Navigate To Policy Imago Tag Profiles``

        :return: 1 if Navigation Successful
        """
        self.navigate_configure_common_objects()
        sleep(3)
        self.utils.print_info("Click on common Policy tab")
        self.navigate_to_common_object_policy_tab()
        self.utils.print_info("Click on Imago Tag Profile tab...")
        self.auto_actions.click_reference(self.get_common_object_policy_imago_tag_profile)
        sleep(5)

        return 1

    def navigate_to_security_ip_firewall_policies(self):
        """
        - This Keyword Navigate to WIPS Policies on Common Objects
        - Flow: CONFIGURE-->COMMON OBJECTS-->SECURITY-->IP Firewall POLICIES
        - Keyword Usage:
         - ``Navigate To Security IP Firewall Policies``

        :return: 1 if Navigation Successful
        """
        self.navigate_configure_common_objects()
        sleep(3)
        self.utils.print_info("Click on IP Firewall Policies tab...")
        if self.get_common_object_security_ip_firewall_policies():
            self.auto_actions.click_reference(self.get_common_object_security_ip_firewall_policies)
            sleep(5)
        else:
            self.utils.print_info("Click Security button")
            self.auto_actions.click_reference(self.get_common_object_security_tab)
            sleep(2)
            self.utils.print_info("Click  IP Firewall Policies button")
            self.auto_actions.click_reference(self.get_common_object_security_ip_firewall_policies)

        sleep(5)

    def navigate_to_policy_user_profiles(self):
        """
        - This Keyword Navigate to User Profiles on Common Objects
        - Flow: CONFIGURE-->COMMON OBJECTS-->POLICY-->USER PROFILES
        - Keyword Usage:
         - ``Navigate To Policy User Profiles``
        :return: 1 if Navigation Successful
        """
        self.navigate_configure_common_objects()
        sleep(3)
        self.utils.print_info("Click on common Policy tab")
        self.navigate_to_common_object_policy_tab()
        self.utils.print_info("Click on User Profiles tab...")
        self.auto_actions.click_reference(self.get_common_object_policy_user_profiles)
        sleep(5)

        return 1

    def navigate_to_device_management_settings(self):
        """
        - This Keyword Navigate to Device Management Settings Page
        - Flow: Global Settings --> Device Management Settings
        - Keyword Usage:
         - ``navigate to device management settings page``
        :return: 1 if Navigation Successful
        """
        self.navigate_to_global_settings_page()
        sleep(2)

        self.utils.print_info("Clicking Device Management Settings Button")
        self.auto_actions.click_reference(self.get_navigate_to_device_management_settings_menu)
        sleep(2)
        return 1

    def navigate_to_configure_private_client_group(self):
        """
        - This keyword Navigates to Private Client Group On Configure Menu
        - Flow: Configure --> Users --> User Management --> Private Client Groups
        - Keyword Usage
         - ``navigate_to_configure_private_client_group``

        :return: 1 if Navigation Successful
        """
        self.navigate_to_configure_tab()
        self.navigate_to_configure_user_sub_tab()
        sleep(5)

        if self.get_configure_users_user_management_side_menu():
            self.auto_actions.click_reference(self.get_configure_users_user_management_side_menu)
            sleep(5)

        self.utils.print_info("Click on private client group menu")
        self.auto_actions.click_reference(self.get_nav_configure_users_management_private_client_group)
        sleep(2)

    def navigate_to_common_objects_management_options(self):
        """
        - This Keyword Navigate to Management Options on Common Objects
        - Flow: CONFIGURE-->COMMON OBJECTS-->NETWORK-->MANAGEMENT OPTIONS
        - Keyword Usage:
         - ``Navigate To Common Objects Management Options``
        :return: 1 if Navigation Successful
        """
        self.navigate_configure_common_objects()
        sleep(3)
        self.utils.print_info("Click on common object Network tab")
        self.navigate_to_common_object_network_tab()
        self.utils.print_info("Click on Management Options tab...")
        self.auto_actions.click_reference(self.get_common_object_network_management_options)
        sleep(5)

        return 1

    def navigate_to_device_utilities_tools(self):
        """
        - This keyword is used to navigate to utilities tools menu
        - Assumes that already navigated to the Manage --> Device page
        - Keyword Usage:
         - ``Navigate To Device Utilities Tools``
        :return: 1 if Navigation Successful else -1
        """
        if not self.get_device_tools_menu_item().is_displayed():
            self.utils.print_info("Clicking on Utilities Button")
            if self.get_device_utilities_button().is_enabled():
                self.auto_actions.click_reference(self.get_device_utilities_button)
                sleep(2)
            else:
                self.utils.print_info("Unable to click on Utilities Button due to being disabled")
                return -1

        self.utils.print_info("Hovering over Tools Menu Item")
        if self.get_device_tools_menu_item().is_displayed():
            self.auto_actions.move_to_element(self.get_device_tools_menu_item())
            sleep(2)
        else:
            self.utils.print_info("Unable to hover over Tools Menu Item due to not being displayed")
            return -1

        return 1

    def navigate_to_device_client_information(self):
        """
        - This keyword is used to navigate to a single device client information tool window
        - Assumes that already navigated to the Manage --> Device page
        - Keyword Usage:
         - ``Navigate To Device Client Information``
        :return: 1 if Navigation Successful else -1
        """
        if self.navigate_to_device_utilities_tools() == -1:
            return -1

        self.utils.print_info("Clicking on Client Information Menu Item")
        if self.get_device_tools_client_information_menu_item().is_displayed():
            self.auto_actions.click_reference(self.get_device_tools_client_information_menu_item)
            sleep(2)
        else:
            self.utils.print_info("Unable to click on Client Information Menu Item due to not being displayed")
            return -1

        return 1

    def navigate_to_device_get_tech_data(self):
        """
        - This keyword is used to navigate to single/multiple device get tech data tool window
        - Assumes that already navigated to the Manage --> Device page
        - Keyword Usage:
         - ``Navigate To Device Get Tech Data``
        :return: 1 if Navigation Successful else -1
        """
        if self.navigate_to_device_utilities_tools() == -1:
            return -1

        self.utils.print_info("Clicking on Get Tech Data Menu Item")
        if self.get_device_tools_get_tech_menu_item().is_displayed():
            self.auto_actions.click_reference(self.get_device_tools_get_tech_menu_item)
            sleep(2)
        else:
            self.utils.print_info("Unable to click on Get Tech Data Menu Item due to not being displayed")
            return -1

        return 1

    def navigate_to_device_locate_device(self):
        """
        - This keyword is used to navigate to a single device locate device tool window
        - Assumes that already navigated to the Manage --> Device page
        - Keyword Usage:
         - ``Navigate To Device Locate Device``
        :return: 1 if Navigation Successful else -1
        """
        if self.navigate_to_device_utilities_tools() == -1:
            return -1

        self.utils.print_info("Clicking on Locate Device Menu Item")
        if self.get_device_tools_locate_device_menu_item().is_displayed():
            self.auto_actions.click_reference(self.get_device_tools_locate_device_menu_item)
            sleep(2)
        else:
            self.utils.print_info("Unable to click on Locate Device Menu Item due to not being displayed")
            return -1

        return 1

    def navigate_to_device_layer_neighbor_info(self):
        """
        - This keyword is used to navigate to a single device l2 neighbor info tool window
        - Assumes that already navigated to the Manage --> Device page
        - Keyword Usage:
         - ``Navigate To Device Layer Neighbor Info``
        :return: 1 if Navigation Successful else -1
        """
        if self.navigate_to_device_utilities_tools() == -1:
            return -1

        self.utils.print_info("Clicking on L2 Neighbor Info Menu Item")
        if self.get_device_tools_layer_neighbor_info_menu_item().is_displayed():
            self.auto_actions.click_reference(self.get_device_tools_layer_neighbor_info_menu_item)
            sleep(2)
        else:
            self.utils.print_info("Unable to click on L2 Neighbor Info Menu Item due to not being displayed")
            return -1

        return 1

    def navigate_to_device_packet_capture(self):
        """
        - This keyword is used to navigate to a single packet capture tool window
        - Assumes that already navigated to the Manage --> Device page
        - Keyword Usage:
         - ``Navigate To Device Packet Capture``
        :return: 1 if Navigation Successful else -1
        """
        if self.navigate_to_device_utilities_tools() == -1:
            return -1

        self.utils.print_info("Clicking on Packet Capture Menu Item")
        if self.get_device_tools_packet_capture_menu_item().is_displayed():
            self.auto_actions.click_reference(self.get_device_tools_packet_capture_menu_item)
            sleep(2)
        else:
            self.utils.print_info("Unable to click on Packet Capture Menu Item due to not being displayed")
            return -1

        return 1

    def navigate_to_device_vlan_probe(self):
        """
        - This keyword is used to navigate to single/multiple device vlan probe tool window
        - Assumes that already navigated to the Manage --> Device page
        - Keyword Usage:
         - ``Navigate To Device Vlan Probe``
        :return: 1 if Navigation Successful else -1
        """
        if self.navigate_to_device_utilities_tools() == -1:
            return -1

        self.utils.print_info("Clicking on VLAN Probe Menu Item")
        if self.get_device_tools_vlan_probe_menu_item().is_displayed():
            self.auto_actions.click_reference(self.get_device_tools_vlan_probe_menu_item)
            sleep(2)
        else:
            self.utils.print_info("Unable to click on VLAN Probe Menu Item due to not being displayed")
            return -1

        return 1

    def navigate_to_device_utilities_diagnostics(self):
        """
        - This keyword is used to navigate to utilities diagnostics menu
        - Assumes that already navigated to the Manage --> Device page
        - Keyword Usage:
         - ``Navigate To Device Utilities Diagnostics``
        :return: 1 if Navigation Successful else -1
        """
        self.utils.print_info("Clicking on Utilities Button")
        if self.get_device_utilities_button().is_enabled():
            self.auto_actions.click_reference(self.get_device_utilities_button)
            sleep(2)
        else:
            self.utils.print_info("Unable to click on Utilities Button due to being disabled")
            return -1

        self.utils.print_info("Hovering over Diagnostics Menu Item")
        if self.get_device_diagnostics_menu_item().is_displayed():
            self.auto_actions.move_to_element(self.get_device_diagnostics_menu_item())
            sleep(2)
        else:
            self.utils.print_info("Unable to hover over Diagnostics Menu Item due to not being displayed")
            return -1

        return 1

    def navigate_to_device_ping(self):
        """
        - This keyword is used to navigate to a single device ping diagnostic window
        - Assumes that already navigated to the Manage --> Device page
        - Keyword Usage:
         - ``Navigate To Device Ping``
        :return: 1 if Navigation Successful else -1
        """
        if self.navigate_to_device_utilities_diagnostics() == -1:
            return -1

        self.utils.print_info("Clicking on Show Ping Menu Item")
        if self.get_device_diagnostics_show_ping_menu_item().is_displayed():
            self.auto_actions.click_reference(self.get_device_diagnostics_show_ping_menu_item)
            sleep(2)
        else:
            self.utils.print_info("Unable to click on Show Ping Menu Item due to not being displayed")
            return -1

        return 1

    def navigate_to_device_show_log(self):
        """
        - This keyword is used to navigate to a single device show log diagnostic window
        - Assumes that already navigated to the Manage --> Device page
        - Keyword Usage:
         - ``Navigate To Device Show Log``
        :return: 1 if Navigation Successful else -1
        """
        if self.navigate_to_device_utilities_diagnostics() == -1:
            return -1

        self.utils.print_info("Clicking on Show Log Menu Item")
        if self.get_device_diagnostics_show_log_menu_item().is_displayed():
            self.auto_actions.click_reference(self.get_device_diagnostics_show_log_menu_item)
            sleep(2)
        else:
            self.utils.print_info("Unable to click on Show Log Menu Item due to not being displayed")
            return -1

        return 1

    def navigate_to_device_show_mac_table(self):
        """
        - This keyword is used to navigate to a single device show mac table diagnostic window
        - Assumes that already navigated to the Manage --> Device page
        - Keyword Usage:
         - ``Navigate To Device Show Mac Table``
        :return: 1 if Navigation Successful else -1
        """
        if self.navigate_to_device_utilities_diagnostics() == -1:
            return -1

        self.utils.print_info("Clicking on Show MAC Table Menu Item")
        if self.get_device_diagnostics_show_mac_table_menu_item().is_displayed():
            self.auto_actions.click_reference(self.get_device_diagnostics_show_mac_table_menu_item)
            sleep(2)
        else:
            self.utils.print_info("Unable to click on Show MAC Table Menu Item due to not being displayed")
            return -1

        return 1

    def navigate_to_device_show_version(self):
        """
        - This keyword is used to navigate to a single device show version diagnostic window
        - Assumes that already navigated to the Manage --> Device page
        - Keyword Usage:
         - ``Navigate To Device Show Version``
        :return: 1 if Navigation Successful else -1
        """
        if self.navigate_to_device_utilities_diagnostics() == -1:
            return -1

        self.utils.print_info("Clicking on Show Version Menu Item")
        if self.get_device_diagnostics_show_version_menu_item().is_displayed():
            self.auto_actions.click_reference(self.get_device_diagnostics_show_version_menu_item)
            sleep(2)
        else:
            self.utils.print_info("Unable to click on Show Version Menu Item due to not being displayed")
            return -1

        return 1

    def navigate_to_device_show_running_config(self):
        """
        - This keyword is used to navigate to a single device show running config diagnostic window
        - Assumes that already navigated to the Manage --> Device page
        - Keyword Usage:
         - ``Navigate To Device Show Running Config``
        :return: 1 if Navigation Successful else -1
        """
        if self.navigate_to_device_utilities_diagnostics() == -1:
            return -1

        self.utils.print_info("Clicking on Show Running Config Menu Item")
        if self.get_device_diagnostics_show_running_config_menu_item().is_displayed():
            self.auto_actions.click_reference(self.get_device_diagnostics_show_running_config_menu_item)
            sleep(2)
        else:
            self.utils.print_info("Unable to click on Show Running Config Menu Item due to not being displayed")
            return -1

        return 1

    def navigate_to_device_show_startup_config(self):
        """
        - This keyword is used to navigate to a single device show startup config diagnostic window
        - Assumes that already navigated to the Manage --> Device page
        - Keyword Usage:
         - ``Navigate To Device Show Startup Config``
        :return: 1 if Navigation Successful else -1
        """
        if self.navigate_to_device_utilities_diagnostics() == -1:
            return -1

        self.utils.print_info("Clicking on Show Startup Config Menu Item")
        if self.get_device_diagnostics_show_startup_config_menu_item().is_displayed():
            self.auto_actions.click_reference(self.get_device_diagnostics_show_startup_config_menu_item)
            sleep(2)
        else:
            self.utils.print_info("Unable to click on Show Startup Config Menu Item due to not being displayed")
            return -1

        return 1

    def navigate_to_device_show_ip_routes(self):
        """
        - This keyword is used to navigate to a single device show ip routes diagnostic window
        - Assumes that already navigated to the Manage --> Device page
        - Keyword Usage:
         - ``Navigate To Device Show Ip Routes``
        :return: 1 if Navigation Successful else -1
        """
        if self.navigate_to_device_utilities_diagnostics() == -1:
            return -1

        self.utils.print_info("Clicking on Show IP Routes Menu Item")
        if self.get_device_diagnostics_show_ip_routes_menu_item().is_displayed():
            self.auto_actions.click_reference(self.get_device_diagnostics_show_ip_routes_menu_item)
            sleep(2)
        else:
            self.utils.print_info("Unable to click on Show IP Routes Menu Item due to not being displayed")
            return -1

        return 1

    def navigate_to_device_show_mac_routes(self):
        """
        - This keyword is used to navigate to a single device show mac routes diagnostic window
        - Assumes that already navigated to the Manage --> Device page
        - Keyword Usage:
         - ``Navigate To Device Show Mac Routes``
        :return: 1 if Navigation Successful else -1
        """
        if self.navigate_to_device_utilities_diagnostics() == -1:
            return -1

        self.utils.print_info("Clicking on Show MAC Routes Menu Item")
        if self.get_device_diagnostics_show_mac_routes_menu_item().is_displayed():
            self.auto_actions.click_reference(self.get_device_diagnostics_show_mac_routes_menu_item)
            sleep(2)
        else:
            self.utils.print_info("Unable to click on Show MAC Routes Menu Item due to not being displayed")
            return -1

        return 1

    def navigate_to_device_show_arp_cache(self):
        """
        - This keyword is used to navigate to a single device show arp cache diagnostic window
        - Assumes that already navigated to the Manage --> Device page
        - Keyword Usage:
         - ``Navigate To Device Show Arp Cache``
        :return: 1 if Navigation Successful else -1
        """
        if self.navigate_to_device_utilities_diagnostics() == -1:
            return -1

        self.utils.print_info("Clicking on Show ARP Cache Menu Item")
        if self.get_device_diagnostics_show_arp_cache_menu_item().is_displayed():
            self.auto_actions.click_reference(self.get_device_diagnostics_show_arp_cache_menu_item)
            sleep(2)
        else:
            self.utils.print_info("Unable to click on Show ARP Cache Menu Item due to not being displayed")
            return -1

        return 1

    def navigate_to_device_show_roaming_cache(self):
        """
        - This keyword is used to navigate to a single device show roaming cache diagnostic window
        - Assumes that already navigated to the Manage --> Device page
        - Keyword Usage:
         - ``Navigate To Device Show Roaming Cache``
        :return: 1 if Navigation Successful else -1
        """
        if self.navigate_to_device_utilities_diagnostics() == -1:
            return -1

        self.utils.print_info("Clicking on Show Roaming Cache Menu Item")
        if self.get_device_diagnostics_show_roaming_cache_menu_item().is_displayed():
            self.auto_actions.click_reference(self.get_device_diagnostics_show_roaming_cache_menu_item)
            sleep(2)
        else:
            self.utils.print_info("Unable to click on Show Roaming Cache Menu Item due to not being displayed")
            return -1

        return 1

    def navigate_to_device_show_dnxp_neighbors(self):
        """
        - This keyword is used to navigate to a single device show dnxp neighbors diagnostic window
        - Assumes that already navigated to the Manage --> Device page
        - Keyword Usage:
         - ``Navigate To Device Show Dnxp Neighbors``
        :return: 1 if Navigation Successful else -1
        """
        if self.navigate_to_device_utilities_diagnostics() == -1:
            return -1

        self.utils.print_info("Clicking on Show DNXP Neighbors Menu Item")
        if self.get_device_diagnostics_show_dnxp_neighbors_menu_item().is_displayed():
            self.auto_actions.click_reference(self.get_device_diagnostics_show_dnxp_neighbors_menu_item)
            sleep(2)
        else:
            self.utils.print_info("Unable to click on Show DNXP Neighbors Menu Item due to not being displayed")
            return -1

        return 1

    def navigate_to_device_show_dnxp_cache(self):
        """
        - This keyword is used to navigate to a single device show dnxp cache diagnostic window
        - Assumes that already navigated to the Manage --> Device page
        - Keyword Usage:
         - ``Navigate To Device Show Dnxp Cache``
        :return: 1 if Navigation Successful else -1
        """
        if self.navigate_to_device_utilities_diagnostics() == -1:
            return -1

        self.utils.print_info("Clicking on Show DNXP Cache Menu Item")
        if self.get_device_diagnostics_show_dnxp_cache_menu_item().is_displayed():
            self.auto_actions.click_reference(self.get_device_diagnostics_show_dnxp_cache_menu_item)
            sleep(2)
        else:
            self.utils.print_info("Unable to click on Show DNXP Cache Menu Item due to not being displayed")
            return -1

        return 1

    def navigate_to_device_show_amrp_tunnel(self):
        """
        - This keyword is used to navigate to a single device show amrp tunnel diagnostic window
        - Assumes that already navigated to the Manage --> Device page
        - Keyword Usage:
         - ``Navigate To Device Show Amrp Tunnel``
        :return: 1 if Navigation Successful else -1
        """
        if self.navigate_to_device_utilities_diagnostics() == -1:
            return -1

        self.utils.print_info("Clicking on Show AMRP Tunnel Menu Item")
        if self.get_device_diagnostics_show_amrp_tunnel_menu_item().is_displayed():
            self.auto_actions.click_reference(self.get_device_diagnostics_show_amrp_tunnel_menu_item)
            sleep(2)
        else:
            self.utils.print_info("Unable to click on Show AMRP Tunnel Menu Item due to not being displayed")
            return -1

        return 1

    def navigate_to_device_show_gre_tunnel(self):
        """
        - This keyword is used to navigate to a single device show gre tunnel diagnostic window
        - Assumes that already navigated to the Manage --> Device page
        - Keyword Usage:
         - ``Navigate To Device Show Gre Tunnel``
        :return: 1 if Navigation Successful else -1
        """
        if self.navigate_to_device_utilities_diagnostics() == -1:
            return -1

        self.utils.print_info("Clicking on Show GRE Tunnel Menu Item")
        if self.get_device_diagnostics_show_gre_tunnel_menu_item().is_displayed():
            self.auto_actions.click_reference(self.get_device_diagnostics_show_gre_tunnel_menu_item)
            sleep(2)
        else:
            self.utils.print_info("Unable to click on Show GRE Tunnel Menu Item due to not being displayed")
            return -1

        return 1

    def navigate_to_device_show_ike_event(self):
        """
        - This keyword is used to navigate to a single device show ike event diagnostic window
        - Assumes that already navigated to the Manage --> Device page
        - Keyword Usage:
         - ``Navigate To Device Show Ike Event``
        :return: 1 if Navigation Successful else -1
        """
        if self.navigate_to_device_utilities_diagnostics() == -1:
            return -1

        self.utils.print_info("Clicking on Show IKE Event Menu Item")
        if self.get_device_diagnostics_show_ike_event_menu_item().is_displayed():
            self.auto_actions.click_reference(self.get_device_diagnostics_show_ike_event_menu_item)
            sleep(2)
        else:
            self.utils.print_info("Unable to click on Show IKE Event Menu Item due to not being displayed")
            return -1

        return 1

    def navigate_to_device_show_ike_sa(self):
        """
        - This keyword is used to navigate to a single device show ike sa diagnostic window
        - Assumes that already navigated to the Manage --> Device page
        - Keyword Usage:
         - ``Navigate To Device Show Ike Sa``
        :return: 1 if Navigation Successful else -1
        """
        if self.navigate_to_device_utilities_diagnostics() == -1:
            return -1

        self.utils.print_info("Clicking on Show IKE SA Menu Item")
        if self.get_device_diagnostics_show_ike_sa_menu_item().is_displayed():
            self.auto_actions.click_reference(self.get_device_diagnostics_show_ike_sa_menu_item)
            sleep(2)
        else:
            self.utils.print_info("Unable to click on Show IKE SA Menu Item due to not being displayed")
            return -1

        return 1

    def navigate_to_device_show_ipsec_sa(self):
        """
        - This keyword is used to navigate to a single device show ipsec sa diagnostic window
        - Assumes that already navigated to the Manage --> Device page
        - Keyword Usage:
         - ``Navigate To Device Show Ipsec Sa``
        :return: 1 if Navigation Successful else -1
        """
        if self.navigate_to_device_utilities_diagnostics() == -1:
            return -1

        self.utils.print_info("Clicking on Show IPSec SA Menu Item")
        if self.get_device_diagnostics_show_ipsec_sa_menu_item().is_displayed():
            self.auto_actions.click_reference(self.get_device_diagnostics_show_ipsec_sa_menu_item)
            sleep(2)
        else:
            self.utils.print_info("Unable to click on Show IPSec SA Menu Item due to not being displayed")
            return -1

        return 1

    def navigate_to_device_show_ipsec_tunnel(self):
        """
        - This keyword is used to navigate to a single device show ipsec tunnel diagnostic window
        - Assumes that already navigated to the Manage --> Device page
        - Keyword Usage:
         - ``Navigate To Device Show Ipsec Tunnel``
        :return: 1 if Navigation Successful else -1
        """
        if self.navigate_to_device_utilities_diagnostics() == -1:
            return -1

        self.utils.print_info("Clicking on Show IPSec Tunnel Menu Item")
        if self.get_device_diagnostics_show_ipsec_tunnel_menu_item().is_displayed():
            self.auto_actions.click_reference(self.get_device_diagnostics_show_ipsec_tunnel_menu_item)
            sleep(2)
        else:
            self.utils.print_info("Unable to click on Show IPSec Tunnel Menu Item due to not being displayed")
            return -1

        return 1

    def navigate_to_device_show_vpn_tunnel(self):
        """
        - This keyword is used to navigate to a single device show vpn tunnel diagnostic window
        - Assumes that already navigated to the Manage --> Device page
        - Keyword Usage:
         - ``Navigate To Device Show Vpn Tunnel``
        :return: 1 if Navigation Successful else -1
        """
        if self.navigate_to_device_utilities_diagnostics() == -1:
            return -1

        self.utils.print_info("Clicking on Show VPN Tunnel Menu Item")
        if self.get_device_diagnostics_show_vpn_tunnel_menu_item().is_displayed():
            self.auto_actions.click_reference(self.get_device_diagnostics_show_vpn_tunnel_menu_item)
            sleep(2)
        else:
            self.utils.print_info("Unable to click on Show VPN Tunnel Menu Item due to not being displayed")
            return -1

        return 1

    def navigate_to_device_show_cpu(self):
        """
        - This keyword is used to navigate to a single device show cpu diagnostic window
        - Assumes that already navigated to the Manage --> Device page
        - Keyword Usage:
         - ``Navigate To Device Show Cpu``
        :return: 1 if Navigation Successful else -1
        """
        if self.navigate_to_device_utilities_diagnostics() == -1:
            return -1

        self.utils.print_info("Clicking on Show CPU Menu Item")
        if self.get_device_diagnostics_show_cpu_menu_item().is_displayed():
            self.auto_actions.click_reference(self.get_device_diagnostics_show_cpu_menu_item)
            sleep(2)
        else:
            self.utils.print_info("Unable to click on Show CPU Menu Item due to not being displayed")
            return -1

        return 1

    def navigate_to_device_show_memory(self):
        """
        - This keyword is used to navigate to a single device show memory diagnostic window
        - Assumes that already navigated to the Manage --> Device page
        - Keyword Usage:
         - ``Navigate To Device Show Memory``
        :return: 1 if Navigation Successful else -1
        """
        if self.navigate_to_device_utilities_diagnostics() == -1:
            return -1

        self.utils.print_info("Clicking on Show Memory Menu Item")
        if self.get_device_diagnostics_show_memory_menu_item().is_displayed():
            self.auto_actions.click_reference(self.get_device_diagnostics_show_memory_menu_item)
            sleep(2)
        else:
            self.utils.print_info("Unable to click on Show Memory Menu Item due to not being displayed")
            return -1

        return 1

    def navigate_to_device_show_pse(self):
        """
        - This keyword is used to navigate to a single device show pse diagnostic window
        - Assumes that already navigated to the Manage --> Device page
        - Keyword Usage:
         - ``Navigate To Device Show Pse``
        :return: 1 if Navigation Successful else -1
        """
        if self.navigate_to_device_utilities_diagnostics() == -1:
            return -1

        self.utils.print_info("Clicking on Show PSE Menu Item")
        if self.get_device_diagnostics_show_pse_menu_item().is_displayed():
            self.auto_actions.click_reference(self.get_device_diagnostics_show_pse_menu_item)
            sleep(2)
        else:
            self.utils.print_info("Unable to click on Show PSE Menu Item due to not being displayed")
            return -1

        return 1

    def navigate_to_locked_users_tab(self):
        """"
        - This Keyword Navigate to Locked Users Page
        - Flow: Configure --> Users --> User Management --> Locked Users
        - Keyword Usage:
          - 'Navigate to Locked Users page'
        :return: 1 if Navigation Successful
        """
        self.navigate_to_configure_tab()
        self.navigate_to_configure_user_sub_tab()
        sleep(5)

        if self.get_configure_users_user_management_side_menu():
            self.auto_actions.click_reference(self.get_configure_users_user_management_side_menu)
            sleep(5)

        self.utils.print_info("Click on Locked Users sub menu")
        locked_users_ele = self.weh.get_element(self.locked_users_tab)
        if locked_users_ele.is_displayed():
            self.auto_actions.click(locked_users_ele)
            return 1
        else:
            self.utils.print_info("Unable to navigate to Locked Users Page")
            self.screen.save_screen_shot()
            return -2

    def navigate_to_unbind_device_tab(self):
        """"
        - This Keyword Navigate to Unbind Device Page
        - Flow: Configure --> Users --> User Management --> Unbind Device
        - Keyword Usage:
          - 'Navigate to Unbind Device page'
        :return: 1 if Navigation Successful
        """
        self.navigate_to_configure_tab()
        self.navigate_to_configure_user_sub_tab()
        sleep(5)

        if self.get_configure_users_user_management_side_menu():
            self.auto_actions.click_reference(self.get_configure_users_user_management_side_menu)
            sleep(5)

        self.utils.print_info("Click on Unbind Device sub menu")
        unbind_device_ele = self.weh.get_element(self.unbind_device_tab)
        if unbind_device_ele.is_displayed():
            self.auto_actions.click(unbind_device_ele)
            return 1
        else:
            self.utils.print_info("Unable to navigate to Unbind Device Page")
            self.screen.save_screen_shot()
            return -2

    def navigate_to_client_monitor_and_diagnosis_tab(self):
        """"
        - This Keyword Navigate to Client Monitor and Diagnosis Page
        - Flow: Manage --> Client Monitor & Diagnosis
        - Keyword Usage:
          - 'Navigate To Client Monitor And Diagnosis Tab'
        :return: 1 if Navigation Successful
        """
        self.navigate_to_manage_tab()
        sleep(5)

        self.utils.print_info("Click on Client Monitor & Diagnosis Page")
        client_monitor_diagnosis_ele = self.weh.get_element(self.client_monitor_diagnosis_tab)
        if client_monitor_diagnosis_ele.is_displayed():
            self.auto_actions.click(client_monitor_diagnosis_ele)
            return 1
        else:
            self.utils.print_info("Unable to navigate to Client Monitor & Diagnosis Page")
            self.screen.save_screen_shot()
            return -2

    def navigate_manage_alerts(self):
        """
        - Navigate to the MANAGE->ALERTS
        - Flow: Manage --> Alerts
        - Keyword Usage:
         - ``Navigate Manage Alerts``

        :return: 1 If Navigated successfully else -1
        """
        self.utils.print_info("Clicking Manage Tab...")
        try:
            if self.get_manage_tab().is_displayed():
                self.auto_actions.click_reference(self.get_manage_tab)
            else:
                return -1

            self.utils.print_info("Clicking on Alerts Tab..")
            self.auto_actions.click_reference(self.get_manage_alerts_menu_item)
            sleep(2)
            return 1

        except Exception as e:
            self.utils.print_info("Unable to Navigate to Alerts ", e)
            return -1

    def navigate_to_applications_tab(self):
        """"
        - This Keyword Navigate to Applications Page
        - Flow: Manage --> Applications
        - Keyword Usage:
          - 'Navigate to Applications page'
        :return: 1 if Navigation Successful
        """
        self.navigate_to_manage_tab()
        sleep(5)

        self.utils.print_info("Click on Applications Page")
        applications_page_ele = self.weh.get_element(self.applications_tab)
        if applications_page_ele.is_displayed():
            self.auto_actions.click(applications_page_ele)
            return 1
        else:
            self.utils.print_info("Unable to navigate to Applications Page")
            self.screen.save_screen_shot()
            return -2

    def navigate_to_manage_summary(self):
        """
         - This keyword Navigates to Summary on Manage Menu
         - Flow Manage--> Summary
         - Keyword Usage
          - ``Navigate To Manage Summary``

        :return: 1 if Navigation Successful to Summary Sub tab on Monitor Tab else return -1
        """
        if self.navigate_to_manage_tab() == 1:
            self.utils.print_info("Clicking Summary Tab...")
            if self.auto_actions.click_reference(self.get_manage_summary_menu_item) == 1:
                sleep(2)
                return 1
            else:
                self.utils.print_info("Unable to navigate to Summary tab")
                self.screen.save_screen_shot()
                return -1
        else:
            return -1

    def navigate_to_manage_users(self):
        """
         - This keyword Navigates to Users on Manage Menu
         - Flow Manage--> Users
         - Keyword Usage
          - ``Navigate To Manage Users``

        :return: 1 if Navigation Successful to Users Sub tab on Monitor Tab else return -1
        """
        if self.navigate_to_manage_tab() == 1:
            self.utils.print_info("Clicking Users Tab...")
            if self.auto_actions.click_reference(self.get_manage_users_menu_item) == 1:
                sleep(2)
                return 1
            else:
                self.utils.print_info("Unable to navigate to Users tab")
                self.screen.save_screen_shot()
                return -1
        else:
            return -1

    def navigate_to_configure_guest_essentials_users(self):
        """
         - This keyword Navigates to Guest Essentials Users on Configure Menu
         - Flow Configure--> Guest Essentials Users
         - Keyword Usage
          - ``Navigate To Configure Guest Essentials Users``

        :return: 1 if Navigation Successful to Guest Essentials Users Sub tab on Configure Tab else return -1
        """
        if self.navigate_to_configure_tab() == 1:
            self.utils.print_info("Clicking Guest Essentials Users Tab...")
            if self.auto_actions.click_reference(self.get_configure_guest_essentials_users_menu_item) == 1:
                sleep(2)
                return 1
            else:
                self.utils.print_info("Unable to navigate to Guest Essentials Users tab")
                self.screen.save_screen_shot()
                return -1
        else:
            return -1

    def navigate_to_vpn_management_tab(self):
        """"
        - This Keyword Navigate to VPN Management Page
        - Flow: Manage --> VPN Management
        - Keyword Usage:
          - 'Navigate to VPN Management Tab'
        :return: 1 if Navigation Successful, else -1
        """
        self.navigate_to_manage_tab()
        sleep(5)

        self.utils.print_info("Click on VPN Management Tab")
        if self.get_vpn_management_tab().is_displayed():
            self.auto_actions.click_reference(self.get_vpn_management_tab)
            return 1
        else:
            self.utils.print_info("Unable to navigate to VPN Management Page")
            self.screen.save_screen_shot()
            return -1

    def point_client_hyperlink_to_client360(self):
        """"
        - This Keyword point client hyperlink to Client 360 page in ML Insights
        - Flow: Client Hyperlink --> ML Insights --> Client 360
        - Keyword Usage:
          - 'Point Client Hyperlink To Client360'
        :return: 1 if Navigation Successful, else -1
        """

        self.utils.print_info("Click on Clients Hyperlink")
        if self.get_clients_hyperlink().is_displayed():
            self.auto_actions.click_reference(self.get_clients_hyperlink)
            return 1
        else:
            self.utils.print_info("Unable to open clients hyperlink page")
            self.screen.save_screen_shot()
            return -1

    def navigate_to_vpn_services_tab(self):
        """"
        - This Keyword Navigate to VPN Services Page
        - Flow: Assume that already navigated to Configure > Common Objects > Network tab
                Then navigate to VPN Services page
        - Keyword Usage:
          - 'Navigate to VPN Services Tab'
        :return: 1 if Navigation Successful, else -1
        """

        self.utils.print_info("Click on VPN Services Tab")
        if self.get_vpn_services_tab().is_displayed():
            self.auto_actions.click_reference(self.get_vpn_services_tab)
            return 1
        else:
            self.utils.print_info("Unable to navigate to VPN Services Page")
            self.screen.save_screen_shot()
            return -1
    
    def navigate_to_manage_events(self):
        """
         - This keyword Navigates to Events on Manage Menu
         - Flow Manage--> Events
         - Keyword Usage
          - ``Navigate To Events``
        :return: 1 if Navigation Successful to Devices Sub tab on Monitor Tab else return -1
        """
        if self.navigate_to_manage_tab() == 1:
            self.utils.print_info("Clicking Events Tab...")
            if self.auto_actions.click_reference(self.get_devices_nav) == 1:
                sleep(2)
                return 1
            else:
                self.utils.print_info("Unable to navigate to Devices tab")
                self.screen.save_screen_shot()
                return -1
        else:
            return -1

    def navigate_to_port_configuration_d360(self, **kwargs):
        """
         - Assumes that D360 poge is already open
         - Flow: Clicks 'Configure' button -> Scrolls down -> Clicks 'Port Configuration" ->
                 Waits for the port rows to load
        :return: 1 if 'Port Configuration' has been clicked and the port rows have been loaded on the page
                 -1 if elements are not found along the way
        """

        self.utils.print_info("Finding 'Configure' button...")
        configure_button = self.get_configure_button_d360()
        if configure_button:
            self.utils.print_info("Found 'Configure' button! Clicking...")
            self.auto_actions.scroll_by_horizontal(configure_button)
            self.auto_actions.click(configure_button)
            self.utils.print_info("Finding 'Port Configuration' button...")
            port_configuration_button = self.get_port_configuration_d360()
            if port_configuration_button:
                self.utils.print_info("Found 'Port Configuration' button! Clicking...")
                self.auto_actions.scroll_by_horizontal(port_configuration_button)
                self.auto_actions.click(port_configuration_button)
                self.utils.print_info("Waiting for port rows to load in d360 Port Configuration page...")
                self.utils.wait_till(self.get_port_rows_d360)
                kwargs['pass_msg'] = " 'Port Configuration' button clicked!"
                self.common_validation.passed(**kwargs)
                return 1
            else:
                self.utils.print_info("Failed to find 'Port Configuration' button!")
                kwargs['fail_msg'] = "Failed to find 'Port Configuration' button!"
                self.screen.save_screen_shot()
                self.common_validation.failed(**kwargs)
                return -1
        else:
            self.utils.print_info("Failed to find 'Configure' button!")
            kwargs['fail_msg'] = "Failed to find 'Configure' button!"
            self.screen.save_screen_shot()
            self.common_validation.failed(**kwargs)
            return -1

    def enable_page_size(self, page_size='100', **kwargs):
        """
            - This keyword clicks the page size of that page
                 - Flow Manage--> Common --> Navigator
                 - Keyword Usage
                  - ``enable_page_size  page_size=20``

                :return: 1 if enabling page size successfully else returns -1
        """
        if self.get_network_policy_page_size() != None:
            self.utils.print_info("Clicking on page size...")
            if self.auto_actions.click(self.get_network_policy_page_size(page_size)) == 1:
                self.screen.save_screen_shot()
                kwargs['pass_msg'] = " Clicking on page size "
                self.common_validation.passed(**kwargs)
                return 1
            else:
                self.screen.save_screen_shot()
                kwargs['fail_msg'] = " Not able to click on page size "
                self.common_validation.failed(**kwargs)
                return -1