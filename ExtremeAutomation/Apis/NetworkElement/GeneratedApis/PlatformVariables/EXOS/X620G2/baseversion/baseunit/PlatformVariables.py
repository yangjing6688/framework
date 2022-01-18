from ExtremeAutomation.Library.Utils.DotDict import DotDict
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.PlatformVariables.EXOS.baseplatvars.ExosPlatformVariables \
    import ExosPlatformVariables


def create_instance():
    return PlatformVariables()


class PlatformVariables(ExosPlatformVariables):
    def __init__(self):
        super(PlatformVariables, self).__init__()

        if "policy" not in self.vars:
            self.vars["policy"] = DotDict()
        self.vars["policy"]["allowed_types"] = \
            "[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1]"

        # lldp Platform Variables
        if "lldp" not in self.vars:
            self.vars["lldp"] = DotDict()
        self.vars["lldp"]["link_aggr_tlv_message"] = "0x0100000000"
