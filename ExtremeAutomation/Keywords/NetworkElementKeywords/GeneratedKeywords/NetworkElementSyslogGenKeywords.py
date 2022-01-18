"""
Keyword class for all syslog cli commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.SyslogConstants import \
    SyslogConstants as ParseConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.SyslogConstants import \
    SyslogConstants as CommandConstants
# All imports above this line will be removed after generation.
# User imports must be added below.


class NetworkElementSyslogGenKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementSyslogGenKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "syslog"

    # ##################################################################################################################
    #   Inspection Keywords   ##########################################################################################
    # ##################################################################################################################

    def syslog_verify_server_exists(self, device_name, ip='', port="514", server_facility='', vr='', **kwargs):
        """
        Keyword Arguments:
        [ip]              - The IP address of the syslog server.
        [port]            - The UDP port for the syslog server.
        [server_facility] - The remote server facility.
        [vr]              - The VR the syslog server was applied to.

        Verifies that a specific syslog server was added to the configuration.
        """
        args = {"ip": ip,
                "port": port,
                "server_facility": server_facility,
                "vr": vr}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_TARGET_INFO,
                                           self.parse_const.CHECK_SYSLOG_SERVER, True,
                                           "Syslog server {ip}:{port} exists on {device_name}.",
                                           "Syslog server {ip}:{port} DOES NOT exist on {device_name}!",
                                           **kwargs)

    def syslog_verify_server_does_not_exist(self, device_name, ip='', port="514", server_facility='', vr='', **kwargs):
        """
        Keyword Arguments:
        [ip]              - The IP address of the syslog server.
        [port]            - The UDP port for the syslog server.
        [server_facility] - The remote server facility.
        [vr]              - The VR the syslog server was applied to.

        Verifies that a specific syslog server does not exist in the configuration.
        """
        args = {"ip": ip,
                "port": port,
                "server_facility": server_facility,
                "vr": vr}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_TARGET_INFO,
                                           self.parse_const.CHECK_SYSLOG_SERVER, True,
                                           "Syslog server {ip}:{port} does not exist on {device_name}.",
                                           "Syslog server {ip}:{port} DOES exist on {device_name}!",
                                           **kwargs)
