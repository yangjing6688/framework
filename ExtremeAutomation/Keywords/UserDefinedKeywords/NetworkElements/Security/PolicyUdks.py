from ExtremeAutomation.Keywords.NetworkElementKeywords.GeneratedKeywords.NetworkElementPolicyGenKeywords import NetworkElementPolicyGenKeywords


class PolicyUdks():
    def __init__(self) -> None:
        self.networkElementPolicyGenKeywords = NetworkElementPolicyGenKeywords()

    def Create_Policy_Profile_and_Verify_it_Exists(self, netelem_name, profile_id, **kwargs):
        self.networkElementPolicyGenKeywords.policy_set_profile(netelem_name, profile_id, **kwargs)
        self.networkElementPolicyGenKeywords.policy_verify_profile_exists(netelem_name, profile_id, **kwargs)

    def Create_Policy_Profile_with_Name_and_Verify_it_Exists(self,  netelem_name, profile_id, name, **kwargs):
        self.networkElementPolicyGenKeywords.policy_set_profile_name(netelem_name, profile_id, name, **kwargs)
        self.networkElementPolicyGenKeywords.policy_verify_profile_name(netelem_name, profile_id, name, **kwargs)

    def Remove_Policy_Profile_and_Verify_it_was_Removed(self, netelem_name, profile_id, **kwargs):
        self.networkElementPolicyGenKeywords.policy_clear_profile(netelem_name, profile_id, **kwargs)
        self.networkElementPolicyGenKeywords.policy_verify_profile_does_not_exist(netelem_name, profile_id, **kwargs)

    def Create_Port_Admin_Profile_and_Verify_it_Exists(self, netelem_name, port, profile_id, **kwargs):
        self.networkElementPolicyGenKeywords.policy_set_port_admin_profile(netelem_name, port, profile_id, **kwargs)
        self.networkElementPolicyGenKeywords.policy_verify_port_admin_profile_exists(netelem_name, port, profile_id, **kwargs)

    def Create_Mac_Source_Admin_Profile_and_Verify_it_was_Created(self, netelem_name, mac_source, port, profile_id, mask=48, **kwargs):
        self.networkElementPolicyGenKeywords.policy_set_mac_source_admin_profile(netelem_name, mac_source, port, profile_id, mask, **kwargs)
        self.networkElementPolicyGenKeywords.policy_verify_mac_source_admin_profile_exists(netelem_name, mac_source, port, profile_id, mask, **kwargs)

    def Remove_Port_Admin_Profile_and_Verify_it_was_Removed(self, netelem_name, port, profile_id, **kwargs):
        self.networkElementPolicyGenKeywords.policy_clear_port_admin_profile(netelem_name, port, **kwargs)
        self.networkElementPolicyGenKeywords.policy_verify_port_admin_profile_does_not_exist(netelem_name, port, profile_id, **kwargs)

    def Remove_Mac_Source_Admin_Profile_and_Verify_it_was_Removed(self, netelem_name, mac_source, port, profile_id, mask=48, **kwargs):
        self.networkElementPolicyGenKeywords.policy_clear_mac_source_admin_profile(netelem_name, mac_source, port, mask, **kwargs)
        self.networkElementPolicyGenKeywords.policy_verify_mac_source_admin_profile_does_not_exist(netelem_name, mac_source, port, profile_id, mask, **kwargs)

    def Enable_Policy_and_Verify_it_is_Enabled(self, netelem_name, **kwargs):
        self.networkElementPolicyGenKeywords.policy_enable(netelem_name, **kwargs)
        self.networkElementPolicyGenKeywords.policy_verify_state_enabled(netelem_name, **kwargs)

    def Disable_Policy_and_Verify_it_is_Disabled(self, netelem_name, **kwargs):
        self.networkElementPolicyGenKeywords.policy_disable(netelem_name, **kwargs)
        self.networkElementPolicyGenKeywords.policy_verify_state_disabled(netelem_name, **kwargs)

    def Set_Policy_Invalid_Action_and_Verify(self, netelem_name, policy_action, **kwargs):
        self.networkElementPolicyGenKeywords.policy_set_invalid(netelem_name, policy_action, **kwargs)
        self.networkElementPolicyGenKeywords.policy_verify_invalid_action(netelem_name, policy_action, **kwargs)

    def Clear_Policy_Invalid_Action_and_Verify(self, netelem_name,  policy_action, **kwargs):
        self.networkElementPolicyGenKeywords.policy_clear_invalid(netelem_name, **kwargs)
        self.networkElementPolicyGenKeywords.policy_verify_invalid_action(netelem_name, policy_action, **kwargs)

    def Set_Policy_Maptable_Response_and_Verify(self, netelem_name, policy_maptable_response, **kwargs):
        self.networkElementPolicyGenKeywords.policy_set_maptable_response(netelem_name, policy_maptable_response, **kwargs)
        self.networkElementPolicyGenKeywords.policy_verify_maptable_response(netelem_name, policy_maptable_response, **kwargs)

    def Clear_Policy_Maptable_Response_and_Verify(self, netelem_name, policy_maptable_response, **kwargs):
        self.networkElementPolicyGenKeywords.policy_clear_maptable_response(netelem_name, **kwargs)
        self.networkElementPolicyGenKeywords.policy_verify_maptable_response(netelem_name, policy_maptable_response, **kwargs)

    def Create_Policy_Profile_with_TCI_Overwrite_Enabled_and_Verify(self, netelem_name, profile_id, **kwargs):
        self.networkElementPolicyGenKeywords.policy_set_profile(netelem_name, profile_id, **kwargs)
        self.networkElementPolicyGenKeywords.policy_verify_profile_exists(netelem_name, profile_id, **kwargs)
        self.networkElementPolicyGenKeywords.policy_set_profile_tci_overwrite(netelem_name, profile_id, 'enable', **kwargs)
        self.networkElementPolicyGenKeywords.policy_verify_profile_tci_overwrite_enabled(netelem_name, profile_id, **kwargs)

    def Create_Policy_Profile_with_TCI_Overwrite_Disabled_and_Verify(self, netelem_name, profile_id, **kwargs):
        self.networkElementPolicyGenKeywords.policy_set_profile(netelem_name, profile_id, **kwargs)
        self.networkElementPolicyGenKeywords.policy_verify_profile_exists(netelem_name, profile_id, **kwargs)
        self.networkElementPolicyGenKeywords.policy_set_profile_tci_overwrite(netelem_name, profile_id, 'disable', **kwargs)
        self.networkElementPolicyGenKeywords.policy_verify_profile_tci_overwrite_disabled(netelem_name, profile_id, **kwargs)

    def Create_Policy_Profile_With_PVID_and_PVID_Status_Enabled(self, netelem_name, profile_id, pvid, **kwargs):
        self.Create_Policy_Profile_and_Verify_it_Exists(netelem_name, profile_id, **kwargs)
        self.networkElementPolicyGenKeywords.policy_set_profile_pvid(netelem_name, profile_id, pvid, **kwargs)
        self.networkElementPolicyGenKeywords.policy_set_profile_pvid_status(netelem_name, profile_id, 'enable', **kwargs)
        self.networkElementPolicyGenKeywords.policy_verify_profile_pvid(netelem_name, profile_id, pvid, **kwargs)
        self.networkElementPolicyGenKeywords.policy_verify_profile_pvid_status_enabled(netelem_name, profile_id, **kwargs)

    def Create_Policy_Profile_with_PVID_and_PVID_Status_Enabled_and_TCI_Overwrite_Disabled(self, netelem_name, profile_id, pvid, **kwargs):
        self.Create_Policy_Profile_With_PVID_and_PVID_Status_Enabled(netelem_name, profile_id, 'pvid', **kwargs)
        self.networkElementPolicyGenKeywords.policy_set_profile_tci_overwrite(netelem_name, profile_id, 'disable', **kwargs)
        self.networkElementPolicyGenKeywords.policy_verify_profile_tci_overwrite_disabled(netelem_name, profile_id, **kwargs)

    def Create_Policy_Profile_with_PVID_and_PVID_Status_Enabled_and_TCI_Overwrite_Enabled(self, netelem_name, profile_id, pvid, **kwargs):
        self.Create_Policy_Profile_With_PVID_and_PVID_Status_Enabled(netelem_name, profile_id, pvid, **kwargs)
        self.networkElementPolicyGenKeywords.policy_set_profile_tci_overwrite(netelem_name, profile_id, 'enable', **kwargs)
        self.networkElementPolicyGenKeywords.policy_verify_profile_tci_overwrite_enabled(netelem_name, profile_id, **kwargs)

    def Create_Policy_Profile_with_COS_and_COS_Status_Enabled(self, netelem_name, profile_id, cos_value, **kwargs):
        self.networkElementPolicyGenKeywords.policy_set_profile(netelem_name, profile_id, **kwargs)
        self.networkElementPolicyGenKeywords.policy_set_profile_cos(netelem_name, profile_id, cos_value, **kwargs)
        self.networkElementPolicyGenKeywords.policy_set_profile_cos_status(netelem_name, profile_id, 'enable', **kwargs)
        self.networkElementPolicyGenKeywords.policy_verify_profile_tci_overwrite_disabled(netelem_name, profile_id, **kwargs)
        self.networkElementPolicyGenKeywords.policy_verify_profile_cos(netelem_name, profile_id, cos_value, **kwargs)
        self.networkElementPolicyGenKeywords.policy_verify_profile_cos_status_enabled(netelem_name, profile_id, **kwargs)

    def Create_Policy_Profile_with_COS_COS_Status_and_TCI_Overwrite_Enabled(self, netelem_name, profile_id, cos_value, **kwargs):
        self.networkElementPolicyGenKeywords.policy_set_profile(netelem_name, profile_id, **kwargs)
        self.networkElementPolicyGenKeywords.policy_set_profile_cos(netelem_name, profile_id, cos_value, **kwargs)
        self.networkElementPolicyGenKeywords.policy_set_profile_cos_status(netelem_name, profile_id, 'enable', **kwargs)
        self.networkElementPolicyGenKeywords.policy_set_profile_tci_overwrite(netelem_name, profile_id, 'enable', **kwargs)
        self.networkElementPolicyGenKeywords.policy_verify_profile_tci_overwrite_enabled(netelem_name, profile_id, **kwargs)
        self.networkElementPolicyGenKeywords.policy_verify_profile_cos(netelem_name, profile_id, cos_value, **kwargs)
        self.networkElementPolicyGenKeywords.policy_verify_profile_cos_status_enabled(netelem_name, profile_id, **kwargs)

    def Create_Policy_Profile_with_PVID_PVID_Status_COS_and_COS_Status_Enabled(self, netelem_name, profile_id, pvid, cos_value, **kwargs):
        self.Create_Policy_Profile_With_PVID_and_PVID_Status_Enabled(netelem_name, profile_id,  pvid, **kwargs)
        self.networkElementPolicyGenKeywords.policy_set_profile_cos(netelem_name, profile_id, cos_value, **kwargs)
        self.networkElementPolicyGenKeywords.policy_set_profile_cos_status(netelem_name, profile_id, 'enable', **kwargs)
        self.networkElementPolicyGenKeywords.policy_verify_profile_cos(netelem_name, profile_id,  cos_value, **kwargs)
        self.networkElementPolicyGenKeywords.policy_verify_profile_cos_status_enabled(netelem_name, profile_id, **kwargs)
        self.networkElementPolicyGenKeywords.policy_verify_profile_tci_overwrite_disabled(netelem_name, profile_id, **kwargs)

    def Create_Policy_Profile_with_PVID_PVID_Status_COS_COS_Status_and_TCI_Overwrite_Enabled(self, netelem_name, profile_id, pvid, cos_value, **kwargs):
        self.Create_Policy_Profile_With_PVID_and_PVID_Status_Enabled(netelem_name, profile_id, pvid, **kwargs)
        self.networkElementPolicyGenKeywords.policy_set_profile_tci_overwrite(netelem_name, profile_id, 'enable', **kwargs)
        self.networkElementPolicyGenKeywords.policy_set_profile_cos(netelem_name, profile_id, cos_value, **kwargs)
        self.networkElementPolicyGenKeywords.policy_set_profile_cos_status(netelem_name, profile_id, 'enable', **kwargs)
        self.networkElementPolicyGenKeywords.policy_verify_profile_cos(netelem_name, profile_id, cos_value, **kwargs)
        self.networkElementPolicyGenKeywords.policy_verify_profile_cos_status_enabled(netelem_name, profile_id, **kwargs)
        self.networkElementPolicyGenKeywords.policy_verify_profile_tci_overwrite_enabled(netelem_name, profile_id, **kwargs)

    def Create_Policy_Profile_Untagged_Vlan_With_Pvid_and_Verify(self, netelem_name, profile_id, pvid, profile_name, **kwargs):
        self.networkElementPolicyGenKeywords.policy_set_profile_name(netelem_name, profile_id, profile_name, **kwargs)
        self.networkElementPolicyGenKeywords.policy_set_profile_pvid(netelem_name, profile_id, pvid, **kwargs)
        self.networkElementPolicyGenKeywords.policy_set_profile_untagged_vlan(netelem_name, profile_id, pvid, False, **kwargs)
        self.networkElementPolicyGenKeywords.policy_set_profile_pvid_status(netelem_name, profile_id, 'enable', **kwargs)
        self.networkElementPolicyGenKeywords.policy_verify_profile_exists(netelem_name, profile_id, **kwargs)
