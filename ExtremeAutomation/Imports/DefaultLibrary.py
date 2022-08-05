from ExtremeAutomation.Imports.Udks import Udks
from ExtremeAutomation.Imports.EndSystemUtils import EndSystemUtils
from ExtremeAutomation.Imports.LowLevelApis import LowLevelApis
from ExtremeAutomation.Imports.VirtualMachineUtils import VirtualMachineUtils
from ExtremeAutomation.Imports.NetElementUtils import NetElementUtils
from ExtremeAutomation.Imports.LowLevelTrafficApis import LowLevelTrafficApis
from ExtremeAutomation.Imports.CommonObjectUtils import CommonObjectUtils


class DefaultLibrary():
    """
        Description: The default set of libraries for the framework
    """
    def __init__(self):
        self.apiUdks = Udks()
        self.apiLowLevelApis = LowLevelApis()
        self.apiLowLevelTrafficApis = LowLevelTrafficApis()
        self.deviceEndSystem = EndSystemUtils()
        self.deviceVirtualMachine = VirtualMachineUtils()
        self.deviceNetworkElement = NetElementUtils()
        self.commonObjectUtils = CommonObjectUtils()