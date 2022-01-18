from ExtremeAutomation.Library.Device.Common.CommandObjects.CommandObject import CommandObject


class RestCommandObject(CommandObject):
    def __init__(self):
        super(RestCommandObject, self).__init__()

        self.data = None
        self.return_status_code = None
        self.return_status_text = None
        self.response = None
        self.full_uri = None
        self.headers = None

        # Attributes with setter/getter.
        self._uri = None
        self._request_type = None

    @property
    def uri(self):
        """
        Property function for uri, this function returns the private attribute _uri.
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Setter function for uri. This function sets _uri to the passed <uri> and creates a command
        based on the uri and request_type (if they have both been set).
        """
        self._uri = uri
        self.__set_command()

    @property
    def request_type(self):
        """
        Property function for request type, this function returns the private attribute _request_type.
        """
        return self._request_type

    @request_type.setter
    def request_type(self, request_type):
        """
        Setter function for request type. This function sets the _request_type to the passed <request_type>
        and creates a command based on the uri and request_type (if they have both been set).
        """
        self._request_type = request_type
        self.__set_command()

    def __set_command(self):
        """
        This function returns a command string using the uri and request_type as long as neither is
        currently set ot None.

        For example:
        uri = http://test.com/route
        request_type = post

        Return:
        post http://test.com/route
        """
        if self._uri is not None and self._request_type is not None:
            self.command = self.request_type + " " + self.uri
