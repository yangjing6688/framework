from ExtremeAutomation.Keywords.NetworkElementKeywords.GeneratedKeywords.NetworkElementSpanningtreeGenKeywords import NetworkElementSpanningtreeGenKeywords


class StpUdks():
    def __init__(self) -> None:
        self.networkElementSpanningtreeGenKeywords = NetworkElementSpanningtreeGenKeywords()

    def Create_MSTI_and_Map_a_VLAN(self, netelem_name,   vlan_id,   mst_instance, **kwargs):
        self.networkElementSpanningtreeGenKeywords.spanningtree_create_mst_instance(netelem_name,   mst_instance, **kwargs)
        self.networkElementSpanningtreeGenKeywords.spanningtree_set_instance_msti(netelem_name,   mst_instance, **kwargs)
        self.networkElementSpanningtreeGenKeywords.spanningtree_enable_mst_instance(netelem_name,   mst_instance, **kwargs)
        self.networkElementSpanningtreeGenKeywords.spanningtree_set_msti_vlan_mapping(netelem_name,   vlan_id,  mst_instance, **kwargs)

    def Clear_MSTMapping_and_Delete_MSTI(self, netelem_name,   vlan_id,  mst_instance, **kwargs):
        self.networkElementSpanningtreeGenKeywords.spanningtree_clear_msti_vlan_mapping(netelem_name,   vlan_id,  mst_instance, **kwargs)
        self.networkElementSpanningtreeGenKeywords.spanningtree_disable_mst_instance(netelem_name,   mst_instance, **kwargs)
        self.networkElementSpanningtreeGenKeywords.spanningtree_delete_mst_instance(netelem_name,   mst_instance, **kwargs)

    def Configure_and_Verify_MSTI_Priority(self,  netelem_name,   priority_value,   msti_id=0, **kwargs):
        self.networkElementSpanningtreeGenKeywords.spanningtree_set_priority(netelem_name,   priority_value,   msti_id, **kwargs)
        self.networkElementSpanningtreeGenKeywords.spanningtree_verify_bridge_priority(netelem_name,   priority_value,   msti_id, **kwargs)

    def Verify_Netelem_Root_and_Root_Port(self, netelem_name,   root_mac,    root_port,   msti_id=0, **kwargs):
        self.networkElementSpanningtreeGenKeywords.spanningtree_verify_root_bridge(netelem_name,   root_mac,    msti_id, **kwargs)
        self.networkElementSpanningtreeGenKeywords.spanningtree_verify_root_port(netelem_name,   root_port,   msti_id, **kwargs)

    def Disable_Mstp_on_Port_and_Verify_it_is_Disabled(self, netelem_name,  port, **kwargs):
        self.networkElementSpanningtreeGenKeywords.spanningtree_disable_mstp_on_port(netelem_name,  port, **kwargs)
        self.networkElementSpanningtreeGenKeywords.spanningtree_verify_mstp_disabled_on_port(netelem_name,  port, **kwargs)
