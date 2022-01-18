from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.DFNDR.DfndrinventoryConstants \
    import DfndrinventoryConstants


class UiDfndrInventoryKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiDfndrInventoryKeywords, self).__init__()
        self.api_const = self.constants.API_DFN_INVENTORY
        self.command_const = DfndrinventoryConstants()
