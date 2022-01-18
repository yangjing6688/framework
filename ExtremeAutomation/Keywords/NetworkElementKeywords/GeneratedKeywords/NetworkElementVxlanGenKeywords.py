"""
Keyword class for all vxlan cli commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.VxlanConstants import \
    VxlanConstants as ParseConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.VxlanConstants import \
    VxlanConstants as CommandConstants
# All imports above this line will be removed after generation.
# User imports must be added below.


class NetworkElementVxlanGenKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementVxlanGenKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "vxlan"

    def vxlan_create_logical_switch(self, device_name, name='', **kwargs):
        """
        Description: Creates a logical-switch with the given name.

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "name": name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_LOGICAL_SWITCH,
                                    **kwargs)

    def vxlan_delete_logical_switch(self, device_name, name='', **kwargs):
        """
        Description: Removes a logical-switch with the given name.

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "name": name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DELETE_LOGICAL_SWITCH,
                                    **kwargs)

    def vxlan_create_logical_switch_to_vni_map(self, device_name, name='', vni='', **kwargs):
        """
        Description: Maps a logical-switch to the given VNI.

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "name": name,
            "vni": vni
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_LOGICAL_SWITCH_TO_VNI_MAP,
                                    **kwargs)

    def vxlan_create_logical_switch_to_vlan_map(self, device_name, name='', vlan='', **kwargs):
        """
        Description: Maps a logical-switch to the given VLAN.

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "name": name,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_LOGICAL_SWITCH_TO_VLAN_MAP,
                                    **kwargs)

    def vxlan_create_logical_switch_vni_vlan_map(self, device_name, name='', vlan='', vni='', **kwargs):
        """
        Description: Maps a logical-switch to the given VNI and VLAN.

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "name": name,
            "vlan": vlan,
            "vni": vni
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_LOGICAL_SWITCH_VNI_VLAN_MAP,
                                    **kwargs)

    def vxlan_set_remote_vtep(self, device_name, name='', ip_address='', **kwargs):
        """
        Description: Sets a remote endpoint for the logical-switch.

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "ip_address": ip_address,
            "name": name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_REMOTE_VTEP,
                                    **kwargs)

    def vxlan_clear_remote_vtep(self, device_name, name='', **kwargs):
        """
        Description: Clears the configured remote endpoint for the logical-switch.

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "name": name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_REMOTE_VTEP,
                                    **kwargs)

    # ##################################################################################################################
    #   Inspection Keywords   ##########################################################################################
    # ##################################################################################################################

    def vxlan_verify_logical_switch_exists(self, device_name, name='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [name] - The name to assign the new logical-switch.

        Verifies the logical-switch exists.
        """
        args = {"name": name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_LOGICAL_SWITCH,
                                           self.parse_const.CHECK_LOGICAL_SWITCH_EXISTS, True,
                                           "Logical-switch {name} exists on {device_name}.",
                                           "Logical-switch {name} DOES NOT exist on {device_name}.",
                                           **kwargs)

    def vxlan_verify_logical_switch_does_not_exist(self, device_name, name='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [name] - The name to assign the new logical-switch.

        Verifies the logical-switch exists.
        """
        args = {"name": name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_LOGICAL_SWITCH,
                                           self.parse_const.CHECK_LOGICAL_SWITCH_EXISTS, False,
                                           "Logical-switch {name} does not exists on {device_name}.",
                                           "Logical-switch {name} EXISTS on {device_name}.",
                                           **kwargs)
