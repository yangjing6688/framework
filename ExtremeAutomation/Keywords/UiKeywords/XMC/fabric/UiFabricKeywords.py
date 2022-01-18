from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.XMC.FabricConstants import FabricConstants


class UiFabricKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiFabricKeywords, self).__init__()
        self.api_const = self.constants.API_XMC_FABRIC
        self.command_const = FabricConstants()

    def launch_fabric_manager(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names]         - List of elements the keyword will be run against

        Launch Fabric Manager
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.LAUNCH_FABRIC_MANAGER, **kwargs)
