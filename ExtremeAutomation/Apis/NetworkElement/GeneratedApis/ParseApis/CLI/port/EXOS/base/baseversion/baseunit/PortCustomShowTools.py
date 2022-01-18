from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.port.base.PortBaseCustomShowTools import \
    PortBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return PortCustomShowTools(device)


class PortCustomShowTools(PortBaseCustomShowTools):
    def __init__(self, device):
        super(PortCustomShowTools, self).__init__(device)

    def validate_jumbo_frame_reception(self, output, args, **kwargs):
        returned_jumbo_frame = self.pw.get_value_by_index(output, 22)
        for char in returned_jumbo_frame:
            if char == 'j':
                return True, True
        return False, False

    def verify_port_enabled(self, output, args, **kwargs):
        """
        The following function returns True if the port is admin enabled.
        """
        admin_state = self.pw.get_value_by_offset(output, "Admin state:", 2)
        result = admin_state.lower() == "enabled"

        return result, {"ret_state": admin_state}

    def verify_port_operational(self, output, args, **kwargs):
        """
        The following function returns True if the port link state is active.
        """
        link_state = self.pw.get_value_by_offset(output, "Link State:", 2)
        link_state = link_state.split()

        if len(link_state) > 1:
            admin_state = link_state[1]
        else:
            admin_state = link_state[0]

        result = admin_state.strip(",").lower() == "active"

        return result, {"ret_state": admin_state}

    def verify_port_alias(self, output, args, **kwargs):
        """
        The following function returns True if the output alias is set to the provided alias
        """
        # THIS WILL NOT WORK IF DESCRIPTION CONTAINS SPACES, AS get_value_by_offset SPLITS ON SPACES.
        output_aliases = self.pw.get_value_by_offset(output, "Description String:", 2)
        # output_alias = output_alias.replace('"', "")
        output_aliases = output_aliases.split("\"")
        for output_alias in output_aliases:
            # if output_alias[0].isalnum():
            if output_alias.isalnum():
                if not output_alias.lower() == args["alias"]:
                    return False, output_alias
        return True, output_aliases

    def verify_port_rate_egress(self, output, args, **kwargs):
        """
        The following function returns True if the provided port has the provided rate-limit.
        """
        port_rates = self.pw.get_value_by_offset(output, "Egress Port Rate:", 3).split(" ")

        for port_rate in port_rates:
            if port_rate != args["rate"]:
                return False, False
        return True, True

    def verify_port_rate_broadcast(self, output, args, **kwargs):
        """
        The following function returns True if the provided port has the provided rate-limit.
        """
        port_rates = self.pw.get_value_by_offset(output, "Broadcast Rate:", 2).split(" ")

        for port_rate in port_rates:
            if port_rate != args["rate"]:
                return False, False
        return True, True

    def verify_port_rate_multicast(self, output, args, **kwargs):
        """
        The following function returns True if the provided port has the provided rate-limit.
        """
        port_rates = self.pw.get_value_by_offset(output, "Multicast Rate:", 2).split(" ")

        for port_rate in port_rates:
            if port_rate != args["rate"]:
                return False, False
        return True, True

    def verify_port_rate_unknown_destmac(self, output, args, **kwargs):
        """
        The following function returns True if the provided port has the provided rate-limit.
        """
        port_rates = self.pw.get_value_by_offset(output, "Unknown Dest Mac Rate:", 4).split(" ")

        for port_rate in port_rates:
            if port_rate != args["rate"]:
                return False, False
        return True, True

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

    def verify_port_advertised_speed_duplex(self, output, args, **kwargs):
        flag_list = list(args["flags"])
        if args["speed"].lower() == "100baset":
            if args["duplex"].lower() == "half":
                found_flags = self.pw.get_value_by_offset(output, args["port"] + "  ", 3)
            else:
                found_flags = self.pw.get_value_by_offset(output, args["port"] + "  ", 4)
        elif args["speed"].lower() == "100x":
            if args["duplex"].lower() == "half":
                found_flags = self.pw.get_value_by_offset(output, args["port"] + "  ", 5)
            else:
                found_flags = self.pw.get_value_by_offset(output, args["port"] + "  ", 6)
        elif args["speed"].lower() == "1000baset":
            if args["duplex"].lower() == "half":
                found_flags = self.pw.get_value_by_offset(output, args["port"] + "  ", 7)
            else:
                found_flags = self.pw.get_value_by_offset(output, args["port"] + "  ", 8)
        elif args["speed"].lower() == "1000x":
            if args["duplex"].lower() == "half":
                found_flags = self.pw.get_value_by_offset(output, args["port"] + "  ", 9)
            else:
                found_flags = self.pw.get_value_by_offset(output, args["port"] + "  ", 10)
        else:
            if args["duplex"].lower() == "half":
                found_flags = self.pw.get_value_by_offset(output, args["port"] + "  ", 1)
            else:
                found_flags = self.pw.get_value_by_offset(output, args["port"] + "  ", 2)
        for flag in flag_list:
            if flag not in found_flags:
                return False, {"ret_foundflags": found_flags}
        return True, {"ret_foundflags": found_flags}
