from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.EMC.ReportdesignerConstants import ReportdesignerConstants


class UiReportDesignerKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiReportDesignerKeywords, self).__init__()
        self.api_const = self.constants.API_REPORT_DESIGNER
        self.command_const = ReportdesignerConstants()

    def reportdesigner_click_new(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks "New..." on the toolbar.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.REPORTDESIGNER_CLICK_NEW, **kwargs)
