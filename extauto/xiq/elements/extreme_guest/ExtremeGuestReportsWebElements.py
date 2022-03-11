from extauto.xiq.defs.extreme_guest.ExtremeGuestReportsWebElementsDefs import ExtremeGuestReportsWebElementsDefs
from extauto.common.WebElementHandler import *


class ExtremeGuestReportsWebElements(ExtremeGuestReportsWebElementsDefs):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_extreme_guest_manage_reports_tab(self):
        return self.weh.get_element(self.extreme_guest_manage_reports_tab)

    def get_extreme_guest_manage_reports_add_button(self):
        return self.weh.get_element(self.extreme_guest_manage_reports_add_button)

    def get_extreme_guest_manage_reports_add_report_name_field(self):
        return self.weh.get_element(self.extreme_guest_manage_reports_add_report_name_field)

    def get_extreme_guest_manage_reports_add_report_type_dropdown(self):
        return self.weh.get_element(self.extreme_guest_manage_reports_add_report_type_dropdown)

    def get_extreme_guest_manage_reports_add_report_type_dropdown_items(self):
        return self.weh.get_elements(self.extreme_guest_manage_reports_add_report_type_dropdown_items)

    def get_extreme_guest_manage_reports_add_report_scope_dropdown(self):
        return self.weh.get_element(self.extreme_guest_manage_reports_add_report_scope_dropdown)

    def get_extreme_guest_manage_reports_add_report_scope_root_name(self):
        return self.weh.get_elements(self.extreme_guest_manage_reports_add_report_scope_root_name)

    def get_extreme_guest_manage_reports_add_report_scope_city_name(self):
        return self.weh.get_elements(self.extreme_guest_manage_reports_add_report_scope_city_name)

    def get_extreme_guest_manage_reports_add_report_scope_building_name(self):
        return self.weh.get_elements(self.extreme_guest_manage_reports_add_report_scope_building_name)

    def get_extreme_guest_manage_reports_add_report_scope_floor_name(self):
        return self.weh.get_elements(self.extreme_guest_manage_reports_add_report_scope_floor_name)

    def get_extreme_guest_manage_reports_add_report_scope_root_name_expand_button(self):
        return self.weh.get_elements(self.extreme_guest_manage_reports_add_report_scope_root_name_expand_button)

    def get_extreme_guest_manage_reports_add_report_scope_city_name_expand_button(self):
        return self.weh.get_elements(self.extreme_guest_manage_reports_add_report_scope_city_name_expand_button)

    def get_extreme_guest_manage_reports_add_report_scope_building_name_expand_button(self):
        return self.weh.get_elements(self.extreme_guest_manage_reports_add_report_scope_building_name_expand_button)

    def get_extreme_guest_manage_reports_add_report_period_dropdown(self):
        return self.weh.get_element(self.extreme_guest_manage_reports_add_report_period_dropdown)

    def get_extreme_guest_manage_reports_add_report_period_dropdown_items(self):
        return self.weh.get_elements(self.extreme_guest_manage_reports_add_report_period_dropdown_items)

    def get_extreme_guest_manage_reports_add_report_format_dropdown(self):
        return self.weh.get_element(self.extreme_guest_manage_reports_add_report_format_dropdown)

    def get_extreme_guest_manage_reports_add_report_format_dropdown_items(self):
        return self.weh.get_elements(self.extreme_guest_manage_reports_add_report_format_dropdown_items)

    def get_extreme_guest_manage_reports_add_report_dashboard_name_dropdown(self):
        return self.weh.get_element(self.extreme_guest_manage_reports_add_report_dashboard_name_dropdown)

    def get_extreme_guest_manage_reports_add_report_dashboard_name_dropdown_items(self):
        return self.weh.get_elements(self.extreme_guest_manage_reports_add_report_dashboard_name_dropdown_items)

    def get_extreme_guest_manage_reports_add_report_save_button(self):
        return self.weh.get_element(self.extreme_guest_manage_reports_add_report_save_button)

    def get_extreme_guest_manage_reports_add_report_run_button(self):
        return self.weh.get_element(self.extreme_guest_manage_reports_add_report_run_button)

    def get_extreme_guest_manage_reports_add_report_save_run_button(self):
        return self.weh.get_element(self.extreme_guest_manage_reports_add_report_save_run_button)

    def get_extreme_guest_manage_reports_add_report_cancel_button(self):
        return self.weh.get_element(self.extreme_guest_manage_reports_add_report_cancel_button)

    def get_extreme_guest_manage_reports_add_report_ok_button(self):
        return self.weh.get_element(self.extreme_guest_manage_reports_add_report_ok_button)

    def get_extreme_guest_manage_reports_delete_button(self):
        return self.weh.get_element(self.extreme_guest_manage_reports_delete_button)

    def get_extreme_guest_manage_reports_grid_rows(self):
        return self.weh.get_elements(self.extreme_guest_manage_reports_grid_rows)

    def get_extreme_guest_manage_reports_grid_row_cells(self, row, field='reports', search_string=None):
        cells = self.weh.get_elements(self.extreme_guest_manage_reports_grid_row_cells, row)
        prev_cell = None
        for cell in cells:
            if search_string in cell.text:
                if field == "reports":
                    return cell
                if field == "x-grid-checkcolumn":
                    return prev_cell
            prev_cell = cell

    def get_extreme_guest_generated_reports_tab(self):
        return self.weh.get_element(self.extreme_guest_generated_reports_tab)

    def get_extreme_guest_generated_reports_grid_rows(self):
        return self.weh.get_elements(self.extreme_guest_generated_reports_grid_rows)

    def get_extreme_guest_generated_reports_grid_row_cells(self, row, field='eguest-report', search_string=None):
        cells = self.weh.get_elements(self.extreme_guest_generated_reports_grid_row_cells, row)
        prev_cell = None
        for cell in cells:
            if search_string in cell.text:
                if field == "eguest-report":
                    return cell
                if field == "x-grid-checkcolumn":
                    return prev_cell
            prev_cell = cell

    def get_extreme_guest_generated_reports_delete_button(self):
        return self.weh.get_element(self.extreme_guest_generated_reports_delete_button)