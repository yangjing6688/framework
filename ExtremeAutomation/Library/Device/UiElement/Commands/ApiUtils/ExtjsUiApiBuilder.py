import time
from ExtremeAutomation.Library.Utils.Constants.Constants import Constants
from ExtremeAutomation.Library.Device.Common.Agents.ExtjsSeleniumAgent import ExtjsSeleniumConstants
from ExtremeAutomation.Library.Device.UiElement.Commands.ApiUtils.UiApiBuilder import UiApiBuilder, SeleniumConstants
from selenium.common.exceptions import TimeoutException


class ExtjsUiApiBuilder(UiApiBuilder):
    def __init__(self, device):
        super(ExtjsUiApiBuilder, self).__init__(device)
        self.ext_constants = ExtjsSeleniumConstants()
        self.builder_const = ExtJsUiApiBuilderConstants()

    # +--------------------+
    # | Overridden Actions |
    # +--------------------+
    def click(self, cmd_obj, target, strategy=SeleniumConstants.STRATEGY_SIESTA, **kwargs):
        """
        This calls the parent class's click method but sets the strategy to Siesta by default.
        It can still be changed if another strategy is needed.
        """
        return super(ExtjsUiApiBuilder, self).click(cmd_obj, target, strategy, **kwargs)

    def double_click(self, cmd_obj, target, strategy=SeleniumConstants.STRATEGY_SIESTA, **kwargs):
        """
        This calls the parent class's double click method but sets the strategy to Siesta by default.
        It can still be changed if another strategy is needed.
        """
        return super(ExtjsUiApiBuilder, self).double_click(cmd_obj, target, strategy, **kwargs)

    def right_click(self, cmd_obj, target, strategy=SeleniumConstants.STRATEGY_SIESTA, **kwargs):
        """
        This calls the parent class's right click method but sets the strategy to Siesta by default.
        It can still be changed if another strategy is needed.
        """
        return super(ExtjsUiApiBuilder, self).right_click(cmd_obj, target, strategy, **kwargs)

    def mouse_down(self, cmd_obj, target, strategy=SeleniumConstants.STRATEGY_SIESTA, **kwargs):
        """
        This calls the parent class's mouse down method but sets the strategy to Siesta by default.
        It can still be changed if another strategy is needed.
        """
        return super(ExtjsUiApiBuilder, self).mouse_down(cmd_obj, target, strategy, **kwargs)

    def mouse_up(self, cmd_obj, target, strategy=SeleniumConstants.STRATEGY_SIESTA, **kwargs):
        """
        This calls the parent class's mouse up method but sets the strategy to Siesta by default.
        It can still be changed if another strategy is needed.
        """
        return super(ExtjsUiApiBuilder, self).mouse_up(cmd_obj, target, strategy, **kwargs)

    def move_cursor(self, cmd_obj, target, strategy=SeleniumConstants.STRATEGY_SIESTA, **kwargs):
        """
        This calls the parent class's move cursor method but sets the strategy to Siesta by default.
        It can still be changed if another strategy is needed.
        """
        return super(ExtjsUiApiBuilder, self).move_cursor(cmd_obj, target, strategy, **kwargs)

    def enter_text(self, cmd_obj, text, target, strategy=SeleniumConstants.STRATEGY_SIESTA, clear_existing=True,
                   **kwargs):
        """
        This calls the parent class's type method but sets the strategy to Siesta by default.
        It can still be changed if another strategy is needed.
        """
        return super(ExtjsUiApiBuilder, self).enter_text(cmd_obj, text, target, strategy, clear_existing, **kwargs)

    def find_element(self, cmd_obj, target, strategy=SeleniumConstants.STRATEGY_SIESTA, **kwargs):
        """
        This calls the parent class's find_element method but it sets the strategy to Siesta by default.
        It can still be changed if another strategy is needed.
        """
        return super(ExtjsUiApiBuilder, self).find_element(cmd_obj, target, strategy, **kwargs)

    def execute_async_script(self, cmd_obj, script, return_val=None, **kwargs):
        """
        This calls the parent class's execute_async_script method
        """
        return super(ExtjsUiApiBuilder, self).execute_async_script(cmd_obj, script, return_val)

    def execute_script(self, cmd_obj, script, return_val=None, **kwargs):
        """
        This calls the parent class's execute_script method
        """
        return super(ExtjsUiApiBuilder, self).execute_script(cmd_obj, script, return_val)

    # +--------------------+
    # | ExtJS Only Actions |
    # +--------------------+
    def component_query(self, cmd_obj, target, args, **kwargs):
        """
        [target] - The target of the component query.
        [args] - The args that should be appended to end of the component query.
        [timeout] - The length of time in milliseconds before the action is considered failing.

        Example:
        The following call
        self.component_query("grid[stateId=AlarmDefinitions]", "[0]")

        Would result in the following component query.
        Ext.ComponentQuery.query("grid[stateId=AlarmDefinitions]")[0]

        This function will perform a component query with the given target and arguments. If a string, boolean, int,
        float, or None (null) is returned by the component query the query_info attribute of ui_cmd_obj will be set to
        the returned value.
        """
        arg_dict = {"target": target,
                    "args": args}

        return self._add_action(cmd_obj, self.ext_constants.ACTION_COMPONENT_QUERY, arg_dict, **kwargs)

    def get_component_index(self, cmd_obj, target, args, key, val, exact_match=True, **kwargs):
        """
        Args:
        [target] - The target of the component query.
        [args] - The args that should be appended to end of the component query.
        [key] - The key within the component to search for.
        [val] - The value the key should have configured.
        [exact_match] - A boolean flag that determines whether <table_val> must match the configured value exactly
                        or only needs to be found in the beginning of a the string. This value is defaulted to True.

        Example:
        The following call
        self.get_component_index("grid[stateId=AlarmDefinitions]", "[0]", "name", "AP Radio OnOff")

        Would result in the following component query.
        Ext.ComponentQuery.query("grid[stateId=AlarmDefinitions]")[0]

        This function returns the index if the key value pair is found within the component. It returns -1 if
        it is not found.
        """
        arg_dict = {"target": target,
                    "args": args,
                    "key": key,
                    "val": val,
                    "exact_match": exact_match}

        return self._add_action(cmd_obj, self.ext_constants.ACTION_GET_COMPONENT_INDEX, arg_dict, **kwargs)

    def get_menu_index(self, cmd_obj, target, args, text, exact_match=True, **kwargs):
        """
        Args:
        [target] - The target of the component query.
        [args] - The args that should be appended to end of the component query.
        [text] - The key within the component to search for.
        [exact_match] - A boolean flag that determines whether <table_val> must match the configured value exactly
                        or only needs to be found in the beginning of a the string. This value is defaulted to True.

        Example:
        The following call
        self.get_component_index("grid[stateId=AlarmDefinitions]", "[0]", "AP Radio OnOff")

        Would result in the following component query.
        Ext.ComponentQuery.query("grid[stateId=AlarmDefinitions]")[0]

        This function returns the index if the text is found within the menu. It returns -1 if
        it is not found.
        """
        arg_dict = {"target": target,
                    "args": args,
                    "text": text,
                    "exact_match": exact_match}

        return self._add_action(cmd_obj, self.ext_constants.ACTION_GET_MENU_INDEX, arg_dict, **kwargs)

    def is_item_in_component(self, cmd_obj, target, args, key, val, exact_match=True, **kwargs):
        """
        Args:
        [target] - The target of the component query.
        [args] - The args that should be appended to end of the component query.
        [key] - The key within the component to search for.
        [val] - The value the key should have configured.
        [exact_match] - A boolean flag that determines whether <comp_val> must match the configured value exactly
                        or only needs to be found in the beginning of a the string. This value is defaulted to True.

        Example:
        The following call
        self.is_item_in_component("grid[stateId=AlarmDefinitions]", "[0]", "name", "AP Radio OnOff")

        Would result in the following component query.
        Ext.ComponentQuery.query("grid[stateId=AlarmDefinitions]")[0]

        This function will return True if the name "AP Radio OnOff" was present in the component. Otherwise
        it would return False.
        """
        arg_dict = {"target": target,
                    "args": args,
                    "key": key,
                    "val": val,
                    "exact_match": exact_match,
                    "action_name": self.builder_const.IS_ITEM_IN_COMPONENT}

        self._log_action(self.builder_const.IS_ITEM_IN_COMPONENT, arg_dict, **kwargs)

        return_val = self.get_component_index(cmd_obj, target, args, key, val, exact_match,
                                              log_action=False).return_data

        if return_val == "" or return_val is None:
            cmd_obj.return_data = False
        else:
            cmd_obj.return_data = True if return_val > -1 else False

        return cmd_obj

    def is_item_in_menu(self, cmd_obj, target, args, text, exact_match=True, **kwargs):
        """
        Args:
        [target] - The target of the component query.
        [args] - The args that should be appended to end of the component query.
        [text] - The text to search for within the table.
        [exact_match] - A boolean flag that determines whether <comp_val> must match the configured value exactly
                        or only needs to be found in the beginning of a the string. This value is defaulted to True.

        Example:
        The following call
        self.is_item_in_menu("grid[stateId=AlarmDefinitions]", "[0]", "AP Radio OnOff")

        Would result in the following component query.
        Ext.ComponentQuery.query("grid[stateId=AlarmDefinitions]")[0]

        This function will return True if the name "AP Radio OnOff" was present in the menu. Otherwise
        it would return False.
        """
        arg_dict = {"target": target,
                    "args": args,
                    "text": text,
                    "exact_match": exact_match,
                    "action_name": self.builder_const.IS_ITEM_IN_MENU}

        self._log_action(self.builder_const.IS_ITEM_IN_MENU, arg_dict, **kwargs)

        return_val = self.get_menu_index(cmd_obj, target, args, text, exact_match, log_action=False).return_data
        if return_val == "" or return_val is None:
            cmd_obj.return_data = False
        else:
            cmd_obj.return_data = True if return_val > -1 else False

        return cmd_obj

    def select_table_row_by_attr(self, cmd_obj, target, args, table_key, table_val, exact_match=True, **kwargs):
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
        arg_dict = {"target": target,
                    "args": args,
                    "table_key": table_key,
                    "table_val": table_val,
                    "exact_match": exact_match,
                    "action_name": self.builder_const.SELECT_TABLE_ROW_BY_ATTR}

        self._log_action(self.builder_const.SELECT_TABLE_ROW_BY_ATTR, arg_dict, **kwargs)

        row_index = self.get_component_index(cmd_obj, target, args, table_key, table_val, exact_match,
                                             log_action=False).return_data

        if row_index > -1:
            self.component_query(cmd_obj, target, args + ".getSelectionModel().select(" + str(row_index) + ")",
                                 log_action=False)
        else:
            cmd_obj.error_state = True
            cmd_obj.error_text = "Unable to find " + table_val + " in table."
        return cmd_obj

    def select_table_row_by_index(self, cmd_obj, target, args, index, **kwargs):
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
        arg_dict = {"target": target,
                    "args": args,
                    "index": index,
                    "action_name": self.builder_const.SELECT_TABLE_ROW_BY_INDEX}

        self._log_action(self.builder_const.SELECT_TABLE_ROW_BY_INDEX, arg_dict, **kwargs)

        try:
            self.component_query(cmd_obj, target, args + ".getSelectionModel().select(" + str(int(index)) + ")",
                                 log_action=False)
        except ValueError:
            cmd_obj.error_state = True
            cmd_obj.error_text = "Index could not be converted into an integer. Verify a number was passed."
        return cmd_obj

    def select_last_table_row(self, cmd_obj, target, args, **kwargs):
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
        arg_dict = {"target": target,
                    "args": args,
                    "action_name": self.builder_const.SELECT_LAST_TABLE_ROW}

        self._log_action(self.builder_const.SELECT_LAST_TABLE_ROW, arg_dict, **kwargs)

        table_len = self.component_query(cmd_obj, target, args + ".store.getCount()", log_action=False).return_data

        if isinstance(table_len, int) and table_len > -1:
            actual_len = str(table_len - 1)
            self.component_query(cmd_obj, target, args + ".getSelectionModel().select(" + actual_len + ")",
                                 log_action=False)
        else:
            cmd_obj.error_state = True
            cmd_obj.error_text = "Could not find the specified table."
        return cmd_obj

    def clear_table_selection(self, cmd_obj, target, args, **kwargs):
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
        arg_dict = {"target": target,
                    "args": args,
                    "action_name": self.builder_const.CLEAR_TABLE_SELECTION}

        self._log_action(self.builder_const.CLEAR_TABLE_SELECTION, arg_dict, **kwargs)

        return self.component_query(cmd_obj, target, args + ".getSelectionModel().deselectAll()", log_action=False)

    def scroll_to_index(self, cmd_obj, target, args, index, **kwargs):
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
        arg_dict = {"target": target,
                    "args": args,
                    "index": index,
                    "action_name": self.builder_const.SCROLL_TO_INDEX}

        self._log_action(self.builder_const.SCROLL_TO_INDEX, arg_dict, **kwargs)

        table_len = self.component_query(cmd_obj, target, args + ".store.getCount()", log_action=False).return_data

        if index <= table_len:
            if index != table_len:
                index += 1
            self.component_query(cmd_obj, target, args + ".bufferedRenderer.scrollTo(" + str(index) + ", true)",
                                 log_action=False)
        else:
            cmd_obj.error_state = True
            cmd_obj.error_text = "Index was not within the number of items in the table, unable to scroll."
        return cmd_obj

    def expand_tree_node(self, cmd_obj, target, args, tree_key, tree_val, exact_match=True, **kwargs):
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
        arg_dict = {"target": target,
                    "args": args,
                    "tree_key": tree_key,
                    "tree_val": tree_val,
                    "exact_match": exact_match,
                    "action_name": self.builder_const.EXPAND_TREE_NODE}

        self._log_action(self.builder_const.EXPAND_TREE_NODE, arg_dict, **kwargs)

        node_index = self.get_component_index(cmd_obj, target, args, tree_key, tree_val, exact_match,
                                              log_action=False).return_data

        if isinstance(node_index, int) and node_index > -1:
            tree_expanded = self.component_query(cmd_obj, target, args + ".store.getAt(" + str(node_index) +
                                                 ").data.expanded", log_action=False).return_data

            if isinstance(tree_expanded, bool) and not tree_expanded:
                self.component_query(cmd_obj, target, args + ".store.getAt(" + str(node_index) + ").expand()",
                                     log_action=False)
        else:
            cmd_obj.error_state = True
            cmd_obj.error_state = "Unable to find " + tree_val + "in tree. Verify the component query is correct."
        return cmd_obj

    def collapse_tree_node(self, cmd_obj, target, args, tree_key, tree_val, exact_match=True, **kwargs):
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
        arg_dict = {"target": target,
                    "args": args,
                    "tree_key": tree_key,
                    "tree_val": tree_val,
                    "exact_match": exact_match,
                    "action_name": self.builder_const.COLLAPSE_TREE_NODE}

        self._log_action(self.builder_const.COLLAPSE_TREE_NODE, arg_dict, **kwargs)

        node_index = self.get_component_index(cmd_obj, target, args, tree_key, tree_val, exact_match,
                                              log_action=False).return_data

        if isinstance(node_index, int) and node_index > -1:
            tree_expanded = self.component_query(cmd_obj, target, args + ".store.getAt(" + str(node_index) +
                                                 ").data.expanded", log_action=False).return_data

            if isinstance(tree_expanded, bool) and tree_expanded:
                self.component_query(cmd_obj, target, args + ".store.getAt(" + str(node_index) + ").collapse()",
                                     log_action=False)
        else:
            cmd_obj.error_state = True
            cmd_obj.error_text = "Unable to find " + tree_val + " in tree. Verify the component query is correct."
        return cmd_obj

    def select_tree_node(self, cmd_obj, target, args, tree_key, tree_val, exact_match=True, **kwargs):
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
        arg_dict = {"target": target,
                    "args": args,
                    "tree_key": tree_key,
                    "tree_val": tree_val,
                    "exact_match": exact_match,
                    "action_name": self.builder_const.SELECT_TREE_NODE}

        self._log_action(self.builder_const.SELECT_TREE_NODE, arg_dict, **kwargs)

        node_index = self.get_component_index(cmd_obj, target, args, tree_key, tree_val, exact_match,
                                              log_action=False).return_data

        if isinstance(node_index, int) and node_index > -1:
            self.component_query(cmd_obj, target, args + ".getSelectionModel().select(" + str(node_index) + ")",
                                 log_action=False)
        else:
            cmd_obj.error_state = True
            cmd_obj.error_text = "Unable to find " + tree_val + " in tree. Verify the component query is c orrect."
        return cmd_obj

    def wait_for_load_mask(self, cmd_obj, target, args, timeout=10, **kwargs):
        """
        Args:
        [target] - The target of the component query.
        [args] - The args that should be appended to end of the component query.
        [timeout] - How long in seconds the waitFor should run before it's considered failing.

        This function will add a command that will wait for the given load mask to be either null
        or marked as hidden.
        """
        arg_dict = {"target": target,
                    "args": args,
                    "timeout": timeout,
                    "action_name": self.builder_const.WAIT_FOR_LOAD_MASK}

        self._log_action(self.builder_const.WAIT_FOR_LOAD_MASK, arg_dict, **kwargs)

        load_mask_hidden = True

        load_mask = self.component_query(cmd_obj, target, args, log_action=False).return_data

        if load_mask is not None:
            load_mask_hidden = self.component_query(cmd_obj, target, args + ".hidden", log_action=False).return_data

        start = time.time()

        while load_mask is not None and not load_mask_hidden:
            if self.__check_wait_for_timeout(start, timeout):
                cmd_obj.error_state = True
                break
            load_mask = self.component_query(cmd_obj, target, args, log_action=False).return_data

            if load_mask is not None:
                load_mask_hidden = self.component_query(cmd_obj, target, args + ".hidden", log_action=False).return_data
            time.sleep(1)
        return cmd_obj

    def wait_for_tree_to_expand(self, cmd_obj, target, args, timeout=10, **kwargs):
        """
        Args:
        [target] - The target of the component query.
        [args] - The args that should be appended to end of the component query.
        [timeout] - How long in seconds the waitFor should run before it's considered failing.

        This function will add a command that will for a the given tree to expand.
        """
        arg_dict = {"target": target,
                    "args": args,
                    "timeout": timeout,
                    "action_name": self.builder_const.WAIT_FOR_TREE_TO_EXPAND}

        self._log_action(self.builder_const.WAIT_FOR_TREE_TO_EXPAND, arg_dict, **kwargs)

        tree_count = self.component_query(cmd_obj, target, args + ".store.getCount()", log_action=False).return_data

        start = time.time()

        while tree_count == 0:
            if self.__check_wait_for_timeout(start, timeout):
                cmd_obj.error_state = True
                break
            tree_count = self.component_query(cmd_obj, target, args + ".store.getCount()", log_action=False).return_data
            time.sleep(1)
        return cmd_obj

    def wait_for_item_in_table(self, cmd_obj, target, args, key, val, refresh_target=None, exact_match=True,
                               timeout=10, **kwargs):
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
        arg_dict = {"target": target,
                    "args": args,
                    "key": key,
                    "val": val,
                    "refresh_target": refresh_target,
                    "exact_match": exact_match,
                    "timeout": timeout,
                    "action_name": self.builder_const.WAIT_FOR_ITEM_IN_TABLE}

        self._log_action(self.builder_const.WAIT_FOR_ITEM_IN_TABLE, arg_dict, **kwargs)

        item_in_table = self.is_item_in_component(cmd_obj, target, args, key, val, exact_match,
                                                  log_action=False).return_data

        start = time.time()

        while not item_in_table:
            if self.__check_wait_for_timeout(start, timeout):
                cmd_obj.error_state = True
                break

            if refresh_target is not None:
                self.click(cmd_obj, refresh_target)

            item_in_table = self.is_item_in_component(cmd_obj, target, args, key, val, exact_match,
                                                      log_action=False).return_data
            time.sleep(1)
        return cmd_obj

    def wait_for_item_not_in_table(self, cmd_obj, target, args, key, val, refresh_target=None, exact_match=True,
                                   timeout=10, **kwargs):
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
        arg_dict = {"target": target,
                    "args": args,
                    "key": key,
                    "val": val,
                    "refresh_target": refresh_target,
                    "exact_match": exact_match,
                    "timeout": timeout,
                    "action_name": self.builder_const.WAIT_FOR_ITEM_NOT_IN_TABLE}

        self._log_action(self.builder_const.WAIT_FOR_ITEM_NOT_IN_TABLE, arg_dict, **kwargs)

        item_in_table = self.is_item_in_component(cmd_obj, target, args, key, val, exact_match,
                                                  log_action=False).return_data

        start = time.time()

        while item_in_table:
            if self.__check_wait_for_timeout(start, timeout):
                cmd_obj.error_state = True
                break

            if refresh_target is not None:
                self.click(cmd_obj, refresh_target)

            item_in_table = self.is_item_in_component(cmd_obj, target, args, key, val, exact_match,
                                                      log_action=False).return_data
            time.sleep(1)
        return cmd_obj

    def wait_for_user_log_out(self, cmd_obj, target, timeout=10, **kwargs):
        """
        Args:
        [target] - The target to be passed to the querySelector.
        [timeout] - How long in seconds the waitFor should run before it's considered failing.

        Waits until the user is successfully logged out of EMC.
        """
        arg_dict = {"target": target,
                    "timeout": timeout,
                    "action_name": self.builder_const.WAIT_FOR_USER_LOG_OUT}

        self._log_action(self.builder_const.WAIT_FOR_USER_LOG_OUT, arg_dict, **kwargs)

        login_form = self.document_query(cmd_obj, target).return_data

        start = time.time()

        while login_form is None:
            if self.__check_wait_for_timeout(start, timeout):
                cmd_obj.error_state = True
                break
            login_form = self.document_query(cmd_obj, target).return_data
            time.sleep(1)
        return cmd_obj

    def wait_for_attribute(self, cmd_obj, target, args, expected_val, timeout=30, **kwargs):
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
        arg_dict = {"target": target,
                    "args": args,
                    "expected_val": expected_val,
                    "timeout": timeout,
                    "action_name": self.builder_const.WAIT_FOR_ATTRIBUTE}

        self._log_action(self.builder_const.WAIT_FOR_ATTRIBUTE, arg_dict, **kwargs)

        return_val = self.component_query(cmd_obj, target, args).return_data

        start = time.time()

        while return_val != expected_val:
            if self.__check_wait_for_timeout(start, timeout):
                cmd_obj.error_state = True
                break
            return_val = self.component_query(cmd_obj, target, args).return_data
        return cmd_obj

    def document_ready(self):
        """
        This waits until the document ready state is "complete". It will wait up to a minute for this.
        If the timeout expires a TimeoutException is raised.
        """
        timeout = 60 * 1000  # 1 minute in milliseconds.
        start = time.time()

        while time.time() - start < timeout:
            if self.execute_async_script("var state = document.readyState;", "state") == "complete":
                return True
        raise TimeoutException("Page state was not complete within " + str(timeout * 1000) + " seconds.")

    # +----------------------------+
    # | Non-Builder Helper Methods |
    # +----------------------------+
    @staticmethod
    def __check_wait_for_timeout(start_time, timeout):
        """
        [start_time] - The time value when the timer was started.
        [timeout] - The amount of time (in seconds) allowed to pass before True is returned.

        This function returns True if > <timeout> seconds have passed since <start_time> otherwise
        it returns False.
        """
        time_delta = time.time() - start_time

        return time_delta > int(timeout)


