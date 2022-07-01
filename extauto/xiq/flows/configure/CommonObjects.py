import re
from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from extauto.common.CommonValidation import CommonValidation

from extauto.xiq.flows.common.Navigator import Navigator
import extauto.xiq.flows.common.ToolTipCapture as tool_tip
from extauto.xiq.elements.CommonObjectsWebElements import CommonObjectsWebElements
from extauto.xiq.elements.WirelessCWPWebElements import WirelessCWPWebElements
from extauto.xiq.elements.WirelessWebElements import WirelessWebElements
from extauto.xiq.elements.NetworkManagementOptionsElements import NetworkManagementOptionsElements
from extauto.xiq.elements.UserProfileWebElements import UserProfileWebElements


class CommonObjects(object):

    def __init__(self):
        self.utils = Utils()
        self.screen = Screen()
        self.auto_actions = AutoActions()
        self.navigator = Navigator()
        self.cobj_web_elements = CommonObjectsWebElements()
        self.cwp_web_elements = WirelessCWPWebElements()
        self.wireless_web_elements = WirelessWebElements()
        self.network_management_options_elements = NetworkManagementOptionsElements()
        self.user_profile_web_elements = UserProfileWebElements()
        self.common_validation = CommonValidation()

    def navigate_to_basic_ip_object_hostname(self):
        """
        - FLow: CONFIGURE-->COMMON OBJECTS-->BASIC-->IP Objects / HostNames
        - Keyword Usage:
         - ``Navigate To Basic Ip Object Hostname```

        :return: None
        """
        self.utils.print_info("Navigating to the configure---> Common Objects")
        self.navigator.navigate_configure_common_objects()
        sleep(2)
        self.utils.print_info("Click on Basic Tab")
        if not self.cobj_web_elements.get_basic_tab().is_displayed():
            self.auto_actions.click(self.cobj_web_elements.get_basic_tab())
            sleep(2)

        self.utils.print_info("Click on ip objects/host name button")
        self.auto_actions.click(self.cobj_web_elements.get_ip_object_host_name_button())
        sleep(2)

    def _get_common_object_row(self, search_string):
        """
        Getting the row in Common Object is same for all the objects
        :param search_string:
        :return:
        """
        self.utils.print_info("Getting common object rows")
        rows = self.cobj_web_elements.get_common_object_grid_rows()
        if rows:
            for row in rows:
                if cell := self.cobj_web_elements.get_common_object_grid_row_cells(row):
                    if cell.text == search_string:
                        return row

        self.utils.print_info(f"common object row {search_string} not present")
        return False

    def _search_common_object(self, search_string):
        """
        Search the passed search string object in grid rows
        :param search_string:
        :return:
        """
        row = self._get_common_object_row(search_string)
        if row:
            self.utils.print_info(f"{search_string} object present in grid row")
            return 1

    def _select_common_object_row(self, search_string):
        """
        select the common object row
        :param search_string:
        :return:
        """
        row = self._get_common_object_row(search_string)
        self.auto_actions.click(self.cobj_web_elements.get_common_object_grid_row_cells(row, 'dgrid-selector'))
        sleep(2)

    def _delete_common_objects(self):
        """
        Click on delete button and confirmation YES Windows,
        This is common for all objects
        :return:
        """
        self.utils.print_info("Clicking on delete button")
        self.auto_actions.click(self.cobj_web_elements.get_common_objects_delete_button())
        sleep(2)

        confirm_delete_btn = self.cobj_web_elements.get_common_object_confirm_delete_button()
        if confirm_delete_btn:
            self.utils.print_info("Clicking on confirm Yes button")
            self.auto_actions.click(confirm_delete_btn)
            sleep(3)

    def _select_delete_common_object(self, object_name):
        """
        Select and delete the object
        :param object_name:
        :return:
        """
        self._select_common_object_row(object_name)
        self.screen.save_screen_shot()
        sleep(2)

        self._delete_common_objects()
        self.screen.save_screen_shot()
        sleep(5)
        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)
        return tool_tp_text

    def _get_ssid_list(self):
        """
        - get all ssid from the grid

        :return: list of ssid
        """
        ssid_list = []
        for row in self.cobj_web_elements.get_common_object_grid_rows():
            if cell := self.cobj_web_elements.get_common_object_grid_row_cells(row, 'field-name'):
                ssid_list.append(cell.text)
        return ssid_list

    def delete_ssid(self, ssid_name):
        """
        - Flow: Configure --> Common Objects --> Policy -->SSIDs
        - Delete SSID from the ssid grid
        - Keyword Usage:
         - ``Delete SSID  ${SSID_NAME}``

        :param ssid_name: Name of the ssid_name
        :return: 1 if deleted else -1
        """
        self.navigator.navigate_to_ssids()
        sleep(5)

        if not self._search_common_object(ssid_name):
            self.utils.print_info(f"SSID Name {ssid_name} doesn't exist in the list")
            return 1

        self.utils.print_info(f"Select and delete SSID {ssid_name}")
        tool_tp_text = self._select_delete_common_object(ssid_name)

        self.utils.print_info(f"Tooltip text list:{tool_tp_text}")
        for value in tool_tp_text:
            if "cannot be deleted because this item is still used by another item " in value:
                self.utils.print_info(f"{value}")
                return -1
            elif "Deleted SSID successfully" in value:
                self.utils.print_info(f"Successfully deleted SSID {ssid_name}")
                return 1
        return -1

    def delete_ssids(self, *ssids, **kwargs):
        """
        - Flow: Configure --> Common Objects --> Policy -->SSIDs
        - Delete ssid's from ssid grid
        - Keyword Usage:
         - ``Delete ssids  ${SSID1}  ${SSID2}  ${SSID3}``

        :param ssids: (list) list of ssid's to delete
        :return: 1 if deleted else -1
        """

        self.navigator.navigate_to_ssids()
        sleep(5)

        self.utils.print_info("Click on full page view")
        if self.cobj_web_elements.get_paze_size_element():
            self.auto_actions.click(self.cobj_web_elements.get_paze_size_element())
            sleep(5)

        select_ssid_flag = None
        for ssid in ssids:
            if self._search_common_object(ssid):
                self._select_common_object_row(ssid)
                select_ssid_flag = True
            else:
                self.utils.print_info(f"SSID {ssid} doesn't exist in the list")

        if not select_ssid_flag:
            kwargs['pass_msg'] = "Given SSIDs are not present. Nothing to delete!"
            self.common_validation.validate(1, 1, **kwargs)
            return 1
        self._delete_common_objects()

        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(f"Tooltip text list:{tool_tp_text}")
        for value in tool_tp_text:
            if "cannot be deleted because this item is still used by another item " in value:
                kwargs['fail_msg'] = f"Cannot be deleted because this item is still used by another item {value}"
                self.common_validation.validate(-1, 1, **kwargs)
                return -1
            elif "Deleted SSID successfully" in value:
                kwargs['pass_msg'] = "Successfully deleted SSIDs"
                self.common_validation.validate(1, 1, **kwargs)
                return 1

        kwargs['fail_msg'] = "Unsuccessfully deleted SSIDs"
        self.common_validation.validate(-1, 1)
        return -1

    def delete_all_ssids(self):
        """
        - Flow: Configure --> Common Objects --> Policy -->SSIDs
        - Delete all SSIDs from the grid expect exclude_list SSIDs
        - Keyword Usage:
         - ``Delete All ssids   `

        :return: 1 if deleted else -1
        """
        exclude_list = 'ssid0'
        self.navigator.navigate_to_ssids()

        self.utils.print_info("Click on full page view")
        if self.cobj_web_elements.get_paze_size_element():
            self.auto_actions.click(self.cobj_web_elements.get_paze_size_element())
            sleep(3)

        exclude_list = exclude_list.split(",")
        np_list = self._get_ssid_list()

        delete_ssid_list = [np for np in np_list if np not in exclude_list]
        self.utils.print_info(f"Deleting SSIDs list:{delete_ssid_list}")

        return self.delete_ssids(*delete_ssid_list)

    def delete_captive_web_portal(self, cwp_name):
        """
        - Flow: Configure --> Common Objects --> Authentication --> Captive Web Portal
        - Delete captive web portal from the grid
        - Keyword Usage:
         - ``Delete Captive Web Portal  ${CWP_NAME}``

        :param cwp_name: Name of the Captive Web portal
        :return: 1 deleted
                -1 cannot be removed because it is used by another object
        """
        self.navigator.navigate_to_captive_web_portal()

        if not self._search_common_object(cwp_name):
            self.utils.print_info("CWP Name does't exists in the list")
            return 1

        self.utils.print_info("Select and delete Captive Web Portal row")
        tool_tp_text = self._select_delete_common_object(cwp_name)

        self.utils.print_info(tool_tp_text)
        for value in tool_tp_text:
            if "cannot be removed because it is used by another object" in value:
                self.utils.print_info(f"value")
                return -1
            elif "Deleted captive web portal successfully" in value:
                return 1
        return -1

    def delete_captive_web_portals(self, *cwp_names):
        """
        - Flow: Configure --> Common Objects --> Authentication --> Captive Web Portal
        - Delete captive web portals from the grid
        - Keyword Usage:
         - ``Delete Captive Web Portals   ${CWP_NAME1}  ${CWP_NAME2}   ${CWP_NAME3}``

        :param cwp_names: Name of the Captive Web portal
        :return: 1 deleted
                -1 cannot be removed because it is used by another object
        """
        self.navigator.navigate_to_captive_web_portal()
        cwp_flag = None
        self.utils.print_info("Click on 50 page size")

        if self.cobj_web_elements.get_paze_size_element():
            self.auto_actions.click(self.cobj_web_elements.get_paze_size_element())
            sleep(3)

        for cwp in cwp_names:
            if self._search_common_object(cwp):
                self._select_common_object_row(cwp)
                cwp_flag = True
            else:
                self.utils.print_info(f"cwp:{cwp} does't exists in the list")

        if not cwp_flag:
            return 1
        self._delete_common_objects()
        sleep(5)
        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)
        for value in tool_tp_text:
            if "cannot be removed because it is used by another object" in value:
                self.utils.print_info(f"{value}")
                return -1
            elif "Deleted captive web portal successfully" in value:
                return 1
        return -1

    def delete_external_radius_server(self, radius_server):
        """
        - Flow: Configure --> Common Objects --> Authentication --> External radius server
        - Delete external radius server from grid
        - Keyword Usage:
         - ``Delete External Radius Server   ${RADIUS_SERVER_NAME}``

        :param radius_server: radius server name
        :return: 1 if deleted
                -1 if can not be removed
        """
        self.navigator.navigate_to_external_radius_server()

        if not self._search_common_object(radius_server):
            self.utils.print_info("Radius server does't exists in the list")
            return 1

        self.utils.print_info("select  and delete radius server row")
        tool_tp_text = self._select_delete_common_object(radius_server)

        for value in tool_tp_text[::-1]:
            if "The External RADIUS Server cannot be removed because it is used by another object" in value:
                self.utils.print_info(value)
                return -1
        return 1

    def delete_ip_object_hostname(self, object_name):
        """
        - Flow: Configure --> Common Objects --> Basic --> IP Objects / HostName
        - Delete the ip object or hostname from Basic-->IP Objects/ Hostname
        - Keyword Usage:
         - ``Delete IP Object Hostname  ${IP_OR_HOSTNAME}``

        :param object_name: Ip object or hostname
        :return: 1 if deleted
                -1 if can not be removed
        """
        self.navigate_to_basic_ip_object_hostname()

        if not self._search_common_object(object_name):
            self.utils.print_info("Ip/Hostname object does't exists in the list")
            return 1

        self.utils.print_info("select and delete ip/hostname object")
        tool_tp_text = self._select_delete_common_object(object_name)

        for value in tool_tp_text[::-1]:
            if "The IP Object/Hostname cannot be removed because it is used by another object" in value:
                self.utils.print_info(value)
                return -1
            elif "IP object or host name was deleted successfully" in value:
                return 1
        return -1

    def _edit_captive_web_portal(self, cwp_name):
        """
        Navigate to cwp , select the cwp and click on edit button
        :param cwp_name:
        :return:
        """
        self.navigator.navigate_to_captive_web_portal()
        if not self._search_common_object(cwp_name):
            self.utils.print_info("CWP Name does't exists in the list")
            return 1

        self.utils.print_info("Select Captive Web Portal row")
        self._select_common_object_row(cwp_name)
        sleep(2)

        self.utils.print_info("Click on edit button")
        self.auto_actions.click(self.cobj_web_elements.get_common_object_edit_button())
        sleep(2)

    def disable_cwp_employee_approval(self, cwp_name):
        """
        - Flow: Configure --> Common Objects --> Authentication --> Captive Web Portal
        - Disable the employee approval in captive web portal configuration
        - Keyword Usage:
         - ``Disable Cwp Employee Approval  ${CWP_NAME}``

        :param cwp_name: name of the captive web portal
        :return:
        """
        self.utils.print_info("Navigate to cwp edit window")
        self._edit_captive_web_portal(cwp_name)

        if self.cobj_web_elements.get_cwp_self_reg_employee_approval_button().is_selected():
            self.utils.print_info("Click on employee cwp employee approval button")
            self.auto_actions.click(self.cobj_web_elements.get_cwp_self_reg_employee_approval_button())
            sleep(2)

        self.screen.save_screen_shot()
        self.auto_actions.click(self.cobj_web_elements.get_cwp_save_button())
        return 1

    def edit_captive_web_portal_social_login_configuration(self, **cwp_template_config):
        """
        - Flow: Configure --> Common Objects --> Authentication --> Captive Web Portal
        - Edit social login captive web portal from the grid
        - Keyword Usage:
         - ``Edit Captive Web Portal Social Login Configuration   &{CWP_TEMPLATE_CONFIG}``

        :param cwp_template_config: social login cwp edit variables
        :return: 1 edited
        """

        temp_cwp_name = cwp_template_config.get('cwp_name')
        social_fb_status = cwp_template_config.get('social_login_type_fb')
        social_google_status = cwp_template_config.get('social_login_type_google')
        social_linkedin_status = cwp_template_config.get('social_login_type_linkedin')
        restrict_access_domain = cwp_template_config['restrict_access']
        auth_cache_duration = cwp_template_config['auth_cache_duration']

        self.utils.print_info("Temp Name : ", temp_cwp_name)
        self.utils.print_info("Facebook Checkbox status to configure : ", social_fb_status)
        self.utils.print_info("Google Checkbox status to configure : ", social_google_status)
        self.utils.print_info("Linkedin Checkbox status to configure : ", social_linkedin_status)
        self.utils.print_info("Restrict Domain access : ", restrict_access_domain)
        self.utils.print_info("Authentication Cache Duration : ", auth_cache_duration)

        self.navigator.navigate_to_captive_web_portal()

        if not self._search_common_object(temp_cwp_name):
            self.utils.print_info("CWP Name does't exists in the list")
            return 1

        self._select_common_object_row(temp_cwp_name)
        sleep(2)

        self.utils.print_info("Click on edit button")
        self.auto_actions.click(self.cobj_web_elements.get_common_object_edit_button())
        sleep(4)

        if social_fb_status:
            if social_fb_status.upper() == "ENABLE":
                self.utils.print_info("Select facebook check box")
                if not self.cwp_web_elements.get_cloud_cwp_social_login_type_fb().is_selected():
                    self.auto_actions.click(self.cwp_web_elements.get_cloud_cwp_social_login_type_fb())
                    sleep(2)
            if social_fb_status.upper() == "DISABLE":
                self.utils.print_info("UnSelect facebook check box")
                if self.cwp_web_elements.get_cloud_cwp_social_login_type_fb().is_selected():
                    self.auto_actions.click(self.cwp_web_elements.get_cloud_cwp_social_login_type_fb())
                    sleep(2)

        if social_google_status:
            if social_google_status.upper() == "ENABLE":
                self.utils.print_info("Select google check box")
                if not self.cwp_web_elements.get_cloud_cwp_social_login_type_google().is_selected():
                    self.auto_actions.click(self.cwp_web_elements.get_cloud_cwp_social_login_type_google())
                    sleep(2)

            if social_google_status.upper() == "DISABLE":
                self.utils.print_info("UnSelect google check box")
                if self.cwp_web_elements.get_cloud_cwp_social_login_type_google().is_selected():
                    self.auto_actions.click(self.cwp_web_elements.get_cloud_cwp_social_login_type_google())
                    sleep(2)

        if social_linkedin_status:
            if social_linkedin_status.upper() == "ENABLE":
                self.utils.print_info("Select Linkedin check box")
                if not self.cwp_web_elements.get_cloud_cwp_social_login_type_linkedin().is_selected():
                    self.auto_actions.click(self.cwp_web_elements.cloud_cwp_social_login_type_linkedin())
                    sleep(2)
            if social_linkedin_status.upper() == "DISABLE":
                self.utils.print_info("UnSelect Linkedin check box")
                if self.cwp_web_elements.get_cloud_cwp_social_login_type_linkedin().is_selected():
                    self.auto_actions.click(self.cwp_web_elements.get_cloud_cwp_social_login_type_linkedin())
                    sleep(2)

        if restrict_access_domain.upper() != "DEFAULT":
            self.utils.print_info("Enter Restrict Domain Name")
            sleep(2)
            self.auto_actions.send_keys(self.cwp_web_elements.get_cloud_cwp_restrict_domain_field(),
                                        restrict_access_domain)
            sleep(2)

        if auth_cache_duration.upper() != "DEFAULT":
            self.utils.print_info("Enter Cache Duration in Minutes")
            self.auto_actions.send_keys(self.cwp_web_elements.get_cloud_cwp_cache_duration_field(), auth_cache_duration)
            sleep(2)

        self.utils.print_info("Click cwp save button")
        self.auto_actions.click(self.cwp_web_elements.get_default_add_windows_cwp_save_cwp_button())

        self.screen.save_screen_shot()
        sleep(2)

        tool_tip_text = tool_tip.tool_tip_text
        self.utils.print_info("Tool tip Text Displayed on Page", tool_tip_text)
        if "Captive web portal was saved successfully." in tool_tip_text:
            return 1
        else:
            return -1

    def delete_aaa_server_profile(self, aaa_profile_name):
        """
        - Flow: CONFIGURE-->COMMON OBJECTS-->AUTHENTICATION-->AAA SERVER SETTINGS
        - Delete AAA server profile from the grid
        -Keyword Usage:
         - ``Delete AAA Server Profile  ${AAA_PROFILE_NAME}``

        :param aaa_profile_name: Name of AAA Profile
        :return: 1 if aaa profile deleted successfully else returns -1
        """
        self.utils.print_info("Navigate to AAA Server Profile Settings")
        self.navigator.navigate_to_aaa_server_settings()

        if not self._search_common_object(aaa_profile_name):
            self.utils.print_info("AAA Profile Name does't exists in the list")
            return 1

        self.utils.print_info("Select and delete AAA Profile row")
        self._select_delete_common_object(aaa_profile_name)

        sleep(5)
        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)

        for value in tool_tp_text:
            if "Deleted AAA server profile successfully" in value:
                return 1
        return -1

    def delete_port_type_profile(self, port_type_name):
        """
        - Flow: CONFIGURE-->COMMON OBJECTS-->PORT TYPES
        - Delete Port Type from the grid
        - Keyword Usage:
         - ``Delete Port Type Profile  ${PORT_TYPE_NAME}``

        :param port_type_name: Name of Port Tye
        :return: 1 if Port Type deleted successfully, else returns -1
        """
        self.utils.print_info("Navigate to Port Types Settings")
        self.navigator.navigate_to_policy_port_types()

        self.utils.print_info("Click Full pages button")
        self.auto_actions.click(self.cobj_web_elements.get_common_object_policy_port_types_view_all_pages())
        sleep(2)

        if not self._search_common_object(port_type_name):
            self.utils.print_info("Port Type Profile Name does't exists in the list",port_type_name)
            return 1

        self.utils.print_info("Select and delete Port Type Profile row")
        self._select_delete_common_object(port_type_name)
        self.utils.print_info("Clicking 'YES' button...")
        confirmation_button = self.cobj_web_elements.get_policy_port_types_confirmation_button()
        if confirmation_button:
            self.utils.print_info("Found 'YES' button.")
            self.auto_actions.click(confirmation_button)
        else:
            self.utils.print_info("Did not find the confirmation button!")
            return -1

        sleep(5)
        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)

        for value in tool_tp_text:
            if "The vlan has been deleted" in value:
                return 1
        return -1

    def delete_sub_network_profile(self, sub_network_name):
        """
        - Flow: CONFIGURE-->COMMON OBJECTS-->NETWORK-->Subnetwork Space
        - Delete Sub Network in Common Object from the grid
        - Keyword Usage:
         - ``Delete Sub Network Profile   ${SUB_NETWORK_NAME}``

        :param sub_network_name: Name of SubNetwork Space
        :return: 1 if SubNetwork Space deleted successfully else returns -1
        """
        self.utils.print_info("Navigate to SubNetwork Space Settings")
        self.navigator.navigate_to_network_subnetwork_space()

        if not self._search_common_object(sub_network_name):
            self.utils.print_info("SubNetwork Space Name does't exists in the list")
            return 1

        self.utils.print_info("Select and delete SubNetwork Space row")
        self._select_delete_common_object(sub_network_name)

        sleep(5)
        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)

        for value in tool_tp_text:
            if "The subnetwork has been deleted" in value:
                return 1
        return -1

    def delete_vlan_profile(self, vlan_name):
        """
        - Flow: CONFIGURE-->COMMON OBJECTS-->BASIC-->VLAN's
        - Delete Vlans in Common Object from the grid
        - Keyword Usage:
         - ``Delete Vlan Profile  ${VLAN_NAME}``

        :param vlan_name: Name of Vlan
        :return: 1 if vlan name deleted successfully else returns -1
        """
        self.utils.print_info("Navigate to Basic--> VLANS Settings")
        self.navigator.navigate_to_basic_vlans_tab()

        if not self._search_common_object(vlan_name):
            self.utils.print_info("VLAN Name does't exists in the list")
            return 1

        self.utils.print_info("Select and delete VLAN row")
        self._select_delete_common_object(vlan_name)

        sleep(5)
        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)

        for value in tool_tp_text:
            if "VLAN has been deleted" in value:
                return 1
        return -1

    def navigate_to_security_wips_policies(self):
        """
        - Flow: CONFIGURE-->COMMON OBJECTS-->SECURITY-->WIPS POLICIES
        - Keyword Usage:
         - ``Navigate To Security Wips Policies``

        :return: None
        """
        self.utils.print_info("Navigating to the configure---> Common Objects")
        self.navigator.navigate_configure_common_objects()
        sleep(3)

        if self.cobj_web_elements.get_common_object_security_wips_policies_tab().is_displayed():
            self.utils.print_info("Click WIPS Policies button")
            self.auto_actions.click(self.cobj_web_elements.get_common_object_security_wips_policies_tab())
        else:
            self.utils.print_info("Click Security button")
            self.auto_actions.click(self.cobj_web_elements.get_common_object_security_tab())
            sleep(2)
            self.utils.print_info("Click  WIPS Policies button")
            self.auto_actions.click(self.cobj_web_elements.get_common_object_security_wips_policies_tab())

        sleep(5)

    def delete_wips_policy_profile(self, wips_policy_name):
        """
        - Flow: CONFIGURE-->COMMON OBJECTS-->SECURITY-->WIPS POLICIES
        - Delete wips_policys in Common Object from the grid
        - Keyword Usage:
         - ``Delete Wips Policy Profile   ${WIPS_POLICY_NAME}``

        :param wips_policy_name: Name of wips policy name
        :return: 1 if wips policy name deleted successfully else returns -1
        """
        self.utils.print_info("Navigate to Basic--> VLANS Settings")
        self.navigator.navigate_to_security_wips_policies()

        if not self._search_common_object(wips_policy_name):
            self.utils.print_info("WIPS Policy Name does't exists in the list")
            return 1

        self.utils.print_info("Select and delete Wips Policy row")
        self._select_delete_common_object(wips_policy_name)

        sleep(5)
        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)

        for value in tool_tp_text:
            if "cannot be deleted because this item is still used by another item" in value:
                return -1
        return 1

    def delete_ap_template_profile(self, ap_template_name):
        """
        -
        -->COMMON OBJECTS-->AP Templates
        - Delete ap_template_name in Common Object from the grid
        - Keyword Usage:
         - ``Delete Ap Template Profile  ${AP_TEMPLATE_NAME}``

        :param ap_template_name: Name of AP Template
        :return: 1 if ap template name deleted successfully else returns -1
        """
        ap_template_name = ap_template_name.replace(" ", "")

        self.utils.print_info("Navigate to Policy--> AP Templates")
        self.navigator.navigate_to_policy_ap_template()

        if self.cobj_web_elements.get_common_object_policy_ap_templates_view_all_pages():
            self.utils.print_info("Click Full pages button")
            self.auto_actions.click(self.cobj_web_elements.get_common_object_policy_ap_templates_view_all_pages())
            sleep(2)

        if not self._search_common_object_template(ap_template_name):
            self.utils.print_info("AP Template Name does't exists in the list")
            return 1

        self.utils.print_info("Select and delete AP Template row")
        self._select_delete_common_object_template(ap_template_name)

        sleep(5)
        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)

        if "Template was successfully removed from policy." in tool_tp_text[-1]:
            return 1
        elif "The Device Template cannot be removed because it is used by another object" in tool_tp_text[-1]:
            return -1
        return -2

    def _get_common_object_template_row(self, search_string):
        """
        Getting the row in Common Object is same for all the objects
        :param search_string:
        :return:
        """
        self.utils.print_info("Getting common object rows")
        rows = self.cobj_web_elements.get_common_object_grid_rows()
        if not rows:
            self.utils.print_info("{} row not present in the grid")
            return False
        for row in rows:
            cell = self.cobj_web_elements.get_common_object_template_grid_row_cells(row)
            if not cell:
                pass
            elif cell.text == search_string:
                return row
        return False

    def _search_common_object_template(self, search_string):
        """
        - Search the passed search string object in grid rows
        :param search_string:
        :return:
        """
        if self._get_common_object_template_row(search_string):
            self.utils.print_info(f"{search_string} object present in grid row")
            return 1

    def _select_common_object_template_row(self, search_string):
        """
        select the common object row
        :param search_string:
        :return:
        """
        row = self._get_common_object_template_row(search_string)
        self.auto_actions.click(self.cobj_web_elements.get_common_object_grid_row_cells(row, 'dgrid-selector'))
        sleep(2)

    def _select_delete_common_object_template(self, object_name):
        """
        Select and delete the object
        :param object_name:
        :return:
        """
        self._select_common_object_template_row(object_name)
        sleep(2)
        self._delete_common_objects()

    def _select_edit_common_object(self, object_name):
        """
        Select and edit the object
        :param object_name:
        :return:
        """
        self._select_common_object_row(object_name)
        sleep(2)
        self._delete_common_objects()
        sleep(5)

    def _search_switch_template(self, search_string):
        """
        Search the passed search string object in Switch Template grid rows
        :param search_string:
        :return:
        """
        row = self._get_switch_template_row(search_string)
        if row:
            self.utils.print_info(f"{search_string} object present in grid row")
            return 1

    def delete_switch_template(self, template_name):
        """
        - Flow: Configure --> Common Objects --> Policy -->Switch Template
        - Delete specified switch template from the Switch Templates grid
        - Keyword Usage:
         - ``Delete Switch Template  ${TEMPLATE_NAME}``
        :param template_name: Name of the switch template
        :return: 1 if deleted else -1
        """
        self.navigator.navigate_to_switch_templates()

        self.utils.print_info("Click on full page view for switch template")
        page_size_el = self.cobj_web_elements.get_paze_size_element(page_size='100')
        if page_size_el:
            self.utils.print_info("  -- clicking page size element 100 for switch template")
            self.auto_actions.click(page_size_el)
            sleep(3)
        else:
            self.utils.print_info("  -- could not find page size element 100")

        if not self._search_switch_template(template_name):
            self.utils.print_info("Switch Template doesn't exist on first page")
            next_page_el = self.cobj_web_elements.get_next_page_element()
            if next_page_el:
                device_page_numbers = self.cobj_web_elements.get_page_numbers()
                page_len = int(max(device_page_numbers.text))
                while page_len:
                    self.utils.print_info("  -- clicking next page")
                    self.auto_actions.click(next_page_el)
                    sleep(2)
                    page_len = page_len - 1
            if not self._search_switch_template(template_name):
                self.utils.print_info("Switch Template doesn't exist in the list")
                return 1

        self.utils.print_info("Select and delete switch template")
        tool_tp_text = self._select_delete_switch_template_row(template_name)

        self.utils.print_info(f"Tooltip text list:{tool_tp_text}")
        for value in tool_tp_text:
            if "cannot be deleted because this item is still used by another item " in value:
                self.utils.print_info(f"{value}")
                return -1
            elif "Deleted Switch Template successfully" in value:
                return 1
        return -1

    def _get_switch_template_row(self, search_string):
        """
        Gets the row in Switch Template grid;  this is different from common as it uses a different field name to find the Template
        :param search_string:
        :return:
        """
        self.utils.print_info("Getting common object rows")
        rows = self.cobj_web_elements.get_common_object_grid_rows()
        if rows:
            for row in rows:
                if cell := self.cobj_web_elements.get_common_object_grid_row_cells(row,
                                                                                   field='dgrid-column-2 field-tmpl'):
                    if cell.text == search_string:
                        return row
        else:
            self.utils.print_info("No rows found")

        self.utils.print_info(f"common object row '{search_string}' not present")
        return False

    def _select_switch_template_row(self, search_string):
        """
        select the switch template row
        :param search_string:
        :return:
        """
        row = self._get_switch_template_row(search_string)
        self.auto_actions.click(self.cobj_web_elements.get_common_object_grid_row_cells(row, 'dgrid-selector'))
        sleep(2)

    def _select_delete_switch_template_row(self, object_name):
        """
        Select and delete the object
        :param object_name:
        :return:
        """
        self._select_switch_template_row(object_name)
        sleep(2)
        self._delete_switch_template()
        sleep(5)
        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)
        return tool_tp_text

    def _delete_switch_template(self):
        """
        Click on delete button for the Switch Template view (no confirmation in this view)
        :return:
        """
        self.utils.print_info("Click on delete button")
        self.auto_actions.click(self.cobj_web_elements.get_common_objects_delete_button())
        self.auto_actions.click(self.cobj_web_elements.get_common_objects_delete_button())
        sleep(2)

    def create_open_ssid_in_common_objects(self, ssid_name):
        """
        - Flow: Configure --> Common Objects --> Policy -->SSIDs
        - Create Open SSID from the ssid grid
        - Keyword Usage:
         - ``Create Open SSID In Common Objects  ${SSID_NAME}``

        :param ssid_name: Name of the ssid_name
        :return: 1 if Created Open SSID Successfully else -1
        """
        self.navigator.navigate_to_ssids()
        sleep(5)

        if self._search_common_object(ssid_name):
            self.utils.print_info(f"SSID Name {ssid_name} already exists in the list")
            return 1

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Click on Add SSID Button")
        self.auto_actions.click(self.cobj_web_elements.get_common_object_policy_add_ssid_button())
        sleep(2)

        self.utils.print_info("Enter the Wireless Networks SSID Name:{}".format(ssid_name))
        self.auto_actions.send_keys(self.wireless_web_elements.get_wireless_ssid_field(), ssid_name)
        sleep(2)

        self.utils.print_info("Enter the Wireless Networks Broadcast Name:{}".format(ssid_name))
        self.auto_actions.click(self.wireless_web_elements.get_wireless_broadcast_name_field())
        sleep(2)

        self.utils.print_info("selecting Authentication type OPEN for wireless network")
        self.auto_actions.click(self.wireless_web_elements.get_wireless_authtype_open())
        sleep(2)

        self.utils.print_info("click on wireless network save button")
        self.auto_actions.click(self.wireless_web_elements.get_wireless_network_save_button())
        self.screen.save_screen_shot()
        sleep(2)

        sleep(5)
        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)

        for value in tool_tp_text:
            if "SSID was saved successfully." in value:
                return 1
            elif "The SSID Profile cannot be saved" in value:
                return -2
        return -1

    def clone_open_ssid_in_common_objects(self, ssid_name, clone_ssid_name):
        """
        - Flow: Configure --> Common Objects --> Policy -->SSIDs
        - Clone Open SSID from the Existing ssid grid
        - Keyword Usage:
         - ``Clone Open SSID In Common Objects  ${SSID_NAME}  ${CLONE_SSID_NAME}``

        :param ssid_name: Copy of SSID to clone
        :param clone_ssid_name: Clone SSID name
        :return: 1 if Cloned Open SSID Successfully else -1
        """

        self.navigator.navigate_to_ssids()
        sleep(5)

        if not self._search_common_object(ssid_name):
            self.utils.print_info(f"SSID Name {ssid_name} doesn't exist in the list to clone")
            return -1

        self._select_common_object_row(ssid_name)
        sleep(2)

        self.utils.print_info("click on SSID clone button")
        self.auto_actions.click(self.cobj_web_elements.get_common_object_policy_clone_ssid_button())
        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Enter Clone SSID Name")
        self.auto_actions.send_keys(self.cobj_web_elements.get_common_object_policy_clone_ssid_saveas_textfield(),
                                    clone_ssid_name)
        sleep(2)

        self.utils.print_info("Click SSID Save clone button")
        self.auto_actions.click(self.cobj_web_elements.get_common_object_policy_ssid_clone_save_button())
        self.screen.save_screen_shot()
        sleep(2)

        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)

        for value in tool_tp_text:
            if "The item was copied successfully." in value:
                return 1
        return -1

    def create_radio_profile(self, profile_name, radio_mode, dfs=False):
        """
        - Flow: Configure --> Common Objects --> Policy -->Radio Profile
        - Create Radio profile from the radio grid
        - Keyword Usage:
         - ``Create Radio Profile        ${RADIO_PROFILE_NAME}       ${RADIO_MODE}``

        :param profile_name: Name of the Radio profile
        :param radio_mode : Select the radio mode ("ax (5GHz)" or "ax (2.4GHz)" or  "ac" or  "a/n")
        :param dfs : will select the DFS related option, when its "True", disabled channel: u-1/u-2e/u-3
                    else will create radio profile without DFS options
        :return: 1 if Created Radio profile Successfully else -1
        """

        self.utils.print_info("Navigate to radio profile in Common Object")
        self.navigator.navigate_to_radio_profile()
        sleep(3)
        page = self.cobj_web_elements.get_common_object_radio_profile_pagination_max()
        if page is not None:
            self.utils.print_info("Select pagination to max  value as 100 ")
            self.auto_actions.click(self.cobj_web_elements.get_common_object_radio_profile_pagination_max())
            sleep(2)

        if self._search_common_object(profile_name):
            self.utils.print_info("Radio profile ", profile_name, " already exists in the list")
            return 1

        self.utils.print_info("Click on Add profile Button")
        self.auto_actions.click(self.cobj_web_elements.get_common_object_add_button_radio_profile())
        sleep(2)

        self.utils.print_info("Add profile name")
        self.auto_actions.send_keys(self.cobj_web_elements.get_common_object_radio_profile_name(), profile_name)

        self.utils.print_info("click radio mode")
        self.auto_actions.click(self.cobj_web_elements.get_common_object_radio_profile_mode())

        self.utils.print_info("Selecting radio mode")
        self.auto_actions.select_drop_down_options(self.cobj_web_elements.get_common_object_radio_profile_select_mode(), radio_mode)

        if dfs is True:
            self.utils.print_info("Enable  DFS options")
            self.auto_actions.click(self.cobj_web_elements.get_common_object_radio_profile_enable_dfs())

            self.utils.print_info("Enable Exclude channel")
            self.auto_actions.click(self.cobj_web_elements.get_common_object_radio_profile_exclude_channel())

            self.utils.print_info("Excluding UNII-1")
            self.auto_actions.click(self.cobj_web_elements.get_common_object_radio_profile_exclude_ch_u_1())

            self.utils.print_info("Excluding UNII-2 Extended")
            self.auto_actions.click(self.cobj_web_elements.get_common_object_radio_profile_exclude_ch_u_2e())

            self.utils.print_info("Excluding UNII-3")
            self.auto_actions.click(self.cobj_web_elements.get_common_object_radio_profile_exclude_ch_u_3())

        self.utils.print_info("Save Radio profile")
        self.auto_actions.click(self.cobj_web_elements.get_common_object_radio_profile_save())

        sleep(2)
        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)

        for value in tool_tp_text:
            if "Radio profile was saved successfully." in value:
                return 1
            elif "Radio profile cannot be saved" in value:
                return -2
        return -1
 
    def add_ap_template_from_common_object(self, ap_model, ap_template_name, **wifi_interface_config):
        """"
        - CONFIGURE-->COMMON OBJECTS-->Policy-->AP Templates
        - Adding AP Template in Common Object
        - Checking the AP template presence in the AP Templates Grid
        - If it is not there add New AP Template
        - Keyword Usage
         - ``Add AP Template From Common Object   ${AP_MODEL}   ${AP_TEMPLATE_NAME}     &{AP_TEMPLATE_CONFIG}``

        :param ap_model: Model of the AP like AP630, AP410C etc
        :param ap_template_name: AP Template Name ie AP630-TEMPLATE,AP410C-TEMPLATE etc
        :param wifi_interface_config: (Config Dict) Enable/Disable Client Access,Backhaul Mesh Link,Sensor etc
        :return: 1 if AP Template Configured Successfully else -1
        """
        wifi0_config = wifi_interface_config['wifi0_configuration']
        wifi1_config = wifi_interface_config['wifi1_configuration']
        wifi2_config = wifi_interface_config.get('wifi2_configuration', 'None')
        wired_config = wifi_interface_config.get('wired_configuration', 'None')

        self.utils.print_info("Navigate to Policy--> AP Templates")
        self.navigator.navigate_to_policy_ap_template()

        if self.cobj_web_elements.get_common_object_policy_ap_templates_view_all_pages():
            self.utils.print_info("Click Full pages button")
            self.auto_actions.click(self.cobj_web_elements.get_common_object_policy_ap_templates_view_all_pages())
            sleep(2)

        if self._search_common_object_template(ap_template_name):
            self.utils.print_info("AP Template Name already exists in the list")
            return 1

        self.utils.print_info("Click on AP Template add button")
        self.auto_actions.click(self.cobj_web_elements.get_common_object_add_ap_template_button())
        sleep(2)

        self.screen.save_screen_shot()

        self.utils.print_info("select the AP Model: ", ap_model)
        ap_list_items = self.cobj_web_elements.get_common_object_matched_ap_model_dropdown()
        for el in ap_list_items:
            if not el:
                pass
            if ap_model.upper() in el.text.upper():
                self.auto_actions.click(el)
                break
            print(el.text)
        sleep(3)

        self.utils.print_info("Enter the AP Template Name")
        self.auto_actions.send_keys(self.cobj_web_elements.get_common_object_add_ap_template_name(),
                                    ap_template_name)

        self.screen.save_screen_shot()

        self.utils.print_info("Configure WiFI0 Interface for AP Template")
        self._config_ap_template_wifi0(**wifi0_config)

        self.utils.print_info("Configure WiFI1 Interface for AP Template")
        self._config_ap_template_wifi1(**wifi1_config)

        if not wifi2_config == 'None':
            self._config_ap_template_wifi2(**wifi2_config)

        if not wired_config == "None":
            self._config_ap_template_wired(**wired_config)

        self.utils.print_info("Click on the save template button")
        self.auto_actions.click(self.cobj_web_elements.get_common_object_ap_template_save_button())
        sleep(3)

        tool_tip_text = tool_tip.tool_tip_text
        self.screen.save_screen_shot()
        sleep(2)
        self.utils.print_info("Tool tip Text Displayed on Page", tool_tip_text)
        sub_string = "template"
        strings_with_substring = [msg for msg in tool_tip_text if sub_string in msg]
        self.utils.print_info("Tool tip Text ap template", strings_with_substring)
        if "AP template was saved successfully" in str(strings_with_substring):
            return 1
        else:
            return -1

    def _config_ap_template_wifi0(self, **wifi0_profile):
        """
        - Configure the WIFI0 configuration on AP Template
        - Keyword Usage
         - ``Config AP Template WiFi0  &{WIFI0_CONFIG}``

        :param wifi0_profile: (Config Dict) Enable/Disable Client mode, Client Access,Backhaul Mesh Link, Sensor
        :return: 1 if WiFi0 Profile Configured Successfully else None
        """
        client_mode_status_wifi0   = wifi0_profile.get('client_mode', 'Disable')
        client_access_status_wifi0 = wifi0_profile.get('client_access', 'Enable')
        backhaul_mesh_status_wifi0 = wifi0_profile.get('backhaul_mesh_link', 'Disable')
        sensor_status_wifi0 = wifi0_profile.get('sensor', 'Disable')
        radio_profile_wifi0 = wifi0_profile.get('radio_profile', 'radio_ng_11ax-2g')
        radio_status_wifi0 = wifi0_profile.get('radio_status', 'On')
        enable_SDR = wifi0_profile.get('enable_SDR', 'Disable')
        sdr_profile_name = wifi0_profile.get('sdr_profile_name', '150W-SDR-Profile')

        self.utils.print_info("Click on WiFi0 Tab on AP Template page")
        self.auto_actions.click(self.cobj_web_elements.get_common_object_ap_template_wifi0_tab())

        if radio_status_wifi0.upper() == "OFF":
            self.utils.print_info("Enable Client Access Checkbox on WiFi0 Interface")
            if self.cobj_web_elements.get_common_object_wifi0_radio_status_button().is_selected():
                self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi0_radio_status_button())
            return 1
        else:
            self.utils.print_info("Disable Client Access check box on WiFi0 Interface")
            if not self.cobj_web_elements.get_common_object_wifi0_radio_status_button().is_selected():
                self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi0_radio_status_button())
        self.auto_actions.scroll_down()

        self.utils.print_info(f"select Radio Profile:{radio_profile_wifi0}")
        self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi0_radio_profile_button())
        self.auto_actions.select_drop_down_options(self.cobj_web_elements.
                                                   get_common_object_wifi0_radio_profile_dropdown(),
                                                   radio_profile_wifi0)
        if client_mode_status_wifi0.upper() == "ENABLE":
            self.utils.print_info("Enable Client Mode Checkbox on WiFi0 Interface")
            if not self.cobj_web_elements.get_common_object_wifi0_client_mode().is_selected():
                self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi0_client_mode())

                wifi0_client_mode_profile = wifi0_profile['client_mode_profile']
                client_mode_profile_name  = wifi0_client_mode_profile.get('client_mode_profile_name', 'wifi0')
                client_mode_profile_dhcp  = wifi0_client_mode_profile.get('dhcp_server_scope', '192.168.150.1')
                cm_enable_local_web_page  = wifi0_client_mode_profile.get('local_web_page', 'ENABLE')
                cm_ssid_name              = wifi0_client_mode_profile.get('ssid_name', 'bk_enterprise')
                cm_password               = wifi0_client_mode_profile.get('password', 'aerohive')
                cm_auth_method            = wifi0_client_mode_profile.get('auth_method', 'Pre-Shared Key')
                cm_key_type               = wifi0_client_mode_profile.get('key_type', 'ASCII')
                self.utils.print_info("Click Add Client Mode Profile")
                self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi0_add_client_mode_profile())
                self.utils.print_info(f"Enter Client Mode Profile Name: {client_mode_profile_name}")
                self.auto_actions.send_keys(self.cobj_web_elements.get_common_object_wifi0_1_client_mode_profile_name(), client_mode_profile_name)
                if cm_enable_local_web_page.upper() == 'DISABLE':
                    self.utils.print_info(f"Enable Local Web Page: {cm_enable_local_web_page}")
                    self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi0_1_cm_local_web_page_checkbox())
                    self.utils.print_info(f"Click Add(+)")
                    self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi0_1_cm_local_web_page_add())
                    self.utils.print_info(f"Enter SSID Name: {cm_ssid_name}")
                    self.auto_actions.send_keys(self.cobj_web_elements.get_common_object_wifi0_1_cm_local_web_page_ssid_textbox(), cm_ssid_name)
                    self.utils.print_info(f"Enter Password: {cm_password}")
                    self.auto_actions.send_keys(self.cobj_web_elements.get_common_object_wifi0_1_cm_local_web_page_password_textbox(), cm_password)
                    self.utils.print_info(f"Auth Method: {cm_auth_method}")
                    self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi0_1_cm_local_web_page_auth_dropdown())
                    self.auto_actions.select_drop_down_options(self.cobj_web_elements.get_common_object_wifi0_1_cm_local_web_page_auth_dropdown_option(), cm_auth_method)
                    self.utils.print_info(f"Key Type: {cm_key_type}")
                    self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi0_1_cm_local_web_key_type_dropdown())
                    self.auto_actions.select_drop_down_options(self.cobj_web_elements.get_common_object_wifi0_1_cm_local_web_key_type_dropdown_option(), cm_key_type)
                    self.screen.save_screen_shot()
                    sleep(2)
                    self.utils.print_info(f"Click Add button")
                    self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi0_1_cm_local_web_page_add_button())
                self.utils.print_info(f"Enter DHCP Server Scope: {client_mode_profile_dhcp}")
                self.auto_actions.send_keys(self.cobj_web_elements.get_common_object_wifi0_1_client_mode_profile_dhcp_server_scope(), client_mode_profile_dhcp)
                self.screen.save_screen_shot()
                self.utils.print_info("Click Save Client Mode Profile")
                self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi0_1_client_mode_profile_save())
        else:
            self.utils.print_info("Disable Client Mode check box on WiFi0 Interface")
            if self.cobj_web_elements.get_common_object_wifi0_client_mode().is_selected():
                self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi0_client_mode())

        if client_access_status_wifi0.upper() == "ENABLE":
            self.utils.print_info("Enable Client Access Checkbox on WiFi0 Interface")
            if not self.cobj_web_elements.get_common_object_wifi0_client_access().is_selected():
                self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi0_client_access())
        else:
            self.utils.print_info("Disable Client Access check box on WiFi0 Interface")
            if self.cobj_web_elements.get_common_object_wifi0_client_access().is_selected():
                self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi0_client_access())

        if backhaul_mesh_status_wifi0.upper() == "ENABLE":
            self.utils.print_info("Enable Backhaul Mesh Link Checkbox on WiFi0 Interface")
            if not self.cobj_web_elements.get_common_object_wifi0_mesh_link().is_selected():
                self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi0_mesh_link())
        else:
            self.utils.print_info("Disable Backhaul Mesh Link Checkbox on WiFi0 Interface")
            if self.cobj_web_elements.get_common_object_wifi0_mesh_link().is_selected():
                self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi0_mesh_link())

        if sensor_status_wifi0.upper() == "ENABLE":
            self.utils.print_info("Enable Sensor Checkbox on WiFi0 Interface")
            if not self.cobj_web_elements.get_common_object_wifi0_sensor().is_selected():
                self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi0_sensor())
        else:
            self.utils.print_info("Disable Sensor Checkbox on WiFi0 Interface")
            if self.cobj_web_elements.get_common_object_wifi0_sensor().is_selected():
                self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi0_sensor())

        self.screen.save_screen_shot()

        if enable_SDR.upper() == "ENABLE":
            self.utils.print_info("Enable SDR Checkbox on WiFi0 Interface")
            if not self.cobj_web_elements.get_common_object_ap_template_enable_sdr().is_selected():
                self.auto_actions.click(self.cobj_web_elements.get_common_object_ap_template_enable_sdr())
                self.auto_actions.click(self.cobj_web_elements.get_common_object_ap_template_sdr_dropdown_button())
                self.auto_actions.select_drop_down_options(
                    self.cobj_web_elements.get_common_object_ap_template_sdr_dropdown(), sdr_profile_name)

        else:
            self.utils.print_info("Disable SDR Checkbox on WiFi0 Interface")
            if self.cobj_web_elements.get_common_object_ap_template_enable_sdr().is_selected():
                self.auto_actions.click(self.cobj_web_elements.get_common_object_ap_template_enable_sdr())
        self.auto_actions.scroll_up()
        return 1

    def _config_ap_template_wifi1(self, **wifi1_profile):
        """
        - Configure the WIFI1 configuration on AP Template
        - Keyword Usage
         - ``Config AP Template WiFi1  &{WIFI1_CONFIG}``

        :param wifi1_profile: (Config Dict) Enable/Disable Client mode, Client Access,Backhaul Mesh Link, Sensor
        :return: 1 if WiFi1 Profile Configured Successfully else None
        """
        client_mode_status_wifi1   = wifi1_profile.get('client_mode', 'Disable')
        client_access_status_wifi1 = wifi1_profile.get('client_access', 'Enable')
        backhaul_mesh_status_wifi1 = wifi1_profile.get('backhaul_mesh_link', 'Enable')
        sensor_status_wifi1 = wifi1_profile.get('sensor', 'Enable')
        radio_profile_wifi1 = wifi1_profile.get('radio_profile', 'radio_ng_11ax-5g')
        radio_status_wifi1 = wifi1_profile.get('radio_status', 'On')

        self.utils.print_info("Click on WiFi1 Tab on AP Template page")
        self.auto_actions.click(self.cobj_web_elements.get_common_object_ap_template_wifi1_tab())

        if radio_status_wifi1.upper() == "OFF":
            self.utils.print_info("Enable Client Access Checkbox on wifi1 Interface")
            if self.cobj_web_elements.get_common_object_wifi1_radio_status_button().is_selected():
                self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi1_radio_status_button())
            return 1
        else:
            self.utils.print_info("Disable Client Access check box on wifi1 Interface")
            if not self.cobj_web_elements.get_common_object_wifi1_radio_status_button().is_selected():
                self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi1_radio_status_button())

        self.auto_actions.scroll_down()
        self.utils.print_info(f"select Radio Profile:{radio_profile_wifi1}")
        self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi1_radio_profile_button())
        self.auto_actions.select_drop_down_options(self.cobj_web_elements.
                                                   get_common_object_wifi1_radio_profile_dropdown(),
                                                   radio_profile_wifi1)

        if client_mode_status_wifi1.upper() == "ENABLE":
            self.utils.print_info("Enable Client Mode Checkbox on WiFi1 Interface")
            if not self.cobj_web_elements.get_common_object_wifi1_client_mode().is_selected():
                self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi1_client_mode())

                wifi1_client_mode_profile = wifi1_profile['client_mode_profile']
                client_mode_profile_name  = wifi1_client_mode_profile.get('client_mode_profile_name', 'wifi1')
                client_mode_profile_dhcp  = wifi1_client_mode_profile.get('dhcp_server_scope', '192.168.150.1')
                cm_enable_local_web_page  = wifi1_client_mode_profile.get('local_web_page', 'ENABLE')
                cm_ssid_name              = wifi1_client_mode_profile.get('ssid_name', 'bk_enterprise')
                cm_password               = wifi1_client_mode_profile.get('password', 'aerohive')
                cm_auth_method            = wifi1_client_mode_profile.get('auth_method', 'Pre-Shared Key')
                cm_key_type               = wifi1_client_mode_profile.get('key_type', 'ASCII')
                self.utils.print_info("Click Add Client Mode Profile")
                self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi1_add_client_mode_profile())
                self.utils.print_info(f"Enter Client Mode Profile Name: {client_mode_profile_name}")
                self.auto_actions.send_keys(self.cobj_web_elements.get_common_object_wifi0_1_client_mode_profile_name(), client_mode_profile_name)
                if cm_enable_local_web_page.upper() == 'DISABLE':
                    self.utils.print_info(f"Enable Local Web Page: {cm_enable_local_web_page}")
                    self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi0_1_cm_local_web_page_checkbox())
                    self.utils.print_info(f"Click Add(+)")
                    self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi0_1_cm_local_web_page_add())
                    self.utils.print_info(f"Enter SSID Name: {cm_ssid_name}")
                    self.auto_actions.send_keys(self.cobj_web_elements.get_common_object_wifi0_1_cm_local_web_page_ssid_textbox(), cm_ssid_name)
                    self.utils.print_info(f"Enter Password: {cm_password}")
                    self.auto_actions.send_keys(self.cobj_web_elements.get_common_object_wifi0_1_cm_local_web_page_password_textbox(), cm_password)
                    self.utils.print_info(f"Auth Method: {cm_auth_method}")
                    self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi0_1_cm_local_web_page_auth_dropdown())
                    self.auto_actions.select_drop_down_options(self.cobj_web_elements.get_common_object_wifi0_1_cm_local_web_page_auth_dropdown_option(), cm_auth_method)
                    self.utils.print_info(f"Key Type: {cm_key_type}")
                    self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi0_1_cm_local_web_key_type_dropdown())
                    self.auto_actions.select_drop_down_options(self.cobj_web_elements.get_common_object_wifi0_1_cm_local_web_key_type_dropdown_option(), cm_key_type)
                    self.screen.save_screen_shot()
                    sleep(2)
                    self.utils.print_info(f"Click Add button")
                    self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi0_1_cm_local_web_page_add_button())
                self.utils.print_info(f"Enter DHCP Server Scope: {client_mode_profile_dhcp}")
                self.auto_actions.send_keys(self.cobj_web_elements.get_common_object_wifi0_1_client_mode_profile_dhcp_server_scope(), client_mode_profile_dhcp)
                self.screen.save_screen_shot()
                self.utils.print_info("Click Save Client Mode Profile")
                self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi0_1_client_mode_profile_save())
        else:
            self.utils.print_info("Disable Client Access check box on WiFi0 Interface")
            if self.cobj_web_elements.get_common_object_wifi1_client_mode().is_selected():
                self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi1_client_mode())


        if client_access_status_wifi1.upper() == "ENABLE":
            self.utils.print_info("Enable Client Access Checkbox on WiFi1 Interface")
            if not self.cobj_web_elements.get_common_object_wifi1_client_access().is_selected():
                self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi1_client_access())
        else:
            self.utils.print_info("Disable Client Mode check box on WiFi1 Interface")
            if self.cobj_web_elements.get_common_object_wifi1_client_access().is_selected():
                self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi1_client_access())

        if backhaul_mesh_status_wifi1.upper() == "ENABLE":
            self.utils.print_info("Enable Backhaul Mesh Link Checkbox on WiFi1 Interface")
            if not self.cobj_web_elements.get_common_object_wifi1_mesh_link().is_selected():
                self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi1_mesh_link())
        else:
            self.utils.print_info("Disable Backhaul Mesh Link Checkbox on WiFi1 Interface")
            if self.cobj_web_elements.get_common_object_wifi1_mesh_link().is_selected():
                self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi1_mesh_link())

        self.screen.save_screen_shot()
        self.auto_actions.scroll_up()

        return 1

    def _config_ap_template_wifi2(self, **wifi2_profile):
        """
        - Configure the WIFI2 configuration on AP Template
        :param wifi2_profile: (Config Dict) WiFi2 ADSP server Config ie primary server ip and port
        :return: 1 if WiFi2 Profile Configured Successfully else None
        """

        radio_status_wifi2 = wifi2_profile.get('radio_status', 'Enable')

        self.utils.print_info("Click on WiFi2 Tab on AP Template page")
        self.auto_actions.click(self.cobj_web_elements.get_common_object_ap_template_wifi2_tab())

        self.auto_actions.scroll_down()

        if radio_status_wifi2.upper() == "ENABLE":
            self.utils.print_info("Enable Radio Status on WiFi2 Interface")
            if not self.cobj_web_elements.get_common_object_wifi2_radio_status_button().is_selected():
                self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi2_radio_status_button())

                self.screen.save_screen_shot()

        else:
            self.utils.print_info("Disable Radio Status on WiFi2 Interface")
            if self.cobj_web_elements.get_common_object_wifi2_radio_status_button().is_selected():
                self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi2_radio_status_button())

                self.screen.save_screen_shot()

        """ 
        ##### APC-44337 UI Changes #####
        adsp_primary_server_ip = wifi2_profile.get('primary_server_ip', '1.1.1.1')
        adsp_primary_server_port = wifi2_profile.get('primary_server_port', '11')

        self.utils.print_info("Enter ADSP Primary Server IP Name")
        self.auto_actions.send_keys(self.cobj_web_elements.get_common_object_wifi2_primary_server_ip(),
                                    adsp_primary_server_ip)

        self.utils.print_info("Enter ADSP Primary Server port")
        self.auto_actions.send_keys(self.cobj_web_elements.get_common_object_wifi2_primary_server_port(),
                                    adsp_primary_server_port)
        """

        self.screen.save_screen_shot()
        sleep(1)
        self.auto_actions.scroll_up()

        return 1

    def _config_ap_template_wired(self, **wired_profile):
        """
        - Configure the Wired configuration on AP Template
        :param wifi2_profile: (Config Dict) Wired Config ie Ethernet Status, LLDP, CDP Config
        :return: 1 if Wired Profile Configured Successfully else None
        """
        eth0_status = wired_profile.get('eth0_status', 'Enable')
        eth1_status = wired_profile.get('eth1_status', 'Enable')
        lldp_eth0_status = wired_profile.get('lldp_eth0_status', 'Enable')
        lldp_eth1_status = wired_profile.get('lldp_eth1_status', 'Enable')
        cdp_eth0_status = wired_profile.get('cdp_eth0_status', 'Enable')
        cdp_eth1_status = wired_profile.get('cdp_eth1_status', 'Enable')

        self.auto_actions.scroll_down()

        if eth0_status.upper() == "DISABLE" and self.cobj_web_elements. \
                get_common_object_ap_template_eth0_status().is_selected():
            self.utils.print_info("Disabling Eth0")
            self.auto_actions.click(self.cobj_web_elements.get_common_object_ap_template_eth0_status())

        elif not self.cobj_web_elements. \
                get_common_object_ap_template_eth0_status().is_selected() and eth0_status.upper() == "ENABLE":
            self.utils.print_info("Enabling Eth0")
            self.auto_actions.click(self.cobj_web_elements.get_common_object_ap_template_eth0_status())

        if lldp_eth0_status.upper() == "DISABLE" and self.cobj_web_elements. \
                get_common_object_ap_template_lldp_eth0().is_selected():
            self.utils.print_info("Disabling lldp Eth0")
            self.auto_actions.click(self.cobj_web_elements.get_common_object_ap_template_lldp_eth0())

        elif not self.cobj_web_elements. \
                get_common_object_ap_template_lldp_eth0().is_selected() and lldp_eth0_status.upper() == "ENABLE":
            self.utils.print_info("Enabling lldp Eth0")
            self.auto_actions.click(self.cobj_web_elements.get_common_object_ap_template_lldp_eth0())

        if cdp_eth0_status.upper() == "DISABLE" and self.cobj_web_elements. \
                common_object_ap_template_cdp_eth0().is_selected():
            self.utils.print_info("Disabling cdp Eth0")
            self.auto_actions.click(self.cobj_web_elements.get_common_object_ap_template_cdp_eth0())

        elif not self.cobj_web_elements. \
                get_common_object_ap_template_cdp_eth0().is_selected() and cdp_eth0_status.upper() == "ENABLE":
            self.utils.print_info("Enabling cdp Eth0")
            self.auto_actions.click(self.cobj_web_elements.get_common_object_ap_template_cdp_eth0())
        try:
            if eth1_status.upper() == "DISABLE" and self.cobj_web_elements. \
                    get_common_object_ap_template_eth1_status().is_selected():
                self.utils.print_info("Disabling eth1")
                self.auto_actions.click(self.cobj_web_elements.get_common_object_ap_template_eth1_status())

            elif not self.cobj_web_elements. \
                    get_common_object_ap_template_eth1_status().is_selected() and eth1_status.upper() == "ENABLE":
                self.utils.print_info("Enabling eth1")
                self.auto_actions.click(self.cobj_web_elements.get_common_object_ap_template_eth1_status())

            if lldp_eth1_status.upper() == "DISABLE" and self.cobj_web_elements. \
                    get_common_object_ap_template_lldp_eth1().is_selected():
                self.utils.print_info("Disabling lldp eth1")
                self.auto_actions.click(self.cobj_web_elements.get_common_object_ap_template_lldp_eth1())

            elif not self.cobj_web_elements. \
                    get_common_object_ap_template_lldp_eth1().is_selected() and lldp_eth1_status.upper() == "ENABLE":
                self.utils.print_info("Enabling lldp eth1")
                self.auto_actions.click(self.cobj_web_elements.get_common_object_ap_template_lldp_eth1())

            if cdp_eth1_status.upper() == "DISABLE" and self.cobj_web_elements. \
                    common_object_ap_template_cdp_eth1().is_selected():
                self.utils.print_info("Disabling cdp eth1")
                self.auto_actions.click(self.cobj_web_elements.get_common_object_ap_template_cdp_eth1())

            elif not self.cobj_web_elements. \
                    get_common_object_ap_template_cdp_eth1().is_selected() and cdp_eth1_status.upper() == "ENABLE":
                self.utils.print_info("Enabling cdp eth1")
                self.auto_actions.click(self.cobj_web_elements.get_common_object_ap_template_cdp_eth1())
        except Exception as e:
            self.utils.print_info("Requested ethernet does not exist for this model of AP")
            self.utils.print_info(f'Actual error is :- {e}')
            return 1

        self.screen.save_screen_shot()
        self.auto_actions.scroll_up()
        return 1

    def check_ap_template_in_common_object(self, ap_template_name):
        """"
        - CONFIGURE-->COMMON OBJECTS-->Policy-->AP Templates
        - Checking the AP template presence in the AP Templates Grid
        - Keyword Usage
         - ``Check AP Template In Common Object   ${AP_TEMPLATE_NAME}``

        :param ap_template_name: AP Template Name ie AP630-TEMPLATE,AP410C-TEMPLATE etc
        :return: 1 if AP Template Found else -1
        """

        self.utils.print_info("Navigate to Policy--> AP Templates")
        self.navigator.navigate_to_policy_ap_template()

        ap_template_name = ap_template_name.replace(" ", "")

        if self.cobj_web_elements.get_common_object_policy_ap_templates_view_all_pages():
            self.utils.print_info("Click Full pages button")
            self.auto_actions.click(self.cobj_web_elements.get_common_object_policy_ap_templates_view_all_pages())

        if self._search_common_object_template(ap_template_name):
            self.utils.print_info(f"AP Template {ap_template_name} found in the CommonObject")
            return 1

        else:
            self.utils.print_info(f"AP Template {ap_template_name} not found in the CommonObject")
            return -1

    def delete_ap_templates(self, *templates):
        """
        - Flow: Configure --> Common Objects --> Policy --> AP Templates
        - Delete Templates from Template grid
        - Keyword Usage:
         - ``Delete AP Templates  ${Template1}  ${Template2}  ${Template3}``

        :param templates: (list) list of template's to delete
        :return: 1 if deleted else -1
        """
        self.navigator.navigate_to_policy_ap_template()

        if self.cobj_web_elements.get_common_object_policy_ap_templates_view_all_pages():
            self.utils.print_info("Click Full pages button")
            self.auto_actions.click(self.cobj_web_elements.get_common_object_policy_ap_templates_view_all_pages())

        select_template_flag = None
        for template in templates:
            template = template.replace(" ", "")
            if self._search_common_object_template(template):
                self._select_common_object_template_row(template)
                select_template_flag = True
            else:
                self.utils.print_info(f"Template {template} does't exists in the list")

        if not select_template_flag:
            return 1
        self._delete_common_objects()

        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)

        if "Template was deleted successfully." in tool_tp_text[-1]:
            return 1
        elif "The Device Template cannot be removed because it is used by another object" in tool_tp_text[-1]:
            return -1
        return -2

    def delete_all_ap_templates(self):
        """
        - Flow: Configure --> Common Objects --> Policy --> AP Templates
        - Delete All ap templates except default template from Template grid
        - Keyword Usage:
         - ``Delete All AP Templates``
        :return: 1 if deleted else -1
        """
        self.utils.print_info("Navigate to Configure->Common Objects->Policy->AP Template.")
        self.navigator.navigate_to_policy_ap_template()
        if self.cobj_web_elements.get_common_object_policy_ap_templates_view_all_pages():
            self.utils.print_info("Click Full pages button")
            self.auto_actions.click(self.cobj_web_elements.get_common_object_policy_ap_templates_view_all_pages())

        self.utils.print_info("Getting common object rows")
        rows = self.cobj_web_elements.get_common_object_grid_rows()
        if not rows:
            self.utils.print_info("row(s) not present in the grid")
            return 1

        select_template_flag = None
        for row in rows:
            cell = self.cobj_web_elements.get_common_object_template_grid_row_cells(row)
            if not cell:
                pass
            elif 'default-template' not in cell.text:
                self.auto_actions.click(self.cobj_web_elements.get_common_object_grid_row_cells(row, 'dgrid-selector'))
                select_template_flag = True

        if not select_template_flag:
            return 1
        self.screen.save_screen_shot()
        self._delete_common_objects()
        self.screen.save_screen_shot()
        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)
        if 'Template was successfully removed from policy.' in tool_tp_text:
            return 1
        else:
            return -1

    def delete_all_client_mode_profiles(self):
        """
        - Flow: Configure --> Common Objects --> Basic --> Client Mode Profiles
        - Delete all client mode profiles from Client Mode Profiles grid
        - Keyword Usage:
         - ``Delete All Client Mode Profiles``
        :return: 1 if deleted else -1
        """
        self.utils.print_info("Navigate to Configure->Common Objects-> Basic->Client Mode Profiles.")
        self.navigator.navigate_to_client_mode_profiles()
        rows = self.cobj_web_elements.get_common_object_basic_client_mode_profiles_grid_rows_all()
        if not rows:
            self.utils.print_info("Client Mode Profile(s) not present in the grid")
            return 1
        else:
            try:
                self.utils.print_info(len(rows), " row(s) of client mode profile(s).")
                self.utils.print_info("Selecting Device grid checkbox Icon.")
                self.auto_actions.click(self.cobj_web_elements.get_common_object_basic_client_mode_profiles_selectall())
                self.utils.print_info("Selecting Delete Icon.")
                self.auto_actions.click(self.cobj_web_elements.get_common_object_basic_client_mode_profiles_delete())
                self.utils.print_info("Confirming delete...")
                self.auto_actions.click(self.cobj_web_elements.get_common_object_basic_client_mode_profiles_delete_confirm_ok_button())
                sleep(2)
                self.screen.save_screen_shot()

                return 1
            except Exception as e:
                self.screen.save_screen_shot()
                self.utils.print_info("Unable to delete Client Mode Profiles")
                return -1

    def radio_phy_mode_fiveghz(self, model):
            """
                - Flow: Configure --> Common Objects --> Policy -->Radio Profile
                - Map the Radio phy mode based on the AP
                - Keyword Usage:
                - ``${RADIO_MODE}      Radio Phy Mode Fiveghz      ${AP1_MODEL}``
                - ``${CREATE_RADIO_PROFILE}    Create Radio Profile    ${RADIO_PROFILE_NAME}   ${RADIO_MODE}   True``
                :param model: Name of the model being used our Test
                :return: Radio phy mode based on AP model ("ax (5GHz)" or  "ac" )
            """
            AP = "AP150W", "AP250", "AP30", "AP122", "AP245X", "AP230", "AP1130"
            if model in AP:
                self.utils.print_info("DUT model is : ", model, ". So Picked phy_mode as 11AC")
                return "ac"
            else:
                self.utils.print_info("DUT model is : ", model, ". So Picked phy_mode as 11AX")
                return "ax (5GHz)"

    def radio_phy_mode_twoghz(self, model):
        """
            - Flow: Configure --> Common Objects --> Policy -->Radio Profile
            - Map the Radio phy mode based on the AP
            - Keyword Usage:
             - ``${RADIO_MODE}      Radio Phy Mode Twoghz      ${AP1_MODEL}``
             - ``${CREATE_RADIO_PROFILE}    Create Radio Profile    ${RADIO_PROFILE_NAME}   ${RADIO_MODE}``
            :param model: Name of the model being used our Test
            :return: Radio phy mode based on AP model ("ax (2.4GHz)" or "g/n")
        """
        AP = "AP150W", "AP250", "AP30", "AP122", "AP245X", "AP230", "AP1130"
        if model in AP:
            self.utils.print_info("DUT model is : ", model, ". So Picked phy_mode as 11g/n")
            return "g/n"
        else:
            self.utils.print_info("DUT model is : ", model, ". So Picked phy_mode as 11AX")
            return "ax (2.4GHz)"

    def add_imago_tag_profile(self, profile_name, server='', channel='', fcc_mode=True, server_port='default'):
        """
        - This keyword will create image Tag profile under Common Objects.
        - Flow: Configure --> Common Objects --> Policy -->ImagoTag Profiles
        - Keyword Usage:
         - ``Add Imago Tag profile  ${PROFILE_NAME}  server=${SERVER} channel=${CHANNEL}``
         - ``Add Imago Tag profile  ${PROFILE_NAME}  server=${SERVER} channel=${CHANNEL} server_port=${PORT}``
         - ``Add Imago Tag profile  ${PROFILE_NAME}  server=${SERVER} channel=${CHANNEL}  fcc_mode=False``

        :param profile_name: Imago Tag Profile name
        :param channel: Channel Number
        :param server: Server detail
        :param fcc_mode: By default fcc_mode is enabled.To Disable mention this flag as False
        :param server_port: Server Port Details
        :return: 1 if Imago Tag Profile name Created successfully else -1
        """
        self.utils.print_info("Navigate to Imago Tag in Common Object")
        self.navigator.navigate_to_policy_imago_tag_profiles()
        sleep(3)

        self.utils.print_info("Click on Add Imago Tag profile Button")
        self.auto_actions.click(self.cobj_web_elements.get_common_object_imago_tag_profile_add_button())
        sleep(2)

        self.utils.print_info("Add profile name")
        self.auto_actions.send_keys(self.cobj_web_elements.get_common_object_imago_tag_profile_name_textfield(),
                                    profile_name)

        self.utils.print_info("Add profile Description")
        self.auto_actions.send_keys(self.cobj_web_elements.get_common_object_imago_tag_profile_description_textfield(),
                                    profile_name)
        self.screen.save_screen_shot()

        self.utils.print_info("Enter Server name Textfield")
        self.auto_actions.send_keys(self.cobj_web_elements.get_common_object_imago_tag_profile_server_textfield(),
                                    server)
        self.screen.save_screen_shot()

        self.utils.print_info("clicking Speed drop down Button")
        self.auto_actions.click(self.cobj_web_elements.get_common_object_imago_tag_profile_channel_drop_down_button())
        sleep(2)

        self.utils.print_info(f"Selecting Channel Option : {channel}")
        self.auto_actions.select_drop_down_options(self.cobj_web_elements.
                                                   get_common_object_imago_tag_profile_channel_drop_down_options(),
                                                   channel)
        sleep(2)
        self.screen.save_screen_shot()

        if fcc_mode:
            self.utils.print_info("Click on Enable FCC Mode Checkbox")
            if not self.cobj_web_elements.get_common_object_imago_tag_profile_fcc_mode_checkbox().is_selected():
                self.auto_actions.click(self.cobj_web_elements.get_common_object_imago_tag_profile_fcc_mode_checkbox())
                self.screen.save_screen_shot()
                sleep(2)

        if server_port != 'default':
            self.utils.print_info("Click Advanced Settings Button")
            self.auto_actions.click(self.cobj_web_elements.get_common_object_imago_tag_profile_advanced_settings_tab())
            sleep(2)

            self.utils.print_info("Change server Port Number")
            self.auto_actions.send_keys(
                self.cobj_web_elements.get_common_object_imago_tag_profile_advanced_settings_server_port(), server_port)
            self.screen.save_screen_shot()

        self.utils.print_info("clicking Save Button")
        self.auto_actions.click(self.cobj_web_elements.get_common_object_imago_tag_profile_save_button())
        self.screen.save_screen_shot()
        sleep(5)

        self.utils.print_info("Checking Configured profile Entry on Imago Tag Profile Grid")
        rows = self.cobj_web_elements.get_imago_tag_profile_grid_rows()
        self.screen.save_screen_shot()
        sleep(2)

        if rows:
            for row in rows:
                if profile_name in row.text:
                    self.utils.print_info(f"Found Imago Tag Profile {profile_name} Row in the Grid")
                    return 1
            self.utils.print_info(f"Did not find Imago Tag Profile {profile_name} Configured")
            return -1
        else:
            self.utils.print_info(f"Did not find any Imago Tag Profile Rows")
            return -1

    def delete_imago_tag_profile(self, profile_name):
        """
        - Flow: Configure --> Common Objects --> Policy -->Imago Tag Profile
        - Delete specified Imago Tag Profile from the Imago Tag Profile grid
        - Keyword Usage:
         - ``Delete Imago Tag Profile  ${PROFILE_NAME}``
        :param profile_name: Image Tag Profile Name
        :return: 1 if deleted else -1
        """
        self.utils.print_info("Navigate to Imago Tag Profile in Common Object")
        self.navigator.navigate_to_policy_imago_tag_profiles()
        sleep(3)

        self.utils.print_info("Select and delete Imago Tag Profile row")
        self._select_delete_common_object(profile_name)
        self.screen.save_screen_shot()
        sleep(2)

        sleep(5)
        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)

        if "Successfully Deleted the ImagoTag Policy" in tool_tp_text[-1]:
            return 1
        else:
            self.utils.print_info("Unable to Delete Image Tag Policy")
            return -1

    def edit_imago_tag_profile(self, profile_name, server='', channel='', fcc_mode=True, server_port=''):
        """
        - This keyword will Edit Existing image Tag profile under Common Objects.
        - Flow: Configure --> Common Objects --> Policy -->Select ImagoTag Profile --> Edit
        - Keyword Usage:
         - ``Edit Imago Tag profile  ${PROFILE_NAME}  server=${SERVER}``
         - ``Edit Imago Tag profile  ${PROFILE_NAME}  channel=${CHANNEL}``
         - ``Edit Imago Tag profile  ${PROFILE_NAME}  server_port=${SERVER_PORT}``
         - ``Edit Imago Tag profile  ${PROFILE_NAME}  server=${SERVER} channel=${CHANNEL}  fcc_mode=False``

        :param profile_name: Imago Tag Profile name
        :param channel: Channel Number
        :param server: Server detail
        :param fcc_mode: By default fcc_mode is enabled.To Disable mention this flag as False
        :param server_port: Server Port Details
        :return: 1 if Imago Tag Profile Edited successfully else -1
        """
        self.utils.print_info("Navigate to Imago Tag in Common Object")
        self.navigator.navigate_to_devices()
        self.navigator.navigate_to_policy_imago_tag_profiles()
        sleep(5)

        rows = self.cobj_web_elements.get_imago_tag_profile_grid_rows()
        self.screen.save_screen_shot()
        sleep(2)

        if rows:
            for row in rows:
                if profile_name in row.text:
                    self.utils.print_info(f"Selecting Imago Tag Profile {profile_name} Row in the Grid")
                    self.auto_actions.click(self.cobj_web_elements.get_imago_tag_profile_select_checkbox(row))
                    self.screen.save_screen_shot()
                    sleep(2)

                    self.utils.print_info(f"Click Edit Button")
                    self.auto_actions.click(self.cobj_web_elements.get_imago_tag_profile_edit_button())
                    self.screen.save_screen_shot()
                    sleep(2)
        else:
            self.utils.print_info(f"Imago Tag Profile Rows Not Found on Grid")
            return -1

        if server:
            self.utils.print_info("Change Server name Textfield")
            self.auto_actions.send_keys(self.cobj_web_elements.get_common_object_imago_tag_profile_server_textfield(),
                                        server)
            self.screen.save_screen_shot()

        if channel:
            self.utils.print_info("clicking Channel drop down Button")
            self.auto_actions.\
                click(self.cobj_web_elements.get_common_object_imago_tag_profile_channel_drop_down_button())
            sleep(2)

            self.utils.print_info(f"Changing Channel Option : {channel}")
            self.auto_actions.select_drop_down_options(self.cobj_web_elements.
                                                       get_common_object_imago_tag_profile_channel_drop_down_options(),
                                                       channel)
            sleep(2)
            self.screen.save_screen_shot()

        if fcc_mode:
            self.utils.print_info("Click on Enable FCC Mode Checkbox")
            if not self.cobj_web_elements.get_common_object_imago_tag_profile_fcc_mode_checkbox().is_selected():
                self.auto_actions.click(self.cobj_web_elements.get_common_object_imago_tag_profile_fcc_mode_checkbox())
                self.screen.save_screen_shot()
                sleep(2)

        if server_port:
            self.utils.print_info("Click Advanced Settings Button")
            self.auto_actions.click(self.cobj_web_elements.get_common_object_imago_tag_profile_advanced_settings_tab())
            sleep(2)

            self.utils.print_info("Changing server Port Number")
            self.auto_actions.send_keys(
                self.cobj_web_elements.get_common_object_imago_tag_profile_advanced_settings_server_port(), server_port)
            self.screen.save_screen_shot()

        self.utils.print_info("clicking Save Button")
        self.auto_actions.click(self.cobj_web_elements.get_common_object_imago_tag_profile_save_button())
        self.screen.save_screen_shot()
        sleep(5)

        sleep(5)
        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)

        if "Succesfully Updated" in tool_tp_text[-1]:
            return 1
        else:
            self.utils.print_info("Unable to Edit Image Tag Policy Successfully")
            return -1

    def create_ip_firewall_policy_for_applications(self, policy_name, application='', source_ip='Any',
                                                   destination_ip='Any', action='Permit'):
        """
         - This Keyword will Create IP Firewall Policy for Application Access.
         - Flow: Configure --> Common Objects --> Security -->IP Firewall Policies --> Add
         - Keyword Usage:
          - ``Create IP Firewall Policy For Applications    ${POLICY_NAME}  application=${APP_NAME}  action=${ACTION}``
          - ``Create IP Firewall Policy For Applications    ${POLICY_NAME}  application=${APP_NAME1},${APP_NAME2}
          action=${ACTION}``

        :param policy_name: IP Firewall Policy Name
        :param application: Application Name or Application List
        :param source_ip: Source IP with Default Option Any
        :param destination_ip: Destination IP with Option Default Any
        :param action: Firewall Policy Action Either Permit or Deny
        :return: 1 if IP Firewall Policy Created Successfully else -1
        """
        self.utils.print_info("Navigate to IP Firewall Policies in Common Object")
        self.navigator.navigate_to_security_ip_firewall_policies()
        sleep(3)

        self.utils.print_info("Click on Add IP Firewall Policy Button")
        self.auto_actions.click(self.cobj_web_elements.get_common_object_ip_firewall_policy_add_button())
        sleep(2)

        self.utils.print_info("Add IP Firewall Policy Name")
        self.auto_actions.send_keys(self.cobj_web_elements.get_common_object_ip_firewall_policy_name_textfield(),
                                    policy_name)

        self.utils.print_info("Add IP Firewall Policy Description")
        self.auto_actions.send_keys(self.cobj_web_elements.get_common_object_ip_firewall_policy_description_textfield(),
                                    policy_name)
        self.screen.save_screen_shot()

        self.utils.print_info("Click on IP Firewall Policy Add Rule Button")
        self.auto_actions.click(self.cobj_web_elements.get_common_object_ip_firewall_policy_add_rule_button())
        sleep(2)

        self.utils.print_info("Click on IP Firewall Policy Add Rule Select Button")
        self.auto_actions.click(self.cobj_web_elements.get_common_object_ip_firewall_policy_add_rule_select_button())
        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Click on Application Tab")
        self.auto_actions.click(self.cobj_web_elements.get_common_object_ip_firewall_policy_add_rule_application_tab())
        self.screen.save_screen_shot()
        sleep(4)

        rows = self.cobj_web_elements.get_common_object_ip_firewall_policy_add_rule_select_application_rows()
        application_list = re.split('[,]', application)
        for application_name in application_list:
            for row in rows:
                if application_name in row.text:
                    self.auto_actions.click(self.cobj_web_elements.
                                            get_firewall_policy_add_rule_select_application_check_box(row))
                    self.screen.save_screen_shot()
                    sleep(2)

        self.utils.print_info("Click Save Application Button")
        self.auto_actions.click(self.cobj_web_elements.
                                get_common_object_ip_firewall_policy_select_application_save_button())
        self.screen.save_screen_shot()

        if source_ip != 'Any':
            pass

        if destination_ip != 'Any':
            pass

        self.utils.print_info(f"Select IP Firewall Policy Action : {action}")
        self.auto_actions.click(self.cobj_web_elements.get_common_object_ip_firewall_policy_rule_action_dropdown_button())
        self.auto_actions.select_drop_down_options(
            self.cobj_web_elements.get_common_object_ip_firewall_policy_rule_action_dropdown_options(), action)

        self.utils.print_info("Click Save IP Firewall Policy Button")
        self.auto_actions.click(self.cobj_web_elements.get_common_object_ip_firewall_policy_save_button())
        self.screen.save_screen_shot()

        sleep(5)
        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)

        if "IP firewall policy was saved successfully." in tool_tp_text[-1]:
            self.utils.print_info("Successfully Created IP firewall policy with Mentioned Application/Applications")
            return 1
        else:
            self.utils.print_info("Unable Create IP firewall policy with Application")
            return -1

    def select_ip_firewall_policy_for_new_user_profile(self, user_profile_name='', firewall_policy_name=''):
        """
        - This Keyword will Select Configured IP Firewall Policy Under New User Profile.
        - Flow: Configure --> Common Objects --> Policy --> User Profiles
         - Keyword Usage:
          - ``Select IP Firewall Policy For New User Profile   user_profile_name=${PROFILE_NAME}
          firewall_policy_name=${FW_POLICY_NAME}``

        :param user_profile_name: User Profile Name
        :param firewall_policy_name: Already Created Firewall Policy Name
        :return: 1 if IP Firewall Policy Selected Successfully under New User File Created else -1
        """
        self.utils.print_info("Navigate to User Profiles under Common Object---->Policy")
        self.navigator.navigate_to_policy_user_profiles()
        self.screen.save_screen_shot()
        sleep(3)

        self.utils.print_info("Click on Add User Profile Button")
        self.auto_actions.click(self.cobj_web_elements.get_common_object_user_profile_add_button())

        self.utils.print_info("Add IP Firewall Policy Name")
        self.auto_actions.send_keys(self.cobj_web_elements.get_common_object_policy_user_profile_name_textfield(),
                                    user_profile_name)
        self.screen.save_screen_shot()

        self.utils.print_info("Click on Security Tab")
        self.auto_actions.click(self.cobj_web_elements.get_common_object_policy_user_profile_security_tab())
        self.screen.save_screen_shot()

        self.utils.print_info("Click Firewall Rules Radio Button")
        if not self.cobj_web_elements.get_common_object_user_profile_firewall_rules_radio_button().is_selected():
            self.auto_actions.click(self.cobj_web_elements.get_common_object_user_profile_firewall_rules_radio_button())
            self.screen.save_screen_shot()
            sleep(3)

        self.utils.print_info("Click on Select IP Firewall Policy Button")
        self.auto_actions.click(self.cobj_web_elements.get_common_object_user_profile_select_ip_firewall_policy_button())
        self.screen.save_screen_shot()
        sleep(4)

        fw_policy_rows = self.cobj_web_elements.get_firewall_policy_select_dialog_rows()
        if not fw_policy_rows:
            self.utils.print_info(
                "Firewall Policy: {} doesn't exist, Please create it".format(firewall_policy_name))
            self.auto_actions.click(self.cobj_web_elements.get_firewall_policy_select_dialog_cancel_button())
            self.screen.save_screen_shot()
            sleep(2)
            return -1

        for row in fw_policy_rows:
            if firewall_policy_name.upper() in row.text.upper():
                self.auto_actions.click(self.cobj_web_elements.get_firewall_policy_select_dialog_row_checkbox(row))
                self.screen.save_screen_shot()
                sleep(2)

                self.utils.print_info("Click on Select Button")
                self.auto_actions.click(self.cobj_web_elements.get_firewall_policy_select_dialog_select_button())
                self.screen.save_screen_shot()
                sleep(2)
                break

        self.utils.print_info("Click User Profile Save Button")
        self.auto_actions.click(self.cobj_web_elements.get_user_profile_save_button())
        self.screen.save_screen_shot()
        sleep(2)

        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)

        if "User profile was saved successfully." in tool_tp_text[-1]:
            self.utils.print_info("Successfully Selected IP firewall policy Under New User Profile")
            return 1
        else:
            self.utils.print_info("Unable Select IP firewall policy Under New User Profile")
            return -1

    def delete_management_options(self, management_options_name):
        """
        - Flow: Configure --> Common Objects --> Network -->Management Options-->Delete Management Option Name
        - Delete specified Management Options Name from the Management Options Grid
        - Keyword Usage:
         - ``Delete Management Options  ${NAME}``
        :param management_options_name: Management Options Name
        :return: 1 if deleted else -1
        """
        self.utils.print_info("Navigate to Management Options in Common Object")
        self.navigator.navigate_to_common_objects_management_options()
        sleep(3)

        self.utils.print_info("Select and Delete Management Options row")
        self._select_delete_common_object(management_options_name)
        self.screen.save_screen_shot()
        sleep(2)

        sleep(5)
        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)

        if "Management options were deleted successfully" in tool_tp_text[-1]:
            return 1
        else:
            self.utils.print_info("Unable to Delete Management options")
            return -1

    def add_network_management_options(self,  option_name="management_option_1", enable_legacy_http_redirect="True"):
        """
        - Adds new network management option(s)
        -Flow: Configure --> Common Objects --> Network -->Management Options
           - Keyword Usage:
            - ``Add Network Management Options``
        :param option_name : name of the management option
        :param enable_legacy_http_redirect: determines if enable legacy http redirect should be clicked or not
        :return: 1
        """
        self.navigator.navigate_to_common_objects_management_options()
        sleep(5)

        self.utils.print_info("Clicking on the Add Management Options Button")
        add_button = self.network_management_options_elements.get_add_network_management_options_entry()
        if add_button:
            self.auto_actions.click(add_button)
            sleep(5)
            self.utils.print_info("Set Name for new Add Management Options Entry")
            name_txt_field = self.network_management_options_elements.get_new_management_option_name()
            if name_txt_field:
                self.auto_actions.send_keys(name_txt_field, option_name)
                if enable_legacy_http_redirect.lower() == "true":
                    self.utils.print_info("Enabling legacy http redirect")
                    enable_legacy_http_redirect_checkbox = self.network_management_options_elements.\
                        get_legacy_http_redirect()
                    if enable_legacy_http_redirect_checkbox:
                        self.auto_actions.click(enable_legacy_http_redirect_checkbox)
                    else:
                        self.utils.print_info("Unable to enable legacy http redirect")
                        return -1
                self.utils.print_info("Saving configuration")
                save_button = self.network_management_options_elements.get_save_button()
                if save_button:
                    self.auto_actions.click(save_button)
                    return 1
                else:
                    self.utils.print_info("Unable save configuration")
                    return -1
            else:
                self.utils.print_info("Unable to set  Name field for new Add Management Options Entry")
                return -1
        else:
            self.utils.print_info("Unable to click on the Add Management Options Button")
        return 1

    def delete_user_profile(self, profile="user004"):
        """
        - It deletes user profile
        -Flow: Configure --> Common Objects --> User Profile
           - Keyword Usage:
            - ``Delete User Profile       profile=${PROFILE}``

        :param profile : profile name
        :return: 1
        """
        self.navigator.navigate_to_common_object_user_profile()
        sleep(5)

        self.utils.print_info("Gathering all the user profiles in the profile table")
        profile_rows = self.user_profile_web_elements.get_user_profile_grid_rows()
        profile_was_located = False
        if profile_rows:
            self.utils.print_info("Checking profile list to see if " + profile + " is in the list")
            for row in profile_rows:
                self.utils.print_info(row.text)
                if profile.lower().strip() == row.text.lower().strip():
                    self.utils.print_info("Profile " + profile + " found")
                    profile_was_located = True
                    self.utils.print_info("Selecting the row")
                    row_elements = self.user_profile_web_elements.get_all_profile_row_cells(row)
                    check_box = row_elements[0]
                    if check_box:
                        self.auto_actions.click(check_box)
                        self.utils.print_info("Clicking on the delete button")
                        delete_button = self.user_profile_web_elements.get_user_profile_delete()
                        if delete_button:
                            self.auto_actions.click(delete_button)
                            sleep(5)
                            self.utils.print_info("Clicking yes on the confirm delete popup")
                            confirm_yes = self.user_profile_web_elements.get_user_profile_confirm_delete_yes()
                            if confirm_yes:
                                self.auto_actions.click(confirm_yes)
                                return 1
                            else:
                                self.utils.print_info("Unable to click yes on the confirm delete popup")
                                return -1
                        else:
                            self.utils.print_info("Unable to click the delete button")
                            return -1
                    else:
                        self.utils.print_info("Unable to select the row")
                        return -1

            if not profile_was_located:
                self.utils.print_info("Profile " + profile + "was NOT found")
                return -1
        else:
            self.utils.print_info("Unable to gather user profiles")
            return -1
        return -1

    def delete_ip_firewall_policy(self, ip_firewall_policy_name):
        """
        - Delete specified IP Firewall Policy Name from the Grid
        - Keyword Usage:
        - Flow: Flow: Configure --> Common Objects --> Security -->IP Firewall Policies
         - ``Delete Ip Firewall Policy  ${NAME}``
        :param ip_firewall_policy_name: IP Firewall Policy Name
        :return: 1 if deleted else -1
        """
        self.utils.print_info("Navigate to IP Firewall Policies in Common Object")
        self.navigator.navigate_to_security_ip_firewall_policies()
        sleep(3)

        self.utils.print_info("Select and Delete IP Firewall Policy row")
        tool_tp_text = self._select_delete_common_object(ip_firewall_policy_name)
        self.screen.save_screen_shot()
        sleep(2)

        if "IP firewall policy was deleted successfully" in tool_tp_text[-1]:
            return 1
        else:
            self.utils.print_info(f"Unable to Delete IP Firewall Policy {ip_firewall_policy_name}")
            return -1
