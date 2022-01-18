
from ExtremeAutomation.Keywords.NetworkElementKeywords.GeneratedKeywords.NetworkElementNtpGenKeywords import NetworkElementNtpGenKeywords
from ExtremeAutomation.Keywords.NetworkElementKeywords.Utils.NetworkElementListUtils import NetworkElementListUtils


class NtpUdks():

    def __init__(self):
        self.networkElementNtpGenKeywords = NetworkElementNtpGenKeywords()
        self.networkElementListUtils = NetworkElementListUtils()

    def Configure_and_Verify_NTP_Server(self, netelem, server, key=None, precedence=None, **kwargs):
        self.networkElementNtpGenKeywords.ntp_create_server_precedence(netelem, server, precedence, **kwargs)
        self.networkElementNtpGenKeywords.ntp_create_server_key(netelem, server, key, **kwargs)
        self.networkElementNtpGenKeywords.ntp_enable_client(netelem, **kwargs)
        self.networkElementNtpGenKeywords.ntp_verify_server_exists(netelem, server, key, precedence, **kwargs)
        self.networkElementNtpGenKeywords.ntp_verify_client_enabled(netelem, **kwargs)

    def Configure_and_Verify_NTP_Server_All_Netelems(self, server, key=None, precedence=None, vlan=all, **kwargs):
        netelem_list = self.networkElementListUtils.create_list_of_network_element_names(**kwargs)
        self.networkElementNtpGenKeywords.ntp_create_server_precedence(netelem_list, server, precedence, **kwargs)
        self.networkElementNtpGenKeywords.ntp_create_server_key(netelem_list, server, key, **kwargs)
        self.networkElementNtpGenKeywords.ntp_enable_client(netelem_list, **kwargs)
        self.networkElementNtpGenKeywords.ntp_verify_server_exists(netelem_list, server, key, precedence, **kwargs)
        self.networkElementNtpGenKeywords.ntp_verify_client_enabled(netelem_list, **kwargs)

    def Delete_and_Verify_NTP_Server(self, netelem, server, **kwargs):
        self.networkElementNtpGenKeywords.ntp_disable_client(netelem, **kwargs)
        self.networkElementNtpGenKeywords.ntp_delete_server(netelem, server, **kwargs)
        self.networkElementNtpGenKeywords.ntp_verify_server_does_not_exist(netelem, server, **kwargs)
        self.networkElementNtpGenKeywords.ntp_verify_client_disabled(netelem, **kwargs)

    def Delete_and_Verify_NTP_Server_All_Netelems(self, server, vlan=all, **kwargs):
        netelem_list = self.networkElementListUtils.create_list_of_network_element_names(**kwargs)
        self.networkElementNtpGenKeywords.ntp_disable_client(netelem_list, **kwargs)
        self.networkElementNtpGenKeywords.ntp_disable_client_vlan(netelem_list, vlan, **kwargs)
        self.networkElementNtpGenKeywords.ntp_delete_server(netelem_list, server, **kwargs)
        self.networkElementNtpGenKeywords.ntp_verify_server_does_not_exist(netelem_list, server, **kwargs)
        self.networkElementNtpGenKeywords.ntp_verify_client_disabled(netelem_list, **kwargs)
