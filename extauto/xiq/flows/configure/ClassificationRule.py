from time import sleep

from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions

import extauto.xiq.flows.common.ToolTipCapture as tool_tip
from extauto.xiq.flows.common.Navigator import Navigator
from extauto.xiq.flows.configure.NetworkPolicy import NetworkPolicy
from extauto.common.CommonValidation import CommonValidation

from extauto.xiq.elements.NetworkPolicyWebElements import NetworkPolicyWebElements
from extauto.xiq.elements.ClassificationRuleWebElements import ClassificationRuleWebElements


class ClassificationRule(object):

    def __init__(self):
        self.utils = Utils()
        self.screen = Screen()
        self.navigator = Navigator()
        self.auto_actions = AutoActions()
        self.network = NetworkPolicy()
        self.np_web_elements = NetworkPolicyWebElements()
        self.classification_rule_web_elements = ClassificationRuleWebElements()
        self.common_validation = CommonValidation()

    def add_classification_rule_with_ccg(self, name, description, match_type_flag, ccg_policy, **kwargs):
        """
        - Flow: Configure --> Common Objects --> Policy --> Classification Rule
        - Create Classification Rule with Cloud Config Group Policy
        - Keyword Usage
        ``Add Classification Rule with CCG      ${RULE_NAME}        ${RULE_DESCRIPTION}    ${match_type}    ${CLOUD_CONFIG_GROUP_POLCIY}``

        :param name: Name of the Classification Rule
        :param description: Description of the Classification Rule
        :param match_type_flag: YES = (default) match based on 'Contains' NOT = match based on "Does Not Contain"
        :param ccg_policy: Cloud Config Group Policy Name
        :return: 1 if created else -1
        """

        self.navigator.navigate_to_classification_rule()
        sleep(3)

        self.utils.print_info(f"Adding Classification Rule with name:{name}")
        self.utils.print_info("Clicking on Classification Rule Add Button")
        self.auto_actions.click_reference(self.classification_rule_web_elements.get_classification_rule_add_button)
        sleep(3)

        self.utils.print_info("Enter the Classification Rule name:{}".format(name))
        self.auto_actions.send_keys(self.classification_rule_web_elements.get_classification_rule_name_text(), name)

        self.utils.print_info("Enter the Classification Rule description:{}".format(description))
        self.auto_actions.send_keys(self.classification_rule_web_elements.get_classification_rule_description_text(), description)

        self.utils.print_info("Clicking on Classification Rule Option Button")
        self.auto_actions.click_reference(self.classification_rule_web_elements.get_classification_option_add_button)
        sleep(3)

        self.utils.print_info("Selecting CCG Option from dropdown")
        classification_rule_option = self.classification_rule_web_elements.get_classification_rule_option()
        if self.auto_actions.select_drop_down_options(classification_rule_option, "Cloud Config Group"):
            self.utils.print_info("Selected CCG Classification Rule")
        else:
            kwargs['fail_msg'] = "Not able to Select CCG Classification Rule"
            self.common_validation.fault(**kwargs)
            return -1
        if match_type_flag.upper() == "YES":
            match_type = "Contains"
        elif match_type_flag.upper() == "NOT":
            match_type = "Does Not Contain"
        else:
            self.utils.print_info(f"The ccg Match Type {match_type_flag} is incorrect, force ccg Match Type as default 'Contains' ")
            match_type = "Contains"
        self.utils.print_info("Selecting CCG Match Type from dropdown")
        self.auto_actions.click_reference(self.classification_rule_web_elements.get_ccg_match_type_dropdown_button)
        match_type_options = self.classification_rule_web_elements.get_ccg_match_type_options()
        if self.auto_actions.select_drop_down_options(match_type_options, match_type):
            self.utils.print_info(f"Selected CCG Match Type {match_type}")
        else:
            kwargs['fail_msg'] = f"Not able to Select CCG Match Type {match_type}"
            self.common_validation.fault(**kwargs)
            return -1

        self.utils.print_info(f"Selecting CCG policy :{ccg_policy}")
        self.utils.wait_till(self.classification_rule_web_elements.get_ccg_policy_select_option)
        self.auto_actions.click_reference(self.classification_rule_web_elements.get_ccg_policy_select_option)
        sleep(2)

        ccg_policy_items = self.classification_rule_web_elements.get_ccg_policy_drop_down_items()
        self.auto_actions.scroll_down()
        sleep(2)

        if self.auto_actions.select_drop_down_options(ccg_policy_items, ccg_policy):
            self.utils.print_info(f"Selected CCG policy from drop down:{ccg_policy}")
        else:
            kwargs['fail_msg'] = "CCG policy is not present in drop down"
            self.common_validation.fault(**kwargs)
            return -1

        self.utils.print_info("Clicking on Continue Button")
        self.auto_actions.click_reference(self.classification_rule_web_elements.get_continue_button)
        sleep(2)

        self.utils.print_info("Saving the Classification Rule")
        self.auto_actions.click_reference(self.classification_rule_web_elements.get_save_rule_button)
        sleep(2)

        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)

        for tip_text in tool_tp_text:
            if "Classification Rule saved successfully" in tip_text:
                sleep(1)
                kwargs['pass_msg'] = f"Classification Rule saved successfully: {tip_text}"
                self.common_validation.passed(**kwargs)
                return 1

        kwargs['fail_msg'] = "Classification Rule not saved"
        self.common_validation.failed(**kwargs)
        return -1

    def add_classification_rule_with_location(self, name, description, location, **kwargs):
        """
        - Flow: Configure --> Common Objects --> Policy --> Classification Rule
        - Create Classification Rule Based on AP Location
        - Keyword Usage
        ``Add Classification Rule with Location      ${RULE_NAME}        ${RULE_DESCRIPTION}        &{LOCATION_OF_AP}``

        :param name: Name of the Classification Rule
        :param description: Description of the Classification Rule
        :param location: Location of the AP
        :return: 1 if created else -1
        """

        self.navigator.navigate_to_classification_rule()
        sleep(3)

        self.utils.print_info(f"Adding Classification Rule with name:{name}")
        self.utils.print_info("Clicking on Classification Rule Add Button")
        self.auto_actions.click_reference(self.classification_rule_web_elements.get_classification_rule_add_button)
        sleep(3)

        self.utils.print_info("Enter the Classification Rule name:{}".format(name))
        self.auto_actions.send_keys(self.classification_rule_web_elements.get_classification_rule_name_text(), name)

        self.utils.print_info("Enter the Classification Rule description:{}".format(description))
        self.auto_actions.send_keys(self.classification_rule_web_elements.get_classification_rule_description_text(), description)

        self.utils.print_info("Clicking on Classification Rule Option Button")
        self.auto_actions.click_reference(self.classification_rule_web_elements.get_classification_option_add_button)
        sleep(3)

        self.utils.print_info("Selecting Device Location Option from dropdown")
        classification_rule_option = self.classification_rule_web_elements.get_classification_rule_option()
        if self.auto_actions.select_drop_down_options(classification_rule_option, "Device Location"):
            self.utils.print_info("Selected Device Location Classification Rule")
        else:
            kwargs['fail_msg'] = "Not able to Select Device Location Classification Rule"
            self.common_validation.fault(**kwargs)
            return -1

        if self._assign_locations_to_classification_rule(location):
            self.utils.print_info("Location got assigned to Classification Rule")
        else:
            kwargs['fail_msg'] = "Location assignment to Classification Rule is not proper"
            self.common_validation.fault(**kwargs)
            return -1

        self.utils.print_info("Saving the Classification Rule")
        self.auto_actions.click_reference(self.classification_rule_web_elements.get_save_rule_button)
        sleep(2)

        tool_tp_text = tool_tip.tool_tip_text

        for tip_text in tool_tp_text:
            if "Classification Rule saved successfully" in tip_text:
                sleep(1)
                kwargs['pass_msg'] = f"Classification Rule saved successfully {tip_text}"
                self.common_validation.passed(**kwargs)
                return 1

        kwargs['fail_msg'] = "Classification Rule not saved"
        self.common_validation.failed(**kwargs)
        return -1

    def add_classification_rule_with_ip(self, name, description, option, ip_object_rule, **kwargs):
        """
        - Flow: Configure --> Common Objects --> Policy --> Classification Rule
        - Create Classification Rule Based on AP's IP , Subnet or Range
        - Keyword Usage
        ``Add Classification Rule with IP      ${RULE_NAME}        ${RULE_DESCRIPTION}    ${Option}     &{IP_RULE_DETAILS}``

        :param name: Name of the Classification Rule
        :param description: Description of the Classification Rule
        :param option: Option for the IP Rule, which can be IP, Subnet or Range
        :param ip_object_rule: IP Rule Details
        :return: 1 if created else -1
        """

        self.navigator.navigate_to_classification_rule()
        sleep(3)

        self.utils.print_info(f"Adding Classification Rule with name:{name}")
        self.utils.print_info("Clicking on Classification Rule Add Button")
        self.auto_actions.click_reference(self.classification_rule_web_elements.get_classification_rule_add_button)
        sleep(3)

        self.utils.print_info("Enter the Classification Rule name:{}".format(name))
        self.auto_actions.send_keys(self.classification_rule_web_elements.get_classification_rule_name_text(), name)

        self.utils.print_info("Enter the Classification Rule description:{}".format(description))
        self.auto_actions.send_keys(
            self.classification_rule_web_elements.get_classification_rule_description_text(), description)

        self.utils.print_info("Clicking on Classification Rule Option Button")
        self.auto_actions.click_reference(self.classification_rule_web_elements.get_classification_option_add_button)
        sleep(3)

        if option == "ip_address":

            self.utils.print_info("Selecting IP Address Option from dropdown")
            classification_rule_option = self.classification_rule_web_elements.get_classification_rule_option()
            if self.auto_actions.select_drop_down_options(classification_rule_option, "IP Address"):
                self.utils.print_info("Selected IP Address Classification Rule")
            else:
                kwargs['fail_msg'] = "Not able to Select Device Location Classification Rule"
                self.common_validation.fault(**kwargs)
                return -1

            if self._assign_ip_address_to_classification_rule(**ip_object_rule):
                self.utils.print_info("IP Address got assigned to Classification Rule")
            else:
                kwargs['fail_msg'] = "IP Address assignment to Classification Rule is not proper"
                self.common_validation.fault(**kwargs)
                return -1

        elif option == "ip_subnet":

            self.utils.print_info("Selecting IP Subnet Option from dropdown")
            classification_rule_option = self.classification_rule_web_elements.get_classification_rule_option()
            if self.auto_actions.select_drop_down_options(classification_rule_option, "IP Subnet"):
                self.utils.print_info("Selected IP Subnet Classification Rule")
            else:
                kwargs['fail_msg'] = "Not able to Select Device Location Classification Rule"
                self.common_validation.fault(**kwargs)
                return -1

            if self._assign_ip_subnet_to_classification_rule(**ip_object_rule):
                self.utils.print_info("IP Subnet got assigned to Classification Rule")
            else:
                kwargs['fail_msg'] = "IP Subnet assignment to Classification Rule is not proper"
                self.common_validation.fault(**kwargs)
                return -1

        elif option == "ip_range":

            self.utils.print_info("Selecting IP Range Option from dropdown")
            classification_rule_option = self.classification_rule_web_elements.get_classification_rule_option()
            if self.auto_actions.select_drop_down_options(classification_rule_option, "IP Range"):
                self.utils.print_info("Selected IP Range Classification Rule")
            else:
                kwargs['fail_msg'] = "Not able to Select IP Range Classification Rule"
                self.common_validation.fault(**kwargs)
                return -1

            if self._assign_ip_range_to_classification_rule(**ip_object_rule):
                self.utils.print_info("IP Range got assigned to Classification Rule")
            else:
                kwargs['fail_msg'] = "IP Range assignment to Classification Rule is not proper"
                self.common_validation.fault(**kwargs)
                return -1

        self.utils.print_info("Saving the Classification Rule")
        self.auto_actions.click_reference(self.classification_rule_web_elements.get_save_rule_button)
        sleep(2)

        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)

        for tip_text in tool_tp_text:
            if "Classification Rule saved successfully" in tip_text:
                sleep(1)
                kwargs['pass_msg'] = "Classification Rule saved successfully!"
                self.common_validation.passed(**kwargs)
                return 1

        kwargs['fail_msg'] = "Classification Rule not saved"
        self.common_validation.failed(**kwargs)
        return -1

    def delete_classification_rules(self, *names, **kwargs):
        """
        - Flow: Configure --> Common Objects --> Policy --> Classification Rule
        - Select Multiple Classification Rule and Click on Delete
        - Keyword Usage
        - ``Delete Classification rules      ${Classification_Rule_NAME}``

        :param names: Name of the Classification Rule
        :return: 1 if deleted else return -1
        """

        self.navigator.navigate_to_classification_rule()
        sleep(3)

        if view_all_pages := self.classification_rule_web_elements.view_all_pages():
            if view_all_pages.is_displayed():
                self.utils.print_info("Click Full pages button")
                self.auto_actions.click_reference(self.classification_rule_web_elements.view_all_pages)
                sleep(2)

        name_select_flag = None
        for name in names:
            if not self._search_multiple_classification_rule(name):
                self.utils.print_info("Classification Rule does not exist in the list")
                continue
            else:
                self._select_multiple_classification_rule(name)
                name_select_flag = True
        sleep(2)

        if name_select_flag:
            self.utils.print_info("Deleting classification rules  ")
            self.auto_actions.click_reference(
                self.classification_rule_web_elements.delete_classification_rule_from_common_object)
            sleep(2)

            self.auto_actions.click_reference(
                self.classification_rule_web_elements.get_confirmation_dialog_yes_button)
            sleep(2)
            kwargs['pass_msg'] = "Successfully deleted classification rules!"
            self.common_validation.passed(**kwargs)
            return 1

        kwargs['fail_msg'] = "Failed to delete classification rules "
        self.common_validation.failed(**kwargs)
        return -1

    def delete_single_classification_rule(self, name, **kwargs):
        """
        - Flow: Configure --> Common Objects --> Policy --> Classification Rule
        - Select Single Classification Rule and Click on Delete
        - Keyword Usage
        - ``Delete Single Classification rule      ${Classification_Rule_NAME}``

         :param name: Name of the Classification Rule
         :return: 1 if created else return -1
         """

        if self.search_classification_rule(name, ignore_failure=True) == -1:
            kwargs['pass_msg'] = "search_classification_rule() failed. Classification rule NOT found"
            self.common_validation.passed(**kwargs)
            return 1

        self.navigator.navigate_to_classification_rule()
        if view_all_pages := self.classification_rule_web_elements.view_all_pages():
            if view_all_pages.is_displayed():
                self.utils.print_info("Click Full pages button")
                self.auto_actions.click_reference(self.classification_rule_web_elements.view_all_pages)
                sleep(2)

        get_all_classification_rule = self.classification_rule_web_elements.view_all_classification_rule()
        for rule in get_all_classification_rule:
            if name in rule.text:
                self.utils.print_info("Selecting classification rule:-  ", name)
                sleep(5)
                self.auto_actions.click(self.classification_rule_web_elements.select_classification_rule_from_common_object(rule))
                sleep(2)

                self.utils.print_info("Deleting classification rule:-  ", name)
                self.auto_actions.click_reference(self.classification_rule_web_elements.delete_classification_rule_from_common_object)
                sleep(2)

                self.auto_actions.click_reference(
                    self.classification_rule_web_elements.get_confirmation_dialog_yes_button)
                sleep(2)

                tool_tp_text = tool_tip.tool_tip_text
                self.utils.print_info(tool_tp_text)

                for tip_text in tool_tp_text:
                    if "Delete Success" in tip_text:
                        sleep(1)
                        kwargs['pass_msg'] = "Successfully deleted single classification rule!"
                        self.common_validation.passed(**kwargs)
                        return 1

                kwargs['fail_msg'] = "Failed to delete single classification rule"
                self.common_validation.failed(**kwargs)
                return -1

    def _assign_locations_to_classification_rule(self, location_config, **kwargs):
        """
        - This is the common method for all type of device
        - This method is used to select location tree node

        :param location_config: Contains details like the organization, Country , Building and Floor of the AP
        :return: True if able to select the Location else return False
        """
        loc_node = location_config.get('loc_node')
        country_node = location_config.get('country_node')
        building_node = location_config.get('building_node')
        floor_node = location_config.get('floor_node')

        self.utils.print_info("click on the assign location button")
        self.auto_actions.click_reference(self.classification_rule_web_elements.get_org_loc_button)
        sleep(1)

        self.utils.print_info("Click on country node open icon")
        country_nodes = self.classification_rule_web_elements.get_node_location()
        if not self._open_location_tree_nodes(country_nodes, country_node):
            kwargs['fail_msg'] = f"Country node {country_node} is not present..."
            self.common_validation.fault(**kwargs)
            return False
        sleep(1)

        self.utils.print_info("Click on location node open icon")
        loc_nodes = self.classification_rule_web_elements.get_node_location()
        if not self._open_location_tree_nodes(loc_nodes, loc_node):
            kwargs['fail_msg'] = f"Location node {loc_node} not present"
            self.common_validation.fault(**kwargs)
            return False
        sleep(1)

        self.utils.print_info("Click on building node open icon")
        build_nodes = self.classification_rule_web_elements.get_node_location()
        if not self._open_location_tree_nodes(build_nodes, building_node):
            kwargs['fail_msg'] = f"Building node {building_node} not present"
            self.common_validation.fault(**kwargs)
            return False
        sleep(1)

        self.utils.print_info("Select the floor to assign device")
        floor_nodes = self.classification_rule_web_elements.get_node_location()
        if not self._assign_floor_to_rule(floor_nodes, floor_node):
            kwargs['fail_msg'] = f"Floor node {floor_node} not present"
            self.common_validation.fault(**kwargs)
            return False
        sleep(1)

        self.utils.print_info("Click on location assign button")
        self.auto_actions.click_reference(self.classification_rule_web_elements.select_loc_assign_button)
        sleep(2)

        return 1

    def _open_location_tree_nodes(self, nodes, search_string):
        """
        - This method is used click on the location and country node open icon button
        :param nodes: nodes web elements
        :param search_string: node name to open the icon
        :return: True
        """
        for node in nodes:
            if search_string in node.text:
                icon = self.classification_rule_web_elements.get_location_node_open_icon(node)
                attr = icon.get_attribute("class")
                if "dijitTreeExpandoOpened" in attr:
                    return True
                else:
                    self.utils.print_info("Click on location node open icon")
                    self.auto_actions.click(self.classification_rule_web_elements.get_location_node_open_icon(node))
                    return True

    def _assign_floor_to_rule(self, floor_els, floor):
        """
        - This method assign floor to the device
        :param floor_els:
        :param floor:
        :return: True if assigned else False
        """
        for el in floor_els:
            if floor in el.text:
                self.utils.print_info(f"Clicking on the floor {floor}")
                self.auto_actions.click(el)
                return True

    def _assign_ip_address_to_classification_rule(self, **ip_address_rule):
        """
        - Assign Ip Address Rule to the ClassificationRule based on AP's IP , Subnet or Range

        :param ip_address_rule: IP Rule Details
        :return: 1 if created else False
        """
        ip_name = ip_address_rule.get('ip_object_name')
        ip_address = ip_address_rule.get('ip')

        self.utils.print_info("click on the ip address add details add button")
        self.auto_actions.click_reference(self.classification_rule_web_elements.get_ip_object_add_button)
        sleep(2)

        self.utils.print_info("Entering Ip Object Name")
        self.auto_actions.send_keys(self.classification_rule_web_elements.get_ip_object_name(), ip_name)

        self.utils.print_info("Entering Ip Object Ip Adress")
        self.auto_actions.send_keys(self.classification_rule_web_elements.get_ip_object_ip()
                                    , ip_address)

        self.utils.print_info("Click on Save IP Button")
        self.auto_actions.click_reference(self.classification_rule_web_elements.get_ip_object_save)
        sleep(2)

        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)

        for tip_text in tool_tp_text:
            if "IP Object was successfully saved" in tip_text:
                self.utils.print_info(f"{tip_text}")
                self.utils.print_info("Click on Continue Button")
                self.auto_actions.click_reference(self.classification_rule_web_elements.get_continue_button)
                sleep(1)
                return 1
        return False

    def _assign_ip_subnet_to_classification_rule(self, **ip_subnet_rule):
        """
        - This is the common method used to asssign IP Subnet Config to Classification Rule

        :param ip_subnet_rule: Provide IP Subnet Information
        :return: 1 is assigned else False
        """
        ip_name = ip_subnet_rule.get('ip_object_name')
        ip_subnet = ip_subnet_rule.get('network')
        ip_mask = ip_subnet_rule.get('mask')

        self.utils.print_info("click on the ip address add details add button")
        self.auto_actions.click_reference(self.classification_rule_web_elements.get_ip_object_add_button)
        sleep(2)

        self.utils.print_info("Entering Ip Object Name")
        self.auto_actions.send_keys(self.classification_rule_web_elements.get_ip_object_name()
                                    , ip_name)

        self.utils.print_info("Entering Ip Object Ip Subnet")
        self.auto_actions.send_keys(self.classification_rule_web_elements.get_ip_object_subnet()
                                    , ip_subnet)

        self.utils.print_info("Entering Ip Object Ip Mask")
        self.auto_actions.send_keys(self.classification_rule_web_elements.get_ip_object_mask()
                                    , ip_mask)

        self.utils.print_info("Click on Save IP Button")
        self.auto_actions.click_reference(self.classification_rule_web_elements.get_ip_object_save)
        sleep(2)

        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)

        for tip_text in tool_tp_text:
            if "IP Object was successfully saved" in tip_text:
                self.utils.print_info("Click on Continue Button")
                self.auto_actions.click_reference(self.classification_rule_web_elements.get_continue_button)
                sleep(1)
                return 1
        return False

    def _assign_ip_range_to_classification_rule(self, **ip_subnet_rule):
        """
        - This is the common method used to asssign IP Range Config to Classification Rule

        :param ip_subnet_rule: Provide IP Subnet Information
        :return: 1 if assigned else False
        """
        ip_name = ip_subnet_rule.get('ip_object_name')
        ip_range_from = ip_subnet_rule.get('ip_range_from')
        ip_range_to = ip_subnet_rule.get('ip_range_to')

        self.utils.print_info("click on the ip address add details add button")
        self.auto_actions.click_reference(self.classification_rule_web_elements.get_ip_object_add_button)
        sleep(2)

        self.utils.print_info("Entering Ip Object Name")
        self.auto_actions.send_keys(self.classification_rule_web_elements.get_ip_object_name()
                                    , ip_name)

        self.utils.print_info("Entering Ip Range From")
        self.auto_actions.send_keys(self.classification_rule_web_elements.get_ip_range_from()
                                    , ip_range_from)

        self.utils.print_info("Entering Ip Range To")
        self.auto_actions.send_keys(self.classification_rule_web_elements.get_ip_range_to()
                                    , ip_range_to)

        self.utils.print_info("Click on Save IP Button")
        self.auto_actions.click_reference(self.classification_rule_web_elements.get_ip_object_save)
        sleep(2)

        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)

        for tip_text in tool_tp_text:
            if "IP Object was successfully saved" in tip_text:
                self.utils.print_info("Click on Continue Button")
                self.auto_actions.click_reference(self.classification_rule_web_elements.get_continue_button)
                sleep(1)
                return 1
        return False

    def add_classification_rule_to_ssid(self, policy_name, ssid_name, classification_rule, **kwargs):
        """

        - Flow: Configure --> NetworkPolicy --> Click Policy --> Wireless Networks -> assign classification rule to ssid
        - Select Classification Rule for the mentioned SSiD
        - Keyword Usage
        ``Add Classification Rule to SSID     ${Network_Policy}        ${SSiD_Name}        ${Classification_Rule}``

        :param policy_name: Name of the Network Policy
        :param ssid_name: Name of the SSiD
        :param classification_rule: Classification Rule to be attached to SSiD
        :return: 1 if success else -1

        """
        self.utils.print_info("Click on Network Policy card view button")
        self.navigator.navigate_to_network_policies_card_view_page()

        if self.network.select_network_policy_in_card_view(policy_name):
            if not self._select_classification_rule_for_ssid(ssid_name, classification_rule):
                sleep(2)
                kwargs['fail_msg'] = f"Not able to add classification rule from {ssid_name}"
                self.common_validation.fault(**kwargs)
                return -1
        sleep(2)

        if not self._verify_classification_rule_for_ssid(ssid_name, classification_rule):
            sleep(2)
            kwargs['fail_msg'] = f"Not able to find classification rule attached to {ssid_name}"
            self.common_validation.fault(**kwargs)
            return -1

        kwargs['pass_msg'] = "Successfully added classification rule to ssid"
        self.common_validation.passed(**kwargs)
        return 1

    def check_classification_rule_to_ssid(self, policy_name, ssid_name, classification_rule, **kwargs):
        """

        - Flow: Configure --> NetworkPolicy --> Click Policy --> Wireless Networks -> Check classification rule to ssid
        - This Method Verifies if the Correct Classification Rule is attached to the SSiD
        - Keyword Usage
        ``Check Classification Rule to SSID     ${Network_Policy}        ${SSiD_Name}        ${Classification_Rule}``

        :param policy_name: Name of the Network Policy
        :param ssid_name: Name of the SSiD
        :param classification_rule: Classification Rule to be attached to SSiD
        :return: 1 if correct classification Rule attached else -1

        """
        self.utils.print_info("Click on Network Policy card view button")
        self.navigator.navigate_to_network_policies_card_view_page()

        if self.network.select_network_policy_in_card_view(policy_name):
            sleep(2)
            if not self._verify_classification_rule_for_ssid(ssid_name, classification_rule):
                sleep(2)
                kwargs['fail_msg'] = f"Not able to find classification rule attached to {ssid_name}"
                self.common_validation.failed(**kwargs)
                return -1

        kwargs['pass_msg'] = "Correct classification Rule attached to ssid!"
        self.common_validation.passed(**kwargs)
        return 1

    def remove_classification_rule_from_ssid(self, policy_name, ssid_name, classification_rule, **kwargs):
        """

        - Flow: Configure --> NetworkPolicy --> Click Policy --> Wireless Networks -> remove classification rule to ssid
        - Remove Classification Rule for the mentioned SSiD
        - Keyword Usage
        ``Remove Classification Rule From SSID     ${Network_Policy}        ${SSiD_Name}        ${Classification_Rule}``

        :param policy_name: Name of the Network Policy
        :param ssid_name: Name of the SSiD
        :param classification_rule: Classification Rule to be attached to SSiD
        :return: 1 if success else -1

        """
        self.utils.print_info("Click on Network Policy card view button")
        self.navigator.navigate_to_network_policies_card_view_page()

        if self.network.select_network_policy_in_card_view(policy_name):
            if not self._delete_classification_rule_from_ssid(ssid_name, classification_rule):
                sleep(2)
                kwargs['fail_msg'] = f"Not able to remove classification rule from {ssid_name}"
                self.common_validation.fault(**kwargs)
                return -1
        sleep(2)

        if self._verify_classification_rule_for_ssid(ssid_name, classification_rule):
            sleep(2)
            kwargs['fail_msg'] = f"Not able to find classification rule attached to {ssid_name}"
            self.common_validation.fault(**kwargs)
            return -1

        kwargs['pass_msg'] = "Removed classification Rule from to ssid!"
        self.common_validation.passed(**kwargs)
        return 1

    def _select_classification_rule_for_ssid(self, ssid, classification_rule):
        """
        - This method is used to select the correct classification rule from list of rules to SSiD

        :param ssid: SSID Name
        :param classification_rule: Name of the Classification Rule
        :return: 1 if success else return False
        """
        self.utils.print_info("Searching SSID: ", ssid)
        self.auto_actions.click_reference(self.np_web_elements.get_network_policy_wireless_networks_tab)
        sleep(5)

        if not self.classification_rule_web_elements.enable_classification_rule().is_selected():
            self.utils.print_info("Enabling Assign SSIDs using Classification Rules")
            self.auto_actions.click_reference(self.classification_rule_web_elements.enable_classification_rule)
            sleep(3)

        grid_rows = self.np_web_elements.get_network_policy_wireless_networks_grid_rows()
        for row in grid_rows:
            if ssid in row.text:
                self.utils.print_info("Found SSID: ", ssid)
                self.auto_actions.click(self.classification_rule_web_elements.select_classification_rule(row))
                sleep(3)

                if view_all_pages := self.classification_rule_web_elements.view_all_pages():
                    if view_all_pages.is_displayed():
                        self.utils.print_info("Click Full pages button")
                        self.auto_actions.click_reference(self.classification_rule_web_elements.view_all_pages)
                        sleep(2)

                classification_rule_all = self.classification_rule_web_elements.get_all_classification_rule()
                self.auto_actions.select_drop_down_options(classification_rule_all,classification_rule)
                sleep(1)

                self.auto_actions.click_reference(self.classification_rule_web_elements.get_link_button)
                sleep(1)

                self.auto_actions.click_reference(self.classification_rule_web_elements.get_next_button)
                return 1
        return False

    def _verify_classification_rule_for_ssid(self, ssid, classification_rule):
        """
        - This method is used to Verify the correct classification rule from list of rules to SSiD

        :param ssid: SSID Name
        :param classification_rule: Name of the Classification Rule
        :return: 1 if success else return False
        """
        self.utils.print_info("Searching SSID: ", ssid)
        self.auto_actions.click_reference(self.np_web_elements.get_network_policy_wireless_networks_tab)
        sleep(5)

        grid_rows = self.np_web_elements.get_network_policy_wireless_networks_grid_rows()
        for row in grid_rows:
            if ssid in row.text:
                self.utils.print_info("Found SSID: ", ssid)

                classification_rules_data = self.classification_rule_web_elements.get_classification_rule(row)
                for classification_rule_data in classification_rules_data:
                    if classification_rule in classification_rule_data.text:
                        self.utils.print_info(f"Found classification rule {classification_rule} attached to ssid {ssid}")
                        return 1
                return False

    def _delete_classification_rule_from_ssid(self, ssid, classification_rule):
        """
        - This method is used to Delete the correct classification rule from list of rules to SSiD

        :param ssid: SSID Name
        :param classification_rule: Name of the Classification Rule
        :return: 1 if success else return False
        """
        self.utils.print_info("Searching SSID: ", ssid)
        self.auto_actions.click_reference(self.np_web_elements.get_network_policy_wireless_networks_tab)
        sleep(5)

        grid_rows = self.np_web_elements.get_network_policy_wireless_networks_grid_rows()
        for row in grid_rows:
            if ssid in row.text:
                self.utils.print_info("Found SSID: ", ssid)
                self.auto_actions.click(self.classification_rule_web_elements.delete_classification_rule_from_ssid(row))
                sleep(2)

                self.auto_actions.click_reference(self.classification_rule_web_elements.get_confirmation_dialog_yes_button)
                return 1
        return False

    def search_classification_rule(self, name, **kwargs):
        """
        - Flow: Configure --> Common Objects --> Policy --> Classification Rule
        - Search Single Classification Rule
        - Keyword Usage
        - ``Search Classification rule      ${Classification_Rule_NAME}``

         :param name: Name of the Classification Rule
         :return: 1 if found else return -1
         """
        self.navigator.navigate_to_classification_rule()
        sleep(3)

        if view_all_pages := self.classification_rule_web_elements.view_all_pages():
            if view_all_pages.is_displayed():
                self.utils.print_info("Click Full pages button")
                self.auto_actions.click_reference(self.classification_rule_web_elements.view_all_pages)
                sleep(2)

        get_all_classification_rule = self.classification_rule_web_elements.view_all_classification_rule()
        for rule in get_all_classification_rule:
            if name in rule.text:
                sleep(5)
                kwargs['pass_msg'] = f"Found classification rule: {name}"
                self.common_validation.passed(**kwargs)
                return 1

        kwargs['fail_msg'] = "Classification rule NOT found"
        self.common_validation.failed(**kwargs)
        return -1

    def _search_multiple_classification_rule(self, name):
        """
        - Flow: Configure --> Common Objects --> Policy --> Classification Rule
        - Search Single Classification Rule

         :param name: Name of the Classification Rule
         :return: 1 if found else return False
         """

        get_all_classification_rule = self.classification_rule_web_elements.view_all_classification_rule()
        for rule in get_all_classification_rule:
            if name in rule.text:
                sleep(5)
                self.utils.print_info(f"Found classification rule: {name}")
                return 1
        return False

    def select_classification_rule(self, name, **kwargs):
        """
        - Flow: Configure --> Common Objects --> Policy --> Classification Rule
        - Select Single Classification Rule
        - Keyword Usage
        - ``Select Classification rule      ${Classification_Rule_NAME}``

         :param name: Name of the Classification Rule
         :return: 1 if able to select else return -1
         """
        self.navigator.navigate_to_classification_rule()
        sleep(3)

        if view_all_pages := self.classification_rule_web_elements.view_all_pages():
            if view_all_pages.is_displayed():
                self.utils.print_info("Click Full pages button")
                self.auto_actions.click_reference(self.classification_rule_web_elements.view_all_pages)
                sleep(2)

        get_all_classification_rule = self.classification_rule_web_elements.view_all_classification_rule()
        for rule in get_all_classification_rule:
            if name in rule.text:
                sleep(2)
                self.auto_actions.click(self.classification_rule_web_elements.
                                        select_classification_rule_from_common_object(rule))
                sleep(2)
                kwargs['pass_msg'] = f"Selected classification rule: {name}"
                self.common_validation.passed(**kwargs)
                return 1

        kwargs['fail_msg'] = "Failed to select classification rule"
        self.common_validation.failed(**kwargs)
        return -1

    def _select_multiple_classification_rule(self, name):
        """
        - Flow: Configure --> Common Objects --> Policy --> Classification Rule
        - Select multiple Classification Rule

         :param name: Name of the Classification Rule
         :return: 1 if able to select else return False
         """
        get_all_classification_rule = self.classification_rule_web_elements.view_all_classification_rule()
        for rule in get_all_classification_rule:
            if name in rule.text:
                sleep(2)
                self.auto_actions.click(self.classification_rule_web_elements.
                                        select_classification_rule_from_common_object(rule))
                sleep(2)
                return 1
        return False