from extauto.xiq.defs.ApplicationsWebElementsDefs import *
from extauto.common.WebElementHandler import *


class ApplicationsWebElements(ApplicationsWebElementsDefs):

    def __init__(self):
        self.weh = WebElementHandler()

    def get_dislayed_element(self, elements):
        for el in elements:
            if el.is_displayed():
                return el

    def get_manage_applications(self):
        return self.weh.get_element(self.manage_applications)

    def get_manage_add_custom(self):
        return self.weh.get_element(self.manage_add_custom)

    def get_manage_add_custom_name_textfield(self):
        return self.weh.get_element(self.manage_add_custom_name_textfield)

    def get_manage_add_custom_add_app(self):
        return self.weh.get_element(self.manage_add_custom_add_app)

    def get_manage_add_custom_group_name_textfield(self):
        return self.weh.get_element(self.manage_add_custom_group_name_textfield)

    def get_manage_add_custom_group_name_save(self):
        return self.weh.get_element(self.manage_add_custom_group_name_save)

    def get_manage_add_custom_app_save(self):
        return self.weh.get_element(self.manage_add_custom_app_save)

    def get_manage_add_custom_tooltip_text(self):
        return self.weh.get_element(self.manage_add_custom_tooltip_text)

    def get_manage_add_custom_app_search(self):
        return self.weh.get_element(self.manage_add_custom_app_search)

    def get_manage_add_custom_search_text(self):
        return self.weh.get_element(self.manage_add_custom_search_text)

    def get_manage_apps_cell(self):
        return self.weh.get_element(self.manage_apps_cell)

    def get_manage_add_custom_edit(self):
        return self.weh.get_element(self.manage_add_custom_edit)

    def get_manage_add_custom_delete(self):
        return self.weh.get_element(self.manage_add_custom_delete)

    def get_manage_add_custom_delete_confirm(self):
        return self.weh.get_element(self.manage_add_custom_delete_confirm)

    def get_application_dialogbox_close_button(self):
        return self.weh.get_element(self.application_dialogbox_close_button)

    def get_application_dialogbox_close_tab(self):
        return self.weh.get_element(self.application_dialogbox_close_tab)