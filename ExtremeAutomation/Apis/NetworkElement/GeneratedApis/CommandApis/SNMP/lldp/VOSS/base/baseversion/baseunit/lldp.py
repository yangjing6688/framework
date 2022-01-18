"""
All lldp supported SNMP commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.SNMP.lldp.base.lldpbase import LldpBase


class Lldp(DeviceApi, LldpBase):
    def __init__(self, device):
        super(Lldp, self).__init__(device)
        self.device = device

    def set_tx_interval(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.0.8802.1.1.2.1.1.1.0"
        data_type = "i"
        value = "{0}".format(arg_dict['interval'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_tx_hold_multiplier(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.0.8802.1.1.2.1.1.2.0"
        data_type = "i"
        value = "{0}".format(arg_dict['multiplier'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def show_info(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.0.8802.1.1.2.1.1.1.0||" \
              "1.0.8802.1.1.2.1.1.2.0||" \
              "1.0.8802.1.1.2.1.1.3.0||" \
              "1.0.8802.1.1.2.1.1.4.0||" \
              "1.0.8802.1.1.2.1.1.5.0"

        return self.create_cmd_obj(command_type, oid)
