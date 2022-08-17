
from common.AutoActions import *
from a3.elements.ConnProfileWebElements import ConnProfileWebElements
from a3.elements.GlobalSettingWebElements import *
from xiq.flows.common.DeviceCommon import DeviceCommon
from common.CloudDriver import *


class ConnProfileWebElementsFlow(ConnProfileWebElements):
    def __init__(self):
        super().__init__()
        self.driver1 = None
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.device_common = DeviceCommon()
        self.conn_profile_web_elements = ConnProfileWebElements()
        self.setting = GlobalSettingWebElements()

    def create_mac_conn_profile(self):
        """
        - This keyword will create the Mac connection profile
        - Keyword Usage
        - ``Create Mac Conn Profile``
        :return: 1 if connection profile is created successfully else return -1
        """
        if self.auto_actions.click(self.select_conn_profile_menu()) == 1:
            sleep(5)
            self.utils.print_info("create a new connection profile ")
            sleep(10)
            new_profile = self.weh.get_element(self.conn_profile_new)
            self.auto_actions.click(new_profile)
            sleep(5)
            self.utils.print_info("profile name ")
            description = self.weh.get_element(self.conn_profile_name)
            self.auto_actions.send_keys(description, "802.1X")
            sleep(10)
            self.utils.print_info("click add filter")
            auth_add_rule = self.weh.get_element(self.add_filter)
            self.auto_actions.click(auth_add_rule)
            sleep(10)
            self.utils.print_info("Select action 1 for row 1")
            act1 = self.weh.get_element(self.add_filter_act1)
            self.auto_actions.click(act1)
            sleep(10)
            drop1 = self.weh.get_element(self.drop_opt_act1)
            self.auto_actions.click(drop1)
            sleep(5)
            self.utils.print_info("Select action 2 for row 1")
            act2 = self.weh.get_element(self.add_filter_act2)
            self.auto_actions.click(act2)
            sleep(5)
            drop2 = self.weh.get_element(self.drop_opt_act2)
            self.auto_actions.click(drop2)
            sleep(5)
            self.utils.print_info("Click on Add Source")
            add_src_btn = self.weh.get_element(self.add_source)
            self.auto_actions.click(add_src_btn)
            sleep(5)
            self.utils.print_info("Select Source")
            src = self.weh.get_element(self.select_source)
            self.auto_actions.click(src)
            sleep(5)
            self.utils.print_info("Created Connection Profile")
            create_conn_profile = self.weh.get_element(self.save_button)
            self.auto_actions.click(create_conn_profile)
            sleep(5)
            self.utils.print_info("Connection Profile is created successfully")
            return 1
        else:
            self.utils.print_info("Connection Profile is not created")
            return -1

    def create_guest_conn_profile(self):
        """
        - This keyword will create the Guest connection profile
        - Keyword Usage
        - ``Create Guest Conn Profile``
        :return: 1 if connection profile is created successfully else return -1
        """
        if self.auto_actions.click(self.select_conn_profile_menu()) == 1:
            sleep(5)
            self.utils.print_info("create a new connection profile ")
            sleep(10)
            new_profile = self.weh.get_element(self.conn_profile_new)
            self.auto_actions.click(new_profile)
            sleep(5)
            self.utils.print_info("profile name ")
            description = self.weh.get_element(self.conn_profile_name)
            self.auto_actions.send_keys(description, "802.1X")
            sleep(10)
            self.utils.print_info("click add filter")
            auth_add_rule = self.weh.get_element(self.add_filter)
            self.auto_actions.click(auth_add_rule)
            sleep(10)
            self.utils.print_info("Select action 1 for row 1")
            act1 = self.weh.get_element(self.add_filter_act1)
            self.auto_actions.click(act1)
            sleep(10)
            drop1 = self.weh.get_element(self.drop_opt_act1)
            self.auto_actions.click(drop1)
            sleep(5)
            self.utils.print_info("Select action 2 for row 1")
            act2 = self.weh.get_element(self.add_filter_act2)
            self.auto_actions.click(act2)
            sleep(5)
            drop2 = self.weh.get_element(self.drop_opt_act2)
            self.auto_actions.click(drop2)
            sleep(5)
            self.utils.print_info("Click on Add Source")
            add_src_btn = self.weh.get_element(self.add_source)
            self.auto_actions.click(add_src_btn)
            sleep(5)
            self.utils.print_info("Select Source")
            src = self.weh.get_element(self.select_source)
            self.auto_actions.click(src)
            sleep(5)
            self.utils.print_info("Created Connection Profile")
            create_conn_profile = self.weh.get_element(self.save_button)
            self.auto_actions.click(create_conn_profile)
            sleep(5)
            self.utils.print_info("Connection Profile is created successfully")
            return 1
        else:
            self.utils.print_info("Connection Profile is not created")
            return -1
