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
        output = output.lower().splitlines()
        port_line = None

        for index, line in enumerate(output):
            if line.find("======") == 0:
                port_line = output[index + 1]
                break

        if port_line is not None:
            tx_state = self.pw.get_value_by_offset(port_line, "", 2)

            if tx_state == "enabled":
                return True, {"ret_tx_state": tx_state}
        return False, None

    def determine_lldp_port_receive_state(self, output, args, **kwargs):
        output = output.lower().splitlines()
        port_line = None

        for index, line in enumerate(output):
            if line.find("======") == 0:
                port_line = output[index + 1]
                break

        if port_line is not None:
            rx_state = self.pw.get_value_by_offset(port_line, "", 1)

            if rx_state == "enabled":
                return True, {"ret_rx_state": rx_state}
        return False, None

    def check_tlv_status(self, output, args, **kwargs):
        output = output.splitlines()
        port_line = None

        for index, line in enumerate(output):
            if line.find("======") == 0:
                port_line = output[index + 1]
                break

        if port_line is not None:
            result = False
            dev_tlv_status = None
            if args["tlv"].lower() == "port-desc":
                dev_tlv_status = self.pw.get_value_by_offset(port_line, "", 4)
                result = True if dev_tlv_status[0] == "P" else False
            elif args["tlv"].lower() == "sys-name":
                dev_tlv_status = self.pw.get_value_by_offset(port_line, "", 4)
                result = True if dev_tlv_status[1] == "N" else False
            elif args["tlv"].lower() == "sys-desc":
                dev_tlv_status = self.pw.get_value_by_offset(port_line, "", 4)
                result = True if dev_tlv_status[2] == "D" else False
            elif args["tlv"].lower() == "sys-cap":
                dev_tlv_status = self.pw.get_value_by_offset(port_line, "", 4)
                result = True if dev_tlv_status[3] == "C" else False
            elif args["tlv"].lower() == "mgmt-addr":
                dev_tlv_status = self.pw.get_value_by_offset(port_line, "", 4)
                result = True if dev_tlv_status[4] == "M" else False
            elif args["tlv"].lower() == "vlan-id":
                dev_tlv_status = self.pw.get_value_by_offset(port_line, "", 5)
                result = True if dev_tlv_status[0] == "P" else False
            elif args["tlv"].lower() == "mac-phy":
                dev_tlv_status = self.pw.get_value_by_offset(port_line, "", 6)
                result = True if dev_tlv_status[0] == "M" else False
            elif args["tlv"].lower() == "poe":
                dev_tlv_status = self.pw.get_value_by_offset(port_line, "", 6)
                result = True if dev_tlv_status[1] == "P" else False
            elif args["tlv"].lower() == "link-aggr":
                dev_tlv_status = self.pw.get_value_by_offset(port_line, "", 6)
                result = True if dev_tlv_status[2] == "L" else False
            elif args["tlv"].lower() == "max-frame":
                dev_tlv_status = self.pw.get_value_by_offset(port_line, "", 6)
                result = True if dev_tlv_status[3] == "F" else False
            elif args["tlv"].lower() == "med-cap":
                dev_tlv_status = self.pw.get_value_by_offset(port_line, "", 7)
                result = True if dev_tlv_status[0] == "C" else False
            elif args["tlv"].lower() == "med-loc":
                dev_tlv_status = self.pw.get_value_by_offset(port_line, "", 7)
                result = True if dev_tlv_status[1] == "L" else False
            elif args["tlv"].lower() == "med-pol":
                dev_tlv_status = self.pw.get_value_by_offset(port_line, "", 7)
                result = True if dev_tlv_status[2] == "P" else False
            elif args["tlv"].lower() == "med-poe":
                dev_tlv_status = self.pw.get_value_by_offset(port_line, "", 7)
                result = True if dev_tlv_status[3] == "p" else False
            elif args["tlv"].lower() == "enhanced-trans-config":
                dev_tlv_status = self.pw.get_value_by_offset(port_line, "", 9)
                result = True if dev_tlv_status[0] == "I" else False
            elif args["tlv"].lower() == "enhanced-trans-rec":
                dev_tlv_status = self.pw.get_value_by_offset(port_line, "", 9)
                result = True if dev_tlv_status[0] == "I" else False
            return result, {"ret_tlv_status": dev_tlv_status}
        else:
            return False, None

    def check_lldp_tx_interval(self, output, args, **kwargs):
        dev_interval = self.pw.get_value_by_offset(output, "LLDP transmit interval", 4)

        result = True if args["interval"] == dev_interval else False
        return result, {"ret_tx_interval": dev_interval}

    def check_lldp_remote_port(self, output, args, **kwargs):
        args["port"] += " "
        output_rem_port = self.pw.get_value_by_offset(output, args["port"], 2)
        # Grabbing first item in the list, if there is a second, it's the prompt.
        output_rem_port = output_rem_port.split(" ")[0]

        result = True if output_rem_port == args["remote_port"] else False
        return result, {"ret_remote_port": output_rem_port}

    def check_lldp_neighbor_sysname(self, output, args, **kwargs):
        args["port"] += " "
        output_rem_sysname = self.pw.get_value_by_offset(output, args["port"], 5)
        output_rem_sysname = output_rem_sysname.split(" ")[0]

        result = True if output_rem_sysname == args["neighbor_sysname"] else False
        return result, {"ret_remote_sysname": output_rem_sysname}
