from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as SavedtasksBase
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


class Savedtasks(SavedtasksBase):
    def savedtasks_select_task(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               'scriptTaskGrid gridview => :textEquals(' + arg_dict['task_name'] + ')')

        return ui_cmd_obj

    def savedtasks_click_edit(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'button[actionId=editScriptTask] => .x-btn-inner-default-toolbar-small')

        return ui_cmd_obj

    def savedtasks_click_save_as(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'button[actionId=saveAsScriptTask] => .x-btn-inner-default-toolbar-small')

        return ui_cmd_obj

    def savedtasks_click_run(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'button[actionId=runScriptTask] => .x-btn-inner-default-toolbar-small')

        return ui_cmd_obj

    def savedtasks_click_delete(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'button[actionId=deleteScriptTask] => .x-btn-inner-default-toolbar-small')

        return ui_cmd_obj

    def savedtasks_click_refresh(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'button[actionId=refreshScriptTaskGrid] => '
                                           '.x-btn-inner-default-toolbar-small')

        return ui_cmd_obj

    def savedtasks_dialog_confirm_delete_click_yes(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#yes => .x-btn-inner-blue-small')

        return ui_cmd_obj

    def savedtasks_dialog_confirm_delete_click_no(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#no => .x-btn-inner-default-small')

        return ui_cmd_obj

    def savedtasks_confirm_task_exists(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.is_item_in_component(ui_cmd_obj, 'scriptTaskGrid gridview', '[0]', 'name',
                                                           arg_dict['task_name'])

        # Log the result
        if ui_cmd_obj.return_data is True:
            self.logger.log_info("\nSaved task '" + arg_dict['task_name'] + "' exists.\n")
        else:
            self.logger.log_info("\nSaved task '" + arg_dict['task_name'] + "' does not exist.\n")

        # Pass or fail the test, based on what was expected
        if ui_cmd_obj.return_data is StringUtils.string_to_boolean(arg_dict["exists"]):
            # PASS
            ui_cmd_obj.error_state = False
        else:
            # FAIL
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def savedtasks_wait_for_task_add(self, ui_cmd_obj, arg_dict):
        self.ext_builder.wait_for_item_in_table(ui_cmd_obj, 'scriptTaskGrid gridview', '[0]', 'name',
                                                arg_dict['task_name'], None, 60)
        return ui_cmd_obj

    def savedtasks_wait_for_task_remove(self, ui_cmd_obj, arg_dict):
        self.ext_builder.wait_for_item_not_in_table(ui_cmd_obj, 'scriptTaskGrid gridview', '[0]', 'name',
                                                    arg_dict['task_name'], None, 60)
        return ui_cmd_obj
