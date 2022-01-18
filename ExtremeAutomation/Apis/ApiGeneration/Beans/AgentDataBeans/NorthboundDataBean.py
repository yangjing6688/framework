from ExtremeAutomation.Apis.ApiGeneration.Beans.DataBean import DataBean


class NorthboundDataBean(DataBean):
    def __init__(self):
        super(NorthboundDataBean, self).__init__()
        self.data = None
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
        self.file_name = feature + ".py"
        self.base_file_name = feature + "base.py"
