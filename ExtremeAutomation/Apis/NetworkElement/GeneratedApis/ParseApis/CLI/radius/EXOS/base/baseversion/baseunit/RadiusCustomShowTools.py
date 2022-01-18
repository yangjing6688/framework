from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.radius.base.RadiusBaseCustomShowTools import \
    RadiusBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.ListUtils import ListUtils


class RadiusCustomShowTools(RadiusBaseCustomShowTools):
    def __init__(self, device):
        super(RadiusCustomShowTools, self).__init__(device)

    def check_radius_server_exists(self, output, args, **kwargs):
        addr_list = self.pw.get_value_by_offset(output, args["addr"], 3).split()
        addr_list = ListUtils.convert_to_list(addr_list)
        index_list = self.pw.get_value_by_offset(output, "Status", 0).split()
        index_list = ListUtils.convert_to_list(index_list)

        result = False
        if addr_list[0] != "valueNotPresent":
            for i, address in enumerate(addr_list):
                if args["addr"] == address:
                    result = True if index_list[i].lower() == "radius" else False
                    break
        return result, {"ret_index": str(index_list),
                        "ret_ip": str(addr_list)}

    def check_radius_state(self, output, args, **kwargs):
        state = self.pw.get_value_by_offset(output.lower(), 'radius default state:', 3)

        result = True if state == "enabled" else False
        return result, {"ret_state": state}

    def check_radius_server_status(self, output, args, **kwargs):
        addr_list = self.pw.get_value_by_offset(output, "IP address", 3).split()
        addr_list = ListUtils.convert_to_list(addr_list)
        status_list = self.pw.get_value_by_offset(output, args["index"] + " Status", 6).split()
        status_list = ListUtils.convert_to_list(status_list)

        result = False
        if addr_list[0] != "valueNotPresent":
            for i, address in enumerate(addr_list):
                if args["addr"] == address:
                    result = True if status_list[i].lower() == "active" else False
                    break
        return result, {"ret_status": str(status_list),
                        "ret_index": None,
                        "ret_ip": str(addr_list)}

    def check_radius_server_timeout(self, output, args, **kwargs):
        timeout = self.pw.get_value_by_offset(output.lower(), "timeout:", 3)

        result = True if timeout == args["sec"] else False
        return result, {"ret_timeout": timeout}

    def check_radius_server_retries(self, output, args, **kwargs):
        retries = self.pw.get_value_by_offset(output.lower(), "retries:", 2)

        result = True if retries == args["num"] else False
        return result, {"ret_retries": retries}

    def check_if_radius_timeout_is_set_to_default_setting(self, output, args, **kwargs):
        timeout = self.pw.get_value_by_offset(output.lower(), "timeout:", 3)

        result = True if timeout == "3" else False
        return result, {"ret_timeout": timeout}

    def check_if_radius_retries_is_set_to_default_setting(self, output, args, **kwargs):
        retries = self.pw.get_value_by_offset(output.lower(), "retries:", 2)

        result = True if retries == "3" else False
        return result, {"ret_retries": retries}

    def check_if_radius_algorithm_type_is_standard(self, output, args, **kwargs):
        algorithm_type = self.pw.get_value_by_offset(output.lower(), "algorithm:", 2)

        result = True if algorithm_type == "standard" else False
        return result, {"ret_algorithm_type": algorithm_type}

    def check_if_radius_algorithm_type_is_round_robin(self, output, args, **kwargs):
        algorithm_type = self.pw.get_value_by_offset(output.lower(), "algorithm:", 2)

        result = True if algorithm_type == "round-robin" else False
        return result, {"ret_algorithm_type": algorithm_type}

    def check_radius_accounting_server_exists(self, output, args, **kwargs):
        found_ip = self.pw.get_value_by_offset(output.lower(), 'ip address', 3)
        found_index = self.pw.get_value_by_offset(output.lower(), 'radius acct server', 4)

        result = True if found_ip == args["addr"] and found_index == args["index"] else False
        return result, {"ret_index": found_index,
                        "ret_ip": found_ip}

    def check_radius_accounting_state(self, output, args, **kwargs):
        m_state = self.pw.get_value_by_offset(output.lower(), "switch management radius accounting:", 4)
        n_state = self.pw.get_value_by_offset(output.lower(), "netlogin radius accounting:", 3)

        result = True if m_state and n_state == "enabled" else False
        state = "enabled" if m_state and n_state == "enabled" else "disabled"
        return result, {"ret_state": state}

    def check_radius_mgmt_authentication_state(self, output, args, **kwargs):
        role = self.pw.get_value_by_offset(output.lower(), "switch management radius:", 3)

        result = True if role == "enabled" else False
        return result, {"ret_state": role}

    def check_radius_netlogin_authentication_state(self, output, args, **kwargs):
        role = self.pw.get_value_by_offset(output.lower(), "netlogin radius:", 2)

        result = True if role == "enabled" else False
        return result, {"ret_state": role}
