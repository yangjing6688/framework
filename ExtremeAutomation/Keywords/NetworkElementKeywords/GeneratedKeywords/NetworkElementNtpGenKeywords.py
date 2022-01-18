"""
Keyword class for all ntp cli commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.NtpConstants import \
    NtpConstants as ParseConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.NtpConstants import \
    NtpConstants as CommandConstants
# All imports above this line will be removed after generation.
# User imports must be added below.


class NetworkElementNtpGenKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementNtpGenKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "ntp"

    def ntp_enable_client(self, device_name, ip='', **kwargs):
        """
        Description: Enables the NTP client on the device.

        Supported Agents and OS:
            CLI: EOS, EXOS, VOSS, SLX
            SNMP: VOSS
        """
        args = {
            "ip": ip
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_CLIENT,
                                    **kwargs)

    def ntp_disable_client(self, device_name, ip='', **kwargs):
        """
        Description: Disables the NTP client on the device.

        Supported Agents and OS:
            CLI: EOS, EXOS, VOSS, SLX
            SNMP: VOSS
        """
        args = {
            "ip": ip
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_CLIENT,
                                    **kwargs)

    def ntp_create_server(self, device_name, server='', **kwargs):
        """
        Description: Creates an NTP server to update from using the supplied server IP.

        Supported Agents and OS:
            CLI: EOS, EXOS, VOSS, SLX
            SNMP: VOSS
        """
        args = {
            "server": server
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_SERVER,
                                    **kwargs)

    def ntp_create_server_key(self, device_name, server='', key='', **kwargs):
        """
        Description: Configures an NTP server to update the key from using the supplied server IP.

        Supported Agents and OS:
            CLI: EOS, EXOS, VOSS, SLX
            SNMP: VOSS
        """
        args = {
            "key": key,
            "server": server
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_SERVER_KEY,
                                    **kwargs)

    def ntp_create_server_precedence(self, device_name, server='', precedence='', **kwargs):
        """
        Description: Creates an NTP server to update from using the supplied server IP.

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "precedence": precedence,
            "server": server
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_SERVER_PRECEDENCE,
                                    **kwargs)

    def ntp_create_server_precedence_key(self, device_name, key='', precedence='', server='', **kwargs):
        """
        Description: Configures an NTP server to update the key from using the supplied server IP.

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "key": key,
            "precedence": precedence,
            "server": server
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_SERVER_PRECEDENCE_KEY,
                                    **kwargs)

    def ntp_delete_server(self, device_name, server='', **kwargs):
        """
        Description: Removes the given NTP server from the device.

        Supported Agents and OS:
            CLI: EOS, EXOS, VOSS, SLX
            SNMP: VOSS
        """
        args = {
            "server": server
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DELETE_SERVER,
                                    **kwargs)

    def ntp_enable_client_vlan(self, device_name, vlan='', **kwargs):
        """
        Description: Enables the NTP client on the specified VLAN.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_CLIENT_VLAN,
                                    **kwargs)

    def ntp_disable_client_vlan(self, device_name, vlan='', **kwargs):
        """
        Description: Disables the NTP client on the specified VLAN.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_CLIENT_VLAN,
                                    **kwargs)

    def ntp_enable_server(self, device_name, server='', **kwargs):
        """
        Description: Enables the server for participation in time updates.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "server": server
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_SERVER,
                                    **kwargs)

    def ntp_disable_server(self, device_name, server='', **kwargs):
        """
        Description: Disables the server for participation in time updates.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "server": server
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_SERVER,
                                    **kwargs)

    def ntp_enable_server_auth(self, device_name, server='', **kwargs):
        """
        Description: Enables NTP server authentication.

        Supported Agents and OS:
            CLI: VOSS, SLX
            SNMP: VOSS
        """
        args = {
            "server": server
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_SERVER_AUTH,
                                    **kwargs)

    def ntp_disable_server_auth(self, device_name, server='', **kwargs):
        """
        Description: Disables NTP server authentication.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "server": server
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_SERVER_AUTH,
                                    **kwargs)

    def ntp_set_global_interval(self, device_name, interval='', **kwargs):
        """
        Description: Time interval between successive NTP updates in minutes.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "interval": interval
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_GLOBAL_INTERVAL,
                                    **kwargs)

    def ntp_set_server_source_ip(self, device_name, server='', source_ip='', **kwargs):
        """
        Description: Configures the source IP address for NTP packets.

        Supported Agents and OS:
            CLI: VOSS, SLX
            SNMP: VOSS
        """
        args = {
            "server": server,
            "source_ip": source_ip
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_SERVER_SOURCE_IP,
                                    **kwargs)

    def ntp_set_auth(self, device_name, index='', **kwargs):
        """
        Description: Creates the public Key used to generate MD5/SHA1 digest.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "index": index
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_AUTH,
                                    **kwargs)

    def ntp_set_auth_key(self, device_name, index='', secret='', **kwargs):
        """
        Description: Configures the Private Key used to generate MD5/SHA1 Digest.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "index": index,
            "secret": secret
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_AUTH_KEY,
                                    **kwargs)

    def ntp_set_auth_md5(self, device_name, index='', md5_string='', **kwargs):
        """
        Description: Configures the Private Key used to use MD5 for the digest.

        Supported Agents and OS:
            CLI: VOSS, SLX
            SNMP: VOSS
        """
        args = {
            "index": index,
            "md5_string": md5_string
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_AUTH_MD5,
                                    **kwargs)

    def ntp_set_auth_sha1(self, device_name, index='', **kwargs):
        """
        Description: Configures the Private Key used to use SHA1 for the digest.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "index": index
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_AUTH_SHA1,
                                    **kwargs)

    def ntp_clear_auth_key(self, device_name, index='', **kwargs):
        """
        Description: Deletes the public Key used to generate MD5/SHA1 digest.

        Supported Agents and OS:
            CLI: VOSS, SLX
            SNMP: VOSS
        """
        args = {
            "index": index
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_AUTH_KEY,
                                    **kwargs)

    def ntp_set_source_ip_mm(self, device_name, **kwargs):
        """
        Description: Sets the NTP source IP to use the local MM IP for NTP packets.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_SOURCE_IP_MM,
                                    **kwargs)

    def ntp_set_source_ip_chassis(self, device_name, **kwargs):
        """
        Description: Sets the NTP source IP to use the chassis IP for NTP packets.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_SOURCE_IP_CHASSIS,
                                    **kwargs)

    # ##################################################################################################################
    #   Inspection Keywords   ##########################################################################################
    # ##################################################################################################################

    def ntp_verify_server_enabled(self, device_name, server='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device to check for the NTP Server.
        [server]  -  The IPv4 address of the NTP server.

        Verifies if the server for participation in time updates is enabled.
        VOSS only.
        """
        args = {"server": server}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SERVERS,
                                           self.parse_const.CHECK_NTP_SERVER_ENABLED, True,
                                           "NTP server {server} is enabled.",
                                           "NTP server {server} is NOT enabled!",
                                           **kwargs)

    def ntp_verify_server_disabled(self, device_name, server='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device to check for the NTP Server.
        [server]  -  The IPv4 address of the NTP server.

        Verifies if the server for participation in time updates is disabled.
        VOSS only.
        """
        args = {"server": server}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SERVERS,
                                           self.parse_const.CHECK_NTP_SERVER_ENABLED, False,
                                           "NTP server {server} is disabled.",
                                           "NTP server {server} is NOT disabled!",
                                           **kwargs)

    def ntp_verify_client_enabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device to verify the NTP Client on.

        Verifies that the NTP Client is enabled on the device.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.CHECK_NTP_ENABLED, True,
                                           "NTP is globally enabled.",
                                           "NTP is globally disabled!",
                                           **kwargs)

    def ntp_verify_client_disabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device to verify the NTP Client on.

        Verifies that the NTP Client is enabled on the device.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.CHECK_NTP_ENABLED, False,
                                           "NTP is globally disabled.",
                                           "NTP is globally enabled!",
                                           **kwargs)

    def ntp_verify_server_exists(self, device_name, server='', key='', precedence='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device to check for the NTP Server.
        [server] -       The IP Address of the NTP Server.
        [precedence] -   The server's precedence in relation to others configured. (EOS Only)
        [key] -          The authentication key, if applicable, for the NTP Server.

        Verifies that the given server is configured on the device.
        """
        args = {"server": server,
                "key": key,
                "precedence": precedence}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SERVERS,
                                           self.parse_const.CHECK_NTP_SERVER_EXISTS, True,
                                           "NTP server {server} exists.",
                                           "NTP server {server} does not exist!",
                                           **kwargs)

    def ntp_verify_server_does_not_exist(self, device_name, server='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device to check for the NTP Server.
        [server] -       The IP Address of the NTP Server.
        [precedence] -   The server's precedence in relation to others configured. (EOS Only)
        [key] -          The authentication key, if applicable, for the NTP Server.

        Verifies that the given server is NOT configured on the device.
        """
        args = {"server": server}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SERVERS,
                                           self.parse_const.CHECK_NTP_SERVER_EXISTS, False,
                                           "NTP server {server} does not exist.",
                                           "NTP server {server} exists!",
                                           **kwargs)

    def ntp_verify_interval(self, device_name, interval='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device to check for the NTP Server.
        [interval]  -  The value of NTP updates in minutes.

        Verifies the time interval between successive NTP updates in minutes.
        VOSS only.
        """
        args = {"interval": interval}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.CHECK_NTP_INTERVAL, True,
                                           "NTP interval is {interval}.",
                                           "NTP interval {interval} is NOT interval!",
                                           **kwargs)

    def ntp_verify_server_key_id(self, device_name, server='', key_index='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device to check for the NTP Server.
        [server]  -  The IPv4 address of the NTP server.
        {key_index} - The index of the key used by the server.

        Verifies the Public Key ID used to generate digest for the server.
        VOSS only.
        """
        args = {"server": server,
                "key_index": key_index}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SERVERS,
                                           self.parse_const.CHECK_NTP_SERVER_KEY_INDEX, True,
                                           "NTP server {server} key is {key_index}.",
                                           "NTP server {server} key is NOT {key_index}!",
                                           **kwargs)

    def ntp_verify_server_auth_enabled(self, device_name, server='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device to check for the NTP Server.
        [server]  -  The IPv4 address of the NTP server.

        Verifies if the NTP server is enabled for authentication.
        VOSS only.
        """
        args = {"server": server}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SERVERS,
                                           self.parse_const.CHECK_NTP_SERVER_AUTHENTICATION_ENABLED, True,
                                           "NTP server {server} authentication is enabled.",
                                           "NTP server {server} authentication is NOT enabled!",
                                           **kwargs)

    def ntp_verify_server_auth_disabled(self, device_name, server='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device to check for the NTP Server.
        [server]  -  The IPv4 address of the NTP server.

        Verifies if the NTP server is enabled for authentication.
        VOSS only.
        """
        args = {"server": server}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SERVERS,
                                           self.parse_const.CHECK_NTP_SERVER_AUTHENTICATION_ENABLED, False,
                                           "NTP server {server} authentication is disabled.",
                                           "NTP server {server} authentication is NOT disabled!",
                                           **kwargs)

    def ntp_verify_server_source_ip(self, device_name, server='', source_ip='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device to check for the NTP Server.
        [server]  -  The IPv4 address of the NTP server.
        [source_ip]  - The source IP address used for NTP messaging on the server.

        Verifies the source IP address for NTP packets.
        VOSS only.
        """
        args = {"server": server,
                "source_ip": source_ip}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SERVERS,
                                           self.parse_const.CHECK_NTP_SERVER_SOURCE_IP, True,
                                           "NTP server {server} source IP is {source_ip}.",
                                           "NTP server {server} source IP is NOT {source_ip}!",
                                           **kwargs)

    def ntp_verify_auth_key_exists(self, device_name, key_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device to check for the NTP Server.
        [key_id]  -  Private Key index used to generate MD5/SHA1 Digest.

        Verifies that the Private Key used to generate MD5/SHA1 Digest exists.
        VOSS only.
        """
        args = {"key_id": key_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_KEY,
                                           self.parse_const.CHECK_NTP_KEY_EXISTS, True,
                                           "NTP key ID {key_id} exists.",
                                           "NTP key ID {key_id} does NOT exist!",
                                           **kwargs)

    def ntp_verify_auth_key_does_not_exist(self, device_name, key_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device to check for the NTP Server.
        [key_id]  -  Public Key index used to generate MD5/SHA1 Digest.

        Verifies that the Private Key used to generate MD5/SHA1 Digest does not exist.
        VOSS only.
        """
        args = {"key_id": key_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_KEY,
                                           self.parse_const.CHECK_NTP_KEY_EXISTS, False,
                                           "NTP key ID {key_id} does not exist.",
                                           "NTP key ID {key_id} exists!",
                                           **kwargs)

    def ntp_verify_auth_key_secret(self, device_name, key_id='', key_secret='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device to check for the NTP Server.
        [key_id]  -  Public Key index used to generate MD5/SHA1 Digest.
        [key_secret]  - The Private Key used to generate MD5/SHA1 Digest.

        Verifies the Private Key used to generate MD5/SHA1 Digest for the public key ID.
        VOSS only.
        """
        args = {"key_id": key_id,
                "key_secret": key_secret}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_KEY,
                                           self.parse_const.CHECK_NTP_KEY_SECRET, True,
                                           "NTP key ID {key_id} secret is {key_secret}.",
                                           "NTP key ID {key_id} secret is NOT {key_secret}!",
                                           **kwargs)

    def ntp_verify_auth_key_type(self, device_name, key_id='', key_type='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device to check for the NTP Server.
        [key_id]  -   Public Key index used to generate MD5/SHA1 Digest.
        [key_type]  - Key type: MD5 or SHA1

        Verifies the key type is correct for the public key ID.
        VOSS only.
        """
        args = {"key_id": key_id,
                "key_type": key_type}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_KEY,
                                           self.parse_const.CHECK_NTP_KEY_TYPE, True,
                                           "NTP key ID {key_id} type is {key_type}.",
                                           "NTP key ID {key_id} type is NOT {key_type}!",
                                           **kwargs)

    def ntp_verify_server_reachable(self, device_name, server='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device to check for the NTP Server.
        [server]  -  The IPv4 address of the server.

        Verifies that the NTP server is reachable.
        VOSS only.
        """
        args = {"server": server}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_STATISTICS,
                                           self.parse_const.CHECK_NTP_SERVER_REACHABLE, True,
                                           "NTP server {server} is reachable.",
                                           "NTP server {server} is NOT reachable!",
                                           **kwargs)

    def ntp_verify_server_synced(self, device_name, server='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device to check for the NTP Server.
        [server]  -  The IPv4 address of the server.

        Verifies that the NTP server is synchronized with the device.
        VOSS only.
        """
        args = {"server": server}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_STATISTICS,
                                           self.parse_const.CHECK_NTP_SERVER_SYNCHRONIZED, True,
                                           "NTP server {server} is synchronized.",
                                           "NTP server {server} is NOT synchronized!",
                                           **kwargs)

    def ntp_verify_server_access_failures(self, device_name, server='', failures="0", **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device to check for the NTP Server.
        [server]  -  The IPv4 address of the server.

        Verifies that NTP server access attempts did not have any failures.
        VOSS only.
        """
        args = {"server": server,
                "access_failure": failures}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_STATISTICS,
                                           self.parse_const.CHECK_NTP_SERVER_ACCESS_FAILURE, True,
                                           "NTP server {server} did not have any access failures.",
                                           "NTP server {server} access attempts had failures!",
                                           **kwargs)

    def ntp_verify_server_stratum(self, device_name, server='', server_stratum='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device to check for the NTP Server.
        [server]  -  The IPv4 address of the server.

        Verifies the stratum level of the server.
        VOSS only.
        """
        args = {"server": server,
                "access_failure": "0",
                "server_stratum": server_stratum}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_STATISTICS,
                                           self.parse_const.CHECK_NTP_SERVER_STRATUM, True,
                                           "NTP server {server} stratum level is {server_stratum}.",
                                           "NTP server {server} stratum level is NOT {server_stratum}!",
                                           **kwargs)

    def ntp_verify_server_version(self, device_name, server='', server_version='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device to check for the NTP Server.
        [server]  -  The IPv4 address of the server.

        Verifies the NTP version of the server.
        VOSS only.
        """
        args = {"server": server,
                "access_failure": "0",
                "server_version": server_version}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_NTP_STATISTICS,
                                           self.parse_const.CHECK_NTP_SERVER_VERSION, True,
                                           "NTP server {server} version is {server_version}.",
                                           "NTP server {server} version is NOT {server_version}!",
                                           **kwargs)
