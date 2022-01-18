from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Keywords.BaseClasses.KeywordResult import KeywordResult
from ExtremeAutomation.Library.Utils.ListUtils import ListUtils
from pytest_testconfig import config
from ExtremeAutomation.Imports.pytestConfigHelper import PytestConfigHelper
import datetime


class NetworkElementHealthCheck(NetworkElementKeywordBaseClass):

    def store_current_corefile_list(self, device_names, **kwargs):
        """
        Keyword Arguments:
        [device_names] - The Device(s) to store core file lists from.

        Stores a list of the current core files in Value Storage.
        """
        device_names = ListUtils.convert_to_list(device_names)

        kw_results = []
        for device_name in device_names:
            dev, _, _ = self._init_keyword(device_name, **kwargs)

            if dev.oper_sys == self.constants.OS_EOS:
                kw_results += self._determine_number_of_slots(device_name, **kwargs)

                for slot in dev.slot_list:
                    kw_results += self._store_slot_corefile_list(device_name, slot, **kwargs)

            elif dev.oper_sys == self.constants.OS_EXOS:
                kw_results += self._determine_number_of_slots(device_name, **kwargs)

                if len(dev.slot_list) == 0:
                    kw_results += self._store_nonstacked_corefiles_list(device_name)
                else:
                    for slot in dev.slot_list:
                        kw_results += self._store_slot_corefile_list(device_name, slot, **kwargs)

        self._keyword_cleanup(kw_results)

    def compare_and_store_corefiles(self, device_names, engine_ip=None, vr="vr-default", trm_run=False, **kwargs):
        """
        Keyword Arguments:
        [device_names] - The Device(s) to store core file lists from.
        [engine_ip]    - The IP Address of the Test Engine.
        [vr]           - The VR for management traffic.
        [trm_run]      - Flag for whether the current test is running from TRM.

        Compares the current core file list to the stored a list and stores the current list.
        """
        device_names = ListUtils.convert_to_list(device_names)

        kw_results = []
        for device_name in device_names:
            dev, _, _ = self._init_keyword(device_name, **kwargs)

            result = True
            if len(dev.slot_list) == 0:
                old_corelist = self.value_storage.get_value(device_name, "corelist")

                kw_results += self._store_nonstacked_corefiles_list(device_name)
                new_corelist = self.value_storage.get_value(device_name, "corelist")

                if old_corelist != new_corelist:
                    for corefile in new_corelist:
                        if corefile not in old_corelist:
                            result = False
                            kw_results += self._upload_core_file(device_name, corefile, "1", engine_ip, vr, trm_run)

                    kw_results.append(KeywordResult(device_name, result,
                                                    "No new Core files found on device.",
                                                    "Device has a new Core file(s)!", None))
            else:
                for slot in dev.slot_list:
                    slotname = "slot" + str(slot) + "_core_files"
                    old_corelist = self.value_storage.get_value(device_name, slotname)

                    kw_results.append(self._store_slot_corefile_list(device_name, slot, **kwargs))
                    new_corelist = self.value_storage.get_value(device_name, slotname)

                    if old_corelist != new_corelist:
                        for corefile in new_corelist:
                            if corefile not in old_corelist:
                                result = False
                                kw_results += self._upload_core_file(device_name, corefile, slot, engine_ip, vr,
                                                                     trm_run)

                        kw_results.append(KeywordResult(device_name, result,
                                                        "No new Core files found on slot " + slot + ".",
                                                        "Slot " + slot + " has a new Core file(s)!", None))
            if not result:
                if engine_ip is not None:
                    kw_results += self._store_logging_files(device_name, engine_ip, trm_run)
                    if dev.oper_sys == self.constants.OS_EOS:
                        pass
                        # TODO: Create message_log grabber.

        return self._keyword_cleanup(kw_results)

    def check_system_cpu_usage(self, device_names, cpu_limit="70", **kwargs):
        """
        Keyword Arguments:
        [device_names] - The Device(s) to check CPU utilization on.
        [cpu_limit]    - The allowed CPU load before failing the keyword.

        Checks the system's CPU usage against the allowed limit.
        """
        device_names = ListUtils.convert_to_list(device_names)
        if cpu_limit.isdigit():
            pass
        else:
            self.logger.log_info("CPU Limit, " + cpu_limit + ", is not a valid integer.")

        kw_results = []
        for device_name in device_names:
            dev, cmd_api, parse_api = self._init_keyword(device_name, self.constants.API_SYSINFO,
                                                         self.constants.API_SYSINFO, **kwargs)

            cmd_obj = cmd_api.show_system_cpu_usage(None, **kwargs)
            output = cmd_obj.return_text
            result, slot_usage = parse_api.get_cpu_usage(output)

            high_usage_flag = False
            if len(slot_usage) > 1:
                for slot in slot_usage:
                    usage = slot.split(" ")

                    if float(usage[1]) > int(cpu_limit):
                        high_usage_flag = True
                        self.logger.log_info("Slot " + usage[0] +
                                             " CPU usage was over the limit of " + cpu_limit + "%.")
            else:
                usage = slot_usage[0].split(" ")
                if float(usage[1]) > int(cpu_limit):
                    high_usage_flag = True
                    self.logger.log_info("System CPU usage was over the limit of " + cpu_limit + "%.")

            kw_results.append(self._determine_result(dev, cmd_obj, high_usage_flag, False,
                                                     "CPU utilization within permitted range.",
                                                     "High CPU utilization!", **kwargs))

        return self._keyword_cleanup(kw_results)

    def store_current_boot_date(self, device_names, **kwargs):
        """
        Keyword Arguments:
        [device_names] - The Device(s) to store boot date from.

        Stores a snapshot of the system's current boot date/time in Value Storage.
        """
        device_names = ListUtils.convert_to_list(device_names)

        kw_results = []
        for device_name in device_names:
            dev, _, _ = self._init_keyword(device_name, **kwargs)

            if dev.oper_sys == self.constants.OS_EOS:
                if not dev.slot_list:
                    kw_results += self._determine_number_of_slots(device_name, **kwargs)

                for slot in dev.slot_list:
                    kw_results += self._store_system_slot_boot_date(device_name, slot, **kwargs)
            else:
                kw_results += self._store_system_boot_date(device_name, **kwargs)

        self._keyword_cleanup(kw_results)

    def compare_and_store_boot_date(self, device_names, engine_ip=None, trm_run=False, **kwargs):
        """
        Keyword Arguments:
        [device_names] - The Device(s) to store core file lists from.
        [engine_ip]    - The IP Address of the Test Engine.
        [trm_run]      - Flag for whether the current test is running from TRM.

        Compares the current system boot date/time with the stored value and stores the current boot date/time.
        """
        device_names = ListUtils.convert_to_list(device_names)

        kw_results = []
        for device_name in device_names:
            dev, _, _ = self._init_keyword(device_name, **kwargs)

            result = True
            if dev.oper_sys == self.constants.OS_EOS:

                if not dev.slot_list:
                    kw_results += self._determine_number_of_slots(device_name, **kwargs)
                    self.logger.log_info("No slot list found, device may have reset.")

                for slot in dev.slot_list:
                    slotname = "slot" + str(slot) + "_boot_date"
                    old_boot_date = self.value_storage.get_value(device_name, slotname)

                    kw_results += self._store_system_slot_boot_date(device_name, slot, **kwargs)
                    new_boot_date = self.value_storage.get_value(device_name, slotname)

                    rounded_date1 = old_boot_date - new_boot_date
                    rounded_date2 = new_boot_date - old_boot_date

                    if abs(rounded_date1.total_seconds()) <= datetime.timedelta(seconds=5).total_seconds() or \
                       abs(rounded_date2.total_seconds()) <= datetime.timedelta(seconds=5).total_seconds():
                        self.logger.log_info("Boot date " + str(new_boot_date) + " is within 5 seconds of " +
                                             str(old_boot_date))
                        result = True
                    else:
                        result = False

                    kw_results.append(KeywordResult(device_name, result,
                                                    "System slot " + slot + " boot date was the same.",
                                                    "System slot " + slot + " boot date was NOT the same. " +
                                                    str(old_boot_date) + " != " + str(new_boot_date) + ". Slot reset!",
                                                    None))

            else:
                old_boot_date = self.value_storage.get_value(device_name, "boot_date")

                kw_results += self._store_system_boot_date(device_name)
                new_boot_date = self.value_storage.get_value(device_name, "boot_date")

                rounded_date1 = old_boot_date - new_boot_date
                rounded_date2 = new_boot_date - old_boot_date

                if abs(rounded_date1.total_seconds()) <= datetime.timedelta(seconds=5).total_seconds() or \
                   abs(rounded_date2.total_seconds()) <= datetime.timedelta(seconds=5).total_seconds():
                    self.logger.log_info("Boot date " + str(new_boot_date) + " is within 5 seconds of " +
                                         str(old_boot_date))
                    result = True
                else:
                    result = False
                kw_results.append(KeywordResult(device_name, result,
                                                "System boot date was the same.",
                                                "System boot date was NOT the same. " +
                                                str(old_boot_date) + " != " + str(new_boot_date) + ". System reset!",
                                                None))

            if not result:
                if engine_ip is not None:
                    kw_results += self._store_logging_files(device_name, engine_ip, trm_run)
                    if dev.oper_sys == self.constants.OS_EOS:
                        pass
                        # TODO: Create message_log grabber.

        return self._keyword_cleanup(kw_results)

    def _generate_show_support(self, device_names, filename, slot="1", **kwargs):
        device_names = ListUtils.convert_to_list(device_names)

        kw_results = []
        for device_name in device_names:
            dev, cmd_api, _ = self._init_keyword(device_name, self.constants.API_FILEMANAGEMENT, **kwargs)

            args = {"filename": filename,
                    "slot": slot}

            cmd_obj = cmd_api.generate_support_file(args)

            kw_results.append(self._determine_result(dev, cmd_obj, True, True, **kwargs))

        return kw_results

    def _determine_number_of_slots(self, device_names, **kwargs):
        device_names = ListUtils.convert_to_list(device_names)

        kw_results = []
        for device_name in device_names:
            dev, cmd_api, parse_api = self._init_keyword(device_name, self.constants.API_SYSINFO,
                                                         self.constants.API_SYSINFO, ignore_cli_feedback=True, **kwargs)

            cmd_obj = cmd_api.show_hardware_summary(None)
            output = cmd_obj.return_text
            result, slotlist = parse_api.get_all_slot_numbers(output)
            if slotlist:
                dev.add_slot_to_list(slotlist)

            kw_results.append(self._determine_result(dev, cmd_obj, result, True,
                                                     "All Network Element slots added to slot_list.",
                                                     "Network Element slot numbers could not be found!", **kwargs))
        return kw_results

    def _store_slot_corefile_list(self, device_names, slot, **kwargs):
        device_names = ListUtils.convert_to_list(device_names)

        kw_results = []
        for device_name in device_names:
            dev, cmd_api, parse_api = self._init_keyword(device_name, self.constants.API_SYSINFO,
                                                         self.constants.API_SYSINFO, **kwargs)

            args = {"slot": slot}

            if dev.oper_sys == self.constants.OS_EXOS and str(slot) != "1":
                self.logger.log_info("Changing to system slot " + str(slot) + ".")
                self._change_console_slot(device_name, slot)
                cmd_api = dev.get_api(self.constants.API_SYSINFO)
                cmd_obj = cmd_api.show_core_files(args)
                output = cmd_obj.return_text
                self._exit_console_slot(device_name)
            elif dev.oper_sys == self.constants.OS_EOS:
                cmd_obj = cmd_api.show_slot_files(args)
                output = cmd_obj.return_text
                cores_dir = parse_api.check_for_cores_dir(output)

                if cores_dir:
                    cmd_obj = cmd_api.show_core_files(args)
                    output = cmd_obj.return_text
                else:
                    output = ""
            else:
                cmd_obj = cmd_api.show_core_files(args)
                output = cmd_obj.return_text

            result, corelist = parse_api.get_corefile_list(output)
            slotname = "slot" + str(slot) + "_core_files"
            self.value_storage.add_value(device_name, slotname, corelist)

            kw_results.append(self._determine_result(dev, cmd_obj, result, True,
                                                     "All current core files documented.",
                                                     "No core files found!", **kwargs))
        return kw_results

    def _store_nonstacked_corefiles_list(self, device_names, **kwargs):
        device_names = ListUtils.convert_to_list(device_names)

        kw_results = []
        for device_name in device_names:
            dev, cmd_api, parse_api = self._init_keyword(device_name, self.constants.API_SYSINFO,
                                                         self.constants.API_SYSINFO, **kwargs)

            cmd_obj = cmd_api.show_core_files(None)
            output = cmd_obj.return_text
            result, corelist = parse_api.get_corefile_list(output)
            self.value_storage.add_value(device_name, "corelist", corelist)

            kw_results.append(self._determine_result(dev, cmd_obj, result, True,
                                                     "All current core files documented.",
                                                     "No core files found!", **kwargs))
        return kw_results

    def _change_console_slot(self, device_names, slot="1", **kwargs):
        device_names = ListUtils.convert_to_list(device_names)

        kw_results = []
        for device_name in device_names:
            dev, cmd_api, _ = self._init_keyword(device_name, self.constants.API_UNIT, **kwargs)
            if dev.oper_sys == self.constants.OS_EOS:
                self._init_keyword(device_name, wait_for_prompt=False, **kwargs)

            args = {"username": dev.username,
                    "password": dev.password,
                    "slot": slot}

            cmd_obj = cmd_api.change_current_slot(args)
            kw_results.append(self._determine_result(dev, cmd_obj, **kwargs))

        return kw_results

    def _exit_console_slot(self, device_names, **kwargs):
        device_names = ListUtils.convert_to_list(device_names)

        kw_results = []
        for device_name in device_names:
            dev, cmd_api, _ = self._init_keyword(device_name, self.constants.API_UNIT, wait_for_prompt=False, **kwargs)

            cmd_obj = cmd_api.exit_current_slot(None)
            kw_results.append(self._determine_result(dev, cmd_obj))

        return kw_results

    def _upload_core_file(self, device_names, file_name, slot, server_ip, vr, trm_run, sh_support=False, **kwargs):
        device_names = ListUtils.convert_to_list(device_names)
        yes_no = "No" if sh_support is False else "Yes"

        kw_results = []
        for device_name in device_names:
            dev, cmd_api, parse_api = self._init_keyword(device_name, self.constants.API_FILEMANAGEMENT,
                                                         self.constants.API_FILEMANAGEMENT, **kwargs)

            remote_file = "slot" + slot + "_" + file_name
            args = {"file_name": file_name,
                    "remote_file": remote_file,
                    "server_ip": server_ip,
                    "slot": slot,
                    "vr": vr,
                    "yes_no": yes_no}

            cmd_obj = cmd_api.upload_core_file(args)
            output = cmd_obj.return_text

            if trm_run is True:
                result = parse_api.move_core_files(output, server_ip, remote_file)
            else:
                result = True

            kw_results.append(self._determine_result(dev, cmd_obj, result, True,
                                                     "All new Core files uploaded to Engine.",
                                                     "Core file upload failed!"))
        return kw_results

    def _store_logging_files(self, device_names, server_ip, trm_run, **kwargs):
        device_names = ListUtils.convert_to_list(device_names)

        kw_results = []
        for device_name in device_names:
            dev, cmd_api, parse_api = self._init_keyword(device_name, self.constants.API_FILEMANAGEMENT,
                                                         self.constants.API_FILEMANAGEMENT, **kwargs)

            username = dev.username
            password = dev.password
            if len(dev.slot_list) == 0:
                slot = "1"
                args = {"username": username,
                        "password": password,
                        "slot": slot}

                cmd_obj = cmd_api.show_logging_files(args)
                output = cmd_obj.return_text

                result = parse_api.get_logfile_list(output, slot, server_ip, trm_run)

                kw_results.append(self._determine_result(dev, cmd_obj, result, True,
                                                         "All current log files uploaded.",
                                                         "No current log files found."))

            else:
                for slot in dev.slot_list:
                    if dev.oper_sys == self.constants.OS_EXOS and str(slot) != "1":
                        kw_results += self._change_console_slot(device_name, slot)

                        args = {"username": username,
                                "password": password,
                                "slot": slot}

                        cmd_api = dev.get_api(self.constants.API_FILEMANAGEMENT)
                        cmd_obj = cmd_api.show_logging_files(args)
                        output = cmd_obj.return_text

                        kw_results += self._exit_console_slot(device_name)
                        result = parse_api.get_logfile_list(output, slot, server_ip, trm_run)

                        kw_results.append(self._determine_result(dev, cmd_obj, result, True,
                                                                 "All current log files uploaded.",
                                                                 "No current log files found."))
                    else:
                        args = {"username": username,
                                "password": password,
                                "slot": slot}

                        cmd_obj = cmd_api.show_logging_files(args)
                        output = cmd_obj.return_text

                        result = parse_api.get_logfile_list(output, slot, server_ip, trm_run)

                        kw_results.append(self._determine_result(dev, cmd_obj, result, True,
                                                                 "All current log files uploaded.",
                                                                 "No current log files found."))
        return kw_results

    def _store_system_slot_boot_date(self, device_names, slot, **kwargs):
        device_names = ListUtils.convert_to_list(device_names)

        kw_results = []
        for device_name in device_names:
            kw_results += self._change_console_slot(device_name, slot)
            dev, cmd_api, parse_api = self._init_keyword(device_name, self.constants.API_SYSINFO,
                                                         self.constants.API_SYSINFO, **kwargs)
            if dev.oper_sys == self.constants.OS_EOS:
                self._init_keyword(device_name, wait_for_prompt=False, **kwargs)

            args = {"slot": slot}

            cmd_obj = cmd_api.show_system_slot_info(args)
            output = cmd_obj.return_text
            result, boot_date = parse_api.get_slot_uptime(output)

            kw_results += self._exit_console_slot(device_name)

            slotname = "slot" + str(slot) + "_boot_date"
            self.value_storage.add_value(device_name, slotname, boot_date)

            kw_results += self._determine_result(dev, cmd_obj, result, True,
                                                 "System slot " + slot + " boot date stored.",
                                                 "System slot " + slot + " boot date NOT stored!")
        return kw_results

    def _store_system_boot_date(self, device_names, **kwargs):
        device_names = ListUtils.convert_to_list(device_names)

        kw_results = []
        for device_name in device_names:
            dev, cmd_api, parse_api = self._init_keyword(device_name, self.constants.API_SYSINFO,
                                                         self.constants.API_SYSINFO, **kwargs)

            cmd_obj = cmd_api.show_system_info(None)
            output = cmd_obj.return_text
            result, boot_date = parse_api.get_system_uptime(output)

            if boot_date:
                self.value_storage.add_value(device_name, "boot_date", boot_date)

                kw_results.append(self._determine_result(dev, cmd_obj, result, True,
                                                         "System boot date stored.",
                                                         "System boot date NOT stored!"))
            else:
                kw_results.append(self._determine_result(dev, cmd_obj, False, True,
                                                         "System boot date stored.",
                                                         "System boot date not supported on this device."))
        return kw_results
    def store_device_model(self, **kwargs):
        hConfig = PytestConfigHelper(config)
        kw_results = []
        i=0
        while i < hConfig.node_count:
            i+=1
            device_name = config[f'netelem{i}']['name']
            args = {}
            dev, cmd_api, parse_api = self._init_keyword(device_name, self.constants.API_SYSINFO,
                                                         self.constants.API_SYSINFO, **kwargs)

            cmd_obj = cmd_api.show_system_info(args, **kwargs)
            if not cmd_obj.not_supported:
                cmd_obj = dev.send_command_object(cmd_obj)
                output = cmd_obj.return_text
                result, store_model = parse_api.store_model(output)

                if store_model:
                    self.value_storage.add_value(device_name, "model", store_model)
                    config[f'netelem{i}']['model'] = store_model
                    self.logger.log_debug(f"Netelem model: {store_model}")
                    kw_results.append(self._determine_result(dev, cmd_obj, result, True,
                                                             "System model stored.",
                                                             "System model NOT stored!"))
                else:
                    kw_results.append(self._determine_result(dev, cmd_obj, False, True,
                                                             "System model stored.",
                                                             "System model not supported on this device."))
        return kw_results
