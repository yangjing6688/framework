from ExtremeAutomation.Keywords.NetworkElementKeywords.GeneratedKeywords.NetworkElementVlanGenKeywords \
    import NetworkElementVlanGenKeywords


class VlanUdks():
    def __init__(self):
        self.networkElementVlanGenKeywords = NetworkElementVlanGenKeywords()

    def Create_VLAN_and_Verify_it_Exists(self, netelem_name, vlan, **kwargs):
        """ Description: Creates the specified VLAN ID and Verify it Exists. """
        self.networkElementVlanGenKeywords.vlan_create_vlan(netelem_name, vlan, **kwargs)
        self.networkElementVlanGenKeywords.vlan_verify_exists(netelem_name, vlan, **kwargs)
        
    def Create_VLAN_with_Name_and_Verify_it_Exists(self, netelem_name, vlan_name, vlan_id, **kwargs):
        self.networkElementVlanGenKeywords.vlan_create_vlan_with_name(netelem_name, vlan_name, vlan_id, **kwargs)
        self.networkElementVlanGenKeywords.vlan_verify_name_and_id(netelem_name, vlan_name, vlan_id, **kwargs)  

    def Create_VLAN_and_Expect_Error(self, netelem_name, vlan, **kwargs):
        """ creates vlan(s) and expect error """
        self.networkElementVlanGenKeywords.vlan_create_vlan(netelem_name, vlan, expect_error=True)

    def Create_VMAN_and_Verify_it_Exists(self, netelem_name, vman, **kwargs):
        """ creates vman(s) and verifies it exists """
        self.networkElementVlanGenKeywords.vlan_create_vman(netelem_name, vman, **kwargs)
        self.networkElementVlanGenKeywords.vlan_verify_vman_exists(netelem_name, vman, **kwargs)

    def Create_VLAN_and_Add_Ports_Tagged_then_Verify(self, netelem_name, vlan_id, ports, **kwargs):
        self.Create_VLAN_and_Verify_it_Exists(netelem_name, vlan_id, **kwargs)
        self.Add_Ports_to_Tagged_Egress_for_VLAN_and_Verify_it_is_Added(netelem_name, vlan_id, ports, **kwargs)

    def Create_VLAN_with_Name_and_Add_Ports_Tagged_then_Verify(self, netelem_name, vlan_name, vlan_id, ports, **kwargs):
        self.Create_VLAN_with_Name_and_Verify_it_Exists(netelem_name, vlan_name, vlan_id, **kwargs)
        self.Add_Ports_to_Tagged_Egress_for_VLAN_and_Verify_it_is_Added(netelem_name, vlan_id, ports, **kwargs)

    def Create_VLAN_and_Add_Ports_Untagged_then_Verify(self, netelem_name, vlan_id, ports, **kwargs):
        self.Create_VLAN_and_Verify_it_Exists(netelem_name, vlan_id, **kwargs)
        self.Add_Ports_to_Untagged_Egress_for_VLAN_and_Verify_it_is_Added(netelem_name, vlan_id, ports, **kwargs)
        self.networkElementVlanGenKeywords.vlan_set_pvid(netelem_name, ports, vlan_id, 'modify-egress', **kwargs)

    def Create_VLAN_with_Name_and_Add_Ports_Untagged_then_Verify(self, netelem_name, vlan_name, vlan_id, ports, **kwargs):
        self.Create_VLAN_with_Name_and_Verify_it_Exists(netelem_name, vlan_name, vlan_id)
        self.Add_Ports_to_Untagged_Egress_for_VLAN_and_Verify_it_is_Added(netelem_name, vlan_id, ports, **kwargs)
        self.networkElementVlanGenKeywords.vlan_set_pvid(netelem_name, ports, vlan_id, **kwargs)

    def Configure_Vlan_Nsi_and_Verify_it_is_Set(self, netelem_names, vlan, vlan_nsi, **kwargs):
        """ Configures a Vlan NSI value and verifies it is set """
        self.networkElementVlanGenKeywords.vlan_set_nsi(netelem_names, vlan, vlan_nsi, **kwargs)
        self.networkElementVlanGenKeywords.vlan_verify_nsi_exists(netelem_names, vlan, vlan_nsi, **kwargs)

    def Configure_Vlan_Isid_and_Verify_it_is_Set(self, netelem_names, vlan, i_sid, **kwargs):
        """ Configures a Vlan Isid value and verifies it is set """
        self.networkElementVlanGenKeywords.vlan_set_isid(netelem_names, vlan, i_sid, **kwargs)
        self.networkElementVlanGenKeywords.vlan_verify_isid_exists(netelem_names, vlan, i_sid, **kwargs)

    def Remove_VLAN_and_Expect_Error(self, netelem_name, vlan, **kwargs):
        """ removes vlan(s) and expects error(s) """
        self.networkElementVlanGenKeywords.vlan_delete_vlan(netelem_name, vlan=vlan, expect_error=True)

    def Remove_VLAN_and_Ignore_CLI_Feedback(self, netelem_name, vlan, **kwargs):
        """ removes vlan(s) and expects error(s) """
        self.networkElementVlanGenKeywords.vlan_delete_vlan(netelem_name, vlan, ignore_cli_feedback=True)

    def Remove_VLAN_and_Verify_it_is_Removed(self, netelem_name, vlan, **kwargs):
        self.networkElementVlanGenKeywords.vlan_delete_vlan(netelem_name, vlan, **kwargs)
        self.networkElementVlanGenKeywords.vlan_verify_does_not_exist(netelem_name, vlan, **kwargs)

    def Remove_VLAN_and_Verify_it_is_Removed_Ignore_CLI_Feedback(self, netelem_name, vlan, **kwargs):
        """ removes vlan(s) and verifies it does not exist """
        self.networkElementVlanGenKeywords.vlan_delete_vlan(netelem_name, vlan, ignore_cli_feedback=True)
        self.networkElementVlanGenKeywords.vlan_verify_does_not_exist(netelem_name, vlan, **kwargs)

    def Remove_VMAN_and_Verify_it_is_Removed(self,netelem_name, vman, **kwargs):
        """ removes vman(s) and verifies it does not exist """
        self.networkElementVlanGenKeywords.vlan_delete_vman(netelem_name, vman, **kwargs)
        self.networkElementVlanGenKeywords.vlan_verify_vman_does_not_exist(netelem_name, vman, **kwargs)

    def Add_Ports_to_Untagged_Egress_for_VLAN_and_Verify_it_is_Added(self, netelem_name, vlan, port, **kwargs):
        self.networkElementVlanGenKeywords.vlan_set_egress_untagged(netelem_name, vlan, port, **kwargs)
        self.networkElementVlanGenKeywords.vlan_verify_port_on_untagged_egress(netelem_name, vlan, port, wait_for=True, max_wait=60)

    def Add_Ports_to_Untagged_Egress_for_VLAN_and_Verify_it_is_Added_to_Static_Egress(self, netelem_name, vlan, port, **kwargs):
        self.networkElementVlanGenKeywords.vlan_set_egress_untagged(netelem_name, vlan, port, **kwargs)
        self.networkElementVlanGenKeywords.vlan_verify_port_on_static_untagged_egress(netelem_name, vlan, port, **kwargs)

    def Add_Ports_to_Untagged_Egress_for_VLAN_and_Set_PVID_then_Verify(self, netelem_name, vlan, port, **kwargs):
        self.Add_PORT_to_Untagged_Egress_for_VLAN_and_Verify_it_is_Added(netelem_name, vlan, port, **kwargs)
        self.Set_PVID_and_Verify_it_is_Set(netelem_name, port, vlan, **kwargs)

    def Add_Ports_to_Untagged_Egress_for_VLAN_and_set_PVID_then_Verify_Static_Egress(self, netelem_name, vlan, port, **kwargs):
        self.Add_Ports_to_Untagged_Egress_for_VLAN_and_Verify_it_is_Added_to_Static_Egress(netelem_name, vlan, port, **kwargs)
        self.Set_PVID_and_Verify_it_is_Set(netelem_name, port, vlan, **kwargs)

    def Remove_Ports_from_Untagged_Egress_for_VLAN_and_Verify_it_is_Removed(self, netelem_name, vlan, port, **kwargs):
        self.networkElementVlanGenKeywords.vlan_clear_egress(netelem_name, vlan, port, **kwargs)
        self.networkElementVlanGenKeywords.vlan_verify_port_not_on_untagged_egress(netelem_name, vlan, port, **kwargs)

    def Add_Ports_to_Tagged_Egress_for_VLAN_and_Verify_it_is_Added(self, netelem_name, vlan, port, **kwargs):
        self.networkElementVlanGenKeywords.vlan_set_egress_tagged(netelem_name, vlan, port, **kwargs)
        self.networkElementVlanGenKeywords.vlan_verify_port_on_tagged_egress(netelem_name, vlan, port, wait_for=True)

    def Add_Ports_to_Tagged_Egress_for_VLAN_and_Verify_it_is_Added_to_Static_Egress(self, netelem_name, vlan, port, **kwargs):
        self.networkElementVlanGenKeywords.vlan_set_egress_tagged(netelem_name, vlan, port, **kwargs)
        self.networkElementVlanGenKeywords.vlan_verify_port_on_static_tagged_egress(netelem_name, vlan, port, **kwargs)

    def Remove_Ports_from_Tagged_Egress_for_VLAN_and_Verify_it_is_Removed(self, netelem_name, vlan, port, **kwargs):
        self.networkElementVlanGenKeywords.vlan_clear_egress(netelem_name, vlan, port, **kwargs)
        self.networkElementVlanGenKeywords.vlan_verify_port_not_on_tagged_egress(netelem_name, vlan, port, **kwargs)

    def Add_Port_Untagged_for_VMAN_and_Verify_it_is_Added(self, netelem_name, vlan, port, **kwargs):
        self.networkElementVlanGenKeywords.vlan_set_vman_egress_untagged(netelem_name, vlan, port, **kwargs)
        self.networkElementVlanGenKeywords.vlan_verify_port_on_vman_untagged(netelem_name, vlan, port, wait_for=True)

    def Add_Port_Tagged_for_VMAN_and_Verify_it_is_Added(self, netelem_name, vlan, port, **kwargs):
        self.networkElementVlanGenKeywords.vlan_set_vman_egress_tagged(netelem_name, vlan, port, **kwargs)
        self.networkElementVlanGenKeywords.vlan_verify_port_on_vman_tagged(netelem_name, vlan, port, wait_for=True)

    def Set_PVID_and_Verify_it_is_Set(self, netelem_name, port, pvid, **kwargs):
        self.networkElementVlanGenKeywords.vlan_set_pvid(netelem_name, port, pvid, 'modify-egress', **kwargs)
        self.networkElementVlanGenKeywords.vlan_verify_port_pvid(netelem_name, port, pvid, **kwargs)

    def Clear_PVID_and_Verify_it_is_Cleared(self, netelem_name, port, vlan, **kwargs):
        self.networkElementVlanGenKeywords.vlan_clear_pvid(netelem_name, port, **kwargs)
        self.networkElementVlanGenKeywords.vlan_verify_port_pvid(netelem_name, port, '1', **kwargs)

    def Set_VLAN_Name_and_Verify_it_is_not_Set(self, netelem_name, vlan, vlan_name, **kwargs):
        self.networkElementVlanGenKeywords.vlan_set_name(netelem_name, vlan, vlan_name, **kwargs)
        self.networkElementVlanGenKeywords.vlan_verify_name_is_not(netelem_name, vlan, vlan_name, **kwargs)

    def Set_VLAN_Name_and_Verify_it_is_Set(self, netelem_name, vlan, vlan_name, **kwargs):
        self.networkElementVlanGenKeywords.vlan_set_name(netelem_name, vlan, vlan_name, **kwargs)
        self.networkElementVlanGenKeywords.vlan_verify_name(netelem_name, vlan, vlan_name, **kwargs)

    def Set_VLAN_Name_and_Expect_Error(self, netelem_name, vlan, vlan_name, **kwargs):
        self.networkElementVlanGenKeywords.vlan_set_name(netelem_name, vlan, vlan_name, expect_error=True)
        self.networkElementVlanGenKeywords.vlan_verify_name_is_not(netelem_name, vlan, vlan_name, **kwargs)

    def Set_VLAN_Description_and_Verify_it_is_Set(self, netelem_name, vlan, vlan_name, **kwargs):
        self.networkElementVlanGenKeywords.vlan_set_description(netelem_name, vlan, vlan_name, **kwargs)
        self.networkElementVlanGenKeywords.vlan_verify_description(netelem_name, vlan, vlan_name, **kwargs)

    def Clear_VLAN_Name_and_Verify_it_is_Removed(self, netelem_name, vlan, vlan_name, **kwargs):
        self.networkElementVlanGenKeywords.vlan_clear_name(netelem_name, vlan, **kwargs)
        self.networkElementVlanGenKeywords.vlan_verify_name_is_not(netelem_name, vlan, vlan_name, **kwargs)

    def Clear_VLAN_Description_and_Verify_it_is_Removed(self, netelem_name, vlan, vlan_name, **kwargs):
        self.networkElementVlanGenKeywords.vlan_clear_description(netelem_name, vlan, **kwargs)
        self.networkElementVlanGenKeywords.vlan_verify_description_is_not(netelem_name, vlan, vlan_name, **kwargs)

    def Disable_VLAN_and_Validate_it_is_Disabled(self, netelem_name, vlan, **kwargs):
        self.networkElementVlanGenKeywords.vlan_disable_vlan(netelem_name, vlan, **kwargs)
        self.networkElementVlanGenKeywords.vlan_verify_disabled(netelem_name, vlan, **kwargs)

    def Disable_VLAN_and_Validate_it_is_Still_Enabled(self, netelem_name, vlan, **kwargs):
        self.networkElementVlanGenKeywords.vlan_disable_vlan(netelem_name, vlan, **kwargs)
        self.networkElementVlanGenKeywords.vlan_verify_enabled(netelem_name, vlan, **kwargs)

    def Enable_VLAN_and_Validate_it_is_Enabled(self, netelem_name, vlan, **kwargs):
        self.networkElementVlanGenKeywords.vlan_enable_vlan(netelem_name, vlan, **kwargs)
        self.networkElementVlanGenKeywords.vlan_verify_enabled(netelem_name, vlan, **kwargs)

    def Enable_VLAN_and_Verify_Error_is_Seen(self, netelem_name, vlan, **kwargs):
        self.networkElementVlanGenKeywords.vlan_enable_vlan(netelem_name, vlan, expect_error=True)

    def Disable_VLAN_and_Verify_Error_is_Seen(self, netelem_name, vlan, **kwargs):
        self.networkElementVlanGenKeywords.vlan_disable_vlan(netelem_name, vlan, expect_error=True)

    def Remove_Vlan_Nsi_and_Verify_it_is_Removed(self, netelem_names, vlan, vlan_nsi, **kwargs):
        """ Removes a Vlan NSI value and verifies it is removed """
        self.networkElementVlanGenKeywords.vlan_clear_nsi(netelem_names, vlan, vlan_nsi, **kwargs)
        self.networkElementVlanGenKeywords.vlan_verify_nsi_does_not_exist(netelem_names, vlan, vlan_nsi, **kwargs)

    def Remove_Vlan_Isid_and_Verify_it_is_Removed(self, netelem_names, vlan, i_sid=None, **kwargs):
        """ Removes a Vlan Isid value and verifies it is removed """
        self.networkElementVlanGenKeywords.vlan_clear_isid(netelem_names, vlan, i_sid, **kwargs)
        self.networkElementVlanGenKeywords.vlan_verify_isid_does_not_exist(netelem_names, vlan, i_sid, **kwargs)

    def Remove_Port_From_Default_Vlan_and_Verify_it_is_Removed(self, netelem_name, port, **kwargs):
        """ Removes a port from the default vlan and verifies it is removed """
        self.networkElementVlanGenKeywords.vlan_clear_member(netelem_name, port, 1, **kwargs)
        self.networkElementVlanGenKeywords.vlan_verify_port_is_not_member_of_vlan(netelem_name, port, 1, **kwargs)

    def Configure_Vlan_Name_and_Verify_Name(self, netelem_name, vlan, name, **kwargs):
        """ Assigns a name to an existing vlan and verifies the name. """
        self.networkElementVlanGenKeywords.vlan_set_name(netelem_name, vlan, name, **kwargs)
        self.networkElementVlanGenKeywords.vlan_verify_name(netelem_name, vlan, name, **kwargs)

    def Configure_Port_Encapsulation_Dot1q_and_Verify_it_is_Set(self, netelem_name, port, **kwargs):
        """ Configures a port as a trunk port and verifies it is set properly. """
        self.networkElementVlanGenKeywords.vlan_set_port_encapsulation_dot1q(netelem_name, port, **kwargs)
        self.networkElementVlanGenKeywords.vlan_verify_port_encapsulation_dot1q(netelem_name, port, **kwargs)

    def Create_Spbm_Vlan_and_Verify_it_Exists(self, netelem_name, vlan, **kwargs):
        """ Creates an SPBM vlan and verifies it is created. """
        self.networkElementVlanGenKeywords.vlan_create_spbm(netelem_name, vlan, **kwargs)
        self.networkElementVlanGenKeywords.vlan_verify_exists(netelem_name, vlan, **kwargs)

    def Remove_Port_Encapsulation_Dot1q_and_Verify_it_is_Removed(self, netelem_name, port, **kwargs):
        """ Configures a port as an access port and verifies it is set properly. """
        self.networkElementVlanGenKeywords.vlan_clear_port_encapsulation_dot1q(netelem_name, port, **kwargs)
        self.networkElementVlanGenKeywords.vlan_verify_port_encapsulation_not_dot1q(netelem_name, port, **kwargs)
