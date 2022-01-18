from ExtremeAutomation.Keywords.NetworkElementKeywords.GeneratedKeywords.NetworkElementFabricattachGenKeywords import NetworkElementFabricattachGenKeywords


class FabricAttachUdks():
    def __init__(self) -> None:
        self.networkElementFabricattachGenKeywords = NetworkElementFabricattachGenKeywords()

    def Enable_Fabric_Attach_Service_and_Verify_it_is_Enabled(self, device_names, ports, **kwargs):
        """ Enables Fabric Attach service and verifies it is enabled """
        self.networkElementFabricattachGenKeywords.fabricattach_enable_global(device_names, **kwargs)
        self.networkElementFabricattachGenKeywords.fabricattach_verify_enabled(device_names, **kwargs)

    def Disable_Fabric_Attach_Service_and_Verify_it_is_Disabled(self, device_names, ports, **kwargs):
        """ Disables Fabric Attach service and verifies it is disabled """
        self.networkElementFabricattachGenKeywords.fabricattach_disable_global(device_names, **kwargs)
        self.networkElementFabricattachGenKeywords.fabricattach_verify_disabled(device_names, **kwargs)

    def Enable_Fabric_Attach_on_Port_and_Verify_it_is_Enabled(self, device_names, ports, **kwargs):
        """ Enables Fabric Attach on a port and verifies it is enabled """
        self.networkElementFabricattachGenKeywords.fabricattach_enable_port(device_names, ports, **kwargs)
        self.networkElementFabricattachGenKeywords.fabricattach_verify_enabled_on_port(device_names, ports, **kwargs)

    def Disable_Fabric_Attach_on_Port_and_Verify_it_is_Disabled(self, device_names, ports, **kwargs):
        """ Disables Fabric Attach on a port and verifies it is disabled """
        self.networkElementFabricattachGenKeywords.fabricattach_disable_port(device_names, ports, **kwargs)
        self.networkElementFabricattachGenKeywords.fabricattach_verify_disabled_on_port(device_names, ports, **kwargs)

    def Remove_Fabric_Attach_on_Port_and_Verify_it_is_Removed(self, device_names, ports, **kwargs):
        """ Removes port from the Fabric Attach instance table and verifies it is removed """
        self.networkElementFabricattachGenKeywords.fabricattach_delete_port(device_names, ports, **kwargs)
        self.networkElementFabricattachGenKeywords.fabricattach_verify_removed_on_port(device_names, ports, **kwargs)

    def Remove_Fabric_Attach_on_Mlt_and_Verify_it_is_Removed(self, device_names, mlt_id, **kwargs):
        """ Removes mlt trunk from the Fabric Attach instance table and verifies it is removed """
        self.networkElementFabricattachGenKeywords.fabricattach_delete_mlt(device_names, mlt_id, **kwargs)
        self.networkElementFabricattachGenKeywords.fabricattach_verify_removed_on_mlt(device_names, mlt_id, **kwargs)

    def Enable_Fabric_Attach_Authentication_on_Port_and_Verify_it_is_Enabled(self, device_names, ports, **kwargs):
        """ Enables Fabric Attach Authentication on a port and verifies it is enabled """
        self.networkElementFabricattachGenKeywords.fabricattach_enable_port_auth(device_names, ports, **kwargs)
        self.networkElementFabricattachGenKeywords.fabricattach_verify_auth_enabled_on_port(device_names, ports, **kwargs)

    def Disable_Fabric_Attach_Authentication_on_Port_and_Verify_it_is_Disabled(self, device_names, ports, **kwargs):
        """ Disables Fabric Attach Authentication on a port and verifies it is disabled """
        self.networkElementFabricattachGenKeywords.fabricattach_disable_port_auth(device_names, ports, **kwargs)
        self.networkElementFabricattachGenKeywords.fabricattach_verify_auth_disabled_on_port(device_names, ports, **kwargs)

    def Enable_Fabric_Attach_Authentication_on_Mlt_and_Verify_it_is_Enabled(self, device_names, mlt_id, **kwargs):
        """ Enables Fabric Attach Authentication on a Mlt trunk and verifies it is enabled """
        self.networkElementFabricattachGenKeywords.fabricattach_enable_mlt_auth(device_names, mlt_id, **kwargs)
        self.networkElementFabricattachGenKeywords.fabricattach_verify_auth_enabled_on_mlt(device_names, mlt_id, **kwargs)

    def Disable_Fabric_Attach_Authentication_on_Mlt_and_Verify_it_is_Disabled(self, device_names, mlt_id, **kwargs):
        """ Disables Fabric Attach Authentication on a Mlt trunk and verifies it is disabled """
        self.networkElementFabricattachGenKeywords.fabricattach_disable_mlt_auth(device_names, mlt_id, **kwargs)
        self.networkElementFabricattachGenKeywords.fabricattach_verify_auth_disabled_on_mlt(device_names, mlt_id, **kwargs)

    def Create_Fabric_Attach_Zero_Touch_Client_To_Isid_Auto_Attach_Map_and_Verify_Client_and_Isid(self,  device_names, name, isid, **kwargs):
        """ Creates a Fabric Attach zero touch client name to an ISID and verifies the client name and ISID """
        self.networkElementFabricattachGenKeywords.fabricattach_set_zero_touch_client_isid(device_names, name, isid, **kwargs)
        self.networkElementFabricattachGenKeywords.fabricattach_verify_zero_touch_client_name_exists(device_names, name, **kwargs)
        self.networkElementFabricattachGenKeywords.fabricattach_verify_zero_touch_client_to_isid_auto_attach_map(device_names, name, isid, **kwargs)

    def Remove_Fabric_Attach_Zero_Touch_Client_To_Isid_Auto_Attach_Map_and_Verify_it_is_Removed(self, device_names, name, **kwargs):
        """ Creates a Fabric Attach zero touch client name to an ISID and verifies the client name and ISID """
        self.networkElementFabricattachGenKeywords.fabricattach_clear_zero_touch_client(device_names, name, **kwargs)
        self.networkElementFabricattachGenKeywords.fabricattach_verify_zero_touch_client_name_does_not_exist(device_names, name, **kwargs)
