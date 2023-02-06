from a3.defs.RealmsWebElementDefs import RealmsWebElementDefs
from common.AutoActions import AutoActions
from common.WebElementHandler import WebElementHandler


class RealmsWebElements(RealmsWebElementDefs):
    def __init__(self):
        self.weh = WebElementHandler()
        self.auto_actions = AutoActions()

    def get_realms_ui(self):
        return self.weh.get_element(self.realm_ui)
