"""
Keyword class for all mlag cli commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.MlagConstants import \
    MlagConstants as ParseConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.MlagConstants import \
    MlagConstants as CommandConstants
# All imports above this line will be removed after generation.
# User imports must be added below.


class NetworkElementMlagGenKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementMlagGenKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "mlag"

    def mlag_enable_port_peer_id(self, device_name, port='', peer='', pid='', **kwargs):
        """
        Description: Enables the mlag id on the specified mlag port and peer.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "peer": peer,
            "pid": pid,
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_PORT_PEER_ID,
                                    **kwargs)

    def mlag_enable_port_reload_delay(self, device_name, **kwargs):
        """
        Description: Enables MLAG reload delay for MLAG ports.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_PORT_RELOAD_DELAY,
                                    **kwargs)

    def mlag_disable_port(self, device_name, port='', **kwargs):
        """
        Description: Disables an MLAG port.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_PORT,
                                    **kwargs)

    def mlag_disable_port_reload_delay(self, device_name, **kwargs):
        """
        Description: Disables MLAG reload delay for MLAG ports.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_PORT_RELOAD_DELAY,
                                    **kwargs)

    def mlag_create_peer(self, device_name, peer='', **kwargs):
        """
        Description: Creates an MLAG peer.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "peer": peer
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_PEER,
                                    **kwargs)

    def mlag_create_peer_auth_md5_key(self, device_name, peer='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "peer": peer
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_PEER_AUTH_MD5_KEY,
                                    **kwargs)

    def mlag_create_peer_auth_md5_key_name(self, device_name, key='', peer='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "key": key,
            "peer": peer
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_PEER_AUTH_MD5_KEY_NAME,
                                    **kwargs)

    def mlag_create_peer_auth_md5_key_encrypted(self, device_name, key='', peer='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "key": key,
            "peer": peer
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_PEER_AUTH_MD5_KEY_ENCRYPTED,
                                    **kwargs)

    def mlag_delete_peer(self, device_name, peer='', **kwargs):
        """
        Description: Removes an MLAG peer.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "peer": peer
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DELETE_PEER,
                                    **kwargs)

    def mlag_set_peer(self, device_name, peer='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "peer": peer
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PEER,
                                    **kwargs)

    def mlag_set_peer_alternate_ip(self, device_name, ip='', peer='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "ip": ip,
            "peer": peer
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PEER_ALTERNATE_IP,
                                    **kwargs)

    def mlag_set_peer_alternate_ip_none(self, device_name, peer='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "peer": peer
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PEER_ALTERNATE_IP_NONE,
                                    **kwargs)

    def mlag_set_peer_alternate_ip_vr(self, device_name, ip='', peer='', vr='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "ip": ip,
            "peer": peer,
            "vr": vr
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PEER_ALTERNATE_IP_VR,
                                    **kwargs)

    def mlag_set_peer_auth_none(self, device_name, peer='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "peer": peer
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PEER_AUTH_NONE,
                                    **kwargs)

    def mlag_set_peer_auth_md5_key(self, device_name, peer='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "peer": peer
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PEER_AUTH_MD5_KEY,
                                    **kwargs)

    def mlag_set_peer_auth_md5_key_name(self, device_name, key='', peer='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "key": key,
            "peer": peer
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PEER_AUTH_MD5_KEY_NAME,
                                    **kwargs)

    def mlag_set_peer_auth_md5_key_encrypted(self, device_name, key='', peer='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "key": key,
            "peer": peer
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PEER_AUTH_MD5_KEY_ENCRYPTED,
                                    **kwargs)

    def mlag_set_peer_interval(self, device_name, interval='', peer='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "interval": interval,
            "peer": peer
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PEER_INTERVAL,
                                    **kwargs)

    def mlag_set_peer_ipaddress(self, device_name, peer='', ip='', **kwargs):
        """
        Description: Configures an IPv4 or IPv6 address for the specified MLAG peer.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "ip": ip,
            "peer": peer
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PEER_IPADDRESS,
                                    **kwargs)

    def mlag_set_peer_ipaddress_vr(self, device_name, peer='', ip='', vr='', **kwargs):
        """
        Description: Configures an IPv4 or IPv6 address for the specified MLAG peer and virtual router.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "ip": ip,
            "peer": peer,
            "vr": vr
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PEER_IPADDRESS_VR,
                                    **kwargs)

    def mlag_set_peer_lacp_mac(self, device_name, mac='', peer='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "mac": mac,
            "peer": peer
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PEER_LACP_MAC,
                                    **kwargs)

    def mlag_set_peer_lacp_mac_auto(self, device_name, peer='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "peer": peer
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PEER_LACP_MAC_AUTO,
                                    **kwargs)

    def mlag_set_peer_new_name(self, device_name, peer='', name='', **kwargs):
        """
        Description: Renames a specified MLAG peer.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "name": name,
            "peer": peer
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PEER_NEW_NAME,
                                    **kwargs)

    # ##################################################################################################################
    #   Inspection Keywords   ##########################################################################################
    # ##################################################################################################################

    def mlag_verify_peer_exists(self, device_name, peer='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [peer]        - The MLAG peer to verify.

        Verifies the specified MLAG peer exists on the device.
        """
        args = {"peer": peer}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PEER,
                                           self.parse_const.VERIFY_MLAG_PEER_EXISTS, True,
                                           "The MLAG Peer {peer} is present on {device_name}.",
                                           "The MLAG Peer {peer} is NOT present on {device_name}!",
                                           **kwargs)

    def mlag_verify_peer_does_not_exist(self, device_name, peer='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [peer]        - The MLAG peer to verify.

        Verifies the specified MLAG peer is not present on the device.
        """
        args = {"peer": peer}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PEER,
                                           self.parse_const.VERIFY_MLAG_PEER_EXISTS, False,
                                           "The MLAG Peer {peer} is not present on {device_name}.",
                                           "The MLAG Peer {peer} IS present on {device_name}!",
                                           **kwargs)

    def mlag_verify_peer_ipaddress(self, device_name, peer='', ip='', vr="None", **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [peer]        - The MLAG peer to verify.
        [ip]          - The IPv4 or IPv6 address to verify.
        [vr]          - The Virtual Router to verify. (This is an optional argument).

        Verifies the given IP Address is set for the specified MLAG peer.
        """
        args = {"peer": peer,
                "ip": ip,
                "vr": vr}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PEER,
                                           self.parse_const.VERIFY_MLAG_PEER_IPADDRESS, True,
                                           "The ipaddress {ip} for MLAG Peer {peer} is correctly set on {device_name}.",
                                           "The ipaddress {ip} is NOT set for MLAG Peer {peer} on {device_name}!",
                                           **kwargs)

    def mlag_verify_peer_ipaddress_cleared(self, device_name, peer='', ip='', vr="None", **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [peer]        - The MLAG peer to verify.
        [ip]          - The IPv4 or IPv6 address to verify.
        [vr]          - The Virtual Router to verify. (This is an optional argument).

        Verifies the specified IP Address is NOT set on an MLAG peer.
        """
        args = {"peer": peer,
                "ip": ip,
                "vr": vr}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PEER,
                                           self.parse_const.VERIFY_MLAG_PEER_IPADDRESS, False,
                                           "The ipaddress {ip} is not set on MLAG Peer {peer} for {device_name}.",
                                           "The ipaddress {ip} IS set for MLAG Peer {peer} on {device_name}!",
                                           **kwargs)

    def mlag_verify_peer_id(self, device_name, peer='', pid='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [peer]        - The MLAG peer to verify.
        [pid]         - The MLAG peer id to verify.

        Verifies the specified MLAG Peer ID is set for the given MLAG peer.
        """
        args = {"peer": peer,
                "pid": pid}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORTS_ALL,
                                           self.parse_const.VERIFY_MLAG_PORT_PEER_ID, True,
                                           "MLAG Peer ID {pid} is set for MLAG Peer {peer} on {device_name}.",
                                           "MLAG Peer ID {pid} is NOT set for MLAG Peer {peer} on {device_name}!",
                                           **kwargs)

    def mlag_verify_peer_id_cleared(self, device_name, peer='', pid='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [peer]        - The MLAG peer to verify.
        [pid]         - The MLAG peer id to verify.

        Verifies the specified MLAG Peer ID is NOT set on the given MLAG peer.
        """
        args = {"peer": peer,
                "pid": pid}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PEER,
                                           self.parse_const.VERIFY_MLAG_PORT_PEER_ID, False,
                                           "MLAG Peer ID {pid} is not set on MLAG Peer {peer} on {device_name}.",
                                           "MLAG Peer ID {pid} IS set on MLAG Peer {peer} on {device_name}!",
                                           **kwargs)

    def mlag_verify_reload_delay_enabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [port]        - The MLAG port to verify.

        Verifies MLAG reload delay is enabled on a given MLAG port.
        """
        args = {"port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORTS,
                                           self.parse_const.VERIFY_MLAG_PORT_RELOAD_DELAY_IS_SET, True,
                                           "Reload Delay on MLAG port {port} is enabled on {device_name}.",
                                           "Reload Delay on MLAG port {port} is NOT enabled on {device_name}!",
                                           **kwargs)

    def mlag_verify_reload_delay_disabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [port]        - The MLAG port to verify.

        Verifies MLAG reload delay is disabled on a given MLAG port.
        """
        args = {"port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORTS,
                                           self.parse_const.VERIFY_MLAG_PORT_RELOAD_DELAY_IS_SET, False,
                                           "Reload Delay on MLAG port {port} is disabled on {device_name}.",
                                           "Reload Delay on MLAG port {port} IS enabled on {device_name}!",
                                           **kwargs)

    def mlag_verify_md5_authentication_enabled(self, device_name, peer='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [peer]        - The MLAG peer to verify.

        Verifies MD5 Authentication is set for the specified MLAG peer.
        """
        args = {"peer": peer}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PEER,
                                           self.parse_const.VERIFY_MLAG_PEER_AUTH_IS_SET, True,
                                           "MD5 Authentication is set for MLAG peer {peer} on {device_name}.",
                                           "MD5 Authentication is NOT set for MLAG peer {peer} on {device_name}!",
                                           **kwargs)

    def mlag_verify_port_disabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [port]        - The MLAG port to verify.

        Verifies an MLAG port is disabled.
        """
        args = {"port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORTS,
                                           self.parse_const.VERIFY_MLAG_PORT_RELOAD_DELAY_IS_SET, False,
                                           "MLAG port {port} is disabled on {device_name}.",
                                           "MLAG port {port} is NOT disabled on {device_name}!",
                                           **kwargs)
