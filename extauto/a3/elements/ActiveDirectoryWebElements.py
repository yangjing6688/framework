from a3.defs.ActiveDirectoryWebElementsDefs import ActiveDirectoryWebElementsDefs
from common.AutoActions import AutoActions
from common.WebElementHandler import WebElementHandler


class ActiveDirectoryWebElements(ActiveDirectoryWebElementsDefs):
    def __init__(self):
        self.weh = WebElementHandler()
        self.auto_actions = AutoActions()

    def get_ad_domains(self):
        return self.weh.get_element(self.ad_domain)
