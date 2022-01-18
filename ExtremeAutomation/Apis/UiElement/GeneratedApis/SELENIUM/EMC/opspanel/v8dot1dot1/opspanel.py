from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as OpspanelBase
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils
import time


class Opspanel(OpspanelBase):
    def opspanel_click_operations(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(ui_cmd_obj, '[itemId=operationStatusBtn]', '[0].pressed')
        if ui_cmd_obj.return_data is False:
            self.ext_builder.click(ui_cmd_obj, '#basic-statusbar #operationStatusBtn => '
                                               '.x-btn-inner-extr-nav-action-toolbar-button-small')
        return ui_cmd_obj

    def opspanel_click_clear_all(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(ui_cmd_obj, '[stateId=operationStatusGrid]', '[0].store.totalCount')
        if ui_cmd_obj.return_data >= 1:
            self.ext_builder.right_click(ui_cmd_obj, 'operationStatusGrid gridview => .x-grid-group-hd')
            self.ext_builder.click(ui_cmd_obj, 'menu{isVisible()} menuitem[text=Clear All] => .x-menu-item-text')
        return ui_cmd_obj

    def opspanel_confirm_type_exists(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(ui_cmd_obj, '[viewId=operationStatusGrid]',
                                         '[0].store.data.items[0].data.type')
        if ui_cmd_obj.return_data == arg_dict['operation_type'] and StringUtils.string_to_boolean(arg_dict['exists']) \
                is True:
            ui_cmd_obj.error_state = False
        else:
            ui_cmd_obj.error_state = True
        return ui_cmd_obj

    def opspanel_confirm_result_exists(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(ui_cmd_obj, '[viewId=operationStatusGrid]',
                                         '[0].store.data.items[0].data.result')
        if ui_cmd_obj.return_data == arg_dict['msg_result'] and StringUtils.string_to_boolean(arg_dict['exists']) \
                is True:
            ui_cmd_obj.error_state = False
        else:
            ui_cmd_obj.error_state = True
        return ui_cmd_obj

    def opspanel_confirm_message_exists(self, ui_cmd_obj, arg_dict):
        data_attempts = 0
        while data_attempts <= int(arg_dict['max_wait']):
            self.ext_builder.component_query(ui_cmd_obj, '[viewId=operationStatusGrid]',
                                             '[0].store.data.length')
            self.ext_builder.component_query(ui_cmd_obj, '[viewId=operationStatusGrid]',
                                             '[0].store.data.items[0].data.msg')
            if ui_cmd_obj.return_data == arg_dict['message'] and StringUtils.string_to_boolean(arg_dict['exists']) \
                    is True:
                ui_cmd_obj.error_state = False
                return ui_cmd_obj
            else:
                ui_cmd_obj.error_state = True
                data_attempts += 1
                time.sleep(1)
        return ui_cmd_obj

    def opspanel_confirm_target_exists(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(ui_cmd_obj, '[viewId=operationStatusGrid]',
                                         '[0].store.data.items[0].data.target')
        if ui_cmd_obj.return_data == arg_dict['target'] and StringUtils.string_to_boolean(arg_dict['exists']) \
                is True:
            ui_cmd_obj.error_state = False
        else:
            ui_cmd_obj.error_state = True
        return ui_cmd_obj

    def opspanel_confirm_all_parameters_exist(self, ui_cmd_obj, arg_dict):
        attempts = 0
        match = False
        while attempts <= int(arg_dict['max_attempts']) and not match:
            current_row = 0
            self.ext_builder.component_query(ui_cmd_obj, '[viewId=operationStatusGrid]', '[0].store.data.length')
            total_length = int(ui_cmd_obj.return_data)
            while current_row < total_length and not match:
                match = True
                if arg_dict['event_type'] is not None:
                    self.ext_builder.component_query(ui_cmd_obj, '[viewId=operationStatusGrid]',
                                                     '[0].store.data.items[' + str(current_row) + '].data.type')

                    if arg_dict['event_type'] != ui_cmd_obj.return_data:
                        match = False
                        current_row += 1
                        continue
                if arg_dict['event_target'] is not None:
                    self.ext_builder.component_query(ui_cmd_obj, '[viewId=operationStatusGrid]',
                                                     '[0].store.data.items[' + str(current_row) + '].data.target')

                    arg_dict_target_no_whitespace = arg_dict['event_target'].replace(' ', '')
                    event_target_no_whitespace = ui_cmd_obj.return_data.replace(' ', '')
                    if arg_dict_target_no_whitespace not in event_target_no_whitespace:
                        match = False
                        current_row += 1
                        continue
                if arg_dict['event_result'] is not None:
                    self.ext_builder.component_query(ui_cmd_obj, '[viewId=operationStatusGrid]',
                                                     '[0].store.data.items[' + str(current_row) + '].data.result')

                    if arg_dict['event_result'] != ui_cmd_obj.return_data:
                        match = False
                        current_row += 1
                        continue
                if arg_dict['event_message'] is not None:
                    self.ext_builder.component_query(ui_cmd_obj, '[viewId=operationStatusGrid]',
                                                     '[0].store.data.items[' + str(current_row) + '].data.msg')

                    arg_dict_message_no_whitespace = arg_dict['event_message'].replace(' ', '')
                    event_message_no_whitespace = ui_cmd_obj.return_data.replace(' ', '')
                    if arg_dict_message_no_whitespace not in event_message_no_whitespace:
                        match = False
                        current_row += 1
                        continue
            attempts += 1
            time.sleep(1)
        if match != StringUtils.string_to_boolean(arg_dict['exists']):
            ui_cmd_obj.error_state = True
            current_row = 0
            self.ext_builder.component_query(ui_cmd_obj, '[viewId=operationStatusGrid]', '[0].store.data.length')
            total_length = int(ui_cmd_obj.return_data)
            while current_row < total_length:
                self.ext_builder.component_query(ui_cmd_obj, '[viewId=operationStatusGrid]',
                                                 '[0].store.data.items[' + str(current_row) +
                                                 '].data.type')
                event_type = ui_cmd_obj.return_data
                self.ext_builder.component_query(ui_cmd_obj, '[viewId=operationStatusGrid]',
                                                 '[0].store.data.items[' + str(current_row) +
                                                 '].data.target')
                event_target = ui_cmd_obj.return_data
                self.ext_builder.component_query(ui_cmd_obj, '[viewId=operationStatusGrid]',
                                                 '[0].store.data.items[' + str(current_row) +
                                                 '].data.result')
                event_result = ui_cmd_obj.return_data
                self.ext_builder.component_query(ui_cmd_obj, '[viewId=operationStatusGrid]',
                                                 '[0].store.data.items[' + str(current_row) +
                                                 '].data.msg')
                event_message = ui_cmd_obj.return_data

                self.logger.log_info("Failed OpsPanel Parameters: \n" +
                                     "event_type=" + event_type + "\n" +
                                     "event_target=" + event_target + "\n" +
                                     "event_result=" + event_result + "\n" +
                                     "event_message=" + event_message + "\n"
                                     )
                current_row += 1

        return ui_cmd_obj
