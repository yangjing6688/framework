from time import sleep
from robot.libraries.BuiltIn import BuiltIn
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions

from extauto.xiq.flows.common.Navigator import Navigator
import extauto.xiq.flows.common.ToolTipCapture as tool_tip
from extauto.xiq.elements.CommonObjectsWebElements import CommonObjectsWebElements
from extauto.xiq.elements.WirelessCWPWebElements import WirelessCWPWebElements
from extauto.xiq.elements.WirelessWebElements import WirelessWebElements
from extauto.xiq.elements.NetworkManagementOptionsElements import NetworkManagementOptionsElements
from extauto.xiq.elements.UserProfileWebElements import UserProfileWebElements
from extauto.xiq.elements.ApplicationsWebElements import ApplicationsWebElements


class Applications(object):

    def __init__(self):
        self.utils = Utils()
        self.screen = Screen()
        self.auto_actions = AutoActions()
        self.navigator = Navigator()
        self.cobj_web_elements = CommonObjectsWebElements()
        self.app_web_elements = ApplicationsWebElements()
        self.cwp_web_elements = WirelessCWPWebElements()
        self.wireless_web_elements = WirelessWebElements()
        self.network_management_options_elements = NetworkManagementOptionsElements()
        self.user_profile_web_elements = UserProfileWebElements()

    def add_custom_applications(self, application_name, group_name):
        """
        - This keyword will create Custom Application under Manage > Applications.
        - Flow: Manage --> Applications --> Manage Applications --> ADD CUSTOM
        - Keyword Usage:
         - ``Add Custom Applications  ${APPLICATION_NAME}  ${GROUP_NAME}``

        :param application_name: Custom application name
        :param group_name: group name
        :return: 1 if success and -1 if fails
        """

        self.utils.print_info("Click on Manage Applications Tab")
        self.auto_actions.click(self.app_web_elements.get_manage_applications())
        sleep(2)

        self.utils.print_info("Click on Add Custom button")
        self.auto_actions.click(self.app_web_elements.get_manage_add_custom())
        sleep(2)

        self.utils.print_info("Enter Application name")
        self.auto_actions.send_keys(self.app_web_elements.get_manage_add_custom_name_textfield(), application_name)
        sleep(2)
        self.screen.save_screen_shot()

        self.utils.print_info("Click on Add Custom applications")
        self.auto_actions.click(self.app_web_elements.get_manage_add_custom_add_app())
        sleep(2)

        self.utils.print_info("Enter Group name")
        self.auto_actions.send_keys(self.app_web_elements.get_manage_add_custom_group_name_textfield(), group_name)
        sleep(2)
        self.screen.save_screen_shot()

        self.utils.print_info("clicking Save Button")
        self.auto_actions.click(self.app_web_elements.get_manage_add_custom_group_name_save())
        sleep(5)

        self.utils.print_info("clicking Save Button")
        self.auto_actions.click(self.app_web_elements.get_manage_add_custom_app_save())
        sleep(3)

        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)

        if "Add Custom Application successfully." in tool_tp_text[-1]:
            return 1
        else:
            self.utils.print_info("Unable to add custom application")
            return -1