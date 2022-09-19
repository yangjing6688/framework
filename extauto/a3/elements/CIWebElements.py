from a3.defs.CIWebElementsDefs import *
from common.AutoActions import *
from common.WebElementHandler import *


class CIWebElements(CIWebElementsDefs):
    def __init__(self):
        self.weh = WebElementHandler()
        self.auto_actions = AutoActions()

    def get_cloud(self):
        cloud_element = self.weh.get_element(self.cloud_integration)
        return cloud_element

    def cloud_host(self):
        return self.weh.get_element(self.cloud_host_input)

    def get_cloud_admin(self):
        return self.weh.get_element(self.cloud_admin)

    def get_cloud_password(self):
        return self.weh.get_element(self.cloud_password)

    def get_cloud_link_button(self):
        return self.weh.get_element(self.cloud_link_button)

    def get_cloud_unlink_button(self):
        return self.weh.get_element(self.cloud_unlink_button)
