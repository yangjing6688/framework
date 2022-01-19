from xiq.defs.DeviceActionsDefs import *
from common.WebElementHandler import *


class DeviceActions(DeviceActionsDefs):

    def __init__(self):
        self.weh = WebElementHandler()

    def get_device_actions_button(self):
        """
        :return: Device Actions Button
        """
        return self.weh.get_element(self.device_actions_button)

    def get_device_actions_reboot_menu_item(self):
        """
        :return: Reboot Menu Option
        """
        return self.weh.get_element(self.device_actions_reboot_menu_item)

    def get_device_actions_revert_device_to_template_menu_item(self):
        """
        :return: Revert Device to Template Menu Option
        """
        return self.weh.get_element(self.device_actions_revert_device_to_template_menu_item)

    def get_device_actions_assign_location(self):
        # The identifier differs depending on which type of device is selected,
        # so need to get all and select the displayed element
        elements = self.weh.get_elements(self.device_actions_assign_location)
        for el in elements:
            if el.is_displayed():
                return el

    def get_assign_devices_search_box(self):
        return self.weh.get_element(self.assign_devices_search_box)

    def get_search_location_grid(self):
        return self.weh.get_elements(self.search_location_grid)

    def get_assign_location_button(self):
        return self.weh.get_element(self.assign_location_button)

    def get_assign_location_search_location(self):
        return self.weh.get_elements(self.assign_location_search_location)

    def get_assign_location_search_building(self):
        return self.weh.get_element(self.assign_location_search_building)

    def get_assign_location_search_building_expand(self):
        return self.weh.get_element(self.assign_location_search_building_expand)

    def get_assign_location_search_floors(self):
        return self.weh.get_elements(self.assign_location_search_floors)

    def get_locations_generic(self):
        return self.weh.get_elements(self.locations_generic)

    def get_locations_building(self):
        return self.weh.get_elements(self.locations_building)

    def get_locations_floors(self):
        return self.weh.get_elements(self.locations_floors)

    def get_device_actions_change_management_status(self):
        """
        :return: Reboot Menu Option
        """
        return self.weh.get_element(self.device_actions__change_management_status)

    def get_assign_location_select_button(self):
        return self.weh.get_element(self.assign_location_select_button)

    def get_device_actions_clear_audit_mismatch_menu(self):
        """
        :return: Reboot Menu Option
        """
        return self.weh.get_element(self.clear_audit_mismatch_button)

    def get_device_location_ap_node(self):
        return self.weh.get_element(self.device_location_ap_node)

    def get_device_location_floor_map_section(self):
        return self.weh.get_element(self.device_location_floor_map_section)

    def get_device_reset_yes_dialog(self):
        return self.weh.get_element(self.device_reset_dialog_yes_btn)

    def get_device_reset_close_dialog(self):
        return self.weh.get_element(self.device_reset_close_dialog)

    def get_multiple_device_reset_button(self):
        return self.weh.get_element(self.multiple_device_reset_button)

    def get_single_device_reset_button(self):
        return self.weh.get_element(self.single_device_reset_button)

    def get_device_reset_dialog_box_msg(self):
        return self.weh.get_element(self.device_reset_dialog_box_msg)

    def get_device_utilities(self):
        return self.weh.get_element(self.device_utilities)
    
    def get_device_reset_warning_msg(self):
        return self.weh.get_element(self.device_reset_warning_msg)

    def get_actions_update_version_drop_down(self):
        return self.weh.get_element(self.actions_update_version_drop_down)

    def get_actions_update_version_drop_down_items(self):
        return self.weh.get_elements(self.actions_update_version_drop_down_items)

    def get_device_actions_manage_license(self):
        return self.weh.get_element(self.device_actions_manage_license)

    def get_activate_license(self):
        return self.weh.get_element(self.activate_license)

    def get_revoke_license(self):
        return self.weh.get_element(self.revoke_license)

    def get_act_premier_btn(self):
        return self.weh.get_element(self.act_premier_btn)

    def get_act_macsec_btn(self):
        return self.weh.get_element(self.act_macsec_btn)

    def get_rev_premier_btn(self):
        return self.weh.get_element(self.rev_premier_btn)

    def get_rev_macsec_btn(self):
        return self.weh.get_element(self.rev_macsec_btn)

    def get_yes_confirmation(self):
        return self.weh.get_element(self.yes_confirmation)

