from a3.defs.RolesWebElementDefs import *
from common.AutoActions import *
from common.WebElementHandler import *


class RolesWebElements(RolesWebElementDefs):
    def __init__(self):
        self.weh = WebElementHandler()
        self.auto_actions = AutoActions()

    def select_conn_profile_menu(self):
        return self.weh.get_element(self.conn_profile_menu)