class ExtJsUiApiBuilderConstants(Constants):
    IS_ITEM_IN_COMPONENT = "is_item_in_component"
    IS_ITEM_IN_MENU = "is_item_in_menu"
    SELECT_TABLE_ROW_BY_ATTR = "select_table_row_by_attr"
    SELECT_TABLE_ROW_BY_INDEX = "select_table_row_by_index"
    SELECT_LAST_TABLE_ROW = "select_last_table_row"
    CLEAR_TABLE_SELECTION = "clear_table_selection"
    SCROLL_TO_INDEX = "scroll_to_index"
    EXPAND_TREE_NODE = "expand_tree_node"
    COLLAPSE_TREE_NODE = "collapse_tree_node"
    SELECT_TREE_NODE = "select_tree_node"
    WAIT_FOR_LOAD_MASK = "wait_for_load_mask"
    WAIT_FOR_TREE_TO_EXPAND = "wait_for_tree_to_expand"
    WAIT_FOR_ITEM_IN_TABLE = "wait_for_item_in_table"
    WAIT_FOR_ITEM_NOT_IN_TABLE = "wait_for_item_not_in_table"
    WAIT_FOR_USER_LOG_OUT = "wait_for_user_log_out"
    WAIT_FOR_ATTRIBUTE = "wait_for_attribute"
