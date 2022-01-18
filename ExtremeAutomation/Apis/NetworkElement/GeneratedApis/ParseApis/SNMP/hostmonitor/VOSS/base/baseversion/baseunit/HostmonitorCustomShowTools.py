from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.SNMP.hostmonitor.base.\
    HostmonitorBaseCustomShowTools import HostmonitorBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.NumberUtils import NumberUtils


class HostmonitorCustomShowTools(HostmonitorBaseCustomShowTools):
    def __init__(self, device):
        super(HostmonitorCustomShowTools, self).__init__(device)

    def check_cpu_current_total_utilization(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "=", 2)
        self.logger.log_debug(parse_result)

        result = NumberUtils().verify_expected_count(parse_result, args["operator"], args["percentage"])
        return result, {"ret_total_cpu": parse_result}

    def check_cpu_5_minute_total_utilization(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "=", 2)
        self.logger.log_debug(parse_result)

        result = NumberUtils().verify_expected_count(parse_result, args["operator"], args["percentage"])
        return result, {"ret_5min_cpu": parse_result}

    def check_cpu_highest_5_minute_total_utilization(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "=", 2)
        self.logger.log_debug(parse_result)

        result = NumberUtils().verify_expected_count(parse_result, args["operator"], args["percentage"])
        return result, {"ret_5min_high_cpu": parse_result}

    def check_used_total_memory(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "=", 2)
        self.logger.log_debug(parse_result)

        result = NumberUtils().verify_expected_count(parse_result, args["operator"], args["k_bytes"])
        return result, {"ret_used_memory": parse_result}

    def check_free_total_memory(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "=", 2)
        self.logger.log_debug(parse_result)

        result = NumberUtils().verify_expected_count(parse_result, args["operator"], args["k_bytes"])
        return result, {"ret_free_memory": parse_result}

    def check_memory_total_utilization(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "=", 2)
        self.logger.log_debug(parse_result)

        result = NumberUtils().verify_expected_count(parse_result, args["operator"], args["percentage"])
        return result, {"ret_total_memory": parse_result}

    def check_memory_5_minute_total_utilization(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "=", 2)
        self.logger.log_debug(parse_result)

        result = NumberUtils().verify_expected_count(parse_result, args["operator"], args["percentage"])
        return result, {"ret_5min_memory": parse_result}

    def check_memory_highest_5_minute_total_utilization(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "=", 2)
        self.logger.log_debug(parse_result)

        result = NumberUtils().verify_expected_count(parse_result, args["operator"], args["percentage"])
        return result, {"ret_5min_high_memory": parse_result}

    def check_used_fbuf(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "=", 2)

        result = NumberUtils().verify_expected_count(parse_result, args["operator"], args["value"])
        return result, {"ret_used_fbuf": parse_result}

    def check_free_fbuf(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "=", 2)

        result = NumberUtils().verify_expected_count(parse_result, args["operator"], args["value"])
        return result, {"ret_free_fbuf": parse_result}

    def check_exhausted_fbufs(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "=", 2)

        result = NumberUtils().verify_expected_count(parse_result, args["operator"], args["value"])
        return result, {"ret_exhausted_fbuf": parse_result}

    def check_net_stack_system_free_mbuf(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "=", 2)

        result = NumberUtils().verify_expected_count(parse_result, args["operator"], args["value"])
        return result, {"ret_free_mbuf": parse_result}

    def check_net_stack_data_free_mbuf(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "=", 2)

        result = NumberUtils().verify_expected_count(parse_result, args["operator"], args["value"])
        return result, {"ret_free_mbuf": parse_result}

    def check_net_stack_system_used_mbuf(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "=", 2)

        result = NumberUtils().verify_expected_count(parse_result, args["operator"], args["value"])
        return result, {"ret_used_mbuf": parse_result}

    def check_net_stack_data_used_mbuf(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "=", 2)

        result = NumberUtils().verify_expected_count(parse_result, args["operator"], args["value"])
        return result, {"ret_used_mbuf": parse_result}

    def check_net_stack_system_socket_mbuf(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "=", 2)

        result = NumberUtils().verify_expected_count(parse_result, args["operator"], args["value"])
        return result, {"Ret_socket_mbuf": parse_result}

    def check_highest_queue_entries_consumed(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "=", 2)

        result = NumberUtils().verify_expected_count(parse_result, args["operator"], args["value"])
        return result, {"ret_queue_high_consumed": parse_result}

    def check_current_queue_entries_consumed(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "=", 2)

        result = NumberUtils().verify_expected_count(parse_result, args["operator"], args["value"])
        return result, {"ret_queue_current_consumed": parse_result}

    def check_free_queue_entries(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "=", 2)

        result = NumberUtils().verify_expected_count(parse_result, args["operator"], args["value"])
        return result, {"ret_queue_free": parse_result}
