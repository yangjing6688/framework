from extauto.common.Cli import Cli
from extauto.common.Utils import Utils
from extauto.common.CommonValidation import CommonValidation

class Debugging(object):

    def __init__(self):
        self.cli = Cli()
        self.utils = Utils()
        self.common_validation = CommonValidation()
        self.default_command_list = [' _debug capwap cli', '_debug capwap hvcom', '_debug capwap basic', '_debug capwap info']

    def enable_debug_commands(self, ip, port, username, password, cli_type, commands=None, **kwargs):
        """
        - Enables debug commands on a device
        - Keyword Usage
         - ``Enable Debug Commands``
        :param spawn: device spawn
        :param ip: Ip address of the device under test
        :param port: Communication port
        :param username: Username to log into device
        :param password: Password to log into device
        :param cli_type: Device type
        :param commands: Debug commands to send to device
        :return: if sucessful return output from cli else return empty string
        """
        cli_output = ""
        if not commands:
            commands = self.default_command_list
        self.utils.print_info("Debug command will be sent to device " + ip + " port " + port)
        spawn = self.cli.open_spawn(ip, port, username, password, cli_type, connection_method='ssh')
        if not spawn:
            kwargs['fail_msg'] = "Unable to open span"
            self.common_validation.failed(**kwargs)
            return ""
        cli_output = self.send_commands(spawn, commands)
        if not cli_output:
            kwargs['fail_msg'] = "Data not returned from Cli"
            self.common_validation.failed(**kwargs)
            return ""
        return_value = self.cli.close_spawn(spawn)
        if return_value != 1:
            kwargs['fail_msg'] = "Issue closing spawn"
            self.common_validation.failed(**kwargs)
            return ""
        if cli_output:
            kwargs['pass_msg'] = "Commands successfully sent to device"
            self.common_validation.passed(**kwargs)
            return 1
