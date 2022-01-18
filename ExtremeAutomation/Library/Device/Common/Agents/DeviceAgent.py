from ExtremeAutomation.Library.Device.Common.ManagedObject import ManagedObject
from ExtremeAutomation.Library.Device.Common.Agents.AgentConstants import AgentConstants


class DeviceAgent(ManagedObject):
    def __init__(self, device):
        super(DeviceAgent, self).__init__()
        self.device = device
        self.constants = AgentConstants
