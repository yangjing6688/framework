# *** Settings ***
# Library           ExtremeAutomation/Keywords/NetworkElementKeywords/L2/NetworkElementVlanKeywords.py
# Library           ExtremeAutomation/Keywords/NetworkElementKeywords/L2/NetworkElementFdbKeywords.py
# Library           ExtremeAutomation/Keywords/NetworkElementKeywords/L2/NetworkElementIgmpKeywords.py
# Library           ExtremeAutomation/Keywords/TrafficKeywords/TrafficCaptureKeywords.py
# Library           ExtremeAutomation/Keywords/TrafficKeywords/TrafficPacketCreationKeywords.py
# Library           ExtremeAutomation/Keywords/TrafficKeywords/TrafficPacketInspectionKeywords.py
# Library           ExtremeAutomation/Keywords/TrafficKeywords/TrafficStatisticsKeywords.py
# Library           ExtremeAutomation/Keywords/TrafficKeywords/TrafficTransmitKeywords.py
# Library           ExtremeAutomation/Keywords/NetworkElementKeywords/NetworkElementConnectionManager.py
# Library           ExtremeAutomation/Keywords/VirtualMachineKeywords/VirtualMachineManager.py
# Library           ExtremeAutomation/Keywords/NetworkElementKeywords/Security/NetworkElementPolicyKeywords.py
# Library           ExtremeAutomation/Keywords/TrafficKeywords/TrafficGeneratorConnectionManager.py
# Library           ExtremeAutomation/Keywords/NetworkElementKeywords/L1/NetworkElementPortSettingsKeywords.py
# Library           ExtremeAutomation/Keywords/TrafficKeywords/TrafficPortKeywords.py
# Library           ExtremeAutomation/Keywords/NetworkElementKeywords/HostServices/NetworkElementHostServiceKeywords.py
# Resource          ExtremeAutomation/Keywords/UserDefinedKeywords/Public/L2/VlanUdks.robot
# Resource          ExtremeAutomation/Keywords/UserDefinedKeywords/Public/L2/FdbUdks.robot
# Resource          ExtremeAutomation/Keywords/UserDefinedKeywords/Public/L2/LacpUdks.robot
# Resource          ExtremeAutomation/Resources/Libraries/BaseLibraries/TrafficGenerationLibraries.robot

# *** Variables ***
# ### NetworkElement1 ###
# #${netelem1_name}                 EOS
# #${netelem1_ipv4_address}         10.52.8.191
# #${netelem1_username}             admin
# #${netelem1_password}             enterasysTPB
# #${netelem1_connection_methods}    telnet
# #${netelem1_os}          eos
# #${netelem1_platform}          s-series
# #${netelem1_tgen1_port_a}         tg.1.101
# #${netelem1_tgen1_port_b}         tg.2.101
# #${netelem1_tgen1_port_c}         tg.3.101
# #${netelem1_tgen1_port_d}         tg.4.101

# ${tgen1_ipv4_address}              10.52.153.101
# ${tgen1_vm_ipv4_address}           10.52.2.60
# ${tgen1_name}            Robot_SMOKE_Ostinato
# ${tgen1_username}                SMOKE_FDB_TB01
# ${tgen1_name}            Robot_SMOKE_Ixia
# ${tgen1_chassis_type}             ostinato
# ${tgen1_vm_port}          7878
# ${tgen1_port_a}                   lo
# ${tgen1_port_b}                   lo
