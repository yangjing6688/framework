from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.syslog.base.SyslogBaseCustomShowTools import \
    SyslogBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


class SyslogCustomShowTools(SyslogBaseCustomShowTools):
    def __init__(self, device):
        super(SyslogCustomShowTools, self).__init__(device)

    def verify_login_exists(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None
