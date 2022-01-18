"""
This class outlines all the constants for the dfndrwizard API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(DfndrwizardConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class DfndrwizardConstants(ApiConstants):
    def __init__(self):
        super(DfndrwizardConstants, self).__init__()
        self.DFNDR_CLEANUP_FOR_WIZARD_RUN = {"constant": "dfndr_cleanup_for_wizard_run",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.dfndr_cleanup_for_wizard_run}
        self.DFNDR_WIZARD_CONFIGURATION = {"constant": "dfndr_wizard_configuration",
                                           "tags": ["COMMAND_SELENIUM"],
                                           "link": self.link.dfndr_wizard_configuration}
