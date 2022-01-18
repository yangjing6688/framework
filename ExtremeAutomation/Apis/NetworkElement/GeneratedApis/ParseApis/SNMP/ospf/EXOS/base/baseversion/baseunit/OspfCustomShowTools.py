from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.SNMP.ospf.base.OspfBaseCustomShowTools import \
    OspfBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return OspfCustomShowTools(device)


class OspfCustomShowTools(OspfBaseCustomShowTools):
    def __init__(self, device):
        super(OspfCustomShowTools, self).__init__(device)

    def verify_ospf_globally_enabled(self, *args):
        return self.constants.METHOD_NOT_SUPPORTED, None

    def verify_ospf_globally_disabled(self, *args):
        return self.constants.METHOD_NOT_SUPPORTED, None

    def verify_ospf_router_id(self, *args):
        return self.constants.METHOD_NOT_SUPPORTED, None

    def verify_ospf_router_id_is_removed(self, *args):
        return self.constants.METHOD_NOT_SUPPORTED, None
