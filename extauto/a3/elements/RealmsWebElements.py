from a3.defs.RealmsWebElementDefs import *
from common.AutoActions import *
from common.WebElementHandler import *


class RealmsWebElements(RealmsWebElementDefs):
    def __init__(self):
        self.weh = WebElementHandler()
        self.auto_actions = AutoActions()

    def get_realms_ui(self):
        return self.weh.get_element(self.realm_ui)



