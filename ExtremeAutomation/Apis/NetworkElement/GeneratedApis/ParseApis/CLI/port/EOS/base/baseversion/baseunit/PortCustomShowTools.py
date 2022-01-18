from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.port.base.PortBaseCustomShowTools import \
    PortBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


def create_instance(device):
    return PortCustomShowTools(device)


class PortCustomShowTools(PortBaseCustomShowTools):
    def __init__(self, device):
        super(PortCustomShowTools, self).__init__(device)

    def validate_jumbo_frame_reception(self, output, args, **kwargs):
        oper_status = self.pw.get_value_by_offset(output, "Enabled", 1)
        admin_status = self.pw.get_value_by_offset(output, "Enabled", 2)
        ret_dict = {"ret_oper": oper_status,
                    "ret_admin": admin_status}
        result = True if oper_status == "Enabled" and admin_status == "Enabled" else False
        return result, ret_dict

    def verify_port_enabled(self, output, args, **kwargs):
        """
        The following function returns True if the provided port is admin enabled.
        """
        output = StringUtils.format_json_output(output)

        if isinstance(output, dict):
            admin_state = output["result"][1]["show_ports_info_detail"]["adminState"]

            if admin_state == 1:
                admin_state = "up"
            else:
                admin_state = "down"
        else:
            if self.pw.get_value_by_offset(output, args["port"], 1) == "up" or "down":
                admin_state = self.pw.get_value_by_offset(output, args["port"], 2)
            else:
                admin_state = self.pw.get_value_by_offset(output, args["port"], 3)

        return admin_state.lower() == "up", {"ret_state": admin_state}

    def verify_port_operational(self, output, args, **kwargs):
        """
        The following function returns True if the provided port is admin enabled.
        """
        if self.pw.get_value_by_offset(output, args["port"], 1) == "up" or "down":
            admin_state = self.pw.get_value_by_offset(output, args["port"], 1)
        else:
            admin_state = self.pw.get_value_by_offset(output, args["port"], 2)

        return admin_state.lower() == "up", {"ret_state": admin_state}

    def verify_port_alias(self, output, args, **kwargs):
        """
        The following function returns True if the output alias is set to the provided alias
        """
        output = StringUtils.format_json_output(output)

        if isinstance(output, dict):
            output_alias = output["result"][1]["show_ports_info_detail"]["descriptionString"]
        else:
            output_alias = self.pw.get_value_by_offset(output, "Description String:", 2)
            output_alias = output_alias.replace('"', "")

        return output_alias == args["alias"], {"ret_alias": output_alias}

    def check_port_pvid(self, output, args, **kwargs):
        dev_pvid = self.pw.get_value_by_offset(output, "is set", 4)

        result = True if args["pvid"] == dev_pvid else False
        return result, {"ret_dev_pvid": dev_pvid}

    def verify_port_mtu(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def verify_port_mac_address(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def verify_port_high_speed(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_port_in_octets(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_port_in_unicast_packets(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_port_in_discard_packets(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_port_in_error_packets(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_port_in_unknown_protocol_packets(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_port_out_octets(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_port_out_unicast_packets(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_port_out_discard_packets(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_port_out_error_packets(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_port_in_multicast_packets(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_port_in_broadcast_packets(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_port_out_multicast_packets(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_port_out_broadcast_packets(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_port_64_bit_in_octets(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_port_64_bit_in_unicast_packets(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_port_64_bit_in_multicast_packets(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_port_64_bit_in_broadcast_packets(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_port_64_bit_out_octets(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_port_64_bit_out_unicast_packets(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_port_64_bit_out_multicast_packets(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_port_64_bit_out_broadcast_packets(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None
