from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.EWC.EwcleftnavipanelConstants \
    import EwcleftnavipanelConstants


class UiEwcLeftNaviPanelKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiEwcLeftNaviPanelKeywords, self).__init__()
        self.api_const = self.constants.API_EWC_LEFT_NAVI_PANEL
        self.command_const = EwcleftnavipanelConstants()

    def left_navi_panel_select_section_tab(self, element_name, section_name, **kwargs):
        """Returns the result of left_navi_panel_select_section_tab."""
        args = {"section_name": section_name}

        return self.execute_keyword(element_name, args, self.command_const.LEFT_NAVI_PANEL_SELECT_SECTION_TAB, **kwargs)

    def left_navi_panel_select_link_in_section(self, element_name, link_name, **kwargs):
        """Returns the result of left_navi_panel_select_link_in_section."""
        args = {"link_name": link_name}

        return self.execute_keyword(element_name, args,
                                    self.command_const.LEFT_NAVI_PANEL_SELECT_LINK_IN_SECTION, **kwargs)

    def left_navi_panel_expand_tree_node_in_section(self, element_name, link_name, **kwargs):
        """Returns the result of left_navi_panel_expand_tree_node_in_section."""
        args = {"link_name": link_name}

        return self.execute_keyword(element_name, args,
                                    self.command_const.LEFT_NAVI_PANEL_EXPAND_TREE_NODE_IN_SECTION, **kwargs)

    def left_navi_panel_collapse_tree_node_in_section(self, element_name, link_name, **kwargs):
        """Returns the result of left_navi_panel_collapse_tree_node_in_section."""
        args = {"link_name": link_name}

        return self.execute_keyword(element_name, args,
                                    self.command_const.LEFT_NAVI_PANEL_COLLAPSE_TREE_NODE_IN_SECTION, **kwargs)
