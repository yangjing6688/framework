from extauto.common.CommonValidation import CommonValidation
from robot.libraries.BuiltIn import BuiltIn

class XapiHelper():

    def __init__(self):
        self.common_validation = CommonValidation()
        self.builtin = BuiltIn()

    def set_xapi_configuration(self, value):
        self.builtin.set_global_variable('${XAPI_CONFIGRATION}', value)

    def get_xapi_configuration(self):
        configuration =  self.builtin.get_variable_value('${XAPI_CONFIGRATION}')
        if not configuration:
            raise ('The XAPI configuration was not set, please use the "login_user" method in the Login class with the kwarg XAPI_ENABLED set to True')
        return configuration

    def get_xapi_url(self):
        xapi_url = self.builtin.get_variable_value("${XAPI_URL}")
        if not xapi_url:
            raise ('XAPI url was not set, please use the keyword "set_xapi_url" method in the XapiHelper class to set the XAPI URL')
        else:
            return xapi_url

    def set_xapi_url(self, value):
        self.builtin.set_global_variable("${XAPI_URL}", value)
