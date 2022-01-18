from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.SNMP.spanningtree.base.\
    SpanningtreeBaseCustomShowTools import SpanningtreeBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return SpanningtreeCustomShowTools(device)


class SpanningtreeCustomShowTools(SpanningtreeBaseCustomShowTools):
    def __init__(self, device):
        super(SpanningtreeCustomShowTools, self).__init__(device)

    def check_mstp_enabled_on_interface(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.45.5.5.1.3.1.13." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == "1" else False
        return result, {"ret_state": parse_result}
