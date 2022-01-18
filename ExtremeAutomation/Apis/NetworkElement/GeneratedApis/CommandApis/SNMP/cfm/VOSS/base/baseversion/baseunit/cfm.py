"""
All cfm supported SNMP commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.SNMP.cfm.base.cfmbase import CfmBase


class Cfm(DeviceApi, CfmBase):
    def __init__(self, device):
        super(Cfm, self).__init__(device)
        self.device = device

    def enable_spbm(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.69.10.8.0"
        data_type = "i"
        value = "1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def disable_spbm(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.69.10.8.0"
        data_type = "i"
        value = "2"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def enable_maintenance_endpoint(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.69.3.1.6.{0}".format(arg_dict['mep_id'])
        data_type = "i"
        value = "1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def disable_maintenance_endpoint(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.69.3.1.6.{0}".format(arg_dict['mep_id'])
        data_type = "i"
        value = "2"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_spbm_mepid(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.69.10.10.0"
        data_type = "i"
        value = "{0}".format(arg_dict['mep_id'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_spbm_level(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.69.10.9.0"
        data_type = "i"
        value = "{0}".format(arg_dict['spbm_level'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_maintenance_domain(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.69.1.1.2.{0}||" \
              "1.3.6.1.4.1.2272.1.69.1.1.3.{0}||" \
              "1.3.6.1.4.1.2272.1.69.1.1.6.{0}".format(arg_dict['md_index'])
        data_type = "s||i||i"
        value = "{0}||4||{1}".format(arg_dict['md_name'],
                                     arg_dict['md_level'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_maintenance_domain_name(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.69.1.1.2.{0}||" \
              "1.3.6.1.4.1.2272.1.69.1.1.3.{0}".format(arg_dict['md_index'])
        data_type = "s||i"
        value = "{0}||4".format(arg_dict['md_name'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_maintenance_domain_index(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.69.1.1.2.{0}||" \
              "1.3.6.1.4.1.2272.1.69.1.1.3.{0}".format(arg_dict['md_index'])
        data_type = "s||i"
        value = "{0}||4".format(arg_dict['md_name'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_maintenance_domain_level(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.69.1.1.2.{0}||" \
              "1.3.6.1.4.1.2272.1.69.1.1.3.{0}||" \
              "1.3.6.1.4.1.2272.1.69.1.1.6.{0}".format(arg_dict['md_index'])
        data_type = "s||i||i"
        value = "{0}||4||{1}".format(arg_dict['md_name'],
                                     arg_dict['md_level'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_maintenance_association(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.69.2.1.4.{0}||" \
              "1.3.6.1.4.1.2272.1.69.2.1.5.{0}||" \
              "1.3.6.1.4.1.2272.1.69.2.1.6.{0}".format(arg_dict['md_index'])
        data_type = "s||i||i"
        value = "{0}||2||4".format(arg_dict['ma_name'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_maintenance_endpoint(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.69.3.1.7.0"
        data_type = "i"
        value = "4"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_spbm_mepid(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.69.10.10.0"
        data_type = "i"
        value = "1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_spbm_level(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.69.10.9.0"
        data_type = "i"
        value = "4"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_maintenance_domain(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.69.1.1.3.{0}".format(arg_dict['md_index'])
        data_type = "i"
        value = "6"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_maintenance_association(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.69.2.1.6.0"
        data_type = "i"
        value = "6"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_maintenance_endpoint(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.69.3.1.7.0"
        data_type = "i"
        value = "6"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def show_cmac(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.2272.1.69.10.15.0"

        return self.create_cmd_obj(command_type, oid)

    def show_spbm(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.4.1.2272.1.69.10"

        return self.create_cmd_obj(command_type, oid)

    def show_maintenance_endpoint(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.4.1.2272.1.69.3"

        return self.create_cmd_obj(command_type, oid)

    def show_maintenance_association(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.4.1.2272.1.69.2"

        return self.create_cmd_obj(command_type, oid)

    def show_maintenance_domain(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.4.1.2272.1.69.1"

        return self.create_cmd_obj(command_type, oid)

    def show_association_name(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.4.1.2272.1.69.2.1.4"

        return self.create_cmd_obj(command_type, oid)

    def show_domain_name(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.4.1.2272.1.69.1.1.2"

        return self.create_cmd_obj(command_type, oid)
