from a3.defs.ConnProfileWebElementDefs import *
from common.AutoActions import *
from common.WebElementHandler import *


class ConnProfileWebElements(ConnProfileWebElementDefs):
    def __init__(self):
        self.weh = WebElementHandler()
        self.auto_actions = AutoActions()

    def select_conn_profile_menu(self):
        return self.weh.get_element(self.conn_profile_menu)



