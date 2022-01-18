from ExtremeAutomation.Keywords.NetworkElementKeywords.NetworkElementConnectionManager import NetworkElementConnectionManager
from ExtremeAutomation.Keywords.UserDefinedKeywords.NetworkElements.L1.PortUdks import PortUdks
from ExtremeAutomation.Keywords.UserDefinedKeywords.NetworkElements.L2.VlanUdks import VlanUdks
from ExtremeAutomation.Keywords.UserDefinedKeywords.TrafficGeneration.TrafficGenerationUdks import TrafficGenerationUdks
from ExtremeAutomation.Keywords.NetworkElementKeywords.Utils.NetworkElementCliSend import NetworkElementCliSend 

class DefaultLibraries(object):
    
    def __init__(self):
        self.networkElementConnectionManager = NetworkElementConnectionManager()
        self.portUdks = PortUdks()
        self.vlanUdks = VlanUdks()
        self.networkElementCliSend = NetworkElementCliSend()
        self.trafficGenerationUdks = TrafficGenerationUdks()