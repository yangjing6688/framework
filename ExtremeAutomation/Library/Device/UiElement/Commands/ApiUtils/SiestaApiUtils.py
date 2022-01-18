import time
from ExtremeAutomation.Library.Device.UiElement.Commands.ApiUtils.SiestaApiBuilder import SiestaApiBuilder


class SiestaApiUtils(SiestaApiBuilder):
    def __init__(self, ui_element):
        super(SiestaApiUtils, self).__init__(ui_element)

    def is_item_in_component(self, ui_cmd_obj, target, args, comp_key, comp_val, exact_match=True,
                             component_type=SiestaApiBuilder.COMPONENT_TYPE_TABLE):
        """
        Args:
        [target] - The target of the component query.
        [args] - The args that should be appended to end of the component query.
        [comp_key] - The key within the component to search for.
        [comp_val] - The value the key should have configured.
        [exact_match] - A boolean flag that determines whether <comp_val> must match the configured value exactly
                        or only needs to be found in the beginning of a the string. This value is defaulted to True.
        [component_type] - The type of component being inspected. The default is TABLE. Other supported values are
                           TREE, COMBO, and MENU.

                           The following arguments are required for each type.
                               - TABLE [target, args, key, val, exact_match]
                               - TREE [target, args, key, val, exact_match]
                               - COMBO [target, args, key, val, exact_match]
                               - MENU [target, args, val, exact_match]

        Example:
        The following call
        self.is_item_in_component("grid[stateId=AlarmDefinitions]", "[0]", "name", "AP Radio OnOff")

        Would result in the following component query.
        Ext.ComponentQuery.query("grid[stateId=AlarmDefinitions]")[0]

        This function will return True if the name "AP Radio OnOff" was present in the component. Otherwise
        it would return false.
        """
        return_val = self.get_component_index(ui_cmd_obj, target, args, comp_key, comp_val, exact_match,
                                              component_type).query_info

        ui_cmd_obj.query_info = True if return_val > -1 else False

        return ui_cmd_obj

    def select_table_row_by_attr(self, ui_cmd_obj, target, args, table_key, table_val, exact_match=True):
        """
        Args:
        [target] - The target of the component query.
        [args] - The args that should be appended to end of the component query.
        [table_key] - The key within the table to search for.
        [table_val] - The value the key should have configured.
        [exact_match] - A boolean flag that determines whether <table_val> must match the configured value exactly
                        or only needs to be found in the beginning of a the string. This value is defaulted to True.

        Example:
        The following call
        self.select_table_row_by_attr("grid[stateId=AlarmDefinitions]", "[0]", "name", "AP Radio OnOff")

        Would result in the following component query.
        Ext.ComponentQuery.query("grid[stateId=AlarmDefinitions]")[0]

        This function will select the given item if it is present in the table.
        """
        row_index = self.get_component_index(ui_cmd_obj, target, args, table_key, table_val, exact_match).query_info

        if row_index > -1:
            self.add_component_query(ui_cmd_obj, target, args + ".getSelectionModel().select(" + str(row_index) + ")")
        else:
            ui_cmd_obj.error_state = True
            ui_cmd_obj.error_text = "Unable to find " + table_val + " in table."

        return ui_cmd_obj

    def select_table_row_by_index(self, ui_cmd_obj, target, args, index):
        """
        Args:
        [target] - The target of the component query.
        [args] - The args that should be appended to end of the component query.
        [index] - The index of the row to select (0 based).

        Example:
        The following call
        self.select_table_row_by_index("grid[stateId=AlarmDefinitions]", "[0]", 1)

        Would result in the following component query.
        Ext.ComponentQuery.query("grid[stateId=AlarmDefinitions]")[0].getSelectionModel().select(1)

        This function will select the row at the given index.
        """
        try:
            int_index = int(index)
            self.add_component_query(ui_cmd_obj, target, args + ".getSelectionModel().select(" + str(int_index) + ")")
        except ValueError:
            ui_cmd_obj.error_state = True
            ui_cmd_obj.error_text = "Index could not be converted into an integer. Verify a number was passed."

        return ui_cmd_obj

    def select_last_table_row(self, ui_cmd_obj, target, args):
        """
        Args:
        [target] - The target of the component query.
        [args] - The args that should be appended to end of the component query.

        Example:
        The following call
        self.select_last_table_row("grid[stateId=AlarmDefinitions]", "[0]")

        Would result in the following component query.
        Ext.ComponentQuery.query("grid[stateId=AlarmDefinitions]")[0].store.getCount()

        This function figures out how many items are within the specified the table. Then it selects the last item
        in the table.
        """
        table_len = self.add_component_query(ui_cmd_obj, target, args + ".store.getCount()").query_info

        if isinstance(table_len, int) and table_len > -1:
            actual_len = str(table_len - 1)
            self.add_component_query(ui_cmd_obj, target, args + ".getSelectionModel().select(" + actual_len + ")")
        else:
            ui_cmd_obj.error_state = True
            ui_cmd_obj.error_text = "Could not find the specified table."

        return ui_cmd_obj

    def clear_table_selection(self, ui_cmd_obj, target, args):
        """
        Args:
        [target] - The target of the component query.
        [args] - The args that should be appended to end of the component query.

        Example:
        The following call
        self.clear_table_selection("grid[stateId=AlarmDefinitions]", "[0]")

        Would result in the following component query.
        Ext.ComponentQuery.query("grid[stateId=AlarmDefinitions]")[0].getSelectionModel().clearSelections()

        This function will deselect any selected items within a table.
        """
        self.add_component_query(ui_cmd_obj, target, args + ".getSelectionModel().deselectAll()")

        return ui_cmd_obj

    def scroll_to_index(self, ui_cmd_obj, target, args, index):
        """
        Args:
        [target] - The target of the component query.
        [args] - The args that should be appended to end of the component query.
        [index] - The index within the table to scroll to.

        Example:
        The following call
        self.scroll_to_index("grid[stateId=AlarmDefinitions]", "[0]", 10)

        Would result in the following component query.
        Ext.ComponentQuery.query("grid[stateId=AlarmDefinitions]")[0].bufferedRenderer.scrollTo(<index>, true)

        This function will scroll to the specified index within a table.
        """
        table_len = self.add_component_query(ui_cmd_obj, target, args + ".store.getCount()").query_info

        if index <= table_len:
            if index != table_len:
                index += 1
            self.add_component_query(ui_cmd_obj, target, args + ".bufferedRenderer.scrollTo(" + str(index) + ", true)")
        else:
            ui_cmd_obj.error_state = True
            ui_cmd_obj.error_text = "Index was not within the number of items in the table, unable to scroll."

        return ui_cmd_obj

    def expand_tree_node(self, ui_cmd_obj, target, args, tree_key, tree_val, exact_match=True):
        """
        Args:
        [target] - The target of the component query.
        [args] - The args that should be appended to end of the component query.
        [tree_key] - The key within the tree to search for.
        [tree_val] - The value the key should have configured.
        [exact_match] - A boolean flag that determines whether <table_val> must match the configured value exactly
                        or only needs to be found in the beginning of a the string. This value is defaulted to True.

        Example:
        The following call
        self.expand_tree_node("[itemId=optionsNavigationTree]", "[0]", "name", "Access Control")

        Would result in the following component query.
        Ext.ComponentQuery.query("[itemId=optionsNavigationTree]")[0].store.getAt(<index>).expand()

        The function would expand the node "Access Control" if it's present and not expanded.
        """
        node_index = self.get_component_index(ui_cmd_obj, target, args, tree_key, tree_val, exact_match).query_info

        if isinstance(node_index, int) and node_index > -1:
            tree_expanded = self.add_component_query(ui_cmd_obj, target, args + ".store.getAt(" + str(node_index) +
                                                     ").data.expanded").query_info
            if isinstance(tree_expanded, bool) and not tree_expanded:
                self.add_component_query(ui_cmd_obj, target, args + ".store.getAt(" + str(node_index) + ").expand()")
        else:
            ui_cmd_obj.error_state = True
            ui_cmd_obj.error_text = "Unable to find " + tree_val + " in tree. Verify the component query is correct."

        return ui_cmd_obj

    def collapse_tree_node(self, ui_cmd_obj, target, args, tree_key, tree_val, exact_match=True):
        """
        Args:
        [target] - The target of the component query.
        [args] - The args that should be appended to end of the component query.
        [tree_key] - The key within the tree to search for.
        [tree_val] - The value the key should have configured.
        [exact_match] - A boolean flag that determines whether <table_val> must match the configured value exactly
                        or only needs to be found in the beginning of a the string. This value is defaulted to True.

        Example:
        The following call
        self.collapse_tree_node("[itemId=optionsNavigationTree]", "[0]", "name", "Access Control")

        Would result in the following component query.
        Ext.ComponentQuery.query("[itemId=optionsNavigationTree]")[0].store.getAt(<index>).collapse()

        The function would collapse the node "Access Control" if it's present and expanded.
        """
        node_index = self.get_component_index(ui_cmd_obj, target, args, tree_key, tree_val, exact_match).query_info

        if isinstance(node_index, int) and node_index > -1:
            tree_expanded = self.add_component_query(ui_cmd_obj, target, args + ".store.getAt(" + str(node_index) +
                                                     ").data.expanded").query_info
            if isinstance(tree_expanded, bool) and tree_expanded:
                self.add_component_query(ui_cmd_obj, target, args + ".store.getAt(" + str(node_index) + ").collapse()")
        else:
            ui_cmd_obj.error_state = True
            ui_cmd_obj.error_text = "Unable to find " + tree_val + " in tree. Verify the component query is correct."

        return ui_cmd_obj

    def select_tree_node(self, ui_cmd_obj, target, args, tree_key, tree_val, exact_match=True):
        """
        Args:
        [target] - The target of the component query.
        [args] - The args that should be appended to end of the component query.
        [tree_key] - The key within the tree to search for.
        [tree_val] - The value the key should have configured.
        [exact_match] - A boolean flag that determines whether <table_val> must match the configured value exactly
                        or only needs to be found in the beginning of a the string. This value is defaulted to True.

        Example:
        The following call
        self.select_tree_node("[itemId=optionsNavigationTree]", "[0]", "name", "Access Control")

        Would result in the following component query.
        Ext.ComponentQuery.query("[itemId=optionsNavigationTree]")[0].getSelectionModel().select(<index>)

        The function will select the node "Access Control" if it's present.
        """
        node_index = self.get_component_index(ui_cmd_obj, target, args, tree_key, tree_val, exact_match).query_info

        if isinstance(node_index, int) and node_index > -1:
            self.add_component_query(ui_cmd_obj, target, args + ".getSelectionModel().select(" + str(node_index) + ")")
        else:
            ui_cmd_obj.error_state = True
            ui_cmd_obj.error_text = "Unable to find " + tree_val + " in tree. Verify the component query is correct."

        return ui_cmd_obj

    def wait_for_load_mask(self, ui_cmd_obj, target, args, timeout=30):
        """
        Args:
        [target] - The target of the component query.
        [args] - The args that should be appended to end of the component query.
        [timeout] - How long in seconds the waitFor should run before it's considered failing.

        This function will add a command that will wait for the given load mask to be either null
        or marked as hidden.
        """
        load_mask_hidden = True

        load_mask = self.add_component_query(ui_cmd_obj, target, args).query_info

        if load_mask is not None:
            load_mask_hidden = self.add_component_query(ui_cmd_obj, target, args + ".hidden").query_info

        start_time = time.time()

        while load_mask is not None and not load_mask_hidden:
            if self.__check_wait_for_timeout(start_time, timeout):
                ui_cmd_obj.error_state = True
                break
            load_mask = self.add_component_query(ui_cmd_obj, target, args).query_info
            if load_mask is not None:
                load_mask_hidden = self.add_component_query(ui_cmd_obj, target, args + ".hidden").query_info
            time.sleep(1)

        return ui_cmd_obj

    def wait_for_tree_to_expand(self, ui_cmd_obj, target, args, timeout=30):
        """
        Args:
        [target] - The target of the component query.
        [args] - The args that should be appended to end of the component query.
        [timeout] - How long in seconds the waitFor should run before it's considered failing.

        This function will add a command that will for a the given tree to expand.
        """
        tree_count = self.add_component_query(ui_cmd_obj, target, args + ".store.getCount()")

        start_time = time.time()

        while tree_count == 0:
            if self.__check_wait_for_timeout(start_time, timeout):
                ui_cmd_obj.error_state = True
                break
            tree_count = self.add_component_query(ui_cmd_obj, target, args + ".store.getCount()")
            time.sleep(1)

        return ui_cmd_obj

    def wait_for_item_in_table(self, ui_cmd_obj, target, args, table_key, table_val, refresh_target=None,
                               exact_match=True, timeout=30):
        """
        Args:
        [target] - The target of the component query.
        [args] - The args that should be appended to end of the component query.
        [table_key] - The key within the table to search for.
        [table_val] - The value the key should have configured.
        [refresh_target] - Optional argument. If this argument is provided the given target will be
                           clicked if the item is not present.
        [exact_match] - A boolean flag that determines whether <table_val> must match the configured value exactly
                        or only needs to be found in the beginning of a the string. This value is defaulted to True.
        [timeout] - How long in seconds the waitFor should run before it's considered failing.


        This function will add a command that will wait until the specified item appears in the table.
        If a refresh target is provided the target will be clicked if the item is not present in the table.
        """
        item_in_table = self.is_item_in_component(ui_cmd_obj, target, args, table_key, table_val,
                                                  exact_match).query_info

        start_time = time.time()

        while not item_in_table:
            if self.__check_wait_for_timeout(start_time, timeout):
                ui_cmd_obj.error_state = True
                break

            if refresh_target is not None:
                self.add_click_command(ui_cmd_obj, refresh_target)

            item_in_table = self.is_item_in_component(ui_cmd_obj, target, args, table_key, table_val,
                                                      exact_match).query_info
            time.sleep(1)
        return ui_cmd_obj

    def wait_for_item_not_in_table(self, ui_cmd_obj, target, args, table_key, table_val, refresh_target=None,
                                   exact_match=True, timeout=30):
        """
        Args:
        [target] - The target of the component query.
        [args] - The args that should be appended to end of the component query.
        [table_key] - The key within the table to search for.
        [table_val] - The value the key should have configured.
        [refresh_target] - Optional argument. If this argument is provided the given target will be
                           clicked if the item is not present.
        [exact_match] - A boolean flag that determines whether <table_val> must match the configured value exactly
                        or only needs to be found in the beginning of a the string. This value is defaulted to True.
        [timeout] - How long in seconds the waitFor should run before it's considered failing.


        This function will add a command that will wait until the specified item is not present in the table.
        If a refresh target is provided the target will be clicked if the item is still present in the table.
        """
        item_in_table = self.is_item_in_component(ui_cmd_obj, target, args, table_key, table_val,
                                                  exact_match).query_info

        start_time = time.time()

        while item_in_table:
            if self.__check_wait_for_timeout(start_time, timeout):
                ui_cmd_obj.error_state = True
                break

            if refresh_target is not None:
                self.add_click_command(ui_cmd_obj, refresh_target)

            item_in_table = self.is_item_in_component(ui_cmd_obj, target, args, table_key, table_val,
                                                      exact_match).query_info
            time.sleep(1)

        return ui_cmd_obj

    def wait_for_user_log_out(self, ui_cmd_obj, target, timeout=30):
        """
        Args:
        [target] - The target to be passed to the querySelector.
        [timeout] - How long in seconds the waitFor should run before it's considered failing.

        Waits until the user is successfully logged out of EMC.
        """
        login_form = self.add_document_query(ui_cmd_obj, target).query_info

        start_time = time.time()

        while login_form is None:
            if self.__check_wait_for_timeout(start_time, timeout):
                ui_cmd_obj.error_state = True
                break
            login_form = self.add_document_query(ui_cmd_obj, target).query_info
            time.sleep(1)

        return ui_cmd_obj

    def wait_for_attribute(self, ui_cmd_obj, target, args, expected_val, timeout=30):
        """
        Args:
        [target] - The target of the component query.
        [args] - The args that should be appended to end of the component query.
        [expected_val] - The value that the returned attribute should be configured with.

        Example:
        The following call
        self.wait_for_attribute("#overallFieldId", "[0].text", "100%")

        Would result in the following component query.
        Ext.ComponentQuery.query("[itemId=optionsNavigationTree]")[0].text

        This function will wait until the component query returns <expected_val> or until the timeout expires.
        """
        return_val = self.add_component_query(ui_cmd_obj, target, args).query_info

        start_time = time.time()

        while return_val != expected_val:
            if self.__check_wait_for_timeout(start_time, timeout):
                ui_cmd_obj.error_state = True
                break
            return_val = self.add_component_query(ui_cmd_obj, target, args).query_info
            time.sleep(1)

        return ui_cmd_obj

    def __check_wait_for_timeout(self, start_time, timeout):
        """
        [start_time] - The time value when the timer was started.
        [timeout] - The amount of time (in seconds) allowed to pass before True is returned.

        This function returns True if > <timeout> seconds have passed since <start_time> otherwise
        it returns False.
        """
        # Check if timeout is an int. If it's not see if it can be converted. If it can't
        # be converted default it to 30 seconds and log it.
        if not isinstance(timeout, int):
            if timeout.isdigit():
                timeout = int(timeout)
            else:
                timeout = 30
                self.logger.log_info("Provided timeout value could not be converted to an integer, "
                                     "defaulting to 30 seconds.")

        return time.time() - start_time > timeout
