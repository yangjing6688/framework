from extauto.common.WebElementHandler import *
from xiqse.defs.common.CommonViewWebElementsDefinitions import *
import re


class CommonViewWebElements(CommonViewWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_main_application_body(self):
        """
        :return: main application body; this is present if the user is logged into XIQSE
        """
        return self.weh.get_element(self.main_application_body)

    def get_load_mask(self):
        """
        :return: load mask if displayed, else None
        """
        elements = self.weh.get_elements(self.load_mask)
        return self.weh.get_displayed_element(elements)

    def get_dropdown_id(self, the_element):
        """
        Returns the ID for the specified dropdown element.

        :parm the_element:  dropdown element to get the ID of
        :return: ID of the specified dropdown element
        """
        the_id = -1
        if the_element:
            the_id = the_element.get_attribute("id")
            the_id = re.sub('-inputEl', '', the_id)

        return the_id

    def get_column_id(self, the_element):
        """
        Returns the ID for the specified column element.

        :parm the_element:  column element to get the ID of
        :return: ID of the specified column element
        """
        the_id = -1
        if the_element:
            the_id = the_element.get_attribute("id")
            the_id = re.sub('-textInnerEl', '', the_id)

        return the_id

    def get_div_dropdown_items(self, the_id):
        """
        Returns the dropdown items for the dropdown with the specified ID.  Assumes dropdown is a div type (uses /div).

        :param the_id: ID of the dropdown to return the items of
        :return: Dropdown items of the div type dropdown
        """
        return self.weh.get_template_elements(self.div_dropdown_items, element_id=the_id)

    def get_list_dropdown_items(self, the_id):
        """
        Returns the dropdown items for the dropdown with the specified ID.  Assumes dropdown is a list type (uses /li).

        :param the_id: ID of the dropdown to return the items of
        :return: Dropdown items of the list type dropdown
        """
        return self.weh.get_template_elements(self.list_dropdown_items, element_id=the_id)

    def get_combo_dropdown_items(self, the_id):
        """
        Returns the dropdown items for the dropdown with the specified ID.  Assumes dropdown is a comboxbox type (uses /label).

        :param the_id: ID of the dropdown to return the items of
        :return: Dropdown items of the combobox type dropdown
        """
        return self.weh.get_template_elements(self.combo_dropdown_items, element_id=the_id)
