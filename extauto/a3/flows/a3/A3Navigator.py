from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common.Utils import Utils
from common.Screen import Screen
from common.AutoActions import AutoActions
from a3.elements.A3WebElements import A3WebElements
from a3.elements.NavigatorWebElements import NavigatorWebElements
from xiq.flows.common.DeviceCommon import DeviceCommon
from extauto.common.CommonValidation import CommonValidation


class Navigator(NavigatorWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.device_common = DeviceCommon()
        self.a3_web_elements = A3WebElements()
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
            return 1
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

        :return: None
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

    def navigate_to_devices(self, **kwargs):
        """
         - This keyword Navigates to Devices on Manage Menu
         - Flow Manage--> Devices
         - Keyword Usage
          - ``Navigate To Devices``

        :return: 1 if Navigation Successful to Devices Sub tab on Monitor Tab else return -1
        """
        if self.navigate_to_manage_tab() == 1:
            self.utils.print_info("Clicking Devices Tab...")
            if self.auto_actions.click_reference(self.get_devices_nav) == 1:
                sleep(2)
                kwargs['pass_msg'] = "Navigation Successful to Devices tab"
                self.common_validation.passed(**kwargs)
                return 1
            else:
                self.screen.save_screen_shot()
                kwargs['fail_msg'] = "Unable to navigate to Devices tab"
                self.common_validation.failed(**kwargs)
                return -1

    def navigate_to_ssids(self):
        """
        - This keyword Navigates to SSIDs Menu on Common Objects
        - Flow Configure --> Common Objects --> Policy --> SSIDs
        - Keyword Usage
         - ``Navigate To SSIDs``

        :return: None
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

    def navigate_to_tools_page(self):
        """
        - This keyword Navigates to Tools Page on Monitor Menu
        - Flow MANAGE->Tools
        - Keyword Usage
         - ``Navigate To Tools Page``

        :return:  1 if Navigation Successful to Tools Sub tab on Monitor Tab else return -1
        """
        self.navigate_to_manage_tab()
        self.navigate_to_tools_sub_tab()

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

        self.navigate_to_network_policies_tab()

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

    def navigate_to_network_policies_tab(self):
        """
         - This keyword Navigates to Network Policies
         - Keyword Usage
          - ``Navigate To Network Policies Tab``

        :return: 1 if Navigation Successful to Network Policies On Configure Menu else return -1
        """
        self.utils.print_info("Selecting Network Policies Tab...")
        if self.auto_actions.click_reference(self.get_network_policies_sub_tab) == 1:
            sleep(2)
            return 1
        else:
            self.utils.print_info("Unable to navigate to Network Policies tab")
            self.screen.save_screen_shot()
            return -1

    def navigate_to_clients_tab(self):
        """
         - This keyword Navigates to Clients Tab on Manage Menu
         - Keyword Usage
          - ``Navigate To Clients Tab``

        :return: 1 if Navigation Successful to Clients On Monitor Menu else return -1
        """
        self.utils.print_info("Selecting Clients Tab...")
        if self.auto_actions.click_reference(self.get_clients_sub_tab) == 1:
            sleep(2)
            return 1
        else:
            self.utils.print_info("Unable to navigate to Clients tab")
            self.screen.save_screen_shot()
            return -1

    def navigate_to_clients(self):
        """
        - This keyword Navigates to Clients On Monitor Menu
        - Flow: Monitor --> Clients
        - Keyword Usage
         - ``Navigate To Clients``

        :return: 1 if Navigation Successful to Clients Tab on Monitor else return -1
        :return: -2 if Navigation Not Successful to Monitor Tab
        """
        if self.get_manage_tab().is_displayed():
            self.navigate_to_manage_tab()
            sleep(2)
        else:
            return -2
        self.navigate_to_clients_tab()

    def navigate_to_user_account(self):
        """
        - This keyword Navigates to User Account Menu
        - Keyword Usage
         - ``Navigate To User Account``

        :return: 1 if Navigation Successful to User Account Menu else return -1
        """
        self.utils.print_info("Selecting user account...")
        if self.auto_actions.click_reference(self.get_user_account_nav) == 1:
            sleep(2)
            return 1
        else:
            self.utils.print_info("Unable to navigate to user account")
            self.screen.save_screen_shot()
            return -1

    def _navigate_to_global_settings(self):
        """
        - This method is used to click on the global setting button
        """
        self.utils.print_info("Selecting global settings...")
        if self.auto_actions.click_reference(self.get_global_settings_nav) == 1:
            sleep(2)
            return 1
        else:
            self.utils.print_info("Unable to navigate to global settings")
            self.screen.save_screen_shot()
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
         - ``Navigate To Clients``

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

        :return: None
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

    def navigate_to_authentication_logs_menu(self):
        """
        - This keyword Navigate to the Authentication Logs Slider Menu
        - Flow: Authentication Logs
        - Keyword Usage
         - ``Navigate To Authentication Logs Menu``

        :return: 1 if Navigation Successful to Authentication Logs Slider Menu else return -1
        """
        self.utils.print_info("Selecting Authentication Logs...")

        if self.auto_actions.click_reference(self.global_settings_authentication_logs_slider) == 1:
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
        if self.auto_actions.click_reference(self.global_settings_accounting_logs_slider) == 1:
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

        :return: None
        """
        if not self.get_common_object_authentication_tab().is_selected():
            self.auto_actions.click_reference(self.get_common_object_authentication_tab)
            sleep(2)

    def navigate_to_captive_web_portal(self):
        """
        - This keyword Navigate to the captive web portal tab on common objects
        - FLow: Configure --> Common Object --> Authentication --> Captive Web Portal
        - Keyword Usage
         - ``Navigate To Captive Web Portal``

        :return: None
        """
        self.navigate_configure_common_objects()
        self.utils.print_info("Click on common authentication tab")
        self.navigate_to_common_object_authentication_tab()
        self.utils.print_info("Click on captive web portal tab...")
        self.auto_actions.click_reference(self.get_common_object_authentication_captive_portal)
        sleep(5)

    def navigate_to_aaa_server_settings(self):
        """
        - This Keyword Navigate to AAA server Settings on common objects
        - Flow: Configure --> Common Object --> Authentication --> AAA Server Settings
        - Keyword Usage
         - ``Navigate To AAA Server Settings``

        :return: None
        """
        self.navigate_configure_common_objects()
        self.utils.print_info("Click on common authentication tab")
        self.navigate_to_common_object_authentication_tab()
        self.utils.print_info("Click on AAA server Settings...")
        self.auto_actions.click_reference(self.get_common_object_authentication_aaa_server_settings)
        sleep(5)

    def navigate_to_ad_servers(self):
        """
        - This Keyword Navigate to AD servers on common objects
        - Flow: Configure --> Common Object --> Authentication --> Ad Servers
        - Keyword Usage
         - ``Navigate To Ad Servers``

        :return: None
        """
        self.navigate_configure_common_objects()
        self.utils.print_info("Click on common authentication tab")
        self.navigate_to_common_object_authentication_tab()
        self.utils.print_info("Click on AAA server Settings...")
        self.auto_actions.click_reference(self.get_common_object_authentication_ad_servers)
        sleep(5)

    def navigate_to_external_radius_server(self):
        """
        - This Keyword Navigate to External Radius Server on common objects
        - Flow: Configure --> Common Object --> Authentication --> External Radius Server
        - Keyword Usage
         - ``Navigate To External Radius Server``

        :return: None
        """
        self.navigate_configure_common_objects()
        self.utils.print_info("Click on common authentication tab")
        self.navigate_to_common_object_authentication_tab()
        self.utils.print_info("Click on  external radius server...")
        self.auto_actions.click_reference(self.get_common_object_authentication_external_radius_server)
        sleep(5)

    def navigate_to_extreme_networks_a3(self):
        """
        - This Keyword Navigate to Extreme Networks A3 on common objects
        - Flow: Configure --> Common Object --> Authentication --> Extreme Networks A3
        - Keyword Usage
         - ``Navigate To Extreme Networks A3``

        :return: None
        """
        self.navigate_configure_common_objects()
        self.utils.print_info("Click on common authentication tab")
        self.navigate_to_common_object_authentication_tab()
        self.utils.print_info("Click on External network A3...")
        self.auto_actions.click_reference(self.get_common_object_authentication_extreme_networks_a3)
        sleep(5)

    def navigate_to_servers(self):
        """
        - This Keyword Navigate to Servers on common objects
        - Flow: Configure --> Common Object --> Authentication --> Servers
        - Keyword Usage
         - ``Navigate To Servers``

        :return: None
        """
        self.navigate_configure_common_objects()
        self.utils.print_info("Click on common authentication tab")
        self.navigate_to_common_object_authentication_tab()
        self.utils.print_info("Click on servers tab...")
        self.auto_actions.click_reference(self.get_common_object_authentication_servers)
        sleep(5)

    def navigate_to_ldap_servers(self):
        """
        - This Keyword Navigate to LDAP Servers on common objects
        - Flow: Configure --> Common Object --> Authentication --> LDAP Servers
        - Keyword Usage
         - ``Navigate To Ldap Servers``

        :return: None
        """
        self.navigate_configure_common_objects()
        self.utils.print_info("Click on common authentication tab")
        self.navigate_to_common_object_authentication_tab()
        self.utils.print_info("Click on servers tab...")
        self.auto_actions.click_reference(self.get_common_object_authentication_ldap_servers)
        sleep(5)

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
          - ``Navigate To Manage Security``

        :return: 1 if Navigation Successful to Security tab on Monitor Menu else return -1
        """
        self.navigate_to_manage_tab()
        self.navigate_to_security_option()

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

        :return: None
        """
        self.navigate_configure_common_objects()
        sleep(3)
        self.utils.print_info("Click on common Security tab")
        self.navigate_to_common_object_security_tab()
        self.utils.print_info("Click on WIPS Policies tab...")
        self.auto_actions.click_reference(self.get_common_object_security_wips_policies)
        sleep(5)

    def navigate_to_common_object_policy_tab(self):
        """
        - This Keyword Navigate to Policies option Menu on Common Objects
        - Assumes that already navigated to the configure --> common object
        - Keyword Usage:
         - ``Navigate To Common Object Policy Tab``

        :return: None
        """
        if not self.get_common_object_policy_tab().is_selected():
            self.auto_actions.click_reference(self.get_common_object_policy_tab)
            sleep(2)

    def navigate_to_policy_ap_template(self):
        """
        - This Keyword Navigate to AP Templates on Common Objects
        - Flow: CONFIGURE-->COMMON OBJECTS-->AP Templates
        - Keyword Usage:
         - ``Navigate To Policy Ap Template``

        :return: None
        """
        self.navigate_configure_common_objects()
        sleep(3)
        self.utils.print_info("Click on common Policy tab")
        self.navigate_to_common_object_policy_tab()
        self.utils.print_info("Click on Ap Template tab...")
        self.auto_actions.click_reference(self.get_common_object_policy_ap_template)
        sleep(5)

    def navigate_to_manage_reports(self):
        """
        - This Keyword Navigate to Reports on Manage Menu
        - Flow: Manage --> Reports
        - Keyword Usage:
         - ``Navigate To Manage Reports``

        :return: None
        """
        self.navigate_to_manage_tab()
        self.utils.print_info("Click on reports tab....")
        self.auto_actions.click_reference(self.get_manage_reports_nav)
        sleep(2)

    def navigate_to_policy_port_types(self):
        """
        - This Keyword Navigate to Port Types On Common Objects
        - Flow: CONFIGURE-->COMMON OBJECTS-->POLICIES-->PORT TYPES
        - Keyword Usage:
         - ``Navigate To Policy Port Types``

        :return: None
        """
        self.navigate_configure_common_objects()
        sleep(3)
        self.utils.print_info("Click on common Policy tab")
        self.navigate_to_common_object_policy_tab()

        self.utils.print_info("Click on Port Types tab...")
        self.auto_actions.click_reference(self.get_common_object_policy_port_types)
        sleep(5)

    def navigate_to_common_object_network_tab(self):
        """
        - This Keyword Navigate to Network Tab On Common Objects
        - Assumes that already navigated to the configure --> common object
        - Flow: Networks
        - Keyword Usage:
          - ``Navigate To Common Object Network Tab``

        :return: None
        """
        if not self.get_common_object_network_tab().is_selected():
            self.auto_actions.click_reference(self.get_common_object_network_tab)
            sleep(2)

    def navigate_to_network_subnetwork_space(self):
        """
        - This Keyword Navigate to SubNetwork Space Tab On Common Objects
        - Flow: CONFIGURE-->COMMON OBJECTS-->NETWORK-->Subnetwork Space
        - Keyword Usage:
         - ``Navigate To Network Subnetwork Space``

        :return: None
        """
        self.navigate_configure_common_objects()
        sleep(3)
        self.utils.print_info("Click on common object Network tab")
        self.navigate_to_common_object_network_tab()
        self.utils.print_info("Click on Subnetwork Space tab...")
        self.auto_actions.click_reference(self.get_common_object_network_sub_network_space)
        sleep(5)

    def navigate_to_common_object_basic_tab(self):
        """
        - This Keyword Navigate to Basic Tab On Common Objects
        - Assumes that already navigated to the configure --> common object
        - Flow: Basic
        - Keyword Usage:
         - ``Navigate To Common Object Basic Tab``

        :return: None
        """
        if not self.get_common_object_basic_tab().is_selected():
            self.auto_actions.click_reference(self.get_common_object_basic_tab)
            sleep(2)

    def navigate_to_basic_vlans_tab(self):
        """
        - This Keyword Navigate to Vlans Tabs On Common Objects
        - Flow: CONFIGURE-->COMMON OBJECTS-->BASIC-->VLAN's
        - Keyword Usage:
         - ``Navigate To Basic Vlans Tab``

        :return: None
        """
        self.navigate_configure_common_objects()
        sleep(3)
        self.utils.print_info("Click on common object Basic tab")
        self.navigate_to_common_object_basic_tab()
        self.utils.print_info("Click on Vlan tab...")
        self.auto_actions.click_reference(self.get_common_object_basic_vlans)
        sleep(5)

    def navigate_to_manage_alarms(self):
        """
        - This Keyword Navigate to Alarms on manage Menu
        - Flow: Manage --> Alarms
        - Keyword Usage:
         - `` Navigate To Manage Alarms``

        :return: None
        """
        self.navigate_to_manage_tab()
        sleep(5)
        self.utils.print_info("Click on Alarms tab..")
        self.auto_actions.click_reference(self.get_manage_alarms_nav)
        sleep(5)

    def navigate_to_client360(self):
        """
        - This Keyword Navigate to Client360 on ML Insights Menu
        - Flow: ML Insights --> Client 360
        - Keyword Usage:
         - ``Navigate To Client360``

        :return: None
        """
        self.navigate_to_ml_insight_tab()
        self.utils.print_info("Click on Client 360 tab..")
        self.auto_actions.click_reference(self.get_ml_insight_client360)
        sleep(5)

    def navigate_to_network360plan(self):
        """
        - This Keyword Navigate to network360plan on ML Insights Menu
        - Flow: ML Insights --> Network360Plan
        - Keyword Usage:
         - ``Navigate To Network360Plan``

        :return: None
        """
        self.navigate_to_ml_insight_tab()
        self.utils.print_info("Click on Network 360 tab..")
        self.auto_actions.click_reference(self.get_ml_insight_network360plan)
        sleep(5)

    def navigate_to_network360monitor(self):
        """
        - This Keyword Navigate to network360monitor on ML Insights Menu
        - Flow: ML Insights --> Network360Monitor
        - Keyword Usage:
         - ``Navigate To Network360Monitor``

        :return: None
        """
        self.navigate_to_ml_insight_tab()
        self.utils.print_info("Click on Network 360 Monitor tab..")
        self.auto_actions.click_reference(self.get_ml_insight_network360monitor)
        sleep(5)

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
        :return: 1
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
        :return: 1
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
        sleep(6)
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
        sleep(4)
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
        :return:
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
        self.auto_actions.click(self.weh.get_element(self.device_actions_advanced_cli_access))
        sleep(5)
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
        :return:
        """
        self.navigate_to_devices()
        self.device_common.select_device_row(device_serial)

        self.utils.print_info("Clicking on Utilities")
        self.auto_actions.click_reference(self.get_device_utilities)
        sleep(2)

        self.utils.print_info("Hovering over Status button")
        status_element = self.weh.get_element(self.device_utilities_status)
        self.auto_actions.move_to_element(status_element)
        sleep(5)

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
        :return: 1
        """
        self.navigate_to_devices()
        self.device_common.select_device_row(device_serial)

        self.utils.print_info("Clicking on Utilities")
        self.auto_actions.click_reference(self.get_device_utilities)
        sleep(2)

        self.utils.print_info("Hovering over Status button")
        status_element = self.weh.get_element(self.device_utilities_status)
        self.auto_actions.move_to_element(status_element)
        sleep(5)

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
        :return: 1
        """
        self.navigate_to_devices()
        self.device_common.select_device_row(device_serial)

        self.utils.print_info("Clicking on Utilities")
        self.auto_actions.click_reference(self.get_device_utilities)
        sleep(2)

        self.utils.print_info("Hovering over Status button")
        status_element = self.weh.get_element(self.device_utilities_status)
        self.auto_actions.move_to_element(status_element)
        sleep(5)

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
        :return: None
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
        sleep(2)

    def navigate_to_api_token_mngment(self):
        """
        - This keyword is used to navigate the "API Token Management"
        - Flows XIQ User Menu(Account Info) --> Global Settings --> API Token Management
        - Keyword Usage:
         - ``Navigate To Api Token Mngment``

        :return: None
        """
        self.navigate_to_global_settings_page()
        self.utils.print_info("Click on api token management tab")
        self.auto_actions.click_reference(self.get_api_token_mgmt_tab)
        sleep(5)

    def navigate_a3_inventory(self):
        """
        - This Keyword Navigate to A3 --> Inventory
        - Flow: A3--->Inventory
        - Keyword Usage
          - ``Navigate A3 Inventory``

        :return: 1 if Navigation Successful to Inventory tab on A3 Menu
        """
        self.utils.print_info("Selecting A3 Tab...")
        self.auto_actions.click_reference(self.get_a3_tab)
        sleep(2)

        self.utils.print_info("Selecting Inventory on A3 Page...")
        self.auto_actions.click_reference(self.get_a3_inventory_tab)
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
        self.utils.print_info("Selecting Extreme AirDefence Menu...")
        self.auto_actions.click_reference(self.get_air_defence_menu)
        sleep(5)

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

    def navigate_to_configuration_tab(self):
        """
         - This keyword Navigates to Configuration Tab
         - Keyword Usage
          - ``Navigate To Configuration Tab``

        :return: 1 if Navigation Successful to Configuration Tab else return -1
        """
        self.utils.print_info("Selecting Configuration Tab...")
        if self.auto_actions.click_reference(self.get_configuration_tab) == 1:
            sleep(2)
            return 1
        else:
            self.utils.print_info("Unable to navigate to Configuration tab")
            self.screen.save_screen_shot()
            return -1

    def navigate_to_tools_tab(self):
        """
         - This keyword Navigates to Tools Tab
         - Keyword Usage
          - ``Navigate To Tools Tab``

        :return: 1 if Navigation Successful to Tools Tab else return -1
        """
        self.utils.print_info("Selecting Configuration Tab...")
        if self.auto_actions.click_reference(self.get_tools_tab) == 1:
            sleep(2)
            return 1
        else:
            self.utils.print_info("Unable to navigate to Tools tab")
            self.screen.save_screen_shot()
            return -1

    def select_ssh(self):
        """
         - This keyword selects SSH option in Tools Page
         - Keyword Usage
          - ``Selects SSH option in Tools Page``

        :return: 1 if Navigation Successful to SSH Option else return -1
        """
        import sys
        import pdb
        pdb.Pdb(stdout=sys.__stdout__).set_trace()
        self.utils.print_info("Clicking SSH menu")
        #driver = webdriver.chrome()
        #self.driver.implicitly_wait(10)
        element = self.weh.get_element(self.ssh_option_ui)
        self.auto_actions.click(element)
        sleep(5)


        #self.utils.print_info("Selecting SSH option...")
        #if self.auto_actions.click_reference(self.get_ssh_option_ui) == 1:
        wait = WebDriverWait(self.driver, 17)
        #sleep(10)
        self.utils.print_info("After WebDriverWait")
        #self.utils.print_info("After sleep(10)")
        #ssh_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name ='check-button']")))
        #xpath = "//*[@id='__BVID__280']"
        xpath = "/html/body/div/div[2]/div[2]/div/div[2]/div/div/div/form/div[3]/div/div/label"
        #ssh_btn = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        ssh_btn = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        self.utils.print_info("After wait.until")
        self.driver.execute_script("arguments[0].scrollIntoView();",ssh_btn)
        self.utils.print_info("After ScrollIntoView")
        ssh_btn.click()
        self.utils.print_info("After click")
        #self.auto_actions.click_reference(self.a3_web_elements.get_ssh_button)
        sleep(2)
        return 1
        #else:
          #  self.utils.print_info("Unable to navigate to SSH option")
          #  self.screen.save_screen_shot()
          #  return -1



    def switch_policies_access_control(self):
        """
         - This keyword switches to Policies & Access Control
         - Keyword Usage
          - ``Switch To Policies Access Control``

        :return: 1 if Navigation Successful to Policies & Access Control else return -1
        """
        self.utils.print_info("Selecting Onboard Tab...")
        if self.auto_actions.click_reference(self.get_policies_access_control) == 1:
            sleep(2)
            return 1
        else:
            self.utils.print_info("Unable to navigate to Policies & Access control")
            self.screen.save_screen_shot()
            return -1

    def switch_system_configuration(self):
        """
         - This keyword switches to System Configuration Page
         - Keyword Usage
          - ``Switch To System Configuration Page``

        :return: 1 if Navigation Successful to System Configuration else return -1
        """
        self.utils.print_info("Selecting System Configuration...")
        if self.auto_actions.click_reference(self.get_system_configuration) == 1:
            sleep(2)
            return 1
        else:
            self.utils.print_info("Unable to navigate to System Configuration")
            self.screen.save_screen_shot()
            return -1

    def select_cloud_integration(self):

        """
            - This keyword select the Cloud Integration from the menu System Configuration
            - Keyword Usage
             - ``Select cloud integration``

        :return: 1 if Navigation Successful to Cloud Integration else return -1
        """
        self.utils.print_info("Selecting Cloud Integration from menu...")

        if self.auto_actions.click_reference(self.get_cloud) == 1:
            sleep(2)
            self.utils.print_info("Entering Cloud account details ")
            element1 = self.weh.get_element(self.cloud_host_input)
            element1.clear()
            self.auto_actions.send_keys(element1,'https://g2.qa.xcloudiq.com')
            sleep(5)
            element2 = self.weh.get_element(self.cloud_admin)
            self.auto_actions.send_keys(element2,"testrach17+g2account1@gmail.com")
            sleep(5)
            element3 = self.weh.get_element(self.cloud_password)
            self.auto_actions.send_keys(element3,"Extreme123")
            sleep(5)
            element4 = self.weh.get_element(self.cloud_link_button)
            self.auto_actions.click(element4)
            sleep(20)
            element5 = self.weh.get_element(self.cloud_unlink_button)
            self.auto_actions.click(element5)
            sleep(10)

            return 1
        else:
            self.utils.print_info("Unable to navigate to Cloud Integration")
            self.screen.save_screen_shot()
            return -1

    def ssh_button(self):

        """
            - This keyword select the SSH checkbox and click it
            - Keyword Usage
             - ``Select SSH Checkbox``

        :return: 1 if Navigation Successful to SSH checkbox else return -1
        """

        #self.auto_actions.enable_check_box(self.get_ssh_button())
        #self.utils.print_info("Selecting Enable SSH label...")
        #ssh_btn = self.weh.get_element(self.ssh_selector)
        self.driver.find_element_by_name("check-button").click()

        #self.auto_actions.click_reference(self.a3_web_elements.get_ssh_button)
        #ssh_btn = self.weh.get_element(self.ssh_selector)
        #ssh_btn.click()
        #self.getElementsByName('check-button')[0].click()
        #abc.click()

        #self.auto_actions.move_to_element(ssh_btn)

        #self.auto_actions.enable_check_box(ssh_btn)
        #self.utils.print_info("selected the option finally")

        #self.auto_actions.click(ssh_btn)
        sleep(10)
        return 1


    def ssh_page_entries(self):
        """
        - This keyword will enter the values into SSH page tools
        - Keyword Usage
        - ``SSH Page Inputs``

        :return: 1 if Navigation Successful to SSH inputs else return -1
        """

        ssh_drop = self.weh.get_element(self.select_duration)
        self.auto_actions.click(ssh_drop)
        sleep(5)
        self.utils.print_info("Selected Drop Down")
        self.utils.print_info(ssh_drop)
        #self.utils.print_info(type(ssh_drop))
        drop_options = self.weh.get_elements(self.input_drop_down_options)
        #self.utils.print_info(drop_options)
        self.auto_actions.select_drop_down_options(drop_options,"5 days")
        sleep(5)
        ssh_pwd = self.weh.get_element(self.ssh_password)
        self.auto_actions.send_keys(ssh_pwd,"Extr123")
        sleep(5)
        ssh_save = self.weh.get_element(self.ssh_save_button)
        self.auto_actions.click(ssh_save)
        sleep(5)
        return 1

    def select_roles(self):
        """
            - This keyword select the Roles from the menu Policies and Access Control
            - Keyword Usage
             - ``Select roles``

        :return: 1 if Navigation Successful to Roles else return -1
        """
        self.utils.print_info("Selecting Roles from menu...")

        if self.auto_actions.click_reference(self.get_roles) == 1:
            sleep(2)
            self.utils.print_info("Clicking New Roles ")
            element = self.weh.get_element(self.role_button)
            self.auto_actions.click(element)
            sleep(5)

            element1 = self.weh.get_element(self.name_input)
            self.auto_actions.send_keys(element1,"testRole3")
            sleep(5)
            element2 = self.weh.get_element(self.create_button)
            self.auto_actions.click(element2)
            sleep(10)
            element3 = self.weh.get_element(self.save_button)
            self.auto_actions.click(element3)
            sleep(5)
            #element4 = self.weh.get_element(self.close_button)
            #self.auto_actions.click(element4)
            sleep(5)
            return 1
        else:
            self.utils.print_info("Unable to navigate to Roles")
            self.screen.save_screen_shot()
            return -1

    def select_active_directory_domains(self):
        """
            - This keyword select the Active Directory Domains from the menu Policies and Access Control
            - Keyword Usage
             - ``Select Active Directory Domains``

        :return: 1 if Navigation Successful to Roles else return -1
        """
        self.utils.print_info("Selecting Active Directory Domains from menu...")

        if self.auto_actions.click_reference(self.get_ad_domains) == 1:
            sleep(2)
            self.utils.print_info("Creating domain ")
            element = self.weh.get_element(self.domain_button)
            self.auto_actions.click(element)
            sleep(5)
            element1 = self.weh.get_element(self.identifier_input)
            self.auto_actions.send_keys(element1,"ad240")
            sleep(5)
            element2 = self.weh.get_element(self.workgroup_input)
            self.auto_actions.send_keys(element2,"amra3")
            sleep(5)
            element3 = self.weh.get_element(self.dns_name_input)
            self.auto_actions.send_keys(element3,"amra3.local")
            sleep(10)
            element4 = self.weh.get_element(self.ad_server_input)
            self.auto_actions.send_keys(element4,"10.234.63.27")
            sleep(10)
            element5 = self.weh.get_element(self.dns_server_input)
            self.auto_actions.send_keys(element5,"10.234.63.27")
            sleep(10)
            element6 = self.weh.get_element(self.create_join_button)
            self.auto_actions.click(element6)
            sleep(10)
            #element7 = self.weh.get_element(self.join_ad_domain_username)
            #self.auto_actions.click(element7,"Administrator")
            #sleep(5)
            #element8 = self.weh.get_element(self.join_ad_domain_password)
            #self.auto_actions.click(element8,"Legend123")
            #sleep(5)
            #element9 = self.weh.get_element(self.join_ad)
            #self.auto_actions.click(element9)
            #sleep(10)

            return 1
        else:
            self.utils.print_info("Unable to navigate to Active Directory")
            self.screen.save_screen_shot()
            return -1
