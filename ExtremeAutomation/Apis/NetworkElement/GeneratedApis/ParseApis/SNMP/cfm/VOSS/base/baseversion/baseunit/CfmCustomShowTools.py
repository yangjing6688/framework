from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.SNMP.cfm.base.CfmBaseCustomShowTools import \
    CfmBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


def create_instance(device):
    return CfmCustomShowTools(device)


class CfmCustomShowTools(CfmBaseCustomShowTools):
    def __init__(self, device):
        super(CfmCustomShowTools, self).__init__(device)

    def check_cfm_cmac_level(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.69.10.12." + args["oid_index"]
        level = self.pw.get_value_by_offset(output, item, 2)

        result = True if level == args["cmac_level"] else False
        return result, {"ret_level": level}

    def check_cfm_cmac_state(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.69.10.11." + args["oid_index"]
        state = self.pw.get_value_by_offset(output, item, 2)
        cmac_state = args["cmac_state"].lower()
        res = {"1": "enable",
               "2": "disable"}

        result = True if res[state] == cmac_state else False
        return result, {"ret_state": res[state]}

    def check_cfm_cmac_mepid(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.69.10.10." + args["oid_index"]
        mepid = self.pw.get_value_by_offset(output, item, 2)

        result = True if mepid == args["cmac_mepid"] else False
        return result, {"ret_mepid": mepid}

    def check_cfm_cmac_mac(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.69.10.15." + args["oid_index"]
        cmac_mac = self.pw.get_value_by_offset(output, item, 2)
        cmac_mac = StringUtils().normalize_mac(cmac_mac)

        result = True if cmac_mac == args["cmac_mac"] else False
        return result, {"ret_mac": cmac_mac}

    def check_cfm_spbm_level(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.69.10.9." + args["oid_index"]
        level = self.pw.get_value_by_offset(output, item, 2)

        result = True if level == args["spbm_level"] else False
        return result, {"ret_level": level}

    def check_cfm_spbm_state(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.69.10.8." + args["oid_index"]
        state = self.pw.get_value_by_offset(output, item, 2)
        spbm_state = args["spbm_state"].lower()
        res = {"1": "enable",
               "2": "disable"}

        result = True if res[state] == spbm_state else False
        return result, {"ret_state": res[state]}

    def check_cfm_spbm_state_enable(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.69.10.8." + args["oid_index"]
        state = self.pw.get_value_by_offset(output, item, 2)

        result = True if state == "1" else False
        return result, {"ret_state": state}

    def check_cfm_spbm_mepid(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.69.10.10." + args["oid_index"]
        mepid = self.pw.get_value_by_offset(output, item, 2)

        result = True if mepid == args["mep_id"] else False
        return result, {"ret_mepid": mepid}

    def check_cfm_spbm_mac(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.69.10.14." + args["oid_index"]
        spbm_mac = self.pw.get_value_by_offset(output, item, 2)
        spbm_mac = StringUtils().normalize_mac(spbm_mac)

        result = True if spbm_mac == args["spbm_mac"] else False
        return result, {"ret_mac": spbm_mac}

    def check_cfm_maintenance_association_domain_name(self, *args):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_cfm_maintenance_association_name(self, *args):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_cfm_maintenance_association_domain_index(self, *args):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_cfm_maintenance_association_index(self, *args):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_cfm_maintenance_domain(self, output, args, **kwargs):
        item_name = "SNMPv2-SMI::enterprises.2272.1.69.1.1.2." + args["oid_index"]
        item_level = "SNMPv2-SMI::enterprises.2272.1.69.1.1.6." + args["oid_index"]
        result_name = self.pw.get_value_by_offset(output, item_name, 2)
        result_level = self.pw.get_value_by_offset(output, item_level, 2)

        result = True if result_name == args["md_name"] and result_level == args["md_level"] else False
        return result, {"ret_name": result_name,
                        "ret_level": result_level}

    def check_cfm_maintenance_domain_name(self, output, args, **kwargs):
        result = self.pw.is_exact_string_present_in_output(output, args["md_name"])
        return result, result

    def check_cfm_maintenance_domain_index(self, output, args, **kwargs):
        item_name = "SNMPv2-SMI::enterprises.2272.1.69.1.1.2." + args["md_index"]
        result_name = self.pw.get_value_by_offset(output, item_name, 2)

        result = True if result_name == args["md_name"] else False
        return result, {"ret_md_name": result_name}

    def check_cfm_maintenance_domain_level(self, output, args, **kwargs):
        out1 = output.replace("SNMPv2-SMI::enterprises.2272.1.69.1.1.2.", "")
        name_index = self.pw.get_value_by_offset(out1, args["md_name"], 0)

        item_level = "SNMPv2-SMI::enterprises.2272.1.69.1.1.6." + name_index
        result_level = self.pw.get_value_by_offset(output, item_level, 2)

        result = True if result_level == args["md_level"] else False
        return result, {"ret_level": result_level}

    def check_cfm_maintenance_domain_type(self, output, args, **kwargs):
        out1 = output.replace("SNMPv2-SMI::enterprises.2272.1.69.1.1.2.", "")
        name_index = self.pw.get_value_by_offset(out1, args["md_name"], 0)

        item_type = "SNMPv2-SMI::enterprises.2272.1.69.10.8." + name_index
        domain_type = self.pw.get_value_by_offset(output, item_type, 2)
        main_type = args["md_type"].lower()
        res = {"0": "none",
               "1": "trunk",
               "2": "sg",
               "3": "endpt",
               "4": "vlan",
               "5": "port",
               "6": "mimencapvlan",
               "7": "nodal"}

        result = True if res[domain_type] == main_type else False
        return result, {"ret_md_type": res[domain_type]}

    def check_cfm_maintenance_endpoint_domain_name(self, *args):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_cfm_maintenance_endpoint_association_name(self, *args):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_cfm_maintenance_endpoint_mepid(self, *args):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_cfm_maintenance_endpoint_state(self, *args):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None
