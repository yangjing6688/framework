from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.EMC.DevicegroupsConstants import DevicegroupsConstants


class UiDeviceGroupsKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiDeviceGroupsKeywords, self).__init__()
        self.api_const = self.constants.API_DEVICE_GROUPS
        self.command_const = DevicegroupsConstants()

    def devicegroups_create_device_group(self, element_name, group_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [group_name] -    Name of the device group to create

        Creates a new device group with the specified name.
        """
        args = {"group_name": group_name}

        return self.execute_keyword(element_name, args, self.command_const.DEVICEGROUPS_CREATE_DEVICE_GROUP, **kwargs)

    def devicegroups_delete_device_group(self, element_name, group_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [group_name] -    Name of the device group to delete

        Deletes the device group with the specified name.
        """
        args = {"group_name": group_name}

        return self.execute_keyword(element_name, args, self.command_const.DEVICEGROUPS_DELETE_DEVICE_GROUP, **kwargs)

    def devicegroups_rename_device_group(self, element_name, group_name, new_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [group_name] -    Name of the device group to rename
        [new_name] -      New name for the device group

        Renames the specified device group.
        """
        args = {"group_name": group_name,
                "new_name": new_name}

        return self.execute_keyword(element_name, args, self.command_const.DEVICEGROUPS_RENAME_DEVICE_GROUP, **kwargs)

    def devicegroups_confirm_device_group_exists(self, element_name, group_name, exists, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [group_name] -    Name of the device group to check for
        [exists] -        Indicates whether or not the device group is expected to exist (True/False)

        Verifies whether or not the specified device group exists.
        Passes/fails the test based on the expected value, as indicated by the "exists" argument.
        """
        args = {"group_name": group_name,
                "exists": exists}

        return self.execute_keyword(element_name, args, self.command_const.DEVICEGROUPS_CONFIRM_DEVICE_GROUP_EXISTS,
                                    **kwargs)

    def devicegroups_wait_for_device_group_add(self, element_name, group_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [group_name] -    Name of the device group to wait for being added

        Waits for the specified device group to be added to the tree.
        """
        args = {"group_name": group_name}

        return self.execute_keyword(element_name, args, self.command_const.DEVICEGROUPS_WAIT_FOR_DEVICE_GROUP_ADD,
                                    **kwargs)

    def devicegroups_wait_for_device_group_remove(self, element_name, group_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [group_name] -    Name of the device group to wait for being removed

        Waits for the specified device group to be removed from the tree.
        """
        args = {"group_name": group_name}

        return self.execute_keyword(element_name, args, self.command_const.DEVICEGROUPS_WAIT_FOR_DEVICE_GROUP_REMOVE,
                                    **kwargs)
