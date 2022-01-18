"""
All fabricattach supported SNMP commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.SNMP.fabricattach.base.fabricattachbase import \
    FabricattachBase


class Fabricattach(DeviceApi, FabricattachBase):
    def __init__(self, device):
        super(Fabricattach, self).__init__(device)
        self.device = device

    def enable_global(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.45.5.46.1.1.0"
        data_type = "i"
        value = "1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def disable_global(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.45.5.46.1.1.0"
        data_type = "i"
        value = "2"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def enable_port(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.45.5.46.1.6.1.2.{0}||" \
              "1.3.6.1.4.1.45.5.46.1.6.1.3.{0}".format(arg_dict['port'])
        data_type = "i||i"
        value = "1||4"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def disable_port(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.45.5.46.1.6.1.2.{0}||" \
              "1.3.6.1.4.1.45.5.46.1.6.1.3.{0}".format(arg_dict['port'])
        data_type = "i||i"
        value = "2||4"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def delete_port(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.45.5.46.1.6.1.3.{0}".format(arg_dict['port'])
        data_type = "i"
        value = "6"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def enable_mlt(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.45.5.46.1.6.1.2.{0}||" \
              "1.3.6.1.4.1.45.5.46.1.6.1.3.{0}".format(arg_dict['mlt_id'])
        data_type = "i||i"
        value = "1||4"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def disable_mlt(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.45.5.46.1.6.1.2.{0}||" \
              "1.3.6.1.4.1.45.5.46.1.6.1.3.{0}".format(arg_dict['mlt_id'])
        data_type = "i||i"
        value = "2||4"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def delete_mlt(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.45.5.46.1.6.1.3.{0}".format(arg_dict['mlt_id'])
        data_type = "i"
        value = "6"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def enable_port_auth(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.45.5.46.1.6.1.4.{0}".format(arg_dict['port'])
        data_type = "i"
        value = "1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def disable_port_auth(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.45.5.46.1.6.1.4.{0}".format(arg_dict['port'])
        data_type = "i"
        value = "2"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def enable_mlt_auth(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.45.5.46.1.6.1.4.{0}".format(arg_dict['mlt_id'])
        data_type = "i"
        value = "1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def disable_mlt_auth(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.45.5.46.1.6.1.4.{0}".format(arg_dict['mlt_id'])
        data_type = "i"
        value = "2"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_assignment_timeout(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.45.5.46.1.22.0"
        data_type = "i"
        value = "{0}".format(arg_dict['timeout'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_discovery_timeout(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.45.5.46.1.26.0"
        data_type = "i"
        value = "{0}".format(arg_dict['timeout'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_port_auth_key(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.45.5.46.1.6.1.5.{0}".format(arg_dict['port'])
        data_type = "s"
        value = "{0}".format(arg_dict['auth_key'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_mlt_auth_key(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.45.5.46.1.6.1.5.{0}".format(arg_dict['mlt_id'])
        data_type = "s"
        value = "{0}".format(arg_dict['auth_key'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_port_mgmt_isid(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.45.5.46.1.6.1.6.{0}".format(arg_dict['port'])
        data_type = "i"
        value = "{0}".format(arg_dict['i_sid'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_mlt_mgmt_isid(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.45.5.46.1.6.1.6.{0}".format(arg_dict['mlt_id'])
        data_type = "i"
        value = "{0}".format(arg_dict['i_sid'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_port_mgmt_isid_and_cvid(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.45.5.46.1.6.1.6.{0}||" \
              "1.3.6.1.4.1.45.5.46.1.6.1.7.{0}".format(arg_dict['port'])
        data_type = "i||i"
        value = "{0}||{1}".format(arg_dict['i_sid'],
                                  arg_dict['c_vid'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_mlt_mgmt_isid_and_cvid(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.45.5.46.1.6.1.6.{0}||" \
              "1.3.6.1.4.1.45.5.46.1.6.1.7.{0}".format(arg_dict['mlt_id'])
        data_type = "i||i"
        value = "{0}||{1}".format(arg_dict['i_sid'],
                                  arg_dict['c_vid'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_port_mgmt_isid(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.45.5.46.1.6.1.6.{0}".format(arg_dict['port'])
        data_type = "i"
        value = "0"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_mlt_mgmt_isid(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.45.5.46.1.6.1.6.{0}".format(arg_dict['mlt_id'])
        data_type = "i"
        value = "0"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_zero_touch_client_isid(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.45.5.46.1.29.1.4.{0}||" \
              "1.3.6.1.4.1.45.5.46.1.29.1.5.{0}".format(arg_dict['name'])
        data_type = "i||i"
        value = "{0}||4".format(arg_dict['i_sid'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_zero_touch_client(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.45.5.46.1.29.1.5.{0}".format(arg_dict['name'])
        data_type = "i"
        value = "6"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def show_service_state(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.45.5.46.1.1.0"

        return self.create_cmd_obj(command_type, oid)

    def show_element_type(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.45.5.46.1.2.0"

        return self.create_cmd_obj(command_type, oid)

    def show_provision_mode(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.45.5.46.1.13.0"

        return self.create_cmd_obj(command_type, oid)

    def show_global_timeouts(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.45.5.46.1.22.0||" \
              "1.3.6.1.4.1.45.5.46.1.26.0"

        return self.create_cmd_obj(command_type, oid)

    def show_port(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.45.5.46.1.6.1.2.{0}||" \
              "1.3.6.1.4.1.45.5.46.1.6.1.4.{0}||" \
              "1.3.6.1.4.1.45.5.46.1.6.1.5.{0}||" \
              "1.3.6.1.4.1.45.5.46.1.6.1.6.{0}||" \
              "1.3.6.1.4.1.45.5.46.1.6.1.7.{0}".format(arg_dict['port'])

        return self.create_cmd_obj(command_type, oid)

    def show_mlt(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.45.5.46.1.6.1.2.{0}||" \
              "1.3.6.1.4.1.45.5.46.1.6.1.4.{0}||" \
              "1.3.6.1.4.1.45.5.46.1.6.1.5.{0}||" \
              "1.3.6.1.4.1.45.5.46.1.6.1.6.{0}||" \
              "1.3.6.1.4.1.45.5.46.1.6.1.7.{0}".format(arg_dict['mlt_id'])

        return self.create_cmd_obj(command_type, oid)

    def show_elements_port(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.45.5.46.1.11.1.2.{0}||" \
              "1.3.6.1.4.1.45.5.46.1.11.1.3.{0}||" \
              "1.3.6.1.4.1.45.5.46.1.11.1.4.{0}||" \
              "1.3.6.1.4.1.45.5.46.1.11.1.5.{0}||" \
              "1.3.6.1.4.1.45.5.46.1.11.1.6.{0}||" \
              "1.3.6.1.4.1.45.5.46.1.11.1.8.{0}||" \
              "1.3.6.1.4.1.45.5.46.1.11.1.9.{0}||" \
              "1.3.6.1.4.1.45.5.46.1.11.1.10.{0}".format(arg_dict['port'])

        return self.create_cmd_obj(command_type, oid)

    def show_assignment_port(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.4.1.45.5.46.1.5.1.4.{0}||" \
              "1.3.6.1.4.1.45.5.46.1.5.1.6.{0}".format(arg_dict['port'])

        return self.create_cmd_obj(command_type, oid)

    def show_stats_global(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.4.1.45.5.46.1.24"

        return self.create_cmd_obj(command_type, oid)

    def show_stats_port(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.45.5.46.1.23.1.2.{0}||" \
              "1.3.6.1.4.1.45.5.46.1.23.1.3.{0}||" \
              "1.3.6.1.4.1.45.5.46.1.23.1.4.{0}||" \
              "1.3.6.1.4.1.45.5.46.1.23.1.5.{0}||" \
              "1.3.6.1.4.1.45.5.46.1.23.1.6.{0}||" \
              "1.3.6.1.4.1.45.5.46.1.23.1.7.{0}||" \
              "1.3.6.1.4.1.45.5.46.1.23.1.8.{0}||" \
              "1.3.6.1.4.1.45.5.46.1.23.1.9.{0}||" \
              "1.3.6.1.4.1.45.5.46.1.23.1.10.{0}||" \
              "1.3.6.1.4.1.45.5.46.1.23.1.11.{0}".format(arg_dict['port'])

        return self.create_cmd_obj(command_type, oid)

    def show_zero_touch_client(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.4.1.45.5.46.1.29"

        return self.create_cmd_obj(command_type, oid)

    def show_isid(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.2272.1.87.5.1.3.{0}||" \
              "1.3.6.1.4.1.2272.1.87.5.1.4.{0}||" \
              "1.3.6.1.4.1.2272.1.87.5.1.5.{0}||" \
              "1.3.6.1.4.1.2272.1.87.5.1.6.{0}||" \
              "1.3.6.1.4.1.2272.1.87.5.1.7.{0}".format(arg_dict['port'])

        return self.create_cmd_obj(command_type, oid)
