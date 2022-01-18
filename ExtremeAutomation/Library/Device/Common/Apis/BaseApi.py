from ExtremeAutomation.Library.Logger.Logger import Logger
from ExtremeAutomation.Library.Device.Common.CommandObjects.CommandObject import CommandObject


class BaseApi(object):
    def __init__(self):
        self.logger = Logger()

    @staticmethod
    def base_function(*args, **kwargs):
        """
        This is the function that should be executed if an API function cannot be found.
        """
        cmd_obj = CommandObject()
        cmd_obj.not_supported = True

        return cmd_obj

    def __getattr__(self, item):
        # Return the base_function if the called function does not exist.
        return self.base_function

    @staticmethod
    def get_location():
        """
        This function returns the location of a given API.
        """
        return __file__.replace(".pyc", ".py")
