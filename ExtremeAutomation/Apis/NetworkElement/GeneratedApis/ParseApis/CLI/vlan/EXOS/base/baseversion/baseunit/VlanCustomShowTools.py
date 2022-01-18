from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.vlan.base.VlanBaseCustomShowTools import \
    VlanBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils
import re


def create_instance(device):
    return VlanCustomShowTools(device)


class VlanCustomShowTools(VlanBaseCustomShowTools):
    def __init__(self, device):
        super(VlanCustomShowTools, self).__init__(device)

    def check_vlan_exists(self, output, args, **kwargs):
        vlan_index = " " + args["vlan"] + " "
        vid_from_output = re.findall("(" + vlan_index + r")[^\/]", output)
        result = False
        if len(vid_from_output) == 1:
            vid_from_output = vid_from_output[0].replace(" ", "")
            self.logger.log_info(str(vid_from_output))
            result = vid_from_output == args["vlan"]

        return result, {"ret_vlans": str(vid_from_output)}

    def check_untagged_ports(self, output, args, **kwargs):
        output = output.replace(",\r\n", ",")
        output = output.replace(" ", "")
        output = output.replace("Untag:", "Untag: ")

        untagged_ports = self.pw.get_value_by_offset(output, "Untag:", 1)
        untagged_ports = StringUtils.normalize_exos_ports(untagged_ports)

        result = self.it.compare_port_values(untagged_ports, args["port"], self.inspect_constants.FOUNDIN)

        return result, {"ret_port": ', '.join(untagged_ports)}

    def check_untagged_operational_ports(self, output, args, **kwargs):
        operational_ports_string = "Number of active ports=" + str(len(args["port"]))
        operational_result = operational_ports_string in output
        output = output.replace(",\r\n", ",")
        output = output.replace(" ", "")
        output = output.replace("Untag:", "Untag: ")

        untagged_ports = self.pw.get_value_by_offset(output, "Untag:", 1)
        untagged_ports = StringUtils.normalize_exos_ports(untagged_ports)

        result = self.it.compare_port_values(untagged_ports, args["port"], self.inspect_constants.FOUNDIN)

        result1 = result and operational_result

        return result1, {"ret_port": ', '.join(untagged_ports)}

    def check_static_untagged_ports(self, output, args, **kwargs):
        output = output.replace(",\r\n", ",")
        output = output.replace(" ", "")
        output = output.replace("Untag:", "Untag: ")

        untagged_ports = self.pw.get_value_by_offset(output, "Untag:", 1)
        untagged_ports = StringUtils.normalize_exos_ports(untagged_ports)

        result = self.it.compare_port_values(untagged_ports, args["port"], self.inspect_constants.FOUNDIN)

        return result, {"ret_port": ', '.join(untagged_ports)}

    def check_tagged_ports(self, output, args, **kwargs):
        output = output.replace(",\r\n", ",")
        output = output.replace(" ", "")
        output = output.replace("Tag:", "Tag: ")
        tagged_ports = self.pw.get_value_by_offset(output, "Tag:", 1)
        tagged_ports = StringUtils.normalize_exos_ports(tagged_ports)

        result = self.it.compare_port_values(tagged_ports, args["port"], self.inspect_constants.FOUNDIN)

        return result, {"ret_port": ', '.join(tagged_ports)}

    def check_tagged_operational_ports(self, output, args, **kwargs):
        operational_ports_string = "Number of active ports=" + str(len(args["port"]))
        operational_result = operational_ports_string in output

        output = output.replace(",\r\n", ",")
        output = output.replace(" ", "")
        output = output.replace("Tag:", "Tag: ")
        tagged_ports = self.pw.get_value_by_offset(output, "Tag:", 1)
        tagged_ports = StringUtils.normalize_exos_ports(tagged_ports)

        result = self.it.compare_port_values(tagged_ports, args["port"], self.inspect_constants.FOUNDIN)

        result1 = result and operational_result

        return result1, {"ret_port": ', '.join(tagged_ports)}

    def check_static_tagged_ports(self, output, args, **kwargs):
        output = output.replace(",\r\n", ",")
        output = output.replace(" ", "")
        output = output.replace("Tag:", "Tag: ")
        tagged_ports = self.pw.get_value_by_offset(output, "Tag:", 1)
        tagged_ports = StringUtils.normalize_exos_ports(tagged_ports)

        result = self.it.compare_port_values(tagged_ports, args["port"], self.inspect_constants.FOUNDIN)

        return result, {"ret_port": ', '.join(tagged_ports)}

    def check_vlan_state(self, output, args, **kwargs):
        state = self.pw.get_value_by_offset(output, "Admin State:", 2)

        result = True if state.lower() == "enabled" else False

        return result, {"ret_state": state}

    def get_vlan_tag(self, output, args, **kwargs):
        configured_tag = self.pw.get_value_by_offset(output, "802.1Q Tag", 6)

        result = True if args["tag"] == configured_tag else False

        return result, {"ret_tag": configured_tag}

    def get_vlan_ipv4(self, output, args, **kwargs):
        output = output.replace("/", " /")
        configured_ip = self.pw.get_value_by_offset(output, "Primary IP:", 2)

        result = True if args["ip"] == configured_ip else False

        return result, {"ret_ip": configured_ip}

    def check_vlan_name(self, output, args, **kwargs):
        output_name = self.pw.get_value_by_offset(output, "VLAN Interface with name", 4)

        result = args["name"] in output_name

        return result, {"ret_name": output_name}

    def check_vlan_description(self, output, args, **kwargs):
        output_name = self.pw.get_value_range(output, "Description:", "Virtual router:")

        result = args["description"] in output_name

        return result, {"ret_vlan": output_name}

    def check_vman_exists(self, output, args, **kwargs):
        vman = StringUtils.exos_vlan_string(args["vman"], vman=True)
        dev_names = self.pw.get_value_by_offset(output, vman, 0).split()

        result = True if vman in dev_names else False

        return result, {"ret_vlan": ', '.join(dev_names)}

    def check_vlan_nsi(self, output, args, **kwargs):
        found_nsi = self.pw.get_value_at_location(output, column=3, name=None, row=5)

        result = True if found_nsi == args["nsi"] else False

        return result, {"ret_nsi": found_nsi}

    def check_vlan_isid(self, output, args, **kwargs):
        found_isid = self.pw.get_value_at_location(output, column=3, name=None, row=3)

        result = True if found_isid == args["i_sid"] else False

        return result, {"ret_isid": found_isid}

    def check_vlan_name_id(self, output, args, **kwargs):
        index = 0
        new_output = output.split()
        for item in new_output:
            if item.lower() == args["vlan_name"].lower():
                vlan_id = new_output[index + 1]
                if vlan_id == args["vlan_id"]:
                    return True, {"ret_vlan": vlan_id}
                else:
                    index = index + 1
            else:
                index = index + 1

        return False, output

    def check_vman_tagged_ports(self, output, args, **kwargs):
        output = output.replace(",\r\n", ",")
        output = output.replace(" ", "")
        output = output.replace("Tag:", "Tag: ")
        tagged_ports = self.pw.get_value_by_offset(output, "Tag:", 1)
        tagged_ports = StringUtils.normalize_exos_ports(tagged_ports)

        result = self.it.compare_port_values(tagged_ports, args["port"], self.inspect_constants.FOUNDIN)

        return result, {"ret_port": ', '.join(tagged_ports)}

    def check_vman_untagged_ports(self, output, args, **kwargs):
        output = output.replace(",\r\n", ",")
        output = output.replace(" ", "")
        output = output.replace("Untag:", "Untag: ")

        untagged_ports = self.pw.get_value_by_offset(output, "Untag:", 1)
        untagged_ports = StringUtils.normalize_exos_ports(untagged_ports)

        result = self.it.compare_port_values(untagged_ports, args["port"], self.inspect_constants.FOUNDIN)

        return result, {"ret_port": ', '.join(untagged_ports)}

    def check_vlan_fabric_attach_assignments_port(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_vlan_fabric_attach_assignments_vlan(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_vlan_fabric_attach_assignments_vlan_name(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_vlan_fabric_attach_assignments_type(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_vlan_fabric_attach_assignments_isid(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_vlan_fabric_attach_assignments_status(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None
