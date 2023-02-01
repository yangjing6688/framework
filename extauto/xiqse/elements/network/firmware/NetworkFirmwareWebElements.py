from extauto.common.WebElementHandler import WebElementHandler
from xiqse.defs.network.firmware.NetworkFirmwareWebElementsDefinitions import NetworkFirmwareWebElementsDefinitions


class NetworkFirmwareWebElements(NetworkFirmwareWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_firmware_type_node(self, firmware_type="${FIRMWARE_TYPE}"):
        """
        :param firmware_type: name of the device type tree node; must be specified in switch variables
        :return: Firmware Type Node on the Network> Devices page
        """
        return self.weh.get_template_element(self.firmware_type_node, element_name=firmware_type)

    def get_all_firmware_selector(self):
        """
        :return: All Firmware item in tree
        """
        return self.weh.get_elements(self.all_firmware_selector)

    def get_device_type_firmware_selector(self):
        """
        :return: 'Device Type' element in the firmware tree
        """
        return self.weh.get_element(self.device_type_firmware_selector)

    def get_firmware_refresh_load_mask(self):
        """
        :return: load refresh mask if displayed, else None
        """
        elements = self.weh.get_elements(self.firmware_refresh_load_mask)
        return self.weh.get_displayed_element(elements)

    def get_firmware_refresh_button(self):
        """
        :return: Refresh Button on Firmware Tab
        """
        return self.weh.get_element(self.firmware_refresh_button)

    def get_firmware_upload_button(self):
        """
        :return: Upload Button on Firmware Tab
        """
        return self.weh.get_element(self.firmware_upload_button)

    def get_search_open_button(self):
        """
        :return: Button to open the Search panel on the Network > Firmware page
        """
        return self.weh.get_element(self.search_open_button)

    def get_search_text_field(self):
        """
        :return: Search field on the Network > Firmware page
        """
        return self.weh.get_element(self.search_text_field)

    def get_search_trigger_button(self):
        """
        :return: Button to perform the Search on the Network > Firmware page
        """
        return self.weh.get_element(self.search_trigger_button)

    def get_search_clear_button(self):
        """
        :return: Button to clear the Search field on the Network > Firmware page
        """
        return self.weh.get_element(self.search_clear_button)

    def get_table_rows(self):
        """
        :return: All the rows in the Firmware table
        """
        return self.weh.get_elements(self.firmware_table_rows)

    def get_assign_firmware_menu_item(self):
        """
        :return: The Assign Firmware menu item in the firmware context menu
        """
        return self.weh.get_element(self.assign_firmware_menu_item)

    def get_remove_firmware_from_group_menu_item(self):
        """
        :return: The Remove Firmware from Group menu item on the firmware context menu
        """
        return self.weh.get_element(self.remove_firmware_from_group_menu_item)

    def get_set_as_reference_image_menu_item(self):
        """
        :return: The Set as Reference Image menu item on the firmware context menu
        """
        return self.weh.get_element(self.set_as_reference_image_menu_item)

    def get_unset_as_reference_image_menu_item(self):
        """
        :return: The Unset as Reference Image menu item on the firmware context menu
        """
        return self.weh.get_element(self.unset_as_reference_image_menu_item)

    def get_delete_image_menu_item(self):
        """
        :return: The Delete Image menu item on the firmware context menu
        """
        return self.weh.get_element(self.delete_image_menu_item)
