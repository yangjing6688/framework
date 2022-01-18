from ExtremeAutomation.Apis.UiElement.GeneratedApis.SELENIUM.EMC.archives.v8dot1dot1.archives import Archives as \
    ArchivesBase
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


class Archives(ArchivesBase):
    def archives_dialog_view_config_file_line_contains(self, ui_cmd_obj, arg_dict):
        # Ensure config file dialog box is in focus
        self.ext_builder.click(ui_cmd_obj,
                               "viewArchiveConfigWindow[title=Configuration File Viewer] "
                               "title[text=Configuration File Viewer] => .x-title-text")

        # Get the config file text
        self.ext_builder.component_query(ui_cmd_obj, 'codemirror[name=configFileContent]', '[0].value')
        config_text = ui_cmd_obj.return_data

        # Split the text into lines
        line_list = config_text.split('\n')
        found_value = False
        the_line = ""
        for the_line in line_list:
            self.logger.log_debug("\n  CHECK LINE: '" + the_line + "'")
            # Split the strings to search for
            value_list = arg_dict['value_list'].split(",")
            for the_value in value_list:
                self.logger.log_debug("  CHECK VALUE: '" + the_value + "'")
                # Determine if the value exists on the line
                if the_line.find(the_value) != -1:
                    self.logger.log_debug("    FOUND VALUE ON THIS LINE - breaking.")
                    found_value = True
                else:
                    found_value = False
                    break

            # If all strings were found on this line, break out of the loop
            if found_value is True:
                break

        # Log the result
        if found_value is True:
            self.logger.log_info("\nFound all strings in '" + arg_dict['value_list'] + "' on line \n'" + the_line +
                                 "'.\n")
        else:
            self.logger.log_info("\nDid not find any line which contained all strings in '" + arg_dict['value_list'] +
                                 "'.\n")

        # Pass or fail the test, based on what was expected
        if found_value is StringUtils.string_to_boolean(arg_dict["exists"]):
            # PASS
            ui_cmd_obj.error_state = False
        else:
            # FAIL
            ui_cmd_obj.error_state = True

        return ui_cmd_obj
