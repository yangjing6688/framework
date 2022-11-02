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
