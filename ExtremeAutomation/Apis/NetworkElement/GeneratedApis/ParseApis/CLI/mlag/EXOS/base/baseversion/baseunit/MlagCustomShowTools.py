from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.mlag.base.MlagBaseCustomShowTools import \
    MlagBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


class MlagCustomShowTools(MlagBaseCustomShowTools):
    def __init__(self, device):
        super(MlagCustomShowTools, self).__init__(device)

    def verify_mlag_peer_exists(self, output, args, **kwargs):
        peer_found = self.pw.get_value_by_offset(output.lower(), ("mlag" + " " + "peer"), 3)

        result = True if peer_found == args["peer"].lower() else False
        return result, {"ret_peer": peer_found}

    def verify_mlag_peer_name(self, output, args, **kwargs):
        peer_name_found = self.pw.get_value_by_offset(output.lower(), ("mlag" + " " + "peer"), 3)

        result = True if peer_name_found == args["peer"].lower() else False
        return result, {"ret_peer_name": peer_name_found}

    def verify_mlag_port_reload_delay_is_set(self, output, args, **kwargs):
        port_found = self.pw.get_value_by_offset(output.lower(), args["port"], 1)
        reload_delay_status = self.pw.get_value_by_offset(output.lower(), ("reload" + " " + "delay"), 3)

        result = True if port_found == args["port"] and reload_delay_status == ": enabled" else False
        return result, {"ret_reload_delay_status": reload_delay_status,
                        "ret_port": port_found}

    def verify_mlag_peer_ipaddress(self, output, args, **kwargs):
        peer_found = self.pw.get_value_by_offset(output.lower(), ("mlag" + " " + "peer"), 3)
        ip_found = self.pw.get_value_by_offset(output.lower(), ("peer" + " " + "ip" + " " + "address"), 9)

        result = True if peer_found == args["peer"].lower() and ip_found == args["ip"] else False
        return result, {"ret_peer_ip": ip_found,
                        "ret_peer": peer_found}

    def check_port_is_in_mlag(self, output, args, **kwargs):
        port_found = self.pw.get_value_by_offset(output.lower(), args["port"], 1)

        result = True if port_found == args["port"] else False
        return result, {"ret_port": port_found}

    def verify_mlag_peer_auth_is_set(self, output, args, **kwargs):
        peer_found = self.pw.get_value_by_offset(output.lower(), ("mlag" + " " + "peer"), 3)
        authentication_status = self.pw.get_value_by_offset(output.lower(), "authentication", 2)

        result = True if peer_found == args["peer"].lower() and authentication_status == "md5" else False
        return result, {"ret_peer_auth_status": authentication_status,
                        "ret_peer": peer_found}

    def verify_mlag_peer_auth_md5_key(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def verify_mlag_port_peer_id(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None
