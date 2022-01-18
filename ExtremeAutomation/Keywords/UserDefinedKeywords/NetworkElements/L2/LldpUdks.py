from ExtremeAutomation.Keywords.NetworkElementKeywords.GeneratedKeywords.NetworkElementLldpGenKeywords import NetworkElementLldpGenKeywords


class LldpUdks():
    def __init__(self) -> None:
        self.networkElementLldpGenKeywords = NetworkElementLldpGenKeywords()

    def Enable_LLDP_Tx_Rx_and_Verify_it_is_Enabled(self, device_names,  ports, **kwargs):
        self.networkElementLldpGenKeywords.lldp_enable_port_both(device_names,  ports, **kwargs)
        self.Verify_LLDP_Tx_Rx_is_Enabled(device_names,  ports, **kwargs)

    def Disable_LLDP_Tx_Rx_and_Verify_it_is_Disabled(self, device_names,  ports, **kwargs):
        self.networkElementLldpGenKeywords.lldp_disable_port(device_names,  ports, **kwargs)
        self.Verify_LLDP_Tx_Rx_is_Disabled(device_names,  ports, **kwargs)

    def Verify_LLDP_Tx_Rx_is_Enabled(self, device_names,  ports, **kwargs):
        self.networkElementLldpGenKeywords.lldp_verify_transmit_enabled_on_port(device_names,  ports, **kwargs)
        self.networkElementLldpGenKeywords.lldp_verify_receive_enabled_on_port(device_names,  ports, **kwargs)

    def Verify_LLDP_Tx_Rx_is_Disabled(self, device_names,  ports, **kwargs):
        self.networkElementLldpGenKeywords.lldp_verify_transmit_disabled_on_port(device_names,  ports, **kwargs)
        self.networkElementLldpGenKeywords.lldp_verify_receive_disabled_on_port(device_names,  ports, **kwargs)

    def Configure_LLDP_Tx_Interval_and_Verify_it_is_Configured(self, device_names,  interval, **kwargs):
        self.networkElementLldpGenKeywords.lldp_set_tx_interval(device_names,  interval, **kwargs)
        self.networkElementLldpGenKeywords.lldp_verify_tx_interval(device_names,  interval, **kwargs)

    def Clear_LLDP_Tx_Interval_and_Verify_it_is_set_to_Default_Value(self, device_names, **kwargs):
        self.networkElementLldpGenKeywords.lldp_set_tx_interval(device_names,  20, **kwargs)
        self.networkElementLldpGenKeywords.lldp_verify_tx_interval(device_names,  20, **kwargs)

    ########################################################################################################################
    #    LLDP_TLV_Keywords    ##############################################################################################
    ########################################################################################################################
    def Enable_and_Verify_VLAN_ID_TLV(self, netelem_name,   netelem_tgen_port, **kwargs):
        self.networkElementLldpGenKeywords.lldp_enable_tlv_vlan_id(netelem_name,   netelem_tgen_port, **kwargs)
        self.networkElementLldpGenKeywords.lldp_verify_vlan_id_tlv_enabled(netelem_name,   netelem_tgen_port, **kwargs)

    def Disable_and_Verify_VLAN_ID_TLV(self, netelem_name,   netelem_tgen_port, **kwargs):
        self.networkElementLldpGenKeywords.lldp_disable_tlv_vlan_id(netelem_name,   netelem_tgen_port, **kwargs)
        self.networkElementLldpGenKeywords.lldp_verify_vlan_id_tlv_disabled(netelem_name,   netelem_tgen_port, **kwargs)

    def Enable_and_Verify_STP_TLV(self, netelem_name,   netelem_tgen_port, **kwargs):
        self.networkElementLldpGenKeywords.lldp_enable_tlv_stp(netelem_name,   netelem_tgen_port, **kwargs)
        self.networkElementLldpGenKeywords.lldp_verify_stp_tlv_enabled(netelem_name,   netelem_tgen_port, **kwargs)

    def Disable_and_Verify_STP_TLV(self, netelem_name,   netelem_tgen_port, **kwargs):
        self.networkElementLldpGenKeywords.lldp_disable_tlv_stp(netelem_name,   netelem_tgen_port, **kwargs)
        self.networkElementLldpGenKeywords.lldp_verify_stp_tlv_disabled(netelem_name,   netelem_tgen_port, **kwargs)

    def Enable_and_Verify_LACP_TLV(self, netelem_name,   netelem_tgen_port, **kwargs):
        self.networkElementLldpGenKeywords.lldp_enable_tlv_lacp(netelem_name,   netelem_tgen_port, **kwargs)
        self.networkElementLldpGenKeywords.lldp_verify_lacp_tlv_enabled(netelem_name,   netelem_tgen_port, **kwargs)

    def Disable_and_Verify_LACP_TLV(self, netelem_name,   netelem_tgen_port, **kwargs):
        self.networkElementLldpGenKeywords.lldp_disable_tlv_lacp(netelem_name,   netelem_tgen_port, **kwargs)
        self.networkElementLldpGenKeywords.lldp_verify_lacp_tlv_disabled(netelem_name,   netelem_tgen_port, **kwargs)

    def Enable_and_Verify_GVRP_TLV(self, netelem_name,   netelem_tgen_port, **kwargs):
        self.networkElementLldpGenKeywords.lldp_enable_tlv_gvrp(netelem_name,   netelem_tgen_port, **kwargs)
        self.networkElementLldpGenKeywords.lldp_verify_gvrp_tlv_enabled(netelem_name,   netelem_tgen_port, **kwargs)

    def Disable_and_Verify_GVRP_TLV(self, netelem_name,   netelem_tgen_port, **kwargs):
        self.networkElementLldpGenKeywords.lldp_disable_tlv_gvrp(netelem_name,   netelem_tgen_port, **kwargs)
        self.networkElementLldpGenKeywords.lldp_verify_gvrp_tlv_disabled(netelem_name,   netelem_tgen_port, **kwargs)

    def Enable_and_Verify_Link_Aggr_TLV(self, netelem_name,   netelem_tgen_port, **kwargs):
        self.networkElementLldpGenKeywords.lldp_enable_tlv_link_aggr(netelem_name,   netelem_tgen_port, **kwargs)
        self.networkElementLldpGenKeywords.lldp_verify_link_aggr_tlv_enabled(netelem_name,   netelem_tgen_port, **kwargs)

    def Disable_and_Verify_Link_Aggr_TLV(self, netelem_name,   netelem_tgen_port, **kwargs):
        self.networkElementLldpGenKeywords.lldp_disable_tlv_link_aggr(netelem_name,   netelem_tgen_port, **kwargs)
        self.networkElementLldpGenKeywords.lldp_verify_link_aggr_tlv_disabled(netelem_name,   netelem_tgen_port, **kwargs)

    def Enable_and_Verify_MAC_Phy_TLV(self, netelem_name,   netelem_tgen_port, **kwargs):
        self.networkElementLldpGenKeywords.lldp_enable_tlv_mac_phy(netelem_name,   netelem_tgen_port, **kwargs)
        self.networkElementLldpGenKeywords.lldp_verify_mac_phy_tlv_enabled(netelem_name,   netelem_tgen_port, **kwargs)

    def Disable_and_Verify_MAC_Phy_TLV(self, netelem_name,   netelem_tgen_port, **kwargs):
        self.networkElementLldpGenKeywords.lldp_disable_tlv_mac_phy(netelem_name,   netelem_tgen_port, **kwargs)
        self.networkElementLldpGenKeywords.lldp_verify_mac_phy_tlv_disabled(netelem_name,   netelem_tgen_port, **kwargs)

    def Enable_and_Verify_Max_Frame_Size_TLV(self, netelem_name,   netelem_tgen_port, **kwargs):
        self.networkElementLldpGenKeywords.lldp_enable_tlv_max_frame(netelem_name,   netelem_tgen_port, **kwargs)
        self.networkElementLldpGenKeywords.lldp_verify_max_frame_tlv_enabled(netelem_name,   netelem_tgen_port, **kwargs)

    def Disable_and_Verify_Max_Frame_Size_TLV(self, netelem_name,   netelem_tgen_port, **kwargs):
        self.networkElementLldpGenKeywords.lldp_disable_tlv_max_frame(netelem_name,   netelem_tgen_port, **kwargs)
        self.networkElementLldpGenKeywords.lldp_verify_max_frame_tlv_disabled(netelem_name,   netelem_tgen_port, **kwargs)

    def Enable_and_Verify_Enhanced_Tx_Config_TLV(self, netelem_name,   netelem_tgen_port, **kwargs):
        self.networkElementLldpGenKeywords.lldp_enable_tlv_enhanced_trans_config(netelem_name,   netelem_tgen_port, **kwargs)
        self.networkElementLldpGenKeywords.lldp_verify_enhanced_trans_config_tlv_enabled(netelem_name, netelem_tgen_port, **kwargs)

    def Disable_and_Verify_Enhanced_Tx_Config_TLV(self, netelem_name,   netelem_tgen_port, **kwargs):
        self.networkElementLldpGenKeywords.lldp_disable_tlv_enhanced_trans_config(netelem_name,   netelem_tgen_port, **kwargs)
        self.networkElementLldpGenKeywords.lldp_verify_enhanced_trans_config_tlv_disabled(netelem_name, netelem_tgen_port, **kwargs)

    def Enable_and_Verify_Enhanced_Tx_Rec_TLV(self, netelem_name,   netelem_tgen_port, **kwargs):
        self.networkElementLldpGenKeywords.lldp_enable_tlv_enhanced_trans_rec(netelem_name,   netelem_tgen_port, **kwargs)
        self.networkElementLldpGenKeywords.lldp_verify_enhanced_trans_rec_tlv_enabled(netelem_name,   netelem_tgen_port, **kwargs)

    def Disable_and_Verify_Enhanced_Tx_Rec_TLV(self, netelem_name,   netelem_tgen_port, **kwargs):
        self.networkElementLldpGenKeywords.lldp_disable_tlv_enhanced_trans_rec(netelem_name,   netelem_tgen_port, **kwargs)
        self.networkElementLldpGenKeywords.lldp_verify_enhanced_trans_rec_tlv_disabled(netelem_name, netelem_tgen_port, **kwargs)
