from time import sleep
from robot.libraries.BuiltIn import BuiltIn
from extauto.common.Screen import Screen
from extauto.common.Utils import Utils
from extauto.common.AutoActions import AutoActions
from extauto.xiq.flows.common.Navigator import Navigator
import extauto.xiq.flows.common.ToolTipCapture as tool_tip
from extauto.xiq.elements.UserProfileWebElements import UserProfileWebElements


class UserProfile(UserProfileWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.navigator = Navigator()
        self.screen = Screen()
        self.auto_actions = AutoActions()

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
        self.auto_actions.click(self.get_user_profile_add())

        sleep(5)
        self.utils.print_info("Entering the name of the user profile: ", profile)
        self.auto_actions.send_keys(self.get_user_profile_name(), profile)
        self.utils.print_info("Clicking on add VLAN")
        self.auto_actions.click(self.get_user_profile_vlan_add())

        sleep(5)
        self.utils.print_info("Entering the VLAN name: ", vlan_name)
        self.auto_actions.send_keys(self.get_user_profile_vlan_name(), vlan_name)
        self.utils.print_info("Entering the VLAN id: ", vlan_id)
        self.auto_actions.send_keys(self.get_user_profile_vlan_id(), vlan_id)
        self.utils.print_info("Saving the VLAN info")
        self.auto_actions.click(self.get_user_profile_vlan_save())

        sleep(5)
        self.utils.print_info("Saving the user profile")
        self.auto_actions.click(self.get_user_profile_save())
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
        profile_rows = self.get_user_profile_grid_rows()
        profile_was_located = False
        if profile_rows:
            self.utils.print_info("Checking profile list to see if " + profile + " is in the list")
            for row in profile_rows:
                self.utils.print_info(row.text)
                if profile.lower().strip() == row.text.lower().strip():
                    self.utils.print_info("Profile " + profile + " found")
                    profile_was_located = True
                    self.utils.print_info("Selecting the row")
                    row_elements = self.get_all_profile_row_cells(row)
                    check_box = row_elements[0]
                    if check_box:
                        self.auto_actions.click(check_box)
                        self.utils.print_info("Clicking on the delete button")
                        delete_button = self.get_user_profile_delete()
                        if delete_button:
                            self.auto_actions.click(delete_button)
                            sleep(5)
                            self.utils.print_info("Clicking yes on the confirm delete popup")
                            confirm_yes = self.get_user_profile_confirm_delete_yes()
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
