from ExtremeAutomation.Library.Device.NetworkElement.NetelemLearning.Components.Component import Component


class Port(Component):
    def __init__(self, **port_info):
        super(Port, self).__init__()

        self.type = None
        self.speed = None
        self.connector_type = None
        self.combo_port = False
        self.combo_partner = None
        self.baud_rate = None
        self.usb_version = None
        self.mac_addr = None
        self.port_string = None

        if "type" in port_info:
            self.type = port_info["type"]
        if "speed" in port_info:
            self.speed = port_info["speed"]
        if "connector_type" in port_info:
            self.connector_type = port_info["connector_type"]
        if "combo_port" in port_info:
            self.combo_port = port_info["combo_port"]
        if "combo_partner" in port_info:
            self.combo_partner = port_info["combo_partner"]
        if "baud_rate" in port_info:
            self.baud_rate = port_info["baud_rate"]
        if "usb_version" in port_info:
            self.usb_version = port_info["usb_version"]
        if "mac_addr" in port_info:
            self.mac_addr = port_info["mac_addr"]
        if "port_string" in port_info:
            self.port_string = port_info["port_string"]
