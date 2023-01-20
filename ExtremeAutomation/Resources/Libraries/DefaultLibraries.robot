*** Settings ***
Documentation    This file contains all libraries for both Network Elements and Traffic Generation.

*** Settings ***

############################################
# Base Libraries
############################################
Library    Dialogs
Library    DateTime
Library    Collections
Library    ExtremeAutomation/Keywords/Utils/RobotDebugKeywords.py

############################################
# Network element Libraries
############################################

# Connection Libraries
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/NetworkElementConnectionManager.py


# Host Service Libraries
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/StaticKeywords/NetworkElementCosUtilsKeywords.py
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/StaticKeywords/NetworkElementFileManagementUtilsKeywords.py
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/StaticKeywords/NetworkElementFirmwareUtilsKeywords.py
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/StaticKeywords/NetworkElementHostServiceUtilsKeywords.py
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/StaticKeywords/NetworkElementHostUtilsKeywords.py
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/StaticKeywords/NetworkElementResetDeviceUtilsKeywords.py


############################################
# Generated Keywords
############################################

# L1 Libraries
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/GeneratedKeywords/NetworkElementPortGenKeywords.py
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/GeneratedKeywords/NetworkElementMirroringGenKeywords.py
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/GeneratedKeywords/NetworkElementPoeGenKeywords.py

# L2 Libraries
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/GeneratedKeywords/NetworkElementBridgemodeGenKeywords.py
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/GeneratedKeywords/NetworkElementFdbGenKeywords.py
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/GeneratedKeywords/NetworkElementIgmpGenKeywords.py
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/GeneratedKeywords/NetworkElementGvrpGenKeywords.py
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/GeneratedKeywords/NetworkElementLacpGenKeywords.py
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/GeneratedKeywords/NetworkElementLldpGenKeywords.py
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/GeneratedKeywords/NetworkElementSpanningtreeGenKeywords.py
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/GeneratedKeywords/NetworkElementVlanGenKeywords.py
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/GeneratedKeywords/NetworkElementVxlanGenKeywords.py
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/GeneratedKeywords/NetworkElementSpbmGenKeywords.py
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/GeneratedKeywords/NetworkElementCfmGenKeywords.py
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/GeneratedKeywords/NetworkElementMldGenKeywords.py
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/GeneratedKeywords/NetworkElementFabricattachGenKeywords.py
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/GeneratedKeywords/NetworkElementMltGenKeywords.py
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/GeneratedKeywords/NetworkElementMlagGenKeywords.py
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/GeneratedKeywords/NetworkElementVpexGenKeywords.py

# L3 Libraries
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/GeneratedKeywords/NetworkElementArpGenKeywords.py
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/GeneratedKeywords/NetworkElementBgpGenKeywords.py
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/GeneratedKeywords/NetworkElementAutopeeringGenKeywords.py
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/GeneratedKeywords/NetworkElementDhcpGenKeywords.py
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/GeneratedKeywords/NetworkElementDvrGenKeywords.py
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/GeneratedKeywords/NetworkElementInterfaceGenKeywords.py
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/GeneratedKeywords/NetworkElementNdGenKeywords.py
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/GeneratedKeywords/NetworkElementOspfGenKeywords.py
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/GeneratedKeywords/NetworkElementPimGenKeywords.py
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/GeneratedKeywords/NetworkElementIsisGenKeywords.py
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/GeneratedKeywords/NetworkElementIproutingGenKeywords.py
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/GeneratedKeywords/NetworkElementTunnelGenKeywords.py
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/GeneratedKeywords/NetworkElementVrfGenKeywords.py
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/GeneratedKeywords/NetworkElementRsmltGenKeywords.py
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/GeneratedKeywords/NetworkElementVrrpGenKeywords.py

# Host Service Libraries
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/GeneratedKeywords/NetworkElementHostinformationGenKeywords.py
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/GeneratedKeywords/NetworkElementHostmonitorGenKeywords.py
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/GeneratedKeywords/NetworkElementHostservicesGenKeywords.py
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/GeneratedKeywords/NetworkElementNtpGenKeywords.py
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/GeneratedKeywords/NetworkElementDnsGenKeywords.py
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/GeneratedKeywords/NetworkElementLoggingGenKeywords.py
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/GeneratedKeywords/NetworkElementSshGenKeywords.py
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/GeneratedKeywords/NetworkElementSshGenKeywords.py

# Management Libraries
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/GeneratedKeywords/NetworkElementLoginconfigGenKeywords.py
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/GeneratedKeywords/NetworkElementSnmpGenKeywords.py
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/GeneratedKeywords/NetworkElementSyslogGenKeywords.py
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/GeneratedKeywords/NetworkElementResetdeviceGenKeywords.py

