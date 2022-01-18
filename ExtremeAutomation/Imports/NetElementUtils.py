############################################
# Libraries
############################################
from ExtremeAutomation.Keywords.Utils.PingKeywords import PingKeywords
from ExtremeAutomation.Keywords.Utils.NetworkUtils import NetworkUtils
from ExtremeAutomation.Keywords.NetworkElementKeywords.Utils.NetworkElementCliSend import NetworkElementCliSend
from ExtremeAutomation.Keywords.NetworkElementKeywords.Utils.NetworkElementRestCommandSend import NetworkElementRestCommandSend
from ExtremeAutomation.Keywords.NetworkElementKeywords.NetworkElementConnectionManager import NetworkElementConnectionManager
from ExtremeAutomation.Keywords.NetworkElementKeywords.StaticKeywords.NetworkElementFirmwareUtilsKeywords import NetworkElementFirmwareUtilsKeywords


class NetElementUtils():
    """
        Description: The default set of Network Element functions. This will allow users to interact with the Network Element. This library includes the send_cmd function in case that the low level API hasn't been created.
    """
    def __init__(self):
        ############################################
        # Libraries
        ############################################
        self.pingKeywords = PingKeywords()
        self.networkUtils = NetworkUtils()
        self.networkElementCliSend = NetworkElementCliSend()
        self.networkElementRestCommandSend = NetworkElementRestCommandSend()
        self.networkElementConnectionManager = NetworkElementConnectionManager()
        self.networkElementFirmwareUtilsKeywords = NetworkElementFirmwareUtilsKeywords()