from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.IxiaDevice import IxiaDevice


class IxiaHLTapiDevice(IxiaDevice):
    def __init__(self):
        super(IxiaHLTapiDevice, self).__init__()
        self._nameSpace = "ixia"
        # print "init IxiaDevice"
        self.logger.log_debug("init IxiaDevice")

    def connect(self, *arglist):
        # print arglist
        self.logger.log_debug(arglist)
        telnetlib_client = self.agents[IxiaDevice.TELNET]
        telnetlib_client.connect(arglist)
        # print telnetlib_client.read_until("#")
        self.logger.log_debug(telnetlib_client.read_until("#"))

    def register_apis(self):
        IxiaDevice.register_apis(self)
        # print "registering IxiaApis"
        self.logger.log_debug("registering IxiaApis")

    def register_agents(self):
        IxiaDevice.register_agents(self)
        # print "registering Ixia Agents"
        self.logger.log_debug("registering Ixia Agents")
        self.register_agent(IxiaDevice.TELNET, self)
