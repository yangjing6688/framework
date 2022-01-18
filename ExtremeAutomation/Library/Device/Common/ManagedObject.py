from ExtremeAutomation.Library.Logger.Logger import Logger
from ExtremeAutomation.Library.Device.Common.Agents.AgentConstants import AgentConstants


class ManagedObject(object):
    def __init__(self):
        self.logger = Logger()
        self.agent_constants = AgentConstants
