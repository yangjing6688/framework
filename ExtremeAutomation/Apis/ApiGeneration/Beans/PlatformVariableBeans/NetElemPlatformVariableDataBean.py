from ExtremeAutomation.Apis.ApiGeneration.Beans.DataBean import DataBean


class NetElemPlatformVariableDataBean(DataBean):
    def __init__(self):
        super(NetElemPlatformVariableDataBean, self).__init__()

        self.variable_name = None
        self.variable_value = None
        self.file_name = "PlatformVariables.py"

    def define_folders(self):
        """
        This function defines which of this data bean's attributes are folders, to be created by
        the generator.
        """
        folders = [(self.operating_system, False),
                   (self.platform, False),
                   (self.version, False),
                   (self.unit, False)
                   ]

        return folders
