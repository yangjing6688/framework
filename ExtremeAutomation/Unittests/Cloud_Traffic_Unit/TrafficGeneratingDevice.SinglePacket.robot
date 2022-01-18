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
# Resource          ExtremeAutomation/Resources/Libraries/BaseLibraries/TrafficGenerationLibraries.robot
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

# ${length}     500
# ${vlan_a}     222

# ${svlan_count_a}   2
# ${svlan_id_a}   2
# ${svlan_id_b}   66
# ${svlan_pri_a}   1
# ${svlan_pri_b}  3

# ${packet_name_a}     untagged_pkt
# ${src_mac_a}       00:11:22:33:44:55
# ${dest_mac_a}      00:aa:bb:cc:dd:ee
# ${src_ipv4_a}       1.1.1.1
# ${dest_ipv4_a}      2.2.2.2
# ${src_ipv6_a}       ffff::1111
# ${dest_ipv6_a}      ffff::2222
# ${src_port_a}      56
# ${dest_port_a}      78

# # pybot --variable TestBedVariable:ExtremeAutomation/Library/Unittests/Cloud_Traffic_Unit/Resources/TrafficGeneratingDevice.Ostinato.Transmit.robot TrafficGeneratingDevice.SinglePacket.robot
# # pybot --variable TestBedVariable:ExtremeAutomation/Library/Unittests/Cloud_Traffic_Unit/Resources/TrafficGeneratingDevice.Ixia.Transmit.robot TrafficGeneratingDevice.SinglePacket.robot

# *** Keywords ***
# set up ixia
    # Connect To Traffic Generator    ${tgen1_name}    ${tgen1_chassis_type}    ${tgen1_ipv4_address}    ${tgen1_vm_ipv4_address}    ${tgen1_username}    ${tgen1_vm_port}
# #    Take Port Ownership    ${tgen1_name}    ${tgen1_port_a}    ${tgen1_port_b}

# send receive and check ixia results
    # clear port stats and filters      ${tgen1_name}    ${tgen1_port_a}
    # clear port stats and filters      ${tgen1_name}    ${tgen1_port_b}
    # start capture on port      ${tgen1_name}    ${tgen1_port_b}
    # configure and transmit stream with wait      ${tgen1_name}    ${tgen1_port_a}      1    ${packet_name_a}    100    100
    # stop capture on port      ${tgen1_name}    ${tgen1_port_b}    debug_packet=True
    # sent count should be equal    ${tgen1_name}    ${tgen1_port_a}      100
    # receive count should be equal    ${tgen1_name}    ${tgen1_port_b}      100
    # capture inspection random list     ${tgen1_name}    ${packet_name_a}    ${tgen1_port_b}

# clear tx port
    # Enable Traffic Generator Debug Output  ${tgen1_name} True
    # clear all traffic streams on port  ${tgen1_name}    ${tgen1_port_a}
    # clear all traffic streams on port  ${tgen1_name}    ${tgen1_port_b}


# *** Test Cases ***
# set up step
    # #SETUP
    # set up ixia

# Ethernet 2 packet test
    # [Tags]    IXIA  ENET2
    # #SETUP
    # #set up ixia
    # clear tx port
    # #Procedure
    # create ethernet2 packet    ${packet_name_a}    ${dest_mac_a}  ${src_mac_a}  length=${length}
    # #run and check the packets.
    # send receive and check ixia results
    # #Cleanup
    # #close connection to traffic generator   ${tgen1_name}

# Ethernet 2 tagged packet test
    # [Tags]    IXIA  ENET2  TAGGED
    # #SETUP
    # #set up ixia
    # clear tx port
    # #Procedure
    # create ethernet2 tagged packet    ${packet_name_a}    ${dest_mac_a}  ${src_mac_a}  length=${length}
    # #run and check the packets.
    # send receive and check ixia results
    # #Cleanup
    # #close connection to traffic generator   ${tgen1_name}

# Ethernet 2 vlanstack packet test
    # [Tags]    IXIA  ENET2  VLANSTACK
    # #SETUP
    # #set up ixia
    # clear tx port
    # ${vlan_tag_list_1}=  create list  ${svlan_id_a}  ${svlan_id_b}
    # ${vlan_pri_list_1}=  create list  ${svlan_pri_a}  ${svlan_pri_a}
    # #Procedure
    # create ethernet2 vlanstack packet    ${packet_name_a}    ${dest_mac_a}  ${src_mac_a}  ether_type=0x888  length=${length}  vlanstack_count=${svlan_count_a}  vlanstack_ids=${vlan_tag_list_1}  vlanstack_priorities=${vlan_pri_list_1}
    # #run and check the packets.
    # send receive and check ixia results
    # #Cleanup
    # #close connection to traffic generator   ${tgen1_name}

