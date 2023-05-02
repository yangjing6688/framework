import random
import string
from time import sleep
import time
import re

import selenium.common.exceptions
from robot.libraries.BuiltIn import BuiltIn

# from extauto.common.CloudDriver import CloudDriver
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from extauto.common.CommonValidation import CommonValidation

import extauto.xiq.flows.common.ToolTipCapture as tool_tip
from extauto.xiq.flows.manage.Tools import Tools
from extauto.xiq.flows.common.Navigator import Navigator
from extauto.xiq.flows.manage.Devices import Devices
from extauto.xiq.flows.configure.WirelessNetworks import WirelessNetworks

from extauto.xiq.elements.DeviceUpdate import DeviceUpdate
from extauto.xiq.elements.DialogWebElements import DialogWebElements
from extauto.xiq.elements.WirelessWebElements import WirelessWebElements
from extauto.xiq.elements.NetworkPolicyWebElements import NetworkPolicyWebElements
from extauto.xiq.elements.FilterManageDeviceWebElements import FilterManageDeviceWebElements
from extauto.xiq.elements.DevicesWebElements import DevicesWebElements
from extauto.xiq.flows.configure.UserGroups import UserGroups
from extauto.xiq.flows.configure.CommonObjects import CommonObjects
from extauto.xiq.elements.UserGroupsWebElements import UserGroupsWebElements
from extauto.xiq.elements.Device360WebElements import Device360WebElements

import extauto.xiq.flows.configure.SwitchTemplate
from extauto.xiq.xapi.configure.XapiNetworkPolicy import XapiNetworkPolicy

from extauto.common.KeywordUtils import KeywordUtils


