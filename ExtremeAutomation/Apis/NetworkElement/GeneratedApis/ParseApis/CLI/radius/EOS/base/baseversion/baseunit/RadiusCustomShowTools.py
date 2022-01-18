from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.radius.base.RadiusBaseCustomShowTools import \
    RadiusBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


class RadiusCustomShowTools(RadiusBaseCustomShowTools):
    def __init__(self, device):
        super(RadiusCustomShowTools, self).__init__(device)

    def check_radius_state(self, output, args, **kwargs):
        state = self.pw.get_value_by_offset(output.lower(), "radius state:", 2)

        result = True if state == "enabled" else False
        return result, {"ret_state": state}

    def check_radius_accounting_state(self, output, args, **kwargs):
        state = self.pw.get_value_by_offset(output.lower(), "radius accounting state:", 3)

        result = True if state == "enabled" else False
        return result, {"ret_accounting_state": state}

    def check_radius_server_exists(self, output, args, **kwargs):
        output = output.replace("\n", "\r\n")
        output = self.pw.normalize_header(output, '-', 8)

        found_index = self.pw.get_value_by_offset(output.lower(), args["addr"], 0)
        found_ip = self.pw.get_value_by_offset(output.lower(), args["addr"], 1)

        result = True if found_index == args["index"] and found_ip == args["addr"] else False
        return result, {"ret_index": found_index,
                        "ret_ip": found_ip}

    def check_radius_server_status(self, output, args, **kwargs):
        output = output.replace("\n", "\r\n")
        output = self.pw.normalize_header(output, '-', 8)

        found_index = self.pw.get_value_by_offset(output.lower(), args["addr"], 0)
        found_ip = self.pw.get_value_by_offset(output.lower(), args["addr"], 1)
        found_state = self.pw.get_value_by_offset(output.lower(), args["addr"], 5)

        result = (found_index == args["index"] and
                  found_ip == args["addr"] and
                  found_state == "active")
        return result, {"ret_status": found_state,
                        "ret_index": found_index,
                        "ret_ip": found_ip}

    def get_radius_server_port(self, output, args, **kwargs):
        output = output.replace("\n", "\r\n")
        output = self.pw.normalize_header(output, '-', 8)
        server_port = self.pw.get_value_by_offset(output.lower(), args["addr"], 2)

        result = True if server_port == args["port"] else False
        return result, {"ret_server_port": server_port}

    def check_radius_accounting_server_exists(self, output, args, **kwargs):
        output = output.replace("\n", "\r\n")
        output = self.pw.normalize_header(output, '-', 8)

        found_index = self.pw.get_value_by_offset(output.lower(), args["addr"], 0)
        found_ip = self.pw.get_value_by_offset(output.lower(), args["addr"], 1)

        result = (found_index == args["index"] and
                  found_ip == args["addr"])
        return result, {"ret_index": found_index,
                        "ret_ip": found_ip}

    def check_if_radius_algorithm_type_is_standard(self, output, args, **kwargs):
        algorithm_type = self.pw.get_value_by_offset(output.lower(), "radius retransmission algorithm:", 3)

        result = True if algorithm_type == "standard" else False
        return result, {"ret_algorithm_type": algorithm_type}

    def check_if_radius_algorithm_type_is_round_robin(self, output, args, **kwargs):
        algorithm_type = self.pw.get_value_by_offset(output.lower(), "radius retransmission algorithm:", 3)

        result = True if algorithm_type == "round-robin" else False
        return result, {"ret_algorithm_type": algorithm_type}

    def check_if_radius_algorithm_type_is_sticky_round_robin(self, output, args, **kwargs):
        algorithm_type = self.pw.get_value_by_offset(output.lower(), "radius retransmission algorithm:", 3)

        result = True if algorithm_type == "sticky-round-robin" else False
        return result, {"ret_algorithm_type": algorithm_type}

    def check_radius_server_timeout(self, output, args, **kwargs):
        timeout = self.pw.get_value_by_offset(output.lower(), "radius timeout:", 2)

        result = True if timeout == args["sec"] else False
        return result, {"ret_timeout": timeout}

    def check_if_radius_timeout_is_set_to_default_setting(self, output, args, **kwargs):
        timeout = self.pw.get_value_by_offset(output.lower(), "radius timeout:", 2)

        result = True if timeout == "20" else False
        return result, {"ret_timeout": timeout}

    def check_radius_server_retries(self, output, args, **kwargs):
        retries = self.pw.get_value_by_offset(output.lower(), "radius retries:", 2)

        result = True if retries == args["num"] else False
        return result, {"ret_retries": retries}

    def check_if_radius_retries_is_set_to_default_setting(self, output, args, **kwargs):
        retries = self.pw.get_value_by_offset(output.lower(), "radius retries:", 2)

        result = True if retries == "3" else False
        return result, {"ret_retries": retries}
