from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.dutlearning.base.DutlearningBaseCustomShowTools \
    import DutlearningBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


class DutlearningCustomShowTools(DutlearningBaseCustomShowTools):
    def __init__(self, device):
        super(DutlearningCustomShowTools, self).__init__(device)

    def is_stacked(self, output):
        # TODO: Determine if system is stacked/bonded.
        return False, False

    def is_chassis(self, output):
        chassis_output = output[output.find("Chassis Info:")::]
        chassis_output = chassis_output[0:chassis_output.find("\r\r\n\n", chassis_output.find("Card Info:"))]

        valid_chassis_types = ["8404"]
        chassis_type = self.pw.get_value_by_offset(chassis_output, "Chassis", 2).split()[0]

        result = True if chassis_type.lower() in valid_chassis_types else False
        return result, {"ret_chassis_type": chassis_type}

    def gather_unit_info(self, output, slot_number):
        output = output.split("||")

        unit_info = {"type": "unknown",
                     "sku": "unknown",
                     "firmware_version": "unknown",
                     "bootloader_version": "unknown",
                     "memory": "unknown",
                     "operating_system": self.constants.OS_VOSS,
                     "slot_number": 1}
        # if slot_number is None:
        #     unit_info = {"type": self.pw.get_value_by_offset(output[0], "Switch         :", 2),
        #                  "sku": self.pw.get_value_by_offset(output[1], "Switch      :", 3),
        #                  "firmware_version": self.pw.get_value_by_offset(output[1], "Switch      :", 9),
        #                  "bootloader_version": self.pw.get_value_by_offset(output[1], "Switch      :", 7),
        #                  "memory": (self.pw.get_value_by_offset(output[2], "Total DRAM", 3) + " " +
        #                             self.pw.get_value_by_offset(output[2], "Total DRAM", 2).strip("():")),
        #                  "operating_system": self.constants.OS_VOSS,
        #                  "slot_number": 1}
        # else:
        #     unit_info = {"type": self.pw.get_value_by_offset(output[0], "Slot-" + slot_number + "         :", 2),
        #                  "sku": self.pw.get_value_by_offset(output[1], "Slot-" + slot_number + "      :", 3),
        #                  "firmware_version": self.pw.get_value_by_offset(output[1], "Slot-" + slot_number +
        #                                                                  "      :", 9),
        #                  "bootloader_version": self.pw.get_value_by_offset(output[1], "Slot-" + slot_number +
        #                                                                    "      :", 7),
        #                  "memory": (self.pw.get_value_by_offset(output[2], "Slot-" + slot_number +
        #                                                         "    Total DRAM", 4) + " " +
        #                             self.pw.get_value_by_offset(output[2], "Slot-" + slot_number +
        #                                                         "    Total DRAM", 3).strip("():")),
        #                  "operating_system": self.constants.OS_VOSS,
        #                  "slot_number": int(slot_number)}

        return unit_info, unit_info

    def gather_chassis_info(self, output, chassis_number):
        fw_output = output[output.find("Primary Release")::]
        fw_output = fw_output[0:fw_output.find("\r\r\n\n", fw_output.find("AVAILABLE ENCRYPTION MODULES"))]

        chassis_info = {"type": self.pw.get_value_by_offset(output, "Chassis :", 2),
                        "sku": self.pw.get_value_by_offset(output, "Part Number :", 3),
                        "firmware_version": self.pw.get_value_by_offset(output, "Primary Release", 0),
                        "bootloader_version": self.pw.get_value_by_offset(fw_output, "UBOOT", 1),
                        "memory": None,
                        "operating_system": self.constants.OS_VOSS,
                        "chassis_number": int(chassis_number) if chassis_number is not None else 1}

        return chassis_info, chassis_info

    def gather_system_info(self, output):
        mac_addr = StringUtils.normalize_mac(self.pw.get_value_by_offset(output, "BaseMacAddr", 2))
        system_info = {"mac_addr": mac_addr}

        return system_info, system_info

    def gather_port_info(self, output):
        port_lines = []
        status_lines = []
        port_list = []

        interface_output = output.split("Port Interface")[0]
        status_output = output.split("Port Interface")[1]

        add = False
        for line in interface_output.splitlines():
            if "----------" in line:
                if add:
                    break
                add = True
            elif add:
                if line and self.device.main_prompt not in line and not line.isspace() and "======" not in line:
                    port_lines.append(line)

        add = False
        for line in status_output.splitlines():
            if "----------" in line:
                if add:
                    break
                add = True
            elif add:
                if line and self.device.main_prompt not in line and not line.isspace() and "======" not in line:
                    status_lines.append(line)

        for i, port in enumerate(port_lines):
            port_type = self.pw.get_value_by_offset(port, "", 2)
            port_speed = (self.pw.get_range_by_offset(status_lines[i], "", 5, 6)
                          if self.pw.get_value_by_offset(status_lines[i], "", 5) in ["full", "half"]
                          else self.pw.get_range_by_offset(status_lines[i], "", 4, 5))
            port_connector = "unknown"
            port_mac = StringUtils.normalize_mac(self.pw.get_value_by_offset(port, "", 6))

            port_info = {"type": port_type,
                         "speed": port_speed,
                         "connector_type": port_connector,
                         "mac_addr": port_mac,
                         "port_string": self.pw.get_value_by_offset(port, "", 0)}

            port_list.append(port_info)

        return port_list, port_list

    def get_chassis_slot_numbers(self, output, chassis_number):
        slot_list = []

        slot_output = output[output.find("Card Info :")::]
        slot_output = slot_output[0:slot_output.find("\r\r\n\n", slot_output.find("Temperature Info :"))]

        slot_lines = [line for line in slot_output]

        for slot in slot_lines:
            if isinstance(slot[0], int):
                slot_list.append(self.pw.get_value_by_offset(slot, "", 0))

        return slot_list, slot_list

    def get_stack_slot_numbers(self, *args):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def gather_license_info(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None
