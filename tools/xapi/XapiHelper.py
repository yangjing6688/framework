from extauto.common.CommonValidation import CommonValidation
from robot.libraries.BuiltIn import BuiltIn

class XapiHelper():

    def __init__(self):
        self.common_validation = CommonValidation()
        self.builtin = BuiltIn()

    def set_xapi_global_device(self, value, id):
        """
            This will set the data on the global level for the mapping of device (serial, name or mac) to xapi ID

        :param value: The value for the type (device serial, device name, device mac)
        :param id: The device XAPI ID
        :return: None
        """
        configuration = self.builtin.get_variable_value('${XAPI_GLOBAL_DEVICE}')
        if configuration == None:
            # Create a new object
            self.builtin.set_global_variable('${XAPI_GLOBAL_DEVICE}', {})
            # Get the new object and continue
            configuration = self.builtin.get_variable_value('${XAPI_GLOBAL_DEVICE}')

        # Next add / replace the value
        configuration.update({value:id})

    def delete_xapi_global_device(self, value):
        """
            This will delete the data on the global level for the mapping of device (serial, name or mac) to xapi ID

        :param value: The value for the type (device serial, device name, device mac)
        :return: None
        """
        configuration = self.builtin.get_variable_value('${XAPI_GLOBAL_DEVICE}')
        if configuration != None:
            del configuration[value]

    def get_xapi_global_device(self, value):
        """
           This will set the data on the global level for the mapping of device (serial, name or mac) to xapi ID

        :param value: The value for the type (device serial, device name, device mac)
        :return: The value if found or -1 if not found
        """
        id = -1
        configuration = self.builtin.get_variable_value('${XAPI_GLOBAL_DEVICE}')
        if configuration:
            id = configuration.get(value, -1)
        return id

    def set_xapi_configuration(self, value):
        """
            This function sets the global configuration for the XAPI

        :param value: The configuration object
        :return: None
        """
        self.builtin.set_global_variable('${XAPI_CONFIGRATION}', value)

    def get_xapi_configuration(self):
        """
           This function sets the global configuration for the XAPI

       :param value: The configuration object
       :return: None
       """
        configuration =  self.builtin.get_variable_value('${XAPI_CONFIGRATION}')
        if not configuration:
            raise Exception('The XAPI configuration was not set, please use the "login_user" method in the Login class with the kwarg XAPI_ENABLE set to True. Also ensure that the xapi_url is set in the topo file.')
        return configuration

    def get_xapi_url(self):
        """
            Gets the xapi URL
        :return: the xpai URL or returns None if it is not set
        """
        try:
            xapi_url = self.builtin.get_variable_value("${XAPI_URL}", default=None)
            if not xapi_url:
                print('XAPI url was not set, please make sure the xapi_url is set in the topo file')
                return None
            else:
                return xapi_url
        except Exception:
            raise Exception('XAPI url was not set, please make sure the xapi_url is set in the topo file')
            return None

    def set_xapi_url(self, value):
        """
            Sets the XAPI URL globally
        :param value: The xapi_url
        :return: None
        """
        self.builtin.set_global_variable("${XAPI_URL}", value)

    def is_xapi_enabled(self, **kwargs):
        """
            Checks to see if the XAPI_ENABLE is set globally or in the kwargs
        :param kwargs: dict for kwargs
        :return: True if the XAPI_ENABLE is set, False if it isn't set
        """
        # old way 'access_token'
        old_access_token_kwargs = kwargs.get('access_token', False)
        xapi_enabled_globally = self.builtin.get_variable_value("${XAPI_ENABLE}", False)
        xapi_enabled_kwargs = kwargs.get('XAPI_ENABLE', False)
        if xapi_enabled_globally or xapi_enabled_kwargs or old_access_token_kwargs:
            return True
        else:
            return False

    def set_xapi_enabled_value(self, value):
        """
            Sets the XAPI_ENABLE value globally
        :param value: The XAPI_ENABLE value
        :return: None
        """
        self.builtin.set_global_variable("${XAPI_ENABLE}", value)
