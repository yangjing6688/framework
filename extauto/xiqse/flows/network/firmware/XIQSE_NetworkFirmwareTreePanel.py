from time import sleep
from common.Utils import Utils
from common.Screen import Screen
from common.AutoActions import AutoActions
from xiqse.elements.common.CommonViewWebElements import CommonViewWebElements
from xiqse.elements.network.firmware.NetworkFirmwareWebElements import NetworkFirmwareWebElements


class XIQSE_NetworkFirmwareTreePanel(NetworkFirmwareWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.view_el = CommonViewWebElements()

    def xiqse_select_firmware_type_node(self, firmware_type):
        """
         - This keyword selects the specified firmware type node on the Network > Firmware Tab
         - Keyword Usage
          - ``XIQSE Select Firmware Type Node   ${FIRMWARE_TYPE}``
          - ``XIQSE Select Firmware Type Node   DEVICE TYPE
          - ``XIQSE Select Firmware Type Node   ALL FIRMWARE

        :param firmware_type: name of firmware node to select in the tree
        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        the_node = self.get_firmware_type_node(firmware_type)
        if the_node:
            self.utils.print_info(f"Selecting {firmware_type} Tree Node...")
            self.auto_actions.click(the_node)
            ret_val = 1
            sleep(2)
        else:
            self.utils.print_info(f"Unable to select the {firmware_type} tree node")
            self.screen.save_screen_shot()
        return ret_val