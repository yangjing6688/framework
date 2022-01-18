from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.EMC.AlarmsandeventsConstants \
    import AlarmsandeventsConstants


class UiAlarmsAndEventsKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiAlarmsAndEventsKeywords, self).__init__()
        self.api_const = self.constants.API_ALARMSANDEVENTS
        self.cmd = AlarmsandeventsConstants()

    def alarmsandevents_select_sub_tab(self, element_name, tab_name, **kwargs):
        """Returns the result of alarmsandevents_select_sub_tab."""
        args = {"tab_name": tab_name}

        return self.execute_keyword(element_name, args, self.cmd.ALARMSANDEVENTS_SELECT_SUB_TAB, **kwargs)
