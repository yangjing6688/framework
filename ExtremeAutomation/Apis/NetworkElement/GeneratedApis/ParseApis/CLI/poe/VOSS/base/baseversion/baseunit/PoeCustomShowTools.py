from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.poe.base.PoeBaseCustomShowTools import \
    PoeBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.NumberUtils import NumberUtils


def create_instance(device):
    return PoeCustomShowTools(device)


class PoeCustomShowTools(PoeBaseCustomShowTools):
    def __init__(self, device):
        super(PoeCustomShowTools, self).__init__(device)

    def check_poe_power_usage_threshold(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output.lower(), "threshold", 5)

        result = True if parse_result == args["threshold"] else False
        return result, {"ret_pwr_usage_threshold": parse_result}

    def check_poe_port_state(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output.lower(), args["port"], 1)

        result = True if parse_result == "enable" else False
        return result, {"ret_port_state": parse_result}

    def check_poe_port_power_limit(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output.lower(), args["port"], 4)

        result = True if parse_result == args["power_limit"] else False
        return result, {"ret_pwr_limit": parse_result}

    def check_poe_port_power_priority(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output.lower(), args["port"], 5)

        result = True if parse_result == args["power_priority"] else False
        return result, {"ret_pwr_priority": parse_result}

    def check_poe_port_measured_voltage(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output.lower(), args["port"], 1)
        parse_result = parse_result.replace(".", "")

        result = NumberUtils().verify_expected_count(parse_result, args["value_operator"], args["decivolts"])
        return result, {"ret_measured_voltage": parse_result}

    def check_poe_port_measured_current(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output.lower(), args["port"], 2)
        parse_result = parse_result.replace(".", "")

        result = NumberUtils().verify_expected_count(parse_result, args["value_operator"], args["milliamps"])
        return result, {"ret_measured_current": parse_result}

    def check_poe_port_measured_power(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output.lower(), args["port"], 3)
        parse_result = parse_result.replace(".", "")

        result = NumberUtils().verify_expected_count(parse_result, args["value_operator"], args["milliwatts"])
        return result, {"ret_measured_pwr": parse_result}

    def check_poe_port_detection_status(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output.lower(), args["port"], 2)

        result = True if parse_result == args["detect_status"] else False
        return result, {"ret_detection_status": parse_result}

    def check_poe_port_power_classification(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output.lower(), args["port"], 3)

        result = True if parse_result == args["power_class"] else False
        return result, {"ret_pwr_classification": parse_result}

    def check_poe_main_operational_status(self, *args):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_poe_main_available_power(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output.lower(), "available", 4)

        result = True if parse_result == args["power"] else False
        return result, {"ret_main_available_pwr": parse_result}

    def check_poe_main_consumption_power(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output.lower(), "consumption", 4)

        result = NumberUtils().verify_expected_count(parse_result, args["value_operator"], args["power"])
        return result, {"ret_main_consumption_pwr": parse_result}

    def check_poe_port_power_pairs_on_signal(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_poe_port_power_pairs_on_spare(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_poe_port_detect_type(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None
