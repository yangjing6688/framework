from time import sleep
import re

from extauto.common.Screen import Screen
# from extauto.common.CloudDriver import CloudDriver
from extauto.common.AutoActions import AutoActions
from extauto.common.Utils import Utils
from extauto.common.CommonValidation import CommonValidation

import extauto.xiq.flows.common.ToolTipCapture as tool_tip
from extauto.xiq.flows.configure.NetworkPolicy import NetworkPolicy
from extauto.xiq.flows.configure.CommonObjects import CommonObjects
from extauto.xiq.flows.common.Navigator import Navigator

from extauto.xiq.elements.WipsWebElements import WipsWebElements
from extauto.xiq.elements.DeviceTemplateWebElements import DeviceTemplateWebElements
from extauto.xiq.elements.NetworkPolicyWebElements import NetworkPolicyWebElements
from extauto.xiq.elements.CommonObjectsWebElements import CommonObjectsWebElements


class Wips(WipsWebElements):

    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        # self.driver = extauto.common.CloudDriver.cloud_driver
        self.navigator = Navigator()
        self.device_template_web_elements = DeviceTemplateWebElements()
        self.wips_web_elements = WipsWebElements()
        self.cobj_web_elements = CommonObjectsWebElements()
        self.np_web_elements = NetworkPolicyWebElements()
        self.network_policy = NetworkPolicy()
        self.common_object = CommonObjects()
        self.screen = Screen()
        self.common_validation = CommonValidation()

    def navigate_to_network_policy_edit_tab(self, policy_name):
        """
        - Navigates to Network Policies List and Edit the Specific Network Policy
        - Flow  Network policy list-->Select List View-->Select Network Policy ROW--> Edit
        - Keyword Usage
        - ``Navigate To Network Policy Edit Tab  ${NETWORK_POLICY_NAME}``

        :param policy_name: Network Policy Name
        :return:1 if Navigates to Network Policy edit
        """
        self.navigator.navigate_configure_network_policies()

        self.utils.print_info("Click on network policy list view button")
        self.auto_actions.click_reference(self.np_web_elements.get_network_policy_list_view)
        sleep(2)

        self.utils.print_info("Select the network policy rows")
        self.network_policy.select_network_policy_row(policy_name)

        self.utils.print_info("Click on network policy Edit button")
        self.auto_actions.click_reference(self.np_web_elements.get_np_edit_button)
        sleep(2)
        return 1

    def enable_wips_on_network_policy(self, policy_name, wips_name, **kwargs):
        """
        - Enable wips on Network Policy
        - Flow  Network policy list--->Select Network Policy Edit---> Additional Settings--->Security-->WIPS
        - Keyword Usage
        - ``Enable Wips On Network Policy  ${NETWORK_POLICY_NAME}   ${WIPS_POLICY_NAME}``

        :param policy_name: Network Policy Name
        :param wips_name: WIPS Policy Name
        :return: 1 if WIPS Policy enabled Successfully on Network Policy else -1
        """
        self.utils.print_info("Select the Network Policy to enable WIPS")
        self.navigate_to_network_policy_edit_tab(policy_name)

        self.utils.print_info("Click on Additional Settings tab button")
        self.auto_actions.click_reference(self.get_network_policy_additional_settings_tab)
        sleep(2)

        if self.get_network_policy_additional_settings_wips_menu_option().is_displayed():
            self.utils.print_info("Click WIPS Menu On Security Tab")
            self.auto_actions.click_reference(self.get_network_policy_additional_settings_wips_menu_option)
        else:
            self.utils.print_info("Click Security Tab")
            self.auto_actions.click_reference(self.get_network_policy_additional_settings_security_option)
            sleep(2)
            self.utils.print_info("Click WIPS Menu")
            self.auto_actions.click_reference(self.get_network_policy_additional_settings_wips_menu_option)

        self.utils.print_info("Click on Enable WIPS button")
        self.auto_actions.click_reference(self.get_network_policy_additional_settings_enable_wips_button)
        sleep(2)

        self.utils.print_info("Enter WIPS Name")
        self.auto_actions.send_keys(self.get_network_policy_additional_settings_wips_name_field(), wips_name)
        sleep(3)

        self.utils.print_info("Click on Save button")
        self.auto_actions.click_reference(self.get_wips_save_button)
        sleep(2)

        tool_tip_text = tool_tip.tool_tip_text
        self.utils.print_info("Tool tip Text Displayed on Page", tool_tip_text)
        if "WIPS was updated successfully." in tool_tip_text:
            kwargs['pass_msg'] = "WIPS was updated successfully."
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "enable_wips_on_network_policy() failed. Failed to enable WIPS Policy"
            self.common_validation.failed(**kwargs)
            return -1

    def configure_wips_options_on_network_policy(self, policy_name, **wips_config_profile):
        """
        - Creates WIPS Policy On Network Policy based on the arguments from wireless_networks_config.robot
        - Flow  Network policy list--->Select Network Policy Edit---> Additional Settings--->Security-->WIPS
        - Keyword Usage
        - ``Configure WIPS Options On Network Policy  ${NW_POLICY_NAME}   &{WIPS_CONFIG_SETTINGS}``

        :param policy_name: Network Policy Name
        :param wips_config_profile: (dict) include status of rougue ap detection, detect rogue ap based on Mac and ssid.
        :return:1 if WIPS Policy Options Configured on Network Policy else -1
        """
        rougue_ap_detection = wips_config_profile.get('rougue_ap_detection', 'Enable')
        detect_rougue_ap_wired = wips_config_profile.get('detect_ap_wired', 'Enable')
        detect_ap_mac_oui_basis = wips_config_profile.get('detect_ap_mac_oui_basis', 'Enable')
        detect_ap_ssid_basis = wips_config_profile.get('detect_ap_ssid_basis', 'Disable')
        detect_client_form_adhoc = wips_config_profile.get('detect_client_form_adhoc', 'Enable')
        rougue_client_reporting = wips_config_profile.get('rougue_client_reporting', 'Disable')
        mitigation_mode = wips_config_profile.get('mitigation_mode', 'manual')

        self.utils.print_info("Select the Network Policy to enable WIPS")
        self.navigate_to_network_policy_edit_tab(policy_name)

        self.utils.print_info("Click on Additional Settings tab button")
        self.auto_actions.click_reference(self.get_network_policy_additional_settings_tab)
        sleep(2)

        if self.get_network_policy_additional_settings_wips_menu_option().is_displayed():
            self.utils.print_info("Click WIPS Menu On Security Tab")
            self.auto_actions.click_reference(self.get_network_policy_additional_settings_wips_menu_option)
        else:
            self.utils.print_info("Click Security Tab")
            self.auto_actions.click_reference(self.get_network_policy_additional_settings_security_option)
            sleep(2)
            self.utils.print_info("Click WIPS Menu")
            self.auto_actions.click_reference(self.get_network_policy_additional_settings_wips_menu_option)

        if rougue_ap_detection.upper() == "ENABLE":
            self.utils.print_info("Enable Rogue Access Point Detection")
            if not self.get_wips_rogue_ap_detection_button().is_selected():
                self.auto_actions.click_reference(self.get_wips_rogue_ap_detection_button())
                sleep(5)
        else:
            self.utils.print_info("Disable Rogue Access Point Detection")
            if self.get_wips_rogue_ap_detection_button().is_selected():
                self.auto_actions.click_reference(self.get_wips_rogue_ap_detection_button)
                sleep(5)

        if detect_rougue_ap_wired.upper() == "ENABLE":
            self.utils.print_info("Enable Determine if detected rogue APs are connected to your wired network")
            if not self.get_determine_wips_enable_same_network_checkbox().is_selected():
                self.auto_actions.click_reference(self.get_determine_wips_enable_same_network_checkbox)
                sleep(5)
        else:
            self.utils.print_info("Disable Determine if detected rogue APs are connected to your wired network")
            if self.get_determine_wips_enable_same_network_checkbox().is_selected():
                self.auto_actions.click_reference(self.get_determine_wips_enable_same_network_checkbox)
                sleep(5)

        if detect_ap_mac_oui_basis.upper() == "ENABLE":
            self.utils.print_info("Enable Detect rogue access points based on their MAC OUI")
            if not self.get_wips_rogue_ap_mac_oui_detection_checkbox().is_selected():
                self.auto_actions.click_reference(self.get_wips_rogue_ap_mac_oui_detection_checkbox)
                sleep(5)
        else:
            self.utils.print_info("Disable Detect rogue access points based on their MAC OUI")
            if self.get_wips_rogue_ap_mac_oui_detection_checkbox().is_selected():
                self.auto_actions.click_reference(self.get_wips_rogue_ap_mac_oui_detection_checkbox)
                sleep(5)

        if detect_ap_ssid_basis.upper() == "ENABLE":
            self.utils.print_info("Enable Detect rogue access points based on hosted SSIDs and encryption type")
            if not self.get_wips_enable_rogue_ssid_detection_checkbox().is_selected():
                self.auto_actions.click_reference(self.get_wips_enable_rogue_ssid_detection_checkbox)
                sleep(5)
        else:
            self.utils.print_info("Disable Detect rogue access points based on hosted SSIDs and encryption type")
            if self.get_wips_enable_rogue_ssid_detection_checkbox().is_selected():
                self.auto_actions.click_reference(self.get_wips_enable_rogue_ssid_detection_checkbox)
                sleep(5)

        if detect_client_form_adhoc.upper() == "ENABLE":
            self.utils.print_info("Enable Detect if clients have formed an ad hoc network to identify rogue clients")
            if not self.get_wips_enable_adhoc_network_detection_button().is_selected():
                self.auto_actions.click_reference(self.get_wips_enable_adhoc_network_detection_button)
                sleep(5)
        else:
            self.utils.print_info("Disable Detect if clients have formed an ad hoc network to identify rogue clients")
            if self.get_wips_enable_adhoc_network_detection_button().is_selected():
                self.auto_actions.click_reference(self.get_wips_enable_adhoc_network_detection_button)
                sleep(5)

        if rougue_client_reporting.upper() == "ENABLE":
            self.utils.print_info("Enable rogue client reporting Checkbox")
            if not self.get_wips_enable_rogue_client_reporting_checkbox().is_selected():
                self.auto_actions.click_reference(self.get_wips_enable_rogue_client_reporting_checkbox)
                sleep(5)
        else:
            self.utils.print_info("Disable rogue client reporting Checkbox")
            if self.get_wips_enable_rogue_client_reporting_checkbox().is_selected():
                self.auto_actions.click_reference(self.get_wips_enable_rogue_client_reporting_checkbox)
                sleep(5)

        if mitigation_mode.upper() == "MANUAL":
            self.utils.print_info("Enable Mitigation Mode as Manual")
            self.auto_actions.click_reference(self.get_wips_mitigation_mode_manual_radio_button)
            sleep(5)
        else:
            self.utils.print_info("Enable Mitigation Mode as Automatic")
            self.auto_actions.click_reference(self.get_wips_mitigation_mode_automatic_radio_button)
            sleep(5)

        self.utils.print_info("Click on Save button")
        self.auto_actions.click_reference(self.get_wips_save_button)
        sleep(2)

        tool_tip_text = tool_tip.tool_tip_text
        self.utils.print_info("Tool tip Text Displayed on Page", tool_tip_text)
        if "WIPS was updated successfully." in tool_tip_text:
            return 1
        else:
            return -1

    def add_allowed_ssid_on_network_wips_policy(self, policy_name, ssid_name, auth_type, **kwargs):
        """
        - Configure Allowed SSID and Encryption Type on WIPS Policy
        - Flow  Network policy list--->Select Network Policy Edit---> Additional Settings--->Security-->WIPS-->
                 Enable Detect Rogue Based on SSID and Encryption Type
        - Keyword Usage
        - ``Add Allowed SSID On Network WIPS Policy  ${NW_POLICY_NAME}  ${SSID_NAME}  ${AUTH_TYPE}``

        :param policy_name: Network Policy Name
        :param ssid_name: SSID Name to Allow on WIPS Policy Configured
        :param auth_type: Encryption Type ie OPEN Authentication
        :return:1 if Allowed SSID configured On WIPS Policy else -1
        """
        self.utils.print_info("Select the Network Policy to enable WIPS")
        self.navigate_to_network_policy_edit_tab(policy_name)

        self.utils.print_info("Click on Additional Settings tab button")
        self.auto_actions.click_reference(self.get_network_policy_additional_settings_tab)
        sleep(2)

        if self.get_network_policy_additional_settings_wips_menu_option().is_displayed():
            self.utils.print_info("Click WIPS Menu On Security Tab")
            self.auto_actions.click_reference(self.get_network_policy_additional_settings_wips_menu_option)
        else:
            self.utils.print_info("Click Security Tab")
            self.auto_actions.click_reference(self.get_network_policy_additional_settings_security_option)
            sleep(2)
            self.utils.print_info("Click WIPS Menu")
            self.auto_actions.click_reference(self.get_network_policy_additional_settings_wips_menu_option)

        self.utils.print_info("Enable Detect rogue access points based on hosted SSIDs and encryption type")
        if not self.get_wips_enable_rogue_ssid_detection_checkbox().is_selected():
            self.auto_actions.click_reference(self.get_wips_enable_rogue_ssid_detection_checkbox)
            sleep(5)

        self.utils.print_info("Click on SSID add sign button")
        self.auto_actions.click_reference(self.get_wips_enable_rogue_ssid_detection_add_sign_button)
        sleep(2)

        self.utils.print_info("Click on Enter SSID Name Radio button")
        self.auto_actions.click_reference(self.get_wips_enter_ssid_name_radio_button)
        sleep(2)

        self.utils.print_info("Enter SSID Name Allowed in WLAN")
        self.auto_actions.send_keys(self.get_wips_wips_enter_ssid_name_text_field(), ssid_name)
        sleep(2)

        self.utils.print_info("Enable Encrption Type selection Checkbox")
        self.auto_actions.click_reference(self.get_wips_select_ssid_encryption_type_checkbox)
        sleep(2)

        self.utils.print_info("Click Authentication scroll down box")
        self.auto_actions.click_reference(self.get_wips_select_ssid_encryption_scroll_button)
        sleep(2)

        self.utils.print_info("Select Authentication Type")
        auth_type_items = self.get_authtype_drop_down_items()
        for item in auth_type_items:
            if auth_type.upper() in item.text.upper():
                self.utils.print_info("Selecting Authentication Type from drop down")
                self.auto_actions.click(item)
                sleep(2)
                break

        self.utils.print_info("Click Add SSID Button")
        self.auto_actions.click_reference(self.get_wips_select_ssid_encryption_add_button)
        sleep(2)

        self.utils.print_info("Click on Save button")
        self.auto_actions.click_reference(self.get_wips_save_button)
        sleep(2)

        tool_tip_text = tool_tip.tool_tip_text
        self.utils.print_info("Tool tip Text Displayed on Page", tool_tip_text)
        if "WIPS was updated successfully." in tool_tip_text:
            kwargs['pass_msg'] = "WIPS was updated successfully"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "add_allowed_ssid_on_network_wips_policy() failed. Failed to update wips policy"
            self.common_validation.failed(**kwargs)
            return -1

    def select_allowed_mac_oui_on_network_wips_policy(self, policy_name, mac_oui_name, **kwargs):
        """
        - Select allowed MAC OUI on Network Wips Policy
        - Flow  Network policy list--->Select Network Policy Edit---> Additional Settings--->Security-->WIPS-->
                 Enable Detect Rogue Based on MAC OUI
        - Keyword Usage
        - ``Select Allowed Mac OUI On Network Wips Policy    ${NW_POLICY_NAME}   ${MAC_OUI}``

        :param policy_name: Network Policy Name
        :param mac_oui_name: MAC OUI Name to Allow on WIPS Policy
        :return:1 if Allowed MAC OUI configured On WIPS Policy else -1
        """
        self.utils.print_info("Select the Network Policy to enable WIPS")
        self.navigate_to_network_policy_edit_tab(policy_name)

        self.utils.print_info("Click on Additional Settings tab button")
        self.auto_actions.click_reference(self.get_network_policy_additional_settings_tab)
        sleep(2)

        if self.get_network_policy_additional_settings_wips_menu_option().is_displayed():
            self.utils.print_info("Click WIPS Menu On Security Tab")
            self.auto_actions.click_reference(self.get_network_policy_additional_settings_wips_menu_option)
        else:
            self.utils.print_info("Click Security Tab")
            self.auto_actions.click_reference(self.get_network_policy_additional_settings_security_option)
            sleep(2)
            self.utils.print_info("Click WIPS Menu")
            self.auto_actions.click_reference(self.get_network_policy_additional_settings_wips_menu_option)

        self.utils.print_info("Enable Detect rogue access points based on their MAC OUI")
        if not self.get_wips_rogue_ap_mac_oui_detection_checkbox().is_selected():
            self.auto_actions.click_reference(self.get_wips_rogue_ap_mac_oui_detection_checkbox)
            sleep(5)

        self.utils.print_info("Select All checkboxes for MAC OUI")
        self.auto_actions.click_reference(self.get_wips_mac_oui_select_all_checkbox_list)
        sleep(2)

        self.utils.print_info("Click Delete Button")
        self.auto_actions.click_reference(self.get_wips_mac_oui_delete_symbol_button)
        sleep(2)

        self.utils.print_info("Click on Mac OUI add sign button")
        self.auto_actions.click_reference(self.get_wips_select_mac_ouis_of_wireless_add_sign)
        sleep(2)

        self.utils.print_info("Click Mac OUI scroll down box")
        self.auto_actions.click_reference(self.get_wips_select_mac_oui_scroll_button)
        sleep(2)

        self.utils.print_info("Selecting Mac OUI from the list")
        mac_oui_items = self.get_wips_select_mac_oui_drop_down_items()
        for item in mac_oui_items:
            if mac_oui_name.upper() in item.text.upper():
                self.utils.print_info("Selecting Mac OUI from drop down")
                self.auto_actions.click(item)
                sleep(2)
                break
        """
        In Case need to select device in the grid

        self.utils.print_info("Selecting Device with MAC: ", mac_oui_name)
        rows = self.get_wips_mac_oui_grid_rows()
        for row in rows:
            if mac_oui_name in row.text:
                self.utils.print_debug("Found MAC OUI Row: ", row.text)
                self.auto_actions.click(self.get_wips_mac_oui_select_checkbox(row))
                sleep(2)
                break
        """
        self.utils.print_info("Click Add MAC OUI Button")
        self.auto_actions.click_reference(self.get_wips_add_mac_oui_button)
        sleep(2)

        self.utils.print_info("Click on Save button")
        self.auto_actions.click_reference(self.get_wips_save_button)
        sleep(2)

        tool_tip_text = tool_tip.tool_tip_text
        self.utils.print_info("Tool tip Text Displayed on Page", tool_tip_text)
        if "WIPS was updated successfully." in tool_tip_text:
            kwargs['pass_msg'] = "WIPS was updated successfully."
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "select_allowed_mac_oui_on_network_wips_policy() failed. Failed to update wips policy"
            self.common_validation.failed(**kwargs)
            return -1

    def configure_wips_policy_on_common_objects(self, wips_policy_name, **kwargs):
        """
        - Configure WIPS Policy On Common Objects.
        - Flow  Configure--->Common Objects--->Security-->WIPS Policies--> Add
        - Keyword Usage
        - ``Configure WIPS Policy On Common Objects   {WIPS_POLICY_NAME}``

        :param  wips_policy_name : WIPS Policy Name
        :return: 1 if WIPS POlicy Created on Common Objects else -1
        """

        self.utils.print_info("Navigate to Common Objects---> Security--->WIPS Policies")
        self.navigator.navigate_to_security_wips_policies()
        sleep(2)

        self.utils.print_info("Click on Add button")
        self.auto_actions.click_reference(self.get_wips_common_object_add_button)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Enter WIPS Policy Name")
        self.auto_actions.send_keys(self.get_wips_common_object_policy_name_textfield(), wips_policy_name)
        sleep(3)

        self.utils.print_info("Enter WIPS Policy Description")
        self.auto_actions.send_keys(self.get_wips_common_object_policy_description_textfield(), wips_policy_name)
        self.screen.save_screen_shot()
        sleep(3)

        self.utils.print_info("Enable Wireless Threat Detection")
        if not self.get_wips_common_object_policy_wireless_threat_detection_button().is_selected():
            self.auto_actions.click_reference(self.get_wips_common_object_policy_wireless_threat_detection_button)
            sleep(5)
        else:
            self.utils.print_info("Wireless Threat Detection Already Enabled in WIPS Policy by Default")

        self.utils.print_info("Click on Save button")
        self.auto_actions.click_reference(self.get_wips_common_object_save_button)
        sleep(2)

        self.utils.print_info("Checking the Save profile message...")
        observed_profile_message = self.wips_web_elements.get_wips_profile_save_tool_tip().text
        self.utils.print_info("Observed Message: ", observed_profile_message)

        self.screen.save_screen_shot()
        sleep(2)

        if "WIPS was updated successfully" in observed_profile_message:
            kwargs['pass_msg'] = "WIPS was updated successfully"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "configure_wips_policy_on_common_objects() failed. Failed to update wips policy"
            self.common_validation.failed(**kwargs)
            return -1

    def configure_allowed_ssid_on_wips_policy(self, **wips_ssid_config):
        """
        - Configure Allowed SSID and Encryption Type on WIPS Policy On Common Objects.
        - Flow  Common Objects-->WIPS--> Click Add Button on Enable Detect Rogue Based on SSID Name and Encryption Type
        - Keyword Usage
        - ``Configure Allowed Ssid On Wips Policy   &{WIPS_SSID_CONFIG}``

        :param  wips_ssid_config : (dict) include allowed_ssid, authentication_type
        :return: 1 if SSID and Encryption type added on WIPS Policy on Common Objects else -1
        """
        ssid_name = wips_ssid_config.get('allowed_ssid')
        auth_type = wips_ssid_config.get('authentication_type')

        self.utils.print_info("Click on SSID add sign button")
        self.auto_actions.click_reference(self.get_wips_common_object_enable_rogue_ssid_detection_add_sign_button)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Click on Enter SSID Name Radio button")
        self.auto_actions.click_reference(self.get_wips_enter_ssid_name_radio_button)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Enter SSID Name Allowed in WLAN")
        self.auto_actions.send_keys(self.get_wips_common_object_enter_ssid_name_text_field(), ssid_name)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Enable Encrption Type selection Checkbox")
        self.auto_actions.click_reference(self.get_wips_select_ssid_encryption_type_checkbox)
        sleep(2)

        self.utils.print_info("Click Authentication scroll down box")
        self.auto_actions.click_reference(self.get_wips_select_ssid_encryption_scroll_button)
        sleep(2)

        self.utils.print_info("Select Authentication Type")
        auth_type_items = self.get_authtype_drop_down_items()
        for item in auth_type_items:
            if auth_type.upper() in item.text.upper():
                self.utils.print_info("Selecting Authentication Type from drop down")
                self.auto_actions.click(item)
                sleep(2)
                break

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Click Add SSID Button")
        self.auto_actions.click_reference(self.get_wips_common_object_select_ssid_encryption_add_button)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        return True

    def navigate_to_network_policy_wips_tab(self, nw_policy):
        """
        - To Navigate to Existing Network Policy --->Router Settings --> Security--> WIPS
        - Flow  Configure--> Network policy list--->Select Network Policy Edit---> Router Settings --> Security--> WIPS
        - Keyword Usage
        - ``Navigate To Network Policy Wips Tab  ${NW_POLICY_NAME}``

        :param  nw_policy: Network Policy Name
        :return:1 if Navigated to Existing Network Policy Router Settings WIPS Tab else -1
        """
        self.utils.print_info("Navigating Network Policies")
        self.navigator.navigate_configure_network_policies()
        sleep(1)

        self.utils.print_info("Edit Network Policy")
        self.network_policy.select_network_policy_in_card_view(nw_policy)
        sleep(2)

        self.utils.print_info("Click on Additional Settings tab button")
        self.auto_actions.click_reference(self.get_network_policy_additional_settings_tab)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        self.auto_actions.scroll_down()
        sleep(2)

        self.auto_actions.scroll_down()
        sleep(2)

        if self.get_network_policy_additional_settings_wips_menu_option().is_displayed():
            self.utils.print_info("Click WIPS Menu On Security Tab")
            self.auto_actions.scroll_down()
            self.auto_actions.click_reference(self.get_network_policy_additional_settings_wips_menu_option)
            sleep(2)
        else:
            self.utils.print_info("Click Security Tab")
            self.auto_actions.click_reference(self.get_network_policy_additional_settings_security_option)
            sleep(2)
            self.utils.print_info("Click WIPS Menu")
            self.auto_actions.click_reference(self.get_network_policy_additional_settings_wips_menu_option)
            sleep(2)

        if not self.get_enable_wips_button().is_selected():
            self.utils.print_info("Click on Enable WIPS button")
            self.auto_actions.click_reference(self.get_enable_wips_button)
            sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        return True

    def configure_reuse_wips_policy_on_network_policy(self, nw_policy, wips_policy_name, **kwargs):
        """
        - Select the Configured WIPS Policy on Network Policy
        - Flow  Configure--> Network policy Name Edit---> Router Settings --> Security--> WIPS--> Reuse WIPS Policy
        - Keyword Usage
        - ``Configure Reuse Wips Policy On Network Policy  ${NW_POLICY_NAME}  ${WIPS_POLICY_NAME}``

        :param nw_policy: network policy name
        :param wips_policy_name: wips policy name
        :return: return 1 if WIPS Policy Name selected and applied successfully on Network Policy else -1
        """

        self.utils.print_info("Navigate to Network Policy-->Additional Settings-->WIPS")
        self.navigate_to_network_policy_wips_tab(nw_policy)
        sleep(5)

        self.utils.print_info("Click on WIPS Policy Reuse button")
        self.auto_actions.click_reference(self.get_network_policy_reuse_wips_settings_button)
        sleep(5)

        self.screen.save_screen_shot()
        sleep(2)

        rsg_rows = self.get_wips_policy_dialog_rsg_rows()
        if not rsg_rows:
            self.utils.print_info(
                "WIPS Policy: {} does't exist, Please create default".format(wips_policy_name))
            self.auto_actions.click_reference(self.get_wips_policy_dialog_cancel_button)
            sleep(3)
            return -1

        for row in rsg_rows:
            if wips_policy_name.upper() in row.text.upper():
                self.auto_actions.click(self.get_wips_policy_dialog_rsg_row_checkbox(row))
                sleep(3)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Click on Select button")
        self.auto_actions.click_reference(self.get_wips_policy_dialog_select_button)
        sleep(2)

        self.utils.print_info("Click on Save WIPS button")
        self.auto_actions.click_reference(self.get_wips_common_object_save_button)
        sleep(2)

        self.utils.print_info("Checking the Save profile message...")
        observed_profile_message = self.wips_web_elements.get_wips_profile_save_tool_tip().text
        self.utils.print_info("Observed Message: ", observed_profile_message)
        self.screen.save_screen_shot()
        sleep(2)

        if "WIPS was updated successfully" in observed_profile_message:
            return 1
        else:
            return -1

    def get_rogue_ap_logs_row(self, search_string):
        """
        - Get the Rogue Aps Logs Row from Manage-->Security
        - Flow  Manage--> Security---> Rogue AP --> Row String
        - Keyword Usage
        - ``Get Rogue AP Logs Row    ${SEARCH_STRING}``

        :param search_string: it should be anything which is searched on the row cell
        :return: row element if row exists else return None
        """
        self.utils.print_info("Getting Rogue AP rows")
        rows = self.get_rogue_ap_logs_grid_rows()
        if not rows:
            self.utils.print_info("Rogue AP rows are not available in the page")
            return False
        for row in rows:
            if search_string in row.text:
                return row

    def verify_rogue_ap(self, search_string):
        """
        - Filter the Rogue AP based on AP Name
        - Flow  Manage--> Security---> Rogue AP
        - Keyword Usage
        - ``Verify Rogue AP   ${SEARCH_STRING}``

        :param search_string: it should be anything which is searched on the row cell
        :return: if search string appear Return Rogue AP entry details as dictionary with key and value pair else -1
        """
        self.utils.print_info("Navigate to Manage--->Security")
        self.navigator.navigate_manage_security()
        sleep(2)

        self.utils.print_info("Click on Rogue AP button")
        self.auto_actions.click_reference(self.get_rogue_ap_button)
        sleep(2)

        self.utils.print_info("Click Rogue Filter Type Checkbox")
        if not self.get_rogue_checkbox().is_selected():
            self.auto_actions.click_reference(self.get_rogue_checkbox)
            sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        rogue_ap_dict = {}
        rogue_ap_row = self.get_rogue_ap_logs_row(search_string)

        if rogue_ap_row:
            self.screen.save_screen_shot()
            sleep(2)

            cells = self.get_rogue_ap_logs_row_cells(rogue_ap_row)
            for cell in cells:
                if re.search(r'field-\w*', cell.get_attribute("class")):
                    label = re.search(r'field-\w*', cell.get_attribute("class")).group().split("field-")[-1]
                    rogue_ap_dict[label] = cell.text
            return rogue_ap_dict

        if not rogue_ap_row:
            self.screen.save_screen_shot()
            sleep(2)

            self.utils.print_info("Rogue AP Log Rows Not found")
            return -1

    def get_rogue_client_logs_row(self, search_string):
        """
        - Get the Rogue Clients Logs Row from Manage-->Security
        - Flow  Manage--> Security---> Rogue clients --> Row String
        - Keyword Usage
        - ``Get Rogue Client Logs Row    ${SEARCH_STRING}``

        :param search_string: it should be anything which is searched on the row cell
        :return: row element if row exists else return None
        """
        self.utils.print_info("Getting Rogue AP rows")
        rows = self.get_rogue_client_logs_grid_rows()
        if not rows:
            self.utils.print_info("Rogue Client rows are not available in the page")
            return False
        for row in rows:
            if search_string in row.text:
                return row

    def verify_rogue_client(self, search_string):
        """
        - Filter the Rogue Client based on Client Name Search String
        - Flow  Manage--> Security---> Rogue Clients
        - Keyword Usage
        - ``Verify Rogue Client   ${SEARCH_STRING}``

        :param search_string: it should be anything which is searched on the row cell
        :return: if search string appear Return Rogue client entry details as dictionary with key and value pair else -1
        """
        self.utils.print_info("Navigate to Manage--->Security")
        self.navigator.navigate_manage_security()
        sleep(2)

        self.utils.print_info("Click on Rogue Client button")
        self.auto_actions.click_reference(self.get_rogue_client_button)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Click Rogue Filter Type Checkbox")
        if not self.get_rogue_checkbox().is_selected():
            self.auto_actions.click_reference(self.get_rogue_checkbox)
            sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        rogue_client_dict = {}
        rogue_client_row = self.get_rogue_client_logs_row(search_string)

        if rogue_client_row:
            self.screen.save_screen_shot()
            sleep(2)

            cells = self.get_rogue_client_logs_row_cells(rogue_client_row)
            for cell in cells:
                if re.search(r'field-\w*', cell.get_attribute("class")):
                    label = re.search(r'field-\w*', cell.get_attribute("class")).group().split("field-")[-1]
                    rogue_client_dict[label] = cell.text
            return rogue_client_dict

        if not rogue_client_row:
            self.screen.save_screen_shot()
            sleep(2)

            self.utils.print_info("Rogue Client Log Rows Not found")
            return -1

    def disable_wips_on_network_policy(self, nw_policy):
        """
        - This Keyword will disable WIPS on Network Policy
        - Flow  Configure--> Network policy Name Edit---> Router Settings --> Security--> WIPS--> Disable WIPS
        - Keyword Usage
        - ``Disable Wips On Network Policy  ${NW_POLICY_NAME}``

        :param nw_policy: network policy name
        :return: return 1 if WIPS disabled successfully on Network Policy else -1
        """

        self.utils.print_info("Navigate to Network Policy-->Additional Settings-->WIPS")
        self.navigate_to_network_policy_wips_tab(nw_policy)
        sleep(5)

        if self.get_enable_wips_button().is_selected():
            self.utils.print_info("Disable WIPS button")
            self.auto_actions.click_reference(self.get_enable_wips_button)
            sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Click on Save WIPS button")
        self.auto_actions.click_reference(self.get_wips_common_object_save_button)
        sleep(2)

        tool_tip_text = tool_tip.tool_tip_text
        self.utils.print_info("Tool tip Text Displayed on Page", tool_tip_text)
        if "WIPS was updated successfully." in tool_tip_text:
            return 1
        else:
            return -1

    def create_wips_policy_adess_status_on_common_objects(self, wips_policy_name, status):
        """
        - Configure WIPS Policy On Common Objects.
        - Flow  Configure--->Common Objects--->Security-->WIPS Policies--> Add
        - Keyword Usage
        - ``Configure WIPS Policy On Common Objects   ${wips_policy_name} Enable/Disable``

        :param wips_policy_name: wips policy name
        :return: 1 if WIPS POlicy Created on Common Objects else -1
        """

        self.utils.print_info("Navigate to Common Objects---> Security--->WIPS Policies")
        self.navigator.navigate_to_security_wips_policies()
        sleep(2)

        rsg_rows = self.get_network_policy_wips_policy_dialog_rsg_rows()

        for row in rsg_rows:
            if wips_policy_name.upper() in row.text.upper():
                self.utils.print_info("WIPS Policy: {} already exist".format(wips_policy_name))
                sleep(3)
                return -1

        self.utils.print_info("Click on Add button")
        self.auto_actions.click_reference(self.get_wips_common_object_add_button)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Enter WIPS Policy Name")
        self.auto_actions.send_keys(self.get_wips_common_object_policy_name_textfield(), wips_policy_name)
        sleep(3)

        self.utils.print_info("Enter WIPS Policy Description")
        self.auto_actions.send_keys(self.get_wips_common_object_policy_description_textfield(), wips_policy_name)
        sleep(3)

        if status.upper() == "ENABLE":
            self.utils.print_info("Enable Airdefense Essentials")
            if not self.get_wips_common_object_policy_wireless_threat_detection_button().is_selected():
                self.auto_actions.click_reference(self.get_wips_common_object_policy_wireless_threat_detection_button)
                sleep(5)
        elif status.upper() == "DISABLE":
            self.utils.print_info("Disable Airdefense Essentials")
            if self.get_wips_common_object_policy_wireless_threat_detection_button().is_selected():
                self.auto_actions.click_reference(self.get_wips_common_object_policy_wireless_threat_detection_button)
                sleep(5)
        else:
            self.utils.print_info("could not change the status of  Airdefense Essentials")
            return -1


        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Click on Save button")
        self.auto_actions.click_reference(self.get_wips_common_object_save_button)
        sleep(2)

        self.utils.print_info("Checking the Save profile message...")
        observed_profile_message = self.wips_web_elements.get_wips_profile_save_tool_tip().text
        self.utils.print_info("Observed Message: ", observed_profile_message)

        if "WIPS was updated successfully" in observed_profile_message:
            return 1
        else:
            return -1

    def wips_onprem_adsp_serverip_configuration_on_network_policy(self, nw_policy, wips_policy, status, **onprem_adspip_config):
        """
        - Enable/Disable on prem Airdefense Configuration in Wips Of Network Policy
        - Flow  Network policy list--->Select Network Policy Edit---> Additional Settings--->Security-->WIPS-->Airdefense Configuration
        - Keyword Usage
        - ``Wips onprem adsp serverip configuration on Network Policy  ${NW_POLICY_NAME}  ${WIPS_POLICY_NAME}  enable  &{ON_PREM_ADSP_SERVER_IP_CONFIG}``
           ``Wips onprem adsp serverip configuration on Network policy  ${NW_POLICY_NAME}  ${WIPS_POLICY_NAME}  disable ``
        :param NW_POLICY: Network Policy Name
        :param WIPS_POLICY: WIPS Policy Name
        :param status: Enable/ Disable
        :param  ON_PREM_ADSP_SERVER_IP_CONFIG : (dict) include primary server IP and port, secondary server IP and port
        :return: 1 if WIPS Policy saved Successfully on Network Policy else -1
        """
        adsp_primary_server_ip = onprem_adspip_config.get('primary_server_ip', '1.1.1.1')
        adsp_primary_server_port = onprem_adspip_config.get('primary_server_port', '11')
        adsp_secondary_server_ip = onprem_adspip_config.get('secondary_server_ip', '1.1.1.2')
        adsp_secondary_server_port = onprem_adspip_config.get('secondary_server_port', '12')

        self.navigator.navigate_to_devices()

        self.utils.print_info("Select the Network Policy to enable WIPS")
        self.navigate_to_network_policy_edit_tab(nw_policy)
        self.utils.print_info("Click on Additional Settings tab button")
        self.auto_actions.click_reference(self.get_network_policy_additional_settings_tab)
        sleep(5)

        if status.upper() == "ENABLE":
            #Commenting the code, as we have wips_policy as parameter for this keyword, we need to select the wips policy and configure adsp onprem server with the help of existing keyword reuse wips policy
            #if self.get_network_policy_additional_settings_wips_menu_option().is_displayed():
                #self.utils.print_info("Click WIPS Menu On Security Tab")
                #self.auto_actions.click_reference(self.get_network_policy_additional_settings_wips_menu_option)
            #else:
                #self.utils.print_info("Click Security Tab")
                #self.auto_actions.click_reference(self.get_network_policy_additional_settings_security_option)
                #sleep(2)
                #self.utils.print_info("Click WIPS Menu")
                #self.auto_actions.click_reference(self.get_network_policy_additional_settings_wips_menu_option)
            self.configure_reuse_wips_policy_on_network_policy(nw_policy, wips_policy)
            self.utils.print_info("Enable on-prem Airdefense Configuration toggle button")
            if not self.get_wips_enable_OnPrem_Airdefense_button().is_selected():
                self.auto_actions.click_reference(self.get_wips_enable_OnPrem_Airdefense_button)
                self.screen.save_screen_shot()
                sleep(5)
            self.utils.print_info("Configure Primary server IP")
            self.auto_actions.send_keys(self.get_wips_primary_server_ip_textfield(), adsp_primary_server_ip)
            sleep(3)
            self.utils.print_info("Configure Primary server port")
            self.auto_actions.send_keys(self.get_wips_primary_server_port_textfield(), adsp_primary_server_port)
            sleep(3)
            self.utils.print_info("Configure Secondary server IP")
            self.auto_actions.send_keys(self.get_wips_secondary_server_ip_textfield(), adsp_secondary_server_ip)
            sleep(3)
            self.utils.print_info("Configure Secondary server port")
            self.auto_actions.send_keys(self.get_wips_secondary_server_port_textfield(), adsp_secondary_server_port)
            sleep(3)
            self.screen.save_screen_shot()
            sleep(2)

        elif status.upper() == "DISABLE":
            #Commenting the code, as we have wips_policy as parameter for this keyword, we need to select the wips policy and configure adsp onprem server with the help of existing keyword reuse wips policy
            #if self.get_network_policy_additional_settings_wips_menu_option().is_displayed():
                #self.utils.print_info("Click WIPS Menu On Security Tab")
                #self.auto_actions.click_reference(self.get_network_policy_additional_settings_wips_menu_option)
            #else:
                #self.utils.print_info("Click Security Tab")
                #self.auto_actions.click_reference(self.get_network_policy_additional_settings_security_option)
                #sleep(2)
            #self.utils.print_info("Click WIPS Menu")
            #self.auto_actions.click_reference(self.get_network_policy_additional_settings_wips_menu_option)
            self.configure_reuse_wips_policy_on_network_policy(nw_policy, wips_policy)
            self.utils.print_info("Disable on-prem Airdefense Configuration toggle button")
            sleep(3)
            if self.get_wips_enable_OnPrem_Airdefense_button().is_selected():
                self.auto_actions.click_reference(self.get_wips_enable_OnPrem_Airdefense_button)
                self.screen.save_screen_shot()
                sleep(2)
        else:
            self.utils.print_info("could not change the status of  on-prem Airdefense Configuration")
            return -1

        self.utils.print_info("Click on Save button")
        self.auto_actions.click_reference(self.get_wips_save_button)

        sleep(2)
        self.utils.print_info("Checking the Save profile message...")
        observed_profile_message = self.wips_web_elements.get_wips_profile_save_tool_tip().text
        self.utils.print_info("Observed Message: ", observed_profile_message)

        if "WIPS was updated successfully" in observed_profile_message:
            return 1
        else:
            return -1
