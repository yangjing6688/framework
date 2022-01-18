from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as EndsystemsBase
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.ListUtils import ListUtils


class Endsystems(EndsystemsBase):
    def endsystems_select_device_by_mac_address(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "#endSystemsNavTab endSystemsGrid gridview => "
                                           ".x-grid-cell-inner:textEquals(" + str(arg_dict["mac_address"]) + ")")

        return ui_cmd_obj

    def endsystems_delete_device_by_mac_address(self, ui_cmd_obj, arg_dict):
        self.endsystems_select_device_by_mac_address(ui_cmd_obj, arg_dict)
        self.ext_builder.click(ui_cmd_obj, "#endSystemsNavTab endSystemsGrid button[text=Tools] =>"
                                           ".x-btn-inner-default-toolbar-small")
        self.ext_builder.click(ui_cmd_obj, "#endSystemsNavTab menuitem[text=Delete] => .x-menu-item-text")

        if bool(arg_dict["is_force_delete"]):
            self.ext_builder.click(ui_cmd_obj, "#deleteEndSystemsPanel checkbox[name=deleteForceCheckBox] => "
                                               ".x-form-cb-input")

        self.ext_builder.click(ui_cmd_obj, "#deleteEndSystemsPanel #deleteEndSystemsButton "
                                           "=> .x-btn-inner-blue-small")

        return ui_cmd_obj

    def endsystems_confirm_device_exists_by_ip_address(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(ui_cmd_obj, "#endSystemsNavTab endSystemsGrid",
                                         "[0].store.data.items.length")
        num_of_rows = int(ui_cmd_obj.return_data)
        if num_of_rows >= 1:
            for index in range(num_of_rows):
                self.ext_builder.component_query(ui_cmd_obj, "#endSystemsNavTab endSystemsGrid",
                                                 "[0].store.data.items[" + str(index) + "].data.ip")
                if str(arg_dict["ip_address"]) == str(ui_cmd_obj.return_data):
                    self.logger.log_debug("Device with ip address:" + str(arg_dict["ip_address"]) +
                                          " is displayed in the End-Systems grid.")
                    break
                elif index == num_of_rows - 1:
                    self.logger.log_debug("Device with ip address:" + str(arg_dict["ip_address"]) +
                                          " is not displayed in the End-Systems grid.")
                    ui_cmd_obj.error_state = True
                    break
        elif num_of_rows == 0:
            self.logger.log_debug("No device is displayed in the End-Systems grid")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def endsystems_confirm_device_exists_by_mac_address(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(ui_cmd_obj, "#endSystemsNavTab endSystemsGrid headercontainer",
                                         "[0].el.dom.innerText")
        headers = str(ui_cmd_obj.return_data).split('\n')

        self.ext_builder.component_query(ui_cmd_obj, "#endSystemsNavTab endSystemsGrid",
                                         "[0].body.dom.innerText")
        if '\n\t\n' in ui_cmd_obj.return_data:
            table_content = ui_cmd_obj.return_data.split('\n\t\n')
        else:
            table_content = ui_cmd_obj.return_data.split('\n')

        for i in range(1, len(table_content) // len(headers) + 1):
            index = i * len(headers) - 1
            if '\n' in table_content[index]:
                split_items = table_content[index].split('\n')
                table_content[index] = split_items[0]
                table_content.insert(index + 1, split_items[1])

        table_in_rows = list(ListUtils.chunk(table_content, len(headers)))

        for row in table_in_rows:
            if arg_dict["mac_address"] in row:
                self.logger.log_debug("Device with mac address:" + str(arg_dict["mac_address"]) +
                                      " is displayed in the End-Systems grid.")
                return ui_cmd_obj

        self.logger.log_debug("Device with mac address:" + str(arg_dict["mac_address"]) +
                              " is not displayed in the End-Systems grid.")
        ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def endsystems_verify_cell_display_value_in_end_systems_grid(self, ui_cmd_obj, arg_dict):
        row_dic = {}
        not_displayed = True

        if str(arg_dict["column_header"]) == 'State' or str(arg_dict["column_header"]) == 'Risk':
            self.logger.log_debug("Use keyword 'endsystems_verify_state_or_risk_in_end_systems_grid' "
                                  "to verify the display.")
            ui_cmd_obj.error_state = True

            return ui_cmd_obj

        self.ext_builder.component_query(ui_cmd_obj, "#endSystemsNavTab endSystemsGrid headercontainer",
                                         "[0].el.dom.innerText")
        headers = str(ui_cmd_obj.return_data).split('\n')

        if arg_dict["column_header"] not in headers:
            self.logger.log_debug("The entered column header is not displayed on the page")
            ui_cmd_obj.error_state = True
            return ui_cmd_obj

        self.ext_builder.component_query(ui_cmd_obj, "#endSystemsNavTab endSystemsGrid",
                                         "[0].body.dom.innerText")
        if '\n\t\n' in ui_cmd_obj.return_data:
            table_content = ui_cmd_obj.return_data.split('\n\t\n')
        else:
            table_content = ui_cmd_obj.return_data.split('\n')

        for i in range(1, len(table_content) // len(headers) + 1):
            index = i * len(headers) - 1
            if '\n' in table_content[index]:
                split_items = table_content[index].split('\n')
                table_content[index] = split_items[0]
                table_content.insert(index + 1, split_items[1])
            else:
                table_content.insert(index + 1, " ")

        table_in_rows = list(ListUtils.chunk(table_content, len(headers)))

        for row in table_in_rows:
            if arg_dict["mac_address"] in row:
                row_dic = dict(zip(headers, row))
                not_displayed = False
                break

        if not_displayed:
            self.logger.log_debug("The end-system with mac address: " + str(arg_dict["mac_address"]) +
                                  " is not displayed on the page.")
            ui_cmd_obj.error_state = True

            return ui_cmd_obj

        display_value = str(row_dic.get(str(arg_dict["column_header"]))).replace("\xc2\xa0", " ")

        if display_value == str(arg_dict["expected_value"]) or display_value.strip() == arg_dict['expected_value']:
            self.logger.log_debug("The value of column " + str(arg_dict["column_header"]) + " is displayed as: " +
                                  display_value + " which matches expectation")
        else:
            self.logger.log_debug("The value of column " + str(arg_dict["column_header"]) + " is displayed as: " +
                                  display_value + " which doesn't match expectation (" + str(
                arg_dict["expected_value"]) + ")")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def endsystems_verify_authorization_type_display_value_in_end_systems_grid(self, ui_cmd_obj, arg_dict):
        row_index = 0
        self.ext_builder.component_query(ui_cmd_obj, "#endSystemsNavTab endSystemsGrid",
                                         "[0].store.data.items.length")
        num_of_rows = int(ui_cmd_obj.return_data)
        if num_of_rows >= 1:
            for index in range(num_of_rows):
                self.ext_builder.component_query(ui_cmd_obj, "#endSystemsNavTab endSystemsGrid",
                                                 "[0].store.data.items[" + str(index) + "].data.mac")
                if str(arg_dict["mac_address"]) == str(ui_cmd_obj.return_data):
                    row_index = index
        elif num_of_rows == 0:
            self.logger.log_debug("No device is displayed in the End-Systems grid")
            ui_cmd_obj.error_state = True
            return ui_cmd_obj

        self.ext_builder.component_query(ui_cmd_obj, "#endSystemsNavTab endSystemsGrid",
                                         "[0].store.data.items[" + str(row_index) + "].data.authType")
        list_value_dbname = str(ui_cmd_obj.return_data)

        self.ext_builder.component_query(ui_cmd_obj, "#endSystemsNavTab endSystemsGrid",
                                         "[0].tableView.columns[19].listValues." + list_value_dbname)
        display_value = str(ui_cmd_obj.return_data)

        if str(arg_dict["expected_value"]) == display_value:
            self.logger.log_debug("The value of column Authorization Type is displayed as: " + display_value +
                                  "which matches expectation")
        else:
            self.logger.log_debug("The value of column Authorization Type is displayed as: " + display_value +
                                  "which doesn't match expectation")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def endsystems_verify_extended_state_display_value_in_end_systems_grid(self, ui_cmd_obj, arg_dict):
        row_index = 0
        self.ext_builder.component_query(ui_cmd_obj, "#endSystemsNavTab endSystemsGrid",
                                         "[0].store.data.items.length")
        num_of_rows = int(ui_cmd_obj.return_data)
        if num_of_rows >= 1:
            for index in range(num_of_rows):
                self.ext_builder.component_query(ui_cmd_obj, "#endSystemsNavTab endSystemsGrid",
                                                 "[0].store.data.items[" + str(index) + "].data.mac")
                if str(arg_dict["mac_address"]) == str(ui_cmd_obj.return_data):
                    row_index = index
        elif num_of_rows == 0:
            self.logger.log_debug("No device is displayed in the End-Systems grid")
            ui_cmd_obj.error_state = True
            return ui_cmd_obj

        self.ext_builder.component_query(ui_cmd_obj, "#endSystemsNavTab endSystemsGrid",
                                         "[0].store.data.items[" + str(row_index) + "].data.extendedState")
        list_value_dbname = str(ui_cmd_obj.return_data)

        self.ext_builder.component_query(ui_cmd_obj, "#endSystemsNavTab endSystemsGrid",
                                         "[0].tableView.columns[21].listValues." + list_value_dbname)
        display_value = str(ui_cmd_obj.return_data)

        if str(arg_dict["expected_value"]) == display_value:
            self.logger.log_debug("The value of column Extended State is displayed as: " + display_value +
                                  "which matches expectation")
        else:
            self.logger.log_debug("The value of column Extended State is displayed as: " + display_value +
                                  "which doesn't match expectation")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def endsystems_verify_state_or_risk_in_end_systems_grid(self, ui_cmd_obj, arg_dict):
        row_index = 0
        not_displayed = True
        dbname = 'state' if 'State' in str(arg_dict["column_header"]) else 'riskLevel'

        self.ext_builder.component_query(ui_cmd_obj, "#endSystemsNavTab endSystemsGrid",
                                         "[0].store.data.items.length")
        num_of_rows = int(ui_cmd_obj.return_data)
        if num_of_rows >= 1:
            for index in range(num_of_rows):
                self.ext_builder.component_query(ui_cmd_obj, "#endSystemsNavTab endSystemsGrid",
                                                 "[0].store.data.items[" + str(index) + "].data.mac")
                if str(arg_dict["mac_address"]) == str(ui_cmd_obj.return_data):
                    row_index = index
                    not_displayed = False
                    break

            if not_displayed:
                self.logger.log_debug("The end-system with mac address: " + str(arg_dict["mac_address"]) +
                                      " is not displayed on the page.")
                ui_cmd_obj.error_state = True

                return ui_cmd_obj

        self.ext_builder.component_query(ui_cmd_obj, "#endSystemsNavTab endSystemsGrid",
                                         "[0].store.data.items[" + str(row_index) + "].data." + dbname)

        display_value = str(ui_cmd_obj.return_data).replace(" ", "")
        expect_value = str(arg_dict["expected_value"]).upper() if dbname == "state" else \
            str(arg_dict["expected_value"]).replace(" ", "")

        if display_value == expect_value:
            self.logger.log_debug("The value of column " + str(arg_dict["column_header"]) + " is displayed as: " +
                                  display_value + " which matches expectation")
        else:
            self.logger.log_debug("The value of column " + str(arg_dict["column_header"]) + " is displayed as: " +
                                  display_value + " which doesn't match expectation (" + expect_value + ")")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj
