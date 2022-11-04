from time import sleep
from robot.libraries.BuiltIn import BuiltIn
from extauto.common.Screen import Screen
from extauto.common.Utils import Utils
from extauto.common.AutoActions import AutoActions
from extauto.xiq.flows.common.Navigator import Navigator
import extauto.xiq.flows.common.ToolTipCapture as tool_tip
from extauto.xiq.elements.UserProfileWebElements import UserProfileWebElements
from extauto.xiq.elements.CommonObjectsWebElements import CommonObjectsWebElements
from extauto.common.CommonValidation import CommonValidation

class UserProfile(UserProfileWebElements, CommonObjectsWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.navigator = Navigator()
        self.screen = Screen()
        self.auto_actions = AutoActions()
        self.common_validation = CommonValidation()

    def add_user_profile(self, profile="user004", vlan_name="vlan004", vlan_id="004"):
        """
        - It adds user profile and VLAN
        -Flow: Configure --> Common Objects --> User Profile
           - Keyword Usage:
            - ``Add User Profile       profile=${PROFILE}    vlan_name=${VLAN_NAME}   vlan_id=${VLAN_ID}``

        :param profile : profile name
        :param vlan_name: VLAN name
        :param vlan_id: VLAN id
        :return: 1
        """
        self.navigator.navigate_to_common_object_user_profile()
        sleep(5)
        self.utils.print_info("Clicking on add user profile")
        self.auto_actions.click_reference(self.get_user_profile_add)

        sleep(5)
        self.utils.print_info("Entering the name of the user profile: ", profile)
        self.auto_actions.send_keys(self.get_user_profile_name(), profile)
        self.utils.print_info("Clicking on add VLAN")
        self.auto_actions.click_reference(self.get_user_profile_vlan_add)

        sleep(5)
        self.utils.print_info("Entering the VLAN name: ", vlan_name)
        self.auto_actions.send_keys(self.get_user_profile_vlan_name(), vlan_name)
        self.utils.print_info("Entering the VLAN id: ", vlan_id)
        self.auto_actions.send_keys(self.get_user_profile_vlan_id(), vlan_id)
        self.utils.print_info("Saving the VLAN info")
        self.auto_actions.click_reference(self.get_user_profile_vlan_save)

        sleep(5)
        self.utils.print_info("Saving the user profile")
        self.auto_actions.click_reference(self.get_user_profile_save)
        return 1

    def add_classification_rule_to_user_profile(self, userprofile, vlanid, classificationrule, **kwargs):
        """
        - Add exist classification rule to exist user profile
        -Flow: Configure --> Common Objects --> User Profile
            - Keyword Usage:
             - ``Add Classification Rule to User Profile   ${userprofile}   ${classificationrule}``

        :param userprofile: User Profile Name
        :param vlanid: VLAN ID
        :param classificationrule: Classification Rule Name
        :return: 1 if successfully created else -1
        """
        self.navigator.navigate_to_common_object_user_profile()
        sleep(2)
        if self.get_user_profile_view_all_pages():
            self.utils.print_info("Click Full pages button")
            self.auto_actions.click_reference(self.get_user_profile_view_all_pages)
            sleep(2)

        if rows := self.get_user_profile_grid_rows():
            for row in rows:
                cells = self.get_all_profile_row_cells(row)
                for cell in cells:
                    if userprofile.lower().strip() == cell.text.lower().strip():
                        self.utils.print_info("Selecting " + cell.text + " user profile.")
                        self.auto_actions.click(self.get_user_profile_row_href(cell))
                        self.utils.print_info("click user_profile vlan edit button.")
                        self.auto_actions.click_reference(self.get_user_profile_vlan_edit_btn)

                        if not self.get_user_profile_vlan_apply_vlans_to_device_chkbx().is_selected():
                            self.utils.print_info("Check Apply VLANs to devices using classification.")
                            self.auto_actions.click_reference(self.get_user_profile_vlan_apply_vlans_to_device_chkbx)

                        self.utils.print_info("Click add(+) VLAN ID.")
                        self.auto_actions.click_reference(self.get_user_profile_vlan_apply_vlans_to_device_add)
                        self.utils.print_info("Enter VLAN ID: ", vlanid)
                        self.auto_actions.send_keys(self.get_user_profile_vlan_apply_vlans_to_device_vlanid_txtbx(), vlanid)
                        self.utils.print_info("Click add....")
                        self.auto_actions.click_reference(self.get_user_profile_vlan_apply_vlans_to_device_add_btn)
                        self.screen.save_screen_shot()
                        return 1 if self._add_classification_rule_to_exist_vlan(vlanid, classificationrule) else -1

            kwargs['fail_msg'] = "User Profile " + userprofile + " was NOT found"
            self.screen.save_screen_shot()
            self.common_validation.validate(-1, 1, **kwargs)
            return -1
        else:
            kwargs['fail_msg'] = "Unable to gather user profiles"
            self.screen.save_screen_shot()
            self.common_validation.validate(-1, 1, **kwargs)
            return -1

    def _add_classification_rule_to_exist_vlan(self, vlanid, classificationrule):
        """
        - This local keyword add exist classification rule to exist vlan
        :param vlanid: VLAN ID
        :param classificationrule: Classification Rule Name
        :return: 1 if success else -1
        """
        if vlan_rows := self.get_user_profile_vlan_rows():
            for vlan_row in vlan_rows:
                if vlanid.lower() == vlan_row.text.lower():
                    self.utils.print_info("Select a classification rule href.")
                    self.auto_actions.click(self.get_user_profile_vlan_row_href(vlan_row))

                    if rule_rows := self.get_user_profile_vlan_row_rule_rows():
                        for rule_row in rule_rows:
                            if classificationrule in rule_row.text:
                                self.utils.print_info("Select a classification rule name: ", classificationrule)
                                self.auto_actions.click(rule_row)
                                self.screen.save_screen_shot()
                                self.utils.print_info("Click classification rules link button.")
                                self.auto_actions.click_reference(self.get_user_profile_vlan_row_rule_link_btn)
                                self.screen.save_screen_shot()
                                sleep(2)
                                self.utils.print_info("Click save vlan button.")
                                self.auto_actions.click_reference(self.get_user_profile_vlan_save)
                                sleep(3)
                                tool_tp_text = tool_tip.tool_tip_text
                                self.utils.print_info(tool_tp_text)
                                if "VLAN object was saved successfully." not in tool_tp_text:
                                    self.utils.print_info("Unable to Save VLAN")
                                    return -1

                                self.screen.save_screen_shot()
                                self.utils.print_info("Click save user profile button.")
                                self.auto_actions.click_reference(self.get_user_profile_save)
                                sleep(3)
                                tool_tp_text = tool_tip.tool_tip_text
                                self.utils.print_info(tool_tp_text)
                                if "User profile was saved successfully." in tool_tp_text:
                                    sleep(3)
                                    tool_tip.tool_tip_text = []
                                    return 1
                                else:
                                    self.utils.print_info("Unable to Save User Profile")
                                    return -1
                        self.utils.print_info("classification rule " + classificationrule + " was NOT found")
                        self.screen.save_screen_shot()
                        return -1
                    else:
                        self.utils.print_info("Unable to gather classification rules.")
                        self.screen.save_screen_shot()
                        return -1

            self.utils.print_info("VLAN ID " + vlanid + " was NOT found")
            self.screen.save_screen_shot()
            return -1
        else:
            self.utils.print_info("Unable to gather VLAN ID.")
            self.screen.save_screen_shot()
            return -1

    def apply_different_user_profile_to_various_clients(self, ssidName, **userprofile):
        """
        - Add user profile, and VLAN with assignment rules to exist ssid name and exist assignment rules
        -Flow: Configure --> Common Objects --> SSIDs
           - Keyword Usage:
            - ``Apply Different User Profile to Various Clients   ${ssid}   &{upserprofile}``

        :param ssidName: SSID Name
        :param upserprofileName: dict{profile_name, vlan_name, vlan_id, assignment_rule}
        :return: 1 if successfully created else -1
        """
        profileName = userprofile.get('profile_name'   , 'None')
        vlanName    = userprofile.get('vlan_name'      , 'None')
        vlanId      = userprofile.get('vlan_id'        , 'None')
        assignRule  = userprofile.get('assignment_rule', 'None')

        if profileName == None and vlanName == None and vlanId == None and assignRule == None:
            userprofile['fail_msg'] = 'Missing one of paramenters info. in dictionary: dict{profile_name, vlan_name, vlan_id, assignment_rule}'
            self.common_validation.failed(**userprofile)
            return -1

        self.navigator.navigate_to_ssids()
        if self.get_paze_size_element():
            self.utils.print_info("Click on full page view")
            self.auto_actions.click_reference(self.get_paze_size_element)
            sleep(3)

        if rows := self.get_common_object_grid_rows():
            for row in rows:
                if cell := self.get_common_object_grid_row_cells(row):
                    if cell.text == ssidName:
                        self.utils.print_info("Select SSID Name: ", cell.text)
                        self.auto_actions.click(self.get_common_object_grid_row_cells(row, 'dgrid-selector'))
                        sleep(2)
                        self.screen.save_screen_shot()
                        self.utils.print_info("Click on edit button")
                        self.auto_actions.click_reference(self.get_common_object_edit_button)
                        sleep(2)
                        if not self._edit_ssid_to_apply_different_user_profile(profileName, vlanName, vlanId, assignRule):
                            userprofile['fail_msg'] = "Unable edit VLAN"
                            self.screen.save_screen_shot()
                            self.common_validation.failed(**userprofile)
                            return -1

                        sleep(2)
                        self.utils.print_info("Saving the SSID")
                        self.auto_actions.click_reference(self.get_user_profile_save)
                        sleep(3)
                        tool_tp_text = tool_tip.tool_tip_text
                        self.utils.print_info(tool_tp_text)
                        if 'SSID was saved successfully.' in tool_tp_text:
                            sleep(3)
                            tool_tip.tool_tip_text = []
                            userprofile['pass_msg'] = "SSID was saved successfully."
                            self.common_validation.passed(**userprofile)
                            return 1
                        else:
                            userprofile['fail_msg'] = "Unable to save SSID"
                            self.screen.save_screen_shot()
                            self.common_validation.failed(**userprofile)
                            return -1
            userprofile['fail_msg'] = "SSID name " + ssidName + " was NOT found"
            self.screen.save_screen_shot()
            self.common_validation.validate(-1, 1, **userprofile)
            return -1
        else:
            userprofile['fail_msg'] = "Unable to gather SSID."
            self.screen.save_screen_shot()
            self.common_validation.validate(-1, 1, **userprofile)
            return -1

    def _edit_ssid_to_apply_different_user_profile(self, profileName, vlanName, vlanId, assignRule):
        """
        - This local keyword edit exist ssid to 'Apply a different user profile to various clients and user groups' checkbox
        :param profileName: VLAN ID
        :param vlanName: Classification Rule Name
        :param profileName: VLAN ID
        :param vlanName: Classification Rule Name
        :return: 1 if success else -1
        """
        if not self.get_apply_different_user_profile_to_various_clients_chkbx().is_selected():
            self.utils.print_info("Enable Apply a different user profile to various clients and user groups.")
            self.auto_actions.click_reference(self.get_apply_different_user_profile_to_various_clients_chkbx)

        self.utils.print_info("Click add(+) user profile.")
        self.auto_actions.click_reference(self.get_different_user_profile_add_user_profile)
        self.utils.print_info("Entering the user profile Name: ", profileName)
        self.auto_actions.send_keys(self.get_user_profile_name(), profileName)
        self.screen.save_screen_shot()
        self.utils.print_info("Clicking on add(+) VLAN.")
        self.auto_actions.click_reference(self.get_different_user_profile_add_user_profile_vlan_addbtn)
        sleep(2)
        self.utils.print_info("Entering the VLAN Name: ", vlanName)
        self.auto_actions.send_keys(self.get_user_profile_vlan_name(), vlanName)
        self.utils.print_info("Entering the VLAN id: ", vlanId)
        self.auto_actions.send_keys(self.get_user_profile_vlan_id(), vlanId)
        self.screen.save_screen_shot()
        self.utils.print_info("Saving the VLAN info")
        self.auto_actions.click_reference(self.get_user_profile_vlan_save)
        sleep(3)
        self.screen.save_screen_shot()
        self.utils.print_info("Saving the user profile")
        self.auto_actions.click_reference(self.get_different_user_profile_add_user_profile_save_btn)
        sleep(3)
        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)
        if "VLAN object was saved successfully." not in tool_tp_text and "User profile was saved successfully." in tool_tp_text:
            self.utils.print_info("Unable to save the VLAN or User Profile")
            self.screen.save_screen_shot()
            return -1

        if vlan_rows := self.get_different_user_profile_vlan_rows():
            for vlan_row in vlan_rows:
                if profileName in vlan_row.text or vlanName in vlan_row.text:
                    self.utils.print_info("Select a user profile assignment rule.")
                    self.auto_actions.click(self.get_user_profile_vlan_row_href(vlan_row))
                    if rule_rows := self.get_user_profile_vlan_rows():
                        for rule_row in rule_rows:
                            if assignRule in rule_row.text:
                                self.utils.print_info("Select a assignment rule name: ", assignRule)
                                self.auto_actions.click(self.get_different_user_profile_vlan_rule_optbox(rule_row))
                                self.screen.save_screen_shot()
                                self.utils.print_info("Click classification rules link button.")
                                self.auto_actions.click_reference(self.get_user_profile_vlan_row_rule_link_btn)
                                return 1
                        self.utils.print_info("Assigment Rule " + assignRule + " was NOT found")
                        self.screen.save_screen_shot()
                        return -1
                    else:
                        self.utils.print_info("Unable to gather Assignment Rules.")
                        self.screen.save_screen_shot()
                        return -1
            self.utils.print_info("User Profile " + profileName + " was NOT found")
            self.screen.save_screen_shot()
            return -1
        else:
            self.utils.print_info("Unable to gather VLAN.")
            self.screen.save_screen_shot()
            return -1