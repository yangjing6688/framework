from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass \
    import NetworkElementKeywordBaseClass
from ExtremeAutomation.Library.Device.EndsystemElement.Constants.EndsystemElementConstants \
    import EndsystemElementConstants


class EndsystemKeywordBaseClass(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(EndsystemKeywordBaseClass, self).__init__()
        self.constants = EndsystemElementConstants()
