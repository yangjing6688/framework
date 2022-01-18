from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.SNMP.hostmonitor.base.\
    HostmonitorBaseCustomShowTools import HostmonitorBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.NumberUtils import NumberUtils


class HostmonitorCustomShowTools(HostmonitorBaseCustomShowTools):
    def __init__(self, device):
        super(HostmonitorCustomShowTools, self).__init__(device)

    def check_cpu_monitor_interval(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "=", 2)
        self.logger.log_debug(parse_result)

        result = True if int(args["interval"]) == int(parse_result) else False
        return result, {"ret_interval": parse_result}

    def check_cpu_total_utilization(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "=", 2)
        self.logger.log_debug(parse_result)

        result = NumberUtils().verify_expected_count(parse_result, args["operator"], args["percentage"])
        return result, {"ret_total_cpu": parse_result}

    def check_cpu_threshold(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "=", 2)
        self.logger.log_debug(parse_result)

        result = True if int(args["threshold"]) == int(parse_result) else False
        return result, {"ret_cpu_threshold": parse_result}

    def check_cpu_5_minute_utilization(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "=", 2)
        self.logger.log_debug(parse_result)

        result = NumberUtils().verify_expected_count(parse_result, args["operator"], args["percentage"])
        return result, {"ret_5min_cpu": parse_result}

    def check_cpu_max_utilization(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "=", 2)
        self.logger.log_debug(parse_result)

        result = NumberUtils().verify_expected_count(parse_result, args["operator"], args["percentage"])
        return result, {"ret_max_cpu": parse_result}

    def check_total_memory(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_free_memory(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "=", 2)
        self.logger.log_debug(parse_result)

        result = NumberUtils().verify_expected_count(parse_result, args["operator"], args["k_bytes"])
        return result, {"ret_free_memory": parse_result}

    def check_used_system_service_memory(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "=", 2)
        self.logger.log_debug(parse_result)

        result = NumberUtils().verify_expected_count(parse_result, args["operator"], args["k_bytes"])
        return result, {"ret_used_service_memory": parse_result}

    def check_used_user_application_memory(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "=", 2)
        self.logger.log_debug(parse_result)

        result = NumberUtils().verify_expected_count(parse_result, args["operator"], args["k_bytes"])
        return result, {"ret_used_app_memory": parse_result}

    def check_used_memory_for_process(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "=", 2)
        self.logger.log_debug(parse_result)

        result = NumberUtils().verify_expected_count(parse_result, args["operator"], args["k_bytes"])
        return result, {"ret_process_used_memory": parse_result}

    def check_cpu_process_state(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "=", 2)
        self.logger.log_debug(parse_result)

        result = True if args["state"].lower() == parse_result.lower() else False
        return result, {"ret_process_state_cpu": parse_result}

    def check_cpu_process_5_minute_utilization(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "=", 2)
        self.logger.log_debug(parse_result)

        result = NumberUtils().verify_expected_count(parse_result, args["operator"], args["percentage"])
        return result, {"ret_process_5min_cpu": parse_result}

    def check_cpu_process_max_utilization(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_cpu_process_application_time(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_cpu_process_kernel_time(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None