# QOS Libraries
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/GeneratedKeywords/NetworkElementCosGenKeywords.py

# Security Libraries
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/GeneratedKeywords/NetworkElementAclGenKeywords.py
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/GeneratedKeywords/NetworkElementDot1xGenKeywords.py
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/GeneratedKeywords/NetworkElementIpsecurityGenKeywords.py
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/GeneratedKeywords/NetworkElementPolicyGenKeywords.py
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/GeneratedKeywords/NetworkElementRadiusGenKeywords.py
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/GeneratedKeywords/NetworkElementWebauthGenKeywords.py
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/GeneratedKeywords/NetworkElementMultiauthGenKeywords.py
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/GeneratedKeywords/NetworkElementMacauthGenKeywords.py
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/GeneratedKeywords/NetworkElementMacsecGenKeywords.py
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/GeneratedKeywords/NetworkElementUpmGenKeywords.py


############################################
# User Defined Keywords
############################################

# Suite Setup/Teardown *** Keywords ***
Library  ExtremeAutomation/Keywords/UserDefinedKeywords/NetworkElements/SetupTeardown/SetupTeardownUdks.py

# L1 Global User Defined Keywords
Library  ExtremeAutomation/Keywords/UserDefinedKeywords/NetworkElements/L1/PortUdks.py
Library  ExtremeAutomation/Keywords/UserDefinedKeywords/NetworkElements/L1/MirroringUdks.py

# L2 Global User Defined Keywords
Library  ExtremeAutomation/Keywords/UserDefinedKeywords/NetworkElements/L2/BridgeModeUdks.py
Library  ExtremeAutomation/Keywords/UserDefinedKeywords/NetworkElements/L2/FdbUdks.py
Library  ExtremeAutomation/Keywords/UserDefinedKeywords/NetworkElements/L2/GvrpUdks.py
Library  ExtremeAutomation/Keywords/UserDefinedKeywords/NetworkElements/L2/LacpUdks.py
Library  ExtremeAutomation/Keywords/UserDefinedKeywords/NetworkElements/L2/LldpUdks.py
Library  ExtremeAutomation/Keywords/UserDefinedKeywords/NetworkElements/L2/StpUdks.py
#
Library  ExtremeAutomation/Keywords/UserDefinedKeywords/NetworkElements/L2/VlanUdks.py
Library  ExtremeAutomation/Keywords/UserDefinedKeywords/NetworkElements/L2/FabricAttachUdks.py
Library  ExtremeAutomation/Keywords/UserDefinedKeywords/NetworkElements/L2/SpbmUdks.py
Library  ExtremeAutomation/Keywords/UserDefinedKeywords/NetworkElements/L2/MltUdks.py

# L3 Global User Defined Keywords
Library  ExtremeAutomation/Keywords/UserDefinedKeywords/NetworkElements/L3/ArpUdks.py
Library  ExtremeAutomation/Keywords/UserDefinedKeywords/NetworkElements/L3/InterfaceUdks.py
Library  ExtremeAutomation/Keywords/UserDefinedKeywords/NetworkElements/L3/NdUdks.py
Library  ExtremeAutomation/Keywords/UserDefinedKeywords/NetworkElements/L3/IsisUdks.py

# QOS Global User Defined Keywords
Library  ExtremeAutomation/Keywords/UserDefinedKeywords/NetworkElements/QOS/CosUdks.py

# Host Service User Defined Keywords
Library  ExtremeAutomation/Keywords/UserDefinedKeywords/NetworkElements/HostServices/HostServicesUdks.py
Library  ExtremeAutomation/Keywords/UserDefinedKeywords/NetworkElements/HostServices/TestbedVerificationUdks.py
Library  ExtremeAutomation/Keywords/UserDefinedKeywords/NetworkElements/HostServices/NtpUdks.py
Library  ExtremeAutomation/Keywords/UserDefinedKeywords/NetworkElements/HostServices/HostInformationUdks.py

# Security Global User Defined Keywords
Library  ExtremeAutomation/Keywords/UserDefinedKeywords/NetworkElements/Security/PolicyUdks.py
Library  ExtremeAutomation/Keywords/UserDefinedKeywords/NetworkElements/Security/MacAuthUdks.py
Library  ExtremeAutomation/Keywords/UserDefinedKeywords/NetworkElements/Security/WebAuthUdks.py
Library  ExtremeAutomation/Keywords/UserDefinedKeywords/NetworkElements/Security/Dot1xUdks.py
Library  ExtremeAutomation/Keywords/UserDefinedKeywords/NetworkElements/Security/RadiusUdks.py
Library  ExtremeAutomation/Keywords/UserDefinedKeywords/NetworkElements/Security/MultiAuthUdks.py

