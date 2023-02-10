from extauto.xiq.defs.SwitchWebElementsDefinitions import SwitchWebElementsDefinitions
from extauto.common.AutoActions import AutoActions
from extauto.common.Utils import Utils
from extauto.common.WebElementHandler import WebElementHandler


class SwitchWebElements(SwitchWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()
        self.auto_actions = AutoActions()
        self.utils = Utils()

    def select_drop_down_options(self, options, item):
        for opt in options:
            if opt.text.upper() == item.upper():
                self.utils.print_info("Selected opt:{}".format(opt.text))
                self.auto_actions.click(opt)
                return True

    def get_switch_port_button(self, port_number):
        """
        :return: switch ethernet button
        """
        self.switch_select_port_button['index'] = int(port_number) - 1
        return self.weh.get_element(self.switch_select_port_button)

    def get_grid_rows(self):
        """
        :return: all the rows in the devices grid
        """
        grid_rows = self.weh.get_elements(self.devices_page_grid_rows)
        if grid_rows:
            return grid_rows
        else:
            return False

    def get_switch_name(self):
        """
        :return: device select checkbox
        """
        return self.weh.get_element(self.devices_switch_name_link )

    def get_switch_port_detail_rows(self):
        """
        :return: Get Switch Ports details
        """
        return self.weh.get_elements(self.devices_switch_port_detail_rows)

    def get_switch_type_exos1(self):
        """
        :return: select Switch type EXOS
        """
        parent = self.weh.get_elements(self.switch_type_select_exos_parent)
        return self.weh.get_element(self.switch_type_select_child, parent)

    def get_switch_type_exos(self):
        """
        :return: select Switch type EXOS
        """
        return self.weh.get_element(self.switch_type_select_exos_platform)

    def get_switch_exos_serial_text_area(self):
        """
        :return: Exos switch on-boarding text area where we can enter device serial numbers
        """
        return self.weh.get_element(self.switch_exos_serial_text_area)

    def get_devices_refresh_button(self):
        """
        :return: Get devices page grid refresh button
        """
        return self.weh.get_element(self.devices_refresh_page)

    def get_devices_search_field(self):
        """
        :return: device search field
        """
        return self.weh.get_element(self.devices_search_field)

    def get_devices_search_button(self):
        """
        :return: device search button
        """
        return self.weh.get_element(self.devices_search_button)

    def get_devices_select_checkbox_field(self):
        """
        :return: device checkbox in grid
        """
        return self.weh.get_element(self.devices_select_checkbox_field)

    def get_monitor_tab(self):
        """
        :return: get Monitor Tab
        """
        return self.weh.get_element(self.get_monitor_tab_menu)

    def get_monitor_devices_tab(self):
        """
        :return: get Monitor-->devices Menu Tab
        """
        return self.weh.get_element(self.get_monitor_devices_tab_menu)

    def get_switch_type_drop_down(self):
        """
        :return:
        """
        return self.weh.get_element(self.switch_type_drop_down)

    def get_switch_type_drop_down_options(self):
        """
        :return:
        """
        return self.weh.get_elements(self.switch_type_drop_down_options)

    def get_switch_make_drop_down(self):
        """
        :return:
        """
        return self.weh.get_element(self.switch_make_drop_down)

    def get_switch_make_drop_down_options(self):
        """
        :return:
        """
        return self.weh.get_elements(self.switch_make_drop_down_options)

    def get_switch_entry_type_drop_down(self):
        """
        :return:
        """
        return self.weh.get_element(self.switch_entry_type_drop_down)

    def get_switch_entry_type_drop_down_options(self):
        """
        :return:
        """
        return self.weh.get_elements(self.switch_entry_type_drop_down_options)

    def get_switch_connection_host_details(self):
        return self.weh.get_element(self.switch_connection_host_details).text

    def get_switch_type_voss(self):
        """
        :return: switch type selection for VOSS
        """
        return self.weh.get_element(self.switch_type_select_voss_platform)

    def get_switch_voss_serial_text_area(self):
        """
        :return: VOSS switch on-boarding text area where we can enter device serial numbers
        """
        return self.weh.get_element(self.switch_voss_serial_text_area)
