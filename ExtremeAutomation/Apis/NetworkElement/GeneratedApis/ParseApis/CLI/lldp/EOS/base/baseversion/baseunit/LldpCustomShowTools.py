from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.lldp.base.LldpBaseCustomShowTools import \
    LldpBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return LldpCustomShowTools(device)


class LldpCustomShowTools(LldpBaseCustomShowTools):
    def __init__(self, device):
        super(LldpCustomShowTools, self).__init__(device)

    def determine_lldp_port_transmit_state(self, output, args, **kwargs):
        parsed_output = self.pw.get_value_by_offset(output, "Tx-Enabled Ports           : ", 3)

        result = self.it.compare_port_values(parsed_output, args["port"], self.inspect_constants.FOUNDIN)
        return result, {"ret_tx_enabled_ports": parsed_output,
                        "ret_tx_state": "enabled" if result else "disabled"}

    def determine_lldp_port_receive_state(self, output, args, **kwargs):
        parsed_output = self.pw.get_value_by_offset(output, "Rx-Enabled Ports           : ", 3)

        result = self.it.compare_port_values(parsed_output, args["port"], self.inspect_constants.FOUNDIN)
        return result, {"ret_rx_enabled_ports": parsed_output,
                        "ret_rx_state": "enabled" if result else "disabled"}

    def check_tlv_status(self, output, args, **kwargs):
        dev_tlv_status = None

        if args["tlv"].lower() == "port-desc":
            dev_tlv_status = self.pw.get_value_by_offset(output, args["port"], 1)
        elif args["tlv"].lower() == "sys-name":
            dev_tlv_status = self.pw.get_value_by_offset(output, args["port"], 2)
        elif args["tlv"].lower() == "sys-desc":
            dev_tlv_status = self.pw.get_value_by_offset(output, args["port"], 3)
        elif args["tlv"].lower() == "sys-cap":
            dev_tlv_status = self.pw.get_value_by_offset(output, args["port"], 4)
        elif args["tlv"].lower() == "mgmt-addr":
            dev_tlv_status = self.pw.get_value_by_offset(output, args["port"], 5)
        elif args["tlv"].lower() == "vlan-id":
            dev_tlv_status = self.pw.get_value_by_offset(output, args["port"], 6)
        elif args["tlv"].lower() == "stp":
            dev_tlv_status = self.pw.get_value_by_offset(output, args["port"], 7)
        elif args["tlv"].lower() == "lacp":
            dev_tlv_status = self.pw.get_value_by_offset(output, args["port"], 7)
        elif args["tlv"].lower() == "gvrp":
            dev_tlv_status = self.pw.get_value_by_offset(output, args["port"], 7)
        elif args["tlv"].lower() == "mac-phy":
            dev_tlv_status = self.pw.get_value_by_offset(output, args["port"], 8)
        elif args["tlv"].lower() == "poe":
            dev_tlv_status = self.pw.get_value_by_offset(output, args["port"], 9)
        elif args["tlv"].lower() == "link-aggr":
            dev_tlv_status = self.pw.get_value_by_offset(output, args["port"], 10)
        elif args["tlv"].lower() == "max-frame":
            dev_tlv_status = self.pw.get_value_by_offset(output, args["port"], 11)
        elif args["tlv"].lower() == "med-cap":
            dev_tlv_status = self.pw.get_value_by_offset(output, args["port"], 12)
        elif args["tlv"].lower() == "med-pol":
            dev_tlv_status = self.pw.get_value_by_offset(output, args["port"], 13)
        elif args["tlv"].lower() == "med-loc":
            dev_tlv_status = self.pw.get_value_by_offset(output, args["port"], 14)
        elif args["tlv"].lower() == "med-poe":
            dev_tlv_status = self.pw.get_value_by_offset(output, args["port"], 15)
        elif args["tlv"].lower() == "energy-eff-eth":
            dev_tlv_status = self.pw.get_value_by_offset(output, args["port"], 17)
        elif args["tlv"].lower() == "enhanced-trans-config":
            dev_tlv_status = self.pw.get_value_by_offset(output, args["port"], 1)
        elif args["tlv"].lower() == "enhanced-trans-rec":
            dev_tlv_status = self.pw.get_value_by_offset(output, args["port"], 2)
        elif args["tlv"].lower() == "priority-flowctrl":
            dev_tlv_status = self.pw.get_value_by_offset(output, args["port"], 3)
        elif args["tlv"].lower() == "application-pri":
            dev_tlv_status = self.pw.get_value_by_offset(output, args["port"], 4)
        elif args["tlv"].lower() == "congestion-notif":
            dev_tlv_status = self.pw.get_value_by_offset(output, args["port"], 5)

        result = True if dev_tlv_status == "*" else False
        return result, {"ret_tlv_status": dev_tlv_status}

    def check_lldp_tx_interval(self, output, args, **kwargs):
        dev_interval = self.pw.get_value_by_offset(output, "Message Tx Interval", 4)

        result = True if args["interval"] == dev_interval else False
        return result, {"ret_tx_interval": dev_interval}

    def check_lldp_remote_port(self, output, args, **kwargs):
        output_rem_port = self.pw.get_value_by_offset(output, args["port"], 8)

        result = True if output_rem_port == args["remote_port"] else False
        return result, {"ret_remote_port": output_rem_port}
