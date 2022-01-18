from ExtremeAutomation.Keywords.TrafficKeywords.TrafficCaptureKeywords import TrafficCaptureKeywords
from ExtremeAutomation.Keywords.TrafficKeywords.TrafficGeneratorConnectionManager import TrafficGeneratorConnectionManager
from ExtremeAutomation.Keywords.TrafficKeywords.TrafficPacketCreationKeywords import TrafficPacketCreationKeywords
from ExtremeAutomation.Keywords.TrafficKeywords.TrafficPacketInspectionKeywords import TrafficPacketInspectionKeywords
from ExtremeAutomation.Keywords.TrafficKeywords.TrafficStatisticsKeywords import TrafficStatisticsKeywords
from ExtremeAutomation.Keywords.TrafficKeywords.TrafficStreamConfigurationKeywords import TrafficStreamConfigurationKeywords
from ExtremeAutomation.Keywords.TrafficKeywords.EzTrafficValidation.TrafficValidationKeywords import TrafficValidationKeywords
from ExtremeAutomation.Keywords.TrafficKeywords.TrafficTransmitKeywords import TrafficTransmitKeywords
from ExtremeAutomation.Keywords.TrafficKeywords.Utils.Constants.PacketTypeConstants import PacketTypeConstants
from ExtremeAutomation.Keywords.TrafficKeywords.ProtocolEmulationBgpKeywords import ProtocolEmulationBgpKeywords
from ExtremeAutomation.Keywords.TrafficKeywords.ProtocolEmulationDhcpKeywords import ProtocolEmulationDhcpKeywords
from ExtremeAutomation.Keywords.TrafficKeywords.ProtocolEmulationDvrKeywords import ProtocolEmulationDvrKeywords
from ExtremeAutomation.Keywords.TrafficKeywords.ProtocolEmulationIgmpKeywords import ProtocolEmulationIgmpKeywords
from ExtremeAutomation.Keywords.TrafficKeywords.ProtocolEmulationLldpKeywords import ProtocolEmulationLldpKeywords
from ExtremeAutomation.Keywords.TrafficKeywords.ProtocolEmulationOspfKeywords import ProtocolEmulationOspfKeywords
from ExtremeAutomation.Keywords.TrafficKeywords.ProtocolEmulationRipKeywords import ProtocolEmulationRipKeywords
from ExtremeAutomation.Keywords.TrafficKeywords.ProtocolEmulationRipNgKeywords import ProtocolEmulationRipNgKeywords
from ExtremeAutomation.Keywords.TrafficKeywords.ProtocolEmulationSpbmKeywords import ProtocolEmulationSpbmKeywords
from ExtremeAutomation.Keywords.TrafficKeywords.ProtocolEmulationTcpKeywords import ProtocolEmulationTcpKeywords
from ExtremeAutomation.Keywords.TrafficKeywords.ProtocolEmulationVrrpKeywords import ProtocolEmulationVrrpKeywords
from ExtremeAutomation.Keywords.TrafficKeywords.ProtocolEmulationVxlanKeywords import ProtocolEmulationVxlanKeywords
from ExtremeAutomation.Keywords.TrafficKeywords.TrafficApplicationProfileKeywords import TrafficApplicationProfileKeywords
from ExtremeAutomation.Keywords.TrafficKeywords.TrafficPacketCollectionCreationKeywords import TrafficPacketCollectionCreationKeywords
from ExtremeAutomation.Keywords.TrafficKeywords.TrafficPortKeywords import TrafficPortKeywords
from ExtremeAutomation.Keywords.TrafficKeywords.TrafficProtocolConfigurationKeywords import TrafficProtocolConfigurationKeywords




class LowLevelTrafficApis():
    def __init__(self):
        self.trafficCaptureKeywords = TrafficCaptureKeywords()
        self.trafficGeneratorConnectionManager = TrafficGeneratorConnectionManager()
        self.trafficPacketCreationKeywords = TrafficPacketCreationKeywords()
        self.trafficPacketInspectionKeywords = TrafficPacketInspectionKeywords()
        self.trafficStatisticsKeywords = TrafficStatisticsKeywords()
        self.trafficStreamConfigurationKeywords = TrafficStreamConfigurationKeywords()
        self.trafficValidationKeywords = TrafficValidationKeywords()
        self.trafficTransmitKeywords = TrafficTransmitKeywords()
        self.packetTypeConstants = PacketTypeConstants()
        
        
        self.protocolEmulationBgpKeywords = ProtocolEmulationBgpKeywords()
        self.protocolEmulationDhcpKeywords = ProtocolEmulationDhcpKeywords()
        self.protocolEmulationDvrKeywords = ProtocolEmulationDvrKeywords()
        self.protocolEmulationIgmpKeywords = ProtocolEmulationIgmpKeywords()
        self.protocolEmulationLldpKeywords = ProtocolEmulationLldpKeywords()
        self.protocolEmulationOspfKeywords = ProtocolEmulationOspfKeywords()
        self.protocolEmulationRipKeywords = ProtocolEmulationRipKeywords()
        self.protocolEmulationRipNgKeywords = ProtocolEmulationRipNgKeywords()
        self.protocolEmulationSpbmKeywords = ProtocolEmulationSpbmKeywords()
        self.protocolEmulationTcpKeywords = ProtocolEmulationTcpKeywords()
        self.protocolEmulationVrrpKeywords = ProtocolEmulationVrrpKeywords()
        self.protocolEmulationVxlanKeywords = ProtocolEmulationVxlanKeywords()
        self.trafficApplicationProfileKeywords = TrafficApplicationProfileKeywords()
        self.trafficPacketCollectionCreationKeywords = TrafficPacketCollectionCreationKeywords()
        self.trafficPortKeywords = TrafficPortKeywords()
        self.trafficProtocolConfigurationKeywords = TrafficProtocolConfigurationKeywords()
        
