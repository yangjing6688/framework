import telnetlib
from ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent import TelnetAgent


class ConsoleAgent(TelnetAgent):
    def __init__(self, device):
        super(ConsoleAgent, self).__init__(device)
        self.type = self.constants.TYPE_CONSOLE

    def connect(self):
        """Creates a telnet session and attempts to connect with the devices IP (hostname) and port."""
        if not self.connected:
            self.main_session = telnetlib.Telnet()
            port = int(self.device.port)
            self.main_session.open(self.device.hostname, port, timeout=5)
            self.connected = True
        return self.main_session

    def login(self):
        try:
            ret = super(ConsoleAgent, self).login()
            return ret
        except:
            print("test of console obj badness")
            return False

    def disconnect(self):
        """
        Closes the connection to the console session.
        """
        self.main_session.close()
        self.connected = False
