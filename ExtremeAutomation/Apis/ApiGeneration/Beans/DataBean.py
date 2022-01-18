import os


class DataBean(object):
    def __init__(self):
        self.file_name = None
        self.base_file_name = None
        self.data_file_name = None
        self.is_base = False
        self.previous_version = None
        self.uuid = ''

        # Attributes with setter/getter methods.
        self._platform = None
        self._unit = None
        self._version = None
        self._operating_system = None
        self._feature = None

    def get_folders(self):
        """
        Returns all of the given data bean's attributes that are considered folders. If more than
        one folder has the version flag enabled a ValueError is returned. Otherwise the list of
        folders is returned.
        """
        folders = self.define_folders()
        if len([i for i in folders if i[1]]) > 1:
            raise ValueError("Data bean folder attribute must have no more than one folder"
                             "marked as the (application/os version/etc) version folder. ")
        return folders

    def define_folders(self):
        """
        This function defines which of the data bean's attributes are folders that need to be created.
        The default is below. If different or additional folders are needed the child class will
        need to override this function.

        The format is a list of tuples. The first value should be the folders attribute, the second
        is a boolean stating weather or not it is the version field.
        """
        folders = [(self.feature, False),
                   (self.operating_system, False),
                   (self.platform, False),
                   (self.version, True),
                   (self.unit, False)
                   ]

        return folders

    @property
    def platform(self):
        """
        Property function for platform. Returns private attribute _platform.
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """
        Setter function for platform. Verifies that there are no "*" (wildcard) characters
        in the passed <platform>. If none are present set _platform to the passed value.
        """
        if "*" in platform:
            raise Exception("Platform field must not have wildcard values.")
        else:
            self._platform = platform

    @property
    def unit(self):
        """
        Property function for unit. Returns private attribute _unit.
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """
        Setter function for unit. Verifies that there are no "*" (wildcard) characters
        in the passed <unit>. If none are present set _unit to the passed value.
        """
        if "*" in unit:
            raise Exception("Unit field must not have wildcard values.")
        else:
            self._unit = unit

    @property
    def version(self):
        """
        Property function for version. Returns private attribute _version.
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Setter function for version. Runs the passed <version> through the
        convert to version function and sets the result to _version.
        """
        self._version = self.convert_version(version)

    @property
    def operating_system(self):
        """
        Property function for operating_system. Returns private attribute _operating_system.
        """
        return self._operating_system

    @operating_system.setter
    def operating_system(self, operating_system):
        """
        Setter function for operating_system. Uppercases the passed <operating_system> and sets it
        to _operating_system.
        """
        self._operating_system = operating_system.upper()

    @property
    def feature(self):
        """
        Property function for feature. Returns private attribute _feature.
        """
        return self._feature

    @feature.setter
    def feature(self, feature):
        """
        Setter function feature. This exists so that it can be overriden by child classes.
        """
        self._feature = feature

    def get_previous_version_data_path(self, output_dir, previous_version):
        """
        This function returns the path for the previous version of a data file.
        """
        folders = [i[0] if not i[1] else previous_version for i in self.get_folders()]
        return os.path.join(output_dir, "DataTemp", *folders)

    def get_previous_version_api_path(self, output_dir, previous_version):
        """
        This function returns the path for the previous version of an API file.
        """
        folders = [i[0] if not i[1] else previous_version for i in self.get_folders()]
        return os.path.join(output_dir, "ApiTemp", *folders)

    @staticmethod
    def convert_version(version):
        """
        This function converts a dotted notation version into the following.

        8.0.0 -> v8dot0dot0

        This is needed because python folders cannot start with a number and cannot
        contain ".".
        """
        if version[0].isdigit():
            version = "v" + version
        version = version.replace(".", "dot")

        return version
