from ExtremeAutomation.Apis.ApiGeneration.Beans.DataBean import DataBean


class UiDataBean(DataBean):
    def __init__(self):
        super(UiDataBean, self).__init__()
        self.application = None
        self.interface_method = None

        # Attributes with setter/getter functions.
        self._app_version = None

    def define_folders(self):
        """
        This function defines which of this data bean's attributes are folders, to be created by
        the generator.
        """
        folders = [(self.feature, False),
                   (self.app_version, True)
                   ]

        return folders

    @property
    def feature(self):
        """
        Property function for feature. Returns the private attribute _feature.
        """
        return self._feature

    @feature.setter
    def feature(self, feature):
        """
        Setter function for feature. Sets the private attribute _feature as well as the file_name,
        base_file_name, and data_file_name.
        """
        self._feature = feature
        self.file_name = feature + ".py"
        self.base_file_name = feature + "base.py"

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
