from ExtremeAutomation.Library.Device.NetworkElement.NetelemLearning.Components.Unit import Unit
from ExtremeAutomation.Library.Device.NetworkElement.NetelemLearning.Components.Chassis import Chassis
from ExtremeAutomation.Library.Device.NetworkElement.NetelemLearning.Components.NetworkComponent import NetworkComponent
from ExtremeAutomation.Library.Device.NetworkElement.NetelemLearning.Components.ComponentCollection \
    import ComponentCollection


class Stack(ComponentCollection, NetworkComponent):
    def __init__(self, **stack_info):
        super(Stack, self).__init__()

        self._valid_components = [Unit(), Chassis()]

        # todo: populate attributes with stack info.
