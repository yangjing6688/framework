from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.ECIQ.EciqmlinsightsConstants import \
    EciqmlinsightsConstants


class UiEciqMLinsightsKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiEciqMLinsightsKeywords, self).__init__()
        self.api_const = self.constants.API_ECIQ_ML_INSIGHTS
        self.command_const = EciqmlinsightsConstants()

    def eciq_ml_insights_comparative_analytics_popup_click_done_button(self, element_name, **kwargs):
        """
        Returns the result of ml_insights_comparative_analytics_popup_click_done_button.
        [element_name] - The UI element(s) the keyword should be run against.
        """
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.ML_INSIGHTS_COMPARATIVE_ANALYTICS_POPUP_CLICK_DONE_BUTTON,
                                    **kwargs)
