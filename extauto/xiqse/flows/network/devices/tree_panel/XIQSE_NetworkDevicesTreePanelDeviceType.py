from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.elements.common.CommonViewWebElements import CommonViewWebElements
from xiqse.elements.network.devices.tree_panel.NetworkDevicesTreePanelDeviceTypeWebElements import NetworkDevicesTreePanelDeviceTypeWebElements


class XIQSE_NetworkDevicesTreePanelDeviceType(NetworkDevicesTreePanelDeviceTypeWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.view_el = CommonViewWebElements()
        #self.select_device_type = XIQSE_NetworkDevicesTreePanelDeviceType()

    def xiqse_select_device_type_node(self, device_type):
        """
        - This keyword selects the specified device type node on the Network> Devices Tab
        - Keyword Usage
        - ``XIQSE Devices Select Device Type Node   ${DEVICE_TYPE}``

        :param device_type: name of device type node to select
        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        the_node = self.get_device_type_node(device_type)
        if the_node:
            self.utils.print_info(f"Selecting {device_type} Tree Node...")
            self.auto_actions.click(the_node)
            ret_val = 1
            sleep(2)
        else:
            self.utils.print_info(f"Unable to select the {device_type} tree node")
            self.screen.save_screen_shot()
        return ret_val