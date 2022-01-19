from common.WebElementHandler import *
from xiqse.defs.network.devices.tree_panel.NetworkDevicesTreePanelDeviceTypeWebElementsDefinitions import *


class NetworkDevicesTreePanelDeviceTypeWebElements(NetworkDevicesTreePanelDeviceTypeWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_device_type_node(self, device_type="${DEVICE_TYPE}"):
        """
        :param device_type: name of the device type tree node; must be specified in switch variables
        :return: Device Type Node on the Network> Devices page
        """
        return self.weh.get_template_element(self.device_type_node, element_name=device_type)
