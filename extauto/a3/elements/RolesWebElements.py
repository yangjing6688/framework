from a3.defs.RolesWebElementDefs import RolesWebElementDefs
from common.AutoActions import AutoActions
from common.WebElementHandler import WebElementHandler


class RolesWebElements(RolesWebElementDefs):
    def __init__(self):
        self.weh = WebElementHandler()
        self.auto_actions = AutoActions()

    def get_roles(self):
        return self.weh.get_element(self.roles)
