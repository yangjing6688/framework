import json
from ExtremeAutomation.Library.Device.Common.Apis.BaseApi import BaseApi
from ExtremeAutomation.Library.Device.Common.CommandObjects.RestCommandObject import RestCommandObject


class RestBaseApi(BaseApi):
    @staticmethod
    def create_cmd_obj(uri, request_type, data_func=None, data_func_args=None, headers=None):
        """Creates the command object to send to the current_agent."""
        cmd_obj = RestCommandObject()

        cmd_obj.uri = uri
        cmd_obj.request_type = request_type

        if data_func:
            if data_func_args is None:
                raise ValueError("data_func_args must be supplied if a data_func is passed\n"
                                 "This is probably an issue with the REST API generation.")
            cmd_obj.data = json.dumps(data_func(data_func_args))

        if headers:
            cmd_obj.headers = headers

        return cmd_obj
