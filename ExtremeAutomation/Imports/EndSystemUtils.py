############################################
# EndSystem Control Libraries
############################################
from ExtremeAutomation.Keywords.EndsystemKeywords.EndsystemConnectionManager import EndsystemConnectionManager
from ExtremeAutomation.Keywords.EndsystemKeywords.Common.CommonEndsystemKeywords import CommonEndsystemKeywords
from ExtremeAutomation.Keywords.EndsystemKeywords.Networking.EndsystemNetworkingKeywords import EndsystemNetworkingKeywords
from ExtremeAutomation.Keywords.EndsystemKeywords.MultiauthKeywords.EndsystemMultiAuthMethodClientKeywords import EndsystemMultiAuthMethodClientKeywords
from ExtremeAutomation.Keywords.EndsystemKeywords.HostServices.EndsystemHostServiceKeywords import EndsystemHostServiceKeywords
# from ExtremeAutomation.Keywords.EndsystemKeywords.ECIQ.EndsystemEciqDevicesKeywords import EndsystemEciqDevicesKeywords


class EndSystemUtils():
    """
        Description: The default set of End System functions. This will allow users to interact with the End Systems.
    """
    def __init__(self):       
        ############################################
        # EndSystem Control Libraries
        ############################################
        self.endsystemConnectionManager = EndsystemConnectionManager()
        self.commonEndsystemKeywords = CommonEndsystemKeywords()
        self.endsystemNetworkingKeywords = EndsystemNetworkingKeywords()
        self.endsystemMultiAuthMethodClientKeywords = EndsystemMultiAuthMethodClientKeywords()
        self.endsystemHostServiceKeywords = EndsystemHostServiceKeywords()
        # self.endsystemEciqDevicesKeywords = EndsystemEciqDevicesKeywords()