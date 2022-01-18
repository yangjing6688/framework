from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.EMC.MapsConstants import MapsConstants


class UiMapsKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiMapsKeywords, self).__init__()
        self.api_const = self.constants.API_MAPS
        self.command_const = MapsConstants()

    def maps_create_map(self, element_name, map_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [map_name] -      Name of the map to create

        Creates a new map with the specified name.
        """
        args = {"map_name": map_name}

        return self.execute_keyword(element_name, args, self.command_const.MAPS_CREATE_MAP, **kwargs)

    def maps_delete_map(self, element_name, map_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [map_name] -      Name of the map to delete

        Deletes the map with the specified name.
        """
        args = {"map_name": map_name}

        return self.execute_keyword(element_name, args, self.command_const.MAPS_DELETE_MAP, **kwargs)

    def maps_confirm_map_exists(self, element_name, map_name, exists, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [map_name] -      Name of the map to check for
        [exists] -        Indicates whether or not the map is expected to exist (True/False)

        Verifies whether or not the specified map exists.
        Passes/fails the test based on the expected value, as indicated by the "exists" argument.
        """
        args = {"map_name": map_name,
                "exists": exists}

        return self.execute_keyword(element_name, args, self.command_const.MAPS_CONFIRM_MAP_EXISTS, **kwargs)

    def maps_wait_for_map_add(self, element_name, map_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [map_name] -      Name of the map to wait for being added

        Waits for the specified map to be added to the tree.
        """
        args = {"map_name": map_name}

        return self.execute_keyword(element_name, args, self.command_const.MAPS_WAIT_FOR_MAP_ADD, **kwargs)

    def maps_wait_for_map_remove(self, element_name, map_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [map_name] -      Name of the map to wait for being removed

        Waits for the specified map to be removed from the tree.
        """
        args = {"map_name": map_name}

        return self.execute_keyword(element_name, args, self.command_const.MAPS_WAIT_FOR_MAP_REMOVE, **kwargs)

    def maps_select_map(self, element_name, map_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [map_name] -      Name of the map to create

        Selects map with the specified name.
        """
        args = {"map_name": map_name}

        return self.execute_keyword(element_name, args, self.command_const.MAPS_SELECT_MAP, **kwargs)

    def maps_edit_map(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [map_name] -      Name of the map to create

        Edit Map
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.MAPS_EDIT_MAP, **kwargs)

    def maps_rename_map(self, element_name, map_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [map_name] -      Name of the map to create

        Updates map name
        """
        args = {"map_name": map_name}

        return self.execute_keyword(element_name, args, self.command_const.MAPS_RENAME_MAP, **kwargs)

    def maps_confirm_maps_menu_exists(self, element_name, menu_name, exists=True, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [map_name] -      Name of the map to create

        Updates map name
        """
        args = {"menu_name": menu_name,
                'exists': exists}

        return self.execute_keyword(element_name, args, self.command_const.MAPS_CONFIRM_MAPS_MENU_EXISTS, **kwargs)
