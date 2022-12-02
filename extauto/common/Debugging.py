from extauto.common.Cli import Cli
from extauto.common.Utils import Utils
from extauto.common.CommonValidation import CommonValidation


class Debugging(object):

    def __init__(self):
        self.cli = Cli()
        self.utils = Utils()
        self.common_validation = CommonValidation()
        self.default_enable_command_string = '_debug capwap cli,_debug capwap hvcom,_debug capwap basic,'\
                                             '_debug capwap info,_debug capwap stat,_debug capwap delay'
        self.default_disable_command_string = 'no _debug capwap cli,no _debug capwap hvcom,no _debug capwap basic,'\
                                              'no _debug capwap info,no _debug capwap stat,no _debug capwap delay'
        self.default_log_command_string = 'show capwap client,show idm,show logging buffered,_show capwap event,'\
                                          '_show capwap event buff,_show capwap cli buffer,_show capwap alarms buffer,'\
                                          '_show capwap hvcom status,show tech'

    def run_diagnostic_debug_commands(self, dut, device_spawn, commands=None, **kwargs):
        """
        - Run Diagnostic Debug Commands on a device
        - Keyword Usage
         - ``Run Diagnostic Debug Commands``
        :param dut: dictionary with device information
        :param device_spawn: device connection (spawn)
        :param commands: Debug commands to send to device
        :return: if sucessful return output from cli else return empty string
        """
        cli_output = ""
        ip = dut['ip']
        port = dut['port']
        cli_type = dut['cli_type']

        if cli_type != "AH-AP":
            kwargs['fail_msg'] = "Run Diagnostic Debug Commands Keyword is not supported on " + cli_type
            self.common_validation.failed(**kwargs)
            return ""

        if not device_spawn or not dut:
            kwargs['fail_msg'] = "Run Diagnostic Debug Commands Keyword requirements not meet"
            self.common_validation.failed(**kwargs)
            return ""

        self.utils.print_info("Debug command(s) will be sent to device " + str(ip) + " port " + str(port))

        cli_output = self.cli.send_commands(device_spawn, commands)

        if not cli_output:
            kwargs['fail_msg'] = "Data not returned from Cli"
            self.common_validation.failed(**kwargs)
        else:
            kwargs['pass_msg'] = "Commands successfully sent to device"
            self.common_validation.passed(**kwargs)
        return cli_output

    def enable_debug_commands(self, dut, device_spawn, commands=None, **kwargs):
        """
        - Enables debug commands on a device
        - Keyword Usage
         - ``Enable Debug Commands``
        :param dut: dictionary with device information
        :param device_spawn: device connection (spawn)
        :param commands: Debug commands to send to device
        :return: if sucessful return output from cli else return empty string
        """

        if not commands:
            commands = self.default_enable_command_string
        return self.run_diagnostic_debug_commands(dut, device_spawn, commands, **kwargs)

    def disable_debug_commands(self, dut, device_spawn, commands=None, **kwargs):
        """
        - Disables debug commands on a device
        - Keyword Usage
         - ``Disable Debug Commands``
        :param dut: dictionary with device information
        :param device_spawn: device connection (spawn)
        :param commands: Debug commands to send to device
        :return: if sucessful return output from cli else return empty string
        """

        if not commands:
            commands = self.default_disable_command_string
        return self.run_diagnostic_debug_commands(dut, device_spawn, commands, **kwargs)

    def log_debug_commands(self, dut, device_spawn, commands=None, **kwargs):
        """
        - Log debug commands
        - Keyword Usage
         - ``Log Debug Commands``
        :param dut: dictionary with device information
        :param device_spawn: device connection (spawn)
        :param commands: Debug commands to send to device
        :return: if sucessful return output from cli else return empty string
        """

        if not commands:
            commands = self.default_log_command_string
        return self.run_diagnostic_debug_commands(dut, device_spawn, commands, **kwargs)