# Ethernet 2 ipv4 packet test
    # [Tags]    IXIA  ENET2   IPV4
    # #SETUP
    # #set up ixia
    # clear tx port
    # #Procedure
    # create ethernet2 ipv4 packet    ${packet_name_a}    ${dest_mac_a}  ${src_mac_a}  ether_type=0x800  length=${length}  dip=${dest_ipv4_a}  sip=${src_ipv4_a}
    # #run and check the packets.
    # send receive and check ixia results
    # #Cleanup
    # #close connection to traffic generator   ${tgen1_name}

# Ethernet 2 ipv4 tagged packet test
    # [Tags]    IXIA  ENET2   IPV4  TAGGED
    # #SETUP
    # #set up ixia
    # clear tx port
    # #Procedure
    # create ethernet2 ipv4 tagged packet   ${packet_name_a}    ${dest_mac_a}  ${src_mac_a}  ether_type=0x800  length=${length}  dip=${dest_ipv4_a}  sip=${src_ipv4_a}
    # #run and check the packets.
    # send receive and check ixia results
    # #Cleanup
    # #close connection to traffic generator   ${tgen1_name}

# Ethernet 2 ipv4 vlanstack packet test
    # [Tags]    IXIA  ENET2   IPV4  VLANSTACK
    # #SETUP
    # #set up ixia
    # clear tx port
    # ${vlan_tag_list_1}=  create list  ${svlan_id_a}  ${svlan_id_b}
    # ${vlan_pri_list_1}=  create list  ${svlan_pri_a}  ${svlan_pri_a}
    # #Procedure
    # create ethernet2 ipv4 vlanstack packet   ${packet_name_a}    ${dest_mac_a}  ${src_mac_a}  ether_type=0x800  length=${length}  dip=${dest_ipv4_a}  sip=${src_ipv4_a}  vlanstack_count=${svlan_count_a}  vlanstack_ids=${vlan_tag_list_1}  vlanstack_priorities=${vlan_pri_list_1}
    # #run and check the packets.
    # send receive and check ixia results
    # #Cleanup
    # #close connection to traffic generator   ${tgen1_name}

# Ethernet 2 ipv4 tcp packet test
    # [Tags]    IXIA  ENET2   IPV4  TCP
    # #SETUP
    # #set up ixia
    # clear tx port
    # #Procedure
    # create ethernet2 ipv4 tcp packet   ${packet_name_a}    ${dest_mac_a}  ${src_mac_a}  ether_type=0x800  length=${length}  dip=${dest_ipv4_a}  sip=${src_ipv4_a}  src_port=${src_port_a}  dst_port=${dest_port_a}
    # #run and check the packets.
    # send receive and check ixia results
    # #Cleanup
    # #close connection to traffic generator   ${tgen1_name}

# Ethernet 2 ipv4 tcp tagged packet test
    # [Tags]    IXIA  ENET2   IPV4  TCP  TAGGED
    # #SETUP
    # #set up ixia
    # clear tx port
    # #Procedure
    # create ethernet2 ipv4 tagged tcp packet   ${packet_name_a}    ${dest_mac_a}  ${src_mac_a}  ether_type=0x800  length=${length}  dip=${dest_ipv4_a}  sip=${src_ipv4_a}  src_port=${src_port_a}  dst_port=${dest_port_a}
    # #run and check the packets.
    # send receive and check ixia results
    # #Cleanup
    # #close connection to traffic generator   ${tgen1_name}

# Ethernet 2 ipv4 tcp vlanstack packet test
    # [Tags]    IXIA  ENET2   IPV4  TCP   VLANSTACK
    # #SETUP
    # #set up ixia
    # clear tx port
    # ${vlan_tag_list_1}=  create list  ${svlan_id_a}  ${svlan_id_b}
    # ${vlan_pri_list_1}=  create list  ${svlan_pri_a}  ${svlan_pri_a}
    # #Procedure
    # create ethernet2 ipv4 vlanstack tcp packet   ${packet_name_a}    ${dest_mac_a}  ${src_mac_a}  ether_type=0x800  length=${length}  dip=${dest_ipv4_a}  sip=${src_ipv4_a}  src_port=${src_port_a}  dst_port=${dest_port_a}  vlanstack_count=${svlan_count_a}  vlanstack_ids=${vlan_tag_list_1}  vlanstack_priorities=${vlan_pri_list_1}
    # #run and check the packets.
    # send receive and check ixia results
    # #Cleanup
    # #close connection to traffic generator   ${tgen1_name}

