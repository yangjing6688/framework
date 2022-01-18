from xiq.defs.CloudConfigGroupWebElementDefinition import *
from common.WebElementHandler import *


class CloudConfigGroupWebElements(CloudConfigGroupWebElementDefinition):

    def __init__(self):
        self.weh = WebElementHandler()

    def get_actions_add_ccg_policy(self):
        return self.weh.get_element(self.add_ccg_policy)

    def get_actions_add_ccg_button(self):
        return self.weh.get_element(self.add_ccg_policy_button)

    def get_ccg_policy_dropdown(self):
        return self.weh.get_element(self.click_select_ccg_policy)

    def get_actions_ccg_policy_drop_down_items(self):
        return self.weh.get_elements(self.dropdown_items)

    def get_actions_ccg_policy_contimue_button(self):
        return self.weh.get_element(self.click_ccg_policy_continue)

    def get_ccg_members_of_ap(self,row):
        return self.weh.get_element(self.ccg_members, row)

    def get_ccg_member_of_ap(self,row):
        ccg= self.weh.get_element(self.ccg_member, row)
        return self.weh.get_element(self.ccg_member_all, ccg)

    def get_ccg_members_arrow(self,row):
        return self.weh.get_element(self.ccg_members_arrow,parent=row)

    def get_ccg_add_button(self):
        return self.weh.get_element(self.ccg_add_button)

    def get_ccg_name_text(self):
        return self.weh.get_element(self.get_ccg_name)

    def get_ccg_description_text(self):
        return self.weh.get_element(self.get_ccg_description)

    def get_form_error_text(self):
        return self.weh.get_element(self.get_form_error)

    def get_ccg_description_manage_text(self):
        return self.weh.get_element(self.get_ccg_description_manage_page)

    def get_ccg_save_button(self):
        return self.weh.get_element(self.ccg_save_button)

    def get_ccg_cancel_button(self):
        return self.weh.get_element(self.ccg_cancel_button)

    def get_actions_ccg_policy_cancel_button(self):
        return self.weh.get_element(self.ccg_select_cancel_button)

    def get_ccg_continue_button(self):
        return self.weh.get_element(self.ccg_continue_button)

    def get_ap_hostname(self, row):
        return self.weh.get_element(self.get_device_hostname, parent=row)

    def get_ap_serial(self, row):
        return self.weh.get_element(self.get_device_serial, parent=row)

    def get_ap_remove_from_ccg(self, hostname):
        return self.weh.get_element(self.remove_device_from_ccg, parent=hostname)

    def get_ccg_ap_hostname(self):
        return self.weh.get_elements(self.get_device_ccg_hostname)

    def get_ap_select_checkbox_ccg(self,row):
        return self.weh.get_element(self.device_select_check_box_common_object, parent=row)

    def get_grid_rows(self):
        """
        :return: all the rows in the devices grid
        """
        grid_rows = self.weh.get_elements(self.ccg_page_grid_rows)
        if grid_rows:
            return grid_rows
        else:
            return False

    def edit_ccg_button_common_object(self):
        return self.weh.get_element(self.edit_ccg_button)

    def delete_ccg_button_common_object(self):
        return self.weh.get_element(self.delete_ccg_button)

    def delete_ccg_yes_confirmation_button(self):
        return self.weh.get_element(self.delete_ccg_yes_button)

    def get_ccg_grid_rows(self):
        return self.weh.get_elements(self.get_ccg_grid_row)

    def get_ccg_select_checkbox(self,row):
        return self.weh.get_element(self.ccg_select_check_box_common_object, parent=row)

    def get_ccg_row_name(self,row):
        return self.weh.get_element(self.ccg_row_name, parent=row)

    def get_ccg_members_hostname(self):
        return self.weh.get_elements(self.ccg_members_hostname)