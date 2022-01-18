"""
This class outlines all the constants for the eciqmlinsights API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(EciqmlinsightsConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class EciqmlinsightsConstants(ApiConstants):
    def __init__(self):
        super(EciqmlinsightsConstants, self).__init__()
        self.ML_INSIGHTS_COMPARATIVE_ANALYTICS_POPUP_CLICK_DONE_BUTTON = {"constant": "ml_insights_comparative_analytics_popup_click_done_button",
                                                                          "tags": ["COMMAND_SELENIUM"],
                                                                          "link": self.link.ml_insights_comparative_analytics_popup_click_done_button}
