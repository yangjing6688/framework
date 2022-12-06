from time import sleep
import re
from robot.libraries.BuiltIn import BuiltIn
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
import extauto.xiq.flows.common.ToolTipCapture as tool_tip
from extauto.xiq.flows.manage.Tools import Tools
from extauto.xiq.flows.common.Navigator import Navigator
from extauto.xiq.flows.manage.Devices import Devices
from extauto.xiq.elements.DeviceUpdate import DeviceUpdate
from extauto.xiq.elements.DevicesWebElements import DevicesWebElements
from extauto.xiq.elements.CloudConfigGroupWebElements import CloudConfigGroupWebElements
from extauto.xiq.elements.ClassificationRuleWebElements import ClassificationRuleWebElements
from extauto.common.CommonValidation import CommonValidation


class CloudConfigGroup(object):

    def __init__(self):
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.navigator = Navigator()
        self.device = Devices()
        self.devices_web_elements = DevicesWebElements()
        self.device_update_web_elements = DeviceUpdate()
        self.screen = Screen()
        self.tools = Tools()
        self.robot_built_in = BuiltIn()
        self.ccg_web_elements = CloudConfigGroupWebElements()
        self.classification_rule_web_elements = ClassificationRuleWebElements()
        self.common_validation = CommonValidation()

    def _select_ccg_policy(self, policy_name, option):
        """
        This Keyword is used to select ccg policy from Manage --> Devices --> Select AP --> Actions --> Add to Cloud Config Group
        Select CCG Policy from the list
        :param policy_name: CCG Policy Name
        :param option: Cancel/Continue based on the requirement
        :return: 1 if CCG policy is selected else return False
        """
        self.utils.print_info("Click on actions button")
        self.auto_actions.click_reference(self.devices_web_elements.get_manage_device_actions_button)
        sleep(3)

        self.utils.print_info("Click on Add CCG policy action")
        self.auto_actions.click_reference(self.ccg_web_elements.get_actions_add_ccg_policy)
        sleep(4)

        self.utils.print_info("Click on CCG Select policy drop down")
        self.auto_actions.click_reference(self.ccg_web_elements.get_ccg_policy_dropdown)
        sleep(5)

        self.utils.print_info("Reading all CCG policy items")
        ccg_policy_items = self.ccg_web_elements.get_actions_ccg_policy_drop_down_items()
        self.auto_actions.scroll_down()
        sleep(2)

        if self.auto_actions.select_drop_down_options(ccg_policy_items, policy_name):
            self.utils.print_info(f"Selected CCG policy from drop down:{policy_name}")
        else:
            self.utils.print_info("CCG policy is not present in drop down")
            return False

        self.screen.save_screen_shot()
        sleep(5)

        if option == "Cancel":
            self.auto_actions.click_reference(self.ccg_web_elements.get_actions_ccg_policy_cancel_button)
            sleep(5)
            self.utils.print_info("Click on cancel button")
            return 1

        self.auto_actions.click_reference(self.ccg_web_elements.get_actions_ccg_policy_contimue_button)
        sleep(5)
        return 1

    def assign_cloud_config_group(self, policy_name=None, update_method="Delta", option="Continue", *ap_serials, **kwargs):
        """
        - By default this keyword do delta config push
        - Go To MANAGE-->Devices-->Select AP row  to apply the CCG policy
        - Actions-->Add to Cloud Config group -->Select the CCG policy to assign
        - select AP-->Continue
        - Keyword Usage:
        - ``assign cloud config group       ${CCG_NAME}        ${Update_method}       ${Option}      ${AP_SERIAL}``

        :param policy_name: name of the CCG Policy
        :param update_method: Perform Complete update or delta update
        :param option: Continue/Cancel assign CCG Policy to AP
        :return: 1 if policy is updated else -1
        """
        self.utils.print_info("Navigate to Manage-->Devices")
        self.navigator.navigate_to_devices()
        sleep(5)

        for ap_serial in ap_serials:
            self.utils.print_info("Select row for ap with serial",ap_serial)
            if not self.device.select_device(ap_serial):
                kwargs['fail_msg'] = f"assign_cloud_config_group() failed. AP {ap_serial} is not present in the grid"
                self.common_validation.failed(**kwargs)
                return -1
        sleep(2)

        if not self._select_ccg_policy(policy_name, option):
            kwargs['fail_msg'] = f"assign_cloud_config_group() failed. CCG {policy_name} is not present in the CCG List"
            self.common_validation.failed(**kwargs)
            return -1
        sleep(5)

        if option == "Continue":
            for ap_serial in ap_serials:
                self.utils.print_info("Select row for ap with serial", ap_serial)
                if not self.device.select_device(ap_serial):
                    kwargs['fail_msg'] = f"assign_cloud_config_group() failed. AP {ap_serial} is not present in the grid"
                    self.common_validation.failed(**kwargs)
                    return -1
                sleep(2)

            sleep(2)
            self.device._update_network_policy(update_method)

        for ap_serial in ap_serials:
            if option == "Continue":
                if self._check_update_ccg_policy_status(policy_name, ap_serial) == -1:
                    kwargs['fail_msg'] = f"assign_cloud_config_group() failed. CCG Policy update not proper"
                    self.common_validation.failed(**kwargs)
                    return -1

            elif option == "Cancel":
                if self._check_update_ccg_policy_status(policy_name, ap_serial) == 1:
                    kwargs['fail_msg'] = f"assign_cloud_config_group() failed. CCG Policy update not proper"
                    self.common_validation.failed(**kwargs)
                    return -1

        kwargs['pass_msg'] = "CCG Policy is updated"
        self.common_validation.passed(**kwargs)
        return 1

    def _check_update_ccg_policy_status(self, policy_name, device_serial, **kwargs):
        """
        - This keyword is used to check the cloud config policy applied status to the device
        - It will poll the "update status" every 30 seconds to get the status of the ccg policy applied
        - Assuming that config push will take the maximum five minutes,

        :param policy_name: cloud config group name
        :param device_serial: device serial number to check the config push status
        :return: 1 if config push success else -1
        """
        self.device.column_picker_select("Cloud Config Groups")

        retry_count = 0
        max_config_push_wait = self.robot_built_in.get_variable_value("${MAX_CONFIG_PUSH_TIME}")
        while True:
            self.utils.print_info(f"Time elapsed for device update:{retry_count} seconds")
            device_update_status = self.device.get_device_updated_status(device_serial)
            if re.search(r'\d+-\d+-\d+', device_update_status):
                break
            elif retry_count >= int(max_config_push_wait):
                kwargs['fail_msg'] = f"_check_update_ccg_policy_status() failed." \
                                     f"Config push to AP taking more than {max_config_push_wait} seconds"
                self.common_validation.failed(**kwargs)
                return -1
            sleep(30)
            retry_count += 30

        ccg_members = self.device_ccg_members(device_serial)
        if policy_name in ccg_members:
            self.utils.print_info(f"CCG Group {policy_name} got configured to AP with serial :{device_serial}")
            return 1

        self.utils.print_info(f"CCG Group {policy_name} did not get configured to AP with serial :{device_serial}")
        return -1

    def device_ccg_members(self, device_serial, **kwargs):
        """
        This keyword is used to get the list of CLoud Config Groups that the AP is member of
        - Keyword Usage:
        - ``Device CCG Members     ${DEVICE_SERIAL}``
        :param device_serial: serial_number of the AP
        :return: List of Cloud Config Groups that the AP is attached to, else -1
        """
        device_row = self.device.get_device_row(device_serial)
        sleep(3)

        if view_arrow := self.ccg_web_elements.get_ccg_members_arrow(device_row):
            if view_arrow.is_displayed():
                self.utils.print_info("Click on CCG arrow to display all CCG Members")
                self.auto_actions.click(self.ccg_web_elements.get_ccg_members_arrow(device_row))
                sleep(3)
                self.utils.print_info(f"Getting all the CCG Groups for AP serial :{device_serial}")
                ccg_members = self.ccg_web_elements.get_ccg_member_of_ap(device_row)
                self.utils.print_info(f"AP is member of the following CCG Groups :{ccg_members.text}")
        else:
            self.utils.print_info(f"Getting all the CCG Groups for AP serial :{device_serial}")
            ccg_members = self.ccg_web_elements.get_ccg_members_of_ap(device_row)
            self.utils.print_info(f"AP is member of the following CCG Groups :{ccg_members.text}")

        if ccg_members:
            ccg_member = ccg_members.text.split(",")
            ccg_members = [member.strip() for member in ccg_member]
            kwargs['pass_msg'] = f"AP is member of the following CCG Groups: {ccg_members}"
            self.common_validation.passed(**kwargs)
            return ccg_members
        else:
            kwargs['fail_msg'] = "device_ccg_members() failed. AP is not a member of any CCG Group"
            self.common_validation.failed(**kwargs)
            return -1

    def add_cloud_config_group(self, policy, description, *ap_serials, **kwargs):
        """
        - Flow: Configure --> Common Objects --> Policy --> Cloud Config Group
        - Create Cloud Config Group and include APs to the group
        - Same Keyword can be used to add single or multiple APs to the CCG Group
        - Keyword Usage
        - ``Add Cloud Config Group      ${CCG_NAME}        ${CCG_DESCRIPTION}        ${AP_SERIAL}``

        :param policy: Name of the CCG Group
        :param description: Description of the Group
        :param ap_serials:[List] Single or multiple APs who are members of the Group
        :return: 1 if created else -1, -2, -3 depending on the error received.
        """
        self.utils.print_info(f"AP {ap_serials} to be added to CCG Group {policy}")
        self.navigator.navigate_to_cloud_config_groups()
        sleep(2)

        self.utils.print_info(f"Adding CCG Group with name:{policy}")
        self.utils.print_info("Clicking on CCG Group Add Button")
        self.auto_actions.click_reference(self.ccg_web_elements.get_ccg_add_button)
        sleep(3)

        self.utils.print_info("Enter the policy name:{}".format(policy))
        self.auto_actions.send_keys(self.ccg_web_elements.get_ccg_name_text(), policy)

        self.utils.print_info("Enter the policy description:{}".format(description))
        self.auto_actions.send_keys(self.ccg_web_elements.get_ccg_description_text(), description)

        for ap_serial in ap_serials:
            if not self.select_ap_for_ccg(ap_serial):
                kwargs['fail_msg'] = f"add_cloud_config_group() failed. AP {ap_serial} is not present in the grid"
                self.common_validation.failed(**kwargs)

        sleep(2)

        self.utils.print_info("Clicking on CCG Group Save Button")
        self.auto_actions.click_reference(self.ccg_web_elements.get_ccg_save_button)
        sleep(3)

        if self.ccg_web_elements.get_form_error_text():
            if "This field is required" in self.ccg_web_elements.get_form_error_text().text:
                self.auto_actions.click_reference(self.ccg_web_elements.get_ccg_cancel_button)
                kwargs['fail_msg'] = "add_cloud_config_group() failed. Entering CCG Name is Mandatory. " \
                                     "Clicked on CCG Group Cancel Button"
                self.common_validation.validate(-2,- 2, **kwargs)
                return -2


        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)

        for tip_text in tool_tp_text:
            if "already exists" in tip_text:
                sleep(1)
                kwargs['fail_msg'] = f"add_cloud_config_group() failed. {tip_text}"
                self.common_validation.failed(**kwargs)

        if self.search_ccg_group_from_common_object(policy):
            ccg_group_members = self.get_ccg_group_members(policy)
            for ap_serial in ap_serials:
                if ap_serial not in ccg_group_members:
                    kwargs['fail_msg'] = f"add_cloud_config_group() failed. {ap_serial} not in {ccg_group_members}"
                    self.common_validation.failed(**kwargs)

            kwargs['pass_msg'] = "Created Cloud Config Group and included APs to the group."
            self.common_validation.validate(1, 1, **kwargs)
            return 1

        kwargs['fail_msg'] = "add_cloud_config_group() failed. " \
                             "Unable to Create Cloud Config Group and to include APs to the group. "
        self.common_validation.failed(**kwargs)


    def add_cloud_config_group_from_manage(self, policy, description, *ap_serials, **kwargs):
        """
        - Flow: Manage --> Devices --> Select AP -> Actions -> Add to CLoud Config Group
        - Create Cloud Config Group and include APs to the group
        - Keyword Usage
        - ``Add Cloud Config Group From Manage     ${CCG_NAME}        ${CCG_DESCRIPTION}        ${AP_SERIAL}``

        :param policy: Name of the CCG Group
        :param description: Description of the Group
        :param ap_serials: Serial number of the AP who is member of the Group
        :return: 1 if created else -1
        """
        self.utils.print_info("Navigate to Manage-->Devices")
        self.navigator.navigate_to_devices()
        sleep(5)

        self.utils.print_info("Select ap row")
        for ap_serial in ap_serials:
            if not self.device.select_ap(ap_serial):
                kwargs['fail_msg'] = f"add_cloud_config_group_from_manage() failed. " \
                                     f"AP {ap_serial} is not present in the grid"
                self.common_validation.failed(**kwargs)

        sleep(2)

        self.utils.print_info(f"AP {ap_serials} to be added to CCG Group {policy}")
        sleep(2)

        self.utils.print_info("Click on actions button")
        self.auto_actions.click_reference(self.devices_web_elements.get_manage_device_actions_button)
        sleep(3)

        self.utils.print_info("Click on Add CCG policy action")
        self.auto_actions.click_reference(self.ccg_web_elements.get_actions_add_ccg_policy)
        sleep(3)

        self.utils.print_info(f"Adding CCG Group with name:{policy}")
        self.utils.print_info("Clicking on CCG Group Add Button")
        self.auto_actions.click_reference(self.ccg_web_elements.get_actions_add_ccg_button)
        sleep(3)

        self.utils.print_info("Enter the policy name:{}".format(policy))
        self.auto_actions.send_keys(self.ccg_web_elements.get_ccg_name_text(), policy)
        sleep(1)

        self.utils.print_info("Enter the description:{}".format(description))
        self.auto_actions.send_keys(self.ccg_web_elements.get_ccg_description_manage_text(), description)

        # for ap_serial in ap_serials:
        #     if not self.select_ap_for_ccg_manage_page(ap_serial):
        #         self.utils.print_info(f"AP {ap_serial} is not present in the grid")
        #         return -1
        # sleep(2)

        self.utils.print_info("Clicking on CCG Group Save Button")
        self.auto_actions.click_reference(self.ccg_web_elements.get_ccg_save_button)
        sleep(2)

        self.utils.print_info("Clicking on CCG Group Continue Button")
        self.auto_actions.click_reference(self.ccg_web_elements.get_ccg_continue_button)
        sleep(3)

        if ccg_group_members := self.get_ccg_group_members(policy):
            for ap_serial in ap_serials:
                if ap_serial not in ccg_group_members:
                    kwargs['fail_msg'] = f"add_cloud_config_group_from_manage() failed. " \
                                         f"{ap_serial} not in {ccg_group_members}"
                    self.common_validation.failed(**kwargs)

            kwargs['pass_msg'] = "Added Cloud Config Group from manage"
            self.common_validation.passed(**kwargs)
            return 1
        kwargs['fail_msg'] = "add_cloud_config_group_from_manage() failed. Unable to add Cloud Config Group from manage"
        self.common_validation.failed(**kwargs)


    def create_bulk_cloud_config_group(self, policy_name, ap_serial, num, **kwargs):
        """
        - Flow: Configure --> Common Objects --> Policy --> Cloud Config Group
        - Create Cloud Config Group and include AP to the group
        - This Keyword is used to create CCG in bulk.
        - Keyword Usage
        - ``Create Bulk Cloud Config Group      ${CCG_NAME}        ${AP_SERIAL}        ${NUMBER_of_CCG_Policy}``

        :param policy_name: Name of the CCG Group
        :param ap_serial:AP who are members of the Group
        :param num: Number of the CCG Policy to be configured
        :return: 1 if created else -1
        """
        self.navigator.navigate_to_cloud_config_groups()
        sleep(2)

        for i in range(1, int(num) + 1):
            self.utils.print_info(type(i))
            policy = policy_name + "_" + str(i)

            self.utils.print_info(f"Adding CCG Group with name:{policy}")
            self.utils.print_info("Clicking on CCG Group Add Button")
            self.auto_actions.click_reference(self.ccg_web_elements.get_ccg_add_button)
            sleep(3)

            self.utils.print_info("Enter the policy name:{}".format(policy))
            self.auto_actions.send_keys(self.ccg_web_elements.get_ccg_name_text(), policy)

            self.utils.print_info("Enter the policy description:{}".format(policy))
            self.auto_actions.send_keys(self.ccg_web_elements.get_ccg_description_text(), policy)

            if not self.select_ap_for_ccg(ap_serial):
                kwargs['fail_msg'] = f"create_bulk_cloud_config_group() failed. AP {ap_serial} is not present in the grid"
                self.common_validation.failed(**kwargs)

            sleep(2)

            self.utils.print_info("Clicking on CCG Group Save Button")
            self.auto_actions.click_reference(self.ccg_web_elements.get_ccg_save_button)
            sleep(3)

            if self.ccg_web_elements.get_form_error_text():
                if "This field is required" in self.ccg_web_elements.get_form_error_text().text:
                    self.auto_actions.click_reference(self.ccg_web_elements.get_ccg_cancel_button)
                    kwargs['fail_msg'] = "create_bulk_cloud_config_group() failed. Entering CCG Name is Mandatory. " \
                                         "Clicked on CCG Group Cancel Button"
                    self.common_validation.failed(**kwargs)


            tool_tp_text = tool_tip.tool_tip_text
            self.utils.print_info(tool_tp_text)

            for tip_text in tool_tp_text:
                if "already exists" in tip_text:
                    sleep(1)
                    kwargs['fail_msg'] = f"create_bulk_cloud_config_group() failed. {tip_text}"
                    self.common_validation.failed(**kwargs)


            if not self.search_ccg_group_from_common_object(policy):
                kwargs['fail_msg'] = f"create_bulk_cloud_config_group() failed. Didn't find CCG group"
                self.common_validation.failed(**kwargs)


        kwargs['pass_msg'] = "Created bulk Cloud Config Group"
        self.common_validation.passed(**kwargs)


    def edit_cloud_config_group(self, policy, option="add", *ap_serials, **kwargs):
        """
        - Flow: Configure --> Common Objects --> Policy --> Cloud Config Group
        - Select Cloud Config Group and Click on Edit
        - Same Keyword can be used to add/remove single or multiple APs to the CCG Group
        - Keyword Usage
        - ``Edit Cloud Config Group      ${CCG_NAME}        ${Option}        ${AP_SERIAL}``

        :param policy: Name of the CCG Group
        :param option: Whether to add new APs or remove AP from the CCG Group.
        :param ap_serials:[List] Single or multiple APs who are members of the Group
        :return: 1 if created else return -1
        """
        device_hostnames = []
        self.utils.print_info("AP Serial are :- ", ap_serials)
        for ap_serial in ap_serials:
            device_hostname = self.device.get_device_details(ap_serial, 'HOST NAME')
            device_hostnames.append(device_hostname)
            sleep(2)
        self.utils.print_info("Device Hostname :- ", device_hostnames)

        self.navigator.navigate_to_cloud_config_groups()
        sleep(2)

        self.utils.print_info(f"Selecting CCG Group with name:{policy}")
        if not self.select_ccg_group_from_common_object(policy):
            kwargs['fail_msg'] = f"edit_cloud_config_group() failed. Not able to find CCG Group with name:{policy}"
            self.common_validation.failed(**kwargs)

        sleep(3)

        self.utils.print_info("Clicking on CCG Edit Button")
        self.screen.save_screen_shot()
        self.auto_actions.click_reference(self.ccg_web_elements.edit_ccg_button_common_object)
        self.screen.save_screen_shot()
        #import pdb; pdb.set_trace()
        if option == "add":
            for ap_serial in ap_serials:
                if not self.select_ap_for_ccg(ap_serial):
                    kwargs['fail_msg'] = f"edit_cloud_config_group() failed. AP {ap_serial} is not present in the grid"
                    self.common_validation.failed(**kwargs)

        else:
            sleep(2)
            for device_hostname in device_hostnames:
                if not self._remove_device_ccg(device_hostname, policy):
                    kwargs['fail_msg'] = f"edit_cloud_config_group() failed. AP {device_hostname} " \
                                         f"is not present in the grid"
                    self.common_validation.failed(**kwargs)


        sleep(5)

        self.utils.print_info("Clicking on CCG Group Save Button")
        self.auto_actions.click_reference(self.ccg_web_elements.get_ccg_save_button)
        sleep(5)

        if self.search_ccg_group_from_common_object(policy):
            ccg_members = self.get_ccg_group_members(policy)
            if option == "add":
                for ap_serial in ap_serials:
                    if ap_serial not in ccg_members:
                        kwargs['fail_msg'] = f"edit_cloud_config_group() failed. AP {ap_serial} did not " \
                                             f"get added to CCG Group"
                        self.common_validation.failed(**kwargs)

            else:
                for ap_serial in ap_serials:
                    if ap_serial in ccg_members:
                        kwargs['fail_msg'] = f"edit_cloud_config_group() failed. AP {ap_serial} did not " \
                                             f"get removed from CCG Group"
                        self.common_validation.failed(**kwargs)


        else:
            kwargs['fail_msg'] = f"edit_cloud_config_group() failed. CCG Group {policy} is not found in  CCG List"
            self.common_validation.failed(**kwargs)
            return -1

        for ap_serial in ap_serials:
            self.utils.print_info("Navigating to the Device Page")
            self.utils.print_info("Select row for ap with serial", ap_serial)
            self.navigator.navigate_to_devices()
            sleep(5)
            if not self.device.select_device(ap_serial):
                kwargs['fail_msg'] = f"edit_cloud_config_group() failed. AP {ap_serial} is not present in the grid"
                self.common_validation.failed(**kwargs)
                return -1
            sleep(2)

        sleep(2)
        self.device._update_network_policy()
        kwargs['pass_msg'] = "Successfully Selected Cloud Config Group and Edited"
        self.common_validation.passed(**kwargs)
        return 1

    def delete_bulk_cloud_config_group(self, policy_name, num):
        """
        - Flow: Configure --> Common Objects --> Policy --> Cloud Config Group
        - Delete Cloud Config Group
        - This Keyword is used to delete CCG in bulk.
        - Keyword Usage
        - ``Delete Bulk Cloud Config Group      ${CCG_NAME}        ${AP_SERIAL}        ${NUMBER_of_CCG_Policy}``

        :param policy_name: Name of the CCG Group
        :param num: Number of the CCG Policy to be configured
        :return: 1 if created else -1
        """

        self.navigator.navigate_to_cloud_config_groups()

        sleep(2)

        if view_all_pages := self.classification_rule_web_elements.view_all_pages():
            if view_all_pages.is_displayed():
                self.utils.print_info("Click Full pages button")
                self.auto_actions.click_reference(self.classification_rule_web_elements.view_all_pages)
                sleep(2)

        policy_select_flag = None

        for i in range(1, int(num) + 1):
            self.utils.print_info(type(i))
            policy = policy_name + "_" + str(i)
            if not self._search_multiple_ccg_group_from_common_object(policy):
                self.utils.print_info("CCG Group does not exist in the list")
                continue
            else:
                self._select_multiple_ccg_group_from_common_object(policy)
                policy_select_flag = True

        sleep(2)

        if policy_select_flag:
            self.utils.print_info("Clicking on CCG Delete Button")
            self.auto_actions.click_reference(self.ccg_web_elements.delete_ccg_button_common_object)

            self.utils.print_info("Clicking CCG Yes Confirmation Button")
            self.auto_actions.click_reference(self.ccg_web_elements.delete_ccg_yes_confirmation_button)
            sleep(3)
            return 1

    def delete_cloud_config_group(self, policy, **kwargs):
        """
        - Flow: Configure --> Common Objects --> Policy --> Cloud Config Group
        - Select Cloud Config Group and Click on Delete
        - Keyword Usage
        - ``Delete Cloud Config Group      ${CCG_NAME}``

        :param policy: Name of the CCG Group
        :return: 1 if created else return -1
        """

        if not self.select_ccg_group_from_common_object(policy):
            kwargs['fail_msg'] = f"delete_cloud_config_group() failed. Not able to find CCG Group with name:{policy}"
            self.common_validation.validate(-1,-1, **kwargs)
            return -1
        sleep(3)

        self.utils.print_info("Clicking on CCG Delete Button")
        self.auto_actions.click_reference(self.ccg_web_elements.delete_ccg_button_common_object)

        self.utils.print_info("Clicking CCG Yes Confirmation Button")
        self.auto_actions.click_reference(self.ccg_web_elements.delete_ccg_yes_confirmation_button)
        sleep(3)

        if self.search_ccg_group_from_common_object(policy):
            kwargs['fail_msg'] = "delete_cloud_config_group() failed. CCG Still Not Deleted"
            self.common_validation.validate(-1,-1, **kwargs)
            return -1
        else:
            kwargs['pass_msg'] = "CCG Deleted Successfully"
            self.common_validation.validate(1,1, **kwargs)
            return 1

    def delete_cloud_config_groups(self, *policys):
        """
        - Flow: Configure --> Common Objects --> Policy --> Cloud Config Group
        - Select Cloud Config Group and Click on Delete
        - Keyword Usage
        - ``Delete Cloud Config Groups      ${CCG_NAMES}``

        :param policys: Names of the CCG Group
        :return: 1 if created else return -1
        """

        self.navigator.navigate_to_cloud_config_groups()
        sleep(2)

        if view_all_pages := self.classification_rule_web_elements.view_all_pages():
            if view_all_pages.is_displayed():
                self.utils.print_info("Click Full pages button")
                self.auto_actions.click_reference(self.classification_rule_web_elements.view_all_pages)
                sleep(2)

        policy_select_flag = None
        for policy in policys:
            if not self._search_multiple_ccg_group_from_common_object(policy):
                self.utils.print_info("CCG Group does not exist in the list")
                continue
            else:
                self._select_multiple_ccg_group_from_common_object(policy)
                policy_select_flag = True
        sleep(2)

        if policy_select_flag:
            self.utils.print_info("Clicking on CCG Delete Button")
            self.auto_actions.click_reference(self.ccg_web_elements.delete_ccg_button_common_object)

            self.utils.print_info("Clicking CCG Yes Confirmation Button")
            self.auto_actions.click_reference(self.ccg_web_elements.delete_ccg_yes_confirmation_button)
            sleep(3)
            return 1

    def select_ap_for_ccg(self, ap_serial, **kwargs):
        """
        - Selects the AP row marching with AP's Serial Number
        - Keyword USage:
        - ``Select AP For CCG   ${AP_SERIAL}``

        :param ap_serial: AP's Serial Number
        :return: return 1 if AP found and selected else -1
        """
        self.utils.print_info("Selecting Device with serial: ", ap_serial)

        sleep(5)
        rows = self.devices_web_elements.get_grid_rows()
        for row in rows:
            if ap_serial in row.text:
                self.screen.save_screen_shot()
                self.auto_actions.click(self.ccg_web_elements.get_ap_select_checkbox_ccg(row))
                self.screen.save_screen_shot()
                sleep(5)
                kwargs['pass_msg'] = "Found AP Row"
                self.common_validation.passed(**kwargs)
                return 1
        kwargs['fail_msg'] = "select_ap_for_ccg() failed. Didn't Find AP Row"
        self.common_validation.failed(**kwargs)
        return -1

    def select_ap_for_ccg_manage_page(self, ap_serial, **kwargs):
        """
        - Selects the AP row marching with AP's Serial Number
        - Keyword USage:
        - ``Select AP For CCG Manage Page   ${AP_SERIAL}``

        :param ap_serial: AP's Serial Number
        :return: return 1 if AP found and selected else -1
        """
        self.utils.print_info("Selecting Device with serial: ", ap_serial)

        sleep(5)
        rows = self.ccg_web_elements.get_grid_rows()
        for row in rows:
            if ap_serial in row.text:
                self.auto_actions.click(self.ccg_web_elements.get_ap_select_checkbox_ccg(row))
                sleep(2)
                kwargs['pass_msg'] = "Found AP Row"
                self.common_validation.passed(**kwargs)
                return 1
        kwargs['fail_msg'] = "select_ap_for_ccg_manage_page() failed. Didn't Find AP Row"
        self.common_validation.failed(**kwargs)
        return -1

    def _get_device_details_from_CCG_page(self, search_string, return_string):
        """
        This Keyword is used to get Hostname/Serial Number when either of them is provided
        :param search_string: search for AP Hostname/Serial
        :param return_string: return AP Serial/Hostname
        :return: Hostname/Serial
        """
        self.utils.print_info("Selecting Device: ", search_string)

        sleep(5)
        rows = self.devices_web_elements.get_grid_rows()
        for row in rows:
            if search_string in row.text:
                self.utils.print_debug("Found AP Row ")
                sleep(2)
                if return_string == "HOSTNAME":
                    hostname = self.ccg_web_elements.get_ap_hostname(row)
                    self.utils.print_info("Hostname found: ", hostname.text)
                    return hostname.text
                elif return_string == "APSERIAL":
                    serial = self.ccg_web_elements.get_ap_serial(row)
                    self.utils.print_info("Hostname found: ", serial.text)
                    return serial.text

    def _remove_device_ccg(self, device_hostname, policy):
        """
        removes device from CCG Policy
        :param device_hostname: hostname of the AP to be removed
        :param policy: CCG Policy Name
        :return: 1
        """
        hostnames = self.ccg_web_elements.get_ccg_ap_hostname()
        for hostname in hostnames:
            if device_hostname in hostname.text :
                self.auto_actions.click(self.ccg_web_elements.get_ap_remove_from_ccg(hostname))
                return 1

    def search_ccg_group_from_common_object(self, policy, **kwargs):
        """
        - Flow: Configure --> Common Objects --> Policy --> Cloud Config Group
        This keyword Checks if the CCG Policy is available in CCG List
        :param policy: CCG Policy name
        :return: 1 if found else -1
        """

        self.navigator.navigate_to_cloud_config_groups()
        sleep(4)

        if view_all_pages := self.classification_rule_web_elements.view_all_pages():
            if view_all_pages.is_displayed():
                self.utils.print_info("Click Full pages button")
                self.auto_actions.click_reference(self.classification_rule_web_elements.view_all_pages)
                sleep(2)

        self.utils.print_info(f"Searching CCG Group with name:{policy}")
        rows = self.ccg_web_elements.get_ccg_grid_rows()
        for row in rows:
            ccg = self.ccg_web_elements.get_ccg_row_name(row)
            if policy == ccg.text.strip():
                kwargs['pass_msg'] = f"Found CCG Group with name:{policy}"
                self.common_validation.validate(1, 1, **kwargs)
                return 1

        kwargs['fail_msg'] = f"search_ccg_group_from_common_object() failed. Didn't find CCG Group with name: {policy}"
        self.common_validation.validate(-1,- 1, **kwargs)
        return -1

    def _search_multiple_ccg_group_from_common_object(self, policy):
        """
        - Flow: Configure --> Common Objects --> Policy --> Cloud Config Group
        This keyword Checks if the CCG Policy is available in CCG List
        :param policy: CCG Policy name
        :return: 1 if found else -1
        """

        self.utils.print_info(f"Searching CCG Group with name:{policy}")
        rows = self.ccg_web_elements.get_ccg_grid_rows()
        for row in rows:
            ccg = self.ccg_web_elements.get_ccg_row_name(row)
            if policy == ccg.text.strip():
                self.utils.print_debug("Found CCG Group with name:{policy}")
                sleep(2)
                return 1
        return False

    def select_ccg_group_from_common_object(self, policy, **kwargs):
        """
        - Flow: Configure --> Common Objects --> Policy --> Cloud Config Group
        This keyword Selects if the CCG Policy is available in CCG List
        :param policy: CCG Policy name
        :return: 1 if found else False
        """

        self.navigator.navigate_to_cloud_config_groups()
        sleep(2)

        if view_all_pages := self.classification_rule_web_elements.view_all_pages():
            if view_all_pages.is_displayed():
                self.utils.print_info("Click Full pages button")
                self.auto_actions.click_reference(self.classification_rule_web_elements.view_all_pages)
                sleep(2)

        self.utils.print_info(f"Searching CCG Group with name:{policy}")
        rows = self.ccg_web_elements.get_ccg_grid_rows()

        for row in rows:
            ccg = self.ccg_web_elements.get_ccg_row_name(row)
            if policy == ccg.text.strip():
                self.auto_actions.click(self.ccg_web_elements.get_ccg_select_checkbox(row))
                sleep(2)
                kwargs['pass_msg'] = f"Selected CCG Group with name:{policy}"
                self.common_validation.passed(**kwargs)
                return 1

        kwargs['fail_msg'] = f"select_ccg_group_from_common_object() failed. " \
                             f"Didn't find CCG Group with name: {policy}"
        self.common_validation.failed(**kwargs)
        return False

    def _select_multiple_ccg_group_from_common_object(self, policy):
        """
        - Flow: Configure --> Common Objects --> Policy --> Cloud Config Group
        This keyword Selects if the CCG Policy is available in CCG List
        :param policy: CCG Policy name
        :return: 1 if found else -1
        """

        self.utils.print_info(f"Searching CCG Group with name:{policy}")
        rows = self.ccg_web_elements.get_ccg_grid_rows()

        for row in rows:
            ccg = self.ccg_web_elements.get_ccg_row_name(row)
            if policy == ccg.text.strip():
                self.auto_actions.click(self.ccg_web_elements.get_ccg_select_checkbox(row))
                self.utils.print_debug("Found CCG Group with name:{policy}")
                sleep(2)
                return 1
        return False

    def get_ccg_group_members(self, policy, **kwargs):
        """
        This keyword is used to get the list of  APs which are members of the CCG Policy
        - Keyword Usage:
        - ``Get CCG Group Members   ${POLICY_NAME}``
        :param policy: CCG Policy
        :return: List of APs that are member of CCG Policy
        """
        self.navigator.navigate_to_cloud_config_groups()
        sleep(2)

        if view_all_pages := self.classification_rule_web_elements.view_all_pages():
            if view_all_pages.is_displayed():
                self.utils.print_info("Click Full pages button")
                self.auto_actions.click_reference(self.classification_rule_web_elements.view_all_pages)
                sleep(2)

        rows = self.ccg_web_elements.get_ccg_grid_rows()

        for row in rows:
            if policy in row.text:
                self.utils.print_debug(f"Found CCG Group with name:{policy}")
                sleep(2)

                self.utils.print_debug(f"Selecting CCG Group with name:{policy}")
                self.auto_actions.click(self.ccg_web_elements.get_ccg_select_checkbox(row))
                sleep(2)

                self.utils.print_info("Clicking on CCG Edit Button")
                self.auto_actions.click_reference(self.ccg_web_elements.edit_ccg_button_common_object)
                sleep(2)

                get_ccg_members_hostname = self.ccg_web_elements.get_ccg_members_hostname()
                get_ccg_members_hostnames = [member.text.split("\n")[0] for member in get_ccg_members_hostname]
                get_ccg_members_serial_numbers = []
                self.utils.print_info(f"CCG Group members :{policy} are {get_ccg_members_hostnames}")

                sleep(2)
                # self.utils.print_info("Clicking on CCG Group Cancel Button")
                # self.auto_actions.click_reference(self.ccg_web_elements.get_ccg_cancel_button)
                # sleep(5)

                for member in get_ccg_members_hostnames:
                    # device_serial_num = self.device.get_device_details(member, 'SERIAL')
                    device_serial_num = self._get_device_details_from_CCG_page(member, 'APSERIAL')
                    self.utils.print_info(f"AP serial number for :{member} is {device_serial_num}")
                    get_ccg_members_serial_numbers.append(device_serial_num)

                self.utils.print_info("Clicking on CCG Group Cancel Button")
                self.auto_actions.click_reference(self.ccg_web_elements.get_ccg_cancel_button)
                sleep(5)

                kwargs['pass_msg'] = f"CCG Group members :{policy} are {get_ccg_members_serial_numbers}"
                self.common_validation.passed(**kwargs)
                return get_ccg_members_serial_numbers

        kwargs['fail_msg'] = "get_ccg_group_members() failed. " \
                             "Failed to get the list of  APs which are members of the CCG Policy"
        self.common_validation.failed(**kwargs)
        return False
