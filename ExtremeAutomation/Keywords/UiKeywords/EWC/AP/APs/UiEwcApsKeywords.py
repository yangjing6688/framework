from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.EWC.EwcapsConstants import EwcapsConstants


class UiEwcApsKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiEwcApsKeywords, self).__init__()
        self.api_const = self.constants.API_EWC_APS
        self.command_const = EwcapsConstants()

    def aps_rename_ap_name(self, element_name, current_ap_name, new_ap_name, **kwargs):
        """Returns the result of aps_rename_ap_name."""
        args = {"current_ap_name": current_ap_name,
                "new_ap_name": new_ap_name}

        return self.execute_keyword(element_name, args, self.command_const.APS_RENAME_AP_NAME, **kwargs)

    def aps_ap_name_should_exist(self, element_name, ap_name, **kwargs):
        """Returns the result of aps_ap_name_should_exist."""
        args = {"ap_name": ap_name}

        return self.execute_keyword(element_name, args, self.command_const.APS_AP_NAME_SHOULD_EXIST, **kwargs)

    def aps_ap_name_should_not_exist(self, element_name, ap_name, **kwargs):
        """Returns the result of aps_ap_name_should_not_exist."""
        args = {"ap_name": ap_name}

        return self.execute_keyword(element_name, args, self.command_const.APS_AP_NAME_SHOULD_NOT_EXIST, **kwargs)

    def aps_edit_ap_environment(self, element_name, ap_name, ap_environment, **kwargs):
        """Returns the result of aps_edit_ap_environment."""
        args = {"ap_name": ap_name,
                "ap_environment": ap_environment}

        return self.execute_keyword(element_name, args, self.command_const.APS_EDIT_AP_ENVIRONMENT, **kwargs)

    def aps_ap_environment_should_exist(self, element_name, ap_name, ap_environment, **kwargs):
        """Returns the result of aps_ap_environment_should_exist."""
        args = {"ap_name": ap_name,
                "ap_environment": ap_environment}

        return self.execute_keyword(element_name, args, self.command_const.APS_AP_ENVIRONMENT_SHOULD_EXIST, **kwargs)
