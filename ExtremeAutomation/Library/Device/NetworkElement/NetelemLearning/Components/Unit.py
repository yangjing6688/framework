from ExtremeAutomation.Library.Device.NetworkElement.NetelemLearning.Components.NetworkComponent import NetworkComponent


class Unit(NetworkComponent):
    def __init__(self, **unit_info):
        super(Unit, self).__init__()

        self.type = None
        self.slot_number = None

        if "sku" in unit_info:
            self.sku = unit_info["sku"]
        if "firmware_version" in unit_info:
            self.firmware_version = unit_info["firmware_version"]
        if "bootloader_version" in unit_info:
            self.bootloader_version = unit_info["bootloader_version"]
        if "memory" in unit_info:
            self.memory = unit_info["memory"]
        if "operating_system" in unit_info:
            self.operating_system = unit_info["operating_system"]
        if "type" in unit_info:
            self.type = unit_info["type"]
        if "slot_number" in unit_info:
            self.slot_number = unit_info["slot_number"]
