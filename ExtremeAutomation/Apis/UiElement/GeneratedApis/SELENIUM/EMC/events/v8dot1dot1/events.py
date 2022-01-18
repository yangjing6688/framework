from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as EventsBase
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils
import math
import time


class Events(EventsBase):

    def events_set_time_span(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Events, self).events_set_time_span(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def events_set_event_types(self, ui_cmd_obj, arg_dict):
        max_attempts = 3
        attempts = 0
        while attempts <= max_attempts:
            # Clear any existing selections in the Type drop down
            self.ext_builder.click(ui_cmd_obj,
                                   '#alarmsEventsTabPanel multicombobox[name=eventCategoryId] => .x-form-clear-trigger')

            # Open the Type drop down
            self.ext_builder.click(ui_cmd_obj,
                                   '#alarmsEventsTabPanel multicombobox[name=eventCategoryId] => .x-form-arrow-trigger')

            # Split the comma-separated list of event types and select each one in the Type drop down
            event_type_list = str(arg_dict['event_types']).split(",")
            for event_type in event_type_list:
                # Make sure the specified event type exists in the drop down
                ui_cmd_obj = self.ext_builder.is_item_in_component(ui_cmd_obj,
                                                                   '#alarmsEventsTabPanel '
                                                                   'multicombobox[name=eventCategoryId]', '[0]',
                                                                   'eventType', event_type)
                # Select the item if it is present
                if ui_cmd_obj.return_data is True:
                    next_item_in_list = ''
                    self.ext_builder.component_query(ui_cmd_obj,
                                                     "#alarmsEventsTabPanel multicombobox[name=eventCategoryId]",
                                                     '[0].store.data.items.length')
                    table_length = ui_cmd_obj.return_data
                    item = 0
                    while item < table_length:
                        self.ext_builder.component_query(ui_cmd_obj,
                                                         "#alarmsEventsTabPanel multicombobox[name=eventCategoryId]",
                                                         '[0].store.data.items[' + str(item) + '].data.eventType')
                        if event_type.lower() == ui_cmd_obj.return_data.lower():
                            item += 1
                            self.ext_builder.component_query(ui_cmd_obj, "#alarmsEventsTabPanel "
                                                                         "multicombobox[name=eventCategoryId]",
                                                             '[0].store.data.items[' + str(item) + '].data.eventType')
                            next_item_in_list = ui_cmd_obj.return_data
                            break
                        else:
                            item += 1
                    self.ext_builder.move_cursor(ui_cmd_obj,
                                                 '#alarmsEventsTabPanel multicombobox[name=eventCategoryId] boundlist '
                                                 '=> :textEquals(' + next_item_in_list + ')')
                    self.ext_builder.click(ui_cmd_obj,
                                           '#alarmsEventsTabPanel multicombobox[name=eventCategoryId] boundlist '
                                           '=> :textEquals(' + event_type + ')')
                else:
                    self.logger.log_info("\nCould not find event type '" + event_type + "' in Type dropdown.\n")
                    ui_cmd_obj.error_state = True

            # Close the Type drop down
            self.ext_builder.click(ui_cmd_obj,
                                   '#alarmsEventsTabPanel multicombobox[name=eventCategoryId] => .x-form-arrow-trigger')

            if ui_cmd_obj.error_state is True:
                self.ext_builder.click(ui_cmd_obj, '#ok => .x-btn-inner-blue-small')
                ui_cmd_obj.error_state = False
                attempts += 1
            else:
                return ui_cmd_obj
        ui_cmd_obj.error_state = True
        return ui_cmd_obj

    def events_click_next_page(self, ui_cmd_obj, arg_dict):
        self.click_paging_button(ui_cmd_obj, "#next")
        return ui_cmd_obj

    def events_click_prev_page(self, ui_cmd_obj, arg_dict):
        self.click_paging_button(ui_cmd_obj, "#prev")
        return ui_cmd_obj

    def events_click_first_page(self, ui_cmd_obj, arg_dict):
        self.click_paging_button(ui_cmd_obj, "#first")
        return ui_cmd_obj

    def events_click_last_page(self, ui_cmd_obj, arg_dict):
        self.click_paging_button(ui_cmd_obj, "#last")
        return ui_cmd_obj

    def events_click_reset(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#alarmsEventsTabPanel panel[title=Events] eventLogGrid pagingtoolbar '
                               'button[text=Reset] => .x-btn-icon-el')

        return ui_cmd_obj

    def events_set_column_filter(self, ui_cmd_obj, arg_dict):
        col_name = arg_dict['col_name']
        col_id = "text=" + col_name
        filter_type = "text"

        # Determine the column identifier and filter_type
        if col_name == "Information":
            col_id = "stateId=console_message"
        elif col_name == "Subcomponent":
            # This column exists in both the alarms and events tables, so need a unique identifier
            col_id = "stateId=console_subComponent"
        elif col_name == "Source":
            # This column exists in both alarms and events tables, so need a unique identifier
            col_id = "colId=sourceDisplayString"
        elif col_name == "Severity":
            # This column exists in both alarms and events tables, so need a unique identifier
            col_id = "stateId=console_severity"
            filter_type = "checkbutton"

        # Make sure the column exists
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      '#alarmsEventsTabPanel gridcolumn[' + col_id + ']', '[0]')
        if ui_cmd_obj.return_data is not None:
            # Access the column menu's filter option
            self.ext_builder.move_cursor(ui_cmd_obj,
                                         '#alarmsEventsTabPanel gridcolumn[' + col_id + '] => .x-column-header-text')
            self.ext_builder.click(ui_cmd_obj,
                                   '#alarmsEventsTabPanel gridcolumn[' + col_id + '] => .x-column-header-trigger')
            self.ext_builder.click(ui_cmd_obj, '#filters => .x-menu-item-text')

            # Enter the filter value based on what type of input is accepted
            if filter_type == "text":
                ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, '#filters textfield[inputType=text]', '[0]')
                if ui_cmd_obj.return_data is not None:
                    self.ext_builder.click(ui_cmd_obj, '#filters textfield[inputType=text] => .x-form-text')
                    self.ext_builder.enter_text_no_target(ui_cmd_obj, str(arg_dict['the_filter']))
                else:
                    self.logger.log_info("\nCould not find filter text field.\n")
            elif filter_type == "checkbutton":
                filter_list = str(arg_dict['the_filter']).split(",")
                for filter_val in filter_list:
                    ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                                  '#filters menucheckitem[text=' + filter_val + ']',
                                                                  '[0]')
                    if ui_cmd_obj.return_data is not None:
                        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                                      '#filters menucheckitem[text=' + filter_val + ']',
                                                                      '[0].checked')
                        if ui_cmd_obj.return_data is False:
                            self.ext_builder.click(ui_cmd_obj,
                                                   '#filters menucheckitem[text=' + filter_val + '] => '
                                                   '.x-menu-item-icon')
                        else:
                            self.logger.log_info("\nCheck button '" + filter_val + "' is already selected.\n")
                    else:
                        self.logger.log_info("\nCould not find check button for '" + filter_val + "'.\n")
                        ui_cmd_obj.error_state = True
            else:
                self.logger.log_info("\nUnknown filter type '" + filter_type + "'\n")
                ui_cmd_obj.error_state = True

            # Close the column menu by clicking on the toolbar
            self.ext_builder.click(ui_cmd_obj, '#alarmsEventsTabPanel eventLogGrid toolbar(true) => .x-scroller')
        else:
            self.logger.log_info("\nCould not find column '" + col_name + "'.\n")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def events_enable_column_filter(self, ui_cmd_obj, arg_dict):
        self.set_column_filter_state(ui_cmd_obj, arg_dict, True)
        return ui_cmd_obj

    def events_disable_column_filter(self, ui_cmd_obj, arg_dict):
        self.set_column_filter_state(ui_cmd_obj, arg_dict, False)
        return ui_cmd_obj

    def events_clear_column_filter(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Events, self).events_clear_column_filter(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def events_set_table_filter(self, ui_cmd_obj, arg_dict):
        # Click on the search/magnifying glass icon
        self.ext_builder.click(ui_cmd_obj,
                               '#alarmsEventsTabPanel panel[title=Events] eventLogGrid '
                               'button[iconCls=x-form-search-trigger] => .x-btn-icon-el')

        # Enter the string to search for
        self.ext_builder.enter_text(ui_cmd_obj, arg_dict['the_value'],
                                    '#alarmsEventsTabPanel textfield(true) => .x-form-text')

        # Click the magnifying glass to initiate the search
        self.ext_builder.click(ui_cmd_obj, '#alarmsEventsTabPanel textfield(true) => .x-form-search-trigger')

        # Wait for the action to complete
        self.ext_builder.wait_for_load_mask(ui_cmd_obj, 'loadmask[msg=Loading...]', '[0]', 60)

        return ui_cmd_obj

    def events_clear_table_filter(self, ui_cmd_obj, arg_dict):
        # Click the 'X' in the search box to clear the text
        self.ext_builder.click(ui_cmd_obj,
                               '#alarmsEventsTabPanel eventLogGrid textfield(true) => .x-form-clear-trigger')

        # Wait for the action to complete
        self.ext_builder.wait_for_load_mask(ui_cmd_obj, 'loadmask[msg=Loading...]', '[0]', 60)

        return ui_cmd_obj

    def events_select_event(self, ui_cmd_obj, arg_dict):
        # Give the view time to update
        self.ext_builder.delay(ui_cmd_obj, 1000)

        # Determine if the item is visible in the table
        ui_cmd_obj = self.ext_builder.is_item_in_component(ui_cmd_obj, '#alarmsEventsTabPanel eventLogGrid',
                                                           '[0]', 'message', arg_dict['the_value'], exact_match=False)
        if ui_cmd_obj.return_data is True:
            # Select the item
            self.ext_builder.select_table_row_by_attr(ui_cmd_obj, '#alarmsEventsTabPanel eventLogGrid',
                                                      '[0]', 'message', arg_dict['the_value'], exact_match=False)
        else:
            self.logger.log_info("\nCould not find item '" + arg_dict['the_value'] + "' in table.\n")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def events_confirm_event_message_contains(self, ui_cmd_obj, arg_dict):
        # Make sure the event table is accessible
        self.ext_builder.component_query(ui_cmd_obj, '#alarmsEventsTabPanel eventLogGrid gridview', '[0]')
        if ui_cmd_obj.return_data is not None:
            found_item = False

            # Make sure we are starting on the first page
            self.click_paging_button(ui_cmd_obj, "#first")

            # Split the comma-separated event strings to look for into a list
            the_events = str(arg_dict['event_str_list']).split(",")

            # Determine the number of pages to loop through
            page_num = 1
            num_pages = self.get_num_pages(ui_cmd_obj)
            max_pages = int(arg_dict['max_pages'])
            if max_pages != 0 and max_pages < num_pages:
                # A max number of pages was specified, and it is less than the total number of pages,
                # so only loop for the max page count
                num_pages = max_pages
                self.logger.log_debug("\nSetting number of pages to max pages: '" + str(num_pages) + "'\n")

            # Loop through the event table pages until we find an event which contains all of the specified strings
            # in the Information column ("message" attribute)
            while page_num <= num_pages:
                found_on_page = False
                self.logger.log_debug("\nLooping through each page;  current page is '" + str(page_num) + "'\n")

                # Determine the number of items
                ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, '#alarmsEventsTabPanel eventLogGrid gridview',
                                                              '[0].store.data.length')

                # Loop through the items in the table and query each row's event message
                row_index = 0
                total_rows = ui_cmd_obj.return_data
                while row_index < total_rows:
                    ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                                  '#alarmsEventsTabPanel eventLogGrid gridview',
                                                                  '[0].store.data.items[' + str(row_index) +
                                                                  '].data.message')
                    check_message = ui_cmd_obj.return_data
                    self.logger.log_debug("\nChecking event with message '" + check_message + "'\n")
                    # Loop through each of the string we want this message to contain
                    for check_str in the_events:
                        if check_str not in check_message:
                            self.logger.log_debug("\nThe event message did not contain '" + check_str + "'\n")
                            found_on_page = False
                            # Break out of the event string loop since this string was not found
                            break
                        else:
                            self.logger.log_debug("\nThe event message contains '" + check_str + "'\n")
                            found_on_page = True

                    # Determine if we have found the item or if we need to continue
                    if found_on_page is True:
                        found_item = True
                        # Break out of the table row loop since we found a matching row
                        break
                    else:
                        # Continue on with the next row
                        row_index += 1

                # Determine if we found an item on this page or if we need to check the next page
                if found_item is True:
                    self.logger.log_debug("\nFound a match on page " + str(page_num) + "\n")
                    # Break out of the paging loop since we found the item on this page
                    break
                else:
                    # Continue searching on the next page
                    self.click_paging_button(ui_cmd_obj, "#next")
                    page_num += 1

            # Determine if the test passed or failed
            if found_item is True:
                self.logger.log_info("\nFound an event whose Information column contains all strings in '" +
                                     arg_dict['event_str_list'] + "'\n")
                if StringUtils.string_to_boolean(arg_dict['exists']) is False:
                    # We found an item but weren't expecting to, so fail the test
                    ui_cmd_obj.error_state = True
            else:
                self.logger.log_info("\nDid not find an event whose Information column contains all strings in '" +
                                     arg_dict['event_str_list'] + "'\n")
                if StringUtils.string_to_boolean(arg_dict['exists']) is True:
                    # We did not find an item but were expecting to, so fail the test
                    ui_cmd_obj.error_state = True
        else:
            self.logger.log_info("Could not find Events table")

        return ui_cmd_obj

    def events_confirm_event_exists(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#alarmsEventsTabPanel eventLogGrid button[iconCls=x-form-search-trigger] => '
                               '.x-btn-icon-el')
        self.ext_builder.click(ui_cmd_obj,
                               '#alarmsEventsTabPanel eventLogGrid textfield(true) => .x-form-text')
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['event_title']),
                                    '#alarmsEventsTabPanel eventLogGrid textfield(true) => .x-form-text')
        self.ext_builder.click(ui_cmd_obj,
                               '#alarmsEventsTabPanel eventLogGrid textfield(true) => .x-form-search-trigger')
        self.ext_builder.delay(ui_cmd_obj, '5000')
        attempts = 0
        iterate_length = 0
        match = False
        while attempts <= int(arg_dict['max_attempts']):
            self.ext_builder.component_query(ui_cmd_obj, '[stateId=console]', '[0].store.data.length')
            total_length = int(ui_cmd_obj.return_data)
            while iterate_length < total_length:
                if match is True:
                    self.ext_builder.click(ui_cmd_obj,
                                           '#alarmsEventsTabPanel eventLogGrid textfield(true) => '
                                           '.x-form-clear-trigger')
                    return ui_cmd_obj
                self.ext_builder.component_query(ui_cmd_obj, '[stateId=console]', '[0].store.data.items[' +
                                                 str(iterate_length) + '].data.webEventTitle')
                if arg_dict['event_title'] == ui_cmd_obj.return_data:
                    self.ext_builder.component_query(ui_cmd_obj, '[stateId=console]',
                                                     '[0].store.data.items[' + str(iterate_length) + '].data.message')
                    if arg_dict['event_information'] in ui_cmd_obj.return_data:
                        self.ext_builder.component_query(ui_cmd_obj, '[stateId=console]',
                                                         '[0].store.data.items[' +
                                                         str(iterate_length) + '].data.deviceIdentifier')
                        if arg_dict['event_ip'] == ui_cmd_obj.return_data:
                            match = True
                            break
                        else:
                            iterate_length += 1
                    else:
                        iterate_length += 1
                else:
                    iterate_length += 1

            attempts += 1
            if match is True:
                self.ext_builder.click(ui_cmd_obj,
                                       '#alarmsEventsTabPanel eventLogGrid textfield(true) => .x-form-clear-trigger')
                return ui_cmd_obj
        ui_cmd_obj.error_state = True
        self.ext_builder.click(ui_cmd_obj,
                               '#alarmsEventsTabPanel eventLogGrid textfield(true) => .x-form-clear-trigger')

        return ui_cmd_obj

    def events_confirm_event_event(self, ui_cmd_obj, arg_dict):
        item = 0
        self.ext_builder.component_query(ui_cmd_obj, '#alarmsEventsTabPanel eventLogGrid gridview',
                                         '[0].dataSource.data.length')
        table_size = ui_cmd_obj.return_data
        while item <= table_size:
            self.ext_builder.component_query(ui_cmd_obj, '#alarmsEventsTabPanel eventLogGrid gridview',
                                             '[0].dataSource.data.items[' + str(item) + '].data.webEventTitle')
            if ui_cmd_obj.return_data == arg_dict['event']:
                return ui_cmd_obj
            else:
                item += 1
        ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def events_confirm_event_event_and_information(self, ui_cmd_obj, arg_dict):
        item = 0
        attempts = 0
        while attempts <= arg_dict['max_attempts']:
            if arg_dict['number_events_to_check'] == 0:
                self.ext_builder.component_query(ui_cmd_obj, '#alarmsEventsTabPanel eventLogGrid gridview',
                                                 '[0].dataSource.data.length')
                table_size = ui_cmd_obj.return_data
            else:
                table_size = arg_dict['number_events_to_check']
            while item <= table_size:
                self.ext_builder.component_query(ui_cmd_obj, '#alarmsEventsTabPanel eventLogGrid gridview',
                                                 '[0].dataSource.data.items[' + str(item) + '].data.webEventTitle')
                if ui_cmd_obj.return_data == arg_dict['event']:
                    self.ext_builder.component_query(ui_cmd_obj, '#alarmsEventsTabPanel eventLogGrid gridview',
                                                     '[0].dataSource.data.items[' + str(item) + '].data.message')
                    if arg_dict['information'] in ui_cmd_obj.return_data:
                        return ui_cmd_obj
                else:
                    item += 1
            time.sleep(1)
            attempts += 1
        ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def events_confirm_event_event_information_and_source(self, ui_cmd_obj, arg_dict):
        item = 0
        attempts = 0
        match = False
        while attempts <= int(arg_dict['max_attempts']) and not match:
            if int(arg_dict['number_events_to_check']) == 0:
                self.ext_builder.component_query(ui_cmd_obj, '#alarmsEventsTabPanel eventLogGrid gridview',
                                                 '[0].dataSource.data.length')
                table_size = ui_cmd_obj.return_data
            else:
                table_size = arg_dict['number_events_to_check']
            while item <= int(table_size) and not match:
                match = True
                if arg_dict['event'] is not None:
                    self.ext_builder.component_query(ui_cmd_obj, '#alarmsEventsTabPanel eventLogGrid gridview',
                                                     '[0].dataSource.data.items[' + str(item) + '].data.webEventTitle')
                    if arg_dict['event'] != ui_cmd_obj.return_data:
                        match = False
                        item += 1
                        continue
                if arg_dict['information'] is not None:
                    self.ext_builder.component_query(ui_cmd_obj, '#alarmsEventsTabPanel eventLogGrid gridview',
                                                     '[0].dataSource.data.items[' + str(item) + '].data.message')
                    if arg_dict['information'] not in ui_cmd_obj.return_data:
                        match = False
                        item += 1
                        continue
                if arg_dict['source'] is not None:
                    self.ext_builder.component_query(ui_cmd_obj, '#alarmsEventsTabPanel eventLogGrid gridview',
                                                     '[0].dataSource.data.items[' + str(item) +
                                                     '].data.deviceIdentifier')
                    if arg_dict['source'] != ui_cmd_obj.return_data:
                        match = False
                        item += 1
                        continue

            attempts += 1
            item = 0
        if match != StringUtils.string_to_boolean(arg_dict['exists']):
            ui_cmd_obj.error_state = True
            item = 0
            if int(arg_dict['number_events_to_check']) == 0:
                self.ext_builder.component_query(ui_cmd_obj, '#alarmsEventsTabPanel eventLogGrid gridview',
                                                 '[0].dataSource.data.length')
                table_size = ui_cmd_obj.return_data
            else:
                table_size = arg_dict['number_events_to_check']
            while item <= int(table_size):
                self.ext_builder.component_query(ui_cmd_obj,
                                                 '#alarmsEventsTabPanel eventLogGrid gridview',
                                                 '[0].dataSource.data.items[' + str(item) +
                                                 '].data.webEventTitle')
                event_name = ui_cmd_obj.return_data
                self.ext_builder.component_query(ui_cmd_obj,
                                                 '#alarmsEventsTabPanel eventLogGrid gridview',
                                                 '[0].dataSource.data.items[' + str(item) +
                                                 '].data.message')
                event_message = ui_cmd_obj.return_data
                self.ext_builder.component_query(ui_cmd_obj,
                                                 '#alarmsEventsTabPanel eventLogGrid gridview',
                                                 '[0].dataSource.data.items[' + str(item) +
                                                 '].data.deviceIdentifier')
                event_device = ui_cmd_obj.return_data
                self.logger.log_info("Failed Event Parameters: \n" +
                                     "event_name=" + event_name + "\n" +
                                     "event_message=" + event_message + "\n" +
                                     "event_device=" + event_device + "\n"
                                     )
                item += 1

        return ui_cmd_obj

    # HELPER METHODS

    def click_paging_button(self, ui_cmd_obj, btn_id):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      '#alarmsEventsTabPanel eventLogGrid ' + btn_id, '[0]')
        if ui_cmd_obj.return_data is not None:
            ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                          '#alarmsEventsTabPanel eventLogGrid ' + btn_id,
                                                          '[0].disabled')
            if ui_cmd_obj.return_data is False:
                self.ext_builder.click(ui_cmd_obj,
                                       '#alarmsEventsTabPanel eventLogGrid ' + btn_id + ' => .x-btn-button')
            else:
                ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                              '#alarmsEventsTabPanel eventLogGrid ' + btn_id,
                                                              '[0].tooltip')
                self.logger.log_info("\n'" + ui_cmd_obj.return_data + "' button is disabled.\n")
            ui_cmd_obj.error_state = False
        else:
            self.logger.log_info("\nCould not find paging button with ID '" + btn_id + "'\n")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def get_num_pages(self, ui_cmd_obj):
        # Determine the total count of all items
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, '#alarmsEventsTabPanel eventLogGrid gridview',
                                                      '[0].store.totalCount')
        total_items = ui_cmd_obj.return_data
        self.logger.log_debug("\nTotal Items is '" + str(total_items) + "'\n")

        # Determine the number of items per page
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, '#alarmsEventsTabPanel eventLogGrid gridview',
                                                      '[0].store.pageSize')
        items_per_page = ui_cmd_obj.return_data
        self.logger.log_debug("\nItems per Page is '" + str(items_per_page) + "'\n")

        # Calculate the number of pages
        num_pages = 1
        if (items_per_page > 0) and (total_items > items_per_page):
            num_pages = math.ceil(total_items / items_per_page)
        self.logger.log_debug("\nNumber of pages is '" + str(num_pages) + "'\n")

        return num_pages

    def set_column_filter_state(self, ui_cmd_obj, arg_dict, filter_state):
        col_name = arg_dict['col_name']

        # Some columns exist in both the alarms and events tables, so need to determine a unique identifier
        col_id = "text=" + col_name
        if col_name == "Information":
            col_id = "stateId=console_message"
        elif col_name == "Subcomponent":
            col_id = "stateId=console_subComponent"
        elif col_name == "Source":
            col_id = "colId=sourceDisplayString"
        elif col_name == "Severity":
            col_id = "stateId=console_severity"

        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      '#alarmsEventsTabPanel gridcolumn[' + col_id + ']', '[0]')
        if ui_cmd_obj is not None:
            # Access the column menu's Filter option
            self.ext_builder.move_cursor(ui_cmd_obj,
                                         '#alarmsEventsTabPanel gridcolumn[' + col_id + '] => .x-column-header-text')
            self.ext_builder.click(ui_cmd_obj,
                                   '#alarmsEventsTabPanel gridcolumn[' + col_id + '] => .x-column-header-trigger')

            # Determine if the filter check button's state needs to be toggled
            ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, '#filters', '[0].checked')
            if ui_cmd_obj.return_data is not filter_state:
                self.ext_builder.click(ui_cmd_obj, '#filters => .x-menu-item-icon')
            else:
                self.logger.log_info("\nFilter check button for '" + col_name +
                                     "' is already at desired selection state.\n")

            # Close the column menu
            self.ext_builder.click(ui_cmd_obj, '#alarmsEventsTabPanel eventLogGrid toolbar(true) => .x-scroller')
        else:
            self.logger.log_info("\nCould not find column '" + col_name + "'\n")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj
