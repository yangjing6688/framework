from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.hostmonitor.base.HostmonitorBaseCustomShowTools \
    import HostmonitorBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


class HostmonitorCustomShowTools(HostmonitorBaseCustomShowTools):
    def __init__(self, device):
        super(HostmonitorCustomShowTools, self).__init__(device)

    def check_slot_operational(self, output, args, **kwargs):
        slot_state = self.pw.get_value_by_offset(output, "Slot-" + args["slot"] + " ", 3).split(" ")[0]

        result = True if slot_state == "Operational" else False
        return result, {"ret_slot_state": slot_state}
