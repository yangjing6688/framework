from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as UsersBase
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


class Users(UsersBase):

    def users_handle_lock(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "messagebox[title=Conflict]", "[0]")
        if ui_cmd_obj.return_data is not None:
            ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "messagebox[title=Conflict]", "[0].hidden")
            if ui_cmd_obj.return_data is False:
                if StringUtils.string_to_boolean(arg_dict["revoke_lock"]) is True:
                    self.logger.log_info("\nREVOKING LOCK\n")
                    self.ext_builder.click(ui_cmd_obj, '#yes => .x-btn-inner-blue-small')
                else:
                    self.logger.log_info("\nNOT REVOKING LOCK\n")
                    self.ext_builder.click(ui_cmd_obj, '#no => .x-btn-inner-default-small')

        return ui_cmd_obj

    def users_click_add_user(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'button[actionId=addUser] => .x-btn-button')

        return ui_cmd_obj

    def users_click_edit_user(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'button[actionId=editUser] => .x-btn-button')

        return ui_cmd_obj

    def users_click_delete_user(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'button[actionId=deleteUser] => .x-btn-button')

        return ui_cmd_obj

    def users_click_add_group(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'button[actionId=addUserGroup] => .x-btn-button')

        return ui_cmd_obj

    def users_click_edit_group(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'button[actionId=editUserGroup] => .x-btn-button')

        return ui_cmd_obj

    def users_click_copy_group(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'button[actionId=cloneUserGroup] => .x-btn-button')

        return ui_cmd_obj

    def users_click_delete_group(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'button[actionId=deleteUserGroup] => .x-btn-button')

        return ui_cmd_obj

    def users_dialog_add_user_set_name(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, arg_dict['user_name'], '#authUserName => .x-form-text')

        return ui_cmd_obj

    def users_dialog_add_user_set_domain(self, ui_cmd_obj, arg_dict):
        self.add_edit_user_dialog_set_domain(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def users_dialog_add_user_set_group(self, ui_cmd_obj, arg_dict):
        self.add_edit_user_dialog_set_group(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def users_dialog_add_user_click_save(self, ui_cmd_obj, arg_dict):
        self.add_edit_user_dialog_click_save(ui_cmd_obj)

        # Handle an error saving
        self.handle_error(ui_cmd_obj, "user")

        return ui_cmd_obj

    def users_dialog_add_user_click_cancel(self, ui_cmd_obj, arg_dict):
        self.add_edit_user_dialog_click_cancel(ui_cmd_obj)

        return ui_cmd_obj

    def users_dialog_edit_user_set_domain(self, ui_cmd_obj, arg_dict):
        self.add_edit_user_dialog_set_domain(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def users_dialog_edit_user_set_group(self, ui_cmd_obj, arg_dict):
        self.add_edit_user_dialog_set_group(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def users_dialog_edit_user_click_save(self, ui_cmd_obj, arg_dict):
        self.add_edit_user_dialog_click_save(ui_cmd_obj)

        return ui_cmd_obj

    def users_dialog_edit_user_click_cancel(self, ui_cmd_obj, arg_dict):
        self.add_edit_user_dialog_click_cancel(ui_cmd_obj)

        return ui_cmd_obj

    def users_dialog_confirm_delete_user_click_yes(self, ui_cmd_obj, arg_dict):
        self.users_dialog_confirm_delete_click_yes(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def users_dialog_confirm_delete_user_click_no(self, ui_cmd_obj, arg_dict):
        self.users_dialog_confirm_delete_click_no(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def users_dialog_add_group_set_name(self, ui_cmd_obj, arg_dict):
        self.add_copy_group_dialog_set_name(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def users_dialog_add_group_set_membership_criteria(self, ui_cmd_obj, arg_dict):
        self.add_edit_group_dialog_set_membership_criteria(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def users_dialog_add_group_set_snmp_redirect(self, ui_cmd_obj, arg_dict):
        self.add_edit_group_dialog_set_snmp_redirect(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def users_dialog_add_group_expand_capability(self, ui_cmd_obj, arg_dict):
        self.expand_capability(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def users_dialog_add_group_collapse_capability(self, ui_cmd_obj, arg_dict):
        self.collapse_capability(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def users_dialog_add_group_enable_capability(self, ui_cmd_obj, arg_dict):
        self.enable_capability(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def users_dialog_add_group_disable_capability(self, ui_cmd_obj, arg_dict):
        self.disable_capability(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def users_dialog_add_group_click_save(self, ui_cmd_obj, arg_dict):
        self.add_edit_copy_group_dialog_click_save(ui_cmd_obj)

        # Handle an error saving
        self.handle_error(ui_cmd_obj, "group")

        return ui_cmd_obj

    def users_dialog_add_group_click_cancel(self, ui_cmd_obj, arg_dict):
        self.add_edit_copy_group_dialog_click_cancel(ui_cmd_obj)

        return ui_cmd_obj

    def users_dialog_edit_group_set_membership_criteria(self, ui_cmd_obj, arg_dict):
        self.add_edit_group_dialog_set_membership_criteria(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def users_dialog_edit_group_set_snmp_redirect(self, ui_cmd_obj, arg_dict):
        self.add_edit_group_dialog_set_snmp_redirect(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def users_dialog_edit_group_expand_capability(self, ui_cmd_obj, arg_dict):
        self.expand_capability(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def users_dialog_edit_group_collapse_capability(self, ui_cmd_obj, arg_dict):
        self.collapse_capability(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def users_dialog_edit_group_enable_capability(self, ui_cmd_obj, arg_dict):
        self.enable_capability(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def users_dialog_edit_group_disable_capability(self, ui_cmd_obj, arg_dict):
        self.disable_capability(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def users_dialog_edit_group_click_save(self, ui_cmd_obj, arg_dict):
        self.add_edit_copy_group_dialog_click_save(ui_cmd_obj)

        return ui_cmd_obj

    def users_dialog_edit_group_click_cancel(self, ui_cmd_obj, arg_dict):
        self.add_edit_copy_group_dialog_click_cancel(ui_cmd_obj)

        return ui_cmd_obj

    def users_dialog_copy_group_set_name(self, ui_cmd_obj, arg_dict):
        self.add_copy_group_dialog_set_name(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def users_dialog_copy_group_click_save(self, ui_cmd_obj, arg_dict):
        self.add_edit_copy_group_dialog_click_save(ui_cmd_obj)

        # Handle an error saving
        self.handle_error(ui_cmd_obj, "group")

        return ui_cmd_obj

    def users_dialog_copy_group_click_cancel(self, ui_cmd_obj, arg_dict):
        self.add_edit_copy_group_dialog_click_cancel(ui_cmd_obj)

        return ui_cmd_obj

    def users_dialog_confirm_delete_group_click_yes(self, ui_cmd_obj, arg_dict):
        self.users_dialog_confirm_delete_click_yes(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def users_dialog_confirm_delete_group_click_no(self, ui_cmd_obj, arg_dict):
        self.users_dialog_confirm_delete_click_no(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def users_select_user(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#userAdminPanel #userGrid gridview => :textEquals(' + arg_dict['user_name'] + ')')

        return ui_cmd_obj

    def users_select_group(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#userAdminPanel #userLockInfo gridview => :textEquals(' + arg_dict['group_name'] + ')')
        return ui_cmd_obj

    def users_wait_for_user_add(self, ui_cmd_obj, arg_dict):
        self.ext_builder.wait_for_item_in_table(ui_cmd_obj, '#userAdminPanel #userGrid gridview',
                                                '[0]', 'name', arg_dict['user_name'], None, 60)

        return ui_cmd_obj

    def users_wait_for_user_remove(self, ui_cmd_obj, arg_dict):
        self.ext_builder.wait_for_item_not_in_table(ui_cmd_obj, '#userAdminPanel #userGrid gridview',
                                                    '[0]', 'name', arg_dict['user_name'], None, 60)

        return ui_cmd_obj

    def users_wait_for_group_add(self, ui_cmd_obj, arg_dict):
        self.ext_builder.wait_for_item_in_table(ui_cmd_obj, 'userAdminPanel grid[viewId=userGroupGrid]',
                                                '[0]', 'name', arg_dict['group_name'], None, 60)

        return ui_cmd_obj

    def users_wait_for_group_remove(self, ui_cmd_obj, arg_dict):
        self.ext_builder.wait_for_item_not_in_table(ui_cmd_obj, 'userAdminPanel grid[viewId=userGroupGrid]',
                                                    '[0]', 'name', arg_dict['group_name'], None, 60)

        return ui_cmd_obj

    def users_confirm_user_exists(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.is_item_in_component(ui_cmd_obj, '#userAdminPanel #userGrid', '[0]', 'name',
                                                           arg_dict['user_name'])

        # Log the result
        if ui_cmd_obj.return_data is True:
            self.logger.log_info("\nUser '" + arg_dict['user_name'] + "' exists.\n")
        else:
            self.logger.log_info("\nUser '" + arg_dict['user_name'] + "' does not exist.\n")

        # Pass or fail the test, based on what was expected
        if ui_cmd_obj.return_data is StringUtils.string_to_boolean(arg_dict["exists"]):
            # PASS
            ui_cmd_obj.error_state = False
        else:
            # FAIL
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def users_confirm_group_exists(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.is_item_in_component(ui_cmd_obj, '#userAdminPanel grid[viewId=userGroupGrid]',
                                                           '[0]', 'name', arg_dict['group_name'])

        # Log the result
        if ui_cmd_obj.return_data is True:
            self.logger.log_info("\nUser Group '" + arg_dict['group_name'] + "' exists.\n")
        else:
            self.logger.log_info("\nUser Group '" + arg_dict['group_name'] + "' does not exist.\n")

        # Pass or fail the test, based on what was expected
        if ui_cmd_obj.return_data is StringUtils.string_to_boolean(arg_dict["exists"]):
            # PASS
            ui_cmd_obj.error_state = False
        else:
            # FAIL
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def users_confirm_user_logged_in(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "tbtext[cls=statusToolbar]", "[0]")
        if ui_cmd_obj.return_data is not None:
            ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "tbtext[cls=statusToolbar]", "[0].text")
            self.logger.log_info("\nLOGGED IN USER: " + ui_cmd_obj.return_data + "\n")

            check_user = arg_dict['group_name'] + "/" + arg_dict['user_name']
            if check_user in ui_cmd_obj.return_data:
                # PASS
                ui_cmd_obj.error_state = False
            else:
                # FAIL
                ui_cmd_obj.error_state = True
        else:
            self.logger.log_info("\nCOULD NOT FIND STATUS TOOLBAR\n")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    # HELPER METHODS

    def users_dialog_confirm_delete_click_yes(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'button[text=Yes] => .x-btn-button')

        return ui_cmd_obj

    def users_dialog_confirm_delete_click_no(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'button[text=No] => .x-btn-button')

        return ui_cmd_obj

    def add_edit_user_dialog_set_domain(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, arg_dict['domain_name'], 'textfield[name=domain] => .x-form-text')

        return ui_cmd_obj

    def add_edit_user_dialog_set_group(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'form combobox[name=group_id] => .x-form-trigger')
        self.ext_builder.click(ui_cmd_obj, 'form combobox[name=group_id].getPicker() => '
                                           '.x-boundlist-item:contains(' + arg_dict['group_name'] + ')')

        return ui_cmd_obj

    def add_edit_user_dialog_click_save(self, ui_cmd_obj):
        self.ext_builder.click(ui_cmd_obj, 'userDialog button[actionId=addUser] => .x-btn-button')

        return ui_cmd_obj

    def add_edit_user_dialog_click_cancel(self, ui_cmd_obj):
        self.ext_builder.click(ui_cmd_obj, 'userDialog button[actionId=cancel] => .x-btn-inner-default-small')

        return ui_cmd_obj

    def add_copy_group_dialog_set_name(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, arg_dict['group_name'], '#authGroupName => .x-form-text')

        return ui_cmd_obj

    def add_edit_group_dialog_set_membership_criteria(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, arg_dict['member_crit'], 'textfield[name=criteria] => .x-form-text')

        return ui_cmd_obj

    def add_edit_group_dialog_set_snmp_redirect(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'combobox[name=snmpRedirect] => .x-form-trigger')
        self.ext_builder.click(ui_cmd_obj, 'combobox[name=snmpRedirect].getPicker() => '
                                           '.x-boundlist-item:contains(' + arg_dict['snmp_redirect'] + ')')

        return ui_cmd_obj

    def add_edit_copy_group_dialog_click_save(self, ui_cmd_obj):
        self.ext_builder.click(ui_cmd_obj, 'userGroupDialog button[actionId=addUserGroup] => .x-btn-button')

        return ui_cmd_obj

    def add_edit_copy_group_dialog_click_cancel(self, ui_cmd_obj):
        self.ext_builder.click(ui_cmd_obj, 'userGroupDialog button[actionId=cancel] => .x-btn-inner-default-small')

        return ui_cmd_obj

    def expand_capability(self, ui_cmd_obj, arg_dict):
        # Send "False" as last argument so we do a partial match on the tree nodes (since they contain a child node
        # count suffix)
        self.ext_builder.expand_tree_node(ui_cmd_obj, 'capabilityTree treeview', '[0]', 'name',
                                          arg_dict['capability'], False)

        return ui_cmd_obj

    def collapse_capability(self, ui_cmd_obj, arg_dict):
        # Send "False" as last argument so we do a partial match on the tree nodes (since they contain a child node
        # count suffix)
        self.ext_builder.collapse_tree_node(ui_cmd_obj, 'capabilityTree treeview', '[0]', 'name',
                                            arg_dict['capability'], False)

        return ui_cmd_obj

    def enable_capability(self, ui_cmd_obj, arg_dict):
        self.enable_disable_capability(ui_cmd_obj, arg_dict, "enable")

        return ui_cmd_obj

    def disable_capability(self, ui_cmd_obj, arg_dict):
        self.enable_disable_capability(ui_cmd_obj, arg_dict, "disable")

        return ui_cmd_obj

    def enable_disable_capability(self, ui_cmd_obj, arg_dict, enable_or_disable):
        # Figure out how many items are in the tree
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, 'capabilityTree treeview',
                                                      '[0].store.data.items.length')
        item_count = int(ui_cmd_obj.return_data)
        item_count += 1

        # Loop through the items, searching for the node to act on
        item_index = 0
        for x in range(0, item_count):
            ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, 'capabilityTree treeview',
                                                          '[0].store.data.items[' + str(item_index) + '].data.name')
            if ui_cmd_obj.return_data.startswith(arg_dict['capability']):
                tree_index = item_index + 1
                # Check the current checked state of the node
                ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, 'capabilityTree treeview',
                                                              '[0].store.data.items[' + str(item_index) +
                                                              '].data.checked')
                node_checked = ui_cmd_obj.return_data

                # Check the current partial checked state of the node (indicates some of the child nodes are selected
                # and some are not, and is indicated by a filled in square instead of a check mark)
                ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, 'capabilityTree treeview',
                                                              '[0].store.data.items[' + str(item_index) +
                                                              '].data.partialchecked')
                node_partial = ui_cmd_obj.return_data

                if enable_or_disable == "enable" and node_checked is False:
                    # Toggle the check button's selection state - have to do it by index since we are using
                    # "startswith" to avoid naming overlaps, and the tree node functions only have "contains"
                    self.ext_builder.click(ui_cmd_obj, 'capabilityTree treeview => '
                                                       '.x-grid-item:nth-of-type(' + str(tree_index) + ')')
                    self.ext_builder.enter_text_no_target(ui_cmd_obj, '[RETURN]')
                elif enable_or_disable == "disable" and (node_checked is True or node_partial is True):
                    # Toggle the check button's selection state - have to do it by index since we are using
                    # "startswith" to avoid naming overlaps, and the tree node functions only have "contains"
                    self.ext_builder.click(ui_cmd_obj, 'capabilityTree treeview => '
                                                       '.x-grid-item:nth-of-type(' + str(tree_index) + ')')
                    self.ext_builder.enter_text_no_target(ui_cmd_obj, '[RETURN]')

                    # If this is a partially checked node, we will need to toggle the node again
                    # (the first toggle selects the check box, the second toggle deselects it)
                    if node_partial is True:
                        self.ext_builder.enter_text_no_target(ui_cmd_obj, '[RETURN]')
                else:
                    self.logger.log_info("\nCapability " + arg_dict['capability'] + " already at desired state (" +
                                         enable_or_disable + ")\n")
                break
            else:
                item_index += 1

        return ui_cmd_obj

    def handle_error(self, ui_cmd_obj, dlg_type):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "messagebox[title=Save Failed]", "[0]")
        if ui_cmd_obj.return_data is not None:
            ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "messagebox[title=Save Failed]", "[0].hidden")
            if ui_cmd_obj.return_data is False:
                ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "messagebox[title=Save Failed]",
                                                              "[0].msg.html")
                self.logger.log_info("\nSAVE FAILED: " + ui_cmd_obj.return_data + "\n")
                if "already in use" in ui_cmd_obj.return_data:
                    # PASS - already exists so mark as passed and just continue
                    ui_cmd_obj.error_state = False
                else:
                    # FAIL - another error condition so mark as failed
                    ui_cmd_obj.error_state = True

                # Click OK in the error dialog
                self.ext_builder.click(ui_cmd_obj, '#ok => .x-btn-inner-blue-small')

                # Click Cancel in the parent action dialog
                if dlg_type == "user":
                    # Click Cancel in the Add User dialog
                    self.add_edit_user_dialog_click_cancel(ui_cmd_obj)
                elif dlg_type == "group":
                    # Click Cancel in the Add Group dialog
                    self.add_edit_copy_group_dialog_click_cancel(ui_cmd_obj)

        return ui_cmd_obj
