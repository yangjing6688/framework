"""
All poe supported SNMP commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.SNMP.poe.base.poebase import PoeBase


class Poe(DeviceApi, PoeBase):
    def __init__(self, device):
        super(Poe, self).__init__(device)
        self.device = device

    def enable_port(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.2.1.105.1.1.1.3.{0}".format(arg_dict['port'])
        data_type = "i"
        value = "1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def disable_port(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.2.1.105.1.1.1.3.{0}".format(arg_dict['port'])
        data_type = "i"
        value = "2"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_power_usage_threshold(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.2.1.105.1.3.1.1.5.{0}".format(arg_dict['slot'])
        data_type = "i"
        value = "{0}".format(arg_dict['threshold'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_port_power_limit(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.45.5.8.1.1.1.3.{0}".format(arg_dict['port'])
        data_type = "i"
        value = "{0}".format(arg_dict['power_limit'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_port_power_priority(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.2.1.105.1.1.1.7.{0}".format(arg_dict['port'])
        data_type = "i"
        value = "{0}".format(arg_dict['power_priority'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_port_detect_type(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.45.1.6.15.1.1.1.6.{0}".format(arg_dict['port'])
        data_type = "i"
        value = "{0}".format(arg_dict['detect_type'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def show_power_usage_threshold(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.2.1.105.1.3.1.1.5.{0}".format(arg_dict['slot'])

        return self.create_cmd_obj(command_type, oid)

    def show_port_status(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.2.1.105.1.1.1.3.{0}".format(arg_dict['port'])

        return self.create_cmd_obj(command_type, oid)

    def show_port_measurements(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.4.1.45.5.8.1.1"

        return self.create_cmd_obj(command_type, oid)

    def show_port_power_limit(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.45.5.8.1.1.1.3.{0}".format(arg_dict['port'])

        return self.create_cmd_obj(command_type, oid)

    def show_port_power_priority(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.2.1.105.1.1.1.7.{0}".format(arg_dict['port'])

        return self.create_cmd_obj(command_type, oid)

    def show_port_detection_status(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.2.1.105.1.1.1.6.{0}".format(arg_dict['port'])

        return self.create_cmd_obj(command_type, oid)

    def show_port_power_classification(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.2.1.105.1.1.1.10.{0}".format(arg_dict['port'])

        return self.create_cmd_obj(command_type, oid)

    def show_global_status(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.2.1.105.1.3.1.1.2.{0}||" \
              "1.3.6.1.2.1.105.1.3.1.1.3.{0}||" \
              "1.3.6.1.2.1.105.1.3.1.1.4.{0}||" \
              "1.3.6.1.2.1.105.1.3.1.1.5.{0}".format(arg_dict['slot'])

        return self.create_cmd_obj(command_type, oid)

    def show_port_power_pairs(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.2.1.105.1.1.1.5.{0}".format(arg_dict['port'])

        return self.create_cmd_obj(command_type, oid)

    def show_port_detect_type(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.45.1.6.15.1.1.1.6.{0}".format(arg_dict['port'])

        return self.create_cmd_obj(command_type, oid)
