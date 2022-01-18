from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.NetworkEmulatingLldpApi import NetworkEmulatingLldpApi
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


class JetsLldpApi(NetworkEmulatingLldpApi):
    def __init__(self, device):
        super(JetsLldpApi, self).__init__(device)

    def create_lldp_interface(self, port_string, router_id, mac_address, chassis_mac, ttl):
        try:
            dev = self.get_device()
            prt_id = dev.get_port_index_from_group_string(port_string)
            routername = self.__get_lldp_router_name(port_string, router_id)
            # lldp create lldpSim1 -device 1 -mac 00:00:fa:fa:16:01 -chassisMac 00:fa:fa:16:01:00 -ttl 120
            config_isis_ext_ip_reach = " -device " + str(prt_id) + \
                                       " -mac " + str(mac_address) + \
                                       " -chassisMac " + str(chassis_mac) + \
                                       " -ttl " + str(ttl)
            self.send_command("lldp create " + routername + " " + config_isis_ext_ip_reach)
        except Exception:
            self.logger.log_info(StringUtils.exception_to_string())

    def remove_lldp_interface(self, port_string, router_id):
        # lldpSim3 delete
        try:
            dev = self.get_device()
            prt_id = dev.get_port_index_from_group_string(port_string)
            routername = self.__get_lldp_router_name(port_string, router_id)
            self.send_command(routername + " delete ")
        except Exception:
            self.logger.log_info(StringUtils.exception_to_string())

    def enable_lldp(self, port_string, router_id, enabled=True):
        # lldpSim3 delete
        try:
            dev = self.get_device()
            prt_id = dev.get_port_index_from_group_string(port_string)
            routername = self.__get_lldp_router_name(port_string, router_id)
            if enabled:
                self.send_command(routername + " enable ")
            else:
                self.send_command(routername + " disable -sendPduWithZeroTtl true ")
        except Exception:
            self.logger.log_info(StringUtils.exception_to_string())

    def start_transmit_tlv(self, port_string, router_id, tlv_name):
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " txTlv -tlv " + tlv_name)

    def stop_transmit_tlv(self, port_string, router_id, tlv_name):
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " stopTxTlv -tlv " + tlv_name)

    ########################################
    # ####### sys-name #####################
    ########################################
    def add_lldp_tlv_sys_name(self, port_string, router_id, value):
        tlv_type = "sys-name"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " setAttributes -sysName \"" + str(value) + "\"")

    def remove_lldp_tlv_sys_name(self, port_string, router_id, value):
        tlv_type = "sys-name"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " disable -sendPduWithZeroTtl true")

    def start_tlv_sys_name(self, port_string, router_id):
        tlv_type = "sys-name"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " txTlv -tlv " + tlv_type)

    def stop_tlv_sys_name(self, port_string, router_id):
        tlv_type = "sys-name"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " stopTxTlv -tlv " + tlv_type)

    ########################################
    # ####### sys-desc #####################
    ########################################
    def add_lldp_tlv_sys_desc(self, port_string, router_id, value):
        tlv_type = "sys-desc"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " setAttributes -sysDesc \"" + str(value) + "\"")

    def remove_lldp_tlv_sys_desc(self, port_string, router_id, value):
        tlv_type = "sys-desc"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " disable -sendPduWithZeroTtl true")

    def start_tlv_sys_desc(self, port_string, router_id):
        tlv_type = "sys-desc"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " txTlv -tlv " + tlv_type)

    def stop_tlv_sys_desc(self, port_string, router_id):
        tlv_type = "sys-desc"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " stopTxTlv -tlv " + tlv_type)

    ########################################
    # ####### sys-cap ######################
    ########################################
    def add_lldp_tlv_sys_cap(self, port_string, router_id, cap_support, cap_enabled):
        tlv_type = "sys-cap"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " setAttributes -capSupported " + str(cap_support) + " -capEnabled " +
                          str(cap_enabled))

    def remove_lldp_tlv_sys_cap(self, port_string, router_id, value):
        tlv_type = "sys-cap"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " disable -sendPduWithZeroTtl true")

    def start_tlv_sys_cap(self, port_string, router_id):
        tlv_type = "sys-cap"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " txTlv -tlv " + tlv_type)

    def stop_tlv_sys_cap(self, port_string, router_id):
        tlv_type = "sys-cap"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " stopTxTlv -tlv " + tlv_type)

    ########################################
    # ####### port-desc ####################
    ########################################
    def add_lldp_tlv_port_desc(self, port_string, router_id, value):
        tlv_type = "port-desc"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " setAttributes -portDesc \"" + str(value) + "\"")

    def remove_lldp_tlv_port_desc(self, port_string, router_id, value):
        tlv_type = "port-desc"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " disable -sendPduWithZeroTtl true")

    def start_tlv_port_desc(self, port_string, router_id):
        tlv_type = "port-desc"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " txTlv -tlv " + tlv_type)

    def stop_tlv_port_desc(self, port_string, router_id):
        tlv_type = "port-desc"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " stopTxTlv -tlv " + tlv_type)

    ########################################
    # ####### local-mgmt-addr ##############
    ########################################
    # lldpSim1 addLclMgmtAddr -lclMgmtAddr 192.168.1.1 -lclMgmtPort 1/1 -lclMgmtOid 1.3.1.4.1.2272.1.8.2.1.2.64
    # http://avaya-svn.extremenetworks.com/svn/nes/Jets/trunk/src/com/nortel/jets/jetsTcl/lldp/AddLclMgmtLldpCmd.java
    def add_lldp_tlv_local_mgmt_addr(self, port_string, router_id, local_management_address, local_management_port,
                                     local_management_oid):
        tlv_type = "local-mgmt-addr"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " addLclMgmtAddr -lclMgmtAddr " + str(local_management_address) +
                                       " -lclMgmtPort " + str(local_management_port) +
                                       " -lclMgmtOid " + str(local_management_oid))

    # http://avaya-svn.extremenetworks.com/svn/nes/Jets/trunk/src/com/nortel/jets/jetsTcl/lldp/RemoveLclMgmtLldpCmd.java
    def remove_lldp_tlv_local_mgmt_addr(self, port_string, router_id, local_management_address, local_management_port):
        tlv_type = "local-mgmt-addr"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " removeLclMgmtAddr -lclMgmtAddr " + str(local_management_address) +
                          " -lclMgmtPort " + str(local_management_port))

    def start_tlv_local_mgmt_addr(self, port_string, router_id):
        tlv_type = "local-mgmt-addr"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " txTlv -tlv " + tlv_type)

    def stop_tlv_local_mgmt_addr(self, port_string, router_id):
        tlv_type = "local-mgmt-addr"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " stopTxTlv -tlv " + tlv_type)

    ########################################
    # ####### dot1-port-vlan-id ############
    ########################################
    def add_lldp_tlv_dot1_port_vlan_id(self, port_string, router_id, value):
        tlv_type = "dot1-port-vlan-id"
        # http://avaya-svn.extremenetworks.com/svn/nes/Jets/trunk/src/com/nortel/jets/jetsTcl/lldp/
        #   SetDot1LldpAttributesCmd.java
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " setDot1Attributes -pvid " + str(value))

    def remove_lldp_tlv_dot1_port_vlan_id(self, port_string, router_id, value):
        tlv_type = "dot1-port-vlan-id"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command("fix this")

    def start_tlv_dot1_port_vlan_id(self, port_string, router_id):
        tlv_type = "dot1-port-vlan-id"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " txTlv -tlv " + tlv_type)

    def stop_tlv_dot1_port_vlan_id(self, port_string, router_id):
        tlv_type = "dot1-port-vlan-id"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " stopTxTlv -tlv " + tlv_type)

    #############################################
    # ####### dot1-protocol-identity ############
    #############################################
    def add_lldp_tlv_dot1_protocol_identity(self, port_string, router_id, value):
        tlv_type = "dot1-protocol-identity"
        # http://avaya-svn.extremenetworks.com/svn/nes/Jets/trunk/src/com/nortel/jets/jetsTcl/lldp/
        #   AddDot1ProtoIdLldpCmd.java
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " addDot1ProtoId -protoId " + str(value))

    def remove_lldp_tlv_dot1_protocol_identity(self, port_string, router_id, value):
        tlv_type = "dot1-protocol-identity"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " removeDot1ProtoId -protoId " + str(value))

    def start_tlv_dot1_protocol_identity(self, port_string, router_id):
        tlv_type = "dot1-protocol-identity"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " txTlv -tlv " + tlv_type)

    def stop_tlv_dot1_protocol_identity(self, port_string, router_id):
        tlv_type = "dot1-protocol-identity"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " stopTxTlv -tlv " + tlv_type)

    #################################################
    # ####### dot1-port-protocol-vlan-id ############
    #################################################
    # http://avaya-svn.extremenetworks.com/svn/nes/Jets/trunk/src/com/nortel/jets/jetsTcl/lldp/
    #   AddDot1PortProtocolVlanLldpCmd.java
    # addDot1PortProtocol -vlanId <vlanId> -supported <supported> - <enabled>
    def add_lldp_tlv_dot1_port_protocol_vlan_id(self, port_string, router_id, vlan_id, supported, enabled):
        tlv_type = "dot1-port-protocol-vlan-id"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " addDot1PortProtocol -vlanId " + str(vlan_id) + " -supported " +
                          str(supported) + " -enabled " + str(enabled))

    # http://avaya-svn.extremenetworks.com/svn/nes/Jets/trunk/src/com/nortel/jets/jetsTcl/lldp/
    #   RemoveDot1PortProtocolVlanLldpCmd.java
    def remove_lldp_tlv_dot1_port_protocol_vlan_id(self, port_string, router_id, vlan_id):
        tlv_type = "dot1-port-protocol-vlan-id"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " removeDot1PortProtocol -vlanId " + str(vlan_id))

    def start_tlv_dot1_port_protocol_vlan_id(self, port_string, router_id):
        tlv_type = "dot1-port-protocol-vlan-id"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " txTlv -tlv " + tlv_type)

    def stop_tlv_dot1_port_protocol_vlan_id(self, port_string, router_id):
        tlv_type = "dot1-port-protocol-vlan-id"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " stopTxTlv -tlv " + tlv_type)

    ########################################
    # ####### dot1-vlan-name ###############
    ########################################
    def add_lldp_tlv_dot1_vlan_name(self, port_string, router_id, vlan_id, vlan_name):
        # http://avaya-svn.extremenetworks.com/svn/nes/Jets/trunk/src/com/nortel/jets/jetsTcl/lldp/
        #   AddDot1VlanNameLldpCmd.java
        # addDot1VlanName -vlanId <id> -vlanName <nam>
        tlv_type = "dot1-vlan-name"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " addDot1VlanName -vlanId " + str(vlan_id) + " -vlanname " + str(vlan_name))

    # http://avaya-svn.extremenetworks.com/svn/nes/Jets/trunk/src/com/nortel/jets/jetsTcl/lldp/
    #   RemoveDot1VlanNameLldpCmd.java
    def remove_lldp_tlv_dot1_vlan_name(self, port_string, router_id, vlan_id):
        tlv_type = "dot1-vlan-name"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " removeDot1VlanName -vlanId " + str(vlan_id))

    def start_tlv_dot1_vlan_name(self, port_string, router_id):
        tlv_type = "dot1-vlan-name"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " txTlv -tlv " + tlv_type)

    def stop_tlv_dot1_vlan_name(self, port_string, router_id):
        tlv_type = "dot1-vlan-name"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " stopTxTlv -tlv " + tlv_type)

    #################################################
    # ####### dot3-mac-phy-config-status ############
    #################################################
    def add_lldp_tlv_dot3_mac_phy_config_status(self, port_string, router_id, auto_neg_supported, auto_neg_enabled,
                                                auto_neg_ad_cap, op_mau_type):
        tlv_type = "dot3-mac-phy-config-status"
        # http://avaya-svn.extremenetworks.com/svn/nes/Jets/trunk/src/com/nortel/jets/jetsTcl/lldp/
        #   SetDot3LldpAttributesCmd.java
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " setDot3Attributes -autoNegSupported " + str(auto_neg_supported) +
                          " -autoNegEnabled " + str(auto_neg_enabled) +
                          " -autoNegAdCap " + str(auto_neg_ad_cap) +
                          " -opMauType " + str(op_mau_type))

    def remove_lldp_tlv_dot3_mac_phy_config_status(self, port_string, router_id, value):
        tlv_type = "dot3-mac-phy-config-status"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command("fix this")

    def start_tlv_dot3_mac_phy_config_status(self, port_string, router_id):
        tlv_type = "dot3-mac-phy-config-status"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " txTlv -tlv " + tlv_type)

    def stop_tlv_dot3_mac_phy_config_status(self, port_string, router_id):
        tlv_type = "dot3-mac-phy-config-status"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " stopTxTlv -tlv " + tlv_type)

    ########################################
    # ####### dot3-power-mdi ###############
    ########################################
    def add_lldp_tlv_dot3_power_mdi(self, port_string, router_id, mdi_power_support, pse_power_pair, power_class):
        tlv_type = "dot3-power-mdi"
        # http://avaya-svn.extremenetworks.com/svn/nes/Jets/trunk/src/com/nortel/jets/jetsTcl/lldp/
        #   SetDot3LldpAttributesCmd.java
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " setDot3Attributes -mdiPowerSupport " + str(mdi_power_support) +
                          " -psePowerPair " + str(pse_power_pair) +
                          " -powerClass " + str(power_class))

    def remove_lldp_tlv_dot3_power_mdi(self, port_string, router_id, value):
        tlv_type = "dot3-power-mdi"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command("fix this")

    def start_tlv_dot3_power_mdi(self, port_string, router_id):
        tlv_type = "dot3-power-mdi"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " txTlv -tlv " + tlv_type)

    def stop_tlv_dot3_power_mdi(self, port_string, router_id):
        tlv_type = "dot3-power-mdi"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " stopTxTlv -tlv " + tlv_type)

    ############################################
    # ####### dot3-link-aggregation ############
    ############################################
    def add_lldp_tlv_dot3_link_aggregation(self, port_string, router_id, aggregation_supported, aggregation_enabled,
                                           aggregation_id):
        tlv_type = "dot3-link-aggregation"
        # http://avaya-svn.extremenetworks.com/svn/nes/Jets/trunk/src/com/nortel/jets/jetsTcl/lldp/
        #   SetDot3LldpAttributesCmd.java
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " setDot3Attributes -aggrSupported " + str(aggregation_supported) +
                          " -aggrEnabled " + str(aggregation_enabled) +
                          " -aggrId " + str(aggregation_id))

    def remove_lldp_tlv_dot3_link_aggregation(self, port_string, router_id, value):
        tlv_type = "dot3-link-aggregation"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command("fix this")

    def start_tlv_dot3_link_aggregation(self, port_string, router_id):
        tlv_type = "dot3-link-aggregation"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " txTlv -tlv " + tlv_type)

    def stop_tlv_dot3_link_aggregation(self, port_string, router_id):
        tlv_type = "dot3-link-aggregation"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " stopTxTlv -tlv " + tlv_type)

    ##############################################
    # ####### dot3-maximum-frame-size ############
    ##############################################
    def add_lldp_tlv_dot3_maximum_frame_size(self, port_string, router_id, value):
        tlv_type = "dot3-maximum-frame-size"
        # http://avaya-svn.extremenetworks.com/svn/nes/Jets/trunk/src/com/nortel/jets/jetsTcl/lldp/
        #   SetDot3LldpAttributesCmd.java
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " setDot3Attributes -maxFrameSize " + str(value))

    def remove_lldp_tlv_dot3_maximum_frame_size(self, port_string, router_id, value):
        tlv_type = "dot3-maximum-frame-size"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command("fix this")

    def start_tlv_dot3_maximum_frame_size(self, port_string, router_id):
        tlv_type = "dot3-maximum-frame-size"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " txTlv -tlv " + tlv_type)

    def stop_tlv_dot3_maximum_frame_size(self, port_string, router_id):
        tlv_type = "dot3-maximum-frame-size"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " stopTxTlv -tlv " + tlv_type)

    ########################################
    # ####### fa-elem ######################
    ########################################
    def add_lldp_tlv_fa_elem(self, port_string, router_id, element_type, state, sys_id, conn_type, port_mlt_id,
                             mgmt_vlan):
        tlv_type = "fa-elem"
        # http://avaya-svn.extremenetworks.com/svn/nes/Jets/trunk/src/com/nortel/jets/jetsTcl/lldp/AddFaElemLldpCmd.java
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " addFaElem -elemType " + str(element_type) +
                          " -state " + str(state) +
                          " -sysId " + str(sys_id) +
                          " -connType " + str(conn_type) +
                          " -portMltId " + str(port_mlt_id) +
                          " -mgmtVlan " + str(mgmt_vlan))

    def remove_lldp_tlv_fa_elem(self, port_string, router_id, value):
        tlv_type = "fa-elem"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command("fix this")

    def start_tlv_fa_elem(self, port_string, router_id):
        tlv_type = "fa-elem"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " txTlv -tlv " + tlv_type)

    def stop_tlv_fa_elem(self, port_string, router_id):
        tlv_type = "fa-elem"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " stopTxTlv -tlv " + tlv_type)

    ##############################################
    # ####### fa-isid-vlan-assignment ############
    ##############################################
    def add_lldp_tlv_fa_isid_vlan_assignment(self, port_string, router_id, status, vlan, isid, n_mappings, vlan_step,
                                             isid_step):
        tlv_type = "fa-isid-vlan-assignment"
        # http://avaya-svn.extremenetworks.com/svn/nes/Jets/trunk/src/com/nortel/jets/jetsTcl/lldp/
        #   AddFaIsidVlanAssignmentLldpCmd.java
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " addFaIsidVlanAssignment -status " + str(status) +
                          " -vlan " + str(vlan) +
                          " -isid " + str(isid) +
                          " -nMappings " + str(n_mappings) +
                          " -vlanStep " + str(vlan_step) +
                          " -isidStep " + str(isid_step))

    def remove_lldp_tlv_fa_isid_vlan_assignment(self, port_string, router_id, value):
        tlv_type = "fa-isid-vlan-assignment"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command("fix this")

    def start_tlv_fa_isid_vlan_assignment(self, port_string, router_id):
        tlv_type = "fa-isid-vlan-assignment"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " txTlv -tlv " + tlv_type)

    def stop_tlv_fa_isid_vlan_assignment(self, port_string, router_id):
        tlv_type = "fa-isid-vlan-assignment"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " stopTxTlv -tlv " + tlv_type)

    ########################################
    # ####### med-capabilites ##############
    ########################################
    def add_lldp_tlv_med_capabilites(self, port_string, router_id, capabilty, network_policy, location_id,
                                     extended_power_pse, extended_power_pd, inventory, device_type):
        tlv_type = "med-capabilites"
        # http://avaya-svn.extremenetworks.com/svn/nes/Jets/trunk/src/com/nortel/jets/jetsTcl/lldp/
        #   SetMedLldpAttributesCmd.java
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " setMedAttributes -capabilty " + str(capabilty) +
                          " -networkPolicy " + str(network_policy) +
                          " -locationId " + str(location_id) +
                          " -extendedPowerPse " + str(extended_power_pse) +
                          " -extendedPowerPd " + str(extended_power_pd) +
                          " -inventory " + str(inventory) +
                          " -deviceType " + str(device_type))

    def remove_lldp_tlv_med_capabilites(self, port_string, router_id, value):
        tlv_type = "med-capabilites"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command("fix this")

    def start_tlv_med_capabilites(self, port_string, router_id):
        tlv_type = "med-capabilites"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " txTlv -tlv " + tlv_type)

    def stop_tlv_med_capabilites(self, port_string, router_id):
        tlv_type = "med-capabilites"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " stopTxTlv -tlv " + tlv_type)

    #########################################
    # ####### med-network-policy ############
    #########################################
    def add_lldp_tlv_med_network_policy(self, port_string, router_id, network_policy_action, app_ttype, unknown, tagged,
                                        vlan_id, l2_priority, dscp):
        tlv_type = "med-network-policy"
        # http://avaya-svn.extremenetworks.com/svn/nes/Jets/trunk/src/com/nortel/jets/jetsTcl/lldp/
        #   SetMedLldpAttributesCmd.java
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " setMedAttributes -networkPolicyAction " + str(network_policy_action) +
                          " -appType " + str(app_ttype) +
                          " -unknown " + str(unknown) +
                          " -tagged " + str(tagged) +
                          " -vlanId " + str(vlan_id) +
                          " -l2Priority " + str(l2_priority) +
                          " -dscp " + str(dscp))

    def remove_lldp_tlv_med_network_policy(self, port_string, router_id, value):
        tlv_type = "med-network-policy"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command("fix this")

    def start_tlv_med_network_policy(self, port_string, router_id):
        tlv_type = "med-network-policy"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " txTlv -tlv " + tlv_type)

    def stop_tlv_med_network_policy(self, port_string, router_id):
        tlv_type = "med-network-policy"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " stopTxTlv -tlv " + tlv_type)

    ########################################
    # ####### med-location-id ##############
    ########################################
    def add_lldp_tlv_med_location_id(self, port_string, router_id, coordinate_loc_action, civic_loc_action,
                                     ecs_elin_loc_action, coordinate_loc, civic_loc, ecs_elin_loc):
        tlv_type = "med-location-id"
        # http://avaya-svn.extremenetworks.com/svn/nes/Jets/trunk/src/com/nortel/jets/jetsTcl/lldp/
        #   SetMedLldpAttributesCmd.java
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " setMedAttributes -coordinateLocAction " + str(coordinate_loc_action) +
                          " -civicLocAction " + str(civic_loc_action) +
                          " -ecsElinLocAction " + str(ecs_elin_loc_action) +
                          " -coordinateLoc " + str(coordinate_loc) +
                          " -civicLoc " + str(civic_loc) +
                          " -ecsElinLoc " + str(ecs_elin_loc))

    def remove_lldp_tlv_med_location_id(self, port_string, router_id, value):
        tlv_type = "med-location-id"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command("fix this")

    def start_tlv_med_location_id(self, port_string, router_id):
        tlv_type = "med-location-id"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " txTlv -tlv " + tlv_type)

    def stop_tlv_med_location_id(self, port_string, router_id):
        tlv_type = "med-location-id"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " stopTxTlv -tlv " + tlv_type)

    ########################################
    # ####### med-power-via-mdi ############
    ########################################
    def add_lldp_tlv_med_power_via_mdi(self, port_string, router_id, power_type, power_src, power_priority,
                                       power_value):
        tlv_type = "med-power-via-mdi"
        # http://avaya-svn.extremenetworks.com/svn/nes/Jets/trunk/src/com/nortel/jets/jetsTcl/lldp/
        #   SetMedLldpAttributesCmd.java
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " setMedAttributes -powerType " + str(power_type) +
                          " -powerSrc " + str(power_src) +
                          " -powerPriority " + str(power_priority) +
                          " -powerValue " + str(power_value))

    def remove_lldp_tlv_med_power_via_mdi(self, port_string, router_id, value):
        tlv_type = "med-power-via-mdi"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command("fix this")

    def start_tlv_med_power_via_mdi(self, port_string, router_id):
        tlv_type = "med-power-via-mdi"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " txTlv -tlv " + tlv_type)

    def stop_tlv_med_power_via_mdi(self, port_string, router_id):
        tlv_type = "med-power-via-mdi"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " stopTxTlv -tlv " + tlv_type)

    ########################################
    # ####### med-hw-revision ##############
    ########################################
    def add_lldp_tlv_med_hw_revision(self, port_string, router_id, value):
        tlv_type = "med-hw-revision"
        # http://avaya-svn.extremenetworks.com/svn/nes/Jets/trunk/src/com/nortel/jets/jetsTcl/lldp/
        #   SetMedLldpAttributesCmd.java
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " setMedAttributes -hwRevision " + str(value))
        # hwRevision

    def remove_lldp_tlv_med_hw_revision(self, port_string, router_id, value):
        tlv_type = "med-hw-revision"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command("fix this")

    def start_tlv_med_hw_revision(self, port_string, router_id):
        tlv_type = "med-hw-revision"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " txTlv -tlv " + tlv_type)

    def stop_tlv_med_hw_revision(self, port_string, router_id):
        tlv_type = "med-hw-revision"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " stopTxTlv -tlv " + tlv_type)

    ############################################
    # ####### med-firmware-revision ############
    ############################################
    def add_lldp_tlv_med_firmware_revision(self, port_string, router_id, value):
        tlv_type = "med-firmware-revision"
        # http://avaya-svn.extremenetworks.com/svn/nes/Jets/trunk/src/com/nortel/jets/jetsTcl/lldp/
        #   SetMedLldpAttributesCmd.java
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " setMedAttributes -firmwareRevision " + str(value))
        # firmwareRevision

    def remove_lldp_tlv_med_firmware_revision(self, port_string, router_id, value):
        tlv_type = "med-firmware-revision"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command("fix this")

    def start_tlv_med_firmware_revision(self, port_string, router_id):
        tlv_type = "med-firmware-revision"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " txTlv -tlv " + tlv_type)

    def stop_tlv_med_firmware_revision(self, port_string, router_id):
        tlv_type = "med-firmware-revision"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " stopTxTlv -tlv " + tlv_type)

    ############################################
    # ####### med-software-revision ############
    ############################################
    def add_lldp_tlv_med_software_revision(self, port_string, router_id, value):
        tlv_type = "med-software-revision"
        # http://avaya-svn.extremenetworks.com/svn/nes/Jets/trunk/src/com/nortel/jets/jetsTcl/lldp/
        #   SetMedLldpAttributesCmd.java
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " setMedAttributes -softwareRevision " + str(value))
        # softwareRevision

    def remove_lldp_tlv_med_software_revision(self, port_string, router_id, value):
        tlv_type = "med-software-revision"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command("fix this")

    def start_tlv_med_software_revision(self, port_string, router_id):
        tlv_type = "med-software-revision"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " txTlv -tlv " + tlv_type)

    def stop_tlv_med_software_revision(self, port_string, router_id):
        tlv_type = "med-software-revision"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " stopTxTlv -tlv " + tlv_type)

    ########################################
    # ####### med-serial-number ############
    ########################################
    def add_lldp_tlv_med_serial_number(self, port_string, router_id, value):
        tlv_type = "med-serial-number"
        # http://avaya-svn.extremenetworks.com/svn/nes/Jets/trunk/src/com/nortel/jets/jetsTcl/lldp/
        #   SetMedLldpAttributesCmd.java
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " setMedAttributes -serialNum " + str(value))
        #     serialNum

    def remove_lldp_tlv_med_serial_number(self, port_string, router_id, value):
        tlv_type = "med-serial-number"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command("fix this")

    def start_tlv_med_serial_number(self, port_string, router_id):
        tlv_type = "med-serial-number"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " txTlv -tlv " + tlv_type)

    def stop_tlv_med_serial_number(self, port_string, router_id):
        tlv_type = "med-serial-number"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " stopTxTlv -tlv " + tlv_type)

    ########################################
    # ####### med-mfg-name #################
    ########################################
    def add_lldp_tlv_med_mfg_name(self, port_string, router_id, value):
        tlv_type = "med-mfg-name"
        # http://avaya-svn.extremenetworks.com/svn/nes/Jets/trunk/src/com/nortel/jets/jetsTcl/lldp/
        #   SetMedLldpAttributesCmd.java
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " setMedAttributes -mfgName " + str(value))
        # mfgName

    def remove_lldp_tlv_med_mfg_name(self, port_string, router_id, value):
        tlv_type = "med-mfg-name"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command("fix this")

    def start_tlv_med_mfg_name(self, port_string, router_id):
        tlv_type = "med-mfg-name"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " txTlv -tlv " + tlv_type)

    def stop_tlv_med_mfg_name(self, port_string, router_id):
        tlv_type = "med-mfg-name"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " stopTxTlv -tlv " + tlv_type)

    ########################################
    # ####### med-model-name ###############
    ########################################
    def add_lldp_tlv_med_model_name(self, port_string, router_id, value):
        tlv_type = "med-model-name"
        # http://avaya-svn.extremenetworks.com/svn/nes/Jets/trunk/src/com/nortel/jets/jetsTcl/lldp/
        #   SetMedLldpAttributesCmd.java
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " setMedAttributes -modelName " + str(value))
        # modelName

    def remove_lldp_tlv_med_model_name(self, port_string, router_id, value):
        tlv_type = "med-model-name"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command("fix this")

    def start_tlv_med_model_name(self, port_string, router_id):
        tlv_type = "med-model-name"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " txTlv -tlv " + tlv_type)

    def stop_tlv_med_model_name(self, port_string, router_id):
        tlv_type = "med-model-name"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " stopTxTlv -tlv " + tlv_type)

    ########################################
    # ####### med-asset-id ############
    ########################################
    def add_lldp_tlv_med_asset_id(self, port_string, router_id, value):
        tlv_type = "med-asset-id"
        # http://avaya-svn.extremenetworks.com/svn/nes/Jets/trunk/src/com/nortel/jets/jetsTcl/lldp/
        #   SetMedLldpAttributesCmd.java
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " setMedAttributes -assetId " + str(value))
        # assetId

    def remove_lldp_tlv_med_asset_id(self, port_string, router_id, value):
        tlv_type = "med-asset-id"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command("fix this")

    def start_tlv_med_asset_id(self, port_string, router_id):
        tlv_type = "med-asset-id"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " txTlv -tlv " + tlv_type)

    def stop_tlv_med_asset_id(self, port_string, router_id):
        tlv_type = "med-asset-id"
        routername = self.__get_lldp_router_name(port_string, router_id)
        self.send_command(routername + " stopTxTlv -tlv " + tlv_type)

    def __get_lldp_router_name(self, port_string, router_id):
        return ("simLldp_" + str(port_string) + "_" +
                str(router_id)).replace(" ", "_").replace(".", "_").replace(":", "_")