# Management User Defined Keywords
Library  ExtremeAutomation/Keywords/UserDefinedKeywords/NetworkElements/Management/LoginUdks.py

############################################
# Traffic Generation
############################################
Library    ExtremeAutomation/Keywords/TrafficKeywords/TrafficCaptureKeywords.py
Library    ExtremeAutomation/Keywords/TrafficKeywords/TrafficGeneratorConnectionManager.py
Library    ExtremeAutomation/Keywords/TrafficKeywords/TrafficPacketCreationKeywords.py
Library    ExtremeAutomation/Keywords/TrafficKeywords/TrafficPacketInspectionKeywords.py
Library    ExtremeAutomation/Keywords/TrafficKeywords/TrafficPortKeywords.py
Library    ExtremeAutomation/Keywords/TrafficKeywords/TrafficStatisticsKeywords.py
Library    ExtremeAutomation/Keywords/TrafficKeywords/TrafficTransmitKeywords.py
Library    ExtremeAutomation/Keywords/TrafficKeywords/TrafficStreamConfigurationKeywords.py
Library    ExtremeAutomation/Keywords/TrafficKeywords/EzTrafficValidation/TrafficValidationKeywords.py
Library    ExtremeAutomation/Keywords/TrafficKeywords/ProtocolEmulationBgpKeywords.py
Library    ExtremeAutomation/Keywords/TrafficKeywords/ProtocolEmulationDhcpKeywords.py
Library    ExtremeAutomation/Keywords/TrafficKeywords/ProtocolEmulationDvrKeywords.py
Library    ExtremeAutomation/Keywords/TrafficKeywords/ProtocolEmulationIgmpKeywords.py
Library    ExtremeAutomation/Keywords/TrafficKeywords/ProtocolEmulationLldpKeywords.py
Library    ExtremeAutomation/Keywords/TrafficKeywords/ProtocolEmulationOspfKeywords.py
Library    ExtremeAutomation/Keywords/TrafficKeywords/ProtocolEmulationRipKeywords.py
Library    ExtremeAutomation/Keywords/TrafficKeywords/ProtocolEmulationRipNgKeywords.py
Library    ExtremeAutomation/Keywords/TrafficKeywords/ProtocolEmulationSpbmKeywords.py
Library    ExtremeAutomation/Keywords/TrafficKeywords/ProtocolEmulationTcpKeywords.py
Library    ExtremeAutomation/Keywords/TrafficKeywords/ProtocolEmulationVrrpKeywords.py
Library    ExtremeAutomation/Keywords/TrafficKeywords/ProtocolEmulationVxlanKeywords.py
Library   ExtremeAutomation/Keywords/UserDefinedKeywords/TrafficGeneration/TrafficGenerationUdks.py

############################################
# EndSystem Control Libraries
############################################
Library    ExtremeAutomation/Keywords/EndsystemKeywords/EndsystemConnectionManager.py
Library    ExtremeAutomation/Keywords/EndsystemKeywords/Common/CommonEndsystemKeywords.py
Library    ExtremeAutomation/Keywords/EndsystemKeywords/Networking/EndsystemNetworkingKeywords.py
Library    ExtremeAutomation/Keywords/EndsystemKeywords/MultiauthKeywords/EndsystemMultiAuthMethodClientKeywords.py
Library    ExtremeAutomation/Keywords/EndsystemKeywords/HostServices/EndsystemHostServiceKeywords.py
Library    ExtremeAutomation/Keywords/EndsystemKeywords/ECIQ/EndsystemEciqDevicesKeywords.py

############################################
# Virtual Machine User Defined Keywords
############################################
Library  ExtremeAutomation/Keywords/VirtualMachineKeywords/VirtualMachineManager.py

############################################
# Libraries
############################################
Library    ExtremeAutomation/Keywords/Utils/PingKeywords.py
Library    ExtremeAutomation/Keywords/Utils/NetworkUtils.py
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/Utils/NetworkElementCliSend.py
Library    ExtremeAutomation/Keywords/NetworkElementKeywords/Utils/NetworkElementRestCommandSend.py

############################################
# Virtual Machine Library
############################################
Library    ExtremeAutomation/Keywords/VirtualMachineKeywords/VirtualMachineManager.py
Library    ExtremeAutomation/Keywords/VirtualMachineKeywords/Virtualization/VirtualMachineControl.py





