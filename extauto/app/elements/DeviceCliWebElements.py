from extauto.app.defs.DeviceCliDefinitions import DeviceCliDefinitions
from extauto.common.AutoActions import AutoActions
from extauto.common.WebElementHandler import WebElementHandler


class DeviceCliWebElements(DeviceCliDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()
        self.auto_actions = AutoActions()

    def get_device_cli(self):
        return self.weh.get_element(self.device_cli_id)

    def get_device_cli_search_field(self):
        return self.weh.get_element(self.device_cli_command_entry_id)

    def get_device_cli_apply_button(self):
        return self.weh.get_element(self.device_cli_apply_id)

    def get_device_cli_exit(self):
        return self.weh.get_element(self.device_cli_exit_id)

    def get_device_cli_text(self):
        try:
            cli_cmd = self.weh.get_element(self.device_cli_text_id)
            if cli_cmd.is_displayed():
                return cli_cmd.text
            else:
                return "None"
        except Exception:
            return "None"
