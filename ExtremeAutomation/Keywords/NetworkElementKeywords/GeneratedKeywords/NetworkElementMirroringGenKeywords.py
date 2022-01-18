"""
Keyword class for all mirroring cli commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.MirroringConstants import \
    MirroringConstants as ParseConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.MirroringConstants import \
    MirroringConstants as CommandConstants
# All imports above this line will be removed after generation.
# User imports must be added below.


class NetworkElementMirroringGenKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementMirroringGenKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "mirroring"

    def mirroring_create_both(self, device_name, name='', src_port='', dst_port='', **kwargs):
        """
        Description: Creates an ingress and egress port mirror.

        Supported Agents and OS:
            CLI: EOS, EXOS, VOSS, SLX
        """
        args = {
            "dst_port": dst_port,
            "name": name,
            "src_port": src_port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_BOTH,
                                    **kwargs)

    def mirroring_create_ingress(self, device_name, name='', src_port='', dst_port='', **kwargs):
        """
        Description: Creates an ingress-only defined port mirror.

        Supported Agents and OS:
            CLI: EOS, EXOS, VOSS, SLX
        """
        args = {
            "dst_port": dst_port,
            "name": name,
            "src_port": src_port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_INGRESS,
                                    **kwargs)

    def mirroring_create_egress(self, device_name, name='', src_port='', dst_port='', **kwargs):
        """
        Description: Creates an egress-only port mirror.

        Supported Agents and OS:
            CLI: EOS, EXOS, VOSS, SLX
        """
        args = {
            "dst_port": dst_port,
            "name": name,
            "src_port": src_port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_EGRESS,
                                    **kwargs)

    def mirroring_delete_port_mirror(self, device_name, name='', src_port='', dst_port='', **kwargs):
        """
        Description: Deletes the specified port mirror.

        Supported Agents and OS:
            CLI: EOS, EXOS, VOSS, SLX
        """
        args = {
            "dst_port": dst_port,
            "name": name,
            "src_port": src_port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DELETE_PORT_MIRROR,
                                    **kwargs)

    def mirroring_enable_port(self, device_name, name='', src_port='', dst_port='', **kwargs):
        """
        Description: Enables the specified port mirror.

        Supported Agents and OS:
            CLI: EOS, EXOS, VOSS
        """
        args = {
            "dst_port": dst_port,
            "name": name,
            "src_port": src_port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_PORT,
                                    **kwargs)

    def mirroring_disable_port(self, device_name, name='', src_port='', dst_port='', **kwargs):
        """
        Description: Disables the specified port mirror.

        Supported Agents and OS:
            CLI: EOS, EXOS, VOSS
        """
        args = {
            "dst_port": dst_port,
            "name": name,
            "src_port": src_port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_PORT,
                                    **kwargs)

    def mirroring_create_remote_both(self, device_name, ip='', name='', **kwargs):
        """
        Description: Creates an ingress and egress remote port mirror.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "ip": ip,
            "name": name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_REMOTE_BOTH,
                                    **kwargs)

    def mirroring_create_portlist(self, device_name, name='', port_list='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "name": name,
            "port_list": port_list
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_PORTLIST,
                                    **kwargs)

    def mirroring_set_source_port_both(self, device_name, name='', src_port='', **kwargs):
        """
        Description: Configures the specified port as the mirror source.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "name": name,
            "src_port": src_port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_SOURCE_PORT_BOTH,
                                    **kwargs)

    def mirroring_set_source_port_vlan(self, device_name, name='', src_port='', vlan='', **kwargs):
        """
        Description: Configures the specified port as the mirror source.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "name": name,
            "src_port": src_port,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_SOURCE_PORT_VLAN,
                                    **kwargs)

    def mirroring_set_source_port_ingress(self, device_name, name='', src_port='', **kwargs):
        """
        Description: Configures the specified port as the mirror source for ingress only.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "name": name,
            "src_port": src_port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_SOURCE_PORT_INGRESS,
                                    **kwargs)

    def mirroring_set_source_port_egress(self, device_name, name='', src_port='', **kwargs):
        """
        Description: Configures the specified port as the mirror source for egress only.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "name": name,
            "src_port": src_port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_SOURCE_PORT_EGRESS,
                                    **kwargs)

    def mirroring_clear_source_port(self, device_name, name='', src_port='', **kwargs):
        """
        Description: Removes the specified port as the mirror source.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "name": name,
            "src_port": src_port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_SOURCE_PORT,
                                    **kwargs)

    def mirroring_enable_remote_ping_check(self, device_name, name='', src_ip='', dst_ip='', **kwargs):
        """
        Description: Enables ping check for a remote mirror.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "dst_ip": dst_ip,
            "name": name,
            "src_ip": src_ip
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_REMOTE_PING_CHECK,
                                    **kwargs)

    def mirroring_disable_remote_ping_check(self, device_name, name='', src_ip='', dst_ip='', **kwargs):
        """
        Description: Enables ping check for a remote mirror.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "dst_ip": dst_ip,
            "name": name,
            "src_ip": src_ip
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_REMOTE_PING_CHECK,
                                    **kwargs)

    def mirroring_set_description(self, device_name, description='', name='', **kwargs):
        """
        Description: Assigns a name or description to the existing mirror.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {
            "description": description,
            "name": name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_DESCRIPTION,
                                    **kwargs)

    # ##################################################################################################################
    #   Inspection Keywords   ##########################################################################################
    # ##################################################################################################################

    def mirroring_verify_port_mirror_exists(self, device_name, name='', src_port='', dst_port='', **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device the keyword should be run against.
        [name]         - The name or id of the mirror.
        [src_port]     - The source port whose traffic will be mirrored.
        [dst_port]     - The destination port to forward the mirrored packet out.

        Verifies the specified port mirror exists.
        """
        args = {"name": name,
                "src_port": src_port,
                "dst_port": dst_port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_MIRROR_ALL,
                                           self.parse_const.CHECK_PORT_MIRROR_EXISTS, True,
                                           "Port Mirror {name} exists on {device_name}.",
                                           "Port Mirror {name} does NOT exist on {device_name}!",
                                           **kwargs)

    def mirroring_verify_port_mirror_does_not_exist(self, device_name, name='', src_port='', dst_port='',
                                                    **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [name]        - The name or id of the mirror.
        [src_port]    - The source port whose traffic will be mirrored.
        [dst_port]    - The destination port to forward the mirrored packet out.

        Verifies the specified port mirror does not exist.
        """
        args = {"name": name,
                "src_port": src_port,
                "dst_port": dst_port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_MIRROR_ALL,
                                           self.parse_const.CHECK_PORT_MIRROR_EXISTS, False,
                                           "Port Mirror {name} does not exist on {device_name}.",
                                           "Port Mirror {name} STILL exists on {device_name}!",
                                           **kwargs)

    def mirroring_verify_ingress_mirror_exists(self, device_name, name='', src_port='', dst_port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [name]         - The name or id of the mirror.
        [src_port]     - The source port whose traffic will be mirrored. (EOS Only)
        [dst_port]     - The destination port to forward the mirrored packet out.

        Verifies the specified port mirror ingress configuration exists.
        """
        args = {"name": name,
                "src_port": src_port,
                "dst_port": dst_port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_MIRROR,
                                           self.parse_const.CHECK_PORT_MIRROR_INGRESS_EXISTS, True,
                                           "Port Mirror ingress {name} exists on {device_name}.",
                                           "Port Mirror ingress {name} does NOT exist on {device_name}!",
                                           **kwargs)

    def mirroring_verify_ingress_mirror_does_not_exist(self, device_name, name='', src_port='', dst_port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [name]         - The name or id of the mirror.
        [src_port]     - The source port whose traffic will be mirrored. (EOS Only)
        [dst_port]     - The destination port to forward the mirrored packet out.

        Verifies the specified port mirror ingress configuration DOES NOT exists.
        """
        args = {"name": name,
                "src_port": src_port,
                "dst_port": dst_port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_MIRROR,
                                           self.parse_const.CHECK_PORT_MIRROR_INGRESS_EXISTS, False,
                                           "Port Mirror ingress {name} does not exist on {device_name}.",
                                           "Port Mirror ingress {name} STILL exists on {device_name}!",
                                           **kwargs)

    def mirroring_verify_egress_mirror_exists(self, device_name, name='', src_port='', dst_port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [name]         - The name or id of the mirror.
        [src_port]     - The source port whose traffic will be mirrored. (EOS Only)
        [dst_port]     - The destination port to forward the mirrored packet out.

        Verifies the specified port mirror egress configuration exists.
        """
        args = {"name": name,
                "src_port": src_port,
                "dst_port": dst_port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_MIRROR,
                                           self.parse_const.CHECK_PORT_MIRROR_EGRESS_EXISTS, True,
                                           "Port Mirror egress {name} exists on {device_name}.",
                                           "Port Mirror egress {name} does NOT exist on {device_name}!",
                                           **kwargs)

    def mirroring_verify_egress_mirror_does_not_exist(self, device_name, name='', src_port='', dst_port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [name]         - The name or id of the mirror.
        [src_port]     - The source port whose traffic will be mirrored. (EOS Only)
        [dst_port]     - The destination port to forward the mirrored packet out.

        Verifies the specified port mirror egress configuration DOES NOT exists.
        """
        args = {"name": name,
                "src_port": src_port,
                "dst_port": dst_port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_MIRROR,
                                           self.parse_const.CHECK_PORT_MIRROR_EGRESS_EXISTS, False,
                                           "Port Mirror egress {name} does not exist on {device_name}.",
                                           "Port Mirror egress {name} STILL exists on {device_name}!",
                                           **kwargs)

    def mirroring_verify_ingress_egress_mirror_exists(self, device_name, name='', src_port='', dst_port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [name]         - The name or id of the mirror.
        [src_port]     - The source port whose traffic will be mirrored. (EOS Only)
        [dst_port]     - The destination port to forward the mirrored packet out.

        Verifies the specified port mirror ingress-egress configuration exists.
        """
        args = {"name": name,
                "src_port": src_port,
                "dst_port": dst_port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_MIRROR,
                                           self.parse_const.CHECK_PORT_MIRROR_INGRESS_EGRESS_EXISTS, True,
                                           "Port Mirror ingress-egress {name} exists on {device_name}.",
                                           "Port Mirror ingress-egress {name} does NOT exist on {device_name}!",
                                           **kwargs)

    def mirroring_verify_ingress_egress_mirror_does_not_exist(self, device_name, name='', src_port='', dst_port='',
                                                              **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [name]         - The name or id of the mirror.
        [src_port]     - The source port whose traffic will be mirrored. (EOS Only)
        [dst_port]     - The destination port to forward the mirrored packet out.

        Verifies the specified port mirror ingress-egress configuration DOES NOT exists.
        """
        args = {"name": name,
                "src_port": src_port,
                "dst_port": dst_port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_MIRROR,
                                           self.parse_const.CHECK_PORT_MIRROR_INGRESS_EGRESS_EXISTS, False,
                                           "Port Mirror ingress-egress {name} does not exist on {device_name}.",
                                           "Port Mirror ingress-egress {name} STILL exists on {device_name}!",
                                           **kwargs)

    def mirroring_verify_port_mirror_enabled(self, device_name, name='', src_port='', dst_port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [name]        - The name or id of the mirror.
        [src_port]    - The source port whose traffic will be mirrored.
        [dst_port]    - The destination port to forward the mirrored packet out.

        Verifies the specified port mirror is enabled.
        """
        args = {"name": name,
                "src_port": src_port,
                "dst_port": dst_port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_MIRROR_ALL,
                                           self.parse_const.CHECK_PORT_MIRROR_ENABLED, True,
                                           "Port Mirror {name} is enabled on {device_name}.",
                                           "Port Mirror {name} is NOT enabled on {device_name}!",
                                           **kwargs)

    def mirroring_verify_port_mirror_disabled(self, device_name, name='', src_port='', dst_port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [name]        - The name or id of the mirror.
        [src_port]    - The source port whose traffic will be mirrored.
        [dst_port]    - The destination port to forward the mirrored packet out.

        Verifies the specified port mirror is disabled.
        """
        args = {"name": name,
                "src_port": src_port,
                "dst_port": dst_port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_MIRROR_ALL,
                                           self.parse_const.CHECK_PORT_MIRROR_ENABLED, False,
                                           "Port Mirror {name} is disabled on {device_name}.",
                                           "Port Mirror {name} is NOT disabled on {device_name}!",
                                           **kwargs)
