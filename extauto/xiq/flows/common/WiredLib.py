from extauto.common.Utils import Utils
from extauto.xiq.flows.manage.Device360 import Device360
from extauto.common.CommonValidation import CommonValidation
from extauto.common.Cli import Cli

class WiredLib():
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.cli = Cli()
        self.device360 = Device360()
        self.common_validation = CommonValidation()

    def configure_port_duplex_cli(self, range_ports_start, range_ports_end, sw_spawn, operate,speed=100):
        '''
        Thei function configured into CLI on EXOS devices the duplex mode and speed

        :param range_ports_start: First port of range
        :param range_ports_end: End port of range
        :param sw_spawn: spawn
        :param operate: Operate mode
        :param speed: Speed of port
        :return:
        '''
        for cnt in range(int(range_ports_start), int(range_ports_end) + 1):
            self.cli.send(sw_spawn, "configure ports {} auto off speed {} duplex {}".format(cnt,speed,operate))
        return 1

    def configure_port_auto_cli(self, range_ports_start, range_ports_end, sw_spawn):
        '''
        Thei function configured into CLI on EXOS devices the auto transmission mode

        :param range_ports_start: First port of range
        :param range_ports_end: End port of range
        :param sw_spawn: spawn
        :return: 1
        '''
        for cnt in range(int(range_ports_start), int(range_ports_end) + 1):
            self.cli.send(sw_spawn, "configure ports {} auto on".format(cnt))
        return 1

    def check_transmission_mode_exos(self, range_ports_start, range_ports_end, sw_spawn, state, **kwargs):
        '''
        :param range_ports_start: First port of range
        :param range_ports_end: End port of range
        :param sw_spawn: spawn
        :param state: Port state . If state = "" , that port will be ignored
        :return: 1 if the status of transmission in XIQ and CLI are the same
                -1 if the status of transmission in XIQ and CLI are different
        '''
        for cnt in range(int(range_ports_start), int(range_ports_end) + 1):
            result = self.cli.send(sw_spawn, "sh ports {} configuration no-refresh".format(cnt))
            operate_state = self.utils.get_regexp_matches(result,
                        "\\d+\\s+[\\w-]+\\s\\w\\s+(\\w+)\\s+", 1)
            operate_duplex_config = self.utils.get_regexp_matches(result,
                        "\\d+\\s+[\\w-]+\\s+\\w\\s+\\w+\\s+\\w+\\s+\\w+\\s+(\\d+||\\s+)\\s+(\\w+)",2)
            operate_duplex_actual = self.utils.get_regexp_matches(result,
                        "\\d+\\s+[\\w-]+\\s+\\w\\s+\\w+\\s+\\w+\\s+\\w+\\s+(\\d+||\\s+)\\s+(\\w+)\\s(\\w+||\\s+)",3)
            cnt_str = str(cnt)
            operate_state_str = str(operate_state[0])
            operate_duplex_cfg_str = str(operate_duplex_config[0])
            operate_duplex_actual_str = str(operate_duplex_actual[0])
            self.utils.print_info("Operate state for port {} is:{}".format(cnt, operate_state_str))
            self.utils.print_info("Operate duplex Cfg for port {} is:{}".format(cnt, operate_duplex_cfg_str))
            self.utils.print_info("Operate duplex Actual for port {} is:{}".format(cnt, operate_duplex_actual_str))
            if operate_duplex_cfg_str == 'AUTO' and operate_duplex_actual_str.replace(" ", "") == '':
                self.utils.print_info(
                    " 'Operate duplex cfg' is AUTO and 'Operate duplex actual' is empty ."
                    " Check if N/A is displayed into XIQ for port transmission mode ")
                if self.device360.compare_transmission_mode(cnt_str, state,"N/A") == 1:
                    pass
                else:
                    kwargs['fail_msg'] = "The status of transmission in XIQ and" \
                                         " CLI are different"
                    self.common_validation.failed(**kwargs)
                    return -1
            elif operate_duplex_cfg_str == 'AUTO' and not operate_duplex_actual_str.replace(" ", "") == '':
                self.utils.print_info(
                    "'Operate duplex cfg' is AUTO . Check if {} is displayed into XIQ for port transmission mode "
                    .format(operate_duplex_actual_str))
                if self.device360.compare_transmission_mode(cnt_str, state, operate_duplex_actual_str) == 1:
                    pass
                else:
                    kwargs['fail_msg'] = "The status of transmission in " \
                                         "XIQ and CLI are different"
                    self.common_validation.failed(**kwargs)
                    return -1
            else:
                if self.device360.compare_transmission_mode(cnt_str, state, operate_duplex_cfg_str) == 1:
                    pass
                else:
                    kwargs['fail_msg'] = "The status of transmission in" \
                                         " XIQ and CLI are different"
                    self.common_validation.failed(**kwargs)
                    return -1
        return 1

    def check_vlan_cli(self, vlan, device_make, sw_spawn, **kwargs):
        """

        :param vlan:
        :param device_make:
        :param sw_spawn:
        :return:
        """
        if device_make.lower() == "exos":
            result = self.cli.send(sw_spawn, "show vlan description ")
            vlan_list = self.utils.get_regexp_matches(result, "\\w+\\s+(\\d+)\\s+", 1)
            self.utils.print_info("",vlan_list)
            if vlan in vlan_list:
                self.utils.print_info("Vlan {} found in CLI".format(vlan))
                kwargs['pass_msg'] = "Vlan found in CLI"
                self.common_validation.passed(**kwargs)
                return 1
            else:
                self.utils.print_info("Vlan {} not found in CLI".format(vlan))
                kwargs['fail_msg'] = f"Vlan {vlan} not found in CLI"
                self.common_validation.failed(**kwargs)
                return -1
        elif device_make.lower() == "voss":
            result = self.cli.send(sw_spawn, "show vlan name")
            vlan_list = self.utils.get_regexp_matches(result, "(\\d+)\\s+\\d+\\s+[\\w\\-]+", 1)
            if vlan in vlan_list:
                self.utils.print_info("Vlan {} found in CLI".format(vlan))
                kwargs['pass_msg'] = "Vlan found in CLI"
                self.common_validation.passed(**kwargs)
                return 1
            else:
                self.utils.print_info("Vlan {} not found in CLI".format(vlan))
                kwargs['fail_msg'] = f"Vlan {vlan} not found in CLI"
                self.common_validation.failed(**kwargs)
                return -1
        else:
            self.utils.print_info("No device make found")
            kwargs['fail_msg'] = "No device make found"
            self.common_validation.fault(**kwargs)
            return -1
