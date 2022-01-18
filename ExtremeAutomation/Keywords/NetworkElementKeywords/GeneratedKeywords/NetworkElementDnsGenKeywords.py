"""
Keyword class for all dns cli commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.DnsConstants import \
    DnsConstants as ParseConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.DnsConstants import \
    DnsConstants as CommandConstants
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Keywords.NetworkElementKeywords.Utils.NetworkElementSnmpUtils import \
    NetworkElementSnmpUtils as SnmpUtils
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


class NetworkElementDnsGenKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementDnsGenKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "dns"

    def dns_create_domain_name(self, device_name, domain_name='', **kwargs):
        """
        Description: Creates the default domain used for querying the DNS Server.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "domain_name": domain_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_DOMAIN_NAME,
                                    **kwargs)

    def dns_delete_domain_name(self, device_name, **kwargs):
        """
        Description: Deletes the default domain used for querying the DNS Server by setting it to a zero-length string.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DELETE_DOMAIN_NAME,
                                    **kwargs)

    def dns_set_primary_server_ip(self, device_name, ip_addr='', ip_type='', **kwargs):
        """
        Description: Configures the primary DNS Server.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "ip_addr": ip_addr,
            "ip_type": ip_type
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PRIMARY_SERVER_IP,
                                    **kwargs)

    def dns_set_secondary_server_ip(self, device_name, ip_addr='', ip_type='', **kwargs):
        """
        Description: Configures the secondary DNS Server.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "ip_addr": ip_addr,
            "ip_type": ip_type
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_SECONDARY_SERVER_IP,
                                    **kwargs)

    def dns_set_tertiary_server_ip(self, device_name, ip_addr='', ip_type='', **kwargs):
        """
        Description: Configures the tertiary DNS Server.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "ip_addr": ip_addr,
            "ip_type": ip_type
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_TERTIARY_SERVER_IP,
                                    **kwargs)

    def dns_clear_primary_server_ip(self, device_name, **kwargs):
        """
        Description: Clears the primary DNS Server.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_PRIMARY_SERVER_IP,
                                    **kwargs)

    def dns_clear_secondary_server_ip(self, device_name, **kwargs):
        """
        Description: Clears the secondary DNS Server.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_SECONDARY_SERVER_IP,
                                    **kwargs)

    def dns_clear_tertiary_server_ip(self, device_name, **kwargs):
        """
        Description: Clears the tertiary DNS Server.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_TERTIARY_SERVER_IP,
                                    **kwargs)

    # ##################################################################################################################
    #   Inspection Keywords   ##########################################################################################
    # ##################################################################################################################

    def dns_verify_domain_name(self, device_name, domain_name='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.
        [domain_name] - The default domain used for querying the DNS Server.

        Verifies the default domain used for querying the DNS Server.
        Applies to VOSS only.
        """
        args = {"domain_name": domain_name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_DOMAIN_NAME,
                                           self.parse_const.CHECK_DNS_IP_DOMAIN_NAME, True,
                                           "DNS IP default domain name is {domain_name}.",
                                           "DNS IP default domain name is NOT {domain_name}!",
                                           **kwargs)

    def dns_verify_domain_name_does_not_exist(self, device_name, domain_name='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.
        [domain_name] - The default domain used for querying the DNS Server.

        Verifies the default configured domain used for querying the DNS Server does not exist.
        Applies to VOSS only.
        """
        args = {"domain_name": domain_name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_DOMAIN_NAME,
                                           self.parse_const.CHECK_DNS_IP_DOMAIN_NAME, False,
                                           "DNS IP default domain name is not {domain_name}.",
                                           "DNS IP default domain name IS {domain_name}!",
                                           **kwargs)

    def dns_verify_server_ip(self, device_name, ip_addr='', pri_sec_or_ter="primary", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will run against.
        [ip_addr]         - The ip address of the DNS Server.
        [pri_sec_or_ter]  - The designated order of the server.
                            Values: primary,  secondary, tertiary.

        Verifies the primary, secondary, or tertiary DNS server IP address.
        """
        args = {"ip_addr": ip_addr,
                "pri_sec_or_ter": pri_sec_or_ter,
                "index": SnmpUtils().voss_dns_server_order(pri_sec_or_ter)}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SERVERS,
                                           self.parse_const.CHECK_DNS_SERVER_IP, True,
                                           "DNS {pri_sec_or_ter} server IP is {ip_addr}.",
                                           "DNS {pri_sec_or_ter} server IP is NOT {ip_addr}!",
                                           **kwargs)

    def dns_verify_server_status_active(self, device_name, pri_sec_or_ter="primary", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will run against.
        [pri_sec_or_ter]  - The designated order of the server.
                            Values: primary,  secondary, tertiary.

        Verifies the primary, secondary, or tertiary DNS server is active.
        """
        args = {"pri_sec_or_ter": pri_sec_or_ter,
                "index": SnmpUtils().voss_dns_server_order(pri_sec_or_ter)}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SERVERS,
                                           self.parse_const.CHECK_DNS_SERVER_STATUS, True,
                                           "DNS {pri_sec_or_ter} server status is active.",
                                           "DNS {pri_sec_or_ter} server status is NOT active!",
                                           **kwargs)

    def dns_verify_server_status_inactive(self, device_name, pri_sec_or_ter="primary", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will run against.
        [pri_sec_or_ter]  - The designated order of the server.
                            Values: primary,  secondary, tertiary.

        Verifies the primary, secondary, or tertiary DNS server is inactive.
        """
        args = {"pri_sec_or_ter": pri_sec_or_ter,
                "index": SnmpUtils().voss_dns_server_order(pri_sec_or_ter)}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SERVERS,
                                           self.parse_const.CHECK_DNS_SERVER_STATUS, False,
                                           "DNS {pri_sec_or_ter} server status is active.",
                                           "DNS {pri_sec_or_ter} server status is NOT active!",
                                           **kwargs)

    def dns_verify_server_sent_requests(self, device_name, count='', count_operator="=", pri_sec_or_ter="primary",
                                        **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will run against.
        [ip_addr]         - The ip address of the DNS Server.
        [count]           - The expected number of sent requests.
        [count_operator]  - The operator that qualifies the count.  Values are =, > or <.
        [pri_sec_or_ter]  - The designated order of the server.
                            Values: primary,  secondary, tertiary.

        Verifies the number of DNS requests sent by the primary, secondary, or tertiary DNS server.
        """
        args = {"count": count,
                "count_operator": count_operator,
                "pri_sec_or_ter": pri_sec_or_ter,
                "index": SnmpUtils().voss_dns_server_order(pri_sec_or_ter)}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SERVERS,
                                           self.parse_const.CHECK_DNS_SERVER_SENT_REQUESTS, True,
                                           "DNS {pri_sec_or_ter} server requests is {count_operator} {count}.",
                                           "DNS {pri_sec_or_ter} server requests is NOT {count_operator} "
                                           "{count}!", **kwargs)

    def dns_verify_server_successful_requests(self, device_name, count='', count_operator="=", pri_sec_or_ter="primary",
                                              **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will run against.
        [ip_addr]         - The ip address of the DNS Server.
        [count]           - The expected number of sent requests.
        [count_operator]  - The operator that qualifies the count.  Values are =, > or <.
        [pri_sec_or_ter]  - The designated order of the server.
                            Values: primary,  secondary, tertiary.

        Verifies the number of successful sent DNS requests on the primary, secondary, or tertiary DNS server.
        """
        args = {"count": count,
                "count_operator": count_operator,
                "pri_sec_or_ter": pri_sec_or_ter,
                "index": SnmpUtils().voss_dns_server_order(pri_sec_or_ter)}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SERVERS,
                                           self.parse_const.CHECK_DNS_SERVER_SUCCESSFUL_REQUESTS, True,
                                           "DNS {pri_sec_or_ter} successful requests is {count_operator} "
                                           "{count}.",
                                           "DNS {pri_sec_or_ter} successful requests is NOT {count_operator} "
                                           "{count}!", **kwargs)

    def dns_verify_server_does_not_exist(self, device_name, ip_addr='', pri_sec_or_ter="primary", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will run against.
        [ip_addr]         - The ip address of the DNS Server.
        [pri_sec_or_ter]  - The designated order of the server.
                            Values: primary,  secondary, tertiary.

        Verifies the primary, secondary, or tertiary DNS server does not exist by IP address.
        """
        args = {"ip_addr": ip_addr,
                "pri_sec_or_ter": pri_sec_or_ter,
                "index": SnmpUtils().voss_dns_server_order(pri_sec_or_ter)}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SERVERS,
                                           self.parse_const.CHECK_DNS_SERVER_IP, False,
                                           "DNS {pri_sec_or_ter} server does not exist.",
                                           "DNS {pri_sec_or_ter} server exists!",
                                           **kwargs)

    def dns_verify_remote_host_ip(self, device_name, host_ip='', host_name='', **kwargs):
        """
        Keyword Arguments:
        [device_name]   - The device the keyword will run against.
        [host_ip]       - The IP address of the remote host.
        [host_name]     - The fully qualified DNS name of the remote host.

        Verifies the IP address of the queried remote host.
        """
        args = {"host_ip": host_ip,
                "host_name": host_name,
                "oid_index": StringUtils.ascii_to_dec_with_len(host_name)}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_HOST_BY_NAME,
                                           self.parse_const.CHECK_HOST_IP, True,
                                           "Remote host {host_data} IP is {host_ip}.",
                                           "Remote host {host_data} IP is NOT {host_ip}!",
                                           **kwargs)

    def dns_verify_remote_host_name(self, device_name, host_ip='', host_name='', **kwargs):
        """
        Keyword Arguments:
        [device_name]   - The device the keyword will run against.
        [host_ip]       - The IP address of the remote host.
        [host_name]     - The fully qualified DNS name of the remote host.

        Verifies the fully qualified DNS name of the queried remote host.
        """
        args = {"host_ip": host_ip,
                "host_name": host_name,
                "oid_index": StringUtils.ascii_to_dec_with_len(host_ip)}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_HOST_BY_IP,
                                           self.parse_const.CHECK_HOST_NAME, True,
                                           "Remote host {host_data} name is {host_name}.",
                                           "Remote host {host_data} name is NOT {host_name}!",
                                           **kwargs)
