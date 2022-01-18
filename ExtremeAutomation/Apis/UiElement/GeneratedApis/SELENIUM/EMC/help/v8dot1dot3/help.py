from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as HelpBase
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


class Help(HelpBase):
    def help_show_context_help(self, ui_cmd_obj, arg_dict):
        self.show_hide_context_help_panel(ui_cmd_obj, True)

        return ui_cmd_obj

    def help_hide_context_help(self, ui_cmd_obj, arg_dict):
        self.show_hide_context_help_panel(ui_cmd_obj, False)

        return ui_cmd_obj

    def help_show_getting_started(self, ui_cmd_obj, arg_dict):
        self.show_hide_getting_started_panel(ui_cmd_obj, True)

        return ui_cmd_obj

    def help_hide_getting_started(self, ui_cmd_obj, arg_dict):
        self.show_hide_getting_started_panel(ui_cmd_obj, False)

        return ui_cmd_obj

    def help_click_pause(self, ui_cmd_obj, arg_dict):
        # Can only click the button if the panel is being displayed
        self.ext_builder.component_query(ui_cmd_obj, 'helpPanel', '[0].collapsed')
        if ui_cmd_obj.return_data is False:
            self.ext_builder.click(ui_cmd_obj, '#helpPanel #pausehelptool => .x-tool-tool-el')
        else:
            self.logger.log_info("\nContext Help panel is not being displayed, so cannot click button to pause help.\n")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def help_click_resume(self, ui_cmd_obj, arg_dict):
        # Can only click the button if the panel is being displayed
        self.ext_builder.component_query(ui_cmd_obj, 'helpPanel', '[0].collapsed')
        if ui_cmd_obj.return_data is False:
            self.ext_builder.click(ui_cmd_obj, '#helpPanel #resumehelptool => .x-tool-tool-el')
        else:
            self.logger.log_info("\nContext Help panel is not being displayed, so cannot click button to resume "
                                 "help.\n")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def help_click_launch_new_tab(self, ui_cmd_obj, arg_dict):
        # Can only click the button if the panel is being displayed
        self.ext_builder.component_query(ui_cmd_obj, 'helpPanel', '[0].collapsed')
        if ui_cmd_obj.return_data is False:
            self.ext_builder.click(ui_cmd_obj, '#helpPanel #launchhelptool => .x-tool-tool-el')
        else:
            self.logger.log_info("\nContext Help panel is not being displayed, so cannot click button to launch new "
                                 "tab.\n")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def help_confirm_context_help_is_visible(self, ui_cmd_obj, arg_dict):
        expected_value = StringUtils.string_to_boolean(arg_dict['is_visible'])

        expected_state = "hidden"
        if expected_value is True:
            expected_state = "shown"

        self.ext_builder.component_query(ui_cmd_obj, 'helpPanel', '[0].collapsed')

        # "collapsed" will return the direction it is collapsed, not "True", so have to check "not False"
        if (ui_cmd_obj.return_data is not False and expected_value is True) or \
           (ui_cmd_obj.return_data is False and expected_value is False):
            self.logger.log_info("\nContext help panel is not at expected state (" + expected_state + ").\n")
            ui_cmd_obj.error_state = True
        else:
            self.logger.log_info("\nContext help panel is at expected state (" + expected_state + ").\n")

        return ui_cmd_obj

    def help_confirm_getting_started_is_visible(self, ui_cmd_obj, arg_dict):
        expected_value = StringUtils.string_to_boolean(arg_dict['is_visible'])

        expected_state = "hidden"
        if expected_value is True:
            expected_state = "shown"

        # Check if the panel exists (if it doesn't, the "collapsed" query will not matter)
        self.ext_builder.component_query(ui_cmd_obj, '#helpGettingStartedPanel', '[0].hidden')
        if ui_cmd_obj.return_data is False:
            self.ext_builder.component_query(ui_cmd_obj, '#helpGettingStartedPanel', '[0].collapsed')
            # "collapsed" will return the direction it is collapsed, not "True", so have to check "not False"
            if (ui_cmd_obj.return_data is not False and expected_value is True) or \
               (ui_cmd_obj.return_data is False and expected_value is False):
                self.logger.log_info("\nGetting Started panel is not at expected state (" + expected_state + ").\n")
                ui_cmd_obj.error_state = True
            else:
                self.logger.log_info("\nGetting Started panel is at expected state (" + expected_state + ").\n")
        else:
            self.logger.log_info("\nGetting Started panel is not present.\n")
            if expected_value is True:
                ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def help_confirm_getting_started_exists(self, ui_cmd_obj, arg_dict):
        # Take the opposite of what is "expected" for the "exists" argument so the boolean compare will read better
        # since we are querying the attribute "hidden"
        expected_to_be_hidden = False
        if not StringUtils.string_to_boolean(arg_dict['exists']):
            expected_to_be_hidden = True

        expected_state = "does not exist"
        if StringUtils.string_to_boolean(arg_dict['exists']):
            expected_state = "exists"

        self.ext_builder.component_query(ui_cmd_obj, '#helpGettingStartedPanel', '[0].hidden')

        if ui_cmd_obj.return_data is not expected_to_be_hidden:
            self.logger.log_info("\nGetting Started panel is not at expected state (" + expected_state + ").\n")
            ui_cmd_obj.error_state = True
        else:
            self.logger.log_info("\nGetting Started panel is at expected state (" + expected_state + ").\n")

        return ui_cmd_obj

    def show_hide_context_help_panel(self, ui_cmd_obj, show_panel):
        self.ext_builder.component_query(ui_cmd_obj, 'helpPanel', '[0].collapsed')

        # "collapsed" will return the direction it is collapsed, not "True", so have to check "not False"
        if (ui_cmd_obj.return_data is not False and show_panel is True) or\
           (ui_cmd_obj.return_data is False and show_panel is False):
            self.ext_builder.click(ui_cmd_obj, '#navToolbarHelp => .fa')
        else:
            panel_state = "hidden"
            if ui_cmd_obj.return_data is False:
                panel_state = "shown"
            self.logger.log_info("\nContext help panel is already " + panel_state + ".\n")

        return ui_cmd_obj

    def show_hide_getting_started_panel(self, ui_cmd_obj, show_panel):
        self.ext_builder.component_query(ui_cmd_obj, '#helpGettingStartedPanel', '[0].collapsed')

        # "collapsed" will return the direction it is collapsed, not "True", so have to check "not False"
        if ui_cmd_obj.return_data is not False and show_panel is True:
            self.ext_builder.click(ui_cmd_obj,
                                   '#helpPanel #helpGettingStartedPanel tool[type=expand-bottom] => .x-tool-tool-el')
        elif ui_cmd_obj.return_data is False and show_panel is False:
            self.ext_builder.click(ui_cmd_obj,
                                   '#helpPanel #helpGettingStartedPanel tool[type=collapse-top] => .x-tool-tool-el')
        else:
            panel_state = "hidden"
            if ui_cmd_obj.return_data is False:
                panel_state = "shown"
            self.logger.log_info("\nGetting Started panel is already " + panel_state + ".\n")

        return ui_cmd_obj
