from xiq.defs.DeviceCliAccessDefs import DeviceCliAccessDefs
from common.WebElementHandler import WebElementHandler


class DeviceCliAccessElements(DeviceCliAccessDefs):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_cli_cmd_input_field(self):
        return self.weh.get_element(self.cli_cmd_input_field)

    def get_cli_cmd_input_apply_button(self):
        return self.weh.get_element(self.cli_cmd_input_apply_button)

    def get_cli_cmd_output_field(self):
        return self.weh.get_element(self.cli_cmd_output_field)

    def get_cli_dialog_window_close_button(self):
        return self.weh.get_element(self.cli_dialog_window_close_button)

    def get_cli_device_access_list(self):
        return self.weh.get_elements(self.cli_device_access_list)

    def get_cli_command_output_error_tool_tip(self):
        return self.weh.get_element(self.cli_command_output_error_tool_tip)