# Ethernet 2 ipv4 udp packet test
    # [Tags]    IXIA  ENET2   IPV4  UDP
    # #SETUP
    # #set up ixia
    # clear tx port
    # #Procedure
    # create ethernet2 ipv4 udp packet   ${packet_name_a}    ${dest_mac_a}  ${src_mac_a}  ether_type=0x800  length=${length}  dip=${dest_ipv4_a}  sip=${src_ipv4_a}  src_port=${src_port_a}  dst_port=${dest_port_a}
    # #run and check the packets.
    # send receive and check ixia results
    # #Cleanup
    # #close connection to traffic generator   ${tgen1_name}

# Ethernet 2 ipv4 udp tagged packet test
    # [Tags]    IXIA  ENET2   IPV4  UDP  TAGGED
    # #SETUP
    # #set up ixia
    # clear tx port
    # #Procedure
    # create ethernet2 ipv4 tagged udp packet   ${packet_name_a}    ${dest_mac_a}  ${src_mac_a}  ether_type=0x800  length=${length}  dip=${dest_ipv4_a}  sip=${src_ipv4_a}  src_port=${src_port_a}  dst_port=${dest_port_a}
    # #run and check the packets.
    # send receive and check ixia results
    # #Cleanup
    # #close connection to traffic generator   ${tgen1_name}

# Ethernet 2 ipv4 udp vlanstack packet test
    # [Tags]    IXIA  ENET2   IPV4  UDP  VLANSTACK
    # #SETUP
    # #set up ixia
    # clear tx port
    # ${vlan_tag_list_1}=  create list  ${svlan_id_a}  ${svlan_id_b}
    # ${vlan_pri_list_1}=  create list  ${svlan_pri_a}  ${svlan_pri_a}
    # #Procedure
    # create ethernet2 ipv4 vlanstack udp packet   ${packet_name_a}    ${dest_mac_a}  ${src_mac_a}  ether_type=0x800  length=${length}  dip=${dest_ipv4_a}  sip=${src_ipv4_a}  src_port=${src_port_a}  dst_port=${dest_port_a}  vlanstack_count=${svlan_count_a}  vlanstack_ids=${vlan_tag_list_1}  vlanstack_priorities=${vlan_pri_list_1}
    # #run and check the packets.
    # send receive and check ixia results
    # #Cleanup
    # #close connection to traffic generator   ${tgen1_name}


# Ethernet 2 ipv6 packet test
    # [Tags]    IXIA   ENET2   IPV6
    # #SETUP
    # #set up ixia
    # clear tx port
    # #Procedure
    # create ethernet2 ipv6 packet    ${packet_name_a}    ${dest_mac_a}  ${src_mac_a}  ether_type=0x800  length=${length}  ipv6_dip=${dest_ipv6_a}  ipv6_sip=${src_ipv6_a}
    # #run and check the packets.
    # send receive and check ixia results
    # #Cleanup
    # #close connection to traffic generator   ${tgen1_name}

# Ethernet 2 ipv6 tagged packet test
    # [Tags]    IXIA   ENET2   IPV6  TAGGED
    # #SETUP
    # #set up ixia
    # clear tx port
    # #Procedure
    # create ethernet2 ipv6 tagged packet   ${packet_name_a}    ${dest_mac_a}  ${src_mac_a}  ether_type=0x800  length=${length}  ipv6_dip=${dest_ipv6_a}  ipv6_sip=${src_ipv6_a}
    # #run and check the packets.
    # send receive and check ixia results
    # #Cleanup
    # #close connection to traffic generator   ${tgen1_name}

# Ethernet 2 ipv6 vlanstack packet test
    # [Tags]    IXIA   ENET2   IPV6  VLANSTACK
    # #SETUP
    # #set up ixia
    # clear tx port
    # ${vlan_tag_list_1}=  create list  ${svlan_id_a}  ${svlan_id_b}
    # ${vlan_pri_list_1}=  create list  ${svlan_pri_a}  ${svlan_pri_a}
    # #Procedure
    # create ethernet2 ipv6 vlanstack packet   ${packet_name_a}    ${dest_mac_a}  ${src_mac_a}  ether_type=0x800  length=${length}  ipv6_dip=${dest_ipv6_a}  ipv6_sip=${src_ipv6_a}  vlanstack_count=${svlan_count_a}  vlanstack_ids=${vlan_tag_list_1}  vlanstack_priorities=${vlan_pri_list_1}
    # #run and check the packets.
    # send receive and check ixia results
    # #Cleanup
    # #close connection to traffic generator   ${tgen1_name}

