from ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent import TelnetAgent


class IxiaConnectionTelnetAgent(TelnetAgent):
    def __init__(self, device):
        """
        Init function
        """
        super(IxiaConnectionTelnetAgent, self).__init__(device)
        self.HOST = "localhost"
        self.PORT = "4666"
        self.MAIN_SESSION = None

    def is_connected(self):
        """
        This function returns self.connected.

        It should be removed when possible. It was preserved so it would not affect traffic generation.
        It is unnecessary, going forward the connected attribute should be accessed directly.
        """
        return self.connected
