from ExtremeAutomation.Apis.UiElement.GeneratedApis.SELENIUM.EMC.firmware.v8dot3dot0.firmware import Firmware as \
    FirmwareBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Firmware(FirmwareBase):
    def firmware_dialog_restart_click_cancel(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#ResetDeviceWindow button[text=Close] => .x-btn-inner-default-small')

        return ui_cmd_obj

    def firmware_dialog_upgrade_click_cancel(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#firmwareDownloadWindow button[name=finishFirmBtn] => '
                                           '.x-btn-inner-default-small')

        return ui_cmd_obj
