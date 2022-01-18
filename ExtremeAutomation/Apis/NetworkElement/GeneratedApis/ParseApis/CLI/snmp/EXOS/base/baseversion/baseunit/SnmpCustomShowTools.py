from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.snmp.base.SnmpBaseCustomShowTools import \
    SnmpBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return SnmpCustomShowTools(device)


class SnmpCustomShowTools(SnmpBaseCustomShowTools):
    def __init__(self, device):
        super(SnmpCustomShowTools, self).__init__(device)

    def verify_snmp_enabled(self, output, args, **kwargs):
        """
        The following function returns True if snmp is set to enabled.
        """
        snmp_output = self.pw.get_value_by_offset(output, "SNMP access", 3)

        result = True if snmp_output.lower() == "enabled" else False

        return result, {"ret_snmp": snmp_output}
