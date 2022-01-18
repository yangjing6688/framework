from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.dutlearning.base.DutlearningBaseCustomShowTools \
    import DutlearningBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
import re
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


def create_instance(device):
    return DutlearningCustomShowTools(device)


class DutlearningCustomShowTools(DutlearningBaseCustomShowTools):
    def __init__(self, device):
        super(DutlearningCustomShowTools, self).__init__(device)

    def is_stacked(self, output):
        state = self.pw.get_value_by_offset(output, "Global Bonding State", 4)

        result = True if state == "enabled" else False
        return result, {"ret_stacking_state": state}

    def is_chassis(self, output):
        valid_chassis_types = ["s1", "s3", "s4", "s6", "s8",
                               "k6", "k10"]
        chassis_type = self.pw.get_value_by_offset(output, "Chassis Type", 2)

        if "bonded" in chassis_type.lower():
            chassis_type = self.pw.get_value_by_offset(output, "Chassis Type", 3).split()
            chassis_type = [i for i in chassis_type if i != "unknown"][0]

        result = True if chassis_type.lower() in valid_chassis_types else False
        return result, {"ret_chassis_type": chassis_type}

    def gather_unit_info(self, output, slot_number):
        slot_number = slot_number if slot_number is not None else "1"
        mod_output = output.split("SYSTEM SLOT HARDWARE INFORMATION")[1]
        slot_output = mod_output[mod_output.find("SLOT " + slot_number)::]
        slot_output = slot_output[0:slot_output.find("\r\r\n\n")]

        unit_info = {"type": self.pw.get_value_by_offset(slot_output, "Model:", 1).split()[0],
                     "sku": self.pw.get_value_by_offset(slot_output, "Serial Number:", 2).split()[0],
                     "firmware_version": self.pw.get_value_by_offset(slot_output, "Firmware Version:", 2),
                     "bootloader_version": self.pw.get_value_by_offset(slot_output, "BootCode Version:", 2),
                     "memory": (self.pw.get_value_by_offset(slot_output, "SDRAM:", 1) + " " +
                                self.pw.get_value_by_offset(slot_output, "SDRAM:", 2)),
                     "operating_system": self.constants.OS_EOS,
                     "slot_number": int(slot_number)}

        return unit_info, unit_info

    def gather_chassis_info(self, output, chassis_number):
        chassis_header = ("CHASSIS HARDWARE INFORMATION" if chassis_number is None else
                          "CHASSIS " + chassis_number + " HARDWARE INFORMATION")

        chassis_output = output[output.find(chassis_header)::]
        chassis_output = chassis_output[0:chassis_output.find("\r\r\n\n", chassis_output.find("Chassis Type:"))]

        chassis_info = {"type": self.pw.get_value_range(chassis_output, "Chassis Type:", "Chassis Serial Number:"),
                        "sku": self.pw.get_value_by_offset(chassis_output, "Chassis Serial Number:", 3),
                        "firmware_version": None,
                        "bootloader_version": None,
                        "memory": None,
                        "operating_system": self.constants.OS_EOS,
                        "chassis_number": int(chassis_number) if chassis_number is not None else 1}

        return chassis_info, chassis_info

    def gather_system_info(self, output):
        mac_addr = StringUtils.normalize_mac(self.pw.get_value_by_offset(output, "host.0.1", 0).split()[0])
        system_info = {"mac_addr": mac_addr}

        return system_info, system_info

    def gather_port_info(self, output):
        port_re = r"^[a-zA-Z]+\.\d+\.\d+"

        port_list = []
        output_list = output.split("||")[0].splitlines()

        port_output_list = [i for i in output_list if len(re.findall(port_re, i)) == 1]

        for port in port_output_list:
            mod_port = port[0:13] + port[30::]  # Remove the alias column from the port output.
            mac_addr = StringUtils.normalize_mac(self.pw.get_value_by_offset(
                output.split("||")[1], self.pw.get_value_by_offset(port, "", 0) + " ", 0))

            port_info = {"type": self.pw.get_value_by_offset(mod_port, "", 0).split(".")[0],
                         "speed": self.pw.get_value_by_offset(mod_port, "", 3),
                         "connector_type": self.pw.get_value_by_offset(mod_port, "", 5),
                         "mac_addr": mac_addr if mac_addr else None,
                         "port_string": self.pw.get_value_by_offset(mod_port, "", 0)}

            port_list.append(port_info)

        return port_list, port_list

    @staticmethod
    def get_chassis_slot_numbers(output, chassis_number):
        mod_output = output.split("SYSTEM SLOT HARDWARE INFORMATION")[1].splitlines()
        slot_numbers = []
        slot_re = r"^SLOT \d+" if chassis_number is None else r"^SLOT \d+ \(Chassis " + chassis_number

        for i in range(len(mod_output)):
            re_result = re.findall(slot_re, mod_output[i].lstrip())
            if len(re_result) == 1:
                try:
                    if mod_output[i + 1] != "":
                        slot_numbers.append(re_result[0].split()[1])
                except IndexError:
                    pass

        return slot_numbers, slot_numbers

    @staticmethod
    def get_stack_slot_numbers(output):
        mod_output = output.split("SYSTEM SLOT HARDWARE INFORMATION")[0].splitlines()
        stack_numbers = []
        stack_re = r"^CHASSIS \d+"

        for i in range(len(mod_output)):
            re_result = re.findall(stack_re, mod_output[i].lstrip())
            if len(re_result) == 1:
                try:
                    if "unknown" not in mod_output[i + 2]:
                        stack_numbers.append(re_result[0].split()[1])
                except IndexError:
                    pass

        return stack_numbers, stack_numbers

    def gather_license_info(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None
