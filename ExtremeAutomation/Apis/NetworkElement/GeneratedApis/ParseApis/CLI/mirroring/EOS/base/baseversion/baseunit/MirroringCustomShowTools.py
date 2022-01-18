from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.mirroring.base.MirroringBaseCustomShowTools \
    import MirroringBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return MirroringCustomShowTools(device)


class MirroringCustomShowTools(MirroringBaseCustomShowTools):
    def __init__(self, device):
        super(MirroringCustomShowTools, self).__init__(device)

    def check_port_mirror_exists(self, output, args, **kwargs):
        source_list = self.pw.get_value_by_offset(output, "Source Port", 3).split()
        target_list = self.pw.get_value_by_offset(output, "Target Port", 3).split()

        for i, port in enumerate(source_list):
            if port == args["src_port"]:
                if target_list[i] == args["dst_port"]:
                    return True, True
        return False, None

    def check_port_mirror_enabled(self, output, args, **kwargs):
        source_list = self.pw.get_value_by_offset(output, "Source Port", 3).split()
        target_list = self.pw.get_value_by_offset(output, "Target Port", 3).split()
        status_list = self.pw.get_value_by_offset(output, "Admin Status", 3).split()

        for i, port in enumerate(source_list):
            if port == args["src_port"]:
                if target_list[i] == args["dst_port"]:
                    if status_list[i].lower() == "enabled":
                        return True, {"ret_status": status_list[i]}
        return False, None