class NetworkPolicy(object):

    def __init__(self):
        self.utils = Utils()
        self.wireless_nw = WirelessNetworks()
        self.auto_actions = AutoActions()
        self.navigator = Navigator()
        self.common_objects = CommonObjects()
        self.np_web_elements = NetworkPolicyWebElements()
        self.device = Devices()
        self.device_update_web_elements = DeviceUpdate()
        self.dialogue_web_elements = DialogWebElements()
        self.screen = Screen()
        self.wireless_element = WirelessWebElements()
        self.tools = Tools()
        self.filter_element = FilterManageDeviceWebElements()
        self.robot_built_in = BuiltIn()
        self.devices_web_elements = DevicesWebElements()
        self.common_validation = CommonValidation()
        self.user_group = UserGroups()
        self.user_group_elements = UserGroupsWebElements()
        self.dev360 = Device360WebElements()
        self.use_existing_policy = False
        # self.driver = extauto.common.CloudDriver.cloud_driver
        self.switch_template = extauto.xiq.flows.configure.SwitchTemplate.SwitchTemplate()
        self.xapiNetworkPolicy = XapiNetworkPolicy()
        self.keyword_utils = KeywordUtils()

    def select_network_policy_row(self, policy):
        """
        - Select network policy row check box

        :param policy: Name of the policy row to select
        :return: 1
        """
        row = self._get_network_policy_row(policy)
        self.auto_actions.click(self.np_web_elements.get_np_row_cell(row, 'dgrid-selector'))
        return 1

    def _get_network_policy_row(self, policy):
        """
        Get the network policy row element
        :param policy: name of the policy
        :return:
        """
        self.utils.print_info("Getting the network policy rows")
        for row in self.np_web_elements.get_np_grid_rows():
            cell = self.np_web_elements.get_np_row_cell(row, 'field-name')
            if cell.text == policy:
                return row
        return None

    def _get_network_policy_list(self):
        """
        Get the network policy list from the Network policy page
        :return np_list: Network policy list from the network policies page
        """
        np_list = []
        if not self.navigator.navigate_to_network_policies_list_view_page() == 1:
            return -2

        self.utils.print_info("Getting the network policy rows")
        for row in self.np_web_elements.get_np_grid_rows():
            if cell := self.np_web_elements.get_np_row_cell(row, 'field-name'):
                np_list.append(cell.text)
        return np_list

    def _search_network_policy_in_list_view(self, policy):
        """
        - Search the network policy in list view of CONFIGURE-->NETWORK POLICIES page
        :param policy: Name of the policy to search
        :return:
        """
        policy_row = self._get_network_policy_row(policy)
        self.screen.save_screen_shot()
        if policy_row:
            self.utils.print_info(f"Network policy {policy} exists in the network policy list")
            return 1
        return -1

    def _perform_np_delete(self):
        """
        clicking on the network policy delete button
        :return:
        """

        self.utils.print_info("Click on network policy delete button")
        self.auto_actions.click_reference(self.np_web_elements.get_np_delete_button)
        # sleep(2)

        confirm_delete_btn = self.dialogue_web_elements.get_confirm_yes_button()
        if confirm_delete_btn:
            self.utils.print_info("Clicking on confirmation Yes button")
            self.auto_actions.click(confirm_delete_btn)
            confirm_dialog_box_display = True
            confirm_dialog_box = self.dialogue_web_elements.get_confirm_message_dialog_box()
            while confirm_dialog_box_display:
                if confirm_dialog_box.is_displayed():
                    self.utils.print_info("Network policy is deleting, still need some time")
                    sleep(1)
                else:
                    self.utils.print_info("Network policy is deleted successfully")
                    confirm_dialog_box_display = False
            self.screen.save_screen_shot()
            sleep(3)

    def create_network_policy_if_does_not_exist(self, policy, wireless_profile, cli_type='AH-AP', **kwargs):
        """
        - Search for network policy, if it doesn't exist, create it
        :param policy: Name of the network policy to create
        :param wireless_profile: (dict) wireless network creation profile parameters
        :param cli_type: Device type of the DUT
        :return: 1 if policy already exists or if it was successfully created, else -1
        """
        self.navigator.navigate_to_devices()
        if not self.navigator.navigate_to_network_policies_list_view_page() == 1:
            kwargs['fail_msg'] = "Failed to navigate to network policies list page"
            self.common_validation.fault(**kwargs)
        sleep(2)

        if self._search_network_policy_in_list_view(policy) == -1:
            return self.create_network_policy(policy, wireless_profile, cli_type)
        return 1

    def create_network_policy(self, policy, wireless_profile, cli_type='AH-AP', **kwargs):
        """
        - Create the network policy from CONFIGURE-->NETWORK POLICIES
        - This keyword will create the network policy and wireless network
        - Wireless network includes open, ppsk, psk and enterprise network
        - Keyword Usage:
        - ``Create Network Policy   ${POLICY_NAME}   ${WIRELESS_NW_PROFILE}``
        - ``Create Network Policy   ${POLICY_NAME}   ${WIRELESS_NW_PROFILE}     ${CLI_TYPE}``
        - ${POLICY_NAME} --> Name of the network policy to create
        - ${WIRELESS_NW_PROFILE} --> This is dictionary, include all key value pair to create wireless network
        - For Creating  ${WIRELESS_NW_PROFILE} dict refer wireless_network_config.robot
        - ${CLI_TYPE} --> Device type of the DUT. Default is 'AH-AP'.

        :param policy: Name of the network policy to create
        :param wireless_profile: (dict) wireless network creation profile parameters
        :param cli_type: Device type of the DUT. Default is 'AH-AP'.
        :return: 1 if network policy creation is success
        """

        # This code is currently disabled until the XAPI support SSID creation
        # if self.xapiNetworkPolicy.xapiNetworkPolicy.is_xapi_enabled(**kwargs):
        #    return self.xapiNetworkPolicy.xapi_create_network_policy(policy, wireless_profile, cli_type, **kwargs)

        # UI code to add a new network policy
        self.navigator.navigate_to_devices()
        if not self.navigator.navigate_to_network_policies_list_view_page() == 1:
            kwargs['fail_msg'] = "Failed to navigate to network policies list page"
            self.common_validation.fault(**kwargs)
            return -1

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Checking for network policy add button")
        if self.np_web_elements.check_np_add_button() == -2:
            kwargs['fail_msg'] = "Add button is not enabled for the user"
            self.common_validation.fault(**kwargs)
            return -1

        if self._search_network_policy_in_list_view(policy) == 1:
            kwargs['fail_msg'] = f"Network policy {policy} already exists in the network polices list"
            self.common_validation.failed(**kwargs)
            return -1

        self.utils.print_info("Click on network policy add button")
        self.auto_actions.click_reference(self.np_web_elements.get_np_add_button)
        sleep(2)

        self.utils.print_info("Enter the policy name:{}".format(policy))
        self.auto_actions.send_keys(self.np_web_elements.get_np_name_text(), policy)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Click on network policy save button")
        self.auto_actions.click_reference(self.np_web_elements.get_np_save_button)

        sleep(2)
        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)

        for tip_text in reversed(tool_tp_text):
            if "The Network Policy cannot be saved because" in tip_text:
                kwargs['fail_msg'] = f"The Network Policy cannot be saved because {tip_text}"
                self.common_validation.fault(**kwargs)
                return -1
            if "Your account does not have permission to perform that action" in tip_text:
                kwargs['fail_msg'] = f"Your account does not have permission to perform that action {tip_text}"
                self.common_validation.fault(**kwargs)
                return -1

            if "Unable to access data" in tip_text:
                kwargs['fail_msg'] = f"Not able to save the network policy {tip_text}"
                self.common_validation.fault(**kwargs)
                return -1

        if cli_type.upper() == 'AH-AP':
            return self.wireless_nw.create_wireless_network(**wireless_profile)
        if cli_type.upper() == 'VOSS' or cli_type.upper() == 'EXOS':
            switch_template_name = wireless_profile.get('switch_template_name')
            if not switch_template_name:
                self.utils.print_info("No template information in dictionary")
                return 1
            self.switch_template.create_switching_network(policy, wireless_profile)
        if cli_type.upper() == 'AH-XR':
            router_template_name = wireless_profile.get('template_name')
            if not router_template_name:
                self.utils.print_info("No template information in dictionary")
                return 1
            from extauto.xiq.flows.configure.RouterTemplate import RouterTemplate
            router_template = RouterTemplate()
            return router_template.create_routing_network(policy, wireless_profile)

    def delete_network_policy(self, policy, **kwargs):
        """
        - Delete Network Policy from network policy Grid
        - Keyword Usage:
        - ``Delete Network Policy    ${POLICY_NAME}``

        Supported Modes:
            UI - default mode
            XAPI - kwargs XAPI_ENABLE=True (Will only support XAPI keywords in your test)

        :param policy: Name of the policy to delete
        :return: 1 if deleted else -1
        """

        if self.xapiNetworkPolicy.is_xapi_enabled(**kwargs):
            policies = []
            policies.append(policy)
            return self.xapiNetworkPolicy.delete_network_polices(policies, **kwargs)

        if not self.navigator.navigate_to_network_policies_list_view_page() == 1:
            kwargs['fail_msg'] = "Couldn't Navigate to policies list view page"
            self.common_validation.fault(**kwargs)
            return -1

        # Get the total pages
        pages = self.common_objects.cobj_web_elements.get_page_numbers()
        if pages.is_displayed():
            last_page = int(pages.text[-1])
        select_flag = None
        policy_delete_attempted = False
        if pages.is_displayed() and last_page != 1:
            page_counter = 1
            self.utils.print_info(f"There are '{last_page}' page(s) to check")
            while page_counter <= last_page:
                if self._search_network_policy_in_list_view(policy) == 1:
                    self.utils.print_info("Select Network policy row")
                    self.select_network_policy_row(policy)
                    self.screen.save_screen_shot()
                    self._perform_np_delete()
                    select_flag = True
                    policy_delete_attempted = True
                    sleep(1)
                    self.utils.print_info(f"Network policy '{policy}' existed on page '{page_counter}' and was deleted")
                    # Once we have deleted the policy if we are not on page one reset to page one and stop
                    # walking thru the pages
                    if page_counter != 1:
                        # See if still have a pages, we might have delete the last policy on the page
                        still_have_pages = self.common_objects.cobj_web_elements.get_page_numbers()
                        if still_have_pages.is_displayed():
                            pageOne = self.devices_web_elements.get_devices_page_number_one()
                            self.utils.print_info("Clicking on Page 1 in network policy page.")
                            self.auto_actions.click(pageOne)
                            sleep(5)
                            self.screen.save_screen_shot()
                        else:
                            # We do not have pages so we will rest the screen
                            # This is hack to work around XIQ, the only way to refresh the screen
                            # is switch to devices than back to policies
                            if not self.navigator.navigate_to_devices() == 1:
                                kwargs['fail_msg'] = "Couldn't Navigate to devices page"
                                self.common_validation.fault(**kwargs)
                                return -1
                            if not self.navigator.navigate_to_network_policies_list_view_page() == 1:
                                kwargs['fail_msg'] = "Couldn't Navigate to policies list view page"
                                self.common_validation.fault(**kwargs)
                                return -1
                    break
                else:
                    self.utils.print_info(f"Network policy '{policy}' doesn't exist in page '{page_counter}'")
                    # If we did walk thru pages and did not find the device reset to page 1
                    if page_counter != 1:
                        pageOne = self.devices_web_elements.get_devices_page_number_one()
                        self.utils.print_info("Clicking on Page 1 in network policy page.")
                        self.auto_actions.click(pageOne)
                        sleep(5)
                        self.screen.save_screen_shot()

                # goto the next page
                page_counter += 1
                if page_counter <= last_page:
                    self.utils.print_info(f"Move to next page '{page_counter}'")
                    self.auto_actions.click_reference(self.common_objects.cobj_web_elements.get_next_page_element)
                    sleep(5)
                    self.screen.save_screen_shot()

        else:
            if self._search_network_policy_in_list_view(policy) == 1:
                self.utils.print_info("Select Network policy row")
                self.select_network_policy_row(policy)
                self.screen.save_screen_shot()
                self._perform_np_delete()
                select_flag = True
                policy_delete_attempted = True
                sleep(1)
            else:
                self.utils.print_info(f"Network policy '{policy}' doesn't exist in the network policies list")
                self.screen.save_screen_shot()

        if not select_flag:
            kwargs['pass_msg'] = f"Given Network policy {policy} is not present. Nothing to delete!"
            self.common_validation.passed(**kwargs)
            return 1

        if policy_delete_attempted:
            self.screen.save_screen_shot()

            tool_tp_text = tool_tip.tool_tip_text

            for value in reversed(tool_tp_text):
                if "Network policy was deleted successfully" in value:
                    kwargs['pass_msg'] = f"Network policy '{policy}' was deleted successfully"
                    self.common_validation.passed(**kwargs)
                    return 1
                elif "The Network Policy cannot be removed " in value:
                    kwargs['fail_msg'] = f"The Network Policy '{policy}' cannot be removed, {value}"
                    self.common_validation.failed(**kwargs)
                    return -1
                elif "The Network Policy cannot be deleted " in value:
                    kwargs['fail_msg'] = f"The Network Policy '{policy}' cannot be delete, {value}"
                    self.common_validation.failed(**kwargs)
                    return -1
                elif "An unknown error has occurred" in value:
                    kwargs['fail_msg'] = f"Unable to delete the network policy '{policy}', {value}"
                    self.common_validation.failed(**kwargs)
                    return -2

            # If we get here we didn't get an expected tooltip message. Check to see if the policy no longer exists,
            # if it's gone assume success.
            # JPS - May 1, 2023 - This makes a bad assumption- this does not walk thru pages if pages are present
            # This should be updated in the future
            if self._search_network_policy_in_list_view(policy) == 1:
                kwargs['fail_msg'] = f"Unable to perform the delete for network policy {policy}!"
                self.common_validation.failed(**kwargs)
                return -1

        kwargs['pass_msg'] = f"Successfully deleted Network Policy {policy}!"
        self.common_validation.passed(**kwargs)
        return 1

    def delete_network_polices(self, *policies, **kwargs):
        """
        - Deleting the network policies based on the passed list of policies
        - Keyword Usage:
        - ``Delete Network Policies   ${POLICY1}   ${POLICY2}``

        Supported Modes:
            UI - default mode
            XAPI - kwargs XAPI_ENABLE=True (Will only support XAPI keywords in your test)

        :param policies: list of network polices to delete
        :return: 1 if deleted successfully else -1
        """


        if self.xapiNetworkPolicy.is_xapi_enabled(**kwargs):
            return self.xapiNetworkPolicy.xapi_delete_network_polices(policies, **kwargs)

        if not self.navigator.navigate_to_network_policies_list_view_page() == 1:
            kwargs['fail_msg'] = "Couldn't Navigate to policies list view page"
            self.common_validation.failed(**kwargs)
            return -2

        policies_delete = []
        policies_not_present = []

        for policy in policies:
            # See if we have pages of policies
            pages = self.common_objects.cobj_web_elements.get_page_numbers()
            if pages.is_displayed():
                last_page = int(pages.text[-1])
            select_flag = None
            policy_delete_attempted = False
            if pages.is_displayed() and last_page != 1:
                page_counter = 1
                self.utils.print_info(f"There are '{last_page}' page(s) to check")
                while page_counter <= last_page:
                    if self._search_network_policy_in_list_view(policy) == 1:
                        self.utils.print_info("Select Network policy row")
                        self.select_network_policy_row(policy)
                        self.screen.save_screen_shot()
                        self._perform_np_delete()
                        select_flag = True
                        policy_delete_attempted = True
                        sleep(1)
                        self.utils.print_info(f"Network policy '{policy}' existed on page '{page_counter}' and delete was attempted")
                        # Once we have deleted the policy if we are not on page one reset to page one and stop
                        # walking thru the pages
                        if page_counter != 1:
                            # See if still have a pages, we might have delete the last policy on the page
                            still_have_pages = self.common_objects.cobj_web_elements.get_page_numbers()
                            if still_have_pages.is_displayed():
                                pageOne = self.devices_web_elements.get_devices_page_number_one()
                                self.utils.print_info("Clicking on Page 1 in network policy page.")
                                self.auto_actions.click(pageOne)
                                sleep(1)
                                self.screen.save_screen_shot()
                            else:
                                # We do not have pages so we will rest the screen
                                # This is hack to work around XIQ, the only way to refresh the screen
                                # is switch to devices than back to policies
                                if not self.navigator.navigate_to_devices() == 1:
                                    kwargs['fail_msg'] = "Couldn't Navigate to devices page"
                                    self.common_validation.fault(**kwargs)
                                    return -1
                                if not self.navigator.navigate_to_network_policies_list_view_page() == 1:
                                    kwargs['fail_msg'] = "Couldn't Navigate to policies list view page"
                                    self.common_validation.fault(**kwargs)
                                    return -1
                        break
                    else:
                        self.utils.print_info(f"Network policy '{policy}' doesn't exist in page '{page_counter}'")
                        if page_counter != 1:
                            pageOne = self.devices_web_elements.get_devices_page_number_one()
                            self.utils.print_info("Clicking on Page 1 in network policy page.")
                            self.auto_actions.click(pageOne)
                            sleep(1)
                            self.screen.save_screen_shot()

                    # goto the next page
                    page_counter += 1
                    if page_counter <= last_page:
                        self.utils.print_info(f"Move to next page {page_counter}")
                        self.auto_actions.click_reference(self.common_objects.cobj_web_elements.get_next_page_element)
                        sleep(1)
                        self.screen.save_screen_shot()
            else:
                if self._search_network_policy_in_list_view(policy) == 1:
                    self.utils.print_info("Select Network policy row")
                    self.select_network_policy_row(policy)
                    self.screen.save_screen_shot()
                    self._perform_np_delete()
                    select_flag = True
                    policy_delete_attempted = True

                    sleep(1)
                else:
                    self.utils.print_info(f"Network policy '{policy}' doesn't exist in the network policies list")
                    self.screen.save_screen_shot()

            if not select_flag:
                kwargs['pass_msg'] = f"Given Network policy '{policy}' is not present. Nothing to delete!"
                self.common_validation.passed(**kwargs)
                policies_not_present.append(policy)


            # If the desired policy was delete check for confirmation
            if policy_delete_attempted:
                self.screen.save_screen_shot()

                policy_delete_confirmed = False
                tool_tp_text = tool_tip.tool_tip_text
                self.utils.print_info(tool_tp_text)

                # Get the last tool tip generated

                for value in reversed(tool_tp_text):
                    if "Network policy was deleted successfully" in value:
                        kwargs['pass_msg'] = f"Network policy '{policy}' was deleted successfully"
                        self.common_validation.passed(**kwargs)
                        policy_delete_confirmed = True
                        policies_delete.append(policy)
                    elif "The Network Policy cannot be removed " in value:
                        kwargs['fail_msg'] = f"The Network Policy '{policy}' cannot be removed, {value}"
                        self.common_validation.failed(**kwargs)
                        return -1
                    elif "The Network Policy cannot be deleted " in value:
                        kwargs['fail_msg'] = f"The Network Policy '{policy}' cannot be delete, {value}"
                        self.common_validation.failed(**kwargs)
                        return -1
                    elif "An unknown error has occurred" in value:
                        kwargs['fail_msg'] = f"Unable to delete the network policy '{policy}', {value}"
                        self.common_validation.failed(**kwargs)
                        return -2

                # If we get here we didn't get an expected tooltip message. Check to see if the policy no longer exists,
                # if it's gone assume success.
                # JPS - May 1, 2023 - This makes a bad assumption- this does not walk thru pages if pages are present
                # This should be updated in the future
                if policy_delete_confirmed == False:
                    for policy in policies:
                        if self._search_network_policy_in_list_view(policy) == 1:
                            kwargs['fail_msg'] = "Unable to perform the delete!"
                            self.common_validation.failed(**kwargs)
                            return -1
        kwargs['pass_msg'] = f"Successfully deleted Network Policies! '{policies_delete}' and the following policies were not present '{policies_not_present}'"
        self.common_validation.passed(**kwargs)
        return 1

    def delete_all_network_policies(self, exclude_list='', **kwargs):
        """
        - Delete all network policies from the grid expect exclude_list policies
        - keyword Usage:
        - ``Delete All Network Policies  exclude_list=${POLICY1},${POLICY2)``

         Supported Modes:
            UI - default mode
            XAPI - kwargs XAPI_ENABLE=True (Will only support XAPI keywords in your test)

        :param exclude_list: list of policies to exclude from delete
        :return: 1 if deleted successfully else -1
        """

        if self.xapiNetworkPolicy.is_xapi_enabled(**kwargs):
            return self.xapiNetworkPolicy.xapi_delete_network_polices(exclude_list=exclude_list, **kwargs)

        exclude_list = exclude_list.split(",")
        np_list = self._get_network_policy_list()
        if np_list == -2:
            return -2

        delete_np_list = [np for np in np_list if np not in exclude_list]
        self.utils.print_info(f"Deleting network policy list:{delete_np_list}")

        return self.delete_network_polices(*delete_np_list)

    def edit_network_policy_ssid(self, policy_name, ssid_name, new_ssid_name, **kwargs):
        """
        - Edit the SSID name of the wireless network in the network policy
        - Flow: Navigate to the network policy -- > click on network policy card view
                --> click on SSID --> Edit SSID
        - Keyword Usage:
        - ``Edit Network Policy SSID   ${POLICY_NAME}   ${SSID_NAME}   ${NEW_SSID_NAME}``

        :param policy_name: Name of the network policy
        :param ssid_name: name of the ssid already exist on that network policy
        :param new_ssid_name: new ssid name
        :return: 1 if success
        """
        self.utils.print_info("Click on Network Policy card view button")
        self.navigator.navigate_to_network_policies_card_view_page(**kwargs)

        if self.select_network_policy_in_card_view(policy_name):
            if self._select_ssid(ssid_name):
                self.utils.print_info("Sending New SSID: ", new_ssid_name)
                self.auto_actions.send_keys(self.np_web_elements.get_network_policy_wireless_ssid_name_textfield(), new_ssid_name)

        self.utils.print_info("Clicking on Network Save button..")
        self.auto_actions.click_reference(self.np_web_elements.get_network_policy_wireless_networks_save_button)

        return 1

    def select_network_policy_in_card_view(self, policy_name, **kwargs):
        """
        - Selects the existing network polices card view

        :param policy_name: name of the policy to search
        :return: 1 if exists else -1
        """

        self.utils.print_info("Selecting Network Policy: ", policy_name)
        self.utils.print_info("Click on Network Policy card view button")
        self.auto_actions.click_reference(self.np_web_elements.get_network_policy_card_view)
        self.utils.wait_till(self.np_web_elements.get_network_policy_card_item,timeout=6, delay=2)
        policy_card = self.np_web_elements.get_network_policy_card_item()
        if policy_card is None:
            kwargs['fail_msg'] = "No Network Policy cards present. No policy configured"
            self.common_validation.failed(**kwargs)
            return -1
        try:
            policy_cards = self.keyword_utils.wait_for_elements_to_load(self.np_web_elements.get_network_policy_card_items, 2)
        except Exception as e:
            kwargs['fail_msg'] = f"The number of Network Policy cards changed {e} times"
            self.common_validation.failed(**kwargs)
            return -1

        for policy_card in policy_cards:
            if policy_name.upper() in policy_card.text.upper():
                self.utils.print_info(policy_card.text)
                self.auto_actions.click_reference(lambda: self.np_web_elements.get_network_policy_card_item_edit_icon(policy_card))
                kwargs['pass_msg'] = "Network Policy card/s present"
                self.common_validation.passed(**kwargs)
                return 1
        kwargs['fail_msg'] = "Unsuccessfully select network policy in card view"
        self.common_validation.failed(**kwargs)
        return -1

    def _select_ssid(self, ssid):
        """
        - Selects an SSID
        Assumption: Already Opened Network Policy
        :param ssid: name of the ssid
        :return:
        """

        if self._search_ssid(ssid):
            self.utils.print_info("Selecting SSID: ", ssid)
            self.auto_actions.click(self.np_web_elements.get_ssid_href(ssid))
            return 1
        return -1

    def _search_ssid(self, ssid):
        """
        - Search an SSID
        - Assumption: Already Opened Network Policy

        :param ssid:
        :return:
        """
        self.utils.print_info("Searching SSID: ", ssid)
        self.auto_actions.click_reference(self.np_web_elements.get_network_policy_wireless_networks_tab)
        sleep(5)
        grid_rows = self.np_web_elements.get_network_policy_wireless_networks_grid_rows()
        for row in grid_rows:
            if ssid in row.text:
                self.utils.print_info("Found SSID: ", ssid)
                return 1
        return -1

    def _select_device_row(self, search_string):
        """
        - Select the row of device in the deploy policy page

        :param search_string - It should be anything which is searched on the device row cell
        Example search_string be like "device_name", "Device Model", "Mac Address" or "Serial number"
        :return: 1 if device row selected else None
        """
        device_row = self._get_device_rows(search_string)
        sleep(2)
        if device_row:
            self.utils.print_info("Select device row to upload the network policy")
            self.auto_actions.click(self.np_web_elements.get_device_select_check_box(device_row))
            return 1

    def _get_device_rows(self, search_string):
        """
        Get the device rows from the deploy policy page
        :param search_string it should be anything which is searched on the row cell
        example search_string be like device_name, Device Model, Mac Address or Serial number
        :return: row element if row exists else return None
        """
        self.utils.print_info("Getting the Device rows from deploy policy page")
        device_rows = self.np_web_elements.get_device_grid_rows()
        if not device_rows:
            self.utils.print_info("Device rows are not available in the deploy policy page")
            return False
        for row in device_rows:
            if search_string in row.text:
                return row

    def deploy_network_policy(self, policy_name, devices, update_type='delta', next_reboot=False, _date=None,
                              _time=None, **kwargs):
        """
        - Deploy the network policy to the particular device
        - By default it will do delta config push
        - If want to perform different type of config push, pass the appropriate parameter values
        - If already in network policy then deploy the policy else navigate to network policy--> deploy policy tab
        - Keyword Usage:
        - ``Deploy Network Policy  ${POLICY_NAME}   ${DEVICE_MAC}``
        - ``Deploy Network Policy  ${POLICY_NAME}   ${DEVICE_MAC}  update_type=complete``
        - ``Deploy Network Policy  ${POLICY_NAME}   ${DEVICE_MAC}  next_reboot=True``
        - ``Deploy Network Policy  ${POLICY_NAME}   ${DEVICE_MAC}  _date=${DATE}  _time=${TIME}``

        :param policy_name: Name of the policy
        :param devices: Device serial number
        :param update_type: Config update type. By default it is complete
        :param next_reboot: Next reboot option
        :param _date: date when to update
        :param _time: time when to update
        :return:
        """

        if self.np_web_elements.get_np_policy_crumb_button():
            self.utils.print_info("Inside Network Policy...")
        else:
            self.utils.print_info("Not inside Network Policy. Navigating...")
            self.navigate_to_np_edit_tab(policy_name)

        sleep(5)

        self.utils.print_info("Click on deploy policy tab")
        self.auto_actions.click_reference(self.np_web_elements.get_deploy_policy_tab)
        sleep(2)

        self.utils.print_info("Click on eligible device button")
        self.auto_actions.click_reference(self.np_web_elements.get_eligible_device_button)
        sleep(5)

        self.navigator.enable_page_size()

        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)
        for tip_text in tool_tp_text:
            if "An unknown error has" in tip_text:
                kwargs['fail_msg'] = f"{tip_text} occurred while assigning nw policy"
                self.common_validation.fault(**kwargs)
                return -1

        if not self._select_device_row(devices):
            kwargs['fail_msg'] = "Device is not available in the deploy policy page"
            self.common_validation.fault(**kwargs)
            return -1

        self.screen.save_screen_shot()
        sleep(5)
        self.utils.print_info("Click on the policy deploy upload button")
        self.auto_actions.click_reference(self.np_web_elements.get_deploy_policy_upload_button)

        sleep(10)

        if update_type == 'delta' and next_reboot == False and _date == None:
            self.utils.print_info("Selecting Delta Config Update")
            self.auto_actions.click_reference(self.device_update_web_elements.get_delta_config_update_radio)
            sleep(2)
            self.screen.save_screen_shot()
            self.utils.print_info("Click on the perform update")
            self.auto_actions.click_reference(self.np_web_elements.get_perform_update_button)
            sleep(2)
            tool_tp_text = tool_tip.tool_tip_text
            self.utils.print_info(tool_tp_text)
            for value in tool_tp_text:
                if "a device mode change is not supported with a delta configuration update" in value.lower():
                    self.utils.print_info(value)
                    update_type = "complete"

        if update_type == 'complete':
            self.utils.print_info("Selecting Complete Config Update")
            self.auto_actions.click_reference(self.device_update_web_elements.get_complete_config_update_radio)
            self.screen.save_screen_shot()
            sleep(2)

        if next_reboot:
            update_type = "complete"
            self.utils.print_info("Selecting Complete Config Update")
            self.auto_actions.click_reference(self.device_update_web_elements.get_complete_config_update_radio)
            sleep(2)

            self.utils.print_info("Selecting Next Reboot radio")
            self.auto_actions.click_reference(self.device_update_web_elements.get_activate_at_next_reboot_radio)
            sleep(2)

        if _date:
            update_type = "complete"
            self.utils.print_info("Selecting Complete Config Update")
            self.auto_actions.click_reference(self.device_update_web_elements.get_complete_config_update_radio)
            sleep(2)

            self.utils.print_info("Selecting Activate at radio")
            self.auto_actions.click_reference(self.device_update_web_elements.get_activate_at_time_radio)
            sleep(2)

            self.utils.print_info("Selecting Time to update")

            self.auto_actions.send_page_down(self.device_update_web_elements.get_activate_at_time_radio())
            sleep(5)

            self.auto_actions.click_reference(self.device_update_web_elements.get_activate_at_date_textfield)
            sleep(5)
            self.auto_actions.send_keys(self.device_update_web_elements.get_activate_at_date_textfield(), _date)
            sleep(5)

            self.auto_actions.click_reference(self.device_update_web_elements.get_activate_at_time_textfield)
            sleep(5)
            self.auto_actions.send_keys(self.device_update_web_elements.get_activate_at_time_textfield(), _time)
            sleep(5)

        self.screen.save_screen_shot()

        if update_type != 'delta':
            self.utils.print_info("Click on the perform update")
            self.auto_actions.click_reference(self.np_web_elements.get_perform_update_button)
            self.screen.save_screen_shot()
            sleep(20)

        self.utils.print_info("Get the deployed network policy for the AP")
        self.navigator.navigate_to_devices()
        sleep(5)

        self.utils.print_info("Checking the device updating status")
        # Assuming that config push will take maximum five minutes
        # checking device update status for every 30 seconds
        retry_count = 0
        max_config_push_wait = self.robot_built_in.get_variable_value("${MAX_CONFIG_PUSH_TIME}")
        while True:
            self.utils.print_info(f"Time elapsed for device update:{retry_count} seconds")
            device_update_status = self.device.get_device_updated_status(devices)
            if re.search(r'\d+-\d+-\d+', device_update_status):
                break
            elif retry_count >= int(max_config_push_wait):
                kwargs['fail_msg'] = f"Config push to AP taking more than {max_config_push_wait} seconds"
                self.common_validation.failed(**kwargs)
                return -1
            sleep(30)
            retry_count += 30

        network_policy = self.device.get_ap_network_policy(devices)
        if network_policy == policy_name:
            kwargs['pass_msg'] = "Network Policy in Devices grid matches..."
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Network Policy in Devices grid does not matches with the deployed one..."
            self.common_validation.failed(**kwargs)
            return -1

    def navigate_to_np_edit_tab(self, policy_name, **kwargs):
        """
        - Flow: Configure-->Network policy-->Select List View-->Select Network Policy ROW--> Edit

        :param policy_name: policy name
        :return: 1 if navigation to the edit tab was complete
                 -1 if elements are not found along the way
        """

        self.utils.print_info("Navigating to the configure network policies")
        self.navigator.navigate_configure_network_policies()

        self.utils.print_info("Searching for network policy list view button...")
        list_view_button = self.np_web_elements.get_network_policy_list_view()
        if list_view_button:
            self.utils.print_info("Network policy list view button found! Clicking... ")
            self.auto_actions.click_reference(self.np_web_elements.get_network_policy_list_view)
        else:
            kwargs['fail_msg'] = "List view button not found!"
            self.common_validation.fault(**kwargs)
            return -1

        self.utils.print_info("Searching for network policy 100 rows per page button...")
        view_all_pages = self.np_web_elements.get_nw_policy_port_types_view_all_pages()
        if view_all_pages:
            self.utils.print_info("Network Policy fill size is present on page. Clicking... ")
            self.auto_actions.click(view_all_pages)
        else:
            self.utils.print_info("Network Policy fill size is not present on page. Continue running... ")

        self.utils.print_info("Select the network policy rows")
        current_page = 1
        policy_found = False

        while True:
            self.utils.print_info(f"Current page: {current_page}")
            self.utils.print_info("Waiting for Network Policy rows to load...")
            self.utils.wait_till(self.np_web_elements.get_np_grid_rows)
            self.navigator.wait_until_loading_is_done()
            self.utils.print_info("Network Policy rows have been loaded. Searching for "
                                  f"Network Policy: {policy_name} ...")

            try:
                rows = self.np_web_elements.get_np_grid_rows()
                if rows:
                    for row in rows:
                        self.utils.print_info(f"Looking for {policy_name} on row: {row.text}")
                        if policy_name in row.text:
                            policy_found = True
                            self.utils.print_info(f"Network policy: {policy_name} has been found on the row: "
                                                  f"{row.text}")
                            self.utils.print_info(f"Searching the checkbox for row: {row.text} ...")
                            row_check_box = self.np_web_elements.get_np_row_cell(row, 'dgrid-selector')
                            if row_check_box:
                                self.utils.print_info(f"Found the checkbox for row: {row.text}! Clicking ... ")
                                self.auto_actions.click(row_check_box)
                                self.utils.print_info("Clicking on network policy Edit button...")
                                np_edit_button = self.np_web_elements.get_np_edit_button()
                                if np_edit_button:
                                    self.auto_actions.click(np_edit_button)
                                    kwargs['pass_msg'] = "Found the Edit button!"
                                    self.common_validation.passed(**kwargs)
                                    return 1
                                else:
                                    kwargs['fail_msg'] = "Edit button not found!"
                                    self.common_validation.fault(**kwargs)
                                    return -1
                else:
                    kwargs['fail_msg'] = "Rows were not found!"
                    self.common_validation.failed(**kwargs)
                    return -1
            except selenium.common.exceptions.StaleElementReferenceException as e:
                self.utils.print_info("Stale Element error: \n", e)
                self.utils.print_info(f"Checking the rows for the policy: {policy_name} again...")
                continue

            if not policy_found:
                if not self.np_web_elements.get_next_page_element_disabled():
                    self.utils.print_info(f"The network policy {policy_name} is not present on page: {current_page}. "
                                          f"Checking next page: {current_page + 1}...")
                    self.auto_actions.click_reference(self.np_web_elements.get_next_page_element)
                    current_page += 1
                else:
                    kwargs['fail_msg'] = f"This is the last page: {current_page}. Network policy was not found in " \
                                         f"all {current_page} pages. It was deleted or not created at all."
                    self.common_validation.failed(**kwargs)
                    return -1

    def add_wireless_nw_to_network_policy(self, policy_name, **wireless_profile):
        """
        - It will add the wireless network to existing network policy
        - Flow: Navigate to Network policy-->Select List View-->Select Network Policy ROW-->
          Edit-->Select wireless nw tab-->Add other wireless network
        - Keyword Usage:
        - ``Add Wireless Nw To Network Policy    ${POLICY_NAME}    &{WIRELESS_NW_PROFILE}``
        - &{WIRELESS_NW_PROFILE} --> This is dictionary, include all key value pair to create wireless network
        - Fof Creating  &{WIRELESS_NW_PROFILE} dict refer wireless_network_config.robot

        :param policy_name: name of the network policy
        :param wireless_profile: (dict) wireless network profile config parameters
        :return:1 if success else -1
        """
        self.navigator.navigate_to_devices()
        self.navigate_to_np_edit_tab(policy_name)
        return self.wireless_nw.create_wireless_network(**wireless_profile)

    def delete_network_policy_with_ssid(self, ssid_name, **kwargs):
        """
        - Deleting the network policy based on SSID name attached to it
        - list all network policy from card view, get the ssid name of each policy , if any policy consists passed
          ssid_name then delete that network policy
        - Keyword Usage:
        - ``Delete Network Policy With SSID   ${SSID_NAME}``

        :param ssid_name: name of the ssid used to delete the network policy
        :return:
        """
        self.utils.print_info("Deleting policy with SSID: ", ssid_name)
        policy_name = self._get_network_policy_with_ssid(ssid_name)
        sleep(5)

        self.utils.print_info("Found policy with SSID: ", policy_name)

        if policy_name:
            return self.delete_network_policy(policy_name)
        else:
            kwargs['fail_msg'] = f"Unable to find policy with SSID {ssid_name}"
            self.common_validation.failed(**kwargs)
            return -1

    def _get_network_policy_with_ssid(self, ssid_name):
        """
        :param ssid_name:
        :return:
        """
        self.utils.print_info("Navigating Network Policies")
        if self.navigator.navigate_configure_network_policies() == -2:
            return -2
        sleep(5)

        self.utils.print_info("Click on Network Policy card view button")
        self.auto_actions.click_reference(self.np_web_elements.get_network_policy_card_view)
        sleep(2)

        self.utils.print_info("Getting Network Policy list from Card view")
        cards = self.np_web_elements.get_network_policy_cards()
        if cards:
            for card in cards:
                ssids = self.np_web_elements.get_network_policy_card_ssids(card)
                if ssids:
                    for ssid in ssids:
                        if ssid_name in ssid.text:
                            self.utils.print_info("SSID: ", ssid.text)
                            return self.np_web_elements.get_network_policy_name_from_card_view(card).text

        return None

    def deploy_network_policy_with_complete_update(self, policy_name, devices, cli_type='AH-AP', **kwargs):
        """
        - Config push network policy with complete update
        - This will reboot the Device
        - if already in network policy then deploy the policy else navigate to network policy--> deploy policy tab
        - Keyword Usage:
        - ``Deploy Network Policy With Complete Update   ${POLICY_NAME}    ${DEVICE_MAC}``

        Supported Modes:
            UI - default mode
            XAPI - kwargs XAPI_ENABLE=True (Will only support XAPI keywords in your test)

        :param policy_name: Name of the policy
        :param devices: Device serial number
        :return: 1 if success else -1
        """

        # Need to write up a bug on this XAPI not working correctly
        # if self.xapiNetworkPolicy.is_xapi_enabled(**kwargs):
        #     if cli_type == 'AH-AP':
        #         self.utils.print_info("ClI Type: AH-AP detected, updated type to Complete")
        #         update_type = 'complete'
        #     return self.xapiNetworkPolicy.xapi_deploy_network_policy_with_complete_update(policy_name,
        #                                                                                   devices,
        #                                                                                   update_type)
        # UI
        if cli_type == 'AH-AP':
            return self.deploy_network_policy(policy_name, devices, 'complete')
        else:
            return self.device.deploy_switch_network_policy_with_complete_update(devices, policy_name)

    def deploy_network_policy_with_next_reboot(self, policy_name, devices):
        """
        - Config push network policy in next reboot
        - this will do completed config push for the next reboot of device
        - if already in network policy then deploy the policy else navigate to network policy--> deploy policy tab
        - Keyword Usage:
        - ``Deploy Network Policy With Next Reboot   ${POLICY_NAME}    ${DEVICE_MAC}``

        :param policy_name: Name of the policy
        :param devices: Device serial number
        :return:  1 if success else -1
        """
        return self.deploy_network_policy(policy_name, devices, next_reboot=True)

    def deploy_network_policy_at_specific_time(self, policy_name, devices, update_date, update_time):
        """
        - Config push network policy at specific time
        - it will config push at specific date and at specific time
        - if already in network policy then deploy the policy else navigate to network policy--> deploy policy tab
        - Keyword Usage:
        - ``Deploy Network Policy At Specific Time   ${POLICY_NAME}  ${DEVICE_MAC}  ${UPDATE_DATE}  ${UPDATE_TIME}``

        :param policy_name:  Name of the policy
        :param devices:  Device serial number
        :param update_date: date to update
        :param update_time: update time
        :return: 1 if success else -1
        """
        _upgrade_time = self.utils.round_time(update_time)

        self.utils.print_info("Target Time: ", str(_upgrade_time))
        _upgrade_time_24 = self.utils.convert_time_to_24_hours_format(_upgrade_time)

        if self.deploy_network_policy(policy_name, devices, _date=update_date, _time=_upgrade_time):
            return _upgrade_time_24

    def deploy_network_policy_with_delta_update(self, policy_name, devices, **kwargs):
        """
        - delta config push of network policy
        - if already in network policy then deploy the policy else navigate to network policy--> deploy policy tab
        - Keyword Usage:
        - ``Deploy Network Policy With Delta Update   ${POLICY_NAME}   ${DEVICE_MAC}``

        :param policy_name: Name of the policy
        :param devices: Device serial number
        :return:
        """
        # need to write up a bug on this XAPI
        # if self.xapiNetworkPolicy.is_xapi_enabled(**kwargs):
        #     return self.xapiNetworkPolicy.xapi_deploy_network_policy_with_delta_update(policy_name,
        #                                                                                devices,
        #                                                                                 'delta')
        #else:
        return self.deploy_network_policy(policy_name, devices, 'delta')

    def _check_navigation_to_network_policy_page(self):
        """
        Get the network policy list from the Network policy page
        :return np_list: Network policy list from the network policies page
        """
        self.utils.print_info("Navigating to the configure network policies")
        if self.navigator.navigate_configure_network_policies() == -2:
            return -2
        sleep(3)

        self.utils.print_info("Click on network policy list view button")
        self.auto_actions.click_reference(self.np_web_elements.get_network_policy_list_view)

        cell = self.np_web_elements.get_np_page_title()
        sleep(2)
        title = cell.text

        self.utils.print_info("page title :", title)

        if title == "Network Policies":
            return 1
        else:
            return -2

    def navigate_wireless_ssid(self, policy_name, ssid, **kwargs):
        """
        - Flow: Configure --> Network Policies--> Select the policy-->Wireless tab--> Select SSID

        :param policy_name: name of the network policy
        :param ssid: ssid name
        :return:
        """
        self.navigate_to_np_edit_tab(policy_name)
        if not self._select_ssid(ssid) == 1:
            kwargs['fail_msg'] = f"SSID: {ssid} not selected"
            self.common_validation.failed(**kwargs)
            return -1
        return 1

    def delete_radius_group(self, network_policy_name, radius_group_name):
        """
        - Delete Radius Server Group from wireless network
        - For deleting radius server group, navigate to the network policy--> go to wireless network tab
          --> add ssid --> select enterprise network --> click on radius server select button
          --> select the radius server group and delete it
        - Keyword Usage:
        - ``Delete Radius Group    ${POLICY_NAME}   ${RADIUS_SERVER_GROUP_NAME}``

        :param network_policy_name: Network Policy Name
        :param radius_group_name: Name of the radius group to delete
        :return: 1 if deleted else -1
        """

        self.utils.print_info("Navigate to Network Policy Name Edit...")
        self.navigate_to_np_edit_tab(network_policy_name)

        self.utils.print_info("Navigate to Standard Wireless Enterprise Network")
        self.wireless_nw.navigate_to_standard_enterprise_network()

        self.utils.print_info("Delete Radius Server Group")
        self.wireless_nw.radius_server.delete_radius_server_group(radius_group_name)

        return True

    def get_all_ssids_in_policy(self, policy, new_ssid=True, special_char=True):
        """ return all ssids in each policy
            :param: policies: list of policies
            :param: new_ssid: Create a new ssid when the new_ssid is True
            :param: special_char:  Create a new ssid with a special chars if the special_char is true
            :return a dictionary contains policies and ssids
        """
        from collections import defaultdict
        self.utils.print_info(" Get all ssids from the policy " + str(policy))
        ssid_list = defaultdict(list)
        ssid_name = None
        self.navigate_to_np_edit_tab(policy)
        if new_ssid:
            if special_char:
                ssid_name = self.utils.get_random_string() + '$#^&*->'
            else:
                ssid_name = self.utils.get_random_string()
            rc = {'ssid_name': ssid_name, 'network_type': 'GUESTACCESS', 'guest_auth_type': "unsecure",
                  'guest_auth_config': {'guest_access_nw_without_login': 'enable'}}
            self.utils.print_info(" Create a new guess network " + str(ssid_name))
            self.wireless_nw.create_wireless_network(**rc)

        self.auto_actions.click_reference(self.wireless_element.get_wireless_networks_tab)
        ssid_element_list = self.wireless_element.get_ssid_list()

        if ssid_element_list:
            ssids = []
            for ssid in ssid_element_list:
                ssids.append(ssid.text)
            while ("" in ssids): ssids.remove("")
            for ssid in ssids:
                ssid_list[policy].append(ssid)
        else:
            return False, False

        self.utils.print_info(" SSID list of the policy " + str(ssid_list))
        self.utils.print_info(" Exit getting all ssids ")

        return ssid_list, ssid_name

    def delete_all_ssid_in_policy(self, policy, **kwargs):
        """ delete all ssids in the policy
            :param: policy: name of the policy
            :return 1 if deletion of ssids is success
        """
        self.utils.print_info(" Delete all ssids in the policy  " + str(policy))
        self.auto_actions.scroll_up()
        self.navigate_to_np_edit_tab(policy)

        self.utils.print_info(" Click on the wireless network tab")
        try_cnt = 0
        wireless_networks_page = self.wireless_element.get_wireless_nw_tab_page()
        while try_cnt < 10:
            self.auto_actions.click_reference(self.wireless_element.get_wireless_networks_tab)
            self.utils.print_info(f" The value of wireless networks page {wireless_networks_page}")
            if wireless_networks_page:
                self.utils.print_info("Go to Wireless Networks tab successfully")
                break
            else:
                try_cnt += 1
                self.utils.print_info(f"Failed to go to Wireless Networks tab, try {try_cnt} times")
                sleep(1)
                if try_cnt == 10:
                    kwargs['fail_msg'] = f"Max {try_cnt} times to switch to Wireless Networks tab, " \
                                         "but still failed, need figure out issue manually"
                    self.common_validation.fault(**kwargs)
                    return -1
        self.utils.print_info("Get all ssids in the policy")
        ssids = self.wireless_element.get_ssid_list()
        self.utils.print_info(f"The SSIDs in the policy: {ssids}")
        if not ssids:
            self.utils.print_info("There are no SSIDs configured on policy  " + str(policy))
        else:
            self.utils.print_info("Select all SSIDs to be deleted")
            for ssid in ssids:
                self.utils.print_info("Selecting  ssid : " + ssid.text)
                check_box = self.wireless_element.get_ssid_chkbox(ssid)
                if check_box:
                    self.auto_actions.click(check_box)
                else:
                    kwargs['fail_msg'] = "Unable to select row"
                    self.common_validation.fault(**kwargs)
                    return -1

            delete_button = self.wireless_element.get_wireless_delete_button()
            if delete_button:
                self.auto_actions.click(delete_button)
                sleep(5)
                confirm_yes = self.wireless_element.get_confirm_dialog_yes_button()
                if confirm_yes:
                    self.auto_actions.click(confirm_yes)
                    self.screen.save_screen_shot()
                    sleep(5)
                else:
                    kwargs['fail_msg'] = "Unable click the confirm Yes button"
                    self.common_validation.fault(**kwargs)
                    return -1
            else:
                kwargs['fail_msg'] = "Unable to click the Delete button"
                self.common_validation.fault(**kwargs)
                return -1
        reuse_button = self.wireless_element.get_wireless_re_use_button()
        if reuse_button:
            self.auto_actions.click(reuse_button)
            sleep(5)
            all_reusable_rows = self.wireless_element.get_wireless_ssid_select_window_rows()
            if all_reusable_rows:
                for ssid_row in all_reusable_rows:
                    if ssid_row.text != 'ssid0' and ssid_row.text != 'Name':
                        self.utils.print_info(" Selecting  ssid : " + ssid_row.text + " from SSID list")
                        check_box_reusable = self.wireless_element.get_wireless_select_ssid_row_check_box(ssid_row)
                        if check_box_reusable:
                            self.auto_actions.click(check_box_reusable)
                        else:
                            kwargs['fail_msg'] = "Unable to select SSID"
                            self.common_validation.fault(**kwargs)
                            return -1
                self.utils.print_info(" Clicking  delete button ")
                re_use_delete_button = self.wireless_element.get_wireless_re_use_delete_button()
                if re_use_delete_button:
                    self.auto_actions.click(re_use_delete_button)
                    sleep(5)
                    confirm_yes_re_usable = self.wireless_element.get_confirm_dialog_yes_button()
                    if confirm_yes_re_usable:
                        self.auto_actions.click(confirm_yes_re_usable)
                        tool_tp_text = tool_tip.tool_tip_text
                        self.utils.print_info(tool_tp_text)
                        self.utils.print_info(" Closing SSID pop-up window ")
                        self.auto_actions.click_reference(self.wireless_element.get_wireless_re_use_cancel_button)
                        if "deleted successfully" in str(tool_tp_text):
                            kwargs['pass_msg'] = "SSIDs were successfully deleted"
                            self.common_validation.passed(**kwargs)
                            return 1
                        else:
                            kwargs['fail_msg'] = "SSIDs were NOT successfully deleted"
                            self.common_validation.failed(**kwargs)
                            return -1
                    else:
                        kwargs['fail_msg'] = "Unable to click on confirm yes button"
                        self.common_validation.fault(**kwargs)
                        return -1
                else:
                    kwargs['fail_msg'] = "Unable to click the delete button"
                    self.common_validation.fault(**kwargs)
                    return -1
            else:
                kwargs['fail_msg'] = "Unable to gather SSID rows"
                self.common_validation.fault(**kwargs)
                return -1

        kwargs['fail_msg'] = "Unable to delete all SSIDs"
        self.common_validation.failed(**kwargs)
        return -1

    def delete_single_ssid_in_policy(self, policy, ssid_name, **kwargs):
        """ delete all ssids in the policy
            :param: policy: name of the policy
            :return 1 if deletion of ssids is success
        """
        self.utils.print_info(" Delete all ssids in the policy  " + str(policy))
        self.auto_actions.scroll_up()
        self.navigate_to_np_edit_tab(policy)

        self.utils.print_info(" Click on the wireless network tab")
        self.auto_actions.click_reference(self.wireless_element.get_wireless_networks_tab)
        self.tools.wait_til_elements_avail(self.wireless_element.wireless_nw_add_button, 60, False)
        self.utils.print_info(" Get all ssids in the policy")
        ssids = self.wireless_element.get_ssid_list()
        if not ssids:
            kwargs['pass_msg'] = f"There are no SSIDs configured on policy {str(policy)}"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            self.utils.print_info(" Select the SSID to be deleted")
            for ssid in ssids:
                if ssid_name in ssid.text:
                    check_box = self.wireless_element.get_ssid_chkbox(ssid)
                    if check_box:
                        self.auto_actions.click(check_box)
                    else:
                        kwargs['fail_msg'] = "Unable to select row"
                        self.common_validation.fault(**kwargs)
                        return -1

            delete_button = self.wireless_element.get_wireless_delete_button()
            if delete_button:
                self.auto_actions.click(delete_button)
                sleep(5)
                confirm_yes = self.wireless_element.get_confirm_dialog_yes_button()
                if confirm_yes:
                    self.auto_actions.click(confirm_yes)
                    sleep(5)
                    reuse_button = self.wireless_element.get_wireless_re_use_button()
                    if reuse_button:
                        self.auto_actions.click(reuse_button)
                        sleep(5)
                        all_reusable_rows = self.wireless_element.get_wireless_ssid_select_window_rows()
                        if all_reusable_rows:
                            for ssid_row in all_reusable_rows:
                                if ssid_row.text != 'ssid0' and ssid_row.text != 'Name':
                                    if ssid_name in ssid_row.text:
                                        self.utils.print_info(" Selecting  ssid : " + ssid_row.text + " from SSID list")
                                        check_box_reusable = self.wireless_element.get_wireless_select_ssid_row_check_box(ssid_row)
                                        if check_box_reusable:
                                            self.auto_actions.click(check_box_reusable)
                                        else:
                                            kwargs['fail_msg'] = "Unable to select SSID"
                                            self.common_validation.fault(**kwargs)
                                            return -1
                            self.utils.print_info(" Clicking  delete button ")
                            re_use_delete_button = self.wireless_element.get_wireless_re_use_delete_button()
                            if re_use_delete_button:
                                self.auto_actions.click(re_use_delete_button)
                                sleep(5)
                                confirm_yes_re_usable = self.wireless_element.get_confirm_dialog_yes_button()
                                if confirm_yes_re_usable:
                                    self.auto_actions.click(confirm_yes_re_usable)
                                    tool_tp_text = tool_tip.tool_tip_text
                                    self.utils.print_info(tool_tp_text)
                                    self.utils.print_info(" Closing SSID pop-up window ")
                                    self.auto_actions.click_reference(self.wireless_element.get_wireless_re_use_cancel_button)
                                    if "deleted successfully" in str(tool_tp_text):
                                        kwargs['pass_msg'] = "SSIDs were successfully deleted"
                                        self.common_validation.passed(**kwargs)
                                        return 1
                                    else:
                                        kwargs['fail_msg'] = "SSIDs were NOT successfully deleted"
                                        self.common_validation.failed(**kwargs)
                                        return -1
                                else:
                                    kwargs['fail_msg'] = "Unable to click on confirm yes button"
                                    self.common_validation.fault(**kwargs)
                                    return -1
                            else:
                                kwargs['fail_msg'] = "Unable to click the delete button"
                                self.common_validation.fault(**kwargs)
                                return -1
                        else:
                            kwargs['fail_msg'] = "Unable to gather SSID rows"
                            self.common_validation.fault(**kwargs)
                            return -1
                    else:
                        kwargs['fail_msg'] = "Unable click the reusable [select] button"
                        self.common_validation.fault(**kwargs)
                        return -1
                else:
                    kwargs['fail_msg'] = "Unable click the confirm Yes button"
                    self.common_validation.fault(**kwargs)
                    return -1
            else:
                kwargs['fail_msg'] = "Unable to click the Delete button"
                self.common_validation.fault(**kwargs)
                return -1
        return -1

    def enable_nw_presence_analytics(self, nw_policy):
        """
        - This keyword is used to enable the presence analytics
        - Flow: Configure --> Network Policy --> select the Policy --> Enable Presence Analytics
        - Keyword Usage:
        - ``Enable NW Presence Analytics  ${POLICY_NAME}``

        :param nw_policy: name of the policy
        :return: None
        """
        self.navigator.navigate_to_devices()
        self.navigate_to_np_edit_tab(nw_policy)
        sleep(2)

        self.utils.print_info("Clicking on presence analytics button")
        self.auto_actions.click_reference(self.np_web_elements.get_enable_presence_analytics_btn)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Click on network policy save button")
        self.auto_actions.click_reference(self.np_web_elements.get_np_save_button)

    def enable_ibeacon_service_in_network_policy(self, nw_policy, service_name, uuid, monitoring, **kwargs):
        """
        - This keyword is used to enable Ibeacon Service in Network Policy
        - Flow: Configure --> Network Policy --> select the Policy -->Advance Settings-->IBeacon Services
        - Keyword Usage:
        - ''Enable IBeacon Service In Network Policy  ${POLICY_NAME}  ${service_name}  ${uuid} monitoring=enable ''
        - ''Enable IBeacon Service In Network Policy  ${POLICY_NAME}  ${service_name}  ${uuid} monitoring=disable ''

        :param nw_policy: name of the policy
        :param service_name: IBeacon Service Name
        :param uuid: Enter UUID
        :param monitoring=enable : Enable iBeacon Monitoring via checkbox if it was previously disabled
        :param monitoring=disable : Disable iBeacon Monitoring via checkbox
        :return: None
        """

        self.navigator.navigate_to_devices()
        self.navigate_to_np_edit_tab(nw_policy)
        sleep(2)

        self.utils.print_info("Clicking on Additional Settings Tab")
        self.auto_actions.click_reference(self.np_web_elements.get_network_policy_additional_settings_tab)
        sleep(2)

        if self.np_web_elements.get_additional_settings_ibeacon_menu().is_displayed():
            self.utils.print_info("Click on iBeacon Service Menu button")
            self.auto_actions.click_reference(self.np_web_elements.get_additional_settings_ibeacon_menu)
            sleep(2)
        else:
            self.utils.print_info("Click Security Tab")
            self.auto_actions.click_reference(self.np_web_elements.get_policy_settings_menu)
            sleep(2)
            self.utils.print_info("Click on iBeacon Service Menu button")
            self.auto_actions.click_reference(self.np_web_elements.get_additional_settings_ibeacon_menu)
            sleep(2)

        sleep(5)
        self.utils.print_info("Click on Enable IBeacon service button")
        if not self.np_web_elements.get_ibeacon_status_button().is_selected():
            self.auto_actions.click_reference(self.np_web_elements.get_ibeacon_status_button)
            sleep(2)

        self.utils.print_info("Enter IBeacon Service Name")
        self.auto_actions.send_keys(self.np_web_elements.get_ibeacon_service_name_textfield(), service_name)
        sleep(3)

        self.utils.print_info("Enter IBeacon Service Description")
        self.auto_actions.send_keys(self.np_web_elements.get_ibeacon_description_textfield(), service_name)
        sleep(3)

        self.utils.print_info("Enter IBeacon UUID")
        self.auto_actions.send_keys(self.np_web_elements.get_ibeacon_uuid_textfield(), uuid)
        sleep(5)

        if monitoring == 'enable':
            self.utils.print_info("Enable IBeacon Monitoring Checkbox")
            if not self.np_web_elements.get_ibeacon_monitoring_checkbox().is_selected():
                self.auto_actions.click_reference(self.np_web_elements.get_ibeacon_monitoring_checkbox)
                sleep(2)

        elif monitoring == 'disable':
            self.utils.print_info("Disable IBeacon Monitoring Checkbox")
            if self.np_web_elements.get_ibeacon_monitoring_checkbox().is_selected():
                self.auto_actions.click_reference(self.np_web_elements.get_ibeacon_monitoring_checkbox)
                sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Click on Save button")
        self.auto_actions.click_reference(self.np_web_elements.get_ibeacon_services_save_button)
        sleep(3)

        self.utils.print_info("Checking the Save profile message...")
        observed_nwpolicy_message = self.np_web_elements.get_np_save_tool_tip().text
        self.utils.print_info("Observed Message: ", observed_nwpolicy_message)

        if "iBeacon settings saved successfully" in observed_nwpolicy_message:
            kwargs['pass_msg'] = "iBeacon settings saved successfully"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Failed to enable ibeacon service"
            self.common_validation.failed(**kwargs)
            return -1

    def disable_ibeacon_service_in_network_policy(self, nw_policy, **kwargs):
        """
        - This keyword is used to disable Ibeacon Service in Network Policy
        - Flow: Configure --> Network Policy --> select the Policy -->Advance Settings-->IBeacon Services
        - Keyword Usage:
        - ``Disable IBeacon Service In Network Policy  ${POLICY_NAME}''

        :param nw_policy: name of the policy for disabling the iBeacon
        :return: None
        """

        self.navigator.navigate_to_devices()
        self.navigate_to_np_edit_tab(nw_policy)
        sleep(2)

        self.utils.print_info("Clicking on Additional Settings Tab")
        self.auto_actions.click_reference(self.np_web_elements.get_network_policy_additional_settings_tab)
        sleep(2)

        if self.np_web_elements.get_additional_settings_ibeacon_menu().is_displayed():
            self.utils.print_info("Click on iBeacon Service Menu button")
            self.auto_actions.click_reference(self.np_web_elements.get_additional_settings_ibeacon_menu)
            sleep(2)
        else:
            self.utils.print_info("Click Security Tab")
            self.auto_actions.click_reference(self.np_web_elements.get_policy_settings_menu)
            sleep(2)
            self.utils.print_info("Click on iBeacon Service Menu button")
            self.auto_actions.click_reference(self.np_web_elements.get_additional_settings_ibeacon_menu)
            sleep(2)

        sleep(5)
        self.utils.print_info("Click on Disable IBeacon service button")
        self.auto_actions.click_reference(self.np_web_elements.get_ibeacon_status_button)
        sleep(2)

        self.utils.print_info("Click on Save button")
        self.auto_actions.click_reference(self.np_web_elements.get_ibeacon_services_save_button)
        sleep(3)

        tool_tip_text = tool_tip.tool_tip_text
        self.utils.print_info("Tool tip Text Displayed on Page", tool_tip_text)
        if "iBeacon settings saved successfully" in tool_tip_text:
            kwargs['pass_msg'] = "iBeacon settings saved successfully"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Failed to disable ibeacon service"
            self.common_validation.failed(**kwargs)
            return -1

    def configure_access_security_pre_authentication_status(self, status, policy_name, ssid, **kwargs):
        """
        - configure Pre Authentication based on status for the wireless Network
        :param status: (str) status is either enable or disable
        :param policy_name: (str) Network Policy Name
        :param ssid: (str) SSID name
        :return: 1 if successfully changed the pre authentication status else -1
        """

        self.navigator.navigate_to_devices()
        self.navigate_wireless_ssid(policy_name, ssid)
        sleep(2)

        self.utils.print_info("click Additional settings button")
        self.auto_actions.click_reference(self.np_web_elements.get_ssid_authentication_additional_settings_option)
        sleep(2)

        self.utils.print_info("click Customize button")
        self.auto_actions.click_reference(self.np_web_elements.get_advance_access_security_customize_button)
        sleep(2)

        if status.upper() == "ENABLE":
            self.auto_actions.enable_check_box(
                self.np_web_elements.get_access_security_pre_authentication_checkbox())
            self.screen.save_screen_shot()
            sleep(2)

            self.utils.print_info("click on save button")
            self.auto_actions.click_reference(self.np_web_elements.get_access_security_settings_save_button)
            sleep(2)

        else:
            self.auto_actions.disable_check_box(
                self.np_web_elements.get_access_security_pre_authentication_checkbox())
            self.screen.save_screen_shot()
            sleep(2)

            self.utils.print_info("click on save button")
            self.auto_actions.click_reference(self.np_web_elements.get_access_security_settings_save_button)
            sleep(2)

        self.utils.print_info("Click on network policy SSID save button")
        self.auto_actions.click_reference(self.np_web_elements.get_np_ssid_save_button)

        tool_tip_text = tool_tip.tool_tip_text
        self.utils.print_info("Tool tip Text Displayed on Page", tool_tip_text)
        if "SSID was saved successfully." in tool_tip_text:
            kwargs['pass_msg'] = "SSID was saved successfully."
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Failed to configure access security pre authentication"
            self.common_validation.failed(**kwargs)
            return -1

    def edit_network_policy_ssid_authentication(self, policy_name, ssid_name, new_auth_method):
        """
        - This keyword will Change SSID Authentication to Open in the network policy
        - Flow: network policy -- > click on network policy card view --> click on SSID --> Edit SSID Authentication
        - Keyword Usage:
        - ``Edit Network Policy SSID Authentication   ${POLICY_NAME}   ${SSID_NAME}   ${NEW_AUTH_METHOD}``

        :param policy_name: Name of the network policy
        :param ssid_name: name of the ssid already exist on that network policy
        :param new_auth_method: Open SSID authentication
        :return: 1 if successfully changes SSID authentication to open
        """
        self.utils.print_info("Click on Network Policy card view button")
        self.navigator.navigate_to_network_policies_card_view_page()

        if self.select_network_policy_in_card_view(policy_name):
            if self._select_ssid(ssid_name):
                if new_auth_method.upper() == "OPEN":
                    self.auto_actions.click_reference(self.wireless_element.get_wireless_authtype_open)

        self.utils.print_info("Clicking on Network Save button..")
        self.auto_actions.click_reference(self.np_web_elements.get_network_policy_wireless_networks_save_button)

        return 1

    def create_switching_routing_network_policy(self, policy_name, **kwargs):
        """
        - Create Switching and Routing network policy
        - Checks the policy already exists, if it is not exist then create the network policy
        - Routing and Switching checkbox selected and wireless checkbox unselected while creating policy for EXOS
        - Keyword Usage:
        - ``Create Switching Routing Network Policy  ${POLICY_NAME}``

        :param policy_name: Policy Name
        :return: 1 if network policy created successfully else returns -1.
        """
        self.navigator.navigate_to_devices()
        if not self.navigator.navigate_to_network_policies_list_view_page() == 1:
            kwargs['fail_msg'] = "Failed to navigate to network policies list."
            self.common_validation.fault(**kwargs)
            return -1

        self.utils.print_info("Checking for network policy add button")
        if self.np_web_elements.check_np_add_button() == -2:
            kwargs['fail_msg'] = "Add button is not enabled for the user."
            self.common_validation.fault(**kwargs)
            return -1

        if self._search_network_policy_in_list_view(policy_name) == 1:
            kwargs['pass_msg'] = f"Network policy {policy_name} already exists in the network polices list"
            self.common_validation.passed(**kwargs)
            return 1

        self.utils.print_info("Click on network policy add button")
        self.auto_actions.click_reference(self.np_web_elements.get_np_add_button)
        sleep(2)

        self.utils.print_info("Unselect wireless network check box")
        self.auto_actions.disable_check_box(self.np_web_elements.get_np_wireless_check_box())
        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Enter the policy name:{}".format(policy_name))
        self.auto_actions.send_keys(self.np_web_elements.get_np_name_text(), policy_name)
        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Click on network policy save button")
        self.auto_actions.click_reference(self.np_web_elements.get_np_save_button)

        sleep(5)
        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)

        for tip_text in tool_tp_text:
            if "The Network Policy cannot be saved because" in tip_text:
                kwargs['pass_msg'] = f"The Network Policy cannot be saved because {tip_text}"
                self.common_validation.passed(**kwargs)
                return 1
            if "Your account does not have permission to perform that action" in tip_text:
                kwargs['fail_msg'] = f"Your account does not have permission to perform that action {tip_text}"
                self.common_validation.fault(**kwargs)
                return -1

            if "Unable to access data" in tip_text:
                kwargs['fail_msg'] = f"not able to save the network policy {tip_text}"
                self.common_validation.failed(**kwargs)
                return -1

        self.utils.print_info("Click on network policy exit button")
        self.auto_actions.click_reference(self.np_web_elements.get_np_exit_button)
        sleep(2)

        kwargs['pass_msg'] = "Network policy created successfully"
        self.common_validation.passed(**kwargs)
        return 1

    def edit_network_policy_type(self, nw_policy, options_params, **kwargs):
        """
        - This keyword is used to select the type of policy option we are creating, i.e.., Routing, switching, wireless
        - Flow: Configure --> Network Policy --> select the Policy -->enable/disable different policy type options above
        - Keyword Usage:
        - ``Edit Network Policy Type  ${POLICY_NAME}   ${OPTION_PARAMS}``

        :param nw_policy: name of the policy
        :param options_params: wireless=enable,switches=disable,routing=enable
        :return: 1 or -1
        """
        self.navigator.navigate_to_devices()
        self.navigate_to_np_edit_tab(nw_policy)
        sleep(2)

        option_list = options_params.split(",")
        option_dict = {}
        for val in option_list:
            option_dict[val.split("=")[0]] = val.split("=")[1]

        if option_dict["wireless"] == 'enable':
            self.utils.print_info(" Enabling Wireless : " + str(option_dict["wireless"]))
            self.auto_actions.enable_check_box(self.np_web_elements.get_np_wireless_check_box())

        if option_dict["wireless"] == 'disable':
            self.utils.print_info(" Disable Wireless : " + str(option_dict["wireless"]))
            self.auto_actions.disable_check_box(self.np_web_elements.get_np_wireless_check_box())

        if option_dict["switches"] == 'enable':
            self.utils.print_info(" Enabling Switches : " + str(option_dict["switches"]))
            self.auto_actions.enable_check_box(self.np_web_elements.get_np_switches_check_box())

        if option_dict["switches"] == 'disable':
            self.utils.print_info(" Disable Switches : " + str(option_dict["switches"]))
            self.auto_actions.disable_check_box(self.np_web_elements.get_np_switches_check_box())

        if option_dict["routing"] == 'enable':
            self.utils.print_info(" Enabling Routing : " + str(option_dict["routing"]))
            self.auto_actions.enable_check_box(self.np_web_elements.get_np_routing_check_box())

        if option_dict["routing"] == 'disable':
            self.utils.print_info(" Disable Routing : " + str(option_dict["routing"]))
            self.auto_actions.disable_check_box(self.np_web_elements.get_np_routing_check_box())

        sleep(2)
        self.utils.print_info("Click on network policy save button")
        self.auto_actions.click_reference(self.np_web_elements.get_np_save_button)

        self.utils.print_info("Checking the Save profile message...")
        observed_nwpolicy_message = self.np_web_elements.get_np_save_tool_tip().text
        self.utils.print_info("Observed Message: ", observed_nwpolicy_message)

        if "Network Policy was saved successfully" in observed_nwpolicy_message:
            kwargs['pass_msg'] = "Network Policy was saved successfully"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Failed to edit network policy"
            self.common_validation.failed(**kwargs)
            return -1

    def deploy_stack_network_policy(self, device_mac, policy_name, sw_template_name, firmwareUpdate=False, **kwargs):
        """
        - Deploy the network policy to the particular device
        - By default it will do delta config push
        - If want to perform different type of config push, pass the appropriate parameter values
        - If already in network policy then deploy the policy else navigate to network policy--> deploy policy tab
        - Keyword Usage:
        - ``Deploy Network Policy     ${DEVICE_MAC}  ${POLICY_NAME} ${Switch_template}


        :param policy_name: Name of the policy
        :param device_mac : The device mac
        :param sw_template_name: Config update type. By default it is complete
        :return: 1 if successfully updated ; else -1
        """
        if self.np_web_elements.get_np_policy_crumb_button():
            self.utils.print_info("Inside Network Policy...")
        else:
            self.utils.print_info("Not inside Network Policy. Navigating...")
            self.navigate_to_np_edit_tab(policy_name)
        sleep(2)

        self.utils.print_info("Click on deploy policy tab")
        self.auto_actions.click_reference(self.np_web_elements.get_deploy_policy_tab)
        sleep(2)

        def _click_eligible():
            self.utils.print_info("Click on eligible device button")
            self.auto_actions.click_reference(self.np_web_elements.get_eligible_device_button)
        _click_eligible()

        def _check_device_rows():
            return self._get_device_rows(device_mac)
        self.utils.wait_till(_check_device_rows, delay=0.2, is_logging_enabled=True, silent_failure=False)

        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)
        for tip_text in tool_tp_text:
            if "An unknown error has" in tip_text:
                kwargs['fail_msg'] = f"{tip_text} occurred while assigning nw policy"
                self.common_validation.fault(**kwargs)
                return -1

        if not self._select_device_row(device_mac):
            kwargs['fail_msg'] = "Device is not available in the deploy policy page"
            self.common_validation.fault(**kwargs)
            return -1

        self.screen.save_screen_shot()
        sleep(1)
        self.utils.print_info("Click on the policy deploy upload button")
        self.auto_actions.click_reference(self.np_web_elements.get_deploy_policy_upload_button)
        sleep(1)
        self.screen.save_screen_shot()

        # Select from dropdown
        if sw_template_name is not None:
            sleep(10)
            click_dropdown = self.devices_web_elements.get_devices_stack_update_policy_dropdown_btn()
            if click_dropdown:
                self.utils.print_info(" Click on dropdown ")
                self.auto_actions.click(click_dropdown)
            else:
                self.utils.print_info(" Not able to find dropdown  ")
            dropdown_items = self.devices_web_elements.get_devices_stack_update_policy_dropdown_items()
            if dropdown_items:
                self.utils.print_info(" The templates from dropdown are: ")
                for elem in dropdown_items:
                    self.utils.print_info(elem.text)
                for el in dropdown_items:
                    if sw_template_name in el.text:
                        self.utils.print_info(f" Select {el.text} from dropdown")
                        self.auto_actions.select_drop_down_options(dropdown_items, el.text)
                        break
                    else:
                        self.utils.print_info(" The template name was not found in dropdown")
            else:
                self.utils.print_info(" Not able to find dropdown items ")
        else:
            self.utils.print_info(" The sw_template_name is None  ")

        uptd = self.devices_web_elements.get_devices_switch_update_network_policy()

        if not uptd.is_selected():
            self.utils.print_info("Click on the update configuration checkbox")
            self.auto_actions.click(uptd)

        # Uncheck the firmware update checkbox if it is checked
        firmware_update = self.devices_web_elements.get_upgrade_IQ_engine_and_extreme_network_switch_images_checkbox()
        if not firmwareUpdate:
            if firmware_update.is_selected():
                self.utils.print_info("Upgrade IQ engine and extreme network switch images checkbox is checked - Unchecking")
                self.auto_actions.click(firmware_update)
            else:
                self.utils.print_info("Upgrade IQ engine and extreme network switch images checkbox is already unchecked")
        else:
            if firmware_update.is_selected():
                self.utils.print_info("Upgrade IQ engine and extreme network switch images checkbox is already checked")
            else:
                self.utils.print_info("Upgrade IQ engine and extreme network switch images checkbox is not checked - Checking")
                self.auto_actions.click(firmware_update)

        # Perform the update
        self.screen.save_screen_shot()
        sleep(5)

        # Captute tool tip msg before pressing the perform update button
        tool_tp_text_before = tool_tip.tool_tip_text.copy()
        self.utils.print_info(tool_tp_text_before)

        # Press perform update button
        self.utils.print_info("Checking for the perform update button presence")
        if self.np_web_elements.get_perform_update_policy_button():
            self.utils.print_info("Click on perform update button ")
            self.auto_actions.click_reference(self.np_web_elements.get_perform_update_policy_button)
        else:
            kwargs['fail_msg'] = "The perform update button was not found"
            self.common_validation.fault(**kwargs)
            return -1

        self.screen.save_screen_shot()
        sleep(5)

        # Capture the tool tip after pressing the perform update button
        tool_tp_text_after = tool_tip.tool_tip_text.copy()
        self.utils.print_info(tool_tp_text_after)

        # Print and return the displayed tool tip msg if any
        for item_after in tool_tp_text_after:
            if item_after in tool_tp_text_before:
                pass
            else:
                self.utils.print_info("Below message is displayed after pressing the perform update button")
                self.utils.print_info(item_after)
                return item_after
        return 1

    def select_ssid_in_policy(self, policy, ssid, **kwargs):
        """
        - Selects existing SSID in the policy
        - Keyword Usage:
        - ``Select SSID In Policy     ${POLICY}  ${SSID} ``
        :param policy: Name of the policy
        :param ssid : SSID to select
        :return: True if selection is success else False
        """
        self.utils.print_info("Selecting policy  " + str(policy))
        self.auto_actions.scroll_up()
        self.navigate_to_np_edit_tab(policy)

        self.utils.print_info("Clicking on the wireless network tab")
        self.auto_actions.click_reference(self.wireless_element.get_wireless_networks_tab)

        self.utils.print_info("Clicking on the Select option to select SSID")
        self.auto_actions.click_reference(self.wireless_element.get_wireless_ssid_select_button)
        sleep(2)
        self.screen.save_screen_shot()

        for row in self.wireless_element.get_wireless_ssid_select_window_rows():
            if ssid.upper() == row.text.upper():
                self.utils.print_info(f"Selecting the SSID: {ssid}")
                self.auto_actions.move_to_element(self.wireless_element.
                                                  get_wireless_select_ssid_row_check_box(row))
                self.auto_actions.click(self.wireless_element.get_wireless_select_ssid_row_check_box(row))
                sleep(2)
                self.auto_actions.click_reference(self.wireless_element.get_wireless_ssid_select_option_button)
                self.screen.save_screen_shot()
                kwargs['pass_msg'] = "Selected SSID in policy"
                self.common_validation.passed(**kwargs)
                return True

        self.auto_actions.click_reference(self.wireless_element.get_wireless_ssid_select_cancel_button)
        kwargs['fail_msg'] = f"SSID: {ssid} not present"
        self.common_validation.failed(**kwargs)
        return False

    def enable_classifier_maps(self, nw_policy, classifier_name, **kwargs):
        """
        - This keyword is used to enable Classifier Maps which Maps anonymous incoming traffic into the Extreme Networks classification system.
        - Flow: Configure --> Network Policy --> select the Policy -->Advance Settings-->QoS Options --> Classifier Maps
        - Keyword Usage:
        -``Enable Classifier Maps   ${AP_NETWORK_POLICY}  ${classifier_name}''
        :param nw_policy: name of the policy for enabling the Marker Maps
        :param classifier_name: Name and description for classier map settings
        :return: 1 if successfully updated ; else -1
        """
        self.navigator.navigate_to_devices()
        self.navigate_to_np_edit_tab(nw_policy)
        sleep(2)

        self.utils.print_info("Clicking on Additional Settings Tab")
        self.auto_actions.click_reference(self.np_web_elements.get_network_policy_additional_settings_tab)
        sleep(2)

        self.np_web_elements.get_additional_settings_classifiermaps().is_displayed()

        self.utils.print_info("Scroll to the Classifier Maps Option")
        self.auto_actions.click_reference(self.np_web_elements.get_additional_settings_classifiermaps)
        sleep(2)
        self.utils.print_info("Click on Classifier Maps")
        self.auto_actions.click_reference(self.np_web_elements.get_additional_settings_classifiermaps)
        sleep(2)

        self.utils.print_info("Enable Classifier Maps")
        self.auto_actions.click_reference(self.np_web_elements.get_classifiermaps_enable)
        sleep(3)

        self.utils.print_info("Enter Classifier Maps Name")
        self.auto_actions.send_keys(self.np_web_elements.get_classifiermaps_name(), classifier_name)
        sleep(3)

        self.utils.print_info("Enter Classifier Maps Description")
        self.auto_actions.send_keys(self.np_web_elements.get_classifiermaps_description(), classifier_name)
        sleep(3)

        self.utils.print_info("Add Service")
        self.auto_actions.click_reference(self.np_web_elements.get_classifiermaps_add_button)
        sleep(3)

        self.utils.print_info("Select from the following link")
        self.auto_actions.click_reference(self.np_web_elements.get_classifiermaps_services_selectfromfollowing_link)
        sleep(3)

        self.utils.print_info("Select BGP Service")
        self.auto_actions.click_reference(self.np_web_elements.get_classifiermaps_services_select_service_bgp)
        sleep(3)

        self.utils.print_info("Save BGP Service")
        self.auto_actions.click_reference(self.np_web_elements.get_classifiermaps_services_initial_save_button)
        sleep(3)

        self.utils.print_info("Click on Save Services Button")
        self.auto_actions.click_reference(self.np_web_elements.get_classifiermaps_services_save_button)
        sleep(3)

        self.utils.print_info("Click on MAC OUIs")
        self.auto_actions.click_reference(self.np_web_elements.get_classifiermaps_macoui_link)
        sleep(3)

        self.utils.print_info("Click on Add")
        self.auto_actions.click_reference(self.np_web_elements.get_classifiermaps_macoui_add)
        sleep(3)

        self.utils.print_info("Click on DropDown Menu")
        self.auto_actions.click_reference(self.np_web_elements.get_classifiermaps_macoui_dropdown)
        sleep(3)

        self.utils.print_info("Click Aerohive-08EA44")
        self.auto_actions.click_reference(self.np_web_elements.get_classifiermaps_add_macoui_from_dropdown)
        sleep(3)

        self.utils.print_info("Click on Save Button")
        self.auto_actions.click_reference(self.np_web_elements.get_classifiermaps_macoui_save_button)
        sleep(3)

        self.utils.print_info("Click on SSID")
        self.auto_actions.click_reference(self.np_web_elements.get_classifiermaps_ssid_link)
        sleep(3)

        self.utils.print_info("Add SSID")
        self.auto_actions.click_reference(self.np_web_elements.get_classifiermaps_add_ssid)
        sleep(3)

        self.utils.print_info("Click on Save Button")
        self.auto_actions.click_reference(self.np_web_elements.get_classifiermaps_ssid_save_button)
        sleep(3)

        self.utils.print_info("Click on 802.1p/DiffServ/802.11e")
        self.auto_actions.click_reference(self.np_web_elements.get_classifiermaps_802_link)
        sleep(3)

        self.utils.print_info("Enable 802.1p")
        self.auto_actions.click_reference(self.np_web_elements.get_classifiermaps_802enable)
        sleep(3)

        self.utils.print_info("Enable DiffServ")
        self.auto_actions.click_reference(self.np_web_elements.get_classifiermaps_diffservenable)
        sleep(3)

        self.utils.print_info("Enable 802.11e")
        self.auto_actions.click_reference(self.np_web_elements.get_classifiermaps_80211enable)
        sleep(3)

        self.utils.print_info("Click on Save button")
        self.auto_actions.click_reference(self.np_web_elements.get_Classifier_Maps_save_button)
        sleep(3)

        tool_tip_text = tool_tip.tool_tip_text
        self.utils.print_info("Tool tip Text Displayed on Page", tool_tip_text)
        if "Classifier Maps Additional Settings saved successfully" in tool_tip_text:
            kwargs['pass_msg'] = "Classifier Maps Additional Settings saved successfully"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "enable_classifier_maps() failed"
            self.common_validation.failed(**kwargs)
            return -1

    def enable_marker_maps(self, nw_policy, MarkerMap_dict, **kwargs):
        """
        - This keyword is used to enable Marker Maps which Marks the outgoing or upstream traffic with the specified traffic priority markers.
        - Flow: Configure --> Network Policy --> select the Policy -->Advance Settings-->QoS Options --> Marker Maps
        - Keyword Usage:
        -``Enable Marker Maps   ${AP_NETWORK_POLICY}  &{MarkerMap_dict}''
        :param nw_policy: name of the policy for enabling the Marker Maps
        :param MarkerMap_dict: A dictionary that will contains all values required for Marker Maps Configuration
        Marker Values for 802.1p : NC_8021P, CL_8021P, E_8021P, BF2_8021P
        Marker Values for diffServ : NC_diffServ, Voice_diffServ, Video_diffServ, BG_diffServ
        :return: 1 if successfully updated ; else -1
        """
        marker_name = MarkerMap_dict.get('marker_name')
        NC_8021P = MarkerMap_dict.get('NC_8021P')
        CL_8021P = MarkerMap_dict.get('CL_8021P')
        E_8021P = MarkerMap_dict.get('CL_8021P')
        BF2_8021P = MarkerMap_dict.get('BF2_8021P')
        NC_diffServ = MarkerMap_dict.get('NC_diffServ')
        Voice_diffServ = MarkerMap_dict.get('Voice_diffServ')
        Video_diffServ = MarkerMap_dict.get('CL_8021P')
        BG_diffServ = MarkerMap_dict.get('BG_diffServ')

        self.navigator.navigate_to_devices()
        self.navigate_to_np_edit_tab(nw_policy)
        sleep(2)

        self.utils.print_info("Clicking on Additional Settings Tab")
        self.auto_actions.click_reference(self.np_web_elements.get_network_policy_additional_settings_tab)
        sleep(2)

        self.np_web_elements.get_additional_settings_marker_maps().is_displayed()

        self.utils.print_info("Scroll to the Marker Maps Option")
        self.auto_actions.click_reference(self.np_web_elements.get_additional_settings_marker_maps)
        sleep(2)

        self.utils.print_info("Click on Marker Maps")
        self.auto_actions.click_reference(self.np_web_elements.get_additional_settings_marker_maps)
        sleep(2)

        self.utils.print_info("Enable Marker Maps")
        self.auto_actions.click_reference(self.np_web_elements.get_marker_maps_status_button)
        sleep(3)

        self.utils.print_info("Enter Marker Maps Name")
        self.auto_actions.send_keys(self.np_web_elements.get_marker_maps_name_textfield(), marker_name)
        sleep(3)

        self.utils.print_info("Enter Marker Maps Description")
        self.auto_actions.send_keys(self.np_web_elements.get_marker_maps_description(), marker_name)
        sleep(3)

        self.utils.print_info("Enable 802.1p Markers")
        self.auto_actions.click_reference(self.np_web_elements.get_marker_maps_8021P)
        sleep(3)

        self.utils.print_info("Enter 802.1p Network Control")
        self.auto_actions.send_keys(self.np_web_elements.get_marker_maps_NetworkControl_textfield(), NC_8021P)
        sleep(3)

        self.utils.print_info("Enter 802.1p Controlled Load")
        self.auto_actions.send_keys(self.np_web_elements.get_marker_maps_ControlledLoad_textfield(), CL_8021P)
        sleep(3)

        self.utils.print_info("Enter 802.1p Excellent Effort")
        self.auto_actions.send_keys(self.np_web_elements.get_marker_maps_Excellent_Effort_textfield(), E_8021P)
        sleep(3)

        self.utils.print_info("Enter 802.1p Best Effort 2")
        self.auto_actions.send_keys(self.np_web_elements.get_marker_maps_Best_Effort2_textfield(), BF2_8021P)
        sleep(3)

        self.utils.print_info("Switch to diffServ Markers")
        self.auto_actions.click_reference(self.np_web_elements.get_marker_maps_Switch_to_diffServ)
        sleep(3)

        self.utils.print_info("Enable diffServ Markers")
        self.auto_actions.click_reference(self.np_web_elements.get_marker_maps_diffServ)
        sleep(3)

        self.utils.print_info("Enter diffServ Network Control")
        self.auto_actions.send_keys(self.np_web_elements.get_marker_maps_NC_diffServ_textfield(), NC_diffServ)
        sleep(3)

        self.utils.print_info("Enter diffServ Voice")
        self.auto_actions.send_keys(self.np_web_elements.get_marker_maps_Voice_diffServ_textfield(), Voice_diffServ)
        sleep(3)

        self.utils.print_info("Enter diffServ Video")
        self.auto_actions.send_keys(self.np_web_elements.get_marker_maps_Video_diffServ_textfield(), Video_diffServ)
        sleep(3)

        self.utils.print_info("Enter diffServ Background")
        self.auto_actions.send_keys(self.np_web_elements.get_marker_maps_BG_diffServ_textfield(), BG_diffServ)
        sleep(3)

        self.utils.print_info("Click on Save button")
        self.auto_actions.click_reference(self.np_web_elements.get_marker_maps_services_save_button)
        sleep(3)

        tool_tip_text = tool_tip.tool_tip_text
        self.utils.print_info("Tool tip Text Displayed on Page", tool_tip_text)
        if "Marker Maps Settings saved successfully" in tool_tip_text:
            kwargs['pass_msg'] = "Marker Maps Settings saved successfully"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "enable_marker_maps() failed."
            self.common_validation.failed(**kwargs)
            return -1

    def enable_QoS_Overview_DAS(self, nw_policy, **kwargs):
        """
        - This keyword is used to enable Marker Maps which Marks the outgoing or upstream traffic with the specified traffic priority markers.
        - Flow: Configure --> Network Policy --> select the Policy -->Advance Settings-->QoS Options --> QoS Overview --> DAS
        - Keyword Usage:
        -``Enable QoS Overview DAS  ${POLICY_NAME} ''
        :param nw_policy: name of the policy for enabling the Marker Maps
        :return: 1 if successfully updated ; else -1
        """
        self.navigator.navigate_to_devices()
        self.navigate_to_np_edit_tab(nw_policy)
        sleep(2)

        self.utils.print_info("Clicking on Additional Settings Tab")
        self.auto_actions.click_reference(self.np_web_elements.get_network_policy_additional_settings_tab)
        sleep(2)

        if self.np_web_elements.get_additional_settings_marker_maps().is_displayed():
            self.utils.print_info("Scroll to the QoS Overview Option")
            self.auto_actions.click_reference(self.np_web_elements.get_additional_settings_QoS_Overview)
            sleep(2)
        else:
            self.utils.print_info("Click Security Tab")
            self.auto_actions.click_reference(self.np_web_elements.get_qos_options_menu)
            sleep(2)
            self.utils.print_info("Click on QoS Overview")
            self.auto_actions.click_reference(self.np_web_elements.get_additional_settings_QoS_Overview)
            sleep(2)

        self.utils.print_info("Enable Dynamic Airtime Scheduling")
        self.auto_actions.click_reference(self.np_web_elements.get_QoS_Dynamic_Airtime_Scheduling_Enable)
        sleep(2)

        self.utils.print_info("Click on Save button")
        self.auto_actions.click_reference(self.np_web_elements.get_QoS_services_save_button)

        tool_tip_text = tool_tip.tool_tip_text
        self.utils.print_info("Tool tip Text Displayed on Page", tool_tip_text)
        if "QoS Overview Settings are saved successfully" in tool_tip_text:
            kwargs['pass_msg'] = "QoS Overview Settings are saved successfully"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "enable_QoS_Overview_DAS() failed."
            self.common_validation.failed(**kwargs)
            return -1

    def create_owe_ssid(self, nw_policy, ssid, WiFi2, **kwargs):
        """
        - This keyword is ONLY used for OWE SSID testing purposes.
        - Flow: Configure --> Network Policy --> select the Policy -->Wireless Setings -->Add SSID
        - Keyword Usage:
        - ''Create OWE SSID  ${POLICY_NAME}  ${SSID}   WiFi2=enable ''
        - ''Create OWE SSID  ${POLICY_NAME}  ${SSID}   WiFi2=disable ''

        :param nw_policy: name of the policy
        :param SSID: Enter SSID
        :param WiFi2=enable : Enable WiFi2 checkbox
        :param WiFi2=disable : Disable WiFi2 Checkbox
        :return: 1 if OWE SSID is saved and configured successfully; else -1
        """

        self.utils.print_info("Selecting policy  " + str(nw_policy))
        self.navigate_to_np_edit_tab(nw_policy)

        self.utils.print_info("Clicking on the wireless network tab")
        self.auto_actions.click_reference(self.wireless_element.get_wireless_networks_tab)

        self.utils.print_info("Click on Add SSID")
        self.auto_actions.click_reference(self.np_web_elements.get_add_ssid_menu)
        sleep(2)

        self.utils.print_info("Enter SSID")
        self.auto_actions.send_keys(self.np_web_elements.get_wireless_networks_ssid_textfield(), ssid)
        sleep(2)

        if WiFi2 == 'enable':
            self.utils.print_info("Enabling WiFi2 Checkbox")
            self.auto_actions.enable_check_box(self.np_web_elements.get_OWE_wifi2_checkbox())
            sleep(2)

            self.utils.print_info("Clicking 'Yes'")
            self.auto_actions.click_reference(self.np_web_elements.get_OWE_wifi2_dialogue_box_yes)
            sleep(2)

            self.utils.print_info("Click on Enhanced Open Secure SSID Authentication")
            self.auto_actions.click_reference(self.np_web_elements.get_Enhanced_Open_Authentication)
            sleep(3)

            self.utils.print_info("Click on Save Button")
            self.auto_actions.click_reference(self.np_web_elements.get_save_enhanced_open_ssid)
            sleep(3)
            kwargs['pass_msg'] = "OWE SSID is saved and configured successfully"
            self.common_validation.passed(**kwargs)
            return 1

        elif WiFi2 == 'disable':
            self.utils.print_info("Disabling WiFi2 Checkbox")
            self.auto_actions.disable_check_box(self.np_web_elements.get_OWE_wifi2_checkbox())
            sleep(2)

            self.utils.print_info("Click on Enhanced Open Secure SSID Authentication")
            self.auto_actions.click_reference(self.np_web_elements.get_Enhanced_Open_Authentication)
            sleep(10)

            self.utils.print_info("Enable Transition Mode for 2.4Ghz and 5Ghz")
            self.auto_actions.click_reference(self.np_web_elements.get_OWE_Transition_mode)

            self.utils.print_info("Click on Save Button")
            self.auto_actions.click_reference(self.np_web_elements.get_save_enhanced_open_ssid)
            sleep(3)
            kwargs['pass_msg'] = "OWE SSID is saved and configured successfully"
            self.common_validation.passed(**kwargs)
            return 1

        else:
            kwargs['fail_msg'] = "Failed to configure OWE SSID"
            self.common_validation.failed(**kwargs)
            return -1

    def create_ssid_to_policy(self, nw_policy, **wireless_profile):
        """
        - This keyword will create extra new ssid and add to exist policy.
        - Wireless network includes open, ppsk, psk, enhanced, and enterprise network
        - Flow: Configure --> Network Policies --> select exist Policy --> select Wireless Networks tab --> Add(+) SSID
        - Keyword Usage:
        - ''Create SSID to Policy   ${SSID}   ${POLICY_NAME}   &{WIRELESS_NW_PROFILE}``
        - &{WIRELESS_NW_PROFILE} --> This is dictionary, include all key value pair to create wireless network
        - Fof Creating  &{WIRELESS_NW_PROFILE} dict refer wireless_network_config.robot

        :param nw_policy: name of exist policy
        :param SSID: extra new SSID to create
        :param wireless_profile: (dict) wireless network creation profile parameters
        :return: 1 if ssid creation and addition is success, otherwise -1
        """
        self.navigator.navigate_to_devices()
        self.utils.print_info("Selecting exist policy  " + str(nw_policy))
        self.navigate_to_np_edit_tab(nw_policy)

        return self.wireless_nw.create_wireless_network(**wireless_profile)

    def enable_mgmt_option_http_redirect(self, nw_policy, mgmt_option_name, **kwargs):
        """
        - This keyword is used to enable HTTP Redirect under enable Management Options.
        - Flow: Configure --> Network Policy --> edit the Policy --> Additional Settings --> Management Options > Http Redirect
        - Keyword Usage:
        -``Enable Mgmt Option Http Redirect  ${POLICY_NAME}   ${MGMT_OPTION_NAME}''
        :param nw_policy: name of the policy
        :param mgmt_option_name: name of the management option
        :return: 1 if successfully updated ; else -1
        """

        self.navigator.navigate_to_devices()
        self.navigate_to_np_edit_tab(nw_policy)
        sleep(2)

        self.utils.print_info("Clicking on Additional Settings Tab")
        self.auto_actions.click_reference(self.np_web_elements.get_network_policy_additional_settings_tab)
        sleep(2)

        self.utils.print_info("Clicking on Management Options")
        self.auto_actions.click_reference(self.np_web_elements.get_network_policy_management_options)
        sleep(5)

        self.utils.print_info("Enabling Management Option")
        self.auto_actions.click_reference(self.np_web_elements.enable_management_options_button)
        sleep(2)

        self.utils.print_info("Entering the name of Management Option")
        self.auto_actions.send_keys(self.np_web_elements.management_option_name_textfield(), mgmt_option_name)
        sleep(2)

        self.utils.print_info("Enabling HTTP Re-direct Option")
        self.auto_actions.click_reference(self.np_web_elements.enable_legacy_http_redirect_checkbox)
        sleep(5)

        self.utils.print_info("Saving Management Option")
        self.auto_actions.click_reference(self.np_web_elements.save_management_option_button)
        sleep(2)

        tool_tip_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tip_text)

        if "Managements options were saved successfully." in tool_tip_text:
            kwargs['pass_msg'] = "Managements options were saved successfully."
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "enable_mgmt_option_http_redirect() failed"
            self.common_validation.failed(**kwargs)
            return -1

    def select_network_policy_management_option(self, nw_policy, mgmt_option_name, **kwargs):
        """
        - This keyword is used to select a Management Options under a Network Policy.
        - Flow: Configure --> Network Policy --> edit the Policy --> Additional Settings --> Management Options
        - Keyword Usage:
        -``Select Network Policy Management Option  ${POLICY_NAME}   ${MGMT_OPTION_NAME}''
        :param nw_policy: name of the policy
        :param mgmt_option_name: name of the management option
        :return: 1 if successfully updated ; else -1
        """

        self.navigator.navigate_to_devices()
        self.navigate_to_np_edit_tab(nw_policy)
        sleep(2)

        self.utils.print_info("Clicking on Additional Settings Tab")
        self.auto_actions.click_reference(self.np_web_elements.get_network_policy_additional_settings_tab)
        sleep(2)

        self.utils.print_info("Clicking on Management Options")
        self.auto_actions.click_reference(self.np_web_elements.get_network_policy_management_options)
        sleep(5)
        self.auto_actions.scroll_up()
        sleep(10)

        self.utils.print_info("Clicking on management options on/off button")
        on_off_button = self.np_web_elements.get_management_option_on_off_button()
        if on_off_button:
            self.auto_actions.click(on_off_button)
            self.utils.print_info("Clicking on Re-Use Management Options button")
            re_use_button = self.np_web_elements.get_re_use_management_options_setting_button()
            if re_use_button:
                self.auto_actions.click(re_use_button)
                sleep(5)
                self.utils.print_info("Gathering all the Management Options")
                all_table_rows = self.np_web_elements.get_table_management_options_rows()
                if all_table_rows:
                    for row in all_table_rows:
                        self.utils.print_info("row text: ", row.text)
                        if row.text == mgmt_option_name:
                            self.utils.print_info("Selecting row " + row.text + "...")
                            row_check = (self.np_web_elements.get_table_management_options_row_checkbox(row))[0]
                            if row_check:
                                self.auto_actions.click(row_check)
                                self.utils.print_info("Clicking on Select button...")
                                select_button = self.np_web_elements.get_management_options_select_button()
                                if select_button:
                                    self.auto_actions.click(select_button)
                                    self.utils.print_info("Save changes to policy ")
                                    self.auto_actions.click_reference(self.np_web_elements.save_management_option_button)
                                    kwargs['pass_msg'] = "Select network policy option"
                                    self.common_validation.passed(**kwargs)
                                    return 1
                                else:
                                    kwargs['fail_msg'] = "Unable to click on the Select button"
                                    self.common_validation.fault(**kwargs)
                                    return -1
                            else:
                                kwargs['fail_msg'] = f"Unable to select row {row.text}"
                                self.common_validation.fault(**kwargs)
                                return -1
                else:
                    kwargs['fail_msg'] = "Unable to locate gather the Management Options"
                    self.common_validation.fault(**kwargs)
                    return -1
            else:
                kwargs['fail_msg'] = "Unable to locate Re-Use Management Options button"
                self.common_validation.fault(**kwargs)
                return -1
        else:
            kwargs['fail_msg'] = "Unable to locate management options on/off button"
            self.common_validation.fault(**kwargs)
            return -1

    def add_user_group_to_network_policy_ssid(self, policy_name, ssid_name, auth_profile, **kwargs):
        """
        - This keyword will add user group to the SSID which have user group item in a Network Policy
        - Flow: network policy -- > click on network policy card view --> click on SSID --> Add user group
        - Keyword Usage:
        - ``Add User Group To Network Policy Ssid   ${POLICY_NAME}   ${SSID_NAME}   &{AUTH_PROFILE}``

        :param policy_name: Name of the network policy
        :param ssid_name: name of the ssid already exist on that network policy
        :param auth_profile: PPSK or 8021x auth profile in file ../CFD/Resource/wireless_networks_related_config.robot
        :return: 1 if successfully else -1
        """
        user_group_config = auth_profile.get('user_group_config', 'None')
        self.utils.print_info(f"The user group configuration: {user_group_config}")
        self.utils.print_info("Click on Network Policy card view button")
        self.navigator.navigate_to_network_policies_card_view_page()

        if self.select_network_policy_in_card_view(policy_name):
            if self._select_ssid(ssid_name):
                self.utils.print_info("Check if there is User Group item...")
                if self.user_group_elements.get_ssid_user_group_item():
                    self.utils.print_info("Select the user group")
                    if not user_group_config == 'None':
                        usr_group_name = user_group_config.get('group_name')
                        group_profile = user_group_config.get('user_group_profile')
                        if not group_profile == 'None':
                            self.user_group.add_wireless_nw_user_group(usr_group_name, group_profile)
                        else:
                            db_loc = user_group_config.get('db_loc')
                            if not self.user_group.select_wireless_user_group(usr_group_name, db_loc, 'PPSK'):
                                kwargs['fail_msg'] = "add_user_group_to_network_policy_ssid() failed. " \
                                                           f"User group:{usr_group_name} not created !"
                                self.common_validation.failed(**kwargs)
                                return -1
                else:
                    kwargs['fail_msg'] = "No User Group item found in the SSID."
                    self.common_validation.failed(**kwargs)
                    return -1

        self.utils.print_info("Clicking on Network Save button..")
        self.auto_actions.click_reference(self.np_web_elements.get_network_policy_wireless_networks_save_button)

        return 1
    # This is not a real keyword, it only clicks on an element. Let it comment as I do not know who else is using it.
    # def get_switching_tab(self):
    #     self.auto_actions.click_reference(self.np_web_elements.get_switching_tab)

    def check_port_types_section(self, **kwargs):
        """
        - This keyword will navigate to Port Types section in Network Policies tab
        - Assumption: Already Opened Network Policy
        - Flow: Switching tab --> Click on Port Types
        - Keyword Usage:

        :return: 1 if successfully else -1
        """
        # this sleep is necessary for allowing the page to load before performing any action
        time.sleep(1)
        self.auto_actions.click_reference(self.np_web_elements.get_port_types_section)
        self.navigator.wait_until_loading_is_done()
        self.screen.save_screen_shot()
        title = self.np_web_elements.get_port_types_title_page()
        title_text = title.text
        if 'Port Types' in title_text:
            kwargs['pass_msg'] = "Port types section displayed"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Port types section not found on page"
            self.common_validation.fault(**kwargs)
            return -1

    def configure_port_type(self, port_type_name, path_cost=None, description=None, status=None,
                                       port_usage="access", priority=None, bpdu_protection=None, stp_enabled=None,
                                       edge_port=None, save=True, **kwargs):
        """
        - This keyword will configures/edits a new port Type section using the Port Types section in Network Policies tab
        - Assumption: Already Opened Port type Configuration window
        - Flow: Switching tab --> Click on Port Types
        The only mandatory arguments are switch_port, port_type_name. All the other arguments are optional.

        The function will return a tuple that contains the status of the function and the summary of the newly created port type.

        args:
            :switch_port:        str  - the name of the port
            :port_type_name:     str  - the name of the port type

        kwargs:
            :description:        str  - the description|None for no action
            :status:             bool - True for enabled|False for disabled|None for no action
            :port_usage:         str  - "access"|"trunk"|None for no action
            :priority:           int  - 0, 16, 32, ...|None for no action
            :bpdu_protection:    str  - "Disabled"|"Guard"|None for no action
            :stp_enabled:        bool - True for enabled|False for disabled|None for no action
            :edge_port:          bool - True for enabled|False for disabled|None for no action
            :save:               bool - True for saving the port type at the end|False for not saving
            :path_cost:          int  - the value of path cost

        return: if the function succeeds it will return (1, {...})
                if the function fails it will return (-1, {})

        usage:

            status, summary = self.xiq.xflowsconfigureNetworkPolicy.create_new_port_type("VOSS", testing_port_type_1",
            1111, description="description", status=True, port_usage="access", priority=64, bpdu_protection="Disabled",
             stp_enabled=True, edge_port=True)
            status           1
            summary            {'STP': 'Enabled', 'Edge Port': 'Enabled', 'BPDU Protection': 'Disabled', 'Priority': '64', 'Path Cost': '1111'}
        """

        name_element = self.dev360.get_select_element_port_type("name")
        if not name_element:
            kwargs['fail_msg'] = "Port name element was not found"
            self.common_validation.fault(**kwargs)
            return -1, {}

        if self.auto_actions.send_keys(name_element, port_type_name) == 1:
            kwargs['pass_msg'] = "Successfully configured the name field"
            self.common_validation.passed(**kwargs)
            sleep(2)
        else:
            kwargs['fail_msg'] = "Failed to configure the name field"
            self.common_validation.fault(**kwargs)
            return -1, {}

        if description is not None:
            description_element = self.dev360.get_select_element_port_type("description")
            if not description_element:
                kwargs['fail_msg'] = "Port description element was not found"
                self.common_validation.fault(**kwargs)
                return -1, {}

            if self.auto_actions.send_keys(description_element, description) == 1:
                kwargs['pass_msg'] = "Successfully configured the description field"
                self.common_validation.passed(**kwargs)
                sleep(2)
            else:
                kwargs['fail_msg'] = "Failed to configure the description field"
                self.common_validation.fault(**kwargs)
                return -1, {}

        if status is not None:
            status_element = self.dev360.get_select_element_port_type("status")
            if not status_element:
                kwargs['fail_msg'] = "Port status element was not found"
                self.common_validation.fault(**kwargs)
                return -1, {}

            if (not status_element.is_selected() and status) or (
                    status_element.is_selected() and not status):

                if self.auto_actions.click(status_element) == 1:
                    kwargs['pass_msg'] = "Successfully clicked on the status element"
                    self.common_validation.passed(**kwargs)
                    sleep(2)
                else:
                    kwargs['fail_msg'] = "Failed to click on the status element"
                    self.common_validation.fault(**kwargs)
                    return -1, {}

        auto_sense = self.dev360.get_select_element_port_type("auto-sense")
        if auto_sense:
            if auto_sense.is_selected():
                if self.auto_actions.click(auto_sense) == 1:
                    kwargs['pass_msg'] = "Successfully disabled the auto sense on chosen port"
                    self.common_validation.passed(**kwargs)
                    sleep(2)
                else:
                    kwargs['fail_msg'] = "Failed to disable the auto sense on chosen port"
                    self.common_validation.fault(**kwargs)
                    return -1, {}

        port_element = self.dev360.get_select_element_port_type("port usage", f"{port_usage} port")
        if not port_element:
            kwargs['fail_msg'] = f"{port_usage} port type element was not found"
            self.common_validation.fault(**kwargs)
            return -1, {}

        if self.auto_actions.click(port_element) == 1:
            kwargs['pass_msg'] = "Successfully chose the port usage field"
            self.common_validation.passed(**kwargs)
            sleep(2)
        else:
            kwargs['fail_msg'] = "Failed to chose the port usage field"
            self.common_validation.fault(**kwargs)
            return -1, {}

        self.utils.print_info("Go to the STP settings page")
        for _ in range(5):
            if "active" in self.dev360.get_select_element_port_type("stpPage").get_attribute("class"):
                break
            get_next_button = self.dev360.get_select_element_port_type("next_button")
            if get_next_button:
                if get_next_button.is_enabled():
                    self.auto_actions.click(get_next_button)
                    sleep(2)
                else:
                    break
            else:
                kwargs['fail_msg'] = "get_next_button not found"
                self.common_validation.fault(**kwargs)
                return -1, {}

        if stp_enabled is not None:
            stp_enabled_element = self.dev360.get_select_element_port_type("stp enable")

            if not stp_enabled_element:
                kwargs['fail_msg'] = "STP Enabled element was not found"
                self.common_validation.fault(**kwargs)
                return -1, {}

            if (not stp_enabled_element.is_selected() and stp_enabled) or (
                stp_enabled_element.is_selected() and not stp_enabled):

                if self.auto_actions.click(stp_enabled_element) == 1:
                    kwargs['pass_msg'] = "Successfully clicked on the STP enabled element"
                    self.common_validation.passed(**kwargs)
                    sleep(2)
                else:
                    kwargs['fail_msg'] = "Failed to click on the STP Enabled element"
                    self.common_validation.fault(**kwargs)
                    return -1, {}

        if edge_port is not None:
            edge_port_element = self.dev360.get_select_element_port_type("edge port")

            if not edge_port_element:
                kwargs['fail_msg'] = "Edge Port element was not found"
                self.common_validation.fault(**kwargs)
                return -1, {}

            if (not edge_port_element.is_selected() and edge_port) or (
                edge_port_element.is_selected() and not edge_port):

                if self.auto_actions.click(edge_port_element) == 1:
                    kwargs['pass_msg'] = "Successfully clicked on the Edge Port element"
                    self.common_validation.passed(**kwargs)
                    sleep(2)
                else:
                    kwargs['fail_msg'] = "Failed to click on the Edge Port element"
                    self.common_validation.fault(**kwargs)
                    return -1, {}

        if bpdu_protection is not None:
            bpdu_protection_element = self.dev360.get_select_element_port_type("bpdu protection")

            if not bpdu_protection_element:
                kwargs['fail_msg'] = "BPDU Protection element was not found"
                self.common_validation.fault(**kwargs)
                return -1, {}

            if self.auto_actions.click(bpdu_protection_element) == 1:
                self.utils.print_info("Successfully clicked on the BPDU Protection element")
                sleep(5)
            else:
                kwargs['fail_msg'] = "Failed to click on the BPDU Protection element"
                self.common_validation.fault(**kwargs)
                return -1, {}

            get_bpdu_protection_items = self.dev360.get_select_element_port_type("bpdu_protection_items")

            if not get_bpdu_protection_items:
                kwargs['fail_msg'] = "BPDU Protection list elements not found"
                self.common_validation.fault(**kwargs)
                return -1, {}

            if self.auto_actions.select_drop_down_options(get_bpdu_protection_items, bpdu_protection):
                self.utils.print_info("Selected into dropdown value : ", bpdu_protection)
            else:
                kwargs['fail_msg'] = "Failed to select from BPDU Protection dropdown"
                self.common_validation.fault(**kwargs)
                return -1, {}

        if path_cost:
            path_cost_element = self.dev360.get_select_element_port_type("path cost")

            if not path_cost_element:
                kwargs['fail_msg'] = "Path Cost element was not found"
                self.common_validation.fault(**kwargs)
                return -1, {}

            if self.auto_actions.send_keys(path_cost_element, str(path_cost)) == 1:
                self.utils.print_info("Successfully configured the path cost field")
                sleep(2)
            else:
                kwargs['fail_msg'] = "Failed to configure the path cost field"
                self.common_validation.fault(**kwargs)
                return -1, {}

        if priority:
            priority_element = self.dev360.get_select_element_port_type("priority")

            if not priority_element:
                kwargs['fail_msg'] = "Failed to configure the path cost field"
                self.common_validation.fault(**kwargs)
                return -1, {}

            if self.auto_actions.click(priority_element) == 1:
                self.utils.print_info("Successfully clicked on the priority element")
                sleep(5)
            else:
                kwargs['fail_msg'] = "Failed to click on the priority element"
                self.common_validation.fault(**kwargs)
                return -1, {}

            get_priority_items = self.dev360.get_select_element_port_type("priority_items")
            if not get_priority_items:
                kwargs['fail_msg'] = "Priority dropdown elements not found"
                self.common_validation.fault(**kwargs)
                return -1, {}

            if self.auto_actions.select_drop_down_options(get_priority_items, str(priority)):
                self.utils.print_info("Selected into dropdown value : ", priority)
            else:
                kwargs['fail_msg'] = "Failed to select item from priority dropdown"
                self.common_validation.fault(**kwargs)
                return -1, {}

        self.utils.print_info("Go to the last page")
        for _ in range(5):
            if "active" in self.dev360.get_select_element_port_type("summaryPage").get_attribute("class"):
                break
            get_next_button = self.dev360.get_select_element_port_type("next_button")
            if get_next_button:
                if get_next_button.is_enabled():
                    self.auto_actions.click(get_next_button)
                    sleep(2)
                else:
                    break
            else:
                kwargs['fail_msg'] = "get_next_button not found"
                self.common_validation.fault(**kwargs)
                return -1, {}

        summary = {}

        for row_name, row_value in zip(
            ["STP", "VLAN", "Status", "Port Usage"],
            ["stp", "vlan", "status", "port usage"]
        ):
            try:
                summary[row_name] = self.dev360.get_select_element_port_type_summary(row_value).text
            except selenium.common.exceptions.StaleElementReferenceException:
                summary[row_name] = ""

        if save:
            save_button = self.dev360.get_close_port_type_box()

            if not save_button:
                kwargs['fail_msg'] = "save button not found"
                self.common_validation.fault(**kwargs)
                return -1, {}

            if self.auto_actions.click_with_js(save_button) == 1:
                self.utils.print_info("Successfully clicked on the Save element")
            else:
                kwargs['fail_msg'] = "Failed to click on the Save element"
                self.common_validation.fault(**kwargs)
                return -1, {}

        return 1, summary

    def create_new_port_type(self, cli_type, **kwargs):
        """
        - This keyword will open the window for creating a new port Type section using the Port Types section in Network Policies tab
        - Assumption: Already Opened Port Types Section
        - Flow: Switching tab --> Click on Port Types
        """
        self.auto_actions.click_reference(self.np_web_elements.get_add_new_port_type)
        self.screen.save_screen_shot()
        cli_type = cli_type.upper()
        if cli_type is not None:
            if cli_type == "VOSS":
                self.auto_actions.click_with_js(self.np_web_elements.get_select_platform_voss())
                kwargs['pass_msg'] = "Selected Platform VOSS"
                self.common_validation.passed(**kwargs)
                self.screen.save_screen_shot()
                return 1
            elif cli_type == "EXOS":
                self.auto_actions.click_with_js(self.np_web_elements.get_select_platform_exos())
                kwargs['pass_msg'] = "Selected Platform EXOS"
                self.common_validation.passed(**kwargs)
                self.screen.save_screen_shot()
                return 1
        else:
            kwargs['fail_msg'] = "Platform type not Found. Only VOSS or EXOS supported"
            self.common_validation.fault(**kwargs)
            return -1

    def edit_port_type(self, port_type_name, **kwargs):
        """Method that selects and edits a non-default port-type from Port Types Tabel.
        :param port_type_name: name of the port-type
        Returns:
            int: 1 if the function call has succeeded else -1
        """

        if self.dev360.get_d360_switch_port_view_all_pages_button():
            self.auto_actions.scroll_down()
            self.auto_actions.click_with_js(self.dev360.get_d360_switch_port_view_all_pages_button())
            self.navigator.wait_until_loading_is_done()
            self.screen.save_screen_shot()

        if port_type_name is not None:
            self.utils.print_info(f"Searching {port_type_name} on first page.")
            port_type_table_item = self.get_port_type_row(port_type_name)
            if not port_type_table_item:
                self.utils.print_info(f"Searching {port_type_name} on next page page.")
                next_page_button = self.dev360.get_device360_pagination_next_button()
                assert next_page_button, "Did not find the next page button"
                self.auto_actions.click_with_js(next_page_button)
                self.navigator.wait_until_loading_is_done()
                port_type_table_item = self.get_port_type_row(port_type_name)
            if not port_type_table_item:
                self.utils.print_info(f"Searching {port_type_name} on next page page.")
                next_page_button = self.dev360.get_device360_pagination_next_button()
                assert next_page_button, "Did not find the next page button"
                self.auto_actions.click_with_js(next_page_button)
                self.navigator.wait_until_loading_is_done()
                port_type_table_item = self.get_port_type_row(port_type_name)
            self.utils.print_info(f"Selecting port-type named {port_type_name} from table")
            self.auto_actions.scroll_down()
            self.auto_actions.click_with_js(self.np_web_elements.get_port_type_row_cell(port_type_table_item, 'dgrid-selector'))
            self.navigator.wait_until_loading_is_done()
            self.screen.save_screen_shot()
            sleep(3)
            self.utils.print_info(f"Editing port_type {port_type_name} ")
            if self.auto_actions.click_with_js(self.np_web_elements.get_edit_port_type()) == 1:
                kwargs['pass_msg'] = f"Successfully opened configuration window for port_type {port_type_name} "
                self.common_validation.passed(**kwargs)
                self.screen.save_screen_shot()
                return 1
            else:
                kwargs['fail_msg'] = f"Failed to open configuration window for port-type {port_type_name}"
                self.common_validation.fault(**kwargs)
                return -1
        else:
            kwargs['fail_msg'] = "No port-type name specified"
            self.common_validation.fault(**kwargs)
            return -1

    def delete_port_type(self, port_type_name, **kwargs):
        """Method that selects and deletes a non-default port-type from Port Types Tabel
        :param port_type_name: name of the port-type
        Returns:
            int: 1 if the function call has succeeded else -1
        """
        if self.dev360.get_d360_switch_port_view_all_pages_button():
            self.auto_actions.scroll_down()
            self.auto_actions.click_with_js(self.dev360.get_d360_switch_port_view_all_pages_button())
            self.navigator.wait_until_loading_is_done()
            self.screen.save_screen_shot()

        if port_type_name is not None:
            self.utils.print_info(f"Searching {port_type_name} on first page.")
            port_type_table_item = self.get_port_type_row(port_type_name)
            if not port_type_table_item:
                self.utils.print_info(f"Searching {port_type_name} on next page page.")
                next_page_button = self.dev360.get_device360_pagination_next_button()
                assert next_page_button, "Did not find the next page button"
                self.auto_actions.click_with_js(next_page_button)
                self.navigator.wait_until_loading_is_done()
                port_type_table_item = self.get_port_type_row(port_type_name)
            if not port_type_table_item:
                self.utils.print_info(f"Searching {port_type_name} on next page page.")
                next_page_button = self.dev360.get_device360_pagination_next_button()
                assert next_page_button, "Did not find the next page button"
                self.auto_actions.click_with_js(next_page_button)
                self.navigator.wait_until_loading_is_done()
                port_type_table_item = self.get_port_type_row(port_type_name)
            self.utils.print_info(f"Selecting port-type named {port_type_name} from table")
            self.auto_actions.click_with_js(self.np_web_elements.get_np_row_cell(port_type_table_item, 'dgrid-selector'))
            self.screen.save_screen_shot()
            self.utils.print_info(f"Deleting port_type {port_type_name} ")
            if self.auto_actions.click_with_js(self.np_web_elements.get_delete_port_type()) == 1:
                kwargs['pass_msg'] = f"Deleting port_type {port_type_name} "
                self.common_validation.passed(**kwargs)
                self.screen.save_screen_shot()
                return 1
            else:
                kwargs['fail_msg'] = f"Failed to delete port-type {port_type_name}"
                self.common_validation.fault(**kwargs)
                return -1
        else:
            kwargs['fail_msg'] = "No port-type name specified"
            self.common_validation.fault(**kwargs)
            return -1

    def get_port_type_row(self, search_string):
        """
        - Get the device row object from the Network Policies --> Port Types Section
        - Based on the search string it will search the device row
        - Search string should be port-type name

        :param search_string: it should be anything which is searched on the row cell
        :return: row element if row exists else return None
        """
        self.utils.print_info("Getting the Port Types rows from Network policy page")
        rows = self.np_web_elements.get_port_types_rows()
        sleep(5)
        if not rows:
            self.utils.print_info("Port type rows are not available in the Port Types Section")
        for row in rows:
            print(row.text)
            if search_string in row.text:
                return row
        return False

    def get_port_type_row_details(self, search_string, col_list, **kwargs):
        """
        - Gets a dictionary of port-type row values based on the passed column label list
        - The column list should be a comma-separated list of column headers, like NAME, PORT STATUS
        - Keyword Usage:
         - ``@{DEVICE_VALUES}=  Get Port Type Row Values  ${DEVICE_SERIAL}  NAME, PORT STATUS``

        :param search_string: string to uniquely identify the row in the device grid
        :param col_list: comma-separated list of column headers (e.g., NAME)
        :return: dictionary containing the values for each of the specified columns else -1 if method unsuccessful
        """
        label_map = {'NAME': 'name',
                     'DEVICE FAMILY*': 'deviceFamily',
                     'DESCRIPTION': 'description',
                     'PORT STATUS': 'enabled',
                     'VLAN': 'vlan',
                     'STP': 'stpSettings',
                     'ELRP': 'elrpSettings',
                     'MAC LOCKING': 'macLockingSettings',
                     'PSE PROFILE': 'pseProfile',
                     'USED BY': 'usedBy',
                     }

        port_type_detail_dict = dict()

        sleep(3)
        port_type_row = self.get_port_type_row(search_string)
        if port_type_row:
            col_labels = col_list.split(",")
            self.utils.print_info("Obtaining data for Column Labels: ", col_labels)

            cells = self.np_web_elements.get_port_type_row_cells(port_type_row)
            for cell in cells:
                if re.search(r'field-\w*', cell.get_attribute("class")):
                    label = re.search(r'field-\w*', cell.get_attribute("class")).group().split("field-")[-1]
                    for label_str in col_labels:
                        map_value = label_map.get(label_str)
                        if label == map_value:
                            if label == "productType":
                                if cell.text:
                                    self.utils.print_debug(f"Got Data {cell.text} For Column {label_str}")
                                    port_type_detail_dict[label_str] = cell.text
                            else:
                                self.utils.print_debug(f"Got Data {cell.text} For Column {label_str}")
                                port_type_detail_dict[label_str] = cell.text
                            break
        else:
            kwargs['fail_msg'] = f"Could not find port-type row matching the search parameter {search_string}"
            self.common_validation.fault(**kwargs)
            return -1

        self.utils.print_info("****************** DEVICE ROW VALUES ************************")
        for key, value in port_type_detail_dict.items():
            kwargs['pass_msg'] = f"{key}:{value}"
            self.common_validation.passed(**kwargs)

        return port_type_detail_dict

    def go_to_specific_tab_in_port_type_configuration(self, tab_name, **kwargs):
        """
        - This keyword will go to  the specified port Type section using the Port Types section in Network Policies tab
        - Assumption: Already Opened Port type Configuration window
        - Flow: Switching tab --> Click on Port Types

        args:
            :tab_name:        str  - the name of the tab that will change view to

        return: if the function succeeds it will return 1
                if the function fails it will return -1
        """
        label_map = {'NAME': 'usagePage',
                     'VLAN': 'tab_vlan',
                     'Transmission Settings': 'transmissionSettingsPage',
                     'STP': 'stpPage',
                     'Storm Control': 'stormControlSettingsPage',
                     'MAC LOCKING': 'MACLOCKINGSettingsPage',
                     'ELRP': 'elrdp',
                     'PSE': 'pseSettingsPage',
                     }

        if label_map[tab_name]:
            if self.dev360.get_select_element_port_type(label_map[tab_name]):
                self.utils.print_info(f"Go to the {tab_name} page")
                if self.auto_actions.click(self.dev360.get_select_element_port_type(label_map[tab_name])) == 1:
                    kwargs['pass_msg'] = f"Successfully accessed tab {tab_name}"
                    self.common_validation.passed(**kwargs)
                    self.screen.save_screen_shot()
                    sleep(3)
                    return 1
                else:
                    kwargs['fail_msg'] = f"Failed to access tab {tab_name}"
                    self.common_validation.fault(**kwargs)
                    return -1
        else:
            kwargs['fail_msg'] = f"Could not find port-type tab matching the search parameter {tab_name}"
            self.common_validation.fault(**kwargs)
            self.screen.save_screen_shot()
            return -1

    def get_random_name(self, base_string):
        """
        Method used to generate a random string with a base string
        :param base_string: a string
        :return: random string from a base string
        """
        policy_name = base_string + "_" + ''.join(random.sample(list(string.digits), k=4))
        self.utils.print_info(f"Policy name is: {policy_name}")
        return policy_name

    def open_network_policy_ssid_page(self, policy_name, ssid_name, **kwargs):
        """
        - This Keyword will Open Particular SSID name of the wireless network in the network policy
        - Flow: Navigate to the network policy -- > click on network policy card view --> click on SSID
        - Keyword Usage:
        - ``Open Network Policy SSID Page   ${POLICY_NAME}   ${SSID_NAME}``

        :param policy_name: Name of the network policy
        :param ssid_name: name of the ssid already exist on that network policy
        :return: 1 if mentioned SSID page opened successfully else -1
        """
        self.utils.print_info("Click on Network Policy card view button")
        self.navigator.navigate_to_network_policies_card_view_page()

        if self.select_network_policy_in_card_view(policy_name):
            self.utils.print_info("Selecting SSID in Network Policy")
            if self._select_ssid(ssid_name):
                self.utils.wait_till(self.np_web_elements.get_network_policy_wireless_ssid_name_textfield, timeout=90, delay=5)
                ssid_field= self.np_web_elements.get_network_policy_wireless_ssid_name_textfield()
                ssid_name_1 = ssid_field.get_attribute("value")
                self.utils.print_info(f"SSID Name in Network Policy Page is {ssid_name_1}")
                if ssid_name_1 == ssid_name:
                    kwargs['pass_msg'] = "SSID page Opened Successfully in network policy"
                    self.screen.save_screen_shot()
                    self.common_validation.passed(**kwargs)
                    return 1
                else:
                    kwargs['fail_msg'] = "SSID page Not Opened Successfully in network policy"
                    self.screen.save_screen_shot()
                    self.common_validation.failed(**kwargs)
                    return -1
        else:
            kwargs['fail_msg'] = "Network Policy Card View Not Opened Successfully"
            self.screen.save_screen_shot()
            self.common_validation.failed(**kwargs)
            return -1

    def set_dns_server_status(self, status="enable", **kwargs):
        
        if not status in ["enable", "disable"]:
            kwargs["fail_msg"] = "given status should be enable or disable"
            self.common_validation.fault(**kwargs)
        
        button, _ = self.utils.wait_till(
            func=self.np_web_elements.get_dns_server_status,
            silent_failure=True,
            exp_func_resp=True,
            delay=5
        )

        if button is None:
            kwargs["fail_msg"] = "Failed to get the dns server status button"
            self.common_validation.fault(**kwargs)
            return -1
        
        if (button.is_selected() and status == "disable") or (not button.is_selected() and status == "enable"):
            self.utils.print_info(f"{status} dns server")
            
            res, _ = self.utils.wait_till(
                func=lambda: self.auto_actions.click(button),
                exp_func_resp=True,
                delay=4,
                silent_failure=True
            )

            if res != 1:
                kwargs["fail_msg"] = "Failed to click the dns server status button"
                self.common_validation.fault(**kwargs)
                return -1
        else:
            self.utils.print_info(f"status of dns server is already {status}d")
            
        kwargs["pass_msg"] = f"Successfully set the status of dns server - {status}d"
        self.common_validation.passed(**kwargs)
        return 1
        
    def go_to_dns_server_tab(self, **kwargs):
        
        tab, _ = self.utils.wait_till(
            func=self.np_web_elements.get_nw_policy_additional_settings_dns_server_tab,
            silent_failure=True,
            exp_func_resp=True,
            delay=5
        )

        if tab is None:
            kwargs["fail_msg"] = "Failed to get the dns server tab"
            self.common_validation.fault(**kwargs)
            return -1
    
        res, _ = self.utils.wait_till(
            func=lambda: self.auto_actions.click(tab),
            exp_func_resp=True,
            delay=4,
            silent_failure=True
        )

        if res != 1:
            kwargs["fail_msg"] = "Failed to click the dns server status tab"
            self.common_validation.fault(**kwargs)
            return -1
            
        kwargs["pass_msg"] = "Successfully went to the dns server tab"
        self.common_validation.passed(**kwargs)
        return 1
    
    def save_dns_server_tab(self, **kwargs):

        button, _ = self.utils.wait_till(
            func=self.np_web_elements.get_dns_server_save_button,
            silent_failure=True,
            exp_func_resp=True,
            delay=5
        )

        if button is None:
            kwargs["fail_msg"] = "Failed to get the dns server save button"
            self.common_validation.fault(**kwargs)
            return -1

        res, _ = self.utils.wait_till(
            func=lambda: self.auto_actions.click(button),
            exp_func_resp=True,
            delay=4,
            silent_failure=True
        )

        if res != 1:
            kwargs["fail_msg"] = "Failed to click the dns server save button"
            self.common_validation.fault(**kwargs)
            return -1
            
        kwargs["pass_msg"] = "Successfully clicked the dns server save button"
        self.common_validation.passed(**kwargs)
        return 1
