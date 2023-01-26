"""
Keyword class for all resetdevice cli commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.ResetdeviceConstants import \
    ResetdeviceConstants as CommandConstants
# All imports above this line will be removed after generation.
# User imports must be added below.


class NetworkElementResetdeviceGenKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementResetdeviceGenKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.api_const = "resetdevice"

    def resetdevice_reset_now(self, device_name, reboot_answer='', reboot_exos='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: EOS, EXOS, VOSS, EOSSTACKS, ALPHA, BOSS, SLX
        """
        args = {
            "reboot_answer": reboot_answer,
            "reboot_exos": reboot_exos
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.RESET_NOW,
                                    **kwargs)

    def resetdevice_reset_system_to_config(self, device_name, config='', reboot_answer='', reboot_exos='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: EOS, EXOS, VOSS, EOSSTACKS
        """
        args = {
            "config": config,
            "reboot_answer": reboot_answer,
            "reboot_exos": reboot_exos
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.RESET_SYSTEM_TO_CONFIG,
                                    **kwargs)

    def resetdevice_reset_factory_default(self, device_name, reboot_answer='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: EXOS, ALPHA
        """
        args = {
            "reboot_answer": reboot_answer
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.RESET_FACTORY_DEFAULT,
                                    **kwargs)

    def resetdevice_bypass_initial_setup(self, device_name, **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.BYPASS_INITIAL_SETUP,
                                    **kwargs)

    def resetdevice_login_after_reset(self, device_name, password='', username='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "password": password,
            "username": username
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.LOGIN_AFTER_RESET,
                                    **kwargs)

    def resetdevice_run_failover(self, device_name, failover_answer='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "failover_answer": failover_answer
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.RUN_FAILOVER,
                                    **kwargs)

    def resetdevice_run_failover_warm(self, device_name, failover_answer='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "failover_answer": failover_answer
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.RUN_FAILOVER_WARM,
                                    **kwargs)

    def resetdevice_reset_system(self, device_name, reboot_answer='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {
            "reboot_answer": reboot_answer
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.RESET_SYSTEM,
                                    **kwargs)
