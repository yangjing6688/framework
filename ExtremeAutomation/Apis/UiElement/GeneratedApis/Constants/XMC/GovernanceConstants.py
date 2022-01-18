"""
This class outlines all the constants for the governance API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(GovernanceConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class GovernanceConstants(ApiConstants):
    def __init__(self):
        super(GovernanceConstants, self).__init__()
        self.ADD_REGIME = {"constant": "add_regime",
                           "tags": ["COMMAND_SELENIUM"],
                           "link": self.link.add_regime}
        self.DELETE_REGIME = {"constant": "delete_regime",
                              "tags": ["COMMAND_SELENIUM"],
                              "link": self.link.delete_regime}
        self.EDIT_REGIME = {"constant": "edit_regime",
                            "tags": ["COMMAND_SELENIUM"],
                            "link": self.link.edit_regime}
        self.ENTER_REGIME_DETAILS = {"constant": "enter_regime_details",
                                     "tags": ["COMMAND_SELENIUM"],
                                     "link": self.link.enter_regime_details}
        self.RUN_REGIME = {"constant": "run_regime",
                           "tags": ["COMMAND_SELENIUM"],
                           "link": self.link.run_regime}
        self.SELECT_AND_MOVE_SINGLE_DEVICE = {"constant": "select_and_move_single_device",
                                              "tags": ["COMMAND_SELENIUM"],
                                              "link": self.link.select_and_move_single_device}
        self.SELECT_REGIME = {"constant": "select_regime",
                              "tags": ["COMMAND_SELENIUM"],
                              "link": self.link.select_regime}
        self.VERIFY_REGIME_EXISTS = {"constant": "verify_regime_exists",
                                     "tags": ["COMMAND_SELENIUM"],
                                     "link": self.link.verify_regime_exists}
        self.VERIFY_SYSTEM_REGIME_IS_NON_EDITABLE = {"constant": "verify_system_regime_is_non_editable",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.verify_system_regime_is_non_editable}
        self.VERIFY_SYSTEM_REGIME_IS_NON_REMOVABLE = {"constant": "verify_system_regime_is_non_removable",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.verify_system_regime_is_non_removable}
