from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.EMC.CustomreportConstants import CustomreportConstants


class UiCustomReportKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiCustomReportKeywords, self).__init__()
        self.api_const = self.constants.API_CUSTOM_REPORT
        self.command_const = CustomreportConstants()

    def customreport_click_submit(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the "Submit" button.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.CUSTOMREPORT_CLICK_SUBMIT, **kwargs)
