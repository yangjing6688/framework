from ExtremeAutomation.Library.Device.NetworkElement.NetelemLearning.Components.Unit import Unit
from ExtremeAutomation.Library.Device.NetworkElement.NetelemLearning.Components.Stack import Stack
from ExtremeAutomation.Library.Device.NetworkElement.NetelemLearning.Components.Chassis import Chassis
from ExtremeAutomation.Library.Device.NetworkElement.NetelemLearning.Components.ComponentCollection \
    import ComponentCollection


class System(ComponentCollection):
    def __init__(self, **system_info):
        super(System, self).__init__()

        self._valid_components = [Unit(), Stack(), Chassis()]
        self.mac_addr = None

        if "mac_addr" in system_info:
            self.mac_addr = system_info["mac_addr"]
