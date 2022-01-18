"""
Keyword class for all macsec cli commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.MacsecConstants import \
    MacsecConstants as ParseConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.MacsecConstants import \
    MacsecConstants as CommandConstants
# All imports above this line will be removed after generation.
# User imports must be added below.


class NetworkElementMacsecGenKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementMacsecGenKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "macsec"

    def macsec_enable_ca_port(self, device_name, ca_name='', port='', **kwargs):
        """
        Description: Configures and enables a connectivity association on port(s).

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "ca_name": ca_name,
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_CA_PORT,
                                    **kwargs)

    def macsec_disable_ca_port(self, device_name, ca_name='', port='', **kwargs):
        """
        Description: Deletes specified port(s) from a MACsec Connectivity-Association.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "ca_name": ca_name,
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_CA_PORT,
                                    **kwargs)

    def macsec_create_ca(self, device_name, ca_name='', key_name='', key='', **kwargs):
        """
        Description: Creates a macsec connectivity association name a shared key name(CKN) and assigns a secret
                     key(CAK) to the Connectivity Association Name.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "ca_name": ca_name,
            "key": key,
            "key_name": key_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_CA,
                                    **kwargs)

    def macsec_create_ca_encrypted(self, device_name, ca_name='', key_name='', key='', **kwargs):
        """
        Description: Creates a macsec connectivity association name a shared key name(CKN) and assigns an encrypted
                     secret key(CAK) to the Connectivity Association Name.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "ca_name": ca_name,
            "key": key,
            "key_name": key_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_CA_ENCRYPTED,
                                    **kwargs)

    def macsec_set_cipher_suite_128(self, device_name, port='', **kwargs):
        """
        Description: Configures the MACsec cipher suite to 128bit encryption.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_CIPHER_SUITE_128,
                                    **kwargs)

    def macsec_set_cipher_suite_256(self, device_name, port='', **kwargs):
        """
        Description: Configures the MACsec cipher suite to 256bit encryption.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_CIPHER_SUITE_256,
                                    **kwargs)

    def macsec_set_confidentiality_offset_0(self, device_name, port='', **kwargs):
        """
        Description: Configures the MACsec confidentiality offset to 0.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_CONFIDENTIALITY_OFFSET_0,
                                    **kwargs)

    def macsec_set_confidentiality_offset_30(self, device_name, port='', **kwargs):
        """
        Description: Configures the MACsec confidentiality offset to 30.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_CONFIDENTIALITY_OFFSET_30,
                                    **kwargs)

    def macsec_set_confidentiality_offset_50(self, device_name, port='', **kwargs):
        """
        Description: Configures the MACsec confidentiality offset to 50.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_CONFIDENTIALITY_OFFSET_50,
                                    **kwargs)

    def macsec_set_hw_mode_half_duplex_mode(self, device_name, port='', **kwargs):
        """
        Description: Configures the MACsec hardware mode to half duplex.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_HW_MODE_HALF_DUPLEX_MODE,
                                    **kwargs)

    def macsec_set_hw_mode_macsec_mode(self, device_name, port='', **kwargs):
        """
        Description: Configures the MACsec hardware mode to MACsec mode.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_HW_MODE_MACSEC_MODE,
                                    **kwargs)

    def macsec_set_include_sci_enable(self, device_name, port='', **kwargs):
        """
        Description: Configures MACsec to enable include sci mode.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_INCLUDE_SCI_ENABLE,
                                    **kwargs)

    def macsec_set_include_sci_disable(self, device_name, port='', **kwargs):
        """
        Description: Configures MACsec to disable include sci mode.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_INCLUDE_SCI_DISABLE,
                                    **kwargs)

    def macsec_set_initialize_ports(self, device_name, port='', **kwargs):
        """
        Description: Initializes the MACsec ports.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_INITIALIZE_PORTS,
                                    **kwargs)

    def macsec_set_mka_actor_priority(self, device_name, priority='', port='', **kwargs):
        """
        Description: Configures the macsec actor priorty on port(s).

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "port": port,
            "priority": priority
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_MKA_ACTOR_PRIORITY,
                                    **kwargs)

    def macsec_set_replay_protect(self, device_name, port='', window_size='', **kwargs):
        """
        Description: Enables MACsec replay protect.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "port": port,
            "window_size": window_size
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_REPLAY_PROTECT,
                                    **kwargs)

    def macsec_set_replay_protect_disable(self, device_name, port='', **kwargs):
        """
        Description: Disables MACsec replay protect.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_REPLAY_PROTECT_DISABLE,
                                    **kwargs)

    def macsec_clear_counters_all(self, device_name, **kwargs):
        """
        Description: Clears all MACsec counters.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_COUNTERS_ALL,
                                    **kwargs)

    def macsec_clear_counters_on_port(self, device_name, port='', **kwargs):
        """
        Description: Clears all MACsec counters on the specified port(s).

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_COUNTERS_ON_PORT,
                                    **kwargs)

    def macsec_delete_ca(self, device_name, ca_name='', **kwargs):
        """
        Description: Deletes a specified MACsec Connectivity-Association.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "ca_name": ca_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DELETE_CA,
                                    **kwargs)

    # ##################################################################################################################
    #   Inspection Keywords   ##########################################################################################
    # ##################################################################################################################

    def macsec_verify_enabled_on_port(self, device_name, port='', **kwargs):
        """
        Keyword arguments:
        [device_name] - The device the keyword will be run against.
        [port]        - The port(s) to verify macsec on.

        Verifies that the MAC Authentication feature is enabled on the specified port(s).
        """
        args = {"port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT,
                                           self.parse_const.VERIFY_MACSEC_ON_PORT, True,
                                           "MAC Authentication is enabled on {device_name} port {port}.",
                                           "MAC Authentication is NOT enabled on {device_name} port {port}!",
                                           **kwargs)

    def macsec_verify_disabled_on_port(self, device_name, port='', **kwargs):
        """
        Keyword arguments:
        [device_name] - The device the keyword will be run against.
        [port]        - The port(s) to verify macsec on.

        Verifies that the MAC Authentication feature is disabled on the specified port(s).
        """
        args = {"port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT,
                                           self.parse_const.VERIFY_MACSEC_ON_PORT, False,
                                           "MAC Authentication is disabled on {device_name} port {port}.",
                                           "MAC Authentication is NOT disabled on {device_name} port {port}!",
                                           **kwargs)

    def macsec_verify_ca_port(self, device_name, ca_name='', port='', **kwargs):
        """
        Keyword arguments:
        [device_name] - The device the keyword will be run against.
        [ca_name]     - The Connectivity Association name to verify.
        [port]        - The macsec port to verify

        Verifies the specified port(s) belong to a specified connectivity-association.
        """
        args = {"ca_name": ca_name,
                "port": port}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_CONNECTIVITY_ASSOCIATION_ALL,
                                           self.parse_const.VERIFY_MACSEC_CA_PORT, True,
                                           "Port(s) {port} belong to MACsec Connectivity-Association {ca_name} "
                                           "on {device_name}.",
                                           "Port(s) {port} do NOT belong to MACsec Connectivity-Association "
                                           "{ca_name} on {device_name}!",
                                           **kwargs)

    def macsec_verify_ca_ckn(self, device_name, ca_name='', ckn_name='', **kwargs):
        """
        Keyword arguments:
        [device_name] - The device the keyword will be run against.
        [ca_name]     - The Connectivity Association name to verify.
        [ckn_name]    - The CKN name to verify

        Verifies the CKN name belongs to the specified Connectivity Association.
        """
        args = {"ca_name": ca_name,
                "ckn_name": ckn_name}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_CONNECTIVITY_ASSOCIATION_ALL,
                                           self.parse_const.VERIFY_MACSEC_CA_CKN, True,
                                           "MACsec CKN {ckn_name} belongs to Connectivity-Association {ca_name} "
                                           "on {device_name}.",
                                           "MACsec CKN {ckn_name} does NOT belong to Connectivity-Association "
                                           "{ca_name} on {device_name}!",
                                           **kwargs)

    def macsec_verify_ca_exists(self, device_name, ca_name='', **kwargs):
        """
        Keyword arguments:
        [device_name] - The device the keyword will be run against.
        [ca_name]     - The Connectivity Association name to verify.

        Verifies that a macsec connectivity association exists on the device.
        """
        args = {"ca_name": ca_name}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_CONNECTIVITY_ASSOCIATION_ALL,
                                           self.parse_const.VERIFY_MACSEC_CA, True,
                                           "The MACsec Connectivity-Association {ca_name] exists on "
                                           "{device_name}.",
                                           "The MACsec Connectivity-Association {ca_name} does NOT exist on "
                                           "{device_name}!",
                                           **kwargs)

    def macsec_verify_ca_does_not_exist(self, device_name, ca_name='', **kwargs):
        """
        Keyword arguments:
        [device_name] - The device the keyword will be run against.
        [ca_name]     - The Connectivity Association name to verify.

        Verifies that a macsec connectivity association does not exist on the device.
        """
        args = {"ca_name": ca_name}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_CONNECTIVITY_ASSOCIATION_ALL,
                                           self.parse_const.VERIFY_MACSEC_CA, False,
                                           "The MACsec Connectivity-Association {ca_name] does not exist on "
                                           "{device_name}.",
                                           "The MACsec Connectivity-Association {ca_name} Exists on "
                                           "{device_name}!",
                                           **kwargs)

    def macsec_verify_port_actor_priority(self, device_name, port='', priority='', **kwargs):
        """
        Keyword arguments:
        [device_name]  - The device the keyword will be run against.
        [priority]     - The macsec actor priority value to verify.

        Verifies a given macsec actor priority value is set.
        """
        args = {"port": port,
                "priority": priority}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_DETAIL,
                                           self.parse_const.VERIFY_MACSEC_MKA_ACTOR_PRIORITY, True,
                                           "MACsec Actor Priority is correctly set to {priority} on {device_name}.",
                                           "MACsec Actor Priority is not set to {priority} on {device_name}!",
                                           **kwargs)

    def macsec_verify_port_removed_from_ca(self, device_name, ca_name='', port='', **kwargs):
        """
        Keyword arguments:
        [device_name] - The device the keyword will be run against.
        [ca_name]     - The Connectivity Association name to verify.
        [port]        - The macsec port(s) to verify

        Verifies the specified port(s) are removed from the specified connectivity-association.
        """
        args = {"ca_name": ca_name,
                "port": port}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_CONNECTIVITY_ASSOCIATION_ALL,
                                           self.parse_const.VERIFY_MACSEC_CA_PORT, False,
                                           "Port(s) {port} do NOT belong to MACsec Connectivity-Association "
                                           "{ca_name} on {device_name}.",
                                           "Port(s) {port} STILL belong to MACsec Connectivity-Association "
                                           "{ca_name} on {device_name}!",
                                           **kwargs)

    def macsec_verify_port_cipher_suite(self, device_name, port='', cipher_value='', **kwargs):
        """
        Keyword arguments:
        [device_name]  - The device the keyword will be run against.
        [port]         - The port(s) to verify macauth cipher suite on.
        [cipher_value] - The cipher suite value expected on the port.  Either 128 or 256.

        Verifies that the given port has the macsec cipher suite value set to 128 or 256.
        """
        args = {"port": port,
                "cipher_value": cipher_value}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_CONFIGURATION,
                                           self.parse_const.VERIFY_MACSEC_CIPHER_SUITE, True,
                                           "Port {port} cipher suite is properly set to gcm-aes-{cipher_value}.",
                                           "Port {port} cipher suite is NOT set to gcm-aes-{cipher_value}!",
                                           **kwargs)

    def macsec_verify_port_connection_status(self, device_name, port='', status='', **kwargs):
        """
        Keyword arguments:
        [device_name] - The device the keyword will be run against.
        [port]        - The port(s) to verify macsec on.
        [status]      - The macsec status to verify.

        Verifies the connection status for the specified macsec port.
        """
        args = {"port": port,
                "status": status}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_DETAIL,
                                           self.parse_const.VERIFY_MACSEC_PORT_CONNECTION_STATUS, True,
                                           "The macsec status for port {port} is correctly set to {status} on "
                                           "{device_name}.",
                                           "The macsec status for port {port} is NOT set to {status} on "
                                           "on {device_name}!",
                                           **kwargs)

    def macsec_verify_port_cipher_suite_admin(self, device_name, port='', suite='', **kwargs):
        """
        Keyword arguments:
        [device_name]  - The device the keyword will be run against.
        [port]         - The port(s) to verify macsec on.
        [suite]        - The macsec cipher suite to verify.

        Verifies the cipher suite admin status for the specified macsec port.
        """
        args = {"port": port,
                "suite": suite}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_DETAIL,
                                           self.parse_const.VERIFY_MACSEC_PORT_CIPHER_SUITE_ADMIN, True,
                                           "The cipher suite admin for macsec port {port} is correctly set to {suite} "
                                           "on {device_name}.",
                                           "The cipher suite admin for macsec port {port} is NOT set to {suite} "
                                           "on {device_name}!",
                                           **kwargs)

    def macsec_verify_port_cipher_suite_oper(self, device_name, port='', suite='', **kwargs):
        """
        Keyword arguments:
        [device_name]  - The device the keyword will be run against.
        [port]         - The port(s) to verify macsec on.
        [suite]        - The macsec cipher suite to verify.

        Verifies the cipher suite operational status for the specified macsec port.
        """
        args = {"port": port,
                "suite": suite}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_DETAIL,
                                           self.parse_const.VERIFY_MACSEC_PORT_CIPHER_SUITE_OPER, True,
                                           "The cipher suite oper for macsec port {port} is correctly set to {suite} "
                                           "on {device_name}.",
                                           "The cipher suite oper for macsec port {port} is NOT set to {suite} "
                                           "on {device_name}!",
                                           **kwargs)

    def macsec_verify_port_confidentiality_offset_admin(self, device_name, port='', offset='', **kwargs):
        """
        Keyword arguments:
        [device_name]  - The device the keyword will be run against.
        [port]         - The port(s) to verify macsec on.
        [offset]       - The macsec confidentiality offset to verify.

        Verifies the confidentiality offset admin status for the specified macsec port.
        """
        args = {"port": port,
                "offset": offset}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_DETAIL,
                                           self.parse_const.VERIFY_MACSEC_PORT_CONFIDENTIALITY_OFFSET_ADMIN, True,
                                           "The confidentiality offset admin for macsec port {port} is correctly set "
                                           "to {offset} on {device_name}.",
                                           "The confidentiality offset admin for macsec port {port} is NOT set to "
                                           "{offset} on {device_name}!",
                                           **kwargs)

    def macsec_verify_port_confidentiality_offset_oper(self, device_name, port='', offset='', **kwargs):
        """
        Keyword arguments:
        [device_name]  - The device the keyword will be run against.
        [port]         - The port(s) to verify macsec on.
        [offset]       - The macsec confidentiality offset to verify.

        Verifies the confidentiality offset operational status for the specified macsec port.
        """
        args = {"port": port,
                "offset": offset}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_DETAIL,
                                           self.parse_const.VERIFY_MACSEC_PORT_CONFIDENTIALITY_OFFSET_OPER, True,
                                           "The confidentiality offset oper for macsec port {port} is correctly set "
                                           "to {offset} on {device_name}.",
                                           "The confidentiality offset oper for macsec port {port} is NOT set to "
                                           "{offset} on {device_name}!",
                                           **kwargs)

    def macsec_verify_tx_port_key_number(self, device_name, port='', tx_key_num='', **kwargs):
        """
        Keyword arguments:
        [device_name]  - The device the keyword will be run against.
        [port]         - The port(s) to verify macsec on.
        [tx_key_num]   - The macsec key number value to verify for the specified tx port.

        Verifies the MACsec key number value for the specified Tx port.
        """
        args = {"port": port,
                "tx_key_num": tx_key_num}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_DETAIL,
                                           self.parse_const.VERIFY_MACSEC_TX_PORT_KEY_NUMBER, True,
                                           "The MACsec key number {tx_key_num} exists for Tx port {port} on "
                                           "{device_name}.",
                                           "The MACsec key number {tx_key_num} does NOT exist for Tx port {port} on "
                                           "{device_name}!",
                                           **kwargs)

    def macsec_verify_rx_port_key_number(self, device_name, port='', rx_key_num='', **kwargs):
        """
        Keyword arguments:
        [device_name]  - The device the keyword will be run against.
        [port]         - The port(s) to verify macsec on.
        [rx_key_num]   - The macsec key number value to verify for the specified rx port.

        Verifies the MACsec key number value for the specified Rx port.
        """
        args = {"port": port,
                "rx_key_num": rx_key_num}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_DETAIL,
                                           self.parse_const.VERIFY_MACSEC_RX_PORT_KEY_NUMBER, True,
                                           "The MACsec key number {rx_key_num} exists for Rx port {port} on "
                                           "{device_name}.",
                                           "The MACsec key number {rx_key} does NOT exist for Rx port {port} on "
                                           "{device_name}!",
                                           **kwargs)

    def macsec_verify_tx_port_association_number(self, device_name, port='', tx_assoc_num='', **kwargs):
        """
        Keyword arguments:
        [device_name]  - The device the keyword will be run against.
        [port]         - The port(s) to verify macsec on.
        [tx_assoc_num] - The macsec association number value to verify for the specified tx port.

        Verifies the macsec association number value for the specified Tx port and direction.
        """
        args = {"port": port,
                "tx_assoc_num": tx_assoc_num}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_DETAIL,
                                           self.parse_const.VERIFY_MACSEC_TX_PORT_ASSOCIATION_NUMBER, True,
                                           "The MACsec association number {tx_assoc_num} exists for Tx port {port} on "
                                           "{device_name}.",
                                           "The MACsec association number {tx_assoc_num} does NOT exist for Tx "
                                           "port {port} on {device_name}!",
                                           **kwargs)

    def macsec_verify_rx_port_association_number(self, device_name, port='', rx_assoc_num='', **kwargs):
        """
        Keyword arguments:
        [device_name]  - The device the keyword will be run against.
        [port]         - The port(s) to verify macsec on.
        [rx_assoc_num] - The macsec association number value to verify for the specified rx port.

        Verifies the macsec association number value for the specified Rx port and direction.
        """
        args = {"port": port,
                "rx_assoc_num": rx_assoc_num}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_DETAIL,
                                           self.parse_const.VERIFY_MACSEC_RX_PORT_ASSOCIATION_NUMBER, True,
                                           "The MACsec association number {rx_assoc_num} exists for Rx port {port} on "
                                           "{device_name}.",
                                           "The MACsec association number {rx_assoc_num} does NOT exist for Rx "
                                           "port {port} on {device_name}!",
                                           **kwargs)

    def macsec_verify_self_elected_key_server(self, device_name, port='', **kwargs):
        """
        Keyword arguments:
        [device_name]  - The device the keyword will be run against.
        [port]         - The port(s) to verify macsec Local keyserver on.

        Verifies the macsec key server election is Local on the specified port.
        """
        args = {"port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT,
                                           self.parse_const.VERIFY_MACSEC_SELF_ELECTED_KEY_SERVER, True,
                                           "The MACsec port {port} has its Key Server election set to Local.",
                                           "The MACsec port {port} DOES NOT have its Key Server election set to Local.",
                                           **kwargs)

    def macsec_verify_peer_elected_key_server(self, device_name, port='', **kwargs):
        """
        Keyword arguments:
        [device_name]  - The device the keyword will be run against.
        [port]         - The port(s) to verify macsec Peer keyserver on.

        Verifies the macsec key server election is Peer on the specified port.
        """
        args = {"port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT,
                                           self.parse_const.VERIFY_MACSEC_PEER_ELECTED_KEY_SERVER, True,
                                           "The MACsec port {port} has its Key Server election set to Peer.",
                                           "The MACsec port {port} DOES NOT have its Key Server election set to Peer.",
                                           **kwargs)

    def macsec_verify_tx_port_no_errors(self, device_name, port='', **kwargs):
        """
        Keyword arguments:
        [device_name]  - The device the keyword will be run against.
        [port]         - The port(s) to verify MACsec Tx error counters are zero on.

        Verifies the MACsec Tx error counts are zero on the specified port.
        """
        args = {"port": port}
        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_COUNTERS,
                                           self.parse_const.VERIFY_MACSEC_TX_PORT_NO_ERRORS, True,
                                           "The MACsec port {port} Tx Error Counters are all zero.",
                                           "The MACsec port {port} Tx Error Counters are NOT all zero.",
                                           **kwargs)

    def macsec_verify_rx_port_no_errors(self, device_name, port='', **kwargs):
        """
        Keyword arguments:
        [device_name]  - The device the keyword will be run against.
        [port]         - The port(s) to verify MACsec Rx error counters are zero on.

        Verifies the MACsec Rx error counts are zero on the specified port.
        """
        args = {"port": port}
        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_COUNTERS,
                                           self.parse_const.VERIFY_MACSEC_RX_PORT_NO_ERRORS, True,
                                           "The MACsec port {port} Rx Error Counters are all zero.",
                                           "The MACsec port {port} Rx Error Counters are NOT all zero.",
                                           **kwargs)
        

    def macsec_verify_tx_sc_octets_encrypted(self, device_name, port='', count='', count_max='', **kwargs):
        """
        Keyword arguments:
        [device_name]  - The device the keyword will be run against.
        [port]         - The port(s) to verify MACsec counter value.
        [count]        - The value to compare against.
        [count_max]    - (optional) If specified actual value must be between
                         'count' and 'count_max'. If not specified actual
                         value must equal 'count'.
        """
        args = {"port": port,
                "count_max": str(count_max),
                "count": str(count)}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_COUNTERS,
                                           self.parse_const.VERIFY_MACSEC_TX_SC_OCTETS_ENCRYPTED, True,
                                           "MACsec port {port}'s Tx SC Octets Encrypted is in range {count}..{count_max}.",
                                           "MACsec port {port}'s Tx SC Octets Encrypted is NOT in range {count}..{count_max}.",
                                           **kwargs)

    def macsec_verify_tx_sc_encrypted_packets(self, device_name, port='', count='', count_max='', **kwargs):
        """
        Keyword arguments:
        [device_name]  - The device the keyword will be run against.
        [port]         - The port(s) to verify MACsec counter value.
        [count]        - The value to compare against.
        [count_max]    - (optional) If specified actual value must be between
                         'count' and 'count_max'. If not specified actual
                         value must equal 'count'.
        """
        args = {"port": port,
                "count_max": str(count_max),
                "count": str(count)}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_COUNTERS,
                                           self.parse_const.VERIFY_MACSEC_TX_SC_ENCRYPTED_PACKETS, True,
                                           "MACsec port {port}'s Tx SC Encrypted Pkts is in range {count}..{count_max}.",
                                           "MACsec port {port}'s Tx SC Encrypted Pkts is in range {count}..{count_max}.",
                                           **kwargs)

    def macsec_verify_tx_sa_encrypted_packets(self, device_name, port='', count='', count_max='', **kwargs):
        """
        Keyword arguments:
        [device_name]  - The device the keyword will be run against.
        [port]         - The port(s) to verify MACsec counter value.
        [count]        - The value to compare against.
        [count_max]    - (optional) If specified actual value must be between
                         'count' and 'count_max'. If not specified actual
                         value must equal 'count'.
        """
        args = {"port": port,
                "count_max": str(count_max),
                "count": str(count)}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_COUNTERS,
                                           self.parse_const.VERIFY_MACSEC_TX_SA_ENCRYPTED_PACKETS, True,
                                           "MACsec port {port}'s Tx SA Encrypted Pkts is in range {count}..{count_max}.",
                                           "MACsec port {port}'s Tx SA Encrypted Pkts is NOT is in range {count}..{count_max}.",
                                           **kwargs)

    def macsec_verify_rx_sc_octets_decrypted(self, device_name, port='', count='', count_max='', **kwargs):
        """
        Keyword arguments:
        [device_name]  - The device the keyword will be run against.
        [port]         - The port(s) to verify MACsec counter value.
        [count]        - The value to compare against.
        [count_max]    - (optional) If specified actual value must be between
                         'count' and 'count_max'. If not specified actual
                         value must equal 'count'.
        """
        args = {"port": port,
                "count_max": str(count_max),
                "count": str(count)}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_COUNTERS,
                                           self.parse_const.VERIFY_MACSEC_RX_SC_OCTETS_DECRYPTED, True,
                                           "MACsec port {port}'s Tx RC Octets Decrypted is in range {count}..{count_max}.",
                                           "MACsec port {port}'s Tx RC Octets Decrypted is NOT in range {count}..{count_max}.",
                                           **kwargs)

    def macsec_verify_rx_sc_ok_packets(self, device_name, port='', count='', count_max='', **kwargs):
        """
        Keyword arguments:
        [device_name]  - The device the keyword will be run against.
        [port]         - The port(s) to verify MACsec counter value.
        [count]        - The value to compare against.
        [count_max]    - (optional) If specified actual value must be between
                         'count' and 'count_max'. If not specified actual
                         value must equal 'count'.
        """
        args = {"port": port,
                "count_max": str(count_max),
                "count": str(count)}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_COUNTERS,
                                           self.parse_const.VERIFY_MACSEC_RX_SC_OK_PACKETS, True,
                                           "MACsec port {port}'s Rx SC OK Pkts is in range {count}..{count_max}.",
                                           "MACsec port {port}'s Rx SC OK Pkts is NOT is in range {count}..{count_max}.",
                                           **kwargs)

    def macsec_verify_rx_sa_ok_packets(self, device_name, port='', count='', count_max='', **kwargs):
        """
        Keyword arguments:
        [device_name]  - The device the keyword will be run against.
        [port]         - The port(s) to verify MACsec counter value.
        [count]        - The value to compare against.
        [count_max]    - (optional) If specified actual value must be between
                         'count' and 'count_max'. If not specified actual
                         value must equal 'count'.
        """
        args = {"port": port,
                "count_max": str(count_max),
                "count": str(count)}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_COUNTERS,
                                           self.parse_const.VERIFY_MACSEC_RX_SA_OK_PACKETS, True,
                                           "MACsec port {port}'s Rx SA OK Pkts is in range {count}..{count_max}.",
                                           "MACsec port {port}'s Rx SA OK Pkts is NOT is in range {count}..{count_max}.",
                                           **kwargs)
