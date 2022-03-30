from extauto.xiq.defs.EspAlertDefs import *
from extauto.common.WebElementHandler import *


class EspAlertWebElements(EspAlertDefs):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_go_to_policy(self):
        return self.weh.get_element(self.go_to_policy)

    def get_configred_tab_txt(self):
        return self.weh.get_element(self.configred_tab_txt)

    def get_not_configred_tab_txt(self):
        return self.weh.get_element(self.not_configred_tab_txt)
