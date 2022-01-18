"""
This class outlines all the constants for the ntp API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(NtpConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class NtpConstants(ApiConstants):
    def __init__(self):
        super(NtpConstants, self).__init__()
        self.CHECK_NTP_ENABLED = {"constant": "check_ntp_enabled",
                                  "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                  "link": self.link.check_ntp_enabled}
        self.CHECK_NTP_INTERVAL = {"constant": "check_ntp_interval",
                                   "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                   "link": self.link.check_ntp_interval}
        self.CHECK_NTP_KEY_EXISTS = {"constant": "check_ntp_key_exists",
                                     "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                     "link": self.link.check_ntp_key_exists}
        self.CHECK_NTP_KEY_SECRET = {"constant": "check_ntp_key_secret",
                                     "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                     "link": self.link.check_ntp_key_secret}
        self.CHECK_NTP_KEY_TYPE = {"constant": "check_ntp_key_type",
                                   "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                   "link": self.link.check_ntp_key_type}
        self.CHECK_NTP_SERVER_ACCESS_ATTEMPTS = {"constant": "check_ntp_server_access_attempts",
                                                 "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                 "link": self.link.check_ntp_server_access_attempts}
        self.CHECK_NTP_SERVER_ACCESS_FAILURE = {"constant": "check_ntp_server_access_failure",
                                                "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                "link": self.link.check_ntp_server_access_failure}
        self.CHECK_NTP_SERVER_ACCESS_SUCCESS = {"constant": "check_ntp_server_access_success",
                                                "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                "link": self.link.check_ntp_server_access_success}
        self.CHECK_NTP_SERVER_AUTHENTICATION_ENABLED = {"constant": "check_ntp_server_authentication_enabled",
                                                        "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                        "link": self.link.check_ntp_server_authentication_enabled}
        self.CHECK_NTP_SERVER_ENABLED = {"constant": "check_ntp_server_enabled",
                                         "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                         "link": self.link.check_ntp_server_enabled}
        self.CHECK_NTP_SERVER_EXISTS = {"constant": "check_ntp_server_exists",
                                        "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                        "link": self.link.check_ntp_server_exists}
        self.CHECK_NTP_SERVER_KEY_INDEX = {"constant": "check_ntp_server_key_index",
                                           "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                           "link": self.link.check_ntp_server_key_index}
        self.CHECK_NTP_SERVER_KEY_TYPE = {"constant": "check_ntp_server_key_type",
                                          "tags": ["PARSE_CLI"],
                                          "link": self.link.check_ntp_server_key_type}
        self.CHECK_NTP_SERVER_PRECISION = {"constant": "check_ntp_server_precision",
                                           "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                           "link": self.link.check_ntp_server_precision}
        self.CHECK_NTP_SERVER_REACHABLE = {"constant": "check_ntp_server_reachable",
                                           "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                           "link": self.link.check_ntp_server_reachable}
        self.CHECK_NTP_SERVER_ROOT_DELAY = {"constant": "check_ntp_server_root_delay",
                                            "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                            "link": self.link.check_ntp_server_root_delay}
        self.CHECK_NTP_SERVER_SOURCE_IP = {"constant": "check_ntp_server_source_ip",
                                           "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                           "link": self.link.check_ntp_server_source_ip}
        self.CHECK_NTP_SERVER_STRATUM = {"constant": "check_ntp_server_stratum",
                                         "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                         "link": self.link.check_ntp_server_stratum}
        self.CHECK_NTP_SERVER_SYNCHRONIZED = {"constant": "check_ntp_server_synchronized",
                                              "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                              "link": self.link.check_ntp_server_synchronized}
        self.CHECK_NTP_SERVER_VERSION = {"constant": "check_ntp_server_version",
                                         "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                         "link": self.link.check_ntp_server_version}
