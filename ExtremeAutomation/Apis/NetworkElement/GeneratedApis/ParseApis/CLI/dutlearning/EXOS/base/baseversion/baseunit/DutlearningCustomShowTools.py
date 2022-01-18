from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.dutlearning.base.DutlearningBaseCustomShowTools \
    import DutlearningBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


def create_instance(device):
    return DutlearningCustomShowTools(device)


class DutlearningCustomShowTools(DutlearningBaseCustomShowTools):
    def __init__(self, device):
        super(DutlearningCustomShowTools, self).__init__(device)

    def is_stacked(self, output):
        if "Invalid input" in output:
            return False, False
        return True, True

    def is_chassis(self, *args):
        return False, False

    def gather_unit_info(self, output, slot_number):
        output = output.split("||")

        if slot_number is None:
            unit_info = {"type": self.pw.get_value_by_offset(output[0], "Switch         :", 2),
                         "sku": self.pw.get_value_by_offset(output[1], "Switch      :", 3),
                         "firmware_version": self.pw.get_value_by_offset(output[1], "Switch      :", 9),
                         "bootloader_version": self.pw.get_value_by_offset(output[1], "Switch      :", 7),
                         "memory": (self.pw.get_value_by_offset(output[2], "Total DRAM", 3) + " " +
                                    self.pw.get_value_by_offset(output[2], "Total DRAM", 2).strip("():")),
                         "operating_system": self.constants.OS_EXOS,
                         "slot_number": 1}
        else:
            unit_info = {"type": self.pw.get_value_by_offset(output[0], "Slot-" + slot_number + "         :", 2),
                         "sku": self.pw.get_value_by_offset(output[1], "Slot-" + slot_number + "      :", 3),
                         "firmware_version": self.pw.get_value_by_offset(output[1], "Slot-" + slot_number + "      :",
                                                                         9),
                         "bootloader_version": self.pw.get_value_by_offset(output[1], "Slot-" + slot_number + "      :",
                                                                           7),
                         "memory": (self.pw.get_value_by_offset(output[2], "Slot-" + slot_number +
                                                                "    Total DRAM", 4) + " " +
                                    self.pw.get_value_by_offset(output[2], "Slot-" + slot_number +
                                                                "    Total DRAM", 3).strip("():")),
                         "operating_system": self.constants.OS_EXOS,
                         "slot_number": int(slot_number)}

        return unit_info, unit_info

    def gather_chassis_info(self, *args):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def gather_system_info(self, output):
        system_info = {"mac_addr": StringUtils.normalize_mac(self.pw.get_value_by_offset(output, "System MAC:", 2))}

        return system_info, system_info

    def gather_port_info(self, output):
        port_lines = []
        port_list = []
        add = False

        for line in output.splitlines():
            if "=========" in line:
                if add:
                    break
                add = True
            elif add:
                port_lines.append(line)

        for port in port_lines:
            index = 11
            while self.pw.get_value_by_offset(port, "", index) == self.constants.VALUE_NOT_PRESENT:
                index -= 1

            port_type = self.pw.get_value_by_offset(port, "", index)
            port_speed = (self.pw.get_value_by_offset(port, "", 6)
                          if self.pw.get_value_by_offset(port, "", 6) not in ["AUTO", "FULL", "HALF"]
                          else self.pw.get_value_by_offset(port, "", 5))
            port_connector = "unknown"
            port_mac = StringUtils.normalize_mac(self.pw.get_value_by_offset(output.split("||")[1], "System MAC:", 2))

            port_info = {"type": port_type,
                         "speed": port_speed,
                         "connector_type": port_connector,
                         "mac_addr": port_mac,
                         "port_string": self.pw.get_value_by_offset(port, "", 0)}

            port_list.append(port_info)

        return port_list, port_list

    def get_chassis_slot_numbers(self, *args):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED

    def get_stack_slot_numbers(self, output):
        slot_lines = []
        slot_list = []
        add = False

        for line in output.splitlines():
            if add:
                if "Slot-8" in line:
                    slot_lines.append(line)
                    break
            if "--------" in line:
                add = True
            elif add:
                slot_lines.append(line)

        for slot in slot_lines:
            if self.pw.get_value_by_offset(slot, "", 1) != "Empty":
                slot_list.append(self.pw.get_value_by_offset(slot, "", 0).strip("Slot-"))

        return slot_list, slot_list

    def gather_license_info(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def is_stack_in_sync(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_backup_slot(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None
