from ExtremeAutomation.Apis.ApiGeneration.Beans.DataBean import DataBean


class CliParseDataBean(DataBean):
    def __init__(self):
        super(CliParseDataBean, self).__init__()

        self.interface_method = None

    @property
    def feature(self):
        """
        Property function for feature. Returns the private attribute _features.
        """
        return self._feature

    @feature.setter
    def feature(self, feature):
        """
        Setter function for feature. Sets the private attribute _feature as well as the file_name
        and base_file_name.
        """
        self._feature = feature
        self.file_name = feature.capitalize() + "CustomShowTools.py"
        self.base_file_name = feature.capitalize() + "BaseCustomShowTools.py"
