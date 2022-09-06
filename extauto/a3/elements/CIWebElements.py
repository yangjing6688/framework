from a3.defs.CIWebElementsDefs import *
from common.AutoActions import *
from common.WebElementHandler import *


class CIWebElements(CIWebElementsDefs):
    def __init__(self):
        self.weh = WebElementHandler()
        self.auto_actions = AutoActions()

    def get_cloud(self):
        return self.weh.get_element(self.cloud_integration)

    def cloud_host(self):
        return self.weh.get_element(self.cloud_host_input)



