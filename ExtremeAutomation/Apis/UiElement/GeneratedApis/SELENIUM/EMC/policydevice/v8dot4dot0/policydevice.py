from ExtremeAutomation.Apis.UiElement.GeneratedApis.SELENIUM.EMC.policydevice.v8dot1dot4.policydevice import \
    Policydevice as PolicydeviceBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Policydevice(PolicydeviceBase):
    def policy_device_click_port_authentication_refresh(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//a[@data-qtip='Refresh Port Authentication Data']")

        return ui_cmd_obj
