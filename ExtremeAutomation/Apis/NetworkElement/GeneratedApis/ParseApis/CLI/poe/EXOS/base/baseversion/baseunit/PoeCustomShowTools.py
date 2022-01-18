from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.poe.base.PoeBaseCustomShowTools import \
    PoeBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


class PoeCustomShowTools(PoeBaseCustomShowTools):
    def __init__(self, device):
        super(PoeCustomShowTools, self).__init__(device)

    def check_poe_power_usage_threshold(self, output, args, **kwargs):

        output = output.replace("\n", "\r\n")

        if self.pw.is_exact_string_present_in_output(output, '{} percent'.format(args['threshold'])):
            return True, None
        return False, None

    def check_poe_port_state(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_poe_port_power_limit(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_poe_port_power_priority(self, output, args, **kwargs):

        output = output.replace("\n", "\r\n")

        if self.pw.is_exact_string_present_in_output(output, args['power_priority']):
            return True, None
        return False, None

    def check_poe_port_detect_type(self, output, args, **kwargs):

        output = output.replace("\n", "\r\n")

        if self.pw.is_exact_string_present_in_output(output, args['detect_type']):
            return True, None
        return False, None

    def check_poe_port_measured_voltage(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_poe_port_measured_current(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_poe_port_measured_power(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_poe_port_detection_status(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_poe_port_power_classification(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_poe_port_power_pairs_on_signal(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_poe_port_power_pairs_on_spare(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_poe_main_operational_status(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_poe_main_available_power(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_poe_main_consumption_power(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_inline_power_disabled(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_inline_power_enabled(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_poe_inline_power_disabled(self, output, args, **kwargs):

        output = output.replace("\n", "\r\n")

        if self.pw.is_exact_string_present_in_output(output, args['disabled']):
            return True, None
        return False, None

    def check_poe_inline_power_enabled(self, output, args, **kwargs):

        output = output.replace("\n", "\r\n")

        if self.pw.is_exact_string_present_in_output(output, args['enabled']):
            return True, None
        return False, None

    def check_poe_inline_power(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_poe_inline_power_port_info(self, output, args, **kwargs):

        output = output.replace("\n", "\r\n")

        if self.pw.is_exact_string_present_in_output(output, args['search_value']):
            return True, None
        return False, None

    def check_poe_inline_power_config_port(self, output, args, **kwargs):

        output = output.replace("\n", "\r\n")

        if args['search_value'] in output:
            if args['search_value_exist']:
                return True, None

        if not args['search_value_exist']:
            return True, None

        return False, None

    def check_poe_inline_power_disconnect_deny_port(self, output, args, **kwargs):

        output = output.replace("\n", "\r\n")

        if self.pw.is_exact_string_present_in_output(output, args['search_value']):
            return True, None

    def check_poe_inline_power_disconnect_lowest_priority(self, output, args, **kwargs):

        output = output.replace("\n", "\r\n")

        if self.pw.is_exact_string_present_in_output(output, args['search_value']):
            return True, None

    def check_poe_inline_power_disconnect_unconfigure(self, output, args, **kwargs):

        output = output.replace("\n", "\r\n")

        if self.pw.is_exact_string_present_in_output(output, args['search_value']):
            return True, None

    def check_poe_inline_power_label(self, output, args, **kwargs):

        output = output.replace("\n", "\r\n")

        if self.pw.is_exact_string_present_in_output(output, args['test_label']):
            return True, None

        return False, None

    def check_poe_inline_power_operator_limit(self, output, args, **kwargs):

        output = output.replace("\n", "\r\n")

        if self.pw.is_exact_string_present_in_output(output, "{} mW".format(args['operator_limit'])):
            return True, None

        return False, None

    def check_poe_inline_power_operator_limit_off_the_range(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None
