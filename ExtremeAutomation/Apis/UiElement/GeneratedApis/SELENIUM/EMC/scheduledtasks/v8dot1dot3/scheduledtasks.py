from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as ScheduledtasksBase
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


class Scheduledtasks(ScheduledtasksBase):
    def scheduledtasks_select_task(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               'scheduleGrid gridview => :textEquals(' + arg_dict['task_name'] + ')')

        return ui_cmd_obj

    def scheduledtasks_click_add(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'button[actionId=addScheduledJob] => .x-btn-inner-default-toolbar-small')

        return ui_cmd_obj

    def scheduledtasks_click_edit(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'button[actionId=editScheduledJob] => .x-btn-inner-default-toolbar-small')

        return ui_cmd_obj

    def scheduledtasks_click_copy(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'button[actionId=copyScheduledJob] => .x-btn-inner-default-toolbar-small')

        return ui_cmd_obj

    def scheduledtasks_click_delete(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'button[actionId=deleteScheduledJob] => .x-btn-inner-default-toolbar-small')

        return ui_cmd_obj

    def scheduledtasks_click_run(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'button[actionId=addScheduledJob] => .x-btn-inner-default-toolbar-small')

        return ui_cmd_obj

    def scheduledtasks_click_refresh(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'button[actionId=refreshScheduleGrid] => .x-btn-inner-default-toolbar-small')

        return ui_cmd_obj

    def scheduledtasks_click_disable(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'button[actionId=disableAllSchedules] => .x-btn-inner-default-toolbar-small')

        return ui_cmd_obj

    def scheduledtasks_click_smtp(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'button[actionId=configSmtp] => .x-btn-inner-default-toolbar-small')

        return ui_cmd_obj

    def scheduledtasks_dialog_add_set_type(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Scheduledtasks, self).scheduledtasks_dialog_add_set_type(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def scheduledtasks_dialog_add_set_report_name(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Scheduledtasks, self).scheduledtasks_dialog_add_set_report_name(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def scheduledtasks_dialog_add_set_task_name(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Scheduledtasks, self).scheduledtasks_dialog_add_set_task_name(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def scheduledtasks_dialog_add_set_task_description(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Scheduledtasks, self).scheduledtasks_dialog_add_set_task_description(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def scheduledtasks_dialog_add_set_task_enabled(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Scheduledtasks, self).scheduledtasks_dialog_add_set_task_enabled(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def scheduledtasks_dialog_add_set_recurrence_hourly(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Scheduledtasks, self).scheduledtasks_dialog_add_set_recurrence_hourly(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def scheduledtasks_dialog_add_set_recurrence_daily(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Scheduledtasks, self).scheduledtasks_dialog_add_set_recurrence_daily(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def scheduledtasks_dialog_add_set_recurrence_weekly(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Scheduledtasks, self).scheduledtasks_dialog_add_set_recurrence_weekly(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def scheduledtasks_dialog_add_set_recurrence_monthly(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Scheduledtasks, self).scheduledtasks_dialog_add_set_recurrence_monthly(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def scheduledtasks_dialog_add_set_start_date(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Scheduledtasks, self).scheduledtasks_dialog_add_set_start_date(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def scheduledtasks_dialog_add_set_start_time(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Scheduledtasks, self).scheduledtasks_dialog_add_set_start_time(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def scheduledtasks_dialog_add_set_end_date(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Scheduledtasks, self).scheduledtasks_dialog_add_set_end_date(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def scheduledtasks_dialog_add_set_end_time(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Scheduledtasks, self).scheduledtasks_dialog_add_set_end_time(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def scheduledtasks_dialog_add_set_email_to(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Scheduledtasks, self).scheduledtasks_dialog_add_set_email_to(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def scheduledtasks_dialog_add_set_email_subject(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Scheduledtasks, self).scheduledtasks_dialog_add_set_email_subject(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def scheduledtasks_dialog_add_set_email_body(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Scheduledtasks, self).scheduledtasks_dialog_add_set_email_body(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def scheduledtasks_dialog_add_click_save(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Scheduledtasks, self).scheduledtasks_dialog_add_click_save(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def scheduledtasks_dialog_add_click_cancel(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Scheduledtasks, self).scheduledtasks_dialog_add_click_cancel(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def scheduledtasks_dialog_edit_set_task_name(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Scheduledtasks, self).scheduledtasks_dialog_edit_set_task_name(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def scheduledtasks_dialog_edit_set_task_description(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Scheduledtasks, self).scheduledtasks_dialog_edit_set_task_description(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def scheduledtasks_dialog_edit_set_task_enabled(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Scheduledtasks, self).scheduledtasks_dialog_edit_set_task_enabled(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def scheduledtasks_dialog_edit_set_recurrence_hourly(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Scheduledtasks, self).scheduledtasks_dialog_edit_set_recurrence_hourly(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def scheduledtasks_dialog_edit_set_recurrence_daily(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Scheduledtasks, self).scheduledtasks_dialog_edit_set_recurrence_daily(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def scheduledtasks_dialog_edit_set_recurrence_weekly(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Scheduledtasks, self).scheduledtasks_dialog_edit_set_recurrence_weekly(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def scheduledtasks_dialog_edit_set_recurrence_monthly(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Scheduledtasks, self).scheduledtasks_dialog_edit_set_recurrence_monthly(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def scheduledtasks_dialog_edit_set_start_date(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Scheduledtasks, self).scheduledtasks_dialog_edit_set_start_date(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def scheduledtasks_dialog_edit_set_start_time(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Scheduledtasks, self).scheduledtasks_dialog_edit_set_start_time(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def scheduledtasks_dialog_edit_set_end_date(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Scheduledtasks, self).scheduledtasks_dialog_edit_set_end_date(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def scheduledtasks_dialog_edit_set_end_time(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Scheduledtasks, self).scheduledtasks_dialog_edit_set_end_time(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def scheduledtasks_dialog_edit_set_email_to(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Scheduledtasks, self).scheduledtasks_dialog_edit_set_email_to(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def scheduledtasks_dialog_edit_set_email_subject(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Scheduledtasks, self).scheduledtasks_dialog_edit_set_email_subject(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def scheduledtasks_dialog_edit_set_email_body(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Scheduledtasks, self).scheduledtasks_dialog_edit_set_email_body(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def scheduledtasks_dialog_edit_click_save(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Scheduledtasks, self).scheduledtasks_dialog_edit_click_save(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def scheduledtasks_dialog_edit_click_cancel(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Scheduledtasks, self).scheduledtasks_dialog_edit_click_cancel(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def scheduledtasks_dialog_copy_set_type(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Scheduledtasks, self).scheduledtasks_dialog_copy_set_type(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def scheduledtasks_dialog_copy_set_task_name(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Scheduledtasks, self).scheduledtasks_dialog_copy_set_task_name(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def scheduledtasks_dialog_copy_set_task_description(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Scheduledtasks, self).scheduledtasks_dialog_copy_set_task_description(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def scheduledtasks_dialog_copy_set_task_enabled(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Scheduledtasks, self).scheduledtasks_dialog_copy_set_task_enabled(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def scheduledtasks_dialog_copy_set_recurrence_hourly(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Scheduledtasks, self).scheduledtasks_dialog_copy_set_recurrence_hourly(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def scheduledtasks_dialog_copy_set_recurrence_daily(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Scheduledtasks, self).scheduledtasks_dialog_copy_set_recurrence_daily(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def scheduledtasks_dialog_copy_set_recurrence_weekly(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Scheduledtasks, self).scheduledtasks_dialog_copy_set_recurrence_weekly(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def scheduledtasks_dialog_copy_set_recurrence_monthly(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Scheduledtasks, self).scheduledtasks_dialog_copy_set_recurrence_monthly(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def scheduledtasks_dialog_copy_set_start_date(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Scheduledtasks, self).scheduledtasks_dialog_copy_set_start_date(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def scheduledtasks_dialog_copy_set_start_time(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Scheduledtasks, self).scheduledtasks_dialog_copy_set_start_time(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def scheduledtasks_dialog_copy_set_end_date(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Scheduledtasks, self).scheduledtasks_dialog_copy_set_end_date(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def scheduledtasks_dialog_copy_set_end_time(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Scheduledtasks, self).scheduledtasks_dialog_copy_set_end_time(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def scheduledtasks_dialog_copy_set_email_to(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Scheduledtasks, self).scheduledtasks_dialog_copy_set_email_to(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def scheduledtasks_dialog_copy_set_email_subject(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Scheduledtasks, self).scheduledtasks_dialog_copy_set_email_subject(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def scheduledtasks_dialog_copy_set_email_body(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Scheduledtasks, self).scheduledtasks_dialog_copy_set_email_body(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def scheduledtasks_dialog_copy_click_save(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Scheduledtasks, self).scheduledtasks_dialog_copy_click_save(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def scheduledtasks_dialog_copy_click_cancel(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Scheduledtasks, self).scheduledtasks_dialog_copy_click_cancel(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def scheduledtasks_dialog_confirm_delete_click_yes(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Scheduledtasks, self).scheduledtasks_dialog_confirm_delete_click_yes(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def scheduledtasks_dialog_confirm_delete_click_no(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Scheduledtasks, self).scheduledtasks_dialog_confirm_delete_click_no(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def scheduledtasks_dialog_confirm_disable_click_yes(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Scheduledtasks, self).scheduledtasks_dialog_confirm_disable_click_yes(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def scheduledtasks_dialog_confirm_disable_click_no(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Scheduledtasks, self).scheduledtasks_dialog_confirm_disable_click_no(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def scheduledtasks_dialog_smtp_set_server(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Scheduledtasks, self).scheduledtasks_dialog_smtp_set_server(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def scheduledtasks_dialog_smtp_set_address(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Scheduledtasks, self).scheduledtasks_dialog_smtp_set_address(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def scheduledtasks_dialog_smtp_set_password(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Scheduledtasks, self).scheduledtasks_dialog_smtp_set_password(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def scheduledtasks_dialog_smtp_click_ok(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Scheduledtasks, self).scheduledtasks_dialog_smtp_click_ok(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def scheduledtasks_dialog_smtp_click_cancel(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Scheduledtasks, self).scheduledtasks_dialog_smtp_click_cancel(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def scheduledtasks_confirm_task_exists(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.is_item_in_component(ui_cmd_obj, 'scheduleGrid gridview', '[0]', 'jobName',
                                                           arg_dict['task_name'])

        # Log the result
        if ui_cmd_obj.return_data is True:
            self.logger.log_info("\nScheduled task '" + arg_dict['task_name'] + "' exists.\n")
        else:
            self.logger.log_info("\nScheduled task '" + arg_dict['task_name'] + "' does not exist.\n")

        # Pass or fail the test, based on what was expected
        if ui_cmd_obj.return_data is StringUtils.string_to_boolean(arg_dict["exists"]):
            # PASS
            ui_cmd_obj.error_state = False
        else:
            # FAIL
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def scheduledtasks_wait_for_task_add(self, ui_cmd_obj, arg_dict):
        self.ext_builder.wait_for_item_in_table(ui_cmd_obj, 'scheduleGrid gridview', '[0]', 'jobName',
                                                arg_dict['task_name'], None, 60)
        return ui_cmd_obj

    def scheduledtasks_wait_for_task_remove(self, ui_cmd_obj, arg_dict):
        self.ext_builder.wait_for_item_not_in_table(ui_cmd_obj, 'scheduleGrid gridview', '[0]', 'jobName',
                                                    arg_dict['task_name'], None, 60)
        return ui_cmd_obj
