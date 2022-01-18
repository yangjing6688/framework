from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.SNMP.ntp.base.NtpBaseCustomShowTools import \
    NtpBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return NtpCustomShowTools(device)


class NtpCustomShowTools(NtpBaseCustomShowTools):
    def __init__(self, device):
        super(NtpCustomShowTools, self).__init__(device)

    def check_ntp_enabled(self, *args):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_ntp_server_exists(self, *args):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None
