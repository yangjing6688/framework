from common.AutoActions import *
from a3.elements.RolesWebElements import RolesWebElements
from a3.elements.GlobalSettingWebElements import *
from xiq.flows.common.DeviceCommon import DeviceCommon


class RolesWebElementsFlow(RolesWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.device_common = DeviceCommon()
        self.roles_web_elements = RolesWebElements()
        self.setting = GlobalSettingWebElements()

    def create_roles(self):
        """
            - This keyword select the Roles from the menu Policies and Access Control and create the role
            - Keyword Usage
             - ``Create Roles``
        :return: 1 if role created successfully else return -1
        """
        self.utils.print_info("Selecting Roles from menu...")

        if self.auto_actions.click(self.get_roles()) == 1:
            sleep(2)
            self.utils.print_info("Click New Role ")
            element = self.weh.get_element(self.role_button)
            self.auto_actions.click(element)
            sleep(10)
            self.utils.print_info("Enter Name")
            element1 = self.weh.get_element(self.role_name)
            self.auto_actions.send_keys(element1, "roleE")
            self.utils.print_info("Enter Description")
            element2 = self.weh.get_element(self.name_desc)
            self.auto_actions.send_keys(element2, "Emp")
            sleep(5)
            element3 = self.weh.get_element(self.create_button)
            status = self.weh.get_element(self.create_button).is_enabled()
            if status:
                self.utils.print_info("state of create button is enabled")
            else:
                self.utils.print_info("state of create button is disabled.")
                sleep(5)
            sleep(5)
            self.auto_actions.click(element3)
            sleep(5)
            element4 = self.weh.get_element(self.save_button)
            self.auto_actions.click(element4)
            sleep(5)
            element5 = self.weh.get_element(self.close_button)
            self.auto_actions.click(element5)
            self.utils.print_info("Role created Successfully")
            return 1
        else:
            self.utils.print_info("Unable to navigate to Roles")
            self.screen.save_screen_shot()
            return -1


