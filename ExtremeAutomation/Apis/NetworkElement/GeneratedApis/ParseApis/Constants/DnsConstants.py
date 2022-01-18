"""
This class outlines all the constants for the dns API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(DnsConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class DnsConstants(ApiConstants):
    def __init__(self):
        super(DnsConstants, self).__init__()
        self.CHECK_DNS_IP_DOMAIN_NAME = {"constant": "check_dns_ip_domain_name",
                                         "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                         "link": self.link.check_dns_ip_domain_name}
        self.CHECK_DNS_SERVER_IP = {"constant": "check_dns_server_ip",
                                    "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                    "link": self.link.check_dns_server_ip}
        self.CHECK_DNS_SERVER_SENT_REQUESTS = {"constant": "check_dns_server_sent_requests",
                                               "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                               "link": self.link.check_dns_server_sent_requests}
        self.CHECK_DNS_SERVER_STATUS = {"constant": "check_dns_server_status",
                                        "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                        "link": self.link.check_dns_server_status}
        self.CHECK_DNS_SERVER_SUCCESSFUL_REQUESTS = {"constant": "check_dns_server_successful_requests",
                                                     "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                     "link": self.link.check_dns_server_successful_requests}
        self.CHECK_HOST_IP = {"constant": "check_host_ip",
                              "tags": ["PARSE_CLI", "PARSE_SNMP"],
                              "link": self.link.check_host_ip}
        self.CHECK_HOST_NAME = {"constant": "check_host_name",
                                "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                "link": self.link.check_host_name}