# Ethernet 2 ipv6 tcp packet test
    # [Tags]    IXIA   ENET2   IPV6   TCP
    # #SETUP
    # #set up ixia
    # clear tx port
    # #Procedure
    # create ethernet2 ipv6 tcp packet   ${packet_name_a}    ${dest_mac_a}  ${src_mac_a}  ether_type=0x800  length=${length}  ipv6_dip=${dest_ipv6_a}  ipv6_sip=${src_ipv6_a}  src_port=${src_port_a}  dst_port=${dest_port_a}
    # #run and check the packets.
    # send receive and check ixia results
    # #Cleanup
    # #close connection to traffic generator   ${tgen1_name}

# Ethernet 2 ipv6 tcp tagged packet test
    # [Tags]    IXIA   ENET2   IPV6  TCP  TAGGED
    # #SETUP
    # #set up ixia
    # clear tx port
    # #Procedure
    # create ethernet2 ipv6 tagged tcp packet   ${packet_name_a}    ${dest_mac_a}  ${src_mac_a}  ether_type=0x800  length=${length}  ipv6_dip=${dest_ipv6_a}  ipv6_sip=${src_ipv6_a}  src_port=${src_port_a}  dst_port=${dest_port_a}
    # #run and check the packets.
    # send receive and check ixia results
    # #Cleanup
    # #close connection to traffic generator   ${tgen1_name}

# Ethernet 2 ipv6 tcp vlanstack packet test
    # [Tags]    IXIA    ENET2   IPV6  TCP  VLANSTACK
    # #SETUP
    # #set up ixia
    # clear tx port
    # ${vlan_tag_list_1}=  create list  ${svlan_id_a}  ${svlan_id_b}
    # ${vlan_pri_list_1}=  create list  ${svlan_pri_a}  ${svlan_pri_a}
    # #Procedure
    # create ethernet2 ipv6 vlanstack tcp packet   ${packet_name_a}    ${dest_mac_a}  ${src_mac_a}  ether_type=0x800  length=${length}  ipv6_dip=${dest_ipv6_a}  ipv6_sip=${src_ipv6_a}  src_port=${src_port_a}  dst_port=${dest_port_a}  vlanstack_count=${svlan_count_a}  vlanstack_ids=${vlan_tag_list_1}  vlanstack_priorities=${vlan_pri_list_1}
    # #run and check the packets.
    # send receive and check ixia results
    # #Cleanup
    # #close connection to traffic generator   ${tgen1_name}

# Ethernet 2 ipv6 udp packet test
    # [Tags]    IXIA   ENET2   IPV6  UDP
    # #SETUP
    # #set up ixia
    # clear tx port
    # #Procedure
    # create ethernet2 ipv6 udp packet   ${packet_name_a}    ${dest_mac_a}  ${src_mac_a}  ether_type=0x800  length=${length}  ipv6_dip=${dest_ipv6_a}  ipv6_sip=${src_ipv6_a}  src_port=${src_port_a}  dst_port=${dest_port_a}
    # #run and check the packets.
    # send receive and check ixia results
    # #Cleanup
    # #close connection to traffic generator   ${tgen1_name}

# Ethernet 2 ipv6 udp tagged packet test
    # [Tags]    IXIA   ENET2   IPV6  UDP  TAGGED
    # #SETUP
    # #set up ixia
    # clear tx port
    # #Procedure
    # create ethernet2 ipv6 tagged udp packet   ${packet_name_a}    ${dest_mac_a}  ${src_mac_a}  ether_type=0x800  length=${length}  ipv6_dip=${dest_ipv6_a}  ipv6_sip=${src_ipv6_a}  src_port=${src_port_a}  dst_port=${dest_port_a}
    # #run and check the packets.
    # send receive and check ixia results
    # #Cleanup
    # #close connection to traffic generator   ${tgen1_name}

# Ethernet 2 ipv6 udp vlanstack packet test
    # [Tags]    IXIA   ENET2   IPV6  UDP  VLANSTACK
    # #SETUP
    # #set up ixia
    # clear tx port
    # ${vlan_tag_list_1}=  create list  ${svlan_id_a}  ${svlan_id_b}
    # ${vlan_pri_list_1}=  create list  ${svlan_pri_a}  ${svlan_pri_a}
    # #Procedure
    # create ethernet2 ipv6 vlanstack udp packet   ${packet_name_a}    ${dest_mac_a}  ${src_mac_a}  ether_type=0x800  length=${length}  ipv6_dip=${dest_ipv6_a}  ipv6_sip=${src_ipv6_a}  src_port=${src_port_a}  dst_port=${dest_port_a}  vlanstack_count=${svlan_count_a}  vlanstack_ids=${vlan_tag_list_1}  vlanstack_priorities=${vlan_pri_list_1}
    # #run and check the packets.
    # send receive and check ixia results
    # #Cleanup
    # #close connection to traffic generator   ${tgen1_name}

# cleanup and closedown
    # #Cleanup
    # close connection to traffic generator   ${tgen1_name}
