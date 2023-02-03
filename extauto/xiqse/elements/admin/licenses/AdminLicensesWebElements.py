from extauto.common.WebElementHandler import WebElementHandler
from xiqse.defs.admin.licenses.AdminLicensesWebElementsDefinitions import AdminLicensesWebElementsDefinitions


class AdminLicensesWebElements(AdminLicensesWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_licenses_panel_title(self):
        """
        :return: 'Licenses' panel title on the Administration> Licenses page
        """
        return self.weh.get_element(self.licenses_panel_title)

    def get_licenses_add_button(self):
        """
        :return: 'Add' button in the Licenses view on the Administration> Licenses page
        """
        return self.weh.get_element(self.licenses_add_button)

    def get_licenses_refresh_button(self):
        """
        :return: 'Refresh' button in the Licenses view on the Administration> Licenses page
        """
        return self.weh.get_element(self.licenses_refresh_button)

    def get_licenses_table_rows(self):
        """
        :return: All the rows in the Licenses  table
        """
        return self.weh.get_elements(self.licenses_table_rows)

    def get_licenses_source_column_value_for_row(self, row):
        """
        :param row:  row to obtain the data of
        :return: Source column value for the specified row in the Licenses table
        """
        return self.weh.get_element(self.licenses_source_col, parent=row)

    def get_licenses_feature_column_value_for_row(self, row):
        """
        :param row:  row to obtain the data of
        :return: Feature column value for the specified row in the Licenses table
        """
        return self.weh.get_element(self.licenses_feature_col, parent=row)

    def get_licenses_type_column_value_for_row(self, row):
        """
        :param row:  row to obtain the data of
        :return: Type column value for the specified row in the Licenses table
        """
        return self.weh.get_element(self.licenses_type_col, parent=row)

    def get_licenses_quantity_column_value_for_row(self, row):
        """
        :param row:  row to obtain the data of
        :return: Quantity column value for the specified row in the Licenses table
        """
        return self.weh.get_element(self.licenses_quantity_col, parent=row)

    def get_licenses_start_date_column_value_for_row(self, row):
        """
        :param row:  row to obtain the data of
        :return: Start Date column value for the specified row in the Licenses table
        """
        return self.weh.get_element(self.licenses_start_date_col, parent=row)

    def get_licenses_end_date_column_value_for_row(self, row):
        """
        :param row:  row to obtain the data of
        :return: End Date column value for the specified row in the Licenses table
        """
        return self.weh.get_element(self.licenses_end_date_col, parent=row)

    def get_licenses_description_column_value_for_row(self, row):
        """
        :param row:  row to obtain the data of
        :return: Description column value for the specified row in the Licenses table
        """
        return self.weh.get_element(self.licenses_description_col, parent=row)
