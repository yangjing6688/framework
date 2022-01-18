"""
This class outlines all the constants for the customreport API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(CustomreportConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class CustomreportConstants(ApiConstants):
    def __init__(self):
        super(CustomreportConstants, self).__init__()
        self.CUSTOMREPORT_CLICK_BOOKMARK = {"constant": "customreport_click_bookmark",
                                            "tags": ["COMMAND_SELENIUM"],
                                            "link": self.link.customreport_click_bookmark}
        self.CUSTOMREPORT_CLICK_EXPORT_TO_CSV = {"constant": "customreport_click_export_to_csv",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.customreport_click_export_to_csv}
        self.CUSTOMREPORT_CLICK_SAVE_TO_REPORT_DESIGNER = {"constant": "customreport_click_save_to_report_designer",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.customreport_click_save_to_report_designer}
        self.CUSTOMREPORT_CLICK_SUBMIT = {"constant": "customreport_click_submit",
                                          "tags": ["COMMAND_SELENIUM"],
                                          "link": self.link.customreport_click_submit}
        self.CUSTOMREPORT_COLLAPSE_DISPLAY_OPTIONS = {"constant": "customreport_collapse_display_options",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.customreport_collapse_display_options}
        self.CUSTOMREPORT_DISPLAY_SET_CHART_TYPE = {"constant": "customreport_display_set_chart_type",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.customreport_display_set_chart_type}
        self.CUSTOMREPORT_DISPLAY_SET_RENDER_AS = {"constant": "customreport_display_set_render_as",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.customreport_display_set_render_as}
        self.CUSTOMREPORT_DISPLAY_SET_TITLE = {"constant": "customreport_display_set_title",
                                               "tags": ["COMMAND_SELENIUM"],
                                               "link": self.link.customreport_display_set_title}
        self.CUSTOMREPORT_DISPLAY_SET_X_AXIS_TITLE = {"constant": "customreport_display_set_x_axis_title",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.customreport_display_set_x_axis_title}
        self.CUSTOMREPORT_DISPLAY_SET_Y_AXIS_TITLE = {"constant": "customreport_display_set_y_axis_title",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.customreport_display_set_y_axis_title}
        self.CUSTOMREPORT_EXPAND_DISPLAY_OPTIONS = {"constant": "customreport_expand_display_options",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.customreport_expand_display_options}
        self.CUSTOMREPORT_SET_CATEGORY = {"constant": "customreport_set_category",
                                          "tags": ["COMMAND_SELENIUM"],
                                          "link": self.link.customreport_set_category}
        self.CUSTOMREPORT_SET_STATISTIC = {"constant": "customreport_set_statistic",
                                           "tags": ["COMMAND_SELENIUM"],
                                           "link": self.link.customreport_set_statistic}
        self.CUSTOMREPORT_SET_TARGET_TYPE = {"constant": "customreport_set_target_type",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.customreport_set_target_type}
        self.CUSTOMREPORT_SET_TARGET_VALUE = {"constant": "customreport_set_target_value",
                                              "tags": ["COMMAND_SELENIUM"],
                                              "link": self.link.customreport_set_target_value}
        self.CUSTOMREPORT_SET_TIME_PERIOD = {"constant": "customreport_set_time_period",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.customreport_set_time_period}
