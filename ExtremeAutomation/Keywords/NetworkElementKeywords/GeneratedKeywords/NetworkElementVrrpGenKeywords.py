"""
Keyword class for all vrrp cli commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.VrrpConstants import \
    VrrpConstants as ParseConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.VrrpConstants import \
    VrrpConstants as CommandConstants
# All imports above this line will be removed after generation.
# User imports must be added below.


class NetworkElementVrrpGenKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementVrrpGenKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "vrrp"

    def vrrp_enable_global(self, device_name, **kwargs):
        """
        Description: Globally Enables VRRP on the device.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_GLOBAL,
                                    **kwargs)

    def vrrp_disable_global(self, device_name, **kwargs):
        """
        Description: Globally Disables VRRP on the device.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_GLOBAL,
                                    **kwargs)

    def vrrp_enable_vlan(self, device_name, vlan='', vrid='', **kwargs):
        """
        Description: Enables a VRRP vlan and virtual router id.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "vlan": vlan,
            "vrid": vrid
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_VLAN,
                                    **kwargs)

    def vrrp_disable_vlan(self, device_name, vlan='', vrid='', **kwargs):
        """
        Description: Disables a VRRP vlan and virtual router id.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "vlan": vlan,
            "vrid": vrid
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_VLAN,
                                    **kwargs)

    def vrrp_enable_vlan_fabric_routing(self, device_name, vlan='', vrid='', **kwargs):
        """
        Description: Enables fabric routing for the specified VRRP vlan and vrid.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "vlan": vlan,
            "vrid": vrid
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_VLAN_FABRIC_ROUTING,
                                    **kwargs)

    def vrrp_disable_vlan_fabric_routing(self, device_name, vlan='', vrid='', **kwargs):
        """
        Description: Disables fabric routing for the specified VRRP vlan and vrid.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "vlan": vlan,
            "vrid": vrid
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_VLAN_FABRIC_ROUTING,
                                    **kwargs)

    def vrrp_create_vlan(self, device_name, vlan='', vrid='', **kwargs):
        """
        Description: Creates a VRRP vlan and assigns a virtual router id to the vlan.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "vlan": vlan,
            "vrid": vrid
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_VLAN,
                                    **kwargs)

    def vrrp_clear_vlan(self, device_name, vlan='', vrid='', **kwargs):
        """
        Description: Deletes a VRRP vlan and virtual router id.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "vlan": vlan,
            "vrid": vrid
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_VLAN,
                                    **kwargs)

    def vrrp_create_group(self, device_name, name='', **kwargs):
        """
        Description: Creates a VRRP group.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "name": name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_GROUP,
                                    **kwargs)

    def vrrp_clear_group(self, device_name, name='', **kwargs):
        """
        Description: Deletes a VRRP group.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "name": name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_GROUP,
                                    **kwargs)

    def vrrp_set_vlan_priority(self, device_name, vlan='', vrid='', priority='', **kwargs):
        """
        Description: Sets the VRRP priority for a given VRRP vlan and vrid.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "priority": priority,
            "vlan": vlan,
            "vrid": vrid
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_VLAN_PRIORITY,
                                    **kwargs)

    def vrrp_set_vlan_ipaddress(self, device_name, vlan='', vrid='', ip='', **kwargs):
        """
        Description: Configures a virtual IP Address for the specified VRRP vlan and vrid.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "ip": ip,
            "vlan": vlan,
            "vrid": vrid
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_VLAN_IPADDRESS,
                                    **kwargs)

    # ##################################################################################################################
    #   Inspection Keywords   ##########################################################################################
    # ##################################################################################################################

    def vrrp_verify_globally_enabled(self, device_name, vlan='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vlan]        - The VRRP vlan to verify.

        Verifies VRRP is globally Enabled for a specified VLAN.
        """
        args = {"vlan": vlan}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VLAN,
                                           self.parse_const.CHECK_VRRP_GLOBALLY_ENABLED, True,
                                           "VRRP is globally enabled for vlan {vlan} on {device_name}.",
                                           "VRRP is Not globally enabled for vlan {vlan} on {device_name}!",
                                           **kwargs)

    def vrrp_verify_globally_disabled(self, device_name, vlan='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vlan]        - The VRRP vlan to verify.

        Verifies VRRP is globally Disabled for a specified VLAN.
        """
        args = {"vlan": vlan}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VLAN,
                                           self.parse_const.CHECK_VRRP_GLOBALLY_DISABLED, True,
                                           "VRRP is globally Disabled for vlan {vlan} on {device_name}.",
                                           "VRRP is Not globally disabled for vlan {vlan} on {device_name}!",
                                           **kwargs)

    def vrrp_verify_vlan_and_vrid_exist(self, device_name, vlan='', vrid='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vlan]        - The VRRP vlan to verify.
        [vrid}        - The VRRP virtual router id to verify.

        Verifies the VRRP vlan with vrid exist on the device.
        """
        args = {"vlan": vlan,
                "vrid": vrid}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VLAN,
                                           self.parse_const.CHECK_VRRP_VLAN_EXISTS, True,
                                           "VRRP vlan {vlan} with vrid {vrid} is present on {device_name}.",
                                           "VRRP vlan {vlan} with vrid {vrid} is NOT present on {device_name}!",
                                           **kwargs)

    def vrrp_verify_vlan_and_vrid_does_not_exist(self, device_name, vlan='', vrid='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vlan]        - The VRRP vlan to verify.
        [vrid}        - The VRRP virtual router id to verify.

        Verifies the VRRP vlan with vrid does not exist on the device.
        """
        args = {"vlan": vlan,
                "vrid": vrid}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL,
                                           self.parse_const.CHECK_VRRP_VLAN_EXISTS, False,
                                           "VRRP vlan {vlan} with vrid {vrid} is not present on {device_name}.",
                                           "VRRP vlan {vlan} with vrid {vrid} IS present on {device_name}!",
                                           **kwargs)

    def vrrp_verify_vlan_priority_is_set(self, device_name, vlan='', vrid='', priority='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vlan]        - The VRRP vlan.
        [vrid}        - The VRRP virtual router id.
        [priority]    - The VRRP Priority to verify

        Verifies the VRRP vlan priority is set for the specified VRRP vlan and vrid.
        """
        args = {"vlan": vlan,
                "vrid": vrid,
                "priority": priority}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VLAN,
                                           self.parse_const.CHECK_VRRP_VLAN_PRIORITY_IS_SET, True,
                                           "VRRP vlan priority {priority} is set on VRRP vlan {vlan} vrid {vrid} on"
                                           " {device_name}.",
                                           "VRRP vlan priority {priority} is Not set on VRRP vlan {vlan} vrid {vrid} on"
                                           " {device_name}!",
                                           **kwargs)

    def vrrp_verify_vlan_virtual_ip_address_is_set(self, device_name, vlan='', vrid='', ip='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vlan]        - The VRRP vlan.
        [vrid}        - The VRRP virtual router id.
        [ip]          - The VRRP virtual IP address to verify

        Verifies the VRRP vlan virtual IP address is set for the specified VRRP vlan and vrid.
        """
        args = {"vlan": vlan,
                "vrid": vrid,
                "ip": ip}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VLAN,
                                           self.parse_const.CHECK_VRRP_VLAN_IP_ADDRESS_IS_SET, True,
                                           "The VRRP virtual IP address {ip} is set for VRRP vlan {vlan} vrid {vrid} on"
                                           " {device_name}.",
                                           "The VRRP virtual IP address {ip} is NOT set for VRRP vlan {vlan} vrid "
                                           "{vrid} on {device_name}!",
                                           **kwargs)

    def vrrp_verify_fabric_routing_is_enabled_on_vlan(self, device_name, vlan='', vrid='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vlan]        - The VRRP vlan.
        [vrid}        - The VRRP virtual router id.

        Verifies Fabric Routing is Enabled for the specified VRRP vlan and vrid.
        """
        args = {"vlan": vlan,
                "vrid": vrid}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VLAN,
                                           self.parse_const.CHECK_VRRP_VLAN_FABRIC_ROUTING_IS_SET, True,
                                           "Fabric Routing is Enabled for VRRP vlan {vlan} vrid {vrid} on "
                                           "{device_name}.",
                                           "Fabric Routing is NOT enabled for VRRP vlan {vlan} vrid {vrid} on "
                                           "{device_name}!",
                                           **kwargs)

    def vrrp_verify_fabric_routing_is_disabled_on_vlan(self, device_name, vlan='', vrid='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vlan]        - The VRRP vlan.
        [vrid}        - The VRRP virtual router id.

        Verifies Fabric Routing is Disabled for the specified VRRP vlan and vrid.
        """
        args = {"vlan": vlan,
                "vrid": vrid}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VLAN,
                                           self.parse_const.CHECK_VRRP_VLAN_FABRIC_ROUTING_IS_SET, False,
                                           "Fabric Routing is Disabled for VRRP vlan {vlan} vrid {vrid} on "
                                           "{device_name}.",
                                           "Fabric Routing IS Enabled for VRRP vlan {vlan} vrid {vrid} on "
                                           "{device_name}!",
                                           **kwargs)

    def vrrp_verify_vlan_enabled(self, device_name, vlan='', vrid='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vlan]        - The VRRP vlan to verify.
        [vrid}        - The VRRP virtual router id to verify.

        Verifies the VRRP vlan with vrid is Enabled.
        """
        args = {"vlan": vlan,
                "vrid": vrid}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VLAN,
                                           self.parse_const.CHECK_VRRP_VLAN_IS_ENABLED, True,
                                           "VRRP vlan {vlan} with vrid {vrid} is Enabled on {device_name}.",
                                           "VRRP vlan {vlan} with vrid {vrid} is NOT Enabled on {device_name}!",
                                           **kwargs)

    def vrrp_verify_vlan_disabled(self, device_name, vlan='', vrid='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vlan]        - The VRRP vlan to verify.
        [vrid}        - The VRRP virtual router id to verify.

        Verifies the VRRP vlan with vrid is Disabled.
        """
        args = {"vlan": vlan,
                "vrid": vrid}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VLAN,
                                           self.parse_const.CHECK_VRRP_VLAN_IS_ENABLED, False,
                                           "VRRP vlan {vlan} with vrid {vrid} is Disabled on {device_name}.",
                                           "VRRP vlan {vlan} with vrid {vrid} is NOT Disabled on {device_name}!",
                                           **kwargs)

    def vrrp_verify_state_master(self, device_name, vlan='', vrid='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vlan]        - The VRRP vlan to verify.
        [vrid}        - The VRRP virtual router id to verify.

        Verifies the state is set to Master for the specified VRRP vlan and vrid.
        """
        args = {"vlan": vlan,
                "vrid": vrid}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VLAN,
                                           self.parse_const.CHECK_VRRP_STATE_IS_MASTER, True,
                                           "VRRP vlan {vlan} with vrid {vrid} is set to MASTER on {device_name}.",
                                           "VRRP vlan {vlan} with vrid {vrid} is NOT set to MASTER on {device_name}!",
                                           **kwargs)

    def vrrp_verify_state_backup(self, device_name, vlan='', vrid='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vlan]        - The VRRP vlan to verify.
        [vrid}        - The VRRP virtual router id to verify.

        Verifies the state is set to Backup for the specified VRRP vlan and vrid.
        """
        args = {"vlan": vlan,
                "vrid": vrid}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VLAN,
                                           self.parse_const.CHECK_VRRP_STATE_IS_BACKUP, True,
                                           "VRRP vlan {vlan} with vrid {vrid} is set to BACKUP on {device_name}.",
                                           "VRRP vlan {vlan} with vrid {vrid} is NOT set to BACKUP on {device_name}!",
                                           **kwargs)

    def vrrp_verify_group_exists(self, device_name, name='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [name]        - The name of the VRRP group to verify.

        Verifies a VRRP group exists on the device.
        """
        args = {"name": name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_GROUP,
                                           self.parse_const.CHECK_VRRP_GROUP_EXISTS, True,
                                           "VRRP group {name} is present on {device_name}.",
                                           "VRRP group {name} is NOT present on {device_name}!",
                                           **kwargs)

    def vrrp_verify_group_does_not_exist(self, device_name, name='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [name]        - The name of the VRRP group to verify.

        Verifies a VRRP group does not exist on the device.
        """
        args = {"name": name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_GROUP,
                                           self.parse_const.CHECK_VRRP_GROUP_EXISTS, False,
                                           "VRRP group {name} is not present on {device_name}.",
                                           "VRRP group {name} IS present on {device_name}!",
                                           **kwargs)
