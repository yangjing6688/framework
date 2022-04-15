from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.sysinfo.base.SysinfoBaseCustomShowTools import \
    SysinfoBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
import time
import datetime
import re

class SysinfoCustomShowTools(SysinfoBaseCustomShowTools):
    def __init__(self, device):
        super(SysinfoCustomShowTools, self).__init__(device)

    def check_firmware_version(self, output, version):
        image = self.pw.get_value_by_offset(output, "ExtremeXOS", 4)
        image2 = self.pw.get_value_by_offset(output, "ExtremeXOS", 5)
        ret_image = ""

        result = False
        if version.lower() == image.lower() and "patch" not in image2:
            result = True
            ret_image = image
        elif version.lower() == image2.lower():
            result = True
            ret_image = image2
        else:
            if "patch" in image2:
                ret_image = image2
            else:
                ret_image = image

        return result, {"ret_version": ret_image}

    def check_installed_xmods(self, output, xmod_file_name):
        if len(xmod_file_name) <= 5 or xmod_file_name[len(xmod_file_name) - 5:len(xmod_file_name)] != ".xmod":
            xmod_file_name += ".xmod"

        output = output.lower()
        all_xmods = self.pw.get_value_by_offset(output, ".xmod ", 9)
        all_xmods = all_xmods.split(" ")

        result = True if xmod_file_name.lower() in all_xmods else False

        return result, {"ret_xmods": str(all_xmods)}

    def get_all_slot_numbers(self, output, *args):
        slots = self.pw.get_value_by_offset(output, "Slot-", 0)
        slots = slots.replace("Slot-", "")
        slots = slots.split(" ")
        slotlist = []

        for slot in slots:
            if slot.isdigit():
                slotlist.append(slot)

        if len(slotlist) > 1:
            result = True
        else:
            slotlist = ["1"]
            result = True

        return result, slotlist

    def get_corefile_list(self, output, *args):
        corelist = self.pw.get_value_by_offset(output, "core", 8)
        corelist = corelist.split(" ")

        if len(corelist) >= 1:
            result = True
        else:
            self.logger.log_info("Device has no current core files.")
            corelist = None
            result = True

        return result, corelist

    def get_cpu_usage(self, output, *args):
        result = True

        # Using 5min CPU average usage.
        if "Slot" in self.pw.get_value_by_offset(output, "System        ", 0):
            cpu_list = self.pw.get_value_by_offset(output, "System        ", 0)
            cpu_list = cpu_list.replace("Slot-", "")
            cpu_list = cpu_list.split(" ")
            usage_list = self.pw.get_value_by_offset(output, "System        ", 5)
            usage_list = usage_list.split(" ")
            slot_usage = []

            for i, slot in enumerate(cpu_list):
                slot_usage.append(slot + " " + usage_list[i])
        else:
            cpu_list = [1]
            usage_list = self.pw.get_value_by_offset(output, "System        ", 5)
            slot_usage = [str("1 " + usage_list)]

        if not len(cpu_list) >= 1:
            self.logger.log_info("No CPUs found!")
            result = False

        return result, slot_usage

    def get_system_uptime(self, output):
        month = self.pw.get_value_by_offset(output, "Boot Time:", 3)
        day = self.pw.get_value_by_offset(output, "Boot Time:", 4)
        hours = self.pw.get_value_by_offset(output, "Boot Time:", 5)
        year = self.pw.get_value_by_offset(output, "Boot Time:", 6)

        boot_date = time.strptime(month + "/" + day + "/" + year + " " + hours, "%b/%d/%Y %H:%M:%S")
        boot_date = datetime.datetime.fromtimestamp(time.mktime(boot_date))

        return True, boot_date

    def store_firmware_version(self, output):
        firmware = self.pw.get_value_by_offset(output, "IMG:", 9)
        self.value_storage.add_value(self.device.name, "firmware", firmware)
        result = True if firmware is not None else False

        return result, {"ret_version": firmware}

    def get_firmware_version(self, output, *args):
        firmware = self.pw.get_value_by_offset(output, "IMG:", 9)

        result = True if firmware.lower() != "valuenotpresent" else False
        return result, firmware

    def store_model(self, output):
        systype = self.pw.get_value_by_offset(output, "System Type:", 2)
        systype = re.sub('\-EXOS', '', str(systype))
        self.logger.log_debug(f"Model: {systype}")
        result = True if systype.lower() != "valuenotpresent" else False
        return result, systype

    def check_for_system_type(self, output, args, **kwargs):
        systype = self.pw.get_value_by_offset(output, "System Type:", 2)
        systype = re.sub('\-EXOS', '', str(systype))
        self.logger.log_debug(f"Model: {systype}")
        expected_value = args['type']
        result = True if systype.lower() != "valuenotpresent" and systype.lower() == expected_value.lower() else False
        return result, {"ret_system_type": systype, "output":output}
