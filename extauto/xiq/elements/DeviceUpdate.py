import re
from extauto.xiq.defs.DeviceUpdateDefs import DeviceUpdateDefs
from extauto.common.WebElementHandler import WebElementHandler


class DeviceUpdate(DeviceUpdateDefs):

    def __init__(self):
        self.weh = WebElementHandler()

    def get_update_devices_button(self):
        return self.weh.get_element(self.update_devices_button)

    def get_update_nw_policy_and_config_checkbox(self):
        return self.weh.get_element(self.update_nw_policy_and_config_checkbox)

    def get_delta_config_update_radio(self):
        return self.weh.get_element(self.delta_config_update_radio)

    def get_complete_config_update_radio(self):
        return self.weh.get_element(self.complete_config_update_radio)

    def get_upgrade_iq_engine_checkbox(self):
        return self.weh.get_element(self.upgrade_iq_engine_checkbox)

    def get_upgrade_to_latest_version_radio(self):
        return self.weh.get_element(self.upgrade_to_latest_version_radio)

    def get_upgrade_even_if_versions_are_same_button(self):
        return self.weh.get_element(self.upgrade_even_if_versions_are_same_button)

    def get_upgrade_to_specific_version_radio(self):
        return self.weh.get_element(self.upgrade_to_specific_version_radio)

    def get_upgrade_to_specific_version_dropdown(self):
        return self.weh.get_element(self.upgrade_to_specific_version_dropdown)

    def get_xiq_upgrade_to_specific_version_dropdown(self):
        return self.weh.get_element(self.xiq_upgrade_to_specific_version_dropdown)

    def get_upgrade_to_specific_version_dropdown_option(self):
        return self.weh.get_element(self.upgrade_to_specific_version_dropdown_option)

    def get_enable_distributed_image_upgrade_checkbox(self):
        return self.weh.get_element(self.enable_distributed_image_upgrade_checkbox)

    def get_upgrade_to_specific_version_add_remove_button(self):
        return self.weh.get_element(self.upgrade_to_specific_version_add_remove_button)

    def get_upgrade_even_if_versions_same_checkbox(self):
        return self.weh.get_element(self.upgrade_even_if_versions_same_checkbox)

    def get_upgrade_even_if_versions_same_checkbox_input(self):
        return self.weh.get_element(self.upgrade_even_if_versions_same_checkbox_input)

    def get_activate_at_next_reboot_radio(self):
        return self.weh.get_element(self.activate_at_next_reboot_radio)

    def get_activate_after_radio(self):
        return self.weh.get_element(self.activate_after_radio)

    def get_activate_after_textfield(self):
        return self.weh.get_element(self.activate_after_textfield)

    def get_activate_at_time_radio(self):
        return self.weh.get_element(self.activate_at_time_radio)

    def get_activate_at_time_date_picker(self):
        return self.weh.get_element(self.activate_at_time_date_picker)

    def get_activate_at_time_date_picker_menu(self):
        return self.weh.get_element(self.activate_at_time_date_picker_menu)

    def get_activate_at_time_picker(self):
        return self.weh.get_element(self.activate_at_time_picker)

    def get_activate_at_time_picker_menu(self):
        return self.weh.get_element(self.activate_at_time_picker_menu)

    def get_save_as_defaults_button(self):
        return self.weh.get_element(self.save_as_defaults_button)

    def get_perform_update_button(self):
        return self.weh.get_element(self.perform_update_button)

    def get_time_pikcker_menu_items(self):
        menu = self.get_activate_at_time_picker_menu()
        return self.weh.get_elements(self.time_pikcker_menu_item, parent=menu)

    def get_activate_at_time_textfield(self):
        return self.weh.get_element(self.activate_at_time_textfield)

    def get_activate_at_date_textfield(self):
        return self.weh.get_element(self.activate_at_date_textfield)

    def get_latest_version(self):
        try:
            label = self.weh.get_element(self.upgrade_to_latest_version_label).text
            return re.search(r'\((.*)\)', label).group(1)
        except AttributeError:
            return -1

    def get_specific_version(self):
        try:
            label = self.weh.get_element(self.upgrade_to_specific_version_dropdown).text
            return re.search(r'-(.*)\.img', label).group(1)
        except AttributeError:
            return -1

    def get_exos_specific_version(self):
        try:
            label = self.weh.get_element(self.xiq_upgrade_to_specific_version_dropdown).text
            return re.search(r'-(\d+\.\d+\.\d+\.\d+([\-A-Za-z\d]+)?)\.?([A-Za-z_\d]+)?\.xos', label).group(1)
        except AttributeError:
            return -1

    def get_upgrade_to_specific_version_dropdown_options(self, upgrade_version):
        options = self.weh.get_elements(self.upgrade_to_specific_version_dropdown_options)
        for option in options:
            if upgrade_version in option.text:
                return option

    def get_upgrade_to_specific_version_dropdown_list(self):
        try:
            options = self.weh.get_elements(self.upgrade_to_specific_version_dropdown_options)
            return options
        except AttributeError:
            return -1

    def get_is_specific_version_dropdown_open(self):
        return self.weh.get_element(self.is_specific_version_dropdown_open)

    def get_device_update_form_error(self, row):
        return self.weh.get_element(self.device_update_form_error, row).get_attribute("title")

    def get_update_close_button(self):
        return self.weh.get_element(self.update_close_button)

    def get_update_devices_button_from_d360(self):
        return self.weh.get_element(self.update_devices_button_from_d360)

    def get_d360_close_button(self):
        return self.weh.get_element(self.update_close_button)

    def get_upgrade_IQ_engine_and_extreme_network_switch_images_checkbox_status(self):
        return self.weh.get_element(self.upgrade_IQ_engine_and_extreme_network_switch_images_checkbox).get_attribute("checked")

    def get_upgrade_IQ_engine_and_extreme_network_switch_images_checkbox(self):
        return self.weh.get_element(self.upgrade_IQ_engine_and_extreme_network_switch_images_checkbox)

    def get_perform_upgrade_if_the_versions_are_the_same_checkbox_status(self):
        return self.weh.get_element(self.perform_upgrade_if_the_versions_are_the_same_checkbox).get_attribute("checked")

    def get_config_download_options_checkbox(self):
        return self.weh.get_element(self.config_download_options_checkbox)

    def get_actions_update_version_drop_down(self):
        return self.weh.get_element(self.upgrade_specific_firmware_drop_down_button)

    def get_actions_update_version_drop_down_items(self):
        return self.weh.get_elements(self.upgrade_specific_firmware_drop_down_items)
