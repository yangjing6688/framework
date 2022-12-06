from extauto.common.Cli import Cli
from extauto.common.Utils import Utils
from extauto.common.CommonValidation import CommonValidation


class Debugging(object):

    def __init__(self):
        self.cli = Cli()
        self.utils = Utils()
        self.common_validation = CommonValidation()

    def run_cli_commands(self, dut, device_spawn, commands, **kwargs):
        """
        - Run cli commands on a device
        - Keyword Usage
         - ``Run Cli Commands``
        :param dut: dictionary with device information
        :param device_spawn: device connection (spawn)
        :param commands: Cli commands to be send to device
        :return: if successful return 1 else return -1
        """

        if not device_spawn:
            kwargs['fail_msg'] = "Device connection (spawn) required for Run Cli Commands keyword"
            self.common_validation.failed(**kwargs)
            return -1

        if not dut:
            kwargs['fail_msg'] = "DUT required for Run Cli Commands keyword"
            self.common_validation.failed(**kwargs)
            return -1

        if not commands or len(commands) == 0:
            kwargs['fail_msg'] = "Commands list required for Run Cli Commands keyword"
            self.common_validation.failed(**kwargs)
            return -1

        ip = dut['ip']
        port = dut['port']

        self.utils.print_info("Debug command(s) will be sent to device " + str(ip) + " port " + str(port))

        for command in commands:
            cli_output = self.cli.send_commands(device_spawn, command)

        kwargs['pass_msg'] = "Commands successfully sent to device"
        self.common_validation.passed(**kwargs)
        return 1
