from extauto.xiq.defs.DeviceCommonDefs import DeviceCommonDefs
from extauto.common.WebElementHandler import WebElementHandler


class DeviceCommonElements(DeviceCommonDefs):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_device_grid_rows(self):
        return self.weh.get_elements(self.device_grid_rows)

    def get_device_row_select_check_box(self, row):
        return self.weh.get_element(self.device_row_select_check_box, row)

    def get_device_row_select_check_box_status(self, row):
        return self.weh.get_element(self.device_row_select_check_box_status, row)

    def get_device_table_edit_button(self):
        return self.weh.get_element(self.device_table_edit_button)

    def get_device_row_cells(self):
        return self.weh.get_elements(self.device_row_cells)

    def get_cell_href(self, cell):
        return self.weh.get_element(self.device360_cells_href, parent=cell)

    def get_device_row_cells_with_row(self, row):
        """
        :return: device row cell elements
        """
        return self.weh.get_elements(self.device_row_cells, parent=row)

    def get_manage_devices_select_all_devices_checkbox(self):
        return self.weh.get_element(self.manage_devices_select_all_devices_checkbox)

    def get_devices_per_page_value(self, device_count):
        return self.weh.get_template_element(self.devices_per_page_value, element_id=device_count)

    def get_devices_per_page_current(self):
        return self.weh.get_element(self.devices_per_page_current)

    def get_change_view_to_100_elems(self):
        return self.weh.get_elements(self.change_view_to_100_elems)

