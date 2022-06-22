from a3.defs.ActiveDirectoryWebElementsDefs import *
from common.AutoActions import *
from common.WebElementHandler import *


class ActiveDirectoryWebElements(ActiveDirectoryWebElementsDefs):
    def __init__(self):
        self.weh = WebElementHandler()
        self.auto_actions = AutoActions()

    def get_ad_domains(self):
        return self.weh.get_element(self.ad_domain)

