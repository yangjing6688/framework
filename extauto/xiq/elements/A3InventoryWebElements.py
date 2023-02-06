from extauto.xiq.defs.A3InventoryWebElementsDefs import A3InventoryWebElementsDefs
from extauto.common.WebElementHandler import WebElementHandler


class A3InventoryWebElements(A3InventoryWebElementsDefs):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_grid_rows(self):
        """
        :return: all the rows in the a3 devices grid
        """
        grid_rows = self.weh.get_elements(self.a3_devices_page_grid_rows)
        rows = []
        for row in grid_rows:
            if row.is_displayed():
                rows.append(row)
        return rows

    def get_refresh_a3_devices_page(self):
        refresh_icon = self.weh.get_element(self.a3_devices_page_refresh_button)
        return refresh_icon

    def get_status_cell(self, row):
        el = self.weh.get_element(self.devices_a3_status_green, row)
        return el.get_attribute("class")

    def get_a3_device_row_cells(self):
        return self.weh.get_elements(self.a3_device_row_cells)

    def get_a3_device_expanded_status(self):
        return self.weh.get_element(self.a3_device_expanded_status)

    def get_a3_device_row_cells_with_row(self, row):
        """
        :return: device row cell elements
        """
        return self.weh.get_element(self.a3_device_row_cells, row)

    def get_a3_device_expanded_button(self, row):
        elements = self.weh.get_elements(self.a3_device_expanded_button, row)
        print(len(elements))
        for el in elements:
            if el.is_displayed():
                return el

    def get_a3_device_host_name_cell(self, row):
        return self.weh.get_element(self.a3_device_host_name_cell, parent=row)

    def get_a3_node_grid_rows(self):
        """
        :return: all the rows in the a3 devices grid
        """
        grid_rows = self.weh.get_elements(self.a3_nodes__grid_rows)
        rows = []
        for row in grid_rows:
            if row.is_displayed():
                rows.append(row)
        return rows

    def get_go_to_a3_button(self, row):
        elements = self.weh.get_elements(self.go_to_a3_button, row)
        print(len(elements))
        for el in elements:
            if el.is_displayed():
                return el

    def get_a3_login_username_field(self):
        return self.weh.get_element(self.a3_login_username_field)

    def get_a3_login_password_field(self):
        return self.weh.get_element(self.a3_login_password_field)

    def get_a3_login_button(self):
        return self.weh.get_element(self.a3_login_button)

    def get_a3_node_go_to_a3_button(self, row):
        elements = self.weh.get_elements(self.a3_node_go_to_a3_button, parent=row)
        print(len(elements))
        for el in elements:
            if el.is_displayed():
                return el

    def get_a3_unlink_page_text(self):
        return self.weh.get_element(self.a3_unlink_page_text)
