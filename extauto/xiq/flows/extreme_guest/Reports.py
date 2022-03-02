import extauto.common.CloudDriver
from time import sleep
from extauto.common.Screen import Screen
from extauto.common.Utils import Utils
from extauto.common.AutoActions import AutoActions
from extauto.xiq.flows.common.Navigator import Navigator
from extauto.xiq.elements.extreme_guest.ExtremeGuestReportsWebElements import ExtremeGuestReportsWebElements
from extauto.xiq.flows.extreme_guest.ExtremeGuest import ExtremeGuest


class Reports(object):
    def __init__(self):
        super().__init__()
        self.navigator = Navigator()
        self.driver = extauto.common.CloudDriver.cloud_driver
        self.screen = Screen()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.reports_web_elem = ExtremeGuestReportsWebElements()
        self.ext_guest = ExtremeGuest()

    def _get_extreme_guest_manage_reports_page_user_row(self, search_string):
        """
        Getting the row in Open SSID is same for all the objects
        :param search_string:
        :return:
        """
        self.utils.print_info("Getting user rows")
        self.utils.print_info(self.reports_web_elem.get_extreme_guest_manage_reports_grid_rows())
        rows = self.reports_web_elem.get_extreme_guest_manage_reports_grid_rows()
        if rows:
            for row in rows:
                self.utils.print_info(f"row: ", row)
                cell = self.reports_web_elem.get_extreme_guest_manage_reports_grid_row_cells(row, "reports",
                                                                                             search_string)
                if cell:
                    self.utils.print_info("returning rows")
                    return row

    def _select_extreme_guest_manage_page_user_row_cell(self, search_string, cell="checkbox"):
        """
        Select the passed search string object in grid rows
        :param search_string:
        :return:
        """
        row = self._get_extreme_guest_manage_reports_page_user_row(search_string)
        if row:
            if cell == "checkbox":
                self.utils.print_info("Selecting report row containing", search_string)
                self.auto_actions.click(
                    self.reports_web_elem.get_extreme_guest_manage_reports_grid_row_cells(row, 'x-grid-checkcolumn',
                                                                                          search_string))
                sleep(2)
                return 1
            elif cell == "name":
                self.utils.print_info("Clicking the report: ", search_string)
                self.auto_actions.click(
                    self.reports_web_elem.get_extreme_guest_manage_reports_grid_row_cells(row, "reports",
                                                                                          search_string))
                sleep(2)
                return 1
        return 0

    def _get_extreme_guest_generated_reports_page_user_row(self, search_string):
        """
        Getting the row in Open SSID is same for all the objects
        :param search_string:
        :return:
        """
        self.utils.print_info("Getting user rows")
        self.utils.print_info(self.reports_web_elem.get_extreme_guest_generated_reports_grid_rows())
        rows = self.reports_web_elem.get_extreme_guest_generated_reports_grid_rows()
        if rows:
            for row in rows:
                cell = self.reports_web_elem.get_extreme_guest_generated_reports_grid_row_cells(row, "eguest-report",
                                                                                                search_string)
                if cell:
                    self.utils.print_info("returning rows")
                    return row

    def _select_extreme_guest_generated_page_user_row(self, search_string, cell="checkbox"):
        """
        Select the passed search string object in grid rows
        :param search_string:
        :return:
        """
        row = self._get_extreme_guest_generated_reports_page_user_row(search_string)
        if row:
            self.utils.print_info("Selecting report row containing", search_string)
            self.auto_actions.click(
                self.reports_web_elem.get_extreme_guest_generated_reports_grid_row_cells(row, 'x-grid-checkcolumn',
                                                                                         search_string))
            sleep(2)
            return 1

    def go_to_manage_reports_tab(self):
        """
        :return:
        """
        self.ext_guest.go_to_analyze_page()
        self.utils.print_info("Clicking on Extreme Guest Manage Reports Tab")
        self.auto_actions.click(self.reports_web_elem.get_extreme_guest_manage_reports_tab())
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

    def _add_edit_manage_guest_report(self, report_name, report_type, report_format, period, dashboard_name, save_type,
                                      scope):
        """
        :param report_name:
        :param report_type:
        :param report_format:
        :param period:
        :param dashboard_name:
        :param save_type:
        :param scope:
        :return:
        """
        self.utils.print_info(
            f"report_name: {report_name}, report_type: {report_type}, report_format: {report_format}, save_type: {save_type}, scope: {scope}, period: {period}, dashboard_name: {dashboard_name}")
        if report_type:
            self.utils.print_info("Clicking report type dropdown")
            self.auto_actions.click(self.reports_web_elem.get_extreme_guest_manage_reports_add_report_type_dropdown())
            self.utils.print_info("selecting report type", report_type)
            self.auto_actions.select_drop_down_options(
                self.reports_web_elem.get_extreme_guest_manage_reports_add_report_type_dropdown_items(), report_type)
            sleep(2)
            if report_type == "Guest Visit History":
                if period:
                    self.utils.print_info("Clicking report period dropdown")
                    self.auto_actions.click(
                        self.reports_web_elem.get_extreme_guest_manage_reports_add_report_period_dropdown())
                    self.utils.print_info("selecting period", period)
                    self.auto_actions.select_drop_down_options(
                        self.reports_web_elem.get_extreme_guest_manage_reports_add_report_period_dropdown_items(),
                        period)
                    sleep(2)
                if scope:
                    self.select_scope_for_add_manage_report_page(scope)
                    sleep(1)

            elif report_type == "Dashboard Report":
                self.utils.print_info("Clicking report dashboard name dropdown")
                self.auto_actions.click(
                    self.reports_web_elem.get_extreme_guest_manage_reports_add_report_dashboard_name_dropdown())
                self.utils.print_info("selecting dashboard name", dashboard_name)
                self.auto_actions.select_drop_down_options(
                    self.reports_web_elem.get_extreme_guest_manage_reports_add_report_dashboard_name_dropdown_items(),
                    dashboard_name)
                sleep(2)

        if report_format:
            self.utils.print_info("Clicking report format dropdown")
            self.auto_actions.click(
                self.reports_web_elem.get_extreme_guest_manage_reports_add_report_format_dropdown())
            self.utils.print_info("selecting report format", report_format)
            self.auto_actions.select_drop_down_options(
                self.reports_web_elem.get_extreme_guest_manage_reports_add_report_format_dropdown_items(),
                report_format)
            sleep(2)

        if save_type == "save":
            self.utils.print_info("Clicking save button")
            self.auto_actions.click(self.reports_web_elem.get_extreme_guest_manage_reports_add_report_save_button())
            sleep(2)
            self.auto_actions.click(self.reports_web_elem.get_extreme_guest_manage_reports_add_report_ok_button())
            sleep(5)
            if self._get_extreme_guest_manage_reports_page_user_row(report_name):
                self.utils.print_info("Save successful")
                return 1
        elif save_type == "run":
            self.utils.print_info("Clicking run button")
            self.auto_actions.click(self.reports_web_elem.get_extreme_guest_manage_reports_add_report_run_button())
            sleep(2)
            self.auto_actions.click(self.reports_web_elem.get_extreme_guest_manage_reports_add_report_ok_button())
            sleep(5)
            self.utils.print_info("Clicking on Extreme Guest Generated Reports Tab")
            self.auto_actions.click(self.reports_web_elem.get_extreme_guest_generated_reports_tab())
            sleep(2)
            if self._get_extreme_guest_generated_reports_page_user_row(report_name):
                self.utils.print_info("Run successful")
                return 1
        elif save_type == "save-run":
            self.utils.print_info("Clicking save & run button")
            self.auto_actions.click(self.reports_web_elem.get_extreme_guest_manage_reports_add_report_save_run_button())
            sleep(2)
            self.auto_actions.click(self.reports_web_elem.get_extreme_guest_manage_reports_add_report_ok_button())
            sleep(5)
            if self._get_extreme_guest_manage_reports_page_user_row(report_name):
                self.utils.print_info("Save successful. Checking for Run state..")
                sleep(2)
                self.utils.print_info("Clicking on Extreme Guest Generated Reports Tab")
                self.auto_actions.click(self.reports_web_elem.get_extreme_guest_generated_reports_tab())
                sleep(2)
                if self._get_extreme_guest_generated_reports_page_user_row(report_name):
                    self.utils.print_info("Run successful")
                    return 1
        return 0

    def select_scope_for_add_manage_report_page(self, scope):
        """
        - This keyword selects a location in the Eguest Users --> Create Bulk users Vouchers Page
        - It is assumed that location is already created
        - Flow : Eguest Essentials --> More Insights --> Settings --> Users --> Add user--> Create Bulk users Vouchers
        - Keyword Usage:
         - ``Select Location For Create Bulk Vouchers Page ${LOCATION}``
        :param scope: location to select, in a comma-separated list format;
               e.g., Extreme Networks,Bangalore,Ecospace,Floor 1
        :return: 1 if location is selected, else -1'
        """
        ret_val = -1
        self.utils.print_info("Clicking Location Drop Down Button in add reports")
        self.auto_actions.click(self.reports_web_elem.get_extreme_guest_manage_reports_add_report_scope_dropdown())
        sleep(2)
        if scope:
            try:
                location_list = scope.split(',')
                location_root_name = location_list[0]
                location_generic_name = location_list[1]
                location_building_name = location_list[2]
                location_floor_name = location_list[3]

                if location_root_name:
                    self.utils.print_info("Expanding Root location: ", location_root_name)
                    location_roots = self.reports_web_elem.get_extreme_guest_manage_reports_add_report_scope_root_name()
                    for location_root in location_roots:
                        if location_root_name.strip() in location_root.text:
                            self.utils.print_info("Match found for location type Root:", location_root_name)
                            root_expand_status = location_root.get_attribute('aria-expanded')
                            if root_expand_status == "true":
                                self.utils.print_info(f"Root Location {location_root} Already Expanded")
                            else:
                                root_name_expand_button = \
                                    self.reports_web_elem.get_extreme_guest_manage_reports_add_report_scope_root_name_expand_button()
                                self.utils.print_info("Expanding the Root Location:", location_root_name)
                                self.auto_actions.click(root_name_expand_button)
                    sleep(5)

                if location_generic_name:
                    self.utils.print_info("Expanding Generic location: ", location_generic_name)
                    location_generics = \
                        self.reports_web_elem.get_extreme_guest_manage_reports_add_report_scope_city_name()
                    for location_generic in location_generics:
                        if location_generic_name.strip() in location_generic.text:
                            self.utils.print_info("Match found for location type Generic:", location_generic_name)
                            city_expand_status = location_generic.get_attribute('aria-expanded')
                            if city_expand_status == "true":
                                self.utils.print_info(f"Generic Location {location_generic_name} Already Expanded")
                            else:
                                generic_name_expand_button = \
                                    self.reports_web_elem.get_extreme_guest_manage_reports_add_report_scope_city_name_expand_button()
                                self.utils.print_info("Expanding Generic Location:", location_generic_name)
                                self.auto_actions.click(generic_name_expand_button)
                    sleep(5)

                if location_building_name:
                    location_buildings = \
                        self.reports_web_elem.get_extreme_guest_manage_reports_add_report_scope_building_name()
                    for location_building in location_buildings:
                        self.utils.print_info("Expanding Building: ", location_building_name)
                        if location_building_name.strip() in location_building.text:
                            self.utils.print_info("Match found for location type Building:", location_building_name)
                            building_expand_status = location_building.get_attribute('aria-expanded')
                            if building_expand_status == "true":
                                self.utils.print_info(f"Building Location {location_building_name} Already Expanded")
                            else:
                                building_name_expand_button = \
                                    self.reports_web_elem.get_extreme_guest_manage_reports_add_report_scope_building_name_expand_button()
                                self.utils.print_info("Expanding Building Location:", location_building_name)
                                self.auto_actions.click(building_name_expand_button)
                    sleep(5)

                if location_floor_name:
                    location_floors = self.reports_web_elem.get_extreme_guest_manage_reports_add_report_scope_floor_name()
                    for location_floor in location_floors:
                        self.utils.print_info("Selecting Floor: ", location_floor_name)
                        if location_floor_name.strip() in location_floor.text:
                            self.utils.print_info("Match found for location type Generic:", location_floor_name)
                            self.auto_actions.click(location_floor)
                            sleep(5)
                        else:
                            self.utils.print_info(f"Floor Name {location_floor_name} Not Found")
                ret_val = 1

            except Exception as e:
                self.utils.print_info(e)
                self.utils.print_info("Unable to select location")
        else:
            self.utils.print_info("Cannot select location - location not specified")

        return ret_val

    def create_extreme_guest_report(self, report_name, report_type, report_format, save_type="save", scope=None,
                                    period=None, dashboard_name=None):
        """
        :param report_name:
        :param report_type:
        :param report_format:
        :param save_type:
        :param scope:
        :param period:
        :param dashboard_name:
        :return:
        """
        self.utils.print_info(
            f"report_name: {report_name}, report_type: {report_type}, report_format: {report_format}, save_type: {save_type}, scope: {scope}, period: {period}, dashboard_name: {dashboard_name}")
        self.go_to_manage_reports_tab()
        self.utils.print_info("Click on create report button")
        self.auto_actions.click(self.reports_web_elem.get_extreme_guest_manage_reports_add_button())
        self.utils.print_info("Entering Report name", report_name)
        self.auto_actions.send_keys(self.reports_web_elem.get_extreme_guest_manage_reports_add_report_name_field(),
                                    report_name)
        return self._add_edit_manage_guest_report(report_name, report_type, report_format, period, dashboard_name,
                                                  save_type, scope)

    def delete_extreme_guest_manage_report(self, report_name):
        """
        :param report_name:
        :return:
        """
        self.go_to_manage_reports_tab()
        if self._select_extreme_guest_manage_page_user_row_cell(report_name):
            self.utils.print_info("Deleting Manage Report: ", report_name)
            self.auto_actions.click(self.reports_web_elem.get_extreme_guest_manage_reports_delete_button())
            sleep(2)
            self.utils.print_info("Clicking OK to delete")
            self.auto_actions.click(self.reports_web_elem.get_extreme_guest_manage_reports_add_report_ok_button())
            sleep(2)
            self.utils.print_info("Clicking OK")
            self.auto_actions.click(self.reports_web_elem.get_extreme_guest_manage_reports_add_report_ok_button())
            return 1
        return 0

    def delete_extreme_guest_generated_report(self, report_name):
        """
        :param report_name:
        :return:
        """
        self.go_to_generated_reports_tab()
        if self._select_extreme_guest_generated_page_user_row(report_name):
            self.utils.print_info("Deleting Generated Report: ", report_name)
            self.auto_actions.click(self.reports_web_elem.get_extreme_guest_generated_reports_delete_button())
            sleep(2)
            self.auto_actions.click(self.reports_web_elem.get_extreme_guest_manage_reports_add_report_ok_button())
            return 1
        return 0

    def go_to_generated_reports_tab(self):
        """
        :return:
        """
        self.utils.print_info("Navigating to Generated Reports Page")
        self.ext_guest.go_to_analyze_page()
        self.utils.print_info("Clicking on Extreme Guest Generated Reports Tab")
        self.auto_actions.click(self.reports_web_elem.get_extreme_guest_generated_reports_tab())
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

    def edit_extreme_guest_report(self, report_name, updated_name, report_type=None, report_format=None,
                                  save_type="save",
                                  scope=None, period=None, dashboard_name=None):
        """
        :param updated_name:
        :param scope:
        :param report_name:
        :param report_type:
        :param period:
        :param dashboard_name:
        :param report_format:
        :param save_type:
        :return:
        """
        self.go_to_manage_reports_tab()
        self.utils.print_info(f"Click on report {report_name} to edit")
        self._select_extreme_guest_manage_page_user_row_cell(report_name, "name")
        sleep(2)
        self.utils.print_info("Entering updated Report name", updated_name)
        self.auto_actions.double_click(self.reports_web_elem.get_extreme_guest_manage_reports_add_report_name_field())
        sleep(1)
        self.auto_actions.send_keys(self.reports_web_elem.get_extreme_guest_manage_reports_add_report_name_field(),
                                    updated_name)
        return self._add_edit_manage_guest_report(updated_name, report_type, report_format, period, dashboard_name,
                                                  save_type, scope)