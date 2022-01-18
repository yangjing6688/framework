from ExtremeAutomation.Keywords.NetworkElementKeywords.GeneratedKeywords.NetworkElementSpbmGenKeywords import NetworkElementSpbmGenKeywords


class SpbmUdks():
    def __init__(self) -> None:
        self.networkElementSpbmGenKeywords = NetworkElementSpbmGenKeywords()

    def Enable_Spbm_Globally_and_Verify_it_is_Enabled(self, netelem_name, **kwargs):
        """  Globally_Enables_Spbm_and_verifies_it_is_enabled """
        self.networkElementSpbmGenKeywords.spbm_enable_global(netelem_name, **kwargs)
        self.networkElementSpbmGenKeywords.spbm_verify_globally_enabled(netelem_name, **kwargs)

    def Disable_Spbm_Globally_and_Verify_it_is_Disabled(self, netelem_name, **kwargs):
        """  Globally_Disables_Spbm_and_verifies_it_is_disabled """
        self.networkElementSpbmGenKeywords.spbm_disable_global(netelem_name, **kwargs)
        self.networkElementSpbmGenKeywords.spbm_verify_globally_disabled(netelem_name, **kwargs)

    def Create_Spbm_Instance_and_Verify_it_Exists(self, netelem_name,  spbm_id, **kwargs):
        """  Creates_an_Spbm_Instance_and_verifies_it_is_created """
        self.networkElementSpbmGenKeywords.spbm_set_isis_instance_id(netelem_name, spbm_id, **kwargs)
        self.networkElementSpbmGenKeywords.spbm_verify_instance_exists(netelem_name, spbm_id, **kwargs)

    def Configure_Spbm_Nickname_and_Verify_it_Exists(self, netelem_name, spbm_id, nickname, **kwargs):
        """  Creates_an_Spbm_Nickname_and_verifies_it_is_created """
        self.networkElementSpbmGenKeywords.spbm_set_isis_nickname(netelem_name,  spbm_id,  nickname, **kwargs)
        self.networkElementSpbmGenKeywords.spbm_verify_nickname(netelem_name,  spbm_id,  nickname, **kwargs)

    def Configure_Spbm_Vlans_and_Verify_They_are_Set(self, netelem_name,  spbm_id,  primary_vlan,  secondary_vlan, **kwargs):
        """  Configures_the_primary_and_secondary_SPBM_VLAN_and_verifies_they_are_configured """
        self.networkElementSpbmGenKeywords.spbm_set_isis_bvid(netelem_name,  spbm_id,  primary_vlan,  secondary_vlan, **kwargs)
        self.networkElementSpbmGenKeywords.spbm_verify_vlan_exists(netelem_name,  spbm_id,  primary_vlan, **kwargs)
        self.networkElementSpbmGenKeywords.spbm_verify_vlan_exists(netelem_name,  spbm_id,  secondary_vlan, **kwargs)

    def Create_Isis_Spbm_Instance_on_Port_and_Verify_it_Exists(self, netelem_name,  port,  spbm_id, **kwargs):
        """  Creates_an_IS-IS_SPBM_instance_on_a_port_and_verifies_it_exists """
        self.networkElementSpbmGenKeywords.spbm_set_port_isis_instance_id(netelem_name,  port,  spbm_id, **kwargs)
        self.networkElementSpbmGenKeywords.spbm_verify_isis_instance_exists_on_port(netelem_name,  port,  spbm_id, **kwargs)

    def Create_Isis_Spbm_Instance_on_Mlt_and_Verify_it_Exists(self, netelem_name,  mlt_id,  spbm_id, **kwargs):
        """  Creates_an_IS-IS_SPBM_instance_on_an_MLT_and_verifies_it_exists """
        self.networkElementSpbmGenKeywords.spbm_set_mlt_isis_instance_id(netelem_name,  mlt_id,  spbm_id, **kwargs)
        self.networkElementSpbmGenKeywords.spbm_verify_isis_instance_exists_on_mlt(netelem_name,  mlt_id,  spbm_id, **kwargs)

    def Configure_Isis_Spbm_L1_Metric_On_Port_and_Verify_it_is_Set(self, netelem_name,  port,  spbm_id,  metric, **kwargs):
        """  Configures_an_IS-IS_SPBM_L1_metric_on_a_port_and_verifies_it_is_set """
        self.networkElementSpbmGenKeywords.spbm_set_port_isis_l1_metric(netelem_name,  port,  spbm_id,  metric, **kwargs)
        self.networkElementSpbmGenKeywords.spbm_verify_isis_l1_metric_on_port(netelem_name,  port,  spbm_id,  metric, **kwargs)

    def Configure_Isis_Spbm_L1_Metric_On_Mlt_and_Verify_it_is_Set(self, netelem_name,  mlt,  spbm_id,  metric, **kwargs):
        """  Configures_an_IS-IS_SPBM_L1_metric_on_an_MLT_and_verifies_it_is_set """
        self.networkElementSpbmGenKeywords.spbm_set_mlt_isis_l1_metric(netelem_name,  mlt,  spbm_id,  metric, **kwargs)
        self.networkElementSpbmGenKeywords.spbm_verify_isis_l1_metric_on_mlt(netelem_name,  mlt,  spbm_id,  metric, **kwargs)

    def Remove_Spbm_Vlans_and_Verify_They_are_Removed(self, netelem_name,  spbm_id,  primary_vlan,  secondary_vlan, **kwargs):
        """  Removes_the_primary_and_secondary_SPBM_VLAN_and_verifies_they_are_removed """
        self.networkElementSpbmGenKeywords.spbm_clear_isis_bvid(netelem_name,  spbm_id,  primary_vlan,  secondary_vlan, **kwargs)
        self.networkElementSpbmGenKeywords.spbm_verify_vlan_does_not_exist(netelem_name,  spbm_id,  primary_vlan, **kwargs)
        self.networkElementSpbmGenKeywords.spbm_verify_vlan_does_not_exist(netelem_name,  spbm_id,  secondary_vlan, **kwargs)

    def Remove_Isis_Spbm_Instance_on_Port_and_Verify_it_is_Removed(self, netelem_name,  port,  spbm_id, **kwargs):
        """  Removes_an_IS-IS_SPBM_instance_on_a_port_and_verifies_it_is_removed """
        self.networkElementSpbmGenKeywords.spbm_clear_port_isis_instance_id(netelem_name,  port,  spbm_id, **kwargs)
        self.networkElementSpbmGenKeywords.spbm_verify_isis_instance_does_not_exist_on_port(netelem_name,  port,  spbm_id, **kwargs)

    def Remove_Spbm_Instance_and_Verify_it_is_Removed(self, netelem_name,  spbm_id, **kwargs):
        """  Deletes_an_Spbm_instance_and_verifies_it_is_deleted """
        self.networkElementSpbmGenKeywords.spbm_clear_isis_instance_id(netelem_name,  spbm_id, **kwargs)
        self.networkElementSpbmGenKeywords.spbm_verify_instance_does_not_exist(netelem_name,  spbm_id, **kwargs)

    def Remove_Isis_Spbm_Instance_on_Mlt_and_Verify_it_is_Removed(self, netelem_name,  mlt_id,  spbm_id, **kwargs):
        """  Removes_an_IS-IS_SPBM_instance_on_an_MLT_and_verifies_it_is_removed """
        self.networkElementSpbmGenKeywords.spbm_clear_mlt_isis_instance_id(netelem_name,  mlt_id,  spbm_id, **kwargs)
        self.networkElementSpbmGenKeywords.spbm_verify_isis_instance_does_not_exist_on_mlt(netelem_name,  mlt_id,  spbm_id, **kwargs)

    ######################################################################################################################
    #                                           VERIFICATION_UDKS                                                        #
    ######################################################################################################################
    def Verify_Isis_Spbm_Unicast_Fib_Entry_is_Present(self, netelem_name,  da,  bvlan,  sys_id,  hostname=None,  port=None,  cost=None, **kwargs):
        """  Verifies_that_an_entry_in_the_isis_spbm_unicast-fib_table_is_present_on_the_device """

        self.networkElementSpbmGenKeywords.spbm_verify_isis_unicast_fib_host_name(netelem_name,  da,  bvlan, sys_id,  hostname, **kwargs)
        self.networkElementSpbmGenKeywords.spbm_verify_isis_unicast_fib_cost(netelem_name,  da,  bvlan, sys_id,  cost, **kwargs)
        self.networkElementSpbmGenKeywords.spbm_verify_isis_unicast_fib_outgoing_port(netelem_name,  da,  bvlan, sys_id,  port, **kwargs)

    def Verify_Isis_Spbm_Multicast_Fib_Entry_is_Present(self, netelem_name,  da,  isid,  bvlan,  sys_id,  hostname=None, out_port=None, in_port=None, **kwargs):
        """  Verifies_that_an_entry_in_the_isis_spbm_multicast-fib_table_is_present_on_the_device """
        self.networkElementSpbmGenKeywords.spbm_verify_isis_multicast_fib_host_name(netelem_name,  da,  isid, sys_id,  bvlan,  hostname, **kwargs)
        self.networkElementSpbmGenKeywords.spbm_verify_isis_multicast_fib_outbound_port(netelem_name,  da,  isid, sys_id,  bvlan,  out_port, **kwargs)
        self.networkElementSpbmGenKeywords.spbm_verify_isis_multicast_fib_inbound_port(netelem_name,  da,  isid, sys_id,  bvlan,  in_port, **kwargs)

    def Verify_Isis_Spbm_Ip_Unicast_Fib_Grt_Entry_is_Present(self, netelem_name, dest, nh_beb, bvlan, out_int, spbm_cost, prefix_cost,
                   prefix_type, ip_route_pref, vrf_isid, dest_isid, nh_bmac, **kwargs):
        """  Verifies_that_an_entry_in_the_isis_spbm_ip_unicast-fib_table_is_present_on_the_device """
        self.networkElementSpbmGenKeywords.spbm_verify_isis_ip_unicast_fib_destination_network(netelem_name,  dest,    nh_beb,   bvlan, **kwargs)
        self.networkElementSpbmGenKeywords.spbm_verify_isis_ip_unicast_fib_nh_beb(netelem_name,  dest,    nh_beb,   bvlan, **kwargs)
        self.networkElementSpbmGenKeywords.spbm_verify_isis_ip_unicast_fib_bvlan(netelem_name,  dest,    nh_beb,   bvlan, **kwargs)
        self.networkElementSpbmGenKeywords.spbm_verify_isis_ip_unicast_fib_outgoing_port(netelem_name,  dest,    nh_beb,   bvlan, out_int, **kwargs)
        self.networkElementSpbmGenKeywords.spbm_verify_isis_ip_unicast_fib_spbm_cost(netelem_name,  dest,    nh_beb,   bvlan, spbm_cost, **kwargs)
        self.networkElementSpbmGenKeywords.spbm_verify_isis_ip_unicast_fib_prefix_cost(netelem_name,  dest,    nh_beb,   bvlan, prefix_cost, **kwargs)
        self.networkElementSpbmGenKeywords.spbm_verify_isis_ip_unicast_fib_prefix_type(netelem_name,  dest,    nh_beb,   bvlan, prefix_type, **kwargs)
        self.networkElementSpbmGenKeywords.spbm_verify_isis_ip_unicast_fib_ip_route_preference(netelem_name,  dest,    nh_beb,   bvlan, ip_route_pref, **kwargs)
        self.networkElementSpbmGenKeywords.spbm_verify_isis_ip_unicast_fib_vrf_isid(netelem_name,  dest,    nh_beb,   bvlan, vrf_isid, **kwargs)
        self.networkElementSpbmGenKeywords.spbm_verify_isis_ip_unicast_fib_destination_network_isid(netelem_name,  dest,    nh_beb,   bvlan, dest_isid, **kwargs)
        self.networkElementSpbmGenKeywords.spbm_verify_isis_ip_unicast_fib_nh_bmac(netelem_name,  dest,    nh_bmac,  bvlan, **kwargs)

    def Verify_Isis_Spbm_Ipv6_Unicast_Fib_Grt_Entry_is_Present(self, netelem_name,  dest,  nh_beb,  bvlan,   out_int,     spbm_cost,  prefix_cost, **kwargs):
        """  Verifies_that_an_entry_in_the_isis_spbm_ipv6_unicast-fib_table_is_present_on_the_device """
        self.networkElementSpbmGenKeywords.spbm_verify_isis_ipv6_unicast_fib_destination_network(netelem_name,  dest,    nh_beb,   bvlan, **kwargs)
        self.networkElementSpbmGenKeywords.spbm_verify_isis_ipv6_unicast_fib_nh_beb(netelem_name,  dest,    nh_beb,   bvlan, **kwargs)
        self.networkElementSpbmGenKeywords.spbm_verify_isis_ipv6_unicast_fib_bvlan(netelem_name,  dest,    nh_beb,   bvlan, **kwargs)
        self.networkElementSpbmGenKeywords.spbm_verify_isis_ipv6_unicast_fib_outgoing_port(netelem_name,  dest,    nh_beb,   bvlan, out_int, **kwargs)
        self.networkElementSpbmGenKeywords.pbm_Verify_Isis_Ipv6_Unicast_Fib_Spbm_Cost(netelem_name,  dest,    nh_beb,   bvlan, spbm_cost, **kwargs)
        self.networkElementSpbmGenKeywords.spbm_verify_isis_ipv6_unicast_fib_prefix_cost(netelem_name,  dest,    nh_beb,   bvlan, prefix_cost, **kwargs)

    def Verify_Isis_Spbm_Ip_Unicast_Fib_Entry_by_Isid(self, netelem_name,  vrf_name,  isid,  dest,  nh_beb,    bvlan,   out_int,  spbm_cost, prefix_cost,   prefix_type,
                                                      ip_route_pref,  vrf_isid,   dest_isid, **kwargs):
        """  Verifies_ip_unicast-fib_table_entries_are_present_for_the_specified_i-sid """
        self.networkElementSpbmGenKeywords.spbm_verify_isis_ip_unicast_fib_vrf_name_by_vrf_name_and_id(netelem_name,  vrf_name,  isid,  dest, netelem_name,  vrf_name, 
                                                                                                       isid, dest,  nh_beb,    bvlan,   out_int,  spbm_cost, prefix_cost,
                                                                                                       prefix_type,   ip_route_pref,  vrf_isid,   dest_isid,  nh_beb,       
                                                                                                       bvlan, **kwargs)
        self.networkElementSpbmGenKeywords.spbm_verify_isis_ip_unicast_fib_dest_network_by_vrf_name_and_id(netelem_name,  vrf_name,  isid,  dest, nh_beb, bvlan, **kwargs)
        self.networkElementSpbmGenKeywords.spbm_verify_isis_ip_unicast_fib_nh_beb_by_vrf_name_and_id(netelem_name,  vrf_name,  isid,  dest, nh_beb, bvlan, **kwargs)
        self.networkElementSpbmGenKeywords.spbm_verify_isis_ip_unicast_fib_bvlan_by_vrf_name_and_id(netelem_name,  vrf_name,  isid,  dest, nh_beb, bvlan, **kwargs)
        self.networkElementSpbmGenKeywords.spbm_verify_isis_ip_unicast_fib_out_int_port_by_vrf_name_and_id(netelem_name,  vrf_name,  isid,  dest, nh_beb, bvlan, out_int, **kwargs)
        self.networkElementSpbmGenKeywords.spbm_verify_isis_ip_unicast_fib_spbm_cost_by_vrf_name_and_id(netelem_name,  vrf_name,  isid,  dest, nh_beb,        bvlan,     spbm_cost, **kwargs)
        self.networkElementSpbmGenKeywords.spbm_verify_isis_ip_unicast_fib_prefix_cost_by_vrf_name_and_id(netelem_name,  vrf_name,  isid,  dest, nh_beb, bvlan, prefix_cost, **kwargs)
        self.networkElementSpbmGenKeywords.spbm_verify_isis_ip_unicast_fib_prefix_type_by_vrf_name_and_id(netelem_name,  vrf_name,  isid,  dest, nh_beb, bvlan, prefix_type, **kwargs)
        self.networkElementSpbmGenKeywords.spbm_verify_isis_ip_unicast_fib_ip_route_pref_by_vrf_name_and_id(netelem_name,  vrf_name,  isid,  dest, nh_beb, bvlan, ip_route_pref, **kwargs)
        self.networkElementSpbmGenKeywords.spbm_verify_isis_ip_unicast_fib_vrf_isid_by_vrf_name_and_id(netelem_name,  vrf_name,  isid,  dest, nh_beb, bvlan, vrf_isid, **kwargs)
        self.networkElementSpbmGenKeywords.spbm_verify_isis_ip_unicast_fib_dest_network_isid_by_vrf_name_and_id(netelem_name,  vrf_name,  isid,  dest, nh_beb, bvlan, dest_isid, **kwargs)

    def Verify_Isis_Spbm_Ipv6_Unicast_Fib_Entry_by_Isid(self, netelem_name,  vrf_name,  isid,  dest,  nh_beb,    bvlan,   out_int,  spbm_cost, prefix_cost, **kwargs):
                   
        """  Verifies_ipv6_unicast-fib_table_entries_are_present_for_the_specified_i-sid """
        self.networkElementSpbmGenKeywords.spbm_verify_isis_ipv6_unicast_fib_vrf_name_by_vrf_name_and_id(netelem_name, vrf_name, isid, dest, nh_beb, bvlan, **kwargs)
        self.networkElementSpbmGenKeywords.spbm_verify_isis_ipv6_unicast_fib_dest_network_by_vrf_name_and_id(netelem_name, vrf_name, isid, dest, nh_beb, bvlan, **kwargs)
        self.networkElementSpbmGenKeywords.spbm_verify_isis_ipv6_unicast_fib_nh_beb_by_vrf_name_and_id(netelem_name, vrf_name, isid, dest, nh_beb, bvlan, **kwargs)
        self.networkElementSpbmGenKeywords.spbm_verify_isis_ipv6_unicast_fib_bvlan_by_vrf_name_and_id(netelem_name, vrf_name, isid, dest, nh_beb, bvlan, **kwargs)
        self.networkElementSpbmGenKeywords.spbm_verify_isis_ipv6_unicast_fib_out_int_port_by_vrf_name_and_id(netelem_name, vrf_name, isid, dest, nh_beb, bvlan, out_int, **kwargs)
        self.networkElementSpbmGenKeywords.spbm_verify_isis_ipv6_unicast_fib_spbm_cost_by_vrf_name_and_id(netelem_name, vrf_name, isid, dest, nh_beb, bvlan, spbm_cost, **kwargs)
        self.networkElementSpbmGenKeywords.spbm_verify_isis_ipv6_unicast_fib_prefix_cost_by_vrf_name_and_id(netelem_name, vrf_name, isid, dest, nh_beb, bvlan, prefix_cost, **kwargs)
