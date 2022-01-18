from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.acl.base.AclBaseCustomShowTools import \
    AclBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


def create_instance(device):
    return AclCustomShowTools(device)


class AclCustomShowTools(AclBaseCustomShowTools):
    def __init__(self, device):
        super(AclCustomShowTools, self).__init__(device)

    def check_ace_exists(self, output, args, **kwargs):
        result_acl_id = self.pw.get_value_by_offset(output, args["ace_name"], 0)
        result_ace_index = self.pw.get_value_by_offset(output, args["ace_name"], 1)

        result = True if result_acl_id == args["acl_id"] and result_ace_index == args["ace_index"] else False
        return result, {"ret_acl_id": result_acl_id,
                        "ret_ace_index": result_ace_index}

    def check_acl_enable(self, output, args, **kwargs):
        result_acl_state = self.pw.get_value_by_offset(output, args["acl_name"], 4)

        result = True if result_acl_state == 'enabled' else False
        return result, {"ret_acl_state": result_acl_state}

    def check_acl_name(self, output, args, **kwargs):
        result_acl_id = self.pw.get_value_by_offset(output, args["acl_name"], 0)

        result = True if result_acl_id == args["acl_id"] else False
        return result, {"ret_acl_id": result_acl_id}

    def check_acl_action(self, output, args, **kwargs):
        result_acl_action = self.pw.get_value_by_offset(output, args["acl_name"], 6)

        result = True if result_acl_action == args["action"] else False
        return result, {"ret_acl_action": result_acl_action}

    def check_acl_port(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_acl_vlan(self, output, args, **kwargs):
        result_acl_vlan = self.pw.get_value_by_offset(output, args["acl_name"], 8)
        result_acl_vlan = StringUtils.expand_voss_vlan_string(result_acl_vlan)

        result = True if args["vlan"] in result_acl_vlan else False
        return result, {"ret_vlans": str(result_acl_vlan)}

    def check_ace_index_oper_state(self, output, args, **kwargs):
        result_ace_oper_state = self.pw.get_value_by_offset(output, args["ace_name"], 4)

        result = True if result_ace_oper_state.lower() == "up" else False
        return result, {"ret_ace_oper_state": result_ace_oper_state}

    def check_ace_index_name(self, output, args, **kwargs):
        result_ace_id = self.pw.get_value_by_offset(output, args["ace_name"], 1)

        result = True if result_ace_id == args["ace_index"] else False
        return result, {"ret_ace_id": result_ace_id}

    def check_ace_index_action(self, output, args, **kwargs):
        result_ace_action = self.pw.get_value_by_offset(output, args["ace_name"], 5)

        result = True if result_ace_action == args["ace_action"].lower() else False
        return result, {"ret_ace_action": result_ace_action}

    def check_ace_index_ethernet_ethertype(self, output, args, **kwargs):
        result_ace_ethertype = self.pw.get_value_by_offset(output, args["ace_ethertype"], 1)

        result = True if result_ace_ethertype == args["ace_index"] else False
        return result, {"ret_ace_ethertype": result_ace_ethertype}

    def check_ipv4_acl_exists(self, output, args, **kwargs):
        result_acl_id = self.pw.get_value_by_offset(output, args["acl_name"], 0)

        result = True if result_acl_id == args["acl_id"] else False
        return result, {"ret_acl_id": result_acl_id}

    def check_ipv6_acl_exists(self, output, args, **kwargs):
        result_acl_id = self.pw.get_value_by_offset(output, args["acl_name"], 0)

        result = True if result_acl_id == args["acl_id"] else False
        return result, {"ret_acl_id": result_acl_id}
