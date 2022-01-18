import abc
from ExtremeAutomation.Library.Device.Common.ManagedObject import ManagedObject
from ExtremeAutomation.Library.Device.Common.Factories.ParseApiFactory import ParseApiFactory
from ExtremeAutomation.Library.Device.Common.Factories.CommandApiFactory import CommandApiFactory


class ManagedDeviceObject(ManagedObject, metaclass=abc.ABCMeta):
    def __init__(self):
        super(ManagedDeviceObject, self).__init__()
        self.apis = {}
        self.parse_apis = {}
        self.agents = {}
        self.prompt_handler = None
        self.inspection_toolkit = None
        self.name = ""
        self.platform = ""
        self.unit = ""
        self.version = {}
        self.hostname = ""
        self.port = ""
        self.connection_method = ""
        self.username = ""
        self.password = ""
        self.continue_on_failure = None
        self.agent_kwargs = {}

        # Factories
        self.api_factory = CommandApiFactory()
        self.parse_factory = ParseApiFactory()

        # Attributes with setters/getters.
        self._oper_sys = ""

    @property
    def oper_sys(self):
        """
        Property function for oper_sys. Returns an upper case version of self._oper_sys.
        """
        return self._oper_sys.upper()

    @oper_sys.setter
    def oper_sys(self, oper_sys):
        """
        Setter function for oper_sys. Sets self._oper_sys to an upper case version of the passed <oper_sys>.
        """
        self._oper_sys = oper_sys.upper()

    def get_api(self, name):
        """
        This function gets a command api based on the passed <name>. It uses the
        api_factory created in a child class.
        """
        if name in self.apis:
            return self.apis[name]
        else:
            # Use the factory to retrieve the needed API.
            api = self.api_factory.get_api(self, name)
            if api is not None:
                self.apis[name] = api
                return api

    def get_parse_api(self, name):
        """
        This function is almost the same as get_api, except it uses the parse factory.
        """
        if name in self.parse_apis:
            return self.parse_apis[name]
        else:
            # Use the factory to retrieve the needed API.
            api = self.parse_factory.get_api(self, name)
            if api is not None:
                self.parse_apis[name] = api
                return api

    def get_device_type(self):
        """
        Gets the type of the device object.

        The return looks something like this.
            <class 'ExtremeAutomation.Library.Device.NetworkElement.NetworkElement.NetworkElement'>

        It converts it to a string, splits it on "." then grabs the last index. Finally it strips out
        the "'>" characters and returns the string "NetworkElement", in this case.
        """
        return str(type(self)).split(".")[-1].strip("'>")

    @abc.abstractmethod
    def connect(self, *args, **kwargs):
        """
        Connect method, this abstract method should be overridden in any child class.
        """
        pass

    @abc.abstractmethod
    def disconnect(self, *args, **kwargs):
        """
        Disconnect method, this abstract method should be overridden in any child class.
        """
        pass

    def login(self, *args, **kwargs):
        """
        Login method, this abstract method should be overridden in any child class.
        """
        pass
