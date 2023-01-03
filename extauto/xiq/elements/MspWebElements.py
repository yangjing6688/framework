from extauto.common.WebElementHandler import *
from extauto.xiq.defs.MspWebElementsDefinitions import *


class MspWebElements(MspWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_view_organization_button(self):
        return self.weh.get_element(self.view_organizations_button)

    def get_select_all_organizations(self):
        return self.weh.get_element(self.view_organization_select)

    def get_view_organization_close_button(self):
        return self.weh.get_element(self.view_organization_close_button)

    def get_organization_grid_rows(self):
        grid_rows = self.weh.get_elements(self.organizations_grid_rows)
        if grid_rows:
            return grid_rows
        else:
            return False

    def get_organizations_select_check_box(self):
        return self.weh.get_element(self.organizations_select_check_box)

    def get_organizations_check_box_enabled_status(self):
        return self.weh.get_element(self.organizations_check_box_enabled_status).get_attribute("checked")

    def get_paze_size_element(self, page_size='50'):
        if els := self.weh.get_elements(self.page_size_element):
            for el in els:
                if str(page_size) in el.text:
                    return el

    def get_page_numbers(self):
        return self.weh.get_elements(self.page_numbers)

    def get_next_page_element(self, page_size='10'):
        return self.weh.get_elements(self.next_page_element)

    def get_organizations_select_radio_button(self):
        return self.weh.get_element(self.organizations_select_radio_button)

    def get_organization_search_text_field(self):
        return self.weh.get_element(self.organization_search_text_field)

    def get_organization_search_icon(self):
        return self.weh.get_element(self.organization_search_icon)

    def get_organization_search_result_option(self):
        return self.weh.get_element(self.organization_search_result_option)