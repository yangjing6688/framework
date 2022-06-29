from a3.defs.RolesWebElementDefs import *
from common.AutoActions import *
from common.WebElementHandler import *


class RolesWebElements(RolesWebElementDefs):
    def __init__(self):
        self.weh = WebElementHandler()
        self.auto_actions = AutoActions()

    def get_roles(self):
        return self.weh.get_element(self.roles)



