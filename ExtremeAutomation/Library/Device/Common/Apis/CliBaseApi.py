from ExtremeAutomation.Library.Device.Common.Apis.BaseApi import BaseApi
from ExtremeAutomation.Library.Device.Common.CommandObjects.CliCommandObject import CliCommandObject


class CliBaseApi(BaseApi):
    @staticmethod
    def create_cmd_obj(uuid, cmd, prompt=None, prompt_args=None, conf=None, conf_args=None):
        """Creates the command object to send to the current_agent."""
        cmd_obj = CliCommandObject()

        cmd_obj.command = cmd
        cmd_obj.uuid = uuid

        if prompt:
            cmd_obj.prompt = prompt

        if prompt_args:
            cmd_obj.prompt_args = prompt_args

        if conf:
            cmd_obj.confirmation_phrases = conf

        if conf_args:
            cmd_obj.confirmation_args = conf_args

        return cmd_obj
