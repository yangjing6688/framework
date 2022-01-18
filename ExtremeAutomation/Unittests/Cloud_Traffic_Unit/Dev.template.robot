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
# Resource          ExtremeAutomation/Keywords/UserDefinedKeywords/Public/L1/PortUdks.robot
# Resource          ExtremeAutomation/Keywords/UserDefinedKeywords/Public/L2/FdbUdks.robot
# Resource          ExtremeAutomation/Keywords/UserDefinedKeywords/Public/L2/LacpUdks.robot
# Resource          ${TestBedVariable}

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
# #
# #${tgen1_ipv4_address}              10.52.8.17
# #${tgen1_vm_ipv4_address}           10.52.2.60
# #${tgen1_name}            Robot_SMOKE_Ixia
# #${tgen1_username}                SMOKE_FDB_TB01
# #${tgen1_name}            Robot_SMOKE_Ixia
# #${tgen1_chassis_type}             ixia
# #${tgen1_vm_port}          5678
# #${tgen1_port_a}                   1/2/7
# #${tgen1_port_b}                   1/2/8
# #${tgen1_port_c}                   1/2/9
# #${tgen1_port_d}                   1/2/10
# #${tgen1_port_e}                   1/2/11

# ${length}     68
# ${vlan_a}     222

# ${packet_name_a}     untagged_pkt
# ${src_mac_a}       00:11:22:33:44:55
# ${dest_mac_a}      00:aa:bb:cc:dd:ee

# *** Keywords ***
# set up ixia
    # ${port_list_1}=  create list  ${netelem1_tgen1_port_a}  ${netelem1_tgen1_port_b}
    # #SETUP
    # # connect to network element    ${netelem1_name}    ${netelem1_ipv4_address}    ${netelem1_username}    ${netelem1_password}    ${netelem1_connection_methods}    ${netelem1_os}
    # Connect To Traffic Generator    ${tgen1_name}    ${tgen1_chassis_type}    ${tgen1_ipv4_address}    ${tgen1_vm_ipv4_address}    ${tgen1_username}    ${tgen1_vm_port}
    # Take Port Ownership    ${tgen1_name}    ${tgen1_port_a}    ${tgen1_port_b}    ${tgen1_port_c}    ${tgen1_port_d}    ${tgen1_port_e}
        # Take Port Ownership    ${tgen1_name}    ${tgen1_port_a}    ${tgen1_port_b}

# send receive and check ixia results
    # clear port stats and filters      ${tgen1_name}    ${tgen1_port_a}
    # clear port stats and filters      ${tgen1_name}    ${tgen1_port_b}
    # start capture on port      ${tgen1_name}    ${tgen1_port_b}
    # configure and transmit stream with wait      ${tgen1_name}    ${tgen1_port_a}      1    ${packet_name_a}    100    100
    # stop capture on port      ${tgen1_name}    ${tgen1_port_b}
    # sent count should be equal    ${tgen1_name}    ${tgen1_port_a}      100
    # receive count should be equal    ${tgen1_name}    ${tgen1_port_b}      100
    # capture inspection random list     ${tgen1_name}    ${packet_name_a}    ${tgen1_port_b}

# clear tx port
    # enable traffic generetor debug output  ${tgen1_name} True
    # clear all traffic streams on port  ${tgen1_name}    ${tgen1_port_a}
    # clear all traffic streams on port  ${tgen1_name}    ${tgen1_port_b}

# *** Test Cases ***
# set up step
    # #SETUP
    # set up ixia

# 01 Basic Test Untagged Frames
    # [Tags]    F-3125    EXOS    EOS
    # ${port_list_1}=  create list  ${netelem1_tgen1_port_a}  ${netelem1_tgen1_port_b}
    # #SETUP
    # #Procedure
    # configure port enable    ${netelem1_name}    ${port_list_1}
    # Create VLAN and Verify it Exists  ${netelem1_name}  ${vlan_a}
    # Set PVID and Verify it was Set  ${netelem1_name}  ${port_list_1}  ${vlan_a}
    # Add PORT/S to Untagged Egress for VLAN and Verify it was Added  ${netelem1_name}  ${vlan_a}  ${port_list_1}
    # create ethernet2 ipv4 packet    ${packet_name_a}    ${dest_mac_a}    ${src_mac_a}    length=${length}

    # clear tx port

    # start capture on port      ${tgen1_name}    ${tgen1_port_b}
    # configure and transmit stream with wait      ${tgen1_name}    ${tgen1_port_a}      1    ${packet_name_a}    100    100
    # sent count should be equal    ${tgen1_name}    ${tgen1_port_a}      100
    # receive count should be equal    ${tgen1_name}    ${tgen1_port_b}      100
    # capture inspection random list     ${tgen1_name}    ${packet_name_a}    ${tgen1_port_b}
    # #Cleanup
    # Clear PVID and Verify it was Cleared  ${netelem1_name}  ${port_list_1}
    # Remove VLAN and Verify it was Removed  ${netelem1_name}  ${vlan_a}
    # configure port disable    ${netelem1_name}    ${port_list_1}

# cleanup and closedown
    # #Cleanup
    # close connection to traffic generator   ${tgen1_name}