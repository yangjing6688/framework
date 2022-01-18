from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.ECIQ.EciqcommonobjectsConstants import \
    EciqcommonobjectsConstants


class UiEciqCommonObjectsKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiEciqCommonObjectsKeywords, self).__init__()
        self.api_const = self.constants.API_ECIQ_COMMON_OBJECTS
        self.command_const = EciqcommonobjectsConstants()

    def eciq_common_objects_expand_section(self, element_name, section_name, **kwargs):
        """
        Returns the result of common_objects_expand_section.
        [element_name] - The UI element(s) the keyword should be run against.
        [section_name] - The section to be expanded.
        """
        args = {"section_name": section_name}

        return self.execute_keyword(element_name, args, self.command_const.COMMON_OBJECTS_EXPAND_SECTION, **kwargs)

    def eciq_common_objects_collapse_section(self, element_name, section_name, **kwargs):
        """
        Returns the result of common_objects_collapse_section.
        [element_name] - The UI element(s) the keyword should be run against.
        [section_name] - The section to be collapsed.
        """
        args = {"section_name": section_name}

        return self.execute_keyword(element_name, args, self.command_const.COMMON_OBJECTS_COLLAPSE_SECTION, **kwargs)

    def eciq_common_objects_select_sub_section(self, element_name, section_name, sub_section_name, **kwargs):
        """
        Returns the result of common_objects_select_sub_section.
        [element_name] - The UI element(s) the keyword should be run against.
        [section_name] - The section containing the sub_section.
        [sub_section_name] - The sub_section to be selected.
        """
        args = {"section_name": section_name,
                "sub_section_name": sub_section_name}

        return self.execute_keyword(element_name, args, self.command_const.COMMON_OBJECTS_SELECT_SUB_SECTION, **kwargs)
