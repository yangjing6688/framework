############################################
# User Defined Keywords
############################################

# Suite Setup.Teardown *** Keywords ***
from ExtremeAutomation.Keywords.UserDefinedKeywords.NetworkElements.SetupTeardown.SetupTeardownUdks import SetupTeardownUdks

# L1 Global User Defined Keywords
from ExtremeAutomation.Keywords.UserDefinedKeywords.NetworkElements.L1.PortUdks import PortUdks
from ExtremeAutomation.Keywords.UserDefinedKeywords.NetworkElements.L1.MirroringUdks import MirroringUdks

# L2 Global User Defined Keywords
from ExtremeAutomation.Keywords.UserDefinedKeywords.NetworkElements.L2.BridgeModeUdks import BridgeModeUdks
from ExtremeAutomation.Keywords.UserDefinedKeywords.NetworkElements.L2.FdbUdks import FdbUdks
from ExtremeAutomation.Keywords.UserDefinedKeywords.NetworkElements.L2.GvrpUdks import GvrpUdks
from ExtremeAutomation.Keywords.UserDefinedKeywords.NetworkElements.L2.LacpUdks import LacpUdks
from ExtremeAutomation.Keywords.UserDefinedKeywords.NetworkElements.L2.LldpUdks import LldpUdks
from ExtremeAutomation.Keywords.UserDefinedKeywords.NetworkElements.L2.StpUdks import StpUdks
#
from ExtremeAutomation.Keywords.UserDefinedKeywords.NetworkElements.L2.VlanUdks import VlanUdks
from ExtremeAutomation.Keywords.UserDefinedKeywords.NetworkElements.L2.FabricAttachUdks import FabricAttachUdks
from ExtremeAutomation.Keywords.UserDefinedKeywords.NetworkElements.L2.SpbmUdks import SpbmUdks
from ExtremeAutomation.Keywords.UserDefinedKeywords.NetworkElements.L2.MltUdks import MltUdks

# L3 Global User Defined Keywords
from ExtremeAutomation.Keywords.UserDefinedKeywords.NetworkElements.L3.ArpUdks import ArpUdks
from ExtremeAutomation.Keywords.UserDefinedKeywords.NetworkElements.L3.InterfaceUdks import InterfaceUdks
from ExtremeAutomation.Keywords.UserDefinedKeywords.NetworkElements.L3.NdUdks import NdUdks
from ExtremeAutomation.Keywords.UserDefinedKeywords.NetworkElements.L3.IsisUdks import IsisUdks

# QOS Global User Defined Keywords
from ExtremeAutomation.Keywords.UserDefinedKeywords.NetworkElements.QOS.CosUdks import CosUdks 

# Host Service User Defined Keywords
from ExtremeAutomation.Keywords.UserDefinedKeywords.NetworkElements.HostServices.HostServicesUdks import HostServicesUdks
from ExtremeAutomation.Keywords.UserDefinedKeywords.NetworkElements.HostServices.TestbedVerificationUdks import TestbedVerificationUdks
from ExtremeAutomation.Keywords.UserDefinedKeywords.NetworkElements.HostServices.NtpUdks import NtpUdks
from ExtremeAutomation.Keywords.UserDefinedKeywords.NetworkElements.HostServices.HostInformationUdks import HostInformationUdks

# Security Global User Defined Keywords
from ExtremeAutomation.Keywords.UserDefinedKeywords.NetworkElements.Security.PolicyUdks import PolicyUdks
from ExtremeAutomation.Keywords.UserDefinedKeywords.NetworkElements.Security.MacAuthUdks import MacAuthUdks
from ExtremeAutomation.Keywords.UserDefinedKeywords.NetworkElements.Security.WebAuthUdks import WebAuthUdks
from ExtremeAutomation.Keywords.UserDefinedKeywords.NetworkElements.Security.Dot1xUdks import Dot1xUdks
from ExtremeAutomation.Keywords.UserDefinedKeywords.NetworkElements.Security.RadiusUdks import RadiusUdks
from ExtremeAutomation.Keywords.UserDefinedKeywords.NetworkElements.Security.MultiAuthUdks import MultiAuthUdks

# Management User Defined Keywords
from ExtremeAutomation.Keywords.UserDefinedKeywords.NetworkElements.Management.LoginUdks import LoginUdks

# Traffic Generator
from ExtremeAutomation.Keywords.UserDefinedKeywords.TrafficGeneration.TrafficGenerationUdks import TrafficGenerationUdks





class Udks():
    """
        Description: The default set of User Defined Keyword functions. These are helper functions that do common actions in a test case.
    """
    def __init__(self):
        # Suite Setup.Teardown *** Keywords ***
        self.setupTeardownUdks = SetupTeardownUdks()
        
        # L1 Global User Defined Keywords
        self.portUdks = PortUdks()
        self.mirroringUdks = MirroringUdks()
        
        # L2 Global User Defined Keywords
        self.bridgeModeUdks = BridgeModeUdks()
        self.fdbUdks = FdbUdks()
        self.gvrpUdks = GvrpUdks()
        self.lacpUdks = LacpUdks()
        self.lldpUdks = LldpUdks()
        self.StpUdks = StpUdks()
        #
        self.vlanUdks = VlanUdks()
        self.fabricAttachUdks = FabricAttachUdks()
        self.spbmUdks = SpbmUdks()
        self.mltUdks = MltUdks()
        
        # L3 Global User Defined Keywords
        self.arpUdks = ArpUdks()
        self.interfaceUdks = InterfaceUdks()
        self.ndUdks = NdUdks()
        self.isisUdks = IsisUdks()
        
        # QOS Global User Defined Keywords
        self.cosUdks  = CosUdks()
        
        # Host Service User Defined Keywords
        self.hostServicesUdks = HostServicesUdks()
        self.testbedVerificationUdks = TestbedVerificationUdks()
        self.ntpUdks = NtpUdks()
        self.hostInformationUdks = HostInformationUdks()
        
        # Security Global User Defined Keywords
        self.policyUdks = PolicyUdks()
        self.macAuthUdks = MacAuthUdks()
        self.webAuthUdks = WebAuthUdks()
        self.dot1xUdks = Dot1xUdks()
        self.radiusUdks = RadiusUdks()
        self.multiAuthUdks = MultiAuthUdks()
        
        # Management User Defined Keywords
        self.loginUdks = LoginUdks()
        
        # Traffic Generator
        self.trafficGenerationUdks = TrafficGenerationUdks()
        
        
        