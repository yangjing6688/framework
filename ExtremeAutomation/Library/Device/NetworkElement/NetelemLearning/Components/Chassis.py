from ExtremeAutomation.Library.Device.NetworkElement.NetelemLearning.Components.Unit import Unit
from ExtremeAutomation.Library.Device.NetworkElement.NetelemLearning.Components.NetworkComponent import NetworkComponent
from ExtremeAutomation.Library.Device.NetworkElement.NetelemLearning.Components.ComponentCollection \
    import ComponentCollection


class Chassis(ComponentCollection, NetworkComponent):
    def __init__(self, **chassis_info):
        super(Chassis, self).__init__()

        self.type = None
        self.chassis_number = None
        self._valid_components = [Unit()]

        if "sku" in chassis_info:
            self.sku = chassis_info["sku"]
        if "firmware_version" in chassis_info:
            self.firmware_version = chassis_info["firmware_version"]
        if "bootloader_version" in chassis_info:
            self.bootloader_version = chassis_info["bootloader_version"]
        if "memory" in chassis_info:
            self.memory = chassis_info["memory"]
        if "operating_system" in chassis_info:
            self.operating_system = chassis_info["operating_system"]
        if "type" in chassis_info:
            self.type = chassis_info["type"]
        if "chassis_number" in chassis_info:
            self.chassis_number = chassis_info["chassis_number"]
