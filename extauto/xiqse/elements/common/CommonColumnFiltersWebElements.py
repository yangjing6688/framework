from extauto.common.WebElementHandler import *
from xiqse.defs.common.CommonColumnFiltersWebElementsDefinitions import CommonColumnFiltersWebElementsDefinitions


class CommonColumnFiltersWebElements(CommonColumnFiltersWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_column_filters_dialog(self):
        """
        :return: Column Filters dialog
        """
        return self.weh.get_element(self.column_filters_dialog)

    def get_column_filters_dialog_add_filter_dropdown_trigger(self):
        """
        :return: Add Filter drop down trigger arrow in the Column Filters dialog
        """
        return self.weh.get_element(self.column_filters_dialog_add_filter_dropdown_trigger)

    def get_column_filters_dialog_add_filter_dropdown(self):
        """
        :return: Add Filter drop down field in the Column Filters dialog
        """
        return self.weh.get_element(self.column_filters_dialog_add_filter_dropdown)

    def get_column_filters_dialog_filter_panel(self, name):
        """
        :param name: name of the filter to get the filter panel for
        :return: filter panel for the specified filter
        """
        return self.weh.get_template_element(self.column_filters_dialog_filter_panel, element_name=name)

    def get_column_filters_dialog_filter_text_field(self, name):
        """
        :param name: name of the filter to get the text field for
        :return: text field for the specified filter
        """
        return self.weh.get_template_element(self.column_filters_dialog_filter_text_field, element_name=name)

    def get_column_filters_dialog_filter_radio_field(self, name, value):
        """
        :param name: name of the filter to get the field for
        :param value: value of the radio button to return
        :return: radio button for the specified filter
        """
        return self.weh.get_template_element(self.column_filters_dialog_filter_radio_field,
                                             element_name=name, element_value=value)

    def get_column_filters_dialog_filter_checkbox_field(self, name, value):
        """
        :param name: name of the filter to get the field for
        :param value: value of the checkbox to return
        :return: checkbox for the specified filter
        """
        return self.weh.get_template_element(self.column_filters_dialog_filter_checkbox_field,
                                             element_name=name, element_value=value)

    def get_column_filters_dialog_remove_filter_button(self, name):
        """
        :param name: name of the filter to get the remove filter button for
        :return: remove filter button for the specified filter
        """
        return self.weh.get_template_element(self.column_filters_dialog_remove_filter_button, element_name=name)

    def get_column_filters_dialog_close_button(self):
        """
        :return: Close button in the Column Filters dialog
        """
        return self.weh.get_element(self.column_filters_dialog_close_button)
