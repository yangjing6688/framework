from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.DFNDR.DfndrwizardConstants \
    import DfndrwizardConstants


class UiDfndrWizardKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiDfndrWizardKeywords, self).__init__()
        self.api_const = self.constants.API_DFN_WIZARD
        self.command_const = DfndrwizardConstants()

    def dfndr_cleanup_for_wizard_run(self, element_name, def_site, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against

        Will used to cleanup xca for re-running the wizard
        """
        args = {
            "def_site": def_site
        }

        return self.execute_keyword(element_name, args, self.command_const.DFNDR_CLEANUP_FOR_WIZARD_RUN, **kwargs)

    def dfndr_wizard_configuration(self, element_name, country_name, time_zone, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against

        Running a Defender wizard to configure XCA
        """
        args = {
            "country_name": country_name,
            "time_zone": time_zone
        }

        return self.execute_keyword(element_name, args, self.command_const.DFNDR_WIZARD_CONFIGURATION, **kwargs)
