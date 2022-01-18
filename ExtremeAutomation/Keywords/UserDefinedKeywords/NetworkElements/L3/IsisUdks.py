from ExtremeAutomation.Keywords.NetworkElementKeywords.GeneratedKeywords.NetworkElementIsisGenKeywords import NetworkElementIsisGenKeywords


class IsisUdks():
    def __init__(self) -> None:
        self.networkElementIsisGenKeywords = NetworkElementIsisGenKeywords()

    def Configure_Isis_System_Id_and_Verify_it_is_Set(self, netelem_name, system_id, **kwargs):
        """  Configures_the_IS-IS_System_ID_and_verifies_it_is_configured """
        self.networkElementIsisGenKeywords.isis_set_system_id(netelem_name, system_id, **kwargs)
        self.networkElementIsisGenKeywords.isis_verify_system_id(netelem_name, system_id, **kwargs)

    def Create_Isis_Manual_Area_and_Verify_it_Exists(self, netelem_name, manual_area, **kwargs):
        """  Creates_an_IS-IS_manual_Area_and_verifies_it_is_created """
        self.networkElementIsisGenKeywords.isis_set_manual_area(netelem_name, manual_area, **kwargs)
        self.networkElementIsisGenKeywords.isis_verify_manual_area_exists(netelem_name, manual_area, **kwargs)

    def Enable_Isis_Globally_and_Verify_it_is_Enabled(self, netelem_name, **kwargs):
        """  Enables_IS-IS_globally_and_verifies_it_is_enabled """
        self.networkElementIsisGenKeywords.isis_enable_global(netelem_name, **kwargs)
        self.networkElementIsisGenKeywords.isis_verify_enabled_globally(netelem_name, **kwargs)

    def Create_Isis_Circuit_on_Port_and_Verify_it_Exists(self, netelem_name, port, **kwargs):
        """  Creates_and_IS-IS_circuit_on_a_port_and_verifies_it_exists """
        self.networkElementIsisGenKeywords.isis_set_circuit_on_port(netelem_name, port, **kwargs)
        self.networkElementIsisGenKeywords.isis_verify_circuit_on_port_exists(netelem_name, port, **kwargs)

    def Create_Isis_Circuit_on_Mlt_and_Verify_it_Exists(self, netelem_name, mlt_id, **kwargs):
        """  Creates_and_IS-IS_circuit_on_an_MLT_and_verifies_it_exists """
        self.networkElementIsisGenKeywords.isis_set_circuit_on_mlt(netelem_name, mlt_id, **kwargs)
        self.networkElementIsisGenKeywords.isis_verify_circuit_on_mlt_exists(netelem_name, mlt_id, **kwargs)

    def Enable_Isis_Circuit_on_Port_and_Verify_it_is_Enabled(self, netelem_name, port, **kwargs):
        """  Enables_an_IS-IS_circuit_on_a_port_and_verifies_it_is_enabled """
        self.networkElementIsisGenKeywords.isis_enable_circuit_on_port(netelem_name, port, **kwargs)
        self.networkElementIsisGenKeywords.isis_verify_circuit_on_port_enabled(netelem_name, port, **kwargs)

    def Enable_Isis_Circuit_on_Mlt_and_Verify_it_is_Enabled(self, netelem_name, mlt_id, **kwargs):
        """  Enables_an_IS-IS_circuit_on_an_MLT_and_verifies_it_is_enabled  """
        self.networkElementIsisGenKeywords.isis_enable_circuit_on_mlt(netelem_name, mlt_id, **kwargs)
        self.networkElementIsisGenKeywords.isis_verify_circuit_on_mlt_enabled(netelem_name, mlt_id, **kwargs)

    def Disable_Isis_Globally_and_Verify_it_is_Disabled(self, netelem_name, **kwargs):
        """  Disables_IS-IS_globally_and_verifies_it_is_disabled """
        self.networkElementIsisGenKeywords.isis_disable_global(netelem_name, **kwargs)
        self.networkElementIsisGenKeywords.isis_verify_disabled_globally(netelem_name, **kwargs)

    def Remove_Isis_System_Id_and_Verify_it_is_Removed(self, netelem_name, system_id, **kwargs):
        """  Removes_the_IS-IS_System_ID_and_verifies_it_is_no_longer_set_to_the_previous_value """
        self.networkElementIsisGenKeywords.isis_clear_system_id(netelem_name, system_id, **kwargs)
        self.networkElementIsisGenKeywords.isis_verify_system_id_is_not(netelem_name, system_id, **kwargs)

    def Remove_Isis_Manual_Area_and_Verify_it_is_Removed(self, netelem_name, manual_area, **kwargs):
        """  Deletes_an_IS-IS_manual_Area_and_verifies_it_is_deleted """
        self.networkElementIsisGenKeywords.isis_clear_manual_area(netelem_name, manual_area, **kwargs)
        self.networkElementIsisGenKeywords.isis_verify_manual_area_does_not_exist(netelem_name, manual_area, **kwargs)

    def Disable_Isis_Circuit_on_Port_and_Verify_it_is_Disabled(self, netelem_name, port, **kwargs):
        """  Disables_an_IS-IS_circuit_on_a_port_and_verifies_it_is_disabled """
        self.networkElementIsisGenKeywords.isis_disable_circuit_on_port(netelem_name, port, **kwargs)
        self.networkElementIsisGenKeywords.isis_verify_circuit_on_port_disabled(netelem_name, port, **kwargs)

    def Remove_Isis_Circuit_on_Port_and_Verify_it_is_Removed(self, netelem_name, port, **kwargs):
        """  Removes_an_IS-IS_circuit_on_a_port_and_verifies_it_is_removed """
        self.networkElementIsisGenKeywords.isis_clear_circuit_on_port(netelem_name, port, **kwargs)
        self.networkElementIsisGenKeywords.isis_verify_circuit_on_port_does_not_exist(netelem_name, port, **kwargs)

    def Disable_Isis_Circuit_on_Mlt_and_Verify_it_is_Disabled(self, netelem_name, mlt_id, **kwargs):
        """  Disables_an_IS-IS_circuit_on_an_MLT_and_verifies_it_is_disabled """
        self.networkElementIsisGenKeywords.isis_disable_circuit_on_mlt(netelem_name, mlt_id, **kwargs)
        self.networkElementIsisGenKeywords.isis_verify_circuit_on_mlt_disabled(netelem_name, mlt_id, **kwargs)

    def Remove_Isis_Circuit_on_Mlt_and_Verify_it_is_Removed(self, netelem_name, mlt_id, **kwargs):
        """  Removes_an_IS-IS_circuit_on_an_MLT_and_verifies_it_is_removed """
        self.networkElementIsisGenKeywords.isis_clear_circuit_on_mlt(netelem_name, mlt_id, **kwargs)
        self.networkElementIsisGenKeywords.isis_verify_circuit_on_mlt_does_not_exist(netelem_name, mlt_id, **kwargs)

    def Configure_Isis_L1_Hello_Interval_On_Port_and_Verify_it_is_Configured(self, netelem_name, port,  interval, **kwargs):
        """  Configures_the_IS-IS_L1_hello_interval_on_a_port_and_verifies_it_is_configured_accordingly. """
        self.networkElementIsisGenKeywords.isis_set_l1_hello_interval_on_port(netelem_name, port,  interval, **kwargs)
        self.networkElementIsisGenKeywords.isis_verify_l1_hello_interval_port(netelem_name, port,  interval, **kwargs)

    def Configure_Isis_L1_Hello_Interval_On_Mlt_and_Verify_it_is_Configured(self, netelem_name, mlt_id,  interval, **kwargs):
        """  Configures_the_IS-IS_L1_hello_interval_on_an_MLT_and_verifies_it_is_configured_accordingly. """
        self.networkElementIsisGenKeywords.isis_set_l1_hello_interval_on_mlt(netelem_name, mlt_id,  interval, **kwargs)
        self.networkElementIsisGenKeywords.isis_verify_l1_hello_interval_mlt(netelem_name, mlt_id,  interval, **kwargs)

    def Configure_Isis_L1_Hello_Multiplier_On_Port_and_Verify_it_is_Configured(self, netelem_name, port,  multiplier, **kwargs):
        """  Configures_the_IS-IS_L1_hello_multiplier_on_a_port_and_verifies_it_is_configured_accordingly. """
        self.networkElementIsisGenKeywords.isis_set_l1_hello_multiplier_on_port(netelem_name, port,  multiplier, **kwargs)
        self.networkElementIsisGenKeywords.isis_verify_l1_hello_multiplier_port(netelem_name, port,  multiplier, **kwargs)

    def Configure_Isis_L1_Hello_Multiplier_On_Mlt_and_Verify_it_is_Configured(self, netelem_name, mlt_id,  multiplier, **kwargs):
        """  Configures_the_IS-IS_L1_hello_multiplier_on_an_MLT_and_verifies_it_is_configured_accordingly. """
        self.networkElementIsisGenKeywords.isis_set_l1_hello_multiplier_on_mlt(netelem_name, mlt_id,  multiplier, **kwargs)
        self.networkElementIsisGenKeywords.isis_verify_l1_hello_multiplier_mlt(netelem_name, mlt_id,  multiplier, **kwargs)

    def Configure_Enable_and_Apply_Isis_Redistribute_Direct_and_Verify(self, netelem_name, **kwargs):
        """  Configures, Enables_and_Applies_IS-IS_Redistribute_Direct_on_the_device """
        self.networkElementIsisGenKeywords.isis_set_redistribute_direct(netelem_name, **kwargs)
        self.networkElementIsisGenKeywords.isis_verify_redistribute_direct(netelem_name, **kwargs)
        self.networkElementIsisGenKeywords.isis_enable_redistribute_direct(netelem_name, **kwargs)
        self.networkElementIsisGenKeywords.isis_verify_redistribute_direct_enabled(netelem_name, **kwargs)
        self.networkElementIsisGenKeywords.isis_set_redistribute_direct_apply(netelem_name, **kwargs)

    def Unconfigure_Isis_Redistribute_Direct_and_Verify(self, netelem_name, **kwargs):
        """  Unconfigures_and_Disables_IS-IS_Redistribute_Direct_on_the_device """
        self.networkElementIsisGenKeywords.isis_clear_redistribute_direct(netelem_name, **kwargs)
        self.networkElementIsisGenKeywords.isis_verify_redistribute_direct_not_set(netelem_name, **kwargs)

    def Enable_Isis_IPv6_Redistribute_Direct_and_Verify(self, netelem_name, **kwargs):
        """  Enables_IS-IS_IPv6_Redistribute_Direct_on_the_device_and_verifies_that_it_is_Enabled """
        self.networkElementIsisGenKeywords.isis_clear_redistribute_direct(netelem_name, **kwargs)
        self.networkElementIsisGenKeywords.isis_verify_redistribute_direct_ipv6_enabled(netelem_name, **kwargs)

    def Disable_Isis_IPv6_Redistribute_Direct_and_Verify(self, netelem_name, **kwargs):
        """  Disables_IS-IS_IPv6_Redistribute_Direct_on_the_device_and_verifies_that_it_is_Disabled """
        self.networkElementIsisGenKeywords.isis_disable_redistribute_direct_ipv6(netelem_name, **kwargs)
        self.networkElementIsisGenKeywords.isis_verify_redistribute_direct_ipv6_disabled(netelem_name, **kwargs)