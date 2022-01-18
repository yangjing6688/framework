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
        output_new = output.replace("\r\n", "")
        output_new = output_new.replace(",", "")
        mirror_entry = self.pw.get_value_from_string_to_eol(output_new, args["name"])

        result = True if mirror_entry != "valueNotPresent" else False

        src_result = True
        source_port = None
        if args["src_port"] is not None:
            source_port = self.pw.get_value_by_offset(mirror_entry, "Description", 11)
            src_result = True if str(source_port) == str(args["src_port"]) else False

        dst_result = True
        target_port = None
        if args["dst_port"] is not None:
            target_port = self.pw.get_value_by_offset(mirror_entry, "Description", 5)
            dst_result = True if str(target_port) == str(args["dst_port"]) else False

        return result and src_result and dst_result, {"ret_source_port": source_port,
                                                      "ret_target_port": target_port}

    def check_port_mirror_enabled(self, output, args, **kwargs):
        status = self.pw.get_value_by_offset(output, args["name"], 1)

        result = True if status.lower() == "(enabled)" else False
        return result, {"ret_status": status}
