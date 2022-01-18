from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.GIM.GimfilemanagerConstants import GimfilemanagerConstants


class UiGimFileManagerKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiGimFileManagerKeywords, self).__init__()
        self.api_const = self.constants.API_GIM_FILE_MANGER
        self.command_const = GimfilemanagerConstants()

    def gim_fm_pref_tab_exist(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against

        Validates the existence of File Manager option under Preferences tab
        """
        args = {

        }

        return self.execute_keyword(element_name, args, self.command_const.FM_PREF_TAB_EXIST, **kwargs)

    def gim_fm_default_sample_files(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against

        Validates the existence of Default sample files under File Manager option
        """
        args = {

        }

        return self.execute_keyword(element_name, args, self.command_const.FM_DEFAULT_SAMPLE_FILES, **kwargs)

    def gim_fm_contents_under_file_manager(self, element_name, file_name, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against
        [file_name]    - File Name Available under File Manager

        Validates the Default states of Add, Download and Delete buttons
        """
        args = {"file_name": file_name
                }

        return self.execute_keyword(element_name, args, self.command_const.FM_CONTENTS_UNDER_FILE_MANAGER, **kwargs)

    def gim_fm_file_manager_availability(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against

        Validates the existence of Default sample files under File Manager option
        """
        args = {

        }

        return self.execute_keyword(element_name, args, self.command_const.FM_FILE_MANAGER_AVAILABILITY, **kwargs)
