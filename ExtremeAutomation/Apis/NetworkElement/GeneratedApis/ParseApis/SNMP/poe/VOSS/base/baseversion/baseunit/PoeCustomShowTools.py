from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.SNMP.poe.base.PoeBaseCustomShowTools import \
    PoeBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.NumberUtils import NumberUtils


class PoeCustomShowTools(PoeBaseCustomShowTools):
    def __init__(self, device):
        super(PoeCustomShowTools, self).__init__(device)

    def check_poe_power_usage_threshold(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "=", 2)

        result = True if parse_result == args["threshold"] else False
        return result, {"ret_threshold": parse_result}

    def check_poe_port_state(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "=", 2)

        result = True if parse_result == "1" else False
        return result, {"ret_state": parse_result}

    def check_poe_port_power_limit(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "=", 2)

        result = True if parse_result == args["power_limit"] else False
        return result, {"ret_power_limit": parse_result}

    def check_poe_port_power_priority(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "=", 2)

        result = True if parse_result == args["power_priority_value"] else False
        return result, {"ret_power_priority": parse_result}

    def check_poe_port_detect_type(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "=", 2)

        result = True if parse_result == args["detect_type_value"] else False
        return result, {"ret_detect_type": parse_result}

    def check_poe_port_measured_voltage(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.45.5.8.1.1.1.5." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = NumberUtils().verify_expected_count(parse_result, args["value_operator"], args["decivolts"])
        return result, {"ret_measured_voltage": parse_result}

    def check_poe_port_measured_current(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.45.5.8.1.1.1.6." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = NumberUtils().verify_expected_count(parse_result, args["value_operator"], args["milliamps"])
        return result, {"ret_measured_current": parse_result}

    def check_poe_port_measured_power(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.45.5.8.1.1.1.6." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = NumberUtils().verify_expected_count(parse_result, args["value_operator"], args["milliwatts"])
        return result, {"ret_measured_power": parse_result}

    def check_poe_port_detection_status(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "=", 2)

        result = True if parse_result == args["status_value"] else False
        return result, {"ret_detect_status": parse_result}

    def check_poe_port_power_classification(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "=", 2)

        result = True if parse_result == args["power_class_value"] else False
        return result, {"ret_power_classification": parse_result}

    def check_poe_main_operational_status(self, *args):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_poe_main_available_power(self, output, args, **kwargs):
        item = "SNMPv2-SMI::mib-2.105.1.3.1.1.2." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["power"] else False
        return result, {"ret_avail_power": parse_result}

    def check_poe_main_consumption_power(self, output, args, **kwargs):
        item = "SNMPv2-SMI::mib-2.105.1.3.1.1.4." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = NumberUtils().verify_expected_count(parse_result, args["value_operator"], args["power"])
        return result, {"ret_consumed_power": parse_result}

    def check_poe_port_power_pairs_on_signal(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "=", 2)

        result = True if parse_result == "1" else False
        return result, {"ret_mode": parse_result}

    def check_poe_port_power_pairs_on_spare(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "=", 2)

        result = True if parse_result == "2" else False
        return result, {"ret_mode": parse_result}
