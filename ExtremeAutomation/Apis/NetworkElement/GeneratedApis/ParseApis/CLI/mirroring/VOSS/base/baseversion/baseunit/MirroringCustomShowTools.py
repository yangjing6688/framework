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
        output = output.replace("\n", "\r\n")
        mirror_name_found = self.pw.get_value_at_location(output, column=0, name=None, row=8)
        src_port_found = self.pw.get_value_at_location(output, column=1, name=None, row=8)
        dst_port_found = self.pw.get_value_at_location(output, column=2, name=None, row=8)

        result = (mirror_name_found == args["name"] and
                  src_port_found == args["src_port"] and
                  dst_port_found == args["dst_port"])

        return result, {"ret_name": mirror_name_found,
                        "ret_source_port": src_port_found,
                        "ret_target_port": dst_port_found}

    def check_port_mirror_ingress_exists(self, output, args, **kwargs):
        output = output.replace("\n", "\r\n")
        mirror_name_found = self.pw.get_value_at_location(output, column=0, name=None, row=8)
        src_port_found = self.pw.get_value_at_location(output, column=1, name=None, row=8)
        dst_port_found = self.pw.get_value_at_location(output, column=2, name=None, row=8)
        mirror_mode_found = self.pw.get_value_at_location(output, column=4, name=None, row=8)

        result = (mirror_name_found == args["name"] and
                  src_port_found == args["src_port"] and
                  dst_port_found == args["dst_port"] and
                  mirror_mode_found == "rx")
        return result, {"ret_name": mirror_name_found,
                        "ret_source_port": src_port_found,
                        "ret_target_port": dst_port_found,
                        "ret_mode": mirror_mode_found}

    def check_port_mirror_egress_exists(self, output, args, **kwargs):
        output = output.replace("\n", "\r\n")
        mirror_name_found = self.pw.get_value_at_location(output, column=0, name=None, row=8)
        src_port_found = self.pw.get_value_at_location(output, column=1, name=None, row=8)
        dst_port_found = self.pw.get_value_at_location(output, column=2, name=None, row=8)
        mirror_mode_found = self.pw.get_value_at_location(output, column=4, name=None, row=8)

        result = (mirror_name_found == args["name"] and
                  src_port_found == args["src_port"] and
                  dst_port_found == args["dst_port"] and
                  mirror_mode_found == "tx")
        return result, {"ret_name": mirror_name_found,
                        "ret_source_port": src_port_found,
                        "ret_target_port": dst_port_found,
                        "ret_mode": mirror_mode_found}

    def check_port_mirror_ingress_egress_exists(self, output, args, **kwargs):
        output = output.replace("\n", "\r\n")
        mirror_name_found = self.pw.get_value_at_location(output, column=0, name=None, row=8)
        src_port_found = self.pw.get_value_at_location(output, column=1, name=None, row=8)
        dst_port_found = self.pw.get_value_at_location(output, column=2, name=None, row=8)
        mirror_mode_found = self.pw.get_value_at_location(output, column=4, name=None, row=8)

        result = (mirror_name_found == args["name"] and
                  src_port_found == args["src_port"] and
                  dst_port_found == args["dst_port"] and
                  mirror_mode_found == "both")
        return result, {"ret_name": mirror_name_found,
                        "ret_source_port": src_port_found,
                        "ret_target_port": dst_port_found,
                        "ret_mode": mirror_mode_found}

    def check_port_mirror_enabled(self, output, args, **kwargs):
        output = output.replace("\n", "\r\n")
        mirror_name_found = self.pw.get_value_at_location(output, column=0, name=None, row=8)
        mirror_is_enabled = self.pw.get_value_at_location(output, column=3, name=None, row=8)

        result = mirror_name_found == args["name"] and mirror_is_enabled == "true"
        return result, {"ret_name": mirror_name_found,
                        "ret_status": mirror_is_enabled}
