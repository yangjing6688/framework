from ExtremeAutomation.Apis.ApiGeneration.Beans.DataBean import DataBean


class UiElementPlatformVariableDataBean(DataBean):
    def __init__(self):
        super(UiElementPlatformVariableDataBean, self).__init__()

        self.variable_name = None
        self.application = None
        self.host_os = None
        self.variable_value = None
        self.file_name = "PlatformVariables.py"

        # Attributes with setter/getter functions.
        self._app_version = None

    def define_folders(self):
        """
        This function defines which of this data bean's attributes are folders, to be created by
        the generator.
        """
        folders = [(self.application, False),
                   (self.app_version, True),
                   ]

        return folders

    @property
    def app_version(self):
        """
        Property function for app_version. Returns private attribute _app_version.
        """
        return self._app_version

    @app_version.setter
    def app_version(self, app_version):
        """
        Setter function for app_version. Runs the passed <app_version> through the
        convert to version function and sets the result to _app_version.
        """
        self._app_version = self.convert_version(app_version)
