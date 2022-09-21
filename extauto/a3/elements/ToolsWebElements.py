from a3.defs.ToolsWebElementsDefs import *
from common.AutoActions import *
from common.WebElementHandler import *


class ToolsWebElements(ToolsWebElementsDefs):
    def __init__(self):
        self.weh = WebElementHandler()
        self.auto_actions = AutoActions()

    def get_conn_profile_test_ui(self):
        return self.weh.get_element(self.conn_profile_test)

    def get_ssh_option_ui(self):
        return self.weh.get_element(self.ssh_option_ui)

    def get_ssh_button(self):
        ssh_btn = self.weh.get_element(self.ssh_selector)
        return ssh_btn

    def get_ssh_duration(self):
        return self.weh.get_element(self.input_drop_down_options)

    def get_log_ui(self):
        return self.weh.get_element(self.log_ui)




