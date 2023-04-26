import re
from time import sleep

import selenium.common.exceptions

from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from extauto.common.CommonValidation import CommonValidation

from extauto.xiq.flows.common.Navigator import Navigator
import extauto.xiq.flows.common.ToolTipCapture as tool_tip
from extauto.xiq.flows.configure.RadiusServer import RadiusServer
from extauto.xiq.elements.CommonObjectsWebElements import CommonObjectsWebElements
from extauto.xiq.elements.WirelessCWPWebElements import WirelessCWPWebElements
from extauto.xiq.elements.WirelessWebElements import WirelessWebElements
from extauto.xiq.elements.NetworkManagementOptionsElements import NetworkManagementOptionsElements
from extauto.xiq.elements.UserProfileWebElements import UserProfileWebElements
from extauto.xiq.xapi.configure.XapiNetworkPolicy import XapiNetworkPolicy


class CommonObjects(object):

    def __init__(self):
        self.utils = Utils()
        self.screen = Screen()
        self.auto_actions = AutoActions()
        self.navigator = Navigator()
        self.cobj_web_elements = CommonObjectsWebElements()
        self.cwp_web_elements = WirelessCWPWebElements()
        self.radius_server = RadiusServer()
        self.wireless_web_elements = WirelessWebElements()
        self.network_management_options_elements = NetworkManagementOptionsElements()
        self.user_profile_web_elements = UserProfileWebElements()
        self.common_validation = CommonValidation()
        self.xapiNetworkPolicy = XapiNetworkPolicy()

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
        self.auto_actions.click(self.cobj_web_elements.get_basic_tab())
        sleep(2)

        self.utils.print_info("Click on ip objects/host name button")
        self.auto_actions.click(self.cobj_web_elements.get_ip_object_host_name_button())
        sleep(2)

    def _get_common_object_row(self, search_string, retries=0):
        """
        Getting the row in Common Object is same for all the objects
        :param search_string:
        :return:
        """
        try:
            self.utils.print_info("Getting common object rows")
            rows = self.cobj_web_elements.get_common_object_grid_rows()
            if rows:
                for row in rows:
                    if cell := self.cobj_web_elements.get_common_object_grid_row_cells(row):
                        if cell.text == search_string:
                            return row
        except Exception:
            if retries > 5:
                retries += 1
                return self._get_common_object_row(search_string, retries)
        self.utils.print_info(f"common object row {search_string} not present")
        self.screen.save_screen_shot()
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
        self.screen.save_screen_shot()
        sleep(2)

    def _delete_common_objects(self):
        """
        Click on delete button and confirmation YES Windows,
        This is common for all objects
        :return:
        """
        self.utils.print_info("Clicking on delete button")
        delete_button = self.cobj_web_elements.get_common_objects_delete_button()
        if delete_button:
            self.utils.print_info("Clicking on delete button")
            self.auto_actions.click(delete_button)
        self.screen.save_screen_shot()
        sleep(2)

        confirm_delete_btn = self.cobj_web_elements.get_common_object_confirm_delete_button()
        if confirm_delete_btn:
            self.utils.print_info("Clicking on confirm Yes button")
            self.auto_actions.click(confirm_delete_btn)
        self.screen.save_screen_shot()
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

    def delete_ssid(self, ssid_name, **kwargs):
        """
        - Flow: Configure --> Common Objects --> Policy -->SSIDs
        - Delete SSID from the ssid grid
        - Keyword Usage:
        - ``Delete SSID  ${SSID_NAME}``

        :param ssid_name: Name of the ssid_name
        :return: 1 if deleted else -1
        """

        # Wating for XAPI SDK Support
        # if self.xapiNetworkPolicy.is_xapi_enabled(**kwargs):
        #     return self.xapiNetworkPolicy.xapi_delete_ssids([ssid_name], **kwargs)

        self.navigator.navigate_to_ssids()
        self.screen.save_screen_shot()
        sleep(5)

        if not self._search_common_object(ssid_name):
            kwargs['pass_msg'] = f"SSID Name {ssid_name} doesn't exist in the list"
            self.common_validation.passed(**kwargs)
            return 1

        self.utils.print_info(f"Select and delete SSID {ssid_name}")
        tool_tp_text = self._select_delete_common_object(ssid_name)

        self.utils.print_info(f"Tooltip text list:{tool_tp_text}")
        for value in tool_tp_text:
            if "cannot be deleted because this item is still used by another item " in value:
                kwargs['fail_msg'] = f"Cannot be deleted because this item is still used by another item {value}"
                self.common_validation.fault(**kwargs)
                return -1
            elif "Deleted SSID successfully" in value:
                kwargs['pass_msg'] = f"Successfully deleted SSID {ssid_name}"
                self.common_validation.passed(**kwargs)
                return 1

        if self._search_common_object(ssid_name):
            kwargs['fail_msg'] = "Unable to delete the SSID!"
            self.common_validation.failed(**kwargs)
            return -1

        kwargs['pass_msg'] = "Successfully deleted the SSID!"
        self.common_validation.passed(**kwargs)
        return 1

    def delete_ssids(self, *ssids, **kwargs):
        """
        - Flow: Configure --> Common Objects --> Policy -->SSIDs
        - Delete ssid's from ssid grid
        - Keyword Usage:
        - ``Delete ssids  ${SSID1}  ${SSID2}  ${SSID3}``

        :param ssids: (list) list of ssid's to delete
        :return: 1 if deleted else -1
        """

        # Wating for XAPI SDK Support
        # if self.xapiNetworkPolicy.is_xapi_enabled(**kwargs):
        #     return self.xapiNetworkPolicy.xapi_delete_ssids(*ssids, **kwargs)

        self.navigator.navigate_to_ssids()
        self.screen.save_screen_shot()
        sleep(5)

        self.utils.print_info("Click on full page view")
        if self.cobj_web_elements.get_page_size_element():
            self.auto_actions.click_reference(self.cobj_web_elements.get_page_size_element)
            self.screen.save_screen_shot()
            sleep(5)

        # Get the total pages
        pages = self.cobj_web_elements.get_page_numbers()
        if pages.text != '':
            last_page = int(pages.text[-1])
        else:
            last_page = 1
        page_counter = 0
        self.utils.print_info(f"There are {last_page} page(s) to check")
        ssid_found = False
        while page_counter < last_page:
            self.utils.print_info(f"Checking SSID's in the Page {page_counter+1}")
            for ssid in ssids:
                if self._search_common_object(ssid):
                    self._select_common_object_row(ssid)
                    ssid_found = True
                    self._delete_common_objects()
                else:
                    self.utils.print_info(f"SSID {ssid} doesn't exist in the page {page_counter+1}")

            # goto the next page
            page_counter += 1
            if (page_counter < last_page):
                self.utils.print_info(f"Move to next page {page_counter+1}")
                self.auto_actions.click_reference(self.cobj_web_elements.get_next_page_element)
                sleep(5)
            else:
                self.utils.print_info(f"There are no more pages to check.  Checking ended on page {page_counter}")

        if ssid_found == False:
            kwargs['pass_msg'] = "Given SSIDs are not present. Nothing to delete!"
            self.screen.save_screen_shot()
            self.common_validation.passed(**kwargs)
            return 1

        sleep(2)
        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(f"Tooltip text list:{tool_tp_text}")
        for value in tool_tp_text:
            if "cannot be deleted because this item is still used by another item " in value:
                kwargs['fail_msg'] = f"Cannot be deleted because this item is still used by another item {value}"
                self.common_validation.fault(**kwargs)
                return -1
            elif "Deleted SSID successfully" in value:
                kwargs['pass_msg'] = "Successfully deleted SSIDs"
                self.common_validation.passed(**kwargs)
                return 1

        for ssid in ssids:
            if self._search_common_object(ssid):
                kwargs['fail_msg'] = "Unable to delete SSIDs"
                self.common_validation.failed(**kwargs)
                return -1
        kwargs['pass_msg'] = "Successfully deleted SSIDs"
        self.common_validation.passed(**kwargs)
        return 1

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
        if self.cobj_web_elements.get_page_size_element():
            self.auto_actions.click_reference(self.cobj_web_elements.get_page_size_element)
            sleep(3)

        exclude_list = exclude_list.split(",")
        np_list = self._get_ssid_list()

        delete_ssid_list = [np for np in np_list if np not in exclude_list]
        self.utils.print_info(f"Deleting SSIDs list:{delete_ssid_list}")

        return self.delete_ssids(*delete_ssid_list)

    def delete_captive_web_portal(self, cwp_name, **kwargs):
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
            kwargs['pass_msg'] = "CWP Name doesn't exists in the list"
            self.common_validation.passed(**kwargs)
            return 1

        self.utils.print_info("Select and delete Captive Web Portal row")
        tool_tp_text = self._select_delete_common_object(cwp_name)

        self.utils.print_info(tool_tp_text)
        for value in tool_tp_text:
            if "cannot be removed because it is used by another object" in value:
                kwargs['fail_msg'] = "Cannot be removed because it is used by another object"
                self.common_validation.fault(**kwargs)
                return -1
            elif "Deleted captive web portal successfully" in value:
                kwargs['pass_msg'] = "Deleted captive web portal successfully"
                self.common_validation.passed(**kwargs)
                return 1

        kwargs['fail_msg'] = "Failed to delete captive web portal from the grid"
        self.common_validation.failed(**kwargs)
        return -1

    def delete_captive_web_portals(self, *cwp_names, **kwargs):
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

        if self.cobj_web_elements.get_page_size_element():
            self.auto_actions.click(self.cobj_web_elements.get_page_size_element())
            sleep(3)

        for cwp in cwp_names:
            if self._search_common_object(cwp):
                self._select_common_object_row(cwp)
                cwp_flag = True
            else:
                self.utils.print_info(f"cwp:{cwp} doesn't exists in the list")

        if not cwp_flag:
            return 1
        self._delete_common_objects()
        sleep(5)
        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)
        for value in tool_tp_text:
            if "cannot be removed because it is used by another object" in value:
                kwargs['fail_msg'] = "Cannot be removed because it is used by another object"
                self.common_validation.fault(**kwargs)
                return -1
            elif "Deleted captive web portal successfully" in value:
                kwargs['pass_msg'] = "Deleted captive web portal successfully"
                self.common_validation.passed(**kwargs)
                return 1

        kwargs['fail_msg'] = "Failed to delete captive web portals from the grid"
        self.common_validation.failed(**kwargs)
        return -1

    def delete_all_captive_web_portals(self, exclude_list=''):
        """
        - Flow: Configure --> Common Objects --> Authentication --> Captive Web Portal
        - Delete captive web portals from the grid
        - Keyword Usage:
        - ``Delete All Captive Web Portals   exclude_list=${cwp1},${cwp2}``
        :param exclude_list: list of cwps to exclude from delete
        :return: 1 deleted
                -1 cannot be removed because it is used by another object
        """
        exclude_list = exclude_list.split(",")
        np_list = []

        self.navigator.navigate_to_captive_web_portal()
        self.utils.print_info("Click on 50 page size")

        if self.cobj_web_elements.get_page_size_element():
            self.auto_actions.click(self.cobj_web_elements.get_page_size_element())
            sleep(3)

        for row in self.cobj_web_elements.get_common_object_grid_rows():
            if cell := self.cobj_web_elements.get_common_object_grid_row_cells(row):
                np_list.append(cell.text)

        delete_cwp_list = [np for np in np_list if np not in exclude_list]
        self.utils.print_info(f"Deleting Captive Web Portal list: {delete_cwp_list}")
        self.navigator.navigate_to_ssids()

        return self.delete_captive_web_portals(*delete_cwp_list)

    def delete_external_radius_server(self, radius_server, **kwargs):
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
            kwargs['pass_msg'] = "Radius server doesn't exists in the list"
            self.common_validation.passed(**kwargs)
            return 1

        self.utils.print_info("select  and delete radius server row")
        tool_tp_text = self._select_delete_common_object(radius_server)

        for value in tool_tp_text[::-1]:
            if "The External RADIUS Server cannot be removed because it is used by another object" in value:
                self.utils.print_info(value)
                kwargs['fail_msg'] = "The External RADIUS Server cannot be removed because it is used by another object"
                self.common_validation.fault(**kwargs)
                return -1

        kwargs['pass_msg'] = "Radius server doesn't exists in the list"
        self.common_validation.passed(**kwargs)
        return 1

    def delete_radius_server_group(self, radius_group_name, **kwargs):
        """
        - Flow: Configure --> Common Objects --> Policy --> SSIDs --> Add(+)
          --> select enterprise network --> Authenticate via RADIUS Server(Select)
        - Delete Radius Server Group from grid
        - Keyword Usage:
        - ``Delete Radius Server Group    ${RADIUS_SERVER_GROUP_NAME}``

        :param radius_group_name: Name of the radius group to delete
        :return: 1 if deleted else -1
        """
        self.navigator.navigate_to_ssids()
        self.screen.save_screen_shot()
        sleep(2)
        try:
            self.utils.print_info("Click Add(+) SSID Button")
            self.auto_actions.click_reference(self.cobj_web_elements.get_common_object_policy_add_ssid_button)
            self.utils.print_info("Click SSID Authentication Enterprise Tab")
            self.auto_actions.click_reference(self.wireless_web_elements.get_wireless_authtype_enterprise)
            self.utils.print_info("Delete Radius Server Group")
            self.radius_server.delete_radius_server_group(radius_group_name)
        except Exception as e:
            kwargs['fail_msg'] = f"Actual error is :- {e}"
            self.common_validation.fault(**kwargs)
            return -1

        kwargs['pass_msg'] = "delete_radius_group() success"
        self.common_validation.passed(**kwargs)
        return 1

    def delete_ip_object_hostname(self, object_name, **kwargs):
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
            kwargs['pass_msg'] = "Ip/Hostname object doesn't exists in the list"
            self.common_validation.passed(**kwargs)
            return 1

        self.utils.print_info("select and delete ip/hostname object")
        tool_tp_text = self._select_delete_common_object(object_name)

        for value in tool_tp_text[::-1]:
            if "The IP Object/Hostname cannot be removed because it is used by another object" in value:
                kwargs['fail_msg'] = "The IP Object/Hostname cannot be removed because it is used by another object"
                self.common_validation.fault(**kwargs)
                return -1
            elif "IP object or host name was deleted successfully" in value:
                kwargs['pass_msg'] = "IP object or host name was deleted successfully"
                self.common_validation.passed(**kwargs)
                return 1

        kwargs['fail_msg'] = "Failed to delete the ip object or hostname from Basic-->IP Objects/ Hostname"
        self.common_validation.failed(**kwargs)
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

    def edit_captive_web_portal_social_login_configuration(self, cwp_template_config, **kwargs):
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
            kwargs['pass_msg'] = "CWP Name doesn't exists in the list"
            self.common_validation.passed(**kwargs)
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
            kwargs['pass_msg'] = "Captive web portal was saved successfully!"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Failed to save captive web portal."
            self.common_validation.failed(**kwargs)
            return -1

    def delete_aaa_server_profile(self, aaa_profile_name, **kwargs):
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
            kwargs['pass_msg'] = "AAA Profile Name({}) doesn't exists in the list.".format(aaa_profile_name)
            self.common_validation.passed(**kwargs)
            return 1

        self.utils.print_info("Select and delete AAA Profile row")
        self._select_delete_common_object(aaa_profile_name)

        sleep(5)
        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)

        for value in tool_tp_text:
            if "AAA Server Profile was deleted successfully" in value:
                kwargs['pass_msg'] = "AAA Server Profile was deleted successfully"
                self.common_validation.passed(**kwargs)
                return 1

        kwargs['fail_msg'] = "Failed to delete AAA server profile."
        self.common_validation.failed(**kwargs)
        return -1

    def delete_ad_server(self, ad_server_name, **kwargs):
        """
        - Flow: CONFIGURE-->COMMON OBJECTS-->AUTHENTICATION-->AD SERVERS
        - Delete AD server profile from the grid
        -Keyword Usage:
        - ``Delete AD Server   ${AD_SERVER_NAME}``

        :param ad_server_name: Name of AD server
        :return: 1 if deleted else -1
        """
        self.utils.print_info("Navigate to AD Servers")
        self.navigator.navigate_to_ad_servers()
        if not self._search_common_object(ad_server_name):
            kwargs['pass_msg'] = "AD Server Name({}) doesn't exists in the list.".format(ad_server_name)
            self.common_validation.passed(**kwargs)
            return 1

        self.utils.print_info("Select and delete AD Server row: ", ad_server_name)
        self._select_delete_common_object(ad_server_name)

        sleep(5)
        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)

        for value in tool_tp_text:
            if "Deleted Active Directory server successfully" in value:
                kwargs['pass_msg'] = "Deleted AD server successfully"
                self.common_validation.passed(**kwargs)
                return 1

        kwargs['fail_msg'] = "Failed to delete AD server."
        self.common_validation.failed(**kwargs)
        return -1

    def delete_port_type_profile(self, port_type_name, **kwargs):
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

        self.utils.print_info("Searching for 100 rows per page button...")
        view_all_pages = self.cobj_web_elements.get_common_object_policy_port_types_view_all_pages()
        if view_all_pages:
            self.utils.print_info("Found the 100 rows per page button! Clicking...")
            self.auto_actions.click(view_all_pages)
        else:
            self.utils.print_info("100 rows per page button was not found. Continue running...")

        self.utils.print_info("Waiting for the rows to load...")
        self.utils.wait_till(self.cobj_web_elements.get_common_object_grid_rows, delay=3)

        self.utils.print_info(f"Searching {port_type_name} profile on all pages...")
        current_page = 1
        while True:
            self.utils.print_info(f"Searching: {port_type_name} profile, on page: {current_page}...")
            try:
                if not self._search_common_object(port_type_name):
                    self.utils.print_info(f"Port Type Profile Name: {port_type_name} is not present on page: "
                                          f"{str(current_page)}")
                    self.utils.print_info("Checking the next page: ", str(current_page+1) + ' ...')
                    self.utils.print_info("Clicking next page...")
                    if not self.cobj_web_elements.get_next_page_element_disabled():
                        if self.cobj_web_elements.get_next_page_element():
                            self.auto_actions.click(self.cobj_web_elements.get_next_page_element())
                            self.utils.print_info("Waiting for the rows to load...")
                            self.utils.wait_till(self.cobj_web_elements.get_common_object_grid_rows, delay=3)
                            current_page += 1
                        else:
                            kwargs['fail_msg'] = "Did not find next page button!"
                            self.common_validation.fault(**kwargs)
                            return -1
                    else:
                        self.utils.print_info("This is the last page: ", str(current_page))
                        kwargs['pass_msg'] = f"Checked all {current_page} pages for Port Type profile:{port_type_name}." \
                                             "It was already deleted or it hasn't been created yet!"
                        self.common_validation.passed(**kwargs)
                        return 1
                else:
                    self.utils.print_info(f"Found the port type profile {port_type_name}. Deleting...")
                    self._select_delete_common_object(port_type_name)
                    kwargs['pass_msg'] = "Port type profile deleted!"
                    self.common_validation.passed(**kwargs)
                    return 1

            except (selenium.common.exceptions.StaleElementReferenceException, TypeError) as e:
                self.utils.print_info("Got the following error: ", e)
                self.utils.print_info("Trying to get the rows again on page: ", str(current_page))
                continue

    def delete_sub_network_profile(self, sub_network_name, **kwargs):
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
            kwargs['pass_msg'] = "SubNetwork Space Name doesn't exists in the list"
            self.common_validation.passed(**kwargs)
            return 1

        self.utils.print_info("Select and delete SubNetwork Space row")
        self._select_delete_common_object(sub_network_name)

        sleep(5)
        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)

        for value in tool_tp_text:
            if "The subnetwork has been deleted" in value:
                kwargs['pass_msg'] = f"SubNetwork Space Name {sub_network_name} was deleted successfully"
                self.common_validation.passed(**kwargs)
                return 1

        if self._search_common_object(sub_network_name):
            kwargs['fail_msg'] = "Unable to delete the SUB NETWORK SPACE!"
            self.common_validation.failed(**kwargs)
            return -1
        else:
            kwargs['pass_msg'] = "Successfully deleted SUB NETWORK SPACE!"
            self.common_validation.passed(**kwargs)
            return 1

    def delete_vlan_profile(self, vlan_name, **kwargs):
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
            kwargs['pass_msg'] = f"VLAN Object {vlan_name} doesn't exists in the list"
            self.common_validation.passed(**kwargs)
            return 1

        self.utils.print_info("Select and delete VLAN row")
        self._select_delete_common_object(vlan_name)

        sleep(5)
        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)

        for value in tool_tp_text:
            if "VLAN has been deleted" in value:
                kwargs['pass_msg'] = f"Vlan object {vlan_name} was deleted successfully"
                self.common_validation.passed(**kwargs)
                return 1

        if self._search_common_object(vlan_name):
            kwargs['fail_msg'] = "Unable to delete the Vlan object"
            self.common_validation.failed(**kwargs)
            return -1
        else:
            kwargs['pass_msg'] = "Successfully deleted the vlan object"
            self.common_validation.passed(**kwargs)
            return 1

    def delete_all_vlan_profiles(self, **kwargs):
        """
        - Flow: CONFIGURE-->COMMON OBJECTS-->BASIC-->VLAN's
        - Delete Vlans in Common Object from the grid
        - Keyword Usage:
        - ``Delete All Vlan Profiles``
        :return: 1 if vlans deleted successfully else returns -1
        """
        exclude_list = ['1', 'Mgmt-4048']
        self.utils.print_info("Navigate to Basic--> VLANS Settings")
        self.navigator.navigate_to_basic_vlans_tab()
        if rows := self.cobj_web_elements.get_common_object_grid_rows():
            for row in rows:
                vlan_name = self.cobj_web_elements.get_common_object_grid_row_cells(row)
                if exclude_list[0] == vlan_name.text.strip() or exclude_list[1] == vlan_name.text.strip():
                    continue
                self.utils.print_info("Selecting the row ", vlan_name.text)
                self.auto_actions.click(self.cobj_web_elements.get_common_object_grid_row_cells(row, 'dgrid-selector'))
            self.utils.print_info("Clicking on the delete button")
            self.auto_actions.click_reference(self.user_profile_web_elements.get_vlan_profile_delete)
            sleep(3)
            self.utils.print_info("Clicking yes on the confirm delete popup")
            self.auto_actions.click_reference(self.user_profile_web_elements.get_user_profile_confirm_delete_yes)

            kwargs['pass_msg'] = "Vlans deleted successfully"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Unable to gather VLANs"
            self.common_validation.failed(**kwargs)
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

    def delete_wips_policy_profile(self, wips_policy_name, **kwargs):
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
            kwargs['pass_msg'] = "WIPS Policy Name doesn't exist in the list"
            self.common_validation.passed(**kwargs)
            return 1

        self.utils.print_info("Select and delete Wips Policy row")
        self._select_delete_common_object(wips_policy_name)

        sleep(5)
        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)

        for value in tool_tp_text:
            if "cannot be deleted because this item is still used by another item" in value:
                kwargs['fail_msg'] = "Cannot be deleted because this item is still used by another item"
                self.common_validation.fault(**kwargs)
                return -1

        kwargs['pass_msg'] = "WIPS policy was deleted successfully"
        self.common_validation.passed(**kwargs)
        return 1

    def delete_ap_template_profile(self, ap_template_name, **kwargs):
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
            kwargs['pass_msg'] = "AP Template Name doesn't exist in the list"
            self.common_validation.passed(**kwargs)
            return 1

        self.utils.print_info("Select and delete AP Template row")
        self._select_delete_common_object_template(ap_template_name)

        sleep(5)
        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)

        if "Template was successfully removed from policy." in tool_tp_text[-1]:
            kwargs['pass_msg'] = "Template was successfully removed from policy."
            self.common_validation.passed(**kwargs)
            return 1
        elif "The Device Template cannot be removed because it is used by another object" in tool_tp_text[-1]:
            kwargs['fail_msg'] = "The Device Template cannot be removed because it is used by another object"
            self.common_validation.fault(**kwargs)
            return -1

        kwargs['fail_msg'] = "Failed to delete ap template profile."
        self.common_validation.failed(**kwargs)
        return -1

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

    def search_switch_template(self, search_string, **kwargs):
        """
        Search the passed search string object in Switch Template grid rows
        :param search_string:
        :return:
        """
        row = self._get_switch_template_row(search_string)
        if row:
            kwargs['pass_msg'] = f"{search_string} object present in grid row"
            self.common_validation.passed(**kwargs)
            return 1

    def delete_switch_template(self, template_name, **kwargs):
        """
        - Flow: Configure --> Common Objects --> Policy -->Switch Template
        - Delete specified switch template from the Switch Templates grid
        - Keyword Usage:
        - ``Delete Switch Template  ${TEMPLATE_NAME}``
        :param template_name: Name of the switch template
        :return: 1 if deleted else -1
        """

        self.navigator.navigate_to_switch_templates()
        self.utils.wait_till(self.cobj_web_elements.get_common_object_grid_rows)

        self.utils.print_info("Searching for 100 rows per page button...")
        view_all_pages = self.cobj_web_elements.get_common_object_policy_port_types_view_all_pages()
        if view_all_pages:
            self.utils.print_info("Found 100 rows per page button. Clicking...")
            self.auto_actions.click(view_all_pages)
        else:
            self.utils.print_info("100 rows per page button not present! Continue running...")

        self.utils.print_info(f"Searching Template: {template_name} on all pages...")
        current_page = 1
        found_template = 0

        while True:
            rows = self.cobj_web_elements.get_common_object_grid_rows()
            self.utils.print_info(f"Searching Template: {template_name} on page: {current_page}...")
            for row in rows:
                if template_name in row.text:
                    self.utils.print_info(f"Found template name: {template_name} on row: ", row.text)
                    found_template = 1

                    self.utils.print_info("Clicking the row's checkbox...")
                    check_box = self.cobj_web_elements.get_common_object_grid_row_cells(row, 'dgrid-selector')
                    if check_box:
                        self.auto_actions.click(check_box)
                    else:
                        kwargs['fail_msg'] = "Did not find row's check box!"
                        self.common_validation.fault(**kwargs)
                        return -1

                    self.utils.print_info("Clicking on delete button")
                    delete_button = self.cobj_web_elements.get_common_objects_delete_button()
                    if delete_button:
                        self.auto_actions.click(delete_button)
                        kwargs['pass_msg'] = f"Delete button has been clicked! Switch Template: {template_name} " \
                                             "has been deleted!"
                        self.common_validation.passed(**kwargs)
                        return 1
                    else:
                        kwargs['fail_msg'] = "Didn't find the delete button!"
                        self.common_validation.fault(**kwargs)
                        return -1

            if not found_template:
                self.utils.print_info(f"Template Name: {template_name} is not present on page: "
                                      f"{str(current_page)}")
                if not self.cobj_web_elements.get_next_page_element_disabled():
                    self.utils.print_info("Checking the next page: ", str(current_page + 1) + ' ...')
                    self.utils.print_info("Clicking next page...")
                    next_page_button = self.cobj_web_elements.get_next_page_element()
                    if self.cobj_web_elements.get_next_page_element():
                        if next_page_button:
                            self.auto_actions.click(next_page_button)
                            current_page += 1
                        else:
                            kwargs['fail_msg'] = "Did not manage to find the next page button"
                            self.common_validation.fault(**kwargs)
                            return -1
                    else:
                        kwargs['fail_msg'] = "delete_switch_template() failed. Did not find next page button!"
                        self.common_validation.fault(**kwargs)
                        return -1
                else:
                    self.utils.print_info("This is the last page: ", str(current_page))
                    kwargs['pass_msg'] = f"Checked all {current_page} pages for Template Name: {template_name}" \
                                         "It was already deleted or it hasn't been created yet!"
                    self.common_validation.passed(**kwargs)
                    return 1

    def delete_supplemental_cli_profile(self, supplemental_cli_name, **kwargs):
        """
        - Flow: Configure --> Common Objects --> Basic --> Supplemental CLI Objects
        - Delete specified supplemental cli profile from the Supplemental CLI Objects grid
        - Keyword Usage:
        - ``Delete Supplemental Cli Profile  ${SUPPLEMENTAL_CLI_NAME}``
        :param supplemental_cli_name: Name of the supplemental cli profile
        :return: 1 if deleted else -1
        """

        self.navigator.navigate_to_supplemental_cli_objects()
        self.utils.wait_till(self.cobj_web_elements.get_common_object_supp_cli_grid_rows)

        self.utils.print_info("Searching for 500 rows per page button...")
        view_all_pages = self.cobj_web_elements.get_common_object_basic_supp_cli_view_all_pages()
        if view_all_pages:
            self.utils.print_info("Found 500 rows per page button. Clicking...")
            self.auto_actions.click(view_all_pages)
        else:
            self.utils.print_info("500 rows per page button not present! Continue running...")

        self.utils.print_info(f"Searching Supplemental Cli Profile: {supplemental_cli_name} on all pages...")
        current_page = 1
        found_scli = 0

        while True:
            rows = self.cobj_web_elements.get_common_object_supp_cli_grid_rows()
            self.utils.print_info(f"Searching SCLI Profile: {supplemental_cli_name} on page: {current_page}...")
            for row in rows:
                if supplemental_cli_name in row.text:
                    self.utils.print_info(f"Found SCLI Profile: {supplemental_cli_name} on row: ", row.text)
                    found_scli = 1

                    self.utils.print_info("Clicking the row's checkbox...")
                    check_box = self.cobj_web_elements.get_common_object_supp_cli_grid_row_cells(row, '0')
                    if check_box:
                        self.auto_actions.click(check_box)
                    else:
                        kwargs['fail_msg'] = "Did not find row's check box!"
                        self.common_validation.fault(**kwargs)
                        return -1

                    self.utils.print_info("Clicking on delete button")
                    delete_button = self.cobj_web_elements.get_common_objects_delete_button()
                    if delete_button:
                        self.auto_actions.click(delete_button)

                        confirm_delete_btn = self.cobj_web_elements.get_common_object_confirm_delete_button()
                        if confirm_delete_btn:
                            self.utils.print_info("Clicking on confirm Yes button")
                            self.auto_actions.click(confirm_delete_btn)
                            kwargs['pass_msg'] = "YES button has been clicked! Supplemental Cli Profile: " \
                                                 f"{supplemental_cli_name} has been deleted!"
                            self.common_validation.passed(**kwargs)
                            return 1

                        kwargs['pass_msg'] = "Delete button has been clicked! Supplemental Cli Profile: " \
                                             f"{supplemental_cli_name} has been deleted!"
                        self.common_validation.passed(**kwargs)
                        return 1
                    else:
                        kwargs['fail_msg'] = "Didn't find the delete button!"
                        self.common_validation.fault(**kwargs)
                        return -1

            if not found_scli:
                self.utils.print_info(f"Supplemental Cli Profile: {supplemental_cli_name} is not present on page: "
                                      f"{str(current_page)}")
                if not self.cobj_web_elements.get_next_page_element_disabled() and self.cobj_web_elements.get_scli_grid_bottom().is_displayed():
                    self.utils.print_info("Checking the next page: ", str(current_page + 1) + ' ...')
                    self.utils.print_info("Clicking next page...")
                    next_page_button = self.cobj_web_elements.get_next_page_element()
                    if self.cobj_web_elements.get_next_page_element():
                        if next_page_button:
                            self.auto_actions.click(next_page_button)
                            current_page += 1
                        else:
                            kwargs['fail_msg'] = "Did not manage to find the next page button"
                            self.common_validation.fault(**kwargs)
                            return -1
                    else:
                        kwargs['fail_msg'] = "Did not find next page button!"
                        self.common_validation.fault(**kwargs)
                        return -1
                else:
                    self.utils.print_info("This is the last page: ", str(current_page))
                    kwargs['pass_msg'] = f"Checked all {current_page} pages for Supplemental Cli Profile: " \
                                         f"{supplemental_cli_name} ;" \
                                         "It was already deleted or it hasn't been created yet!"
                    self.common_validation.passed(**kwargs)
                    return 1

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
                if cell := self.cobj_web_elements.get_common_object_grid_row_cells(row, field='dgrid-column-2 field-tmpl'):
                    if cell.text == search_string:
                        return row
        else:
            self.utils.print_info("No rows found")

        self.utils.print_info(f"Common object row '{search_string}' not present")
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
        sleep(5)

    def create_open_ssid_in_common_objects(self, ssid_name, **kwargs):
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
            kwargs['pass_msg'] = f"SSID Name {ssid_name} already exists in the list"
            self.common_validation.passed(**kwargs)
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

        #Commented due to getting mismatch error in xpath once xpath gets updated it will used
        # sleep(5)
        # tool_tp_text = tool_tip.tool_tip_text
        # self.utils.print_info(tool_tp_text)

        # for value in tool_tp_text:
        #     if "SSID was saved successfully." in value:
        #         return 1
        #     elif "The SSID Profile cannot be saved" in value:
        #         return -2
        # return -1

        if self._search_common_object(ssid_name):
            kwargs['pass_msg'] = f"SSID Name {ssid_name} created"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "SSID Name is not created"
            self.common_validation.failed(**kwargs)
            return -1

    def clone_open_ssid_in_common_objects(self, ssid_name, clone_ssid_name, **kwargs):
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
            kwargs['fail_msg'] = f"SSID Name {ssid_name} doesn't exist in the list to clone"
            self.common_validation.fault(**kwargs)
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
                kwargs['pass_msg'] = "The item was copied successfully"
                self.common_validation.passed(**kwargs)
                return 1

        kwargs['fail_msg'] = "Failed to clone Open SSID"
        self.common_validation.failed(**kwargs)
        return -1

    def create_radio_profile(self, profile_name, radio_mode, dfs=False, **kwargs):
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
            kwargs['pass_msg'] = f"Radio profile {profile_name} already exists in the list"
            self.common_validation.passed(**kwargs)
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
                kwargs['pass_msg'] = "Radio profile was saved successfully."
                self.common_validation.passed(**kwargs)
                return 1
            elif "Radio profile cannot be saved" in value:
                kwargs['fail_msg'] = "Radio profile cannot be saved"
                self.common_validation.fault(**kwargs)
                return -1

        kwargs['fail_msg'] = "Failed to create radio profile"
        self.common_validation.failed(**kwargs)
        return -1

    def add_ap_template_from_common_object(self, ap_model, ap_template_name, wifi_interface_config, **kwargs):
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
            kwargs['pass_msg'] = "AP Template Name already exists in the list"
            self.common_validation.passed(**kwargs)
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
            self._config_ap_template_wired(wired_config)

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
            kwargs['pass_msg'] = "AP template was saved successfully"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Failed to add AP template"
            self.common_validation.failed(**kwargs)
            return -1

    def get_ap_template_wifi(self, ap_template_name, wifi_interface_config, **kwargs):
        """"
        - CONFIGURE-->COMMON OBJECTS-->Policy-->AP Templates
        - Get AP Template wiifi in Common Object
        - Keyword Usage
        - ``Get AP Template Wifi     ${AP_MODEL}    &{AP_TEMPLATE_CONFIG}``

        :param ap_template_name: AP default template name like AP_4000-default-template, AP_305-default-templateA etc
        :param wifi_interface_config: (Get Dict) Enable/Disable Client Access,Backhaul Mesh Link,Sensor etc
        :return: wifi_interface_config if Get AP Template Wifi Successfully else -1
        """
        wifi0_config = wifi_interface_config.get('wifi0_configuration', 'None')
        wifi1_config = wifi_interface_config.get('wifi1_configuration', 'None')
        wifi2_config = wifi_interface_config.get('wifi2_configuration', 'None')
        wired_config = wifi_interface_config.get('wired_configuration', 'None')

        try:
            self.utils.print_info("Navigate to Policy--> AP Templates")
            self.navigator.navigate_to_policy_ap_template()
            if self.cobj_web_elements.get_common_object_policy_ap_templates_view_all_pages():
                self.utils.print_info("Click Full pages button")
                self.auto_actions.click(self.cobj_web_elements.get_common_object_policy_ap_templates_view_all_pages())
                sleep(2)

            for row in self.cobj_web_elements.get_common_object_grid_rows():
                cell = self.cobj_web_elements.get_common_object_template_grid_row_cells(row)
                if cell.text == ap_template_name:
                    self.utils.print_info("Click on AP default template name: ", cell.text)
                    self.auto_actions.click(self.cobj_web_elements.get_common_object_template_grid_row_href(cell))
                    break

            if wifi0_config != 'None':
                self.utils.print_info("Get WiFI0 Interface details")
                wifi_interface_config['wifi0_configuration'] = self._get_ap_template_wifi0(**wifi0_config)
                self.screen.save_screen_shot()

            if wifi1_config != 'None':
                self.utils.print_info("Get WiFI1 Interface details")
                wifi_interface_config['wifi1_configuration'] = self._get_ap_template_wifi1(**wifi1_config)
                self.screen.save_screen_shot()

            if wifi2_config != 'None':
                self.utils.print_info("Get WiFI2 Interface details")
                wifi_interface_config['wifi2_configuration'] = self._get_ap_template_wifi2(**wifi2_config)
                self.screen.save_screen_shot()

            if wired_config != "None":
                self.utils.print_info("Get Wired Interfaces details")
                wifi_interface_config['wired_configuration'] = self._get_ap_template_wired(**wired_config)
                self.screen.save_screen_shot()

            self.utils.print_info("Click on the cancel template button")
            self.auto_actions.click(self.cobj_web_elements.get_common_object_ap_template_cancel_button())
            self.common_validation.passed(**wifi_interface_config)
            return wifi_interface_config

        except Exception as e:
            kwargs['fail_msg'] = f"Actual error is :- {e}"
            self.common_validation.fault(**kwargs)
            return -1

    def set_ap_template_wifi(self, ap_template_name, wifi_interface_config, **kwargs):
        """
        - CONFIGURE-->COMMON OBJECTS-->Policy-->AP Templates
        - Set AP Template wiifi in Common Object
        - Keyword Usage
        - ``Set AP Template WiFi     ${ap_template_name}   &{wifi_interface_config}``

        :param ap_template_name: AP template name like AP_4000-default-template, AP_305-default-templateA etc
        :param wifi_interface_config: (Set Dict) Enable/Disable Client Access,Backhaul Mesh Link,Sensor etc
        :return: 1 if Set AP Template wifi Successfully else -1
        """
        wifi0_config = wifi_interface_config.get('wifi0_configuration', 'None')
        wifi1_config = wifi_interface_config.get('wifi1_configuration', 'None')
        wifi2_config = wifi_interface_config.get('wifi2_configuration', 'None')

        self.utils.print_info("Navigate to Policy--> AP Templates")
        self.navigator.navigate_to_policy_ap_template()
        if self.cobj_web_elements.get_common_object_policy_ap_templates_view_all_pages():
            self.utils.print_info("Click Full pages button")
            self.auto_actions.click(self.cobj_web_elements.get_common_object_policy_ap_templates_view_all_pages())
            sleep(2)

        for row in self.cobj_web_elements.get_common_object_grid_rows():
            cell = self.cobj_web_elements.get_common_object_template_grid_row_cells(row)
            if cell.text == ap_template_name:
                self.utils.print_info("Click on AP default template name: ", cell.text)
                self.auto_actions.click(self.cobj_web_elements.get_common_object_template_grid_row_href(cell))
                break

        if wifi0_config != 'None':
            self.utils.print_info("Set WiFI0 Interface Setting")
            self._set_ap_template_wifi0(wifi0_config)
            self.screen.save_screen_shot()

        if wifi1_config != 'None':
            self.utils.print_info("Set WiFI1 Interface Setting")
            self._set_ap_template_wifi1(wifi1_config)
            self.screen.save_screen_shot()

        if wifi2_config != 'None':
            self.utils.print_info("Set WiFI2 Interface Setting")
            self._set_ap_template_wifi2(wifi2_config)
            self.screen.save_screen_shot()

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
            kwargs['pass_msg'] = "AP template was saved successfully"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Failed to set AP template"
            self.common_validation.failed(**kwargs)
            return -1

    def _set_ap_template_wifi0(self, wifi0_profile, **kwargs):
        """
        - Set the WIFI0 configuration on AP Template
        - Keyword Usage
        - ``Set AP Template WiFi0    &{WIFI0_CONFIG}``

        :param wifi0_profile: (Get Dict) Enable/Disable Client mode, Client Access,Backhaul Mesh Link, Sensor
        :return: 1 if Set WiFi0 Profile Successfully else -1
        """
        client_mode_status_wifi0   = wifi0_profile.get('client_mode'       , 'None')
        client_access_status_wifi0 = wifi0_profile.get('client_access'     , 'None')
        backhaul_mesh_status_wifi0 = wifi0_profile.get('backhaul_mesh_link', 'None')
        sensor_status_wifi0        = wifi0_profile.get('sensor'            , 'None')
        enable_SDR_wifi0           = wifi0_profile.get('enable_SDR'        , 'None')

        self.utils.print_info("Click on WiFi0 Tab on AP Template page")
        self.auto_actions.click(self.cobj_web_elements.get_common_object_ap_template_wifi0_tab())
        self.auto_actions.scroll_down()

        try:
            if client_mode_status_wifi0 != 'None':
                self.utils.print_info("Set Client Mode Checkbox on WiFi0 Interface: ", client_mode_status_wifi0)
                if client_mode_status_wifi0.lower() == 'enable':
                    if not self.cobj_web_elements.get_common_object_wifi0_client_mode().is_selected():
                        self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi0_client_mode())
                else:
                    if self.cobj_web_elements.get_common_object_wifi0_client_mode().is_selected():
                        self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi0_client_mode())

            if client_access_status_wifi0 != 'None':
                self.utils.print_info("Set Client Access Checkbox on WiFi0 Interface: ", client_access_status_wifi0)
                if client_access_status_wifi0.lower() == 'enable':
                    if not self.cobj_web_elements.get_common_object_wifi0_client_access().is_selected():
                        self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi0_client_access())
                else:
                    if self.cobj_web_elements.get_common_object_wifi0_client_access().is_selected():
                        self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi0_client_access())

            if backhaul_mesh_status_wifi0 != 'None':
                self.utils.print_info("Set Backhaul Mesh Link Checkbox on WiFi0 Interface: ", backhaul_mesh_status_wifi0)
                if backhaul_mesh_status_wifi0.lower() == 'enable':
                    if not self.cobj_web_elements.get_common_object_wifi0_mesh_link().is_selected():
                        self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi0_mesh_link())
                else:
                    if self.cobj_web_elements.get_common_object_wifi0_mesh_link().is_selected():
                        self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi0_mesh_link())

            if sensor_status_wifi0 != 'None':
                self.utils.print_info("Set Sensor Checkbox on WiFi0 Interface: ", sensor_status_wifi0)
                if sensor_status_wifi0.lower() == 'enable':
                    if not self.cobj_web_elements.get_common_object_wifi0_sensor().is_selected():
                        self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi0_sensor())
                else:
                    if self.cobj_web_elements.get_common_object_wifi0_sensor().is_selected():
                        self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi0_sensor())

            if enable_SDR_wifi0 != 'None':
                self.utils.print_info("Set Enable SDR Checkbox on WiFi0 Interface: ", enable_SDR_wifi0)
                if enable_SDR_wifi0.lower() == 'enable':
                    if not self.cobj_web_elements.get_common_object_ap_template_enable_sdr().is_selected():
                        self.auto_actions.click(self.cobj_web_elements.get_common_object_ap_template_enable_sdr())
                else:
                    if self.cobj_web_elements.get_common_object_ap_template_enable_sdr().is_selected():
                        self.auto_actions.click(self.cobj_web_elements.get_common_object_ap_template_enable_sdr())

        except Exception as e:
            kwargs['fail_msg'] = f"Actual error is :- {e}"
            self.common_validation.fault(**kwargs)
            return -1
        return 1

    def _set_ap_template_wifi1(self, wifi1_profile, **kwargs):
        """
        - Set the WIFI1 configuration on AP Template
        - Keyword Usage
        - ``Set AP Template WiFi1    &{WIFI0_CONFI1}``

        :param wifi1_profile: (Get Dict) Enable/Disable Client mode, Client Access,Backhaul Mesh Link, Sensor
        :return: 1 if Get WiFi1 Profile Successfully else -1
        """
        client_mode_status_wifi1   = wifi1_profile.get('client_mode'       , 'None')
        client_access_status_wifi1 = wifi1_profile.get('client_access'     , 'None')
        backhaul_mesh_status_wifi1 = wifi1_profile.get('backhaul_mesh_link', 'None')
        sensor_status_wifi1        = wifi1_profile.get('sensor'            , 'None')

        self.utils.print_info("Click on WiFi1 Tab on AP Template page")
        self.auto_actions.click(self.cobj_web_elements.get_common_object_ap_template_wifi1_tab())
        self.auto_actions.scroll_down()

        try:
            if client_mode_status_wifi1 != 'None':
                self.utils.print_info("Set Client Mode Checkbox on WiFi1 Interface: ", client_mode_status_wifi1)
                if client_mode_status_wifi1.lower() == 'enable':
                    if not self.cobj_web_elements.get_common_object_wifi1_client_mode().is_selected():
                        self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi1_client_mode())
                else:
                    if self.cobj_web_elements.get_common_object_wifi1_client_mode().is_selected():
                        self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi1_client_mode())

            if client_access_status_wifi1 != 'None':
                self.utils.print_info("Set Client Access Checkbox on WiFi1 Interface: ", client_access_status_wifi1)
                if client_access_status_wifi1.lower() == 'enable':
                    if not self.cobj_web_elements.get_common_object_wifi1_client_access().is_selected():
                        self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi1_client_access())
                else:
                    if self.cobj_web_elements.get_common_object_wifi1_client_access().is_selected():
                        self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi1_client_access())

            if backhaul_mesh_status_wifi1 != 'None':
                self.utils.print_info("Set Backhaul Mesh Link Checkbox on WiFi1 Interface: ",
                                      backhaul_mesh_status_wifi1)
                if backhaul_mesh_status_wifi1.lower() == 'enable':
                    if not self.cobj_web_elements.get_common_object_wifi1_mesh_link().is_selected():
                        self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi1_mesh_link())
                else:
                    if self.cobj_web_elements.get_common_object_wifi1_mesh_link().is_selected():
                        self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi1_mesh_link())

            if sensor_status_wifi1 != 'None':
                self.utils.print_info("Set Sensor Checkbox on WiFi1 Interface: ", sensor_status_wifi1)
                if sensor_status_wifi1.lower() == 'enable':
                    if not self.cobj_web_elements.get_common_object_wifi1_sensor().is_selected():
                        self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi1_sensor())
                else:
                    if self.cobj_web_elements.get_common_object_wifi1_sensor().is_selected():
                        self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi1_sensor())

        except Exception as e:
            kwargs['fail_msg'] = f"Actual error is :- {e}"
            self.common_validation.fault(**kwargs)
            return -1
        return 1

    def _set_ap_template_wifi2(self, wifi2_profile, **kwargs):
        """
        - Set the WIFI2 configuration on AP Template
        - Keyword Usage
        - ``Set AP Template WiFi2    &{WIFI0_CONFI2}``

        :param wifi2_profile: (Get Dict) Enable/Disable Client mode, Client Access,Backhaul Mesh Link, Sensor
        :return: 1 if Get WiFi2 Profile Successfully else -1
        """
        client_access_status_wifi2 = wifi2_profile.get('client_access'     , 'None')
        backhaul_mesh_status_wifi2 = wifi2_profile.get('backhaul_mesh_link', 'None')
        sensor_status_wifi2        = wifi2_profile.get('sensor'            , 'None')

        self.utils.print_info("Click on WiFi0 Tab on AP Template page")
        self.auto_actions.click(self.cobj_web_elements.get_common_object_ap_template_wifi2_tab())
        self.auto_actions.scroll_down()

        try:
            if client_access_status_wifi2 != 'None':
                self.utils.print_info("Set Client Access Checkbox on WiFi0 Interface: ", client_access_status_wifi2)
                if client_access_status_wifi2.lower() == 'enable':
                    if not self.cobj_web_elements.get_common_object_wifi2_client_access().is_selected():
                        self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi2_client_access())
                else:
                    if self.cobj_web_elements.get_common_object_wifi2_client_access().is_selected():
                        self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi2_client_access())

            if backhaul_mesh_status_wifi2 != 'None':
                self.utils.print_info("Set Backhaul Mesh Link Checkbox on WiFi0 Interface: ", backhaul_mesh_status_wifi2)
                if backhaul_mesh_status_wifi2.lower() == 'enable':
                    if not self.cobj_web_elements.get_common_object_wifi2_mesh_link().is_selected():
                        self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi2_mesh_link())
                else:
                    if self.cobj_web_elements.get_common_object_wifi2_mesh_link().is_selected():
                        self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi2_mesh_link())

            if sensor_status_wifi2 != 'None':
                self.utils.print_info("Set Sensor Checkbox on WiFi0 Interface: ", sensor_status_wifi2)
                if sensor_status_wifi2.lower() == 'enable':
                    if not self.cobj_web_elements.get_common_object_wifi2_sensor().is_selected():
                        self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi2_sensor())
                else:
                    if self.cobj_web_elements.get_common_object_wifi2_sensor().is_selected():
                        self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi2_sensor())

        except Exception as e:
            kwargs['fail_msg'] = f"Actual error is :- {e}"
            self.common_validation.fault(**kwargs)
            return -1
        return 1

    def _get_ap_template_wifi0(self, **wifi0_profile):
        """
        - Get the WIFI0 configuration on AP Template
        - Keyword Usage
        - ``Get AP Template WiFi0    &{WIFI0_CONFIG}``

        :param wifi0_profile: (Get Dict) Enable/Disable Client mode, Client Access,Backhaul Mesh Link, Sensor
        :return: wifi0_profile if Get WiFi0 Profile Successfully else None
        """
        radio_status_wifi0         = wifi0_profile.get('radio_status'      , 'None')   # radio_status=get or yes
        radio_operating_mode       = wifi0_profile.get('operating_mode'    , 'None')
        radio_profile_wifi0        = wifi0_profile.get('radio_profile'     , 'None')
        client_mode_status_wifi0   = wifi0_profile.get('client_mode'       , 'None')
        client_access_status_wifi0 = wifi0_profile.get('client_access'     , 'None')
        backhaul_mesh_status_wifi0 = wifi0_profile.get('backhaul_mesh_link', 'None')
        sensor_status_wifi0        = wifi0_profile.get('sensor'            , 'None')
        enable_SDR_wifi0           = wifi0_profile.get('enable_SDR'        , 'None')

        self.utils.print_info("Click on WiFi0 Tab on AP Template page")
        self.auto_actions.click(self.cobj_web_elements.get_common_object_ap_template_wifi0_tab())

        if radio_status_wifi0 != 'None':
            wifi0_profile['radio_status'] = self._convert_boolean_to_on_off(
                self.cobj_web_elements.get_common_object_wifi0_radio_status_button().is_selected())
            self.utils.print_info("Get Radio Status on WiFi0 Interface: ", wifi0_profile['radio_status'])
            if wifi0_profile['radio_status'] == 'Off':
                return wifi0_profile
        self.auto_actions.scroll_down()
        sleep(3)

        if radio_operating_mode != 'None':
            wifi0_profile['operating_mode'] = self.cobj_web_elements.get_common_object_wifi0_radio_operating_mode_combox().text
            self.utils.print_info("Get Radio Operating Mode status on WiFi0 Interface: ", wifi0_profile['operating_mode'])

        if radio_profile_wifi0 != 'None':
            wifi0_profile['radio_profile'] = self.cobj_web_elements.get_common_object_wifi0_radio_profile_textbox().text
            self.utils.print_info("Get Radio Profile status on WiFi0 Interface: ",  wifi0_profile['radio_profile'])

        if client_mode_status_wifi0 != 'None':
            wifi0_profile['client_mode'] = self._convert_boolean_to_enable_disable(
                self.cobj_web_elements.get_common_object_wifi0_client_mode().is_selected())
            self.utils.print_info("Get Client Mode Checkbox on WiFi0 Interface: ", wifi0_profile['client_mode'])

        if client_access_status_wifi0 != 'None':
            wifi0_profile['client_access'] = self._convert_boolean_to_enable_disable(
                self.cobj_web_elements.get_common_object_wifi0_client_access().is_selected())
            self.utils.print_info("Get Client Access Checkbox on WiFi0 Interface: ", wifi0_profile['client_access'])

        if backhaul_mesh_status_wifi0 != 'None':
            wifi0_profile['backhaul_mesh_link'] = self._convert_boolean_to_enable_disable(
                self.cobj_web_elements.get_common_object_wifi0_mesh_link().is_selected())
            self.utils.print_info("Get Backhaul Mesh Link Checkbox on WiFi0 Interface: ", wifi0_profile['backhaul_mesh_link'])

        try:
            if sensor_status_wifi0 != 'None':
                self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi0_sensor_UI_disable())
                wifi0_profile['sensor'] = 'UIDisable'
        except Exception:
            wifi0_profile['sensor'] = self._convert_boolean_to_enable_disable(
                self.cobj_web_elements.get_common_object_wifi0_sensor().is_selected())
        finally:
            self.utils.print_info("Get Sensor Checkbox on WiFi0 Interface: ", wifi0_profile['sensor'])

        if enable_SDR_wifi0 != 'None':
            wifi0_profile['enable_SDR'] = self._convert_boolean_to_enable_disable(
                self.cobj_web_elements.get_common_object_ap_template_enable_sdr().is_selected())
            self.utils.print_info("Get Enable SDR Checkbox on WiFi0 Interface: ", wifi0_profile['enable_SDR'])

        return wifi0_profile

    def _get_ap_template_wifi1(self, **wifi1_profile):
        """
        - Get the WIFI1 configuration on AP Template
        - Keyword Usage
        - ``Get AP Template WiFi1    &{WIFI1_CONFI1G}``

        :param wifi1_profile: (Get Dict) Enable/Disable Client mode, Client Access,Backhaul Mesh Link, Sensor
        :return: wifi1_profile if Get WiFi1 Profile Successfully else None
        """
        radio_status_wifi1         = wifi1_profile.get('radio_status'      , 'None')  # radio_status=get or yes
        radio_profile_wifi1        = wifi1_profile.get('radio_profile'     , 'None')
        client_mode_status_wifi1   = wifi1_profile.get('client_mode'       , 'None')
        client_access_status_wifi1 = wifi1_profile.get('client_access'     , 'None')
        backhaul_mesh_status_wifi1 = wifi1_profile.get('backhaul_mesh_link', 'None')
        sensor_status_wifi1        = wifi1_profile.get('sensor'            , 'None')

        self.utils.print_info("Click on WiFi1 Tab on AP Template page")
        self.auto_actions.click(self.cobj_web_elements.get_common_object_ap_template_wifi1_tab())

        if radio_status_wifi1 != 'None':
            wifi1_profile['radio_status'] = self._convert_boolean_to_on_off(
                self.cobj_web_elements.get_common_object_wifi1_radio_status_button().is_selected())
            self.utils.print_info("Get Radio Status on WiFi1 Interface: ", wifi1_profile['radio_status'])
            if wifi1_profile['radio_status'] == 'Off':
                return wifi1_profile
        self.auto_actions.scroll_down()

        if radio_profile_wifi1 != 'None':
            wifi1_profile['radio_profile'] = self.cobj_web_elements.get_common_object_wifi1_radio_profile_textbox().text
            self.utils.print_info("Get Radio Profile status on WiFi1 Interface: ", wifi1_profile['radio_profile'])

        if client_mode_status_wifi1 != 'None':
            wifi1_profile['client_mode'] = self._convert_boolean_to_enable_disable(
                self.cobj_web_elements.get_common_object_wifi1_client_mode().is_selected())
            self.utils.print_info("Get Client Mode Checkbox on WiFi1 Interface: ", wifi1_profile['client_mode'])

        if client_access_status_wifi1 != 'None':
            wifi1_profile[
                'client_access'] = self._convert_boolean_to_enable_disable(
                self.cobj_web_elements.get_common_object_wifi1_client_access().is_selected())
            self.utils.print_info("Get Client Access Checkbox on WiFi1 Interface: ", wifi1_profile['client_access'])

        if backhaul_mesh_status_wifi1 != 'None':
            wifi1_profile['backhaul_mesh_link'] = self._convert_boolean_to_enable_disable(
                self.cobj_web_elements.get_common_object_wifi1_mesh_link().is_selected())
            self.utils.print_info("Get Backhaul Mesh Link Checkbox on WiFi1 Interface: ", wifi1_profile['backhaul_mesh_link'])

        try:
            if sensor_status_wifi1 != 'None':
                self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi1_sensor_UI_disable())
                wifi1_profile['sensor'] = 'UIDisable'
        except Exception:
            wifi1_profile['sensor'] = self._convert_boolean_to_enable_disable(
                self.cobj_web_elements.get_common_object_wifi1_sensor().is_selected())
        finally:
            self.utils.print_info("Get Sensor Checkbox on WiFi1 Interface: ", wifi1_profile['sensor'])

        return wifi1_profile

    def _get_ap_template_wifi2(self, **wifi2_profile):
        """
        - Get the WIFI2 configuration on AP Template
        - Keyword Usage
        - ``Get AP Template WiFi2    &{WIFI2_CONFIG}``

        :param wifi2_profile: (Get Dict) Enable/Disable Client mode, Client Access,Backhaul Mesh Link, Sensor
        :return: wifi2_profile if Get WiFi2 Profile Successfully else None
        """
        radio_status_wifi2         = wifi2_profile.get('radio_status'      , 'None')  # radio_status=get or yes
        radio_profile_wifi2        = wifi2_profile.get('radio_profile'     , 'None')
        client_access_status_wifi2 = wifi2_profile.get('client_access'     , 'None')
        backhaul_mesh_status_wifi2 = wifi2_profile.get('backhaul_mesh_link', 'None')
        sensor_status_wifi2        = wifi2_profile.get('sensor'            , 'None')

        try:
            self.utils.print_info("Click on WiFi2 Tab on AP Template page")
            self.auto_actions.click(self.cobj_web_elements.get_common_object_ap_template_wifi2_tab())
        except Exception:
            return wifi2_profile

        if radio_status_wifi2 != 'None':
            wifi2_profile['radio_status'] = self._convert_boolean_to_on_off(
                self.cobj_web_elements.get_common_object_wifi2_radio_status_button().is_selected())
            self.utils.print_info("Get Radio Status on WiFi2 Interface: ", wifi2_profile['radio_status'])
            if  wifi2_profile['radio_status'] == 'Off':
                return wifi2_profile
        self.auto_actions.scroll_down()

        if radio_profile_wifi2 != 'None':
            wifi2_profile['radio_profile'] = self.cobj_web_elements.get_common_object_wifi2_radio_profile_textbox().text
            self.utils.print_info("Get Radio Profile status on WiFi2 Interface: ", wifi2_profile['radio_profile'])

        if client_access_status_wifi2 != 'None':
            wifi2_profile['client_access'] = self._convert_boolean_to_enable_disable(
                self.cobj_web_elements.get_common_object_wifi2_client_access().is_selected())
            self.utils.print_info("Get Client Access Checkbox on WiFi2 Interface: ", wifi2_profile['client_access'])

        if backhaul_mesh_status_wifi2 != 'None':
            wifi2_profile[
                'backhaul_mesh_link'] = self._convert_boolean_to_enable_disable(
                self.cobj_web_elements.get_common_object_wifi2_mesh_link().is_selected())
            self.utils.print_info("Get Backhaul Mesh Link Checkbox on WiFi2 Interface: ", wifi2_profile['backhaul_mesh_link'])

        try:
            if sensor_status_wifi2 != 'None':
                self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi2_sensor_UI_disable())
                wifi2_profile['sensor'] = 'UIDisable'
        except Exception:
            wifi2_profile['sensor'] = self._convert_boolean_to_enable_disable(
                self.cobj_web_elements.get_common_object_wifi2_sensor().is_selected())
        finally:
            self.utils.print_info("Get Sensor Checkbox on WiFi2 Interface: ", wifi2_profile['sensor'])

        return wifi2_profile

    def _get_ap_template_wired(self, **wired_profile):
        """
        - Get the Wired Interfaces on AP Template
        - Keyword Usage
        - ``Get AP Template Wired    &{WIRED_CONFIG}``

        :param wired_profile: (Get Dict) Enable/Disable Eth0, Eth1, and etc
        :return: wired_profile if Successfully else None
        """
        eth0 = wired_profile.get('eth0', 'None')   # eth0=get or yes
        eth1 = wired_profile.get('eth1', 'None')
        port_type_eth0 = wired_profile.get('port_type_eth0', 'None')
        port_type_eth1 = wired_profile.get('port_type_eth1', 'None')
        transmission_type_eth0 = wired_profile.get('transmission_type_eth0', 'None')
        transmission_type_eth1 = wired_profile.get('transmission_type_eth1', 'None')
        speed_eth0 = wired_profile.get('speed_eth0', 'None')
        speed_eth1 = wired_profile.get('speed_eth0', 'None')
        lldp_eth0 = wired_profile.get('lldp_eth0', 'None')
        lldp_eth1 = wired_profile.get('lldp_eth1', 'None')
        cdp_eth0 = wired_profile.get('cdp_eth0', 'None')
        cdp_eth1 = wired_profile.get('cdp_eth1', 'None')

        self.auto_actions.scroll_down()
        if eth0 != 'None':
            wired_profile['eth0'] = self._convert_boolean_to_on_off(
                self.cobj_web_elements.get_common_object_ap_template_eth0_status().is_selected())
            self.utils.print_info('Eth0 status: ', wired_profile['eth0'])

        if eth1 != 'None':
            wired_profile['eth1'] = self._convert_boolean_to_on_off(
                self.cobj_web_elements.get_common_object_ap_template_eth1_status().is_selected())
            self.utils.print_info('Eth1 status: ', wired_profile['eth1'])

        if port_type_eth0 != 'None':
            wired_profile['port_type_eth0'] = self.cobj_web_elements.get_common_object_ap_template_eth0_port_type().text
            self.utils.print_info('Port type eth0 status: ', wired_profile['port_type_eth0'])

        if port_type_eth1 != 'None':
            wired_profile['port_type_eth1'] = self.cobj_web_elements.get_common_object_ap_template_eth1_port_type().text
            self.utils.print_info('Port type eth1 status: ', wired_profile['port_type_eth1'])

        if transmission_type_eth0 != 'None':
            wired_profile['transmission_type_eth0'] = self.cobj_web_elements.get_common_object_ap_template_eth0_transmission_type().text
            self.utils.print_info('Transmission type eth0 status: ', wired_profile['transmission_type_eth0'])

        if transmission_type_eth1 != 'None':
            wired_profile['transmission_type_eth1'] = self.cobj_web_elements.get_common_object_ap_template_eth1_transmission_type().text
            self.utils.print_info('Transmission type eth1 status: ', wired_profile['transmission_type_eth1'])

        if speed_eth0 != 'None':
            wired_profile['speed_eth0'] = self.cobj_web_elements.get_common_object_ap_template_eth0_speed().text
            self.utils.print_info('Speed eth0 status: ', wired_profile['speed_eth0'])

        if speed_eth1 != 'None':
            wired_profile['speed_eth1'] = self.cobj_web_elements.get_common_object_ap_template_eth1_speed().text
            self.utils.print_info('Speed eth1 status: ', wired_profile['speed_eth1'])

        if lldp_eth0 != 'None':
            wired_profile['lldp_eth0'] = self._convert_boolean_to_enable_disable(
                self.cobj_web_elements.get_common_object_ap_template_lldp_eth0().is_selected())
            self.utils.print_info('LLDP eth0 status: ', wired_profile['lldp_eth0'])

        if lldp_eth1 != 'None':
            wired_profile['lldp_eth1'] = self._convert_boolean_to_enable_disable(
                self.cobj_web_elements.get_common_object_ap_template_lldp_eth1().is_selected())
            self.utils.print_info('LLDP eth1 status: ', wired_profile['lldp_eth1'])

        if cdp_eth0 != 'None':
            wired_profile['cdp_eth0'] = self._convert_boolean_to_enable_disable(
                self.cobj_web_elements.get_common_object_ap_template_cdp_eth0().is_selected())
            self.utils.print_info('CDP eth0 status: ', wired_profile['cdp_eth0'])

        if cdp_eth1 != 'None':
            wired_profile['cdp_eth1'] = self._convert_boolean_to_enable_disable(
                self.cobj_web_elements.get_common_object_ap_template_cdp_eth1().is_selected())
            self.utils.print_info('CDP eth1 status: ', wired_profile['cdp_eth1'])

        return wired_profile

    def _convert_boolean_to_enable_disable(self, boolean):
        """
        - Convert boolean to Enable or Disable
        :param boolean : True or False
        :return: Enable or Disable
        """
        return 'Enable' if boolean else 'Disable'

    def _convert_boolean_to_on_off(self, boolean):
        """
        - Convert boolean to On or Off
        :param boolean : True or False
        :return: Enable or Disable
        """
        return 'On' if boolean else 'Off'

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
            self.utils.print_info("Enable Radio Status on WiFi0 Interface")
            if self.cobj_web_elements.get_common_object_wifi0_radio_status_button().is_selected():
                self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi0_radio_status_button())
            return 1
        else:
            self.utils.print_info("Disable Radio Status on WiFi0 Interface")
            if not self.cobj_web_elements.get_common_object_wifi0_radio_status_button().is_selected():
                self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi0_radio_status_button())
        self.auto_actions.scroll_down()

        if '6g' in radio_profile_wifi0:
            self.utils.print_info('Click on Operating Mode: 6 GHz')
            self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi0_radio_operating_mode_combox())
            self.auto_actions.select_drop_down_options(self.cobj_web_elements.
                                                       get_common_object_wifi0_radio_operating_mode_combox_list(), '6 GHz')

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
                    self.utils.print_info("Click Add(+)")
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
                    self.utils.print_info("Click Add button")
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
        # Commented on 1/18/23 because it is unused
        # sensor_status_wifi1 = wifi1_profile.get('sensor', 'Enable')
        radio_profile_wifi1 = wifi1_profile.get('radio_profile', 'radio_ng_11ax-5g')
        radio_status_wifi1 = wifi1_profile.get('radio_status', 'On')

        self.utils.print_info("Click on WiFi1 Tab on AP Template page")
        self.auto_actions.click(self.cobj_web_elements.get_common_object_ap_template_wifi1_tab())

        if radio_status_wifi1.upper() == "OFF":
            self.utils.print_info("Disable Client Access Checkbox on wifi1 Interface")
            if self.cobj_web_elements.get_common_object_wifi1_radio_status_button().is_selected():
                self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi1_radio_status_button())
            return 1
        else:
            self.utils.print_info("Enable Client Access check box on wifi1 Interface")
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
                    self.utils.print_info("Click Add(+)")
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
                    self.utils.print_info("Click Add button")
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

        radio_status_wifi2         = wifi2_profile.get('radio_status'      , 'Off')
        client_access_status_wifi2 = wifi2_profile.get('client_access'     , 'Enable')
        backhaul_mesh_status_wifi2 = wifi2_profile.get('backhaul_mesh_link', 'Disable')

        self.utils.print_info("Click on WiFi2 Tab on AP Template page")
        self.auto_actions.click(self.cobj_web_elements.get_common_object_ap_template_wifi2_tab())

        self.auto_actions.scroll_down()

        if radio_status_wifi2.upper() == "Off":
            self.utils.print_info("Disable Radio Status on WiFi2 Interface")
            if not self.cobj_web_elements.get_common_object_wifi2_radio_status_button().is_selected():
                self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi2_radio_status_button())
            return 1
        else:
            self.utils.print_info("Enable Radio Status on WiFi2 Interface")
            if self.cobj_web_elements.get_common_object_wifi2_radio_status_button().is_selected():
                self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi2_radio_status_button())

        if client_access_status_wifi2.upper() == "ENABLE":
            self.utils.print_info("Enable Client Access Checkbox on WiFi2 Interface")
            if not self.cobj_web_elements.get_common_object_wifi2_client_access().is_selected():
                self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi2_client_access())
        else:
            self.utils.print_info("Disable Client Mode check box on WiFi2Interface")
            if self.cobj_web_elements.get_common_object_wifi2_client_access().is_selected():
                self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi2_client_access())

        if backhaul_mesh_status_wifi2.upper() == "ENABLE":
            self.utils.print_info("Enable Backhaul Mesh Link Checkbox on WiFi2 Interface")
            if not self.cobj_web_elements.get_common_object_wifi2_mesh_link().is_selected():
                self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi2_mesh_link())
        else:
            self.utils.print_info("Disable Backhaul Mesh Link Checkbox on WiFi2 Interface")
            if self.cobj_web_elements.get_common_object_wifi2_mesh_link().is_selected():
                self.auto_actions.click(self.cobj_web_elements.get_common_object_wifi2_mesh_link())

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

    def _config_ap_template_wired(self, wired_profile, **kwargs):
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
                get_common_object_ap_template_cdp_eth0().is_selected():
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
            kwargs['fail_msg'] = f"Actual error is :- {e}"
            self.common_validation.fault(**kwargs)
            return -1

        self.screen.save_screen_shot()
        self.auto_actions.scroll_up()
        return 1

    def check_ap_template_in_common_object(self, ap_template_name, **kwargs):
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
            kwargs['pass_msg'] = f"AP Template {ap_template_name} found in the CommonObject"
            self.common_validation.passed(**kwargs)
            return 1

        else:
            kwargs['fail_msg'] = f"AP Template {ap_template_name} not found in the CommonObject"
            self.common_validation.failed(**kwargs)
            return -1

    def delete_ap_templates(self, *templates, **kwargs):
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
                self.auto_actions.scroll_up()
                select_template_flag = True
            else:
                self.utils.print_info(f"Template {template} doesn't exist in the list")

        if not select_template_flag:
            kwargs['pass_msg'] = f"Template {template} doesn't exist in the list"
            self.common_validation.passed(**kwargs)
            return 1
        self._delete_common_objects()

        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)

        expected_tooltip1 = "Template was deleted successfully."
        expected_tooltip2 = "Template was successfully removed from policy."

        if expected_tooltip1 in tool_tp_text[-1] or expected_tooltip2 in tool_tp_text[-1]:
            kwargs['pass_msg'] = "Template was deleted successfully."
            self.common_validation.passed(**kwargs)
            return 1

        elif expected_tooltip1 in tool_tp_text or expected_tooltip2 in tool_tp_text:
            kwargs['pass_msg'] = "Template was deleted successfully.Tooltip Message is same like previous operation"
            self.common_validation.passed(**kwargs)
            return 1

        elif "The Device Template cannot be removed because it is used by another object" in tool_tp_text[-1]:
            kwargs['fail_msg'] = "The Device Template cannot be removed because it is used by another object"
            self.common_validation.fault(**kwargs)
            return -1

        kwargs['fail_msg'] = "Failed to delete AP templates"
        self.common_validation.failed(**kwargs)
        return -1

    def delete_all_ap_templates(self, **kwargs):
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
            kwargs['pass_msg'] = "Row(s) not present in the grid"
            self.common_validation.passed(**kwargs)
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
            kwargs['pass_msg'] = "Template was successfully removed from policy."
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Failed to delete all ap templates"
            self.common_validation.failed(**kwargs)
            return -1

    def delete_all_client_mode_profiles(self, **kwargs):
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
            kwargs['pass_msg'] = "Client Mode Profile(s) not present in the grid"
            self.common_validation.passed(**kwargs)
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

                kwargs['pass_msg'] = "Successfully deleted all client mode profiles"
                self.common_validation.passed(**kwargs)
                return 1
            except Exception:
                kwargs['fail_msg'] = "Unable to delete Client Mode Profiles"
                self.common_validation.fault(**kwargs)
                return -1

    def radio_phy_mode_fiveghz(self, model):
        """
        - Flow: Configure --> Common Objects --> Policy --> Radio Profile
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

    def add_imago_tag_profile(self, profile_name, server='', channel='', fcc_mode=True, server_port='default', **kwargs):
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
                    kwargs['pass_msg'] = f"Found Imago Tag Profile {profile_name} Row in the Grid"
                    self.common_validation.passed(**kwargs)
                    return 1

            kwargs['fail_msg'] = f"Did not find Imago Tag Profile {profile_name} Configured"
            self.common_validation.failed(**kwargs)
            return -1
        else:
            kwargs['fail_msg'] = "Did not find any Imago Tag Profile Rows"
            self.common_validation.fault(**kwargs)
            return -1

    def delete_imago_tag_profile(self, profile_name, **kwargs):
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
            kwargs['pass_msg'] = "Successfully Deleted the ImagoTag Policy"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Unable to Delete Image Tag Policy"
            self.common_validation.failed(**kwargs)
            return -1

    def edit_imago_tag_profile(self, profile_name, server='', channel='', fcc_mode=True, server_port='', **kwargs):
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

                    self.utils.print_info("Click Edit Button")
                    self.auto_actions.click(self.cobj_web_elements.get_imago_tag_profile_edit_button())
                    self.screen.save_screen_shot()
                    sleep(2)
        else:
            kwargs['fail_msg'] = "Imago Tag Profile Rows Not Found on Grid"
            self.common_validation.fault(**kwargs)
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

        if "Successfully Updated" in tool_tp_text[-1]:
            kwargs['pass_msg'] = "Successfully Updated"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Unable to Edit Image Tag Policy successfully"
            self.common_validation.failed(**kwargs)
            return -1

    def create_ip_firewall_policy_for_applications(self, policy_name, application='', source_ip='Any',
                                                   destination_ip='Any', action='Permit', **kwargs):
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
            kwargs['pass_msg'] = "Successfully Created IP firewall policy with Mentioned Application/Applications"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Unable Create IP firewall policy with Application"
            self.common_validation.failed(**kwargs)
            return -1

    def select_ip_firewall_policy_for_new_user_profile(self, user_profile_name='', firewall_policy_name='', **kwargs):
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
            self.auto_actions.click(self.cobj_web_elements.get_firewall_policy_select_dialog_cancel_button())
            sleep(2)
            kwargs['fail_msg'] = f"Firewall Policy: {firewall_policy_name} doesn't exist"
            self.common_validation.fault(**kwargs)
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
            kwargs['pass_msg'] = "Successfully Selected IP firewall policy Under New User Profile"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Unable to select IP firewall policy Under New User Profile"
            self.common_validation.failed(**kwargs)
            return -1

    def delete_management_options(self, management_options_name, **kwargs):
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
            kwargs['pass_msg'] = "Management options were deleted successfully"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Unable to Delete Management options"
            self.common_validation.failed(**kwargs)
            return -1

    def add_network_management_options(self,  option_name="management_option_1", enable_legacy_http_redirect="True", **kwargs):
        """
        - Adds new network management option(s)
        - Flow: Configure --> Common Objects --> Network -->Management Options
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
                        kwargs['fail_msg'] = "Unable to enable legacy http redirect"
                        self.common_validation.fault(**kwargs)
                        return -1
                self.utils.print_info("Saving configuration")
                save_button = self.network_management_options_elements.get_save_button()
                if save_button:
                    self.auto_actions.click(save_button)
                    kwargs['pass_msg'] = "Added new network management option(s)"
                    self.common_validation.passed(**kwargs)
                    return 1
                else:
                    kwargs['fail_msg'] = "Unable to save configuration"
                    self.common_validation.fault(**kwargs)
                    return -1
            else:
                kwargs['fail_msg'] = "Unable to set Name field for new Add Management Options Entry"
                self.common_validation.fault(**kwargs)
                return -1
        else:
            kwargs['fail_msg'] = "Unable to click on the Add Management Options Button"
            self.common_validation.fault(**kwargs)
            return -1

    def delete_user_profile(self, profile="user004", **kwargs):
        """
        - It deletes user profile
        - Flow: Configure --> Common Objects --> User Profile
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
                                kwargs['pass_msg'] = "Clicked yes to delete user profile"
                                self.common_validation.passed(**kwargs)
                                return 1
                            else:
                                kwargs['fail_msg'] = "Unable to click yes on the confirm delete popup"
                                self.common_validation.fault(**kwargs)
                                return -1
                        else:
                            kwargs['fail_msg'] = "Unable to click the delete button"
                            self.common_validation.fault(**kwargs)
                            return -1
                    else:
                        kwargs['fail_msg'] = "Unable to select the row"
                        self.common_validation.fault(**kwargs)
                        return -1

            if not profile_was_located:
                kwargs['fail_msg'] = f"Profile {profile} was NOT found"
                self.common_validation.fault(**kwargs)
                return -1
        else:
            kwargs['fail_msg'] = "Unable to gather user profiles"
            self.common_validation.fault(**kwargs)
            return -1

        kwargs['fail_msg'] = "Failed to delete user profile"
        self.common_validation.failed(**kwargs)
        return -1

    def delete_all_user_profiles(self, **kwargs):
        """
        - It deletes all user profiles
        - Flow: Configure --> Common Objects --> User Profile
        - Keyword Usage:
        - ``Delete All User Profiles``

        :return: 1 if successfully created else -1
        """
        exclude_list = ['default-profile', 'default-guest-profile']
        self.navigator.navigate_to_common_object_user_profile()
        sleep(5)

        if profile_rows := self.user_profile_web_elements.get_user_profile_grid_rows():
            self.utils.print_info("Gathering all the user profiles in the profile table")
            for row in profile_rows:
                if exclude_list[0] in row.text.lower() or exclude_list[1] in row.text.lower():
                    continue
                self.utils.print_info("Selecting the row ", row.text)
                self.auto_actions.click(self.user_profile_web_elements.get_all_profile_row_cells(row)[0])

            self.utils.print_info("Clicking on the delete button")
            self.auto_actions.click_reference(self.user_profile_web_elements.get_user_profile_delete)
            sleep(3)
            self.utils.print_info("Clicking yes on the confirm delete popup")
            self.auto_actions.click_reference(self.user_profile_web_elements.get_user_profile_confirm_delete_yes)

            kwargs['pass_msg'] = "Deleted all user profiles"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Unable to gather user profiles"
            self.common_validation.failed(**kwargs)
            return -1

    def delete_ip_firewall_policy(self, ip_firewall_policy_name, **kwargs):
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
            kwargs['pass_msg'] = "IP firewall policy was deleted successfully"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = f"Unable to Delete IP Firewall Policy {ip_firewall_policy_name}"
            self.common_validation.failed(**kwargs)
            return -1

    def add_ip_object_hostname_with_ip_or_hostname(self, name, type, global_item, *classify_items, **kwargs):
        """
        - Flow: Configure --> Common Objects --> Basic --> IP Objects / HostName --> Click + to add an ip object profile with IP Address
        - Create ip object profile with ip address
        - Keyword Usage:
        - ``Add IP Object Hostname With IP or Hostname     ${name}     ${type}     ${global_item}    @{classify_items}``

        :param name: The profile name
        :param type: "IP Address", or "Host Name", or "Wildcard Host Name"
        :param global_item:   Unclassified IP address, or unclassified Hostname, or unclassified wildcard hostname
        :param *classify_items:    Classified IP address list, or classified Hostname list, or classified wildcard hostname list
        :return: success return 1 else return -1
        """
        if not self.cobj_web_elements.get_ip_object_hostname_page():
            self.utils.print_info("Not in IP Object management page, need navigate to the page first.")
            self.navigate_to_basic_ip_object_hostname()
        else:
            self.utils.print_info("Already in IP Object management page, go ahead for next steps ...")
        self.utils.print_info("Check the IP object profile if it exists ...")
        find_ipobject_result = self._ip_object_hostname_find_object_profile(name)
        if find_ipobject_result == 1:
            self.utils.print_info(f"Network Object {name} is found, next to delete it...")
            self.ip_object_hostname_delete_object_profile(name)
            self.utils.print_info(f"Network Object {name} is deleted successfully...")
        else:
            self.utils.print_info(f"Network Object {name} is NOT found, go ahead for next step...")
        self.utils.print_info("click + to add an new object profile ...")
        add_button = self.cobj_web_elements.get_ip_object_hostname_add_button()
        if add_button:
            self.auto_actions.click(add_button)
            if type == "IP Address":
                self._ip_object_hostname_choose_type(type)
                self.utils.print_info(f"Add ip object name: {name} ...")
                self.auto_actions.send_keys(self.cobj_web_elements.get_ip_object_hostname_profile_name_textfield(), name)
                self.utils.print_info(f"Input IP address: {global_item} ...")
                self.auto_actions.send_keys(self.cobj_web_elements.get_ip_object_ip_address_textfield(), global_item)
                self.utils.print_info(f'The length of classify_items list the list is {classify_items}')
                classified_items = self._ip_object_hostname_add_objects(type, None, *classify_items)
                if classified_items == -1:
                    self.utils.print_info("Click SAVE button to save IP Object profile ...")
                    self.auto_actions.click(self.cobj_web_elements.get_ip_object_save_button())

                kwargs['pass_msg'] = "Added IP Object with IP Address"
                self.common_validation.passed(**kwargs)
                return 1

            elif type == "Host Name":
                self._ip_object_hostname_choose_type(type)
                self.utils.print_info(f"Add ip object name: {name} ...")
                self.auto_actions.send_keys(self.cobj_web_elements.get_ip_object_hostname_profile_name_textfield(), name)
                self.utils.print_info(f"Input Host Name: {global_item} ...")
                self.auto_actions.send_keys(self.cobj_web_elements.get_ip_object_hostname_textfield(), global_item)
                self.utils.print_info(
                    f'The length of the classified list is {classify_items}')
                classified_items = self._ip_object_hostname_add_objects(type, None, *classify_items)
                if classified_items == -1:
                    self.utils.print_info("Click SAVE button to save IP Object profile ...")
                    self.auto_actions.click(self.cobj_web_elements.get_ip_object_save_button())

                kwargs['pass_msg'] = "Added IP Object with Hostname"
                self.common_validation.passed(**kwargs)
                return 1

            elif type == "Wildcard Host Name":
                self._ip_object_hostname_choose_type(type)
                self.utils.print_info(f"Add ip object name: {name} ...")
                self.auto_actions.send_keys(self.cobj_web_elements.get_ip_object_hostname_profile_name_textfield(), name)
                self.utils.print_info(f"Input Wildcard Host Name: {global_item} ...")
                self.auto_actions.send_keys(self.cobj_web_elements.get_ip_object_wildcard_hostname_textfield(), global_item)
                self.utils.print_info(f'The length of the classified list is {classify_items}')
                classified_items = self._ip_object_hostname_add_objects(type, None, *classify_items)
                if classified_items == -1:
                    self.utils.print_info("Click SAVE button to save IP Object profile ...")
                    self.auto_actions.click(self.cobj_web_elements.get_ip_object_save_button())

                kwargs['pass_msg'] = "Added IP Object with Wildcard Host Name"
                self.common_validation.passed(**kwargs)
                return 1
            else:
                kwargs['fail_msg'] = "Failed to add IP Object with IP or Host Name"
                self.common_validation.failed(**kwargs)
                return -1
        else:
            kwargs['fail_msg'] = "Add button didn't found"
            self.common_validation.fault(**kwargs)
            return -1

    def add_ip_object_hostname_with_ip_network(self, name, type, global_network, netmask, *classify_network, **kwargs):
        """
        - Flow: Configure --> Common Objects --> Basic --> IP Objects / HostName --> Click + to add an ip object profile with Networks
        - Create ip object profile with ip networks
        - Keyword Usage:
        - ``Add IP Object Hostname With IP Network    ${name}     ${type}     ${global_network}     ${netmask}    @{classify_network}``

        :param name: The profile name
        :param type: "Network", or "Wildcard"
        :param global_network:   Unclassified Network, or unclassified Wildcard network
        :param netmask:  Netmask
        :param *classify_network:    Classified network list, or classified wildcard network list
        :return: success return 1
        """
        if not self.cobj_web_elements.get_ip_object_hostname_page():
            self.utils.print_info("Not in IP Object mangement page, need navigate to the page first.")
            self.navigate_to_basic_ip_object_hostname()
        else:
            self.utils.print_info("Already in IP Object management page, go ahead for next steps ...")
        self.utils.print_info("Check the IP object profile if it exists ...")
        find_ipobject_result = self._ip_object_hostname_find_object_profile(name)
        if find_ipobject_result == 1:
            self.utils.print_info(f"Network Object {name} is found, next to delete it...")
            self.ip_object_hostname_delete_object_profile(name)
            self.utils.print_info(f"Network Object {name} is deleted successfully...")
        else:
            self.utils.print_info(f"Network Object {name} is NOT found, go ahead for next step...")
        self.utils.print_info("click + to add an new object profile ...")
        add_button = self.cobj_web_elements.get_ip_object_hostname_add_button()
        if add_button:
            self.auto_actions.click(add_button)
            if type == "Network":
                self._ip_object_hostname_choose_type(type)
                self.utils.print_info(f"Add ip object name: {name} ...")
                self.auto_actions.send_keys(self.cobj_web_elements.get_ip_object_hostname_profile_name_textfield(), name)
                self.utils.print_info(f"Input IP Network: {global_network} ...")
                self.auto_actions.send_keys(self.cobj_web_elements.get_ip_object_ip_network_subnet_textfield(), global_network)
                self.auto_actions.send_keys(self.cobj_web_elements.get_ip_object_ip_network_netmask_textfield(), netmask)
                classified_items = self._ip_object_hostname_add_objects(type, netmask, *classify_network)
                if classified_items == -1:
                    self.utils.print_info("Click SAVE button to save IP Object profile ...")
                    self.auto_actions.click(self.cobj_web_elements.get_ip_object_save_button())

                kwargs['pass_msg'] = "Added IP Object with IP Network"
                self.common_validation.passed(**kwargs)
                return 1
            elif type == "Wildcard":
                self._ip_object_hostname_choose_type(type)
                self.utils.print_info(f"Add ip object name: {name} ...")
                self.auto_actions.send_keys(self.cobj_web_elements.get_ip_object_hostname_profile_name_textfield(), name)
                self.utils.print_info(f"Input Wildcard Network: {global_network} ...")
                self.auto_actions.send_keys(self.cobj_web_elements.get_ip_object_wildcard_ip_textfield(), global_network)
                self.auto_actions.send_keys(self.cobj_web_elements.get_ip_object_wildcard_mask_textfield(), netmask)
                classified_items = self._ip_object_hostname_add_objects(type, netmask, *classify_network)
                if classified_items == -1:
                    self.utils.print_info("Click SAVE button to save IP Object profile ...")
                    self.auto_actions.click(self.cobj_web_elements.get_ip_object_save_button())

                kwargs['pass_msg'] = "Added IP Object with IP Wildcard"
                self.common_validation.passed(**kwargs)
                return 1
            else:
                kwargs['fail_msg'] = "Failed to add IP Object with IP Network"
                self.common_validation.failed(**kwargs)
                return -1
        else:
            kwargs['fail_msg'] = "Add button didn't found"
            self.common_validation.fault(**kwargs)
            return -1

    def add_ip_object_hostname_with_ip_range(self, name, global_range_start, ip_range_gap, *classify_range_start, **kwargs):
        """
        - Flow: Configure --> Common Objects --> Basic --> IP Objects / HostName --> Click + to add an ip object profile with IP Range
        - Create ip object profile with IP Range
        - Keyword Usage:
        - ``Add IP Object Hostname With IP Range    ${name}     ${global_range_start}       ${ip_range_gap}     @{classify_range_start}``

        :param name: The profile name
        :param global_range_start: The unclassified start IP address
        :param ip_range_gap:
            The gap flag between start IP and end IP.
            For example:
            start IP is 192.168.1.1, the gap is 00, and the end IP is 192.168.1.100
            end IP = string "192.168.1.1" + string "00" = string "192.168.1.100"
        :param classify_range_start:    Classified start IP list
        :return: success return 1
        """
        if not self.cobj_web_elements.get_ip_object_hostname_page():
            self.navigate_to_basic_ip_object_hostname()
        else:
            self.utils.print_info("Already in IP Object management page...")
        self.utils.print_info("Check the IP object profile if it exists ...")
        find_ipobject_result = self._ip_object_hostname_find_object_profile(name)
        if find_ipobject_result == 1:
            self.utils.print_info(f"Network Object {name} is found, next to delete it...")
            self.ip_object_hostname_delete_object_profile(name)
            self.utils.print_info(f"Network Object {name} is deleted successfully...")
        else:
            self.utils.print_info(f"Network Object {name} is NOT found, go ahead for next step...")

        self.utils.print_info("click + to add an new object profile ...")
        add_button = self.cobj_web_elements.get_ip_object_hostname_add_button()
        if add_button:
            self.auto_actions.click(add_button)
            self._ip_object_hostname_choose_type("IP Range")
            self.utils.print_info(f"Add ip object name: {name} ...")
            self.auto_actions.send_keys(self.cobj_web_elements.get_ip_object_hostname_profile_name_textfield(), name)
            self.utils.print_info(f"Input Global IP Range Start: {global_range_start} ...")
            self.auto_actions.send_keys(self.cobj_web_elements.get_ip_object_ip_range_start_textfield(), global_range_start)
            self.utils.print_info(f"Input Global IP Range End: {global_range_start + ip_range_gap}")
            self.auto_actions.send_keys(self.cobj_web_elements.get_ip_object_ip_range_end_textfield(), global_range_start + ip_range_gap)
            classified_items = self._ip_object_hostname_add_objects_for_ip_range(ip_range_gap, *classify_range_start)
            if classified_items == -1:
                self.utils.print_info("Click SAVE button to save IP Object profile ...")
                self.auto_actions.click(self.cobj_web_elements.get_ip_object_save_button())

            kwargs['pass_msg'] = "Added IP Object Hostname With IP Range"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Add button didn't found"
            self.common_validation.fault(**kwargs)
            return -1

    def _ip_object_hostname_choose_type(self, object_type):
        """
        - It is internal function for choose object type
        - Flow: IP Object creating page --> Click drop down of object type --> Select the type
        :param object_type: The type of IP Object profile
        :return: success return 1 else return -1
        """
        self.utils.print_info("Click on ip object type drop down")
        self.auto_actions.click(self.cobj_web_elements.get_ip_object_type_drop_down())
        object_types = self.cobj_web_elements.get_ip_object_type_options()
        self.utils.print_info(f"The object type is: {object_type} ...")
        type_choose_result = self.auto_actions.select_drop_down_options(object_types, object_type)
        if type_choose_result:
            self.utils.print_info("Successfully choose ip object")
            return 1
        else:
            return -1

    def _ip_object_hostname_add_objects(self, object_type=None, netmask=None, *classified_items_list):
        """
        - It is internal function for add classified objects except for IP Range object
        - Add more objects in the same profile, based on how many values in the more_items_list list, and then select classification rules for them
        - Flow:
        -- If *classify_items_list is none, not execute this function
        -- Else: Add objects based on *classify_items_list --> Fillin values in blank area without value --> Select classification rule for each object --> Save object profile
        :param object_type: The tyoe of IP Object profile
        :param netmask: Netmask
        :param  *classified_items_list: The classified items(it is a common list for all types items) list
        """
        add_items_result = self._ip_object_hostname_add_objects_sub_add_blank_row(*classified_items_list)
        if add_items_result:
            # Input IP address and select classification rules
            row_loop_num = 0
            blank_row_loop_num = 0
            for row in self.cobj_web_elements.get_ip_object_object_rows():
                # self.utils.print_info(f"Here are the rows: {row}")
                # self.utils.print_info(f"Row TEXT: {self.cobj_web_elements.get_ip_object_object_item_type(row).text}")
                if self.cobj_web_elements.get_ip_object_object_item_type(row).text != "Global":
                    if object_type == "IP Address":
                        fillin_ip = self._ip_object_hostname_add_objects_sub_fillin_ip_address(row_loop_num, blank_row_loop_num, row, *classified_items_list)
                        if fillin_ip == 1:
                            blank_row_loop_num += 1
                        else:
                            self.utils.print_info("This row is not a blank row. Check the next row")

                    if object_type == "Host Name":
                        fillin_ip = self._ip_object_hostname_add_objects_sub_fillin_hostname(row_loop_num, blank_row_loop_num, row, *classified_items_list)
                        if fillin_ip == 1:
                            blank_row_loop_num += 1
                        else:
                            self.utils.print_info("This row is not a blank row. Check the next row")

                    if object_type == "Wildcard Host Name":
                        fillin_ip = self._ip_object_hostname_add_objects_sub_fillin_wildcard_hostname(row_loop_num, blank_row_loop_num, row, *classified_items_list)
                        if fillin_ip == 1:
                            blank_row_loop_num += 1
                        else:
                            self.utils.print_info("This row is not a blank row. Check the next row")

                    if object_type == "Network":
                        fillin_subnet = self._ip_object_hostname_add_objects_sub_fillin_ip_network(row_loop_num, blank_row_loop_num, row, netmask, *classified_items_list)
                        if fillin_subnet == 1:
                            blank_row_loop_num += 1
                        else:
                            self.utils.print_info("This row is not a blank row. Check the next row")

                    row_loop_num = row_loop_num + 1
            self.utils.print_info("Click SAVE button to save IP Object profile ...")
            self.auto_actions.click(self.cobj_web_elements.get_ip_object_save_button())
            return 1
        else:
            return -1

    def _ip_object_hostname_add_objects_for_ip_range(self, ip_range_gap, *classify_range_start):
        """
        - It is internal function for add classified IP Range objects
        - Add more objects in the same profile, based on how many values in the more_items_list list, and then select classification rules for them
        - Flow:
        -- If *classify_range_start is none, not execute this function
        -- Else: Add objects based on *classify_range_start --> Fillin values in blank area without value --> Select classification rule for each object --> Save object profile
        :param ip_range_gap: The string to flag the gap between IP range start and IP range end, use it to generate IP range end
        :param *classify_range_start: The classified IP Range start list
        :return: success return 1 else return False
        """
        add_items_result = self._ip_object_hostname_add_objects_sub_add_blank_row(*classify_range_start)
        if add_items_result:
            # Input IP address and select classification rules
            row_loop_num = 0
            blank_row_loop_num = 0
            for row in self.cobj_web_elements.get_ip_object_object_rows():
                # self.utils.print_info(f"Here are the rows: {row}")
                # self.utils.print_info(f"Row TEXT: {self.cobj_web_elements.get_ip_object_object_item_type(row).text}")
                if self.cobj_web_elements.get_ip_object_object_item_type(row).text != "Global":
                    fillin_ip = self._ip_object_hostname_add_objects_sub_fillin_ip_range(row_loop_num, blank_row_loop_num, row, ip_range_gap, *classify_range_start)
                    if fillin_ip == 1:
                        blank_row_loop_num += 1
                    else:
                        self.utils.print_info("This row is not a blank row. Check the next row")
            self.utils.print_info("Click SAVE button to save IP Object profile ...")
            self.auto_actions.click(self.cobj_web_elements.get_ip_object_save_button())
            return 1
        else:
            return False

    def _ip_object_hostname_add_objects_sub_add_blank_row(self, *classified_items_list):
        """
        - It is internal function for add classified blank rows based on how many values in the list more_items_list
        - Flow:
        -- If *classify_range_start is none, not execute this function
        -- Else: Add blank rows based on *classify_range_start list
        :param *classified_items_list:
        :return: success return 1 else return False
        """
        if classified_items_list is not None:
            more_items_list_len = len(classified_items_list)
            self.utils.print_info(f'The length of classified_items_list {more_items_list_len}, and the list is {classified_items_list}')

            for i in range(more_items_list_len):
                self.auto_actions.click(self.cobj_web_elements.get_ip_object_add_new_object())
                if self.cobj_web_elements.get_ip_object_confirm_message_window():
                    self.auto_actions.click(self.cobj_web_elements.get_ip_object_confirm_message_window_yes_button())
            return 1
        else:
            return False

    def _ip_object_hostname_add_objects_sub_fillin_ip_address(self, row_loop_num, blank_row_loop_num, row,
                                                              *classified_ipaddress_list):
        """
        - It is internal function fillin IP address values to blank row
        :param row_loop_num: For row loop to find all items in the profile
        :param blank_row_loop_num: For blank row loop to Wildcard Hostname
        :param row: Row in profile
        :param *classified_ipaddress_list: The classified IP Address list
        :return: success return 1 else return -1
        """
        self.utils.print_info(f"IP address value: {self.cobj_web_elements.get_ip_object_ip_address_textfield_row(row).get_dom_attribute('value')}")
        if not self.cobj_web_elements.get_ip_object_ip_address_textfield_row(row).get_dom_attribute('value'):
            self.utils.print_info(f"Input IP{blank_row_loop_num} address: {classified_ipaddress_list[blank_row_loop_num]}")
            self.auto_actions.send_keys(self.cobj_web_elements.get_ip_object_ip_address_textfield_row(row), classified_ipaddress_list[blank_row_loop_num])
            sleep(2)
            self._ip_object_hostname_add_objects_sub_select_cls_rule(row_loop_num, row)
            return 1
        else:
            return -1

    def _ip_object_hostname_add_objects_sub_fillin_hostname(self, row_loop_num, blank_row_loop_num, row,
                                                            *classified_hostname_list):
        """
        - It is internal function fillin hostname values to blank row
        :param row_loop_num: For row loop to find all items in the profile
        :param blank_row_loop_num: For blank row loop to Wildcard Hostname
        :param row: Row in profile
        :param *classified_hostname_list: The classified Hostname list
        :return: success return 1 else return -1
        """
        self.utils.print_info(
            f"IP address value: {self.cobj_web_elements.get_ip_object_hostname_textfield_row(row).get_dom_attribute('value')}")
        if not self.cobj_web_elements.get_ip_object_hostname_textfield_row(row).get_dom_attribute('value'):
            self.utils.print_info(f"Input IP{blank_row_loop_num} address: {classified_hostname_list[blank_row_loop_num]}")
            self.auto_actions.send_keys(self.cobj_web_elements.get_ip_object_hostname_textfield_row(row), classified_hostname_list[blank_row_loop_num])
            sleep(2)
            self._ip_object_hostname_add_objects_sub_select_cls_rule(row_loop_num, row)
            return 1
        else:
            return -1

    def _ip_object_hostname_add_objects_sub_fillin_wildcard_hostname(self, row_loop_num, blank_row_loop_num, row,
                                                                     *classified_wildcardhostname_list):
        """
        - It is internal function fillin wildcard hostname values to blank row
        :param row_loop_num: For row loop to find all items in the profile
        :param blank_row_loop_num: For blank row loop to Wildcard Hostname
        :param row: Row in profile
        :param *classified_wildcardhostname_list: The classified Wildcard Hostname list
        :return: success return 1 else return -1
        """
        self.utils.print_info(
            f"IP address value: {self.cobj_web_elements.get_ip_object_wildcard_hostname_textfield_row(row).get_dom_attribute('value')}")
        if not self.cobj_web_elements.get_ip_object_wildcard_hostname_textfield_row(row).get_dom_attribute('value'):
            self.utils.print_info(f"Input IP{blank_row_loop_num} address: {classified_wildcardhostname_list[blank_row_loop_num]}")
            self.auto_actions.send_keys(self.cobj_web_elements.get_ip_object_wildcard_hostname_textfield_row(row), classified_wildcardhostname_list[blank_row_loop_num])
            self._ip_object_hostname_add_objects_sub_select_cls_rule(row_loop_num, row)
            return 1
        else:
            return -1

    def _ip_object_hostname_add_objects_sub_fillin_ip_network(self, row_loop_num, blank_row_loop_num, row, netmask,
                                                              *classified_network_list):
        """
        - It is internal function fillin IP Network values to blank row
        :param row_loop_num: For row loop to loop all items in the profile
        :param blank_row_loop_num: For blank row loop to fillin IP Range
        :param row: Row in profile
        :param netmask: Netmask
        :param *classified_network_list: The classified Network list
        :return: success return 1 else return -1
        """
        self.utils.print_info(f"Subnet value: {self.cobj_web_elements.get_ip_object_ip_network_subnet_textfield_row(row).get_dom_attribute('value')}")
        if not self.cobj_web_elements.get_ip_object_ip_network_subnet_textfield_row(row).get_dom_attribute('value'):
            self.utils.print_info(f"Input Subnet{blank_row_loop_num} : {classified_network_list[blank_row_loop_num]}")
            self.auto_actions.send_keys(self.cobj_web_elements.get_ip_object_ip_network_subnet_textfield_row(row), classified_network_list[blank_row_loop_num])
            self.auto_actions.send_keys(self.cobj_web_elements.get_ip_object_ip_network_netmask_textfield_row(row), netmask)
            self._ip_object_hostname_add_objects_sub_select_cls_rule(row_loop_num, row)
            return 1
        else:
            return -1

    def _ip_object_hostname_add_objects_sub_fillin_ip_range(self, row_loop_num, blank_row_loop_num, row, ip_range_gap, *classify_range_start):
        """
        - It is internal function fillin IP Range values to blank row
        :param row_loop_num: For row loop to loop all items in the profile
        :param blank_row_loop_num: For blank row loop to fillin IP Range
        :param row: Row in profile
        :param ip_range_gap: The string to flag the gap between IP range start and IP range end, use it to generate IP range end
        :param *classify_range_start: The classified IP Range start list
        :return: success return 1 else return -1
        """

        self.utils.print_info(f"Subnet value: {self.cobj_web_elements.get_ip_object_ip_range_start_textfield_row(row).get_dom_attribute('value')}")
        if not self.cobj_web_elements.get_ip_object_ip_range_start_textfield_row(row).get_dom_attribute('value'):
            self.utils.print_info(f"Input Subnet{blank_row_loop_num} : {classify_range_start[blank_row_loop_num]}")
            self.auto_actions.send_keys(self.cobj_web_elements.get_ip_object_ip_range_start_textfield_row(row), classify_range_start[blank_row_loop_num])
            self.utils.print_info(f"Input Subnet{blank_row_loop_num} :", classify_range_start[blank_row_loop_num] + ip_range_gap)
            self.auto_actions.send_keys(self.cobj_web_elements.get_ip_object_ip_range_end_textfield_row(row), classify_range_start[blank_row_loop_num] + ip_range_gap)
            self._ip_object_hostname_add_objects_sub_select_cls_rule(row_loop_num, row)
            return 1
        else:
            return -1

    def _ip_object_hostname_add_objects_sub_select_cls_rule(self, row_loop_num, row, **kwargs):
        """
        - It is internal function select classification rule
        :param row_loop_num: For row loop to loop all items in the profile
        :param row: Row in profile
        """
        self.utils.print_info(f"Click select the button of classification rule for Row{row_loop_num + 2} ... ")
        self.auto_actions.click(self.cobj_web_elements.get_ip_object_hostname_select_cls_rule_button(row))
        max_cls_rules = self._ip_object_hostname_find_cls_rules(row_loop_num)
        if max_cls_rules != -1:
            self.utils.print_info(f"Click LINK button {row_loop_num + 1} times ...")
            self.auto_actions.click(self.cobj_web_elements.get_ip_object_hostname_classification_rule_page_link_button())
            while self.cobj_web_elements.get_ip_object_hostname_classification_rule_used_error():
                self.auto_actions.click(self.cobj_web_elements.get_ip_object_hostname_classification_rule_used_error_close())
                row_loop_num += 1
                self.utils.print_info("Choose another classification rule ...")
                self._ip_object_hostname_find_cls_rules(row_loop_num)
                self.utils.print_info(f"Click LINK button {row_loop_num + 1} times ...")
                self.auto_actions.click(self.cobj_web_elements.get_ip_object_hostname_classification_rule_page_link_button())
                if row_loop_num > max_cls_rules:
                    kwargs['fail_msg'] = "There is no any more classified rule can be selected"
                    self.common_validation.fault(**kwargs)
                    return -1
            return 1
        else:
            return -1

    def _ip_object_hostname_find_cls_rules(self, row_loop_num):
        """
        - It is a internal function to find classification rule
        :param row_loop_num: For row loop to find classification rules
        :return: success return classification rule amount else return -1
        """
        if self.cobj_web_elements.get_ip_object_hostname_classification_rule_page_size_100():
            self.auto_actions.click(self.cobj_web_elements.get_ip_object_hostname_classification_rule_page_size_100())
        sleep(2)    # This line must have, or any classification rule can NOT be picked up after above operation
        cls_rules = []
        for rule in self.cobj_web_elements.get_ip_object_hostname_classification_rules():
            cls_rules.append(rule)
        click = self.auto_actions.click(cls_rules[row_loop_num])
        if click:
            return len(cls_rules)
        else:
            return -1

    def _ip_object_hostname_find_object_profile(self, ip_object_profile_name):
        """
        - It is a internal function to find object profile and check it
        - Flow: IP object Management page --> Click 100 objects per page --> Find object with name --> Check the object
        :param ip_object_profile_name:
        :return: success return 1 else return -1
        """
        find_result = False
        if self.cobj_web_elements.get_ip_object_hostname_object_page_size_100():
            self.auto_actions.click(self.cobj_web_elements.get_ip_object_hostname_object_page_size_100())
        sleep(2)    # This line must have, or IP Object profile can NOT be picked up after above operation
        self.utils.print_info(f"Try to find the IP Object profile {ip_object_profile_name} ...")
        ip_object_rows = self.cobj_web_elements.get_ip_object_hostname_existed_object_list_per_page()
        for ip_object_row in ip_object_rows:
            row_name = self.cobj_web_elements.get_ip_object_hostname_existed_object_name(ip_object_row).text
            self.utils.print_info(f"The IP Object Profile name is {row_name}")
            if row_name == ip_object_profile_name:
                self.utils.print_info(f"The IP object profile {ip_object_profile_name} is  found")
                self.auto_actions.click(ip_object_row)
                if self.cobj_web_elements.get_ip_object_hostname_object_checkbox_checked(ip_object_row) is None:
                    self.utils.print_info(f"The IP object profile {ip_object_profile_name} is NOT Selected...")
                    return -1
                else:
                    find_result = True
        if find_result:
            return 1
        else:
            self.utils.print_info(f"The IP object profile {ip_object_profile_name} is NOT found or NOT Selected...")
            return -1

    def ip_object_hostname_delete_object_profile(self, ip_object_profile_name, **kwargs):
        """
        - Delete IP Object profile
        - Flow: Configure --> Common Objects --> Basic --> IP Objects / HostName --> Find the object profile --> Delete it
        - Keyword Usage:
        - ``IP Object Hostname Delete Object Profile    ${ip_object_profile_name}``

        :param ip_object_profile_name: IP Object profile name
        :return: Find and delete successfully return 1 else return -1
        """
        if not self.cobj_web_elements.get_ip_object_hostname_page():
            self.utils.print_info("Not in IP Object mangement page, need navigate to the page first.")
            self.navigate_to_basic_ip_object_hostname()
        else:
            self.utils.print_info("Already in IP Object management page, go ahead for next steps ...")
        find_ipobject_result = self._ip_object_hostname_find_object_profile(ip_object_profile_name)
        if find_ipobject_result == 1:
            self.auto_actions.click(self.cobj_web_elements.get_common_objects_delete_button())
            if self.cobj_web_elements.get_ip_object_hostname_delete_confirm_win():
                self.auto_actions.click(self.cobj_web_elements.get_ip_object_hostname_delete_confirm_win_yes())
                kwargs['pass_msg'] = f"{ip_object_profile_name} is already deleted"
                self.common_validation.passed(**kwargs)
                return 1
            else:
                kwargs['fail_msg'] = "Select NO button to cancel the deleting operation"
                self.common_validation.fault(**kwargs)
                return -1
        else:
            kwargs['fail_msg'] = "There is no IP object profile finding"
            self.common_validation.failed(**kwargs)
            return -1

    def ip_object_hostname_update_object_profile(self, ip_object_profile_name, netmask=None, ip_range_gap=None,
                                                 *classified_items_list_1, **kwargs):
        f"""
        - Edit and Add new items for existed IP Object profile
        - Flow: Configure --> Common Objects --> Basic --> IP Objects / HostName --> Find the object profile --> Edit it and Add new items
        - Keyword Usage:
        - ``IP Object Hostname Update Object Profile    ${ip_object_profile_name}    ${netmask}    ${ip_range_gap}      ${classified_items_list_1}``

        :param ip_object_profile_name: IP Object profile name
        :param netmask: Netmask, for the profile with type IP address and Hostname related, the netmask is None, for Network and Wildcard Network, the netmask is needed
        :param ip_range_gap: Only for IP Range, keep it as None value if NOT IP Range
        :param *classified_items_list_1: The new items list for update profile, named it as *classified_items_list_1 to be different with *classified_items_list
        :return: Find and delete successfully return 1 else return -1
        """

        if not self.cobj_web_elements.get_ip_object_hostname_page():
            self.utils.print_info("Not in IP Object mangement page, need navigate to the page first.")
            self.navigate_to_basic_ip_object_hostname()
        else:
            self.utils.print_info("Already in IP Object management page, go ahead for next steps ...")
        find_ipobject_result = self._ip_object_hostname_find_object_profile(ip_object_profile_name)
        if find_ipobject_result == 1:
            self.utils.print_info(f"Network Object {ip_object_profile_name} is found, next to Edit it...")
            self.auto_actions.click(self.cobj_web_elements.get_ip_object_hostname_edit_button())
            if self.cobj_web_elements.get_ip_object_hostname_profile_objects_list_page_num_bottom():
                self.auto_actions.click(self.cobj_web_elements.get_ip_object_hostname_profile_objects_list_last_page())
                # self.auto_actions.click(self.cobj_web_elements.get_ip_object_add_new_object())
            object_type = self.cobj_web_elements.get_ip_object_type().text
            if object_type == "IP Range":
                self.utils.print_info(f"The updated object list: {classified_items_list_1}")
                self._ip_object_hostname_add_objects_for_ip_range(ip_range_gap, *classified_items_list_1)
            else:
                self.utils.print_info(f"The updated object list: {classified_items_list_1}")
                self._ip_object_hostname_add_objects(object_type, netmask, *classified_items_list_1)
                kwargs['pass_msg'] = "Edited and Added new items for existed IP Object profile"
                self.common_validation.passed(**kwargs)
                return 1
        else:
            kwargs['fail_msg'] = "Didn't find IP Object"
            self.common_validation.failed(**kwargs)
            return -1

    def ip_object_hostname_list_all_objects_in_profile(self, ip_object_profile_name, **kwargs):
        """
        - Find all the items for existed IP Object profile, and return a list
        - Flow: Configure --> Common Objects --> Basic --> IP Objects / HostName --> Find the object profile --> Edit it --> Click 100 items per page --> Get item row by row
        - Keyword Usage:
        - ``IP Object Hostname List All Objects In Profile    ${ip_object_profile_name}``

        :param ip_object_profile_name: IP Object profile name
        :return: success return a list else return -1
        """
        if not self.cobj_web_elements.get_ip_object_hostname_page():
            self.utils.print_info("Not in IP Object mangement page, need navigate to the page first.")
            self.navigate_to_basic_ip_object_hostname()
        else:
            self.utils.print_info("Already in IP Object management page, go ahead for next steps ...")
        if self._ip_object_hostname_find_object_profile(ip_object_profile_name) == 1:
            self.auto_actions.click(self.cobj_web_elements.get_ip_object_hostname_edit_button())
            if self.cobj_web_elements.get_ip_object_hostname_object_items_page_size_100():
                self.auto_actions.click(self.cobj_web_elements.get_ip_object_hostname_object_items_page_size_100())
            object_type = self.cobj_web_elements.get_ip_object_type().text
            object_items_list = []
            for row in self.cobj_web_elements.get_ip_object_object_rows():
                if object_type == "IP Address":
                    object_items_list.append(self.cobj_web_elements.get_ip_object_ip_address_textfield_row(row).get_dom_attribute('value'))
                if object_type == "Network":
                    object_items_list.append(self.cobj_web_elements.get_ip_object_ip_network_subnet_textfield_row(row).get_dom_attribute('value'))
                if object_type == "Host Name":
                    object_items_list.append(self.cobj_web_elements.get_ip_object_hostname_textfield_row(row).get_dom_attribute('value'))
                if object_type == "Wildcard Host Name":
                    object_items_list.append(self.cobj_web_elements.get_ip_object_wildcard_hostname_textfield_row(row).get_dom_attribute('value'))
                if object_type == "Wildcard":
                    object_items_list.append(self.cobj_web_elements.get_ip_object_wildcard_ip_textfield_row(row).get_dom_attribute('value'))
                if object_type == "IP Range":
                    object_items_list.append(self.cobj_web_elements.get_ip_object_ip_range_start_textfield_row(row).get_dom_attribute('value'))
            self.auto_actions.click(self.cobj_web_elements.get_ip_object_cancel_button())
            self.utils.print_info(f"The items list of object profile: {object_items_list}")
            return object_items_list
        else:
            kwargs['fail_msg'] = f"The IP Object profile {ip_object_profile_name} is NOT found, can NOT list the items"
            self.common_validation.failed(**kwargs)
            return -1

    def delete_switch_templates(self, template_name, **kwargs):
        """
        This keyword will delete the multiple switch templates from common objects.
        - Flow: Configure --> Common Objects --> Policy -->Switch Template
        - Delete specified switch template from the Switch Templates grid
        - Keyword Usage:
        - ``Delete Switch Template  ${TEMPLATE_NAME}``
        - ``Delete Switch Template  template_1,template_2`
        :param template_name: A list of templates which will be deleted. Or a string with templates names separated by comma
        :return: 1 if deleted else -1
        """
        if isinstance(template_name, list):
            sw_template_name_list = template_name.copy()
        else:
            sw_template_name_list = template_name.split(',')

        self.navigator.navigate_to_switch_templates()
        self.utils.wait_till(self.cobj_web_elements.get_common_object_grid_rows)

        self.utils.print_info("Searching for 100 rows per page button...")
        view_all_pages = self.cobj_web_elements.get_common_object_policy_port_types_view_all_pages()
        if view_all_pages:
            self.utils.print_info("Found 100 rows per page button. Clicking...")
            self.auto_actions.click(view_all_pages)
        else:
            self.utils.print_info("100 rows per page button not present! Continue running...")

        self.utils.print_info("Template name list:",sw_template_name_list)
        for template_name in sw_template_name_list:
            page_number = self.cobj_web_elements.get_common_object_policy_max_page_number()
            if page_number:
                self.utils.print_info("There are pages:")
                for el in page_number:
                    self.utils.print_info("Page:", el.text)
            else:
                self.utils.print_info("Can not get the page number")
            first_page = self.cobj_web_elements.get_common_object_policy_go_to_first_page()
            if first_page:
                self.utils.print_info("Go to first page :  ")
                self.auto_actions.click(first_page)
                cnt_page = 1
                sleep(5)
            else:
                self.utils.print_info("Can not navigate to first page")
            for page in page_number:
                self.utils.print_info(f"Searching Template: {template_name} on page: ", cnt_page)
                found_template = False
                rows = self.cobj_web_elements.get_common_object_grid_rows()
                if rows:
                    for row in rows:
                        if template_name in row.text:
                            self.utils.print_info(f"Found template name: {template_name} on row: ", row.text)
                            self.utils.print_info("Clicking the row's checkbox...")
                            check_box = self.cobj_web_elements.get_common_object_grid_row_cells(row, 'dgrid-selector')
                            if check_box:
                                self.auto_actions.click(check_box)
                            else:
                                self.utils.print_info("Did not find row's check box!")
                                kwargs[
                                    'fail_msg'] = "delete_switch_templates() failed. Did not find row's check box!"
                                self.common_validation.fault(**kwargs)
                                return -1
                            self.utils.print_info("Clicking on delete button")
                            delete_button = self.cobj_web_elements.get_common_objects_delete_button()
                            if delete_button:
                                self.auto_actions.click(delete_button)
                                kwargs['pass_msg'] = f"Delete button has been clicked! Switch Template: {template_name} " \
                                                     "has been deleted!"
                                self.common_validation.passed(**kwargs)
                                found_template = True
                                break
                            else:
                                kwargs['fail_msg'] = "Didn't find the delete button!"
                                self.common_validation.fault(**kwargs)
                                return -1
                        else:
                            pass
                else:
                    self.utils.print_info("Didn't find rows")
                if not found_template:
                    self.utils.print_info('len', len(page_number), cnt_page )
                    if len(page_number) == cnt_page:
                        self.utils.print_info(f"Last page is {cnt_page}")
                        kwargs['fail_msg'] = f"Template Name: {template_name} is not present on all pages."
                        self.common_validation.failed(**kwargs)
                        return -1
                    self.utils.print_info(f"Template Name: {template_name} is not present on page: ")
                    next_button = self.cobj_web_elements.get_next_page_element()
                    if next_button:
                        self.utils.print_info("Select next page")
                        self.auto_actions.click(next_button)
                    else:
                        kwargs['fail_msg'] = "Next button not found "
                        self.common_validation.fault(**kwargs)
                        return -1
                else:
                    self.utils.print_info("")
                    break
                cnt_page = cnt_page + 1

        kwargs['pass_msg'] = "Successfully deleted switch templates"
        self.common_validation.passed(**kwargs)
        return 1

    def delete_port_type_profiles(self, port_type_name, **kwargs):
        """
        This keyword will delete the multiple port type profiles from common objects.
        - Flow: CONFIGURE-->COMMON OBJECTS-->PORT TYPES
        - Delete Port Type from the grid
        - Keyword Usage:
        - ``Delete Port Type Profile  ${PORT_TYPE_NAME}``
         ``Delete Port Type Profile  ${PORT_TYPE_NAME1},${PORT_TYPE_NAME2}``
        :param port_type_name: A list of port type profiles which will be deleted. Or a string with profiles names separated by comma
        :return: 1 if Port Type deleted successfully, else returns -1
        """
        if isinstance(port_type_name, list):
            port_type_name_list = port_type_name.copy()
        else:
            port_type_name_list = port_type_name.split(',')
        self.utils.print_info("Navigate to Port Types Settings")
        self.navigator.navigate_to_policy_port_types()

        self.utils.print_info("Searching for 100 rows per page button...")
        view_all_pages = self.cobj_web_elements.get_common_object_policy_port_types_view_all_pages()
        if view_all_pages:
            self.utils.print_info("Found the 100 rows per page button! Clicking...")
            self.auto_actions.click(view_all_pages)
        else:
            self.utils.print_info("100 rows per page button was not found. Continue running...")

        self.utils.print_info("Waiting for the rows to load...")
        self.utils.wait_till(self.cobj_web_elements.get_common_object_grid_rows, delay=3)
        for port_type_name in port_type_name_list:
            self.utils.print_info(f"Searching {port_type_name} profile on all pages...")
            current_page = 1
            while True:
                self.utils.print_info(f"Searching: {port_type_name} profile, on page: {current_page}...")
                try:
                    if not self._search_common_object(port_type_name):
                        self.utils.print_info(f"Port Type Profile Name: {port_type_name} is not present on page: "
                                              f"{str(current_page)}")
                        self.utils.print_info("Checking the next page: ", str(current_page+1) + ' ...')
                        self.utils.print_info("Clicking next page...")
                        if not self.cobj_web_elements.get_next_page_element_disabled():
                            if self.cobj_web_elements.get_next_page_element():
                                self.auto_actions.click(self.cobj_web_elements.get_next_page_element())
                                self.utils.print_info("Waiting for the rows to load...")
                                self.utils.wait_till(self.cobj_web_elements.get_common_object_grid_rows, delay=3)
                                current_page += 1
                            else:
                                kwargs['fail_msg'] = "Did not find next page button!"
                                self.common_validation.fault(**kwargs)
                                return -1
                        else:
                            self.utils.print_info("This is the last page: ", str(current_page))
                            kwargs['pass_msg'] = f"Checked all {current_page} pages for Port Type profile: " \
                                                 f"{port_type_name} ; " \
                                                 "It was already deleted or it hasn't been created yet!"
                            self.common_validation.passed(**kwargs)
                            break
                    else:
                        self.utils.print_info(f"Found the port type profile {port_type_name}. Deleting...")
                        self._select_delete_common_object(port_type_name)
                        kwargs['pass_msg'] = "Port type profile deleted!"
                        self.common_validation.passed(**kwargs)
                        break

                except (selenium.common.exceptions.StaleElementReferenceException, TypeError) as e:
                    self.utils.print_info("Got the following error: ", e)
                    self.utils.print_info("Trying to get the rows again on page: ", str(current_page))
                    continue
        kwargs['pass_msg'] = "Successfully deleted port type profiles"
        self.common_validation.passed(**kwargs)
        return 1
