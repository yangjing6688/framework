"""
Keyword class for all tunnel cli commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.TunnelConstants import \
    TunnelConstants as ParseConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.TunnelConstants import \
    TunnelConstants as CommandConstants
# All imports above this line will be removed after generation.
# User imports must be added below.


class NetworkElementTunnelGenKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementTunnelGenKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "tunnel"

    def tunnel_create_interface(self, device_name, tunnel='', **kwargs):
        """
        Description: Creates a tunnel.

        Supported Agents and OS:
            CLI: EOS, EXOS, SLX
        """
        args = {
            "tunnel": tunnel
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_INTERFACE,
                                    **kwargs)

    def tunnel_delete_interface(self, device_name, tunnel='', **kwargs):
        """
        Description: Deletes a tunnel.

        Supported Agents and OS:
            CLI: EOS, EXOS, SLX
        """
        args = {
            "tunnel": tunnel
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DELETE_INTERFACE,
                                    **kwargs)

    def tunnel_enable_interface(self, device_name, tunnel='', **kwargs):
        """
        Description: Enables a tunnel.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "tunnel": tunnel
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_INTERFACE,
                                    **kwargs)

    def tunnel_disable_interface(self, device_name, tunnel='', **kwargs):
        """
        Description: Disables a tunnel.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "tunnel": tunnel
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_INTERFACE,
                                    **kwargs)

    def tunnel_set_mode_gre(self, device_name, tunnel='', **kwargs):
        """
        Description: Configures a tunnel with mode GRE.

        Supported Agents and OS:
            CLI: EOS, SLX
        """
        args = {
            "tunnel": tunnel
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_MODE_GRE,
                                    **kwargs)

    def tunnel_set_mode_vxlan(self, device_name, tunnel='', **kwargs):
        """
        Description: Configures a tunnel with mode VXLAN.

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "tunnel": tunnel
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_MODE_VXLAN,
                                    **kwargs)

    def tunnel_set_mode_vxlan_l2tb_port(self, device_name, tunnel='', port='', **kwargs):
        """
        Description: Binds a VxLAN tunnel to a port.

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "port": port,
            "tunnel": tunnel
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_MODE_VXLAN_L2TB_PORT,
                                    **kwargs)

    def tunnel_set_mode_gre_l2_port(self, device_name, tunnel='', port='', **kwargs):
        """
        Description: Binds a GRE tunnel to a port.

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "port": port,
            "tunnel": tunnel
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_MODE_GRE_L2_PORT,
                                    **kwargs)

    def tunnel_set_source_ip(self, device_name, tunnel='', ip_address='', **kwargs):
        """
        Description: Configures the tunnel source with the given IP.

        Supported Agents and OS:
            CLI: EOS, SLX
        """
        args = {
            "ip_address": ip_address,
            "tunnel": tunnel
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_SOURCE_IP,
                                    **kwargs)

    def tunnel_set_dest_ip(self, device_name, tunnel='', ip_address='', **kwargs):
        """
        Description: Configures the tunnel destination with the given IP.

        Supported Agents and OS:
            CLI: EOS, SLX
        """
        args = {
            "ip_address": ip_address,
            "tunnel": tunnel
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_DEST_IP,
                                    **kwargs)

    def tunnel_clear_source_ip(self, device_name, **kwargs):
        """
        Description: Removes the source IP.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_SOURCE_IP,
                                    **kwargs)

    def tunnel_clear_dest_ip(self, device_name, **kwargs):
        """
        Description: Removes the destination IP.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_DEST_IP,
                                    **kwargs)

    def tunnel_clear_mode_gre(self, device_name, **kwargs):
        """
        Description: Removes tunnel mode GRE.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_MODE_GRE,
                                    **kwargs)

    # ##################################################################################################################
    #   Inspection Keywords   ##########################################################################################
    # ##################################################################################################################

    def tunnel_verify_interface_exists(self, device_name, tunnels='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [tunnel]      - The tunnel to check the existence of.

        Verify a given tunnel exists.
        """
        args = {"tunnel": tunnels}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL,
                                           self.parse_const.CHECK_TUNNEL_EXISTS, True,
                                           "Tunnel {tunnel} exists on {device_name}.",
                                           "Tunnel {tunnel} DOES NOT exist on {device_name}!",
                                           **kwargs)

    def tunnel_verify_interface_does_not_exist(self, device_name, tunnels='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [tunnel]      - The tunnel to check the existence of.

        Verify a given tunnel does not exist.
        """
        args = {"tunnel": tunnels}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL,
                                           self.parse_const.CHECK_TUNNEL_EXISTS, False,
                                           "Tunnel {tunnel} does not exist on {device_name}.",
                                           "Tunnel {tunnel} EXISTS on {device_name}!",
                                           **kwargs)

    def tunnel_verify_mode_gre(self, device_name, tunnels='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [tunnel]      - The tunnel to check the mode of.

        Verify tunnel(s) mode is GRE.
        """
        args = {"tunnel": tunnels,
                "mode": "gre"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL,
                                           self.parse_const.CHECK_TUNNEL_MODE, True,
                                           "Tunnel {tunnel} on {device_name} is configured as a GRE tunnel.",
                                           "Tunnel {tunnel} on {device_name} is NOT configured as a GRE tunnel!",
                                           **kwargs)

    def tunnel_verify_mode_gre_l2tb(self, device_name, tunnels='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [tunnel]      - The tunnel to check the mode of.

        Verify tunnel(s) mode is GRE L2 TBP.
        """
        args = {"tunnel": tunnels,
                "mode": "l2tb"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL,
                                           self.parse_const.CHECK_TUNNEL_MODE, True,
                                           "Tunnel {tunnel} on {device_name} is configured as an L2 tunnel bridge.",
                                           "Tunnel {tunnel} on {device_name} is NOT configured as an L2 tunnel bridge!",
                                           **kwargs)

    def tunnel_verify_mode_vxlan(self, device_name, tunnels='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [tunnel]      - The tunnel to check the mode of.

        Verify tunnel(s) mode is VxLAN.
        """
        args = {"tunnel": tunnels,
                "mode": "vxlan"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL,
                                           self.parse_const.CHECK_TUNNEL_MODE, True,
                                           "Tunnel {tunnel} on {device_name} is configured as a VXLAN L2 tunnel "
                                           "bridge.",
                                           "Tunnel {tunnel} on {device_name} is NOT configured as a VXLAN L2 tunnel "
                                           "bridge!",
                                           **kwargs)

    def tunnel_verify_mode_l2tb_port(self, device_name, tunnel='', port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [tunnel]      - The tunnel to check the mode of.

        Verify tunnel(s) mode is L2 TBP.
        """
        args = {"tunnel": tunnel,
                "port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL,
                                           self.parse_const.CHECK_TUNNEL_L2TB_PORT, True,
                                           "Tunnel {tunnel} on {device_name} is attached to port {port}.",
                                           "Tunnel {tunnel} on {device_name} is NOT attached to port {port}!",
                                           **kwargs)
