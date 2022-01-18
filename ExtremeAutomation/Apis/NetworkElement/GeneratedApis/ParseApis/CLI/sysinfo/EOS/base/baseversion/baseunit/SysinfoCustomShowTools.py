from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.sysinfo.base.SysinfoBaseCustomShowTools import \
    SysinfoBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
import time
import datetime


class SysinfoCustomShowTools(SysinfoBaseCustomShowTools):
    def __init__(self, device):
        super(SysinfoCustomShowTools, self).__init__(device)

    def get_all_slot_numbers(self, output):
        output = output.replace("SYSTEM SLOT", "")
        slots = self.pw.get_value_by_offset(output, "SLOT", 1)
        slotlist = slots.split(" ")

        if len(slotlist) >= 1:
            result = True
        else:
            slotlist = ["1"]
            result = False

        return result, slotlist

    def get_corefile_list(self, output):
        corelist = self.pw.get_value_by_offset(output, "core", 5)

        if corelist is not None:
            corelist = corelist.split(" ")

        if len(corelist) >= 1:
            result = True
        else:
            self.logger.log_info("Device has no current core files.")
            corelist = None
            result = True

        return result, corelist

    def check_for_cores_dir(self, output):
        cores_dir = self.pw.get_value_by_offset(output, "cores", 4)
        result = True if cores_dir == "<DIR>" else False

        return result, result

    def get_cpu_usage(self, output):
        # Using 5min CPU average usage.
        cpu_list = self.pw.get_value_by_offset(output, "%", 0)
        cpu_list = cpu_list.split(" ")
        cpu_list_new = []

        for cpu in cpu_list:
            if cpu != "CPU":
                cpu_list_new += cpu

        usage_list = self.pw.get_value_by_offset(output, "%", 4)
        usage_list = usage_list.replace("%", "")
        usage_list = usage_list.split(" ")
        usage_list_new = []

        for usage in usage_list:
            if usage != "enabled:":
                usage_list_new.append(usage)

        if len(cpu_list_new) == 0:
            self.logger.log_info("No CPUs found!")
            return False, None

        slot_usage = []

        for i, slot in enumerate(cpu_list_new):
            slot_usage.append(slot + " " + usage_list_new[i])

        return True, slot_usage

    def get_slot_uptime(self, output):
        system_date = self.pw.get_value_by_offset(output, "Current Time:", 2)
        system_time = self.pw.get_value_by_offset(output, "Current Time:", 3)
        days = self.pw.get_value_by_offset(output, "System Uptime:", 2)
        hours = self.pw.get_value_by_offset(output, "System Uptime:", 4)
        mins = self.pw.get_value_by_offset(output, "System Uptime:", 6)
        secs = self.pw.get_value_by_offset(output, "System Uptime:", 8)

        try:
            system_current = time.strptime(system_date + " " + system_time, "%m/%d/%Y %H:%M:%S")
            system_current = datetime.datetime.fromtimestamp(time.mktime(system_current))

            since_boot = datetime.timedelta(days=int(days), hours=int(hours), minutes=int(mins), seconds=int(secs))
            boot_date = system_current - since_boot

            result = True

        except ValueError:
            boot_date = None
            result = False

        return result, boot_date

    def check_firmware_version(self, output, version, *args):
        filename_list = self.pw.get_eol_value(output, "Filename:")
        version_list = self.pw.get_value_by_offset(output, "Version:", 1).split(" ")

        result = False
        output_version = None
        for i, versions in enumerate(version_list):
            if "Active" in filename_list[i]:
                output_version = version_list[i]
                if output_version.lower() == version.lower():
                    result = True
        return result, {"ret_version": output_version}

    def get_firmware_version(self, output, *args):
        filename_list = self.pw.get_eol_value(output, "Filename:")[0].splitlines()
        version_list = self.pw.get_value_by_offset(output, "Version:", 1).split(" ")
        firmware = "unknown"

        for i, versions in enumerate(version_list):
            if "Active" in filename_list[i]:
                firmware = version_list[i]
                break

        result = True if firmware != "unknown" else False
        return result, firmware
