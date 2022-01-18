from ExtremeAutomation.Keywords.NetworkElementKeywords.GeneratedKeywords.NetworkElementRadiusGenKeywords import NetworkElementRadiusGenKeywords


class RadiusUdks():
    def __init__(self) -> None:
        self.networkElementRadiusGenKeywords = NetworkElementRadiusGenKeywords()

    #########################################################################
    ##############  RADIUS_AUTHENTICATION_SERVER_KEYWORDS  ##################
    #########################################################################
    def Add_a_Radius_Server_and_Globally_Enable_Radius(self, device_name, index, addr, port, secret,  client_ip,  vr, **kwargs):
        self.Add_a_Radius_Server_and_Verify_it_was_Added(device_name, index, addr, port, secret, client_ip, vr, **kwargs)
        self.Globally_Enable_Radius_and_Verify_it_is_Enabled(device_name, **kwargs)

    def Add_a_Radius_Server_and_Verify_it_was_Added(self, device_name, index, addr, port, secret,  client_ip,  vr, **kwargs):
        """  Adds_a_RADIUS_server_and_verifies_it_was_added. """
        self.networkElementRadiusGenKeywords.radius_set_server(device_name, addr, secret, index, port, client_ip, vr, **kwargs)
        self.networkElementRadiusGenKeywords.radius_verify_server_exists(device_name, index, addr, **kwargs)

    def Add_a_Radius_Server_and_Verify_Status_is_Active(self, device_name, index, addr, port, secret,  client_ip,  vr, **kwargs):
        """  Adds_a_Radius_Server_and_Verifies_the_Status_is_set_to_Active """
        self.Add_a_Radius_Server_and_Verify_it_was_Added(device_name, index, addr, port, secret, client_ip, vr, **kwargs)
        self.networkElementRadiusGenKeywords.radius_verify_server_active(device_name, index, addr, **kwargs)

    def Remove_Radius_Server_and_Verify_it_is_Removed(self, device_name, index, addr, **kwargs):
        self.networkElementRadiusGenKeywords.radius_clear_server(device_name, index=index, **kwargs)
        self.networkElementRadiusGenKeywords.radius_verify_server_does_not_exist(device_name, index, addr, **kwargs)

    def Disable_Radius_for_Management_Users_and_Verify(self, device_name, **kwargs):
        self.networkElementRadiusGenKeywords.radius_disable_mgmt(device_name, **kwargs)
        self.networkElementRadiusGenKeywords.radius_verify_disabled_for_management(device_name, **kwargs)

    def Enable_Radius_for_Management_Users_and_Verify(self, device_name, **kwargs):
        self.networkElementRadiusGenKeywords.radius_enable_mgmt(device_name, **kwargs)
        self.networkElementRadiusGenKeywords.radius_verify_enabled_for_management(device_name, **kwargs)

    def Enable_Radius_for_Netlogin_Users_and_Verify(self, device_name, **kwargs):
        self.networkElementRadiusGenKeywords.radius_enable_netlogin(device_name, **kwargs)
        self.networkElementRadiusGenKeywords.radius_verify_enabled_for_multiauth(device_name, **kwargs)

    def Cleanup_Radius_Server_Configuration(self, device_name, index, addr, **kwargs):
        self.Remove_Radius_Server_and_Verify_it_is_Removed(device_name, index, addr, **kwargs)
        self.Globally_Disable_Radius_and_Verify_it_is_Disabled(device_name, **kwargs)

    #########################################################################
    ###################  RADIUS_ACCOUNTING_KEYWORDS  ########################
    #########################################################################

    def Add_a_Radius_Accounting_Server_and_Globally_Enable_Accounting(self, device_name,  index, addr, port,    secret,  client_ip,  vr, **kwargs):
        self.Add_a_Radius_Accounting_Server_and_Verify_it_was_Added(device_name,  index, addr, port, secret, client_ip, vr, **kwargs)
        self.Globally_Enable_Radius_Accounting_and_Verify_it_is_Enabled(device_name, **kwargs)

    def Add_a_Radius_Accounting_Server_and_Verify_it_was_Added(self, device_name,  index, addr, port,    secret,  client_ip,  vr, **kwargs):
        """  Note_that_proprietary_arguments_of_client_ip_and_vr_are_passed_in_on_lower_level_keywords. """
        self.networkElementRadiusGenKeywords.radius_set_acct_server(device_name, index, addr, port, secret, client_ip, vr, **kwargs)
        self.networkElementRadiusGenKeywords.radius_verify_accounting_server_exists(device_name, index, addr, **kwargs)

    def Globally_Enable_Radius_Accounting_and_Verify_it_is_Enabled(self, device_name, **kwargs):
        """  This_testcase_Globally_Enables_RADIUS_on_the_Network_Element_and_verifies_it_is_Enabled. """
        self.networkElementRadiusGenKeywords.radius_enable_acct(device_name, **kwargs)
        self.networkElementRadiusGenKeywords.radius_verify_accounting_state_enabled(device_name, **kwargs)

    def Globally_Disable_Radius_Accounting_and_Verify_it_is_Disabled(self, device_name, **kwargs):
        """  Disable_RADIUS_Accounting_and_Verifies. """
        self.networkElementRadiusGenKeywords.radius_disable_acct(device_name, **kwargs)
        self.networkElementRadiusGenKeywords.radius_verify_accounting_state_disabled(device_name, **kwargs)

    def Remove_Radius_Accounting_Server_and_Verify_it_is_Removed(self, device_name, index, addr, **kwargs):
        self.networkElementRadiusGenKeywords.radius_clear_acct_server(device_name, index, **kwargs)
        self.networkElementRadiusGenKeywords.radius_verify_accounting_server_does_not_exist(device_name, index, addr, **kwargs)

    def Cleanup_Radius_Accounting_Server_Configuration(self, device_name, index, addr, **kwargs):
        self.Remove_Radius_Accounting_Server_and_Verify_it_is_Removed(device_name, index, addr, **kwargs)
        self.Globally_Disable_Radius_Accounting_and_Verify_it_is_Disabled(device_name, **kwargs)

    #########################################################################
    ############  GLOBAL_RADIUS_AUTHENTICATION_SETTING_KEYWORDS  ############
    #########################################################################
    def Globally_Enable_Radius_and_Verify_it_is_Enabled(self, device_name, **kwargs):
        """  Globally_Enables_RADIUS_and_Verifies_it_is_Enabled """
        self.networkElementRadiusGenKeywords.radius_enable_global(device_name, **kwargs)
        self.networkElementRadiusGenKeywords.radius_verify_state_enabled(device_name, **kwargs)

    def Globally_Disable_Radius_and_Verify_it_is_Disabled(self, device_name, **kwargs):
        """  Globally_Disables_RADIUS_and_Verifies_it_is_Disabled """
        self.networkElementRadiusGenKeywords.radius_disable_global(device_name, **kwargs)
        self.networkElementRadiusGenKeywords.radius_verify_state_disabled(device_name, **kwargs)

    def Set_Radius_Algorithm_Type_Standard_and_Verify_Setting(self, device_name, **kwargs):
        """  Sets_the_RADIUS_Algorithm_type_to_Standard """
        self.networkElementRadiusGenKeywords.radius_set_algorithm_global_std(device_name, **kwargs)
        self.networkElementRadiusGenKeywords.radius_verify_algorithm_type_standard(device_name, **kwargs)

    def Set_Radius_Algorithm_Type_Round_Robin_and_Verify_Setting(self, device_name, **kwargs):
        """  Sets_the_RADIUS_Algorithm_type_to_Round-Robin """
        self.networkElementRadiusGenKeywords.radius_set_algorithm_global_rr(device_name, **kwargs)
        self.networkElementRadiusGenKeywords.radius_verify_algorithm_type_round_robin(device_name, **kwargs)

    def Set_Radius_Algorithm_Type_Sticky_Round_Robin_and_Verify_Setting(self, device_name, **kwargs):
        """  Sets_the_RADIUS_Algorithm_type_to_Sticky-Round-Robin """
        self.networkElementRadiusGenKeywords.radius_set_algorithm_global_srr(device_name, **kwargs)
        self.networkElementRadiusGenKeywords.radius_verify_algorithm_type_sticky_round_robin(device_name, **kwargs)

    def Set_Radius_Timeout_and_Verify_Value(self, device_name, sec, **kwargs):
        """  Sets_the_RADIUS_Server_timeout_and_verifies_the_value """
        self.networkElementRadiusGenKeywords.radius_set_timeout_global(device_name, sec, **kwargs)
        self.networkElementRadiusGenKeywords.radius_verify_timeout(device_name, sec, **kwargs)

    def Set_Radius_Retries_and_Verify_Value(self, device_name, num, **kwargs):
        """  Sets_the_RADIUS_Server_retries_value_and_verifies_setting """
        self.networkElementRadiusGenKeywords.radius_set_retries_global(device_name, num, **kwargs)
        self.networkElementRadiusGenKeywords.radius_verify_retries(device_name, num, **kwargs)

    ############################################
    ############  CLEANUP_KEYWORDS  ############
    ############################################

    def Restore_Radius_Algorithm_to_Default_Setting_and_Verify(self, device_name, **kwargs):
        self.networkElementRadiusGenKeywords.radius_clear_algorithm_global(device_name, **kwargs)
        self.networkElementRadiusGenKeywords.radius_verify_algorithm_type_standard(device_name, **kwargs)

    def Restore_Radius_Timeout_to_Default_Setting_and_Verify(self, device_name, **kwargs):
        self.networkElementRadiusGenKeywords.radius_clear_timeout_global(device_name, **kwargs)
        self.networkElementRadiusGenKeywords.radius_verify_timeout_set_to_default(device_name, **kwargs)

    def Restore_Radius_Retries_to_Default_Setting_and_Verify(self, device_name, **kwargs):
        self.networkElementRadiusGenKeywords.radius_clear_retries_global(device_name, **kwargs)
        self.networkElementRadiusGenKeywords.radius_verify_retries_set_to_default(device_name, **kwargs)
        
