"""
Keyword class for all ssh cli commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.SshConstants import \
    SshConstants as ParseConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.SshConstants import \
    SshConstants as CommandConstants
# All imports above this line will be removed after generation.
# User imports must be added below.


class NetworkElementSshGenKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementSshGenKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "ssh"

    def ssh_enable(self, device_name, **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE,
                                    **kwargs)

    def ssh_disable(self, device_name, **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE,
                                    **kwargs)

    def ssh_enable_client(self, device_name, **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_CLIENT,
                                    **kwargs)

    def ssh_disable_client(self, device_name, **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_CLIENT,
                                    **kwargs)

    def ssh_set_version(self, device_name, version='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "version": version
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_VERSION,
                                    **kwargs)

    def ssh_set_tcp_port(self, device_name, tcp_port='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: VOSS, SLX
        """
        args = {
            "tcp_port": tcp_port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_TCP_PORT,
                                    **kwargs)

    def ssh_set_client_source_interface(self, device_name, interface='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {
            "interface": interface
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_CLIENT_SOURCE_INTERFACE,
                                    **kwargs)

    def ssh_clear_client_source_interface(self, device_name, interface='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {
            "interface": interface
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_CLIENT_SOURCE_INTERFACE,
                                    **kwargs)

    # ##################################################################################################################
    #   Inspection Keywords   ##########################################################################################
    # ##################################################################################################################

    def ssh_verify_enabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.

        Verifies that ssh access is enabled on the device.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW,
                                           self.parse_const.VERIFY_ENABLED, True,
                                           "SSH Access is enabled.",
                                           "SSH Access is NOT enabled!",
                                           **kwargs)

    def ssh_verify_disabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.

        Verifies that ssh access is disabled on the device.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW,
                                           self.parse_const.VERIFY_DISABLED, True,
                                           "SSH Access is disabled.",
                                           "SSH Access is NOT disabled!",
                                           **kwargs)
