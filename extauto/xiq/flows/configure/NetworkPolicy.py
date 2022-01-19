from time import sleep
import re
from robot.libraries.BuiltIn import BuiltIn
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions

import xiq.flows.common.ToolTipCapture as tool_tip
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


class NetworkPolicy(object):

    def __init__(self):
        self.utils = Utils()
        self.wireless_nw = WirelessNetworks()
        self.auto_actions = AutoActions()
        self.navigator = Navigator()
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
        if policy_row:
            self.utils.print_info(f"Network policy {policy} exists in the network policy list")
            return 1

    def _perform_np_delete(self):
        """
        clicking on the network policy delete button
        :return:
        """
        self.utils.print_info("Click on network policy delete button")
        self.auto_actions.click(self.np_web_elements.get_np_delete_button())

        sleep(2)
        self.utils.print_info("Click on confirmation Yes Button")
        self.auto_actions.click(self.dialogue_web_elements.get_confirm_yes_button())

        sleep(5)
        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)

        sleep(2)
        for value in tool_tp_text:
            if "Network policy was deleted successfully" in value:
                return 1
            elif "The Network Policy cannot be removed " in value:
                self.utils.print_info(f"{value}")
                return -1
            elif "An unknown error has occurred" in value:
                self.utils.print_info("Unable to delete the network policy")
                self.utils.print_info(f"{value}")
                return -2
        return -1

    def create_network_policy(self, policy, **wireless_profile):
        """
        - Create the network policy from CONFIGURE-->NETWORK POLICIES
        - This keyword will create the network policy and wireless network
        - Wireless network includes open, ppsk, psk and enterprise network
        - Keyword Usage:
         - ``Create Network Policy   ${POLICY_NAME}   &{WIRELESS_NW_PROFILE}``
         - &{WIRELESS_NW_PROFILE} --> This is dictionary, include all key value pair to create wireless network
         - Fof Creating  &{WIRELESS_NW_PROFILE} dict refer wireless_network_config.robot

        :param policy: Name of the network policy to create
        :param wireless_profile: (dict) wireless network creation profile parameters
        :return: 1 if network policy creation is success
        """
        self.navigator.navigate_to_devices()
        if not self.navigator.navigate_to_network_policies_list_view_page() == 1:
            return -2

        self.utils.print_info("Checking for network policy add button")
        if self.np_web_elements.check_np_add_button() == -2:
            self.utils.print_info("Add button is not enabled for the user")
            return -2

        if self._search_network_policy_in_list_view(policy):
            self.utils.print_info(f"Network policy {policy} already exists in the network polices list")
            return 1

        self.utils.print_info("Click on network policy add button")
        self.auto_actions.click(self.np_web_elements.get_np_add_button())
        sleep(2)

        self.utils.print_info("Enter the policy name:{}".format(policy))
        self.auto_actions.send_keys(self.np_web_elements.get_np_name_text(), policy)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Click on network policy save button")
        self.auto_actions.click(self.np_web_elements.get_np_save_button())

        sleep(5)
        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)

        for tip_text in tool_tp_text:
            if "The Network Policy cannot be saved because" in tip_text:
                self.utils.print_info(f"{tip_text}")
                return 1
            if "Your account does not have permission to perform that action" in tip_text:
                self.utils.print_info(f"{tip_text}")
                return -2

            if "Unable to access data" in tip_text:
                self.utils.print_info("not able to save the network policy")
                self.utils.print_info(f"{tip_text}")
                return -3

        return self.wireless_nw.create_wireless_network(**wireless_profile)

    def delete_network_policy(self, policy):
        """
        - Delete Network Policy from network policy Grid
        - Keyword Usage:
         - ``Delete Network Policy    ${POLICY_NAME}``

        :param policy: Name of the policy to delete
        :return: 1 if deleted else -1
        """
        if not self.navigator.navigate_to_network_policies_list_view_page() == 1:
            return -2

        if not self._search_network_policy_in_list_view(policy):
            self.utils.print_info(f"Network policy {policy} does't exists in the network policies list")
            return 1

        self.utils.print_info("Select Network policy row")
        self.select_network_policy_row(policy)
        sleep(3)

        return self._perform_np_delete()

    def delete_network_polices(self, *policies):
        """
        - Deleting the network policies based on the passed list of policies
        - Keyword Usage:
         - ``Delete Network Policies   ${POLICY1}   ${POLICY2}``

        :param policies: list of network polices to delete
        :return: 1 if deleted successfully else -1
        """
        if not self.navigator.navigate_to_network_policies_list_view_page() == 1:
            return -2

        select_flag = None
        for policy in policies:
            if self._search_network_policy_in_list_view(policy):
                self.utils.print_info("Select Network policy row")
                self.select_network_policy_row(policy)
                select_flag = True
                sleep(1)
            else:
                self.utils.print_info(f"Network policy does't {policy} exists in the network policies list")

        if select_flag:
            return self._perform_np_delete()
        return 1

    def delete_all_network_policies(self, exclude_list=''):
        """
        - Delete all network policies from the grid expect exclude_list policies
        - keyword Usage:
          - ``Delete All Network Policies  exclude_list=${POLICY1},${POLICY2)``

        :param exclude_list: list of policies to exclude from delete
        :return: 1 if deleted successfully else -1
        """
        exclude_list = exclude_list.split(",")
        np_list = self._get_network_policy_list()
        if np_list == -2:
            return -2

        delete_np_list = [np for np in np_list if np not in exclude_list]
        self.utils.print_info(f"Deleting network policy list:{delete_np_list}")

        return self.delete_network_polices(*delete_np_list)

    def edit_network_policy_ssid(self, policy_name, ssid_name, new_ssid_name):
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
        self.navigator.navigate_to_network_policies_card_view_page()

        if self.select_network_policy_in_card_view(policy_name):
            if self._select_ssid(ssid_name):
                self.utils.print_info("Sending New SSID: ", new_ssid_name)
                self.auto_actions.send_keys(self.np_web_elements.get_network_policy_wireless_ssid_name_textfield(), new_ssid_name)
                sleep(5)

        self.utils.print_info("Clicking on Network Save button..")
        self.auto_actions.click(self.np_web_elements.get_network_policy_wireless_networks_save_button())

        return 1

    def select_network_policy_in_card_view(self, policy_name):
        """
        - Selects the existing network polices card view

        :param policy_name: name of the policy to search
        :return: 1 if exists else -1
        """

        self.utils.print_info("Selecting Network Policy: ", policy_name)

        self.utils.print_info("Click on Network Policy card view button")
        self.auto_actions.click(self.np_web_elements.get_network_policy_card_view())
        sleep(5)
        policy_cards = self.np_web_elements.get_network_policy_card_items()
        for policy_card in policy_cards:
            if policy_name.upper() in policy_card.text.upper():
                self.utils.print_info(policy_card.text)
                self.auto_actions.click(self.np_web_elements.get_network_policy_card_item_edit_icon(policy_card))
                sleep(5)
                return 1
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
        self.auto_actions.click(self.np_web_elements.get_network_policy_wireless_networks_tab())
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
                              _time=None):
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
        self.auto_actions.click(self.np_web_elements.get_deploy_policy_tab())
        sleep(2)

        self.utils.print_info("Click on eligible device button")
        self.auto_actions.click(self.np_web_elements.get_eligible_device_button())
        sleep(5)

        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)
        for tip_text in tool_tp_text:
            if "An unknown error has" in tip_text:
                self.screen.save_screen_shot()
                sleep(2)
                self.robot_built_in.fail(f"{tip_text} occurred while assigning nw policy")

        if not self._select_device_row(devices):
            self.utils.print_info("Device is not available in the deploy policy page")
            return -1
        self.screen.save_screen_shot()
        sleep(5)
        self.utils.print_info("Click on the policy deploy upload button")
        self.auto_actions.click(self.np_web_elements.get_deploy_policy_upload_button())

        sleep(10)

        if update_type == 'delta' and next_reboot == False and _date == None:
            self.utils.print_info("Selecting Delta Config Update")
            self.auto_actions.click(self.device_update_web_elements.get_delta_config_update_radio())
            sleep(2)
            self.screen.save_screen_shot()
            self.utils.print_info("Click on the perform update")
            self.auto_actions.click(self.np_web_elements.get_perform_update_button())
            sleep(2)
            tool_tp_text = tool_tip.tool_tip_text
            self.utils.print_info(tool_tp_text)
            for value in tool_tp_text:
                if "a device mode change is not supported with a delta configuration update" in value.lower():
                    self.utils.print_info(value)
                    update_type = "complete"

        if update_type == 'complete':
            self.utils.print_info("Selecting Complete Config Update")
            self.auto_actions.click(self.device_update_web_elements.get_complete_config_update_radio())
            self.screen.save_screen_shot()
            sleep(2)

        if next_reboot:
            update_type = "complete"
            self.utils.print_info("Selecting Complete Config Update")
            self.auto_actions.click(self.device_update_web_elements.get_complete_config_update_radio())
            sleep(2)

            self.utils.print_info("Selecting Next Reboot radio")
            self.auto_actions.click(self.device_update_web_elements.get_activate_at_next_reboot_radio())
            sleep(2)

        if _date:
            update_type = "complete"
            self.utils.print_info("Selecting Complete Config Update")
            self.auto_actions.click(self.device_update_web_elements.get_complete_config_update_radio())
            sleep(2)

            self.utils.print_info("Selecting Activate at radio")
            self.auto_actions.click(self.device_update_web_elements.get_activate_at_time_radio())
            sleep(2)

            self.utils.print_info("Selecting Time to update")

            self.auto_actions.send_page_down(self.device_update_web_elements.get_activate_at_time_radio())
            sleep(5)

            self.auto_actions.click(self.device_update_web_elements.get_activate_at_date_textfield())
            sleep(5)
            self.auto_actions.send_keys(self.device_update_web_elements.get_activate_at_date_textfield(), _date)
            sleep(5)

            self.auto_actions.click(self.device_update_web_elements.get_activate_at_time_textfield())
            sleep(5)
            self.auto_actions.send_keys(self.device_update_web_elements.get_activate_at_time_textfield(), _time)
            sleep(5)

        self.screen.save_screen_shot()

        if update_type != 'delta':
            self.utils.print_info("Click on the perform update")
            self.auto_actions.click(self.np_web_elements.get_perform_update_button())
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
                self.utils.print_info(f"Config push to AP taking more than {max_config_push_wait}seconds")
                return -1
            sleep(30)
            retry_count += 30

        network_policy = self.device.get_ap_network_policy(devices)
        if network_policy == policy_name:
            self.utils.print_info("Network Policy in Devices grid matches...")
            return 1
        else:
            self.utils.print_info("Network Policy in Devices grid does not matches with the deployed one...")
            return -1

    def navigate_to_np_edit_tab(self, policy_name):
        """
        - Flow: Configure-->Network policy-->Select List View-->Select Network Policy ROW--> Edit

        :param policy_name: policy name
        :return: 1 if success
        """
        self.utils.print_info("Navigating to the configure network policies")
        self.navigator.navigate_configure_network_policies()
        sleep(2)

        self.utils.print_info("Click on network policy list view button")
        self.auto_actions.click(self.np_web_elements.get_network_policy_list_view())
        sleep(2)

        self.utils.print_info("Click on network policy fill size page")
        if self.np_web_elements.get_network_policy_page_size():
            self.auto_actions.click(self.np_web_elements.get_network_policy_page_size())
            sleep(2)

        self.utils.print_info("Select the network policy rows")
        self.select_network_policy_row(policy_name)

        self.utils.print_info("Click on network policy Edit button")
        self.auto_actions.click(self.np_web_elements.get_np_edit_button())
        sleep(2)
        return 1

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

    def delete_network_policy_with_ssid(self, ssid_name):
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
            self.utils.print_info("Unable to find policy with SSID: ", ssid_name)
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
        self.auto_actions.click(self.np_web_elements.get_network_policy_card_view())
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

    def deploy_network_policy_with_complete_update(self, policy_name, devices):
        """
        - Config push network policy with complete update
        - This will reboot the Device
        - if already in network policy then deploy the policy else navigate to network policy--> deploy policy tab
        - Keyword Usage:
         - ``Deploy Network Policy With Complete Update   ${POLICY_NAME}    ${DEVICE_MAC}``

        :param policy_name: Name of the policy
        :param devices: Device serial number
        :return: 1 if success else -1
        """
        return self.deploy_network_policy(policy_name, devices, 'complete')

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

    def deploy_network_policy_with_delta_update(self, policy_name, devices):
        """
        - delta config push of network policy
        - if already in network policy then deploy the policy else navigate to network policy--> deploy policy tab
        - Keyword Usage:
         - ``Deploy Network Policy With Delta Update   ${POLICY_NAME}   ${DEVICE_MAC}``

        :param policy_name: Name of the policy
        :param devices: Device serial number
        :return:
        """
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
        self.auto_actions.click(self.np_web_elements.get_network_policy_list_view())

        cell = self.np_web_elements.get_np_page_title()
        sleep(2)
        title = cell.text

        self.utils.print_info("page title :", title)

        if title == "Network Policies":
            return 1
        else:
            return -2

    def navigate_wireless_ssid(self, policy_name, ssid):
        """
        - Flow: Configure --> Network Policies--> Select the policy-->Wireless tab--> Select SSID

        :param policy_name: name of the network policy
        :param ssid: ssid name
        :return:
        """
        self.navigate_to_np_edit_tab(policy_name)
        if not self._select_ssid(ssid) == 1:
            self.utils.print_info("SSID:{} not selected".format(ssid))
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

        self.auto_actions.click(self.wireless_element.get_wireless_networks_tab())
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

    def delete_all_ssid_in_policy(self, policy):
        """ delete all ssids in the policy
            :param: policy: name of the policy
            :return 1 if deletion of ssids is success
        """
        self.utils.print_info(" Delete all ssids in the policy  " + str(policy))
        self.auto_actions.scroll_up()
        self.navigate_to_np_edit_tab(policy)

        self.utils.print_info(" Click on the wireless network tab")
        self.auto_actions.click(self.wireless_element.get_wireless_networks_tab())
        self.tools.wait_til_elements_avail(self.wireless_element.wireless_nw_add_button, 60, False)
        self.utils.print_info(" Get all ssids in the policy")
        ssids = self.wireless_element.get_ssid_list()
        if not ssids:
            return 1
        else:
            for ssid in range(1, len(ssids) + 1):
                self.utils.print_info(" Delete the ssid " + str(ssid))
                self.tools.wait_til_elements_avail(self.wireless_element.wireless_ssid_list)
                self.auto_actions.click(self.wireless_element.get_ssid_chkbox())
                self.auto_actions.click(self.wireless_element.get_wireless_delete_button())
                self.tools.wait_til_elements_avail(self.filter_element.dialog_yes_filter_btn, 30, False)
                self.auto_actions.click(self.filter_element.get_del_yes_btn())
        self.utils.print_info(" Exit delete all ssids ")

        return 1

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
        self.auto_actions.click(self.np_web_elements.get_enable_presence_analytics_btn())
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Click on network policy save button")
        self.auto_actions.click(self.np_web_elements.get_np_save_button())

    def enable_ibeacon_service_in_network_policy(self, nw_policy, service_name, uuid, monitoring):
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
        self.auto_actions.click(self.np_web_elements.get_network_policy_additional_settings_tab())
        sleep(2)

        if self.np_web_elements.get_additional_settings_ibeacon_menu().is_displayed():
            self.utils.print_info("Click on iBeacon Service Menu button")
            self.auto_actions.click(self.np_web_elements.get_additional_settings_ibeacon_menu())
            sleep(2)
        else:
            self.utils.print_info("Click Security Tab")
            self.auto_actions.click(self.np_web_elements.get_policy_settings_menu())
            sleep(2)
            self.utils.print_info("Click on iBeacon Service Menu button")
            self.auto_actions.click(self.np_web_elements.get_additional_settings_ibeacon_menu())
            sleep(2)

        sleep(5)
        self.utils.print_info("Click on Enable IBeacon service button")
        if not self.np_web_elements.get_ibeacon_status_button().is_selected():
            self.auto_actions.click(self.np_web_elements.get_ibeacon_status_button())
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
                self.auto_actions.click(self.np_web_elements.get_ibeacon_monitoring_checkbox())
                sleep(2)

        elif monitoring == 'disable':
            self.utils.print_info("Disable IBeacon Monitoring Checkbox")
            if self.np_web_elements.get_ibeacon_monitoring_checkbox().is_selected():
                self.auto_actions.click(self.np_web_elements.get_ibeacon_monitoring_checkbox())
                sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Click on Save button")
        self.auto_actions.click(self.np_web_elements.get_ibeacon_services_save_button())
        sleep(3)

        tool_tip_text = tool_tip.tool_tip_text
        self.utils.print_info("Tool tip Text Displayed on Page", tool_tip_text)
        if "iBeacon settings saved successfully" in tool_tip_text:
            return 1
        else:
            return -1

    def disable_ibeacon_service_in_network_policy(self, nw_policy):
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
        self.auto_actions.click(self.np_web_elements.get_network_policy_additional_settings_tab())
        sleep(2)

        if self.np_web_elements.get_additional_settings_ibeacon_menu().is_displayed():
            self.utils.print_info("Click on iBeacon Service Menu button")
            self.auto_actions.click(self.np_web_elements.get_additional_settings_ibeacon_menu())
            sleep(2)
        else:
            self.utils.print_info("Click Security Tab")
            self.auto_actions.click(self.np_web_elements.get_policy_settings_menu())
            sleep(2)
            self.utils.print_info("Click on iBeacon Service Menu button")
            self.auto_actions.click(self.np_web_elements.get_additional_settings_ibeacon_menu())
            sleep(2)

        sleep(5)
        self.utils.print_info("Click on Disable IBeacon service button")
        self.auto_actions.click(self.np_web_elements.get_ibeacon_status_button())
        sleep(2)

        self.utils.print_info("Click on Save button")
        self.auto_actions.click(self.np_web_elements.get_ibeacon_services_save_button())
        sleep(3)

        tool_tip_text = tool_tip.tool_tip_text
        self.utils.print_info("Tool tip Text Displayed on Page", tool_tip_text)
        if "iBeacon settings saved successfully" in tool_tip_text:
            return 1
        else:
            return -1

    def configure_access_security_pre_authentication_status(self, status, policy_name, ssid):
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
        self.auto_actions.click(self.np_web_elements.get_ssid_authentication_additional_settings_option())
        sleep(2)

        self.utils.print_info("click Customize button")
        self.auto_actions.click(self.np_web_elements.get_advance_access_security_customize_button())
        sleep(2)

        if status.upper() == "ENABLE":
            self.auto_actions.enable_check_box(
                self.np_web_elements.get_access_security_pre_authentication_checkbox())
            self.screen.save_screen_shot()
            sleep(2)

            self.utils.print_info("click on save button")
            self.auto_actions.click(self.np_web_elements.get_access_security_settings_save_button())
            sleep(2)

        else:
            self.auto_actions.disable_check_box(
                self.np_web_elements.get_access_security_pre_authentication_checkbox())
            self.screen.save_screen_shot()
            sleep(2)

            self.utils.print_info("click on save button")
            self.auto_actions.click(self.np_web_elements.get_access_security_settings_save_button())
            sleep(2)

        self.utils.print_info("Click on network policy SSID save button")
        self.auto_actions.click(self.np_web_elements.get_np_ssid_save_button())

        tool_tip_text = tool_tip.tool_tip_text
        self.utils.print_info("Tool tip Text Displayed on Page", tool_tip_text)
        if "SSID was saved successfully." in tool_tip_text:
            return 1
        else:
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
                    self.auto_actions.click(self.wireless_element.get_wireless_authtype_open())

        self.utils.print_info("Clicking on Network Save button..")
        self.auto_actions.click(self.np_web_elements.get_network_policy_wireless_networks_save_button())

        return 1

    def create_switching_routing_network_policy(self, policy_name):
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
            return -1

        self.utils.print_info("Checking for network policy add button")
        if self.np_web_elements.check_np_add_button() == -2:
            self.utils.print_info("Add button is not enabled for the user")
            return -1

        if self._search_network_policy_in_list_view(policy_name):
            self.utils.print_info("Network policy {} already exists in the network polices list".format(policy_name))
            return 1

        self.utils.print_info("Click on network policy add button")
        self.auto_actions.click(self.np_web_elements.get_np_add_button())
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
        self.auto_actions.click(self.np_web_elements.get_np_save_button())

        sleep(5)
        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)

        for tip_text in tool_tp_text:
            if "The Network Policy cannot be saved because" in tip_text:
                self.utils.print_info(f"{tip_text}")
                return 1
            if "Your account does not have permission to perform that action" in tip_text:
                self.utils.print_info(f"{tip_text}")
                return -1

            if "Unable to access data" in tip_text:
                self.utils.print_info("not able to save the network policy")
                self.utils.print_info(f"{tip_text}")
                return -1

        self.utils.print_info("Click on network policy exit button")
        self.auto_actions.click(self.np_web_elements.get_np_exit_button())
        sleep(2)

        return 1

    def edit_network_policy_type(self, nw_policy, options_params):
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
        self.auto_actions.click(self.np_web_elements.get_np_save_button())

        sleep(2)
        self.screen.save_screen_shot()
        sleep(2)

        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)
        sleep(5)

        tool_tip_text = tool_tip.tool_tip_text

        self.utils.print_info("Tool tip Text Displayed on Page", tool_tip_text)
        if "Network Policy was saved successfully." in tool_tip_text:
            return 1
        else:
            return -1

    def deploy_stack_network_policy(self, device_mac, policy_name, sw_template_name):
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
        self.auto_actions.click(self.np_web_elements.get_deploy_policy_tab())
        sleep(2)

        self.utils.print_info("Click on eligible device button")
        self.auto_actions.click(self.np_web_elements.get_eligible_device_button())
        sleep(2)

        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)
        for tip_text in tool_tp_text:
            if "An unknown error has" in tip_text:
                self.screen.save_screen_shot()
                sleep(2)
                self.robot_built_in.fail(f"{tip_text} occurred while assigning nw policy")

        if not self._select_device_row(device_mac):
            self.utils.print_info("Device is not available in the deploy policy page")
            return -1
        self.screen.save_screen_shot()
        sleep(1)
        self.utils.print_info("Click on the policy deploy upload button")
        self.auto_actions.click(self.np_web_elements.get_deploy_policy_upload_button())
        sleep(1)
        self.screen.save_screen_shot()
        self.utils.print_info("Click on the perform update")
        self.auto_actions.click(self.np_web_elements.get_perform_after_select_update_policy_button())

        # Select from dropdown
        if sw_template_name is not None:
            sleep(10)
            click_dropdown = self.devices_web_elements.get_devices_stack_update_policy_dropdown_btn()
            if click_dropdown:
                self.utils.print_info(f" Click on dropdown ")
                self.auto_actions.click(click_dropdown)
            else:
                self.utils.print_info(f" Not able to find dropdown  ")
            dropdown_items = self.devices_web_elements.get_devices_stack_update_policy_dropdown_items()
            if dropdown_items:
                self.utils.print_info(f" The templates from dropdown are: ")
                for elem in dropdown_items:
                    self.utils.print_info(elem.text)
                for el in dropdown_items:
                    if sw_template_name in el.text:
                        self.utils.print_info(f" Select {el.text} from dropdown")
                        self.auto_actions.select_drop_down_options(dropdown_items, el.text)
                    else:
                        self.utils.print_info(f" The template name was not found in dropdown")
            else:
                self.utils.print_info(f" Not able to find dropdown items ")
        else:
            self.utils.print_info(f" The sw_template_name is None  ")

        # Perform the update
        self.screen.save_screen_shot()
        sleep(5)
        tool_tp_text_before = tool_tip.tool_tip_text.copy()
        self.utils.print_info(tool_tp_text_before)

        if self.np_web_elements.get_perform_update_policy_button():
            self.utils.print_info("Click on update policy button ")
            self.auto_actions.click(self.np_web_elements.get_perform_update_policy_button())
        else:
            self.utils.print_info("The update policy button was not found")

        self.screen.save_screen_shot()
        sleep(5)
        tool_tp_text_after = tool_tip.tool_tip_text.copy()
        self.utils.print_info(tool_tp_text_after)

        for item_after in tool_tp_text_after:
            if item_after in tool_tp_text_before:
                pass
            else:
                self.utils.print_info(" Below error message is displayed after press update button")
                self.utils.print_info(item_after)
                return item_after
        return 1

    def select_ssid_in_policy(self, policy, ssid):
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
        self.auto_actions.click(self.wireless_element.get_wireless_networks_tab())

        self.utils.print_info("Clicking on the Select option to select SSID")
        self.auto_actions.click(self.wireless_element.get_wireless_ssid_select_button())
        sleep(2)
        self.screen.save_screen_shot()

        for row in self.wireless_element.get_wireless_ssid_select_window_rows():
            if ssid.upper() == row.text.upper():
                self.utils.print_info(f"Selecting the SSID: {ssid}")
                self.auto_actions.move_to_element(self.wireless_element.
                                                  get_wireless_select_ssid_row_check_box(row))
                self.auto_actions.click(self.wireless_element.get_wireless_select_ssid_row_check_box(row))
                sleep(2)
                self.auto_actions.click(self.wireless_element.get_wireless_ssid_select_option_button())
                self.screen.save_screen_shot()
                return True
        self.utils.print_info(f"SSID: {ssid} not present !!!")
        self.auto_actions.click(self.wireless_element.get_wireless_ssid_select_cancel_button())
        return False

    def enable_classifier_maps(self, nw_policy, classifier_name):
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
        self.auto_actions.click(self.np_web_elements.get_network_policy_additional_settings_tab())
        sleep(2)

        self.np_web_elements.get_additional_settings_classifiermaps().is_displayed()

        self.utils.print_info("Scroll to the Classifier Maps Option")
        self.auto_actions.click(self.np_web_elements.get_additional_settings_classifiermaps())
        sleep(2)
        self.utils.print_info("Click on Classifier Maps")
        self.auto_actions.click(self.np_web_elements.get_additional_settings_classifiermaps())
        sleep(2)

        self.utils.print_info("Enable Classifier Maps")
        self.auto_actions.click(self.np_web_elements.get_classifiermaps_enable())
        sleep(3)

        self.utils.print_info("Enter Classifier Maps Name")
        self.auto_actions.send_keys(self.np_web_elements.get_classifiermaps_name(), classifier_name)
        sleep(3)

        self.utils.print_info("Enter Classifier Maps Description")
        self.auto_actions.send_keys(self.np_web_elements.get_classifiermaps_description(), classifier_name)
        sleep(3)

        self.utils.print_info("Add Service")
        self.auto_actions.click(self.np_web_elements.get_classifiermaps_add_button())
        sleep(3)

        self.utils.print_info("Select from the following link")
        self.auto_actions.click(self.np_web_elements.get_classifiermaps_services_selectfromfollowing_link())
        sleep(3)

        self.utils.print_info("Select BGP Service")
        self.auto_actions.click(self.np_web_elements.get_classifiermaps_services_select_service_bgp())
        sleep(3)

        self.utils.print_info("Save BGP Service")
        self.auto_actions.click(self.np_web_elements.get_classifiermaps_services_initial_save_button())
        sleep(3)

        self.utils.print_info("Click on Save Services Button")
        self.auto_actions.click(self.np_web_elements.get_classifiermaps_services_save_button())
        sleep(3)

        self.utils.print_info("Click on MAC OUIs")
        self.auto_actions.click(self.np_web_elements.get_classifiermaps_macoui_link())
        sleep(3)

        self.utils.print_info("Click on Add")
        self.auto_actions.click(self.np_web_elements.get_classifiermaps_macoui_add())
        sleep(3)

        self.utils.print_info("Click on DropDown Menu")
        self.auto_actions.click(self.np_web_elements.get_classifiermaps_macoui_dropdown())
        sleep(3)

        self.utils.print_info("Click Aerohive-08EA44")
        self.auto_actions.click(self.np_web_elements.get_classifiermaps_add_macoui_from_dropdown())
        sleep(3)

        self.utils.print_info("Click on Save Button")
        self.auto_actions.click(self.np_web_elements.get_classifiermaps_macoui_save_button())
        sleep(3)

        self.utils.print_info("Click on SSID")
        self.auto_actions.click(self.np_web_elements.get_classifiermaps_ssid_link())
        sleep(3)

        self.utils.print_info("Add SSID")
        self.auto_actions.click(self.np_web_elements.get_classifiermaps_add_ssid())
        sleep(3)

        self.utils.print_info("Click on Save Button")
        self.auto_actions.click(self.np_web_elements.get_classifiermaps_ssid_save_button())
        sleep(3)

        self.utils.print_info("Click on 802.1p/DiffServ/802.11e")
        self.auto_actions.click(self.np_web_elements.get_classifiermaps_802_link())
        sleep(3)

        self.utils.print_info("Enable 802.1p")
        self.auto_actions.click(self.np_web_elements.get_classifiermaps_802enable())
        sleep(3)

        self.utils.print_info("Enable DiffServ")
        self.auto_actions.click(self.np_web_elements.get_classifiermaps_diffservenable())
        sleep(3)

        self.utils.print_info("Enable 802.11e")
        self.auto_actions.click(self.np_web_elements.get_classifiermaps_80211enable())
        sleep(3)

        self.utils.print_info("Click on Save button")
        self.auto_actions.click(self.np_web_elements.get_Classifier_Maps_save_button())
        sleep(3)

        tool_tip_text = tool_tip.tool_tip_text
        self.utils.print_info("Tool tip Text Displayed on Page", tool_tip_text)
        if "Classifier Maps Additional Settings saved successfully" in tool_tip_text:
            return 1
        else:
            return -1
    
    def enable_marker_maps(self, nw_policy, **MarkerMap_dict):
        """
        - This keyword is used to enable Marker Maps which Marks the outgoing or upstream traffic with the specified traffic priority markers.
        - Flow: Configure --> Network Policy --> select the Policy -->Advance Settings-->QoS Options --> Marker Maps
        - Keyword Usage:
        -``Enable Marker Maps   ${AP_NETWORK_POLICY}  &{MarkerMap_dict}''
        :param nw_policy: name of the policy for enabling the Marker Maps
        :param **MarkerMap_dict: A dictionary that will contains all values required for Marker Maps Configuration
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
        self.auto_actions.click(self.np_web_elements.get_network_policy_additional_settings_tab())
        sleep(2)

        self.np_web_elements.get_additional_settings_marker_maps().is_displayed()
        
        self.utils.print_info("Scroll to the Marker Maps Option")
        self.auto_actions.click(self.np_web_elements.get_additional_settings_marker_maps())
        sleep(2)
        
        self.utils.print_info("Click on Marker Maps")
        self.auto_actions.click(self.np_web_elements.get_additional_settings_marker_maps())
        sleep(2)

        self.utils.print_info("Enable Marker Maps")
        self.auto_actions.click(self.np_web_elements.get_marker_maps_status_button())
        sleep(3)

        self.utils.print_info("Enter Marker Maps Name")
        self.auto_actions.send_keys(self.np_web_elements.get_marker_maps_name_textfield(), marker_name)
        sleep(3)

        self.utils.print_info("Enter Marker Maps Description")
        self.auto_actions.send_keys(self.np_web_elements.get_marker_maps_description(), marker_name)
        sleep(3)

        self.utils.print_info("Enable 802.1p Markers")
        self.auto_actions.click(self.np_web_elements.get_marker_maps_8021P())
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
        self.auto_actions.click(self.np_web_elements.get_marker_maps_Switch_to_diffServ())
        sleep(3)

        self.utils.print_info("Enable diffServ Markers")
        self.auto_actions.click(self.np_web_elements.get_marker_maps_diffServ())
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
        self.auto_actions.click(self.np_web_elements.get_marker_maps_services_save_button())
        sleep(3)

        tool_tip_text = tool_tip.tool_tip_text
        self.utils.print_info("Tool tip Text Displayed on Page", tool_tip_text)
        if "Marker Maps Settings saved successfully" in tool_tip_text:
            return 1
        else:
            return -1

    def enable_QoS_Overview_DAS(self, nw_policy):
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
        self.auto_actions.click(self.np_web_elements.get_network_policy_additional_settings_tab())
        sleep(2)

        if self.np_web_elements.get_additional_settings_marker_maps().is_displayed():
            self.utils.print_info("Scroll to the QoS Overview Option")
            self.auto_actions.click(self.np_web_elements.get_additional_settings_QoS_Overview())
            sleep(2)
        else:
            self.utils.print_info("Click Security Tab")
            self.auto_actions.click(self.np_web_elements.get_qos_options_menu())
            sleep(2)
            self.utils.print_info("Click on QoS Overview")
            self.auto_actions.click(self.np_web_elements.get_additional_settings_QoS_Overview())
            sleep(2)

        self.utils.print_info("Enable Dynamic Airtime Scheduling")
        self.auto_actions.click(self.np_web_elements.get_QoS_Dynamic_Airtime_Scheduling_Enable())
        sleep(2)

        self.utils.print_info("Click on Save button")
        self.auto_actions.click(self.np_web_elements.get_QoS_services_save_button())
        
        tool_tip_text = tool_tip.tool_tip_text
        self.utils.print_info("Tool tip Text Displayed on Page", tool_tip_text)
        if "QoS Overview Settings are saved successfully" in tool_tip_text:
            return 1
        else:
            return -1
          
    def create_owe_ssid(self, nw_policy, ssid, WiFi2):
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
        self.auto_actions.click(self.wireless_element.get_wireless_networks_tab())

        self.utils.print_info("Click on Add SSID")
        self.auto_actions.click(self.np_web_elements.get_add_ssid_menu())
        sleep(2)

        self.utils.print_info("Select All Other Networks(standard)")
        self.auto_actions.click(self.np_web_elements.get_select_all_other_networks())
        sleep(2)

        self.utils.print_info("Enter SSID")
        self.auto_actions.send_keys(self.np_web_elements.get_wireless_networks_ssid_textfield(), ssid)
        sleep(2)

        if WiFi2 == 'enable':
            self.utils.print_info("Enabling WiFi2 Checkbox")
            self.auto_actions.enable_check_box(self.np_web_elements.get_OWE_wifi2_checkbox())
            sleep(2)

            self.utils.print_info("Clicking 'Yes'")
            self.auto_actions.click(self.np_web_elements.get_OWE_wifi2_dialogue_box_yes())
            sleep(2)

            self.utils.print_info("Click on Enhanced Open Secure SSID Authentication")
            self.auto_actions.click(self.np_web_elements.get_Enhanced_Open_Authentication())
            sleep(3)

            self.utils.print_info("Click on Save Button")
            self.auto_actions.click(self.np_web_elements.get_save_enhanced_open_ssid())
            sleep(3)
            return 1

        elif WiFi2 == 'disable':
            self.utils.print_info("Disabling WiFi2 Checkbox")
            self.auto_actions.disable_check_box(self.np_web_elements.get_OWE_wifi2_checkbox())
            sleep(2)

            self.utils.print_info("Click on Enhanced Open Secure SSID Authentication")
            self.auto_actions.click(self.np_web_elements.get_Enhanced_Open_Authentication())
            sleep(10)

            self.utils.print_info("Enable Transition Mode for 2.4Ghz and 5Ghz")
            self.auto_actions.click(self.np_web_elements.get_OWE_Transition_mode())

            self.utils.print_info("Click on Save Button")
            self.auto_actions.click(self.np_web_elements.get_save_enhanced_open_ssid())
            sleep(3)
            return 1

        else:
            return -1

    def enable_mgmt_option_http_redirect(self, nw_policy, mgmt_option_name):
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
        self.auto_actions.click(self.np_web_elements.get_network_policy_additional_settings_tab())
        sleep(2)

        self.utils.print_info("Clicking on Management Options")
        self.auto_actions.click(self.np_web_elements.get_network_policy_management_options())
        sleep(5)

        self.utils.print_info("Enabling Management Option")
        self.auto_actions.click(self.np_web_elements.enable_management_options_button())
        sleep(2)

        self.utils.print_info("Entering the name of Management Option")
        self.auto_actions.send_keys(self.np_web_elements.management_option_name_textfield(), mgmt_option_name)
        sleep(2)

        self.utils.print_info("Enabling HTTP Re-direct Option")
        self.auto_actions.click(self.np_web_elements.enable_legacy_http_redirect_checkbox())
        sleep(5)

        self.utils.print_info("Saving Management Option")
        self.auto_actions.click(self.np_web_elements.save_management_option_button())
        sleep(2)

        tool_tip_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tip_text)

        if "Managements options were saved successfully." in tool_tip_text:
            return 1
        else:
            return -1