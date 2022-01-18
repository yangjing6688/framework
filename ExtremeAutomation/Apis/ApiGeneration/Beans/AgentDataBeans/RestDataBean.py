from ExtremeAutomation.Apis.ApiGeneration.Beans.DataBean import DataBean


class RestDataBean(DataBean):
    def __init__(self):
        super(RestDataBean, self).__init__()
        self.uri = None
        self.request_type = None
        self.data_function = None
        self.headers = None

        # Attributes with setter/getter functions.
        self._interface_method = None
        self._ignore_errors = []
        self._add_errors = []

    @property
    def interface_method(self):
        """
        Property function for prompt_arguments. Returns private attribute _prompt_arguments.
        """
        return self._interface_method

    @interface_method.setter
    def interface_method(self, interface_method):
        """
        Setter function for interface_method. Sets _interface_method as well as the data_function attribute.
        """
        self._interface_method = interface_method
        self.data_function = self._interface_method + "_data"

    @property
    def ignore_errors(self):
        """
        Property function for ignore_errors. Returns the private attribute _ignore_errors.
        """
        return self._ignore_errors

    @ignore_errors.setter
    def ignore_errors(self, ignore_errors):
        """
        Setter function for ignore_errors. Checks if <ignore_errors> is not an empty string. If it's not
        create a list of errors to ignore by splitting the passed string on "||".
        """
        if isinstance(ignore_errors, str):
            if ignore_errors != "":
                self._ignore_errors = [i.strip() for i in ignore_errors.split("||")]
        elif isinstance(ignore_errors, list):
            if ignore_errors:
                self._ignore_errors = [i.strip() for i in ignore_errors]

    @property
    def add_errors(self):
        """
        Property function for add_errors. Returns the private attribute _add_errors.
        """
        return self._add_errors

    @add_errors.setter
    def add_errors(self, add_errors):
        """
        Setter function for add_errors. Checks if <add_errors> is not an empty string. If it's not
        create a list of errors to add by splitting the passed string on "||".
        """
        if isinstance(add_errors, str):
            if add_errors != "":
                self._add_errors = [i.strip() for i in add_errors.split("||")]
        elif isinstance(add_errors, list):
            if add_errors:
                self._ignore_errors = [i.strip() for i in add_errors]

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
        self.data_file_name = feature + "Data.py"
