from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.cfm.base.CfmBaseCustomShowTools import \
    CfmBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return CfmCustomShowTools(device)


class CfmCustomShowTools(CfmBaseCustomShowTools):
    def __init__(self, device):
        super(CfmCustomShowTools, self).__init__(device)

    def check_cfm_cmac_level(self, output, args, **kwargs):
        cmac_level = self.pw.get_value_at_location(output, column=0, name=None, row=9)

        result = True if cmac_level == args["cmac_level"] else False
        return result, {"ret_cmac_level": cmac_level}

    def check_cfm_cmac_state(self, output, args, **kwargs):
        cmac_state = self.pw.get_value_at_location(output, column=1, name=None, row=9)

        result = True if cmac_state == args["cmac_state"] else False
        return result, {"ret_cmac_state": cmac_state}

    def check_cfm_cmac_mepid(self, output, args, **kwargs):
        cmac_mepid = self.pw.get_value_at_location(output, column=2, name=None, row=9)

        result = True if cmac_mepid == args["cmac_mepid"] else False
        return result, {"ret_cmac_mepid": cmac_mepid}

    def check_cfm_cmac_mac(self, output, args, **kwargs):
        cmac_mac = self.pw.get_value_at_location(output, column=3, name=None, row=9)

        result = True if cmac_mac == args["cmac_mac"] else False
        return result, {"ret_cmac_mac": cmac_mac}

    def check_cfm_spbm_level(self, output, args, **kwargs):
        spbm_level = self.pw.get_value_at_location(output, column=0, name=None, row=9)

        result = True if spbm_level == args["spbm_level"] else False
        return result, {"ret_spbm_level": spbm_level}

    def check_cfm_spbm_state(self, output, args, **kwargs):
        spbm_state = self.pw.get_value_at_location(output.lower(), column=1, name=None, row=9)

        result = True if spbm_state == args["spbm_state"] else False
        return result, {"ret_spbm_state": spbm_state}

    def check_cfm_spbm_mepid(self, output, args, **kwargs):
        mep_id = self.pw.get_value_at_location(output, column=2, name=None, row=9)

        result = True if mep_id == args["mep_id"] else False
        return result, {"ret_mep_id": mep_id}

    def check_cfm_spbm_mac(self, output, args, **kwargs):
        spbm_mac = self.pw.get_value_at_location(output, column=3, name=None, row=9)

        result = True if spbm_mac == args["spbm_mac"] else False
        return result, {"ret_spbm_mac": spbm_mac}

    def check_cfm_maintenance_association_domain_name(self, output, args, **kwargs):
        domain_name = self.pw.get_value_at_location(output, column=0, name=None, row=9)

        result = True if domain_name == args["domain_name"] else False
        return result, {"ret_ma_domain_name": domain_name}

    def check_cfm_maintenance_association_name(self, output, args, **kwargs):
        association_name = self.pw.get_value_at_location(output, column=1, name=None, row=9)

        result = True if association_name == args["association_name"] else False
        return result, {"ret_ma_name": association_name}

    def check_cfm_maintenance_association_domain_index(self, output, args, **kwargs):
        domain_index = self.pw.get_value_at_location(output, column=2, name=None, row=9)

        result = True if domain_index == args["domain_index"] else False
        return result, {"ret_ma_domain_index": domain_index}

    def check_cfm_maintenance_association_index(self, output, args, **kwargs):
        association_index = self.pw.get_value_at_location(output, column=3, name=None, row=9)

        result = True if association_index == args["association_index"] else False
        return result, {"ret_ma_index": association_index}

    def check_cfm_maintenance_domain_name(self, output, args, **kwargs):
        md_name_found = self.pw.get_value_at_location(output, column=0, name=args["md_name"])

        result = True if md_name_found == args["md_name"] else False
        return result, {"ret_md_name": md_name_found}

    def check_cfm_maintenance_domain_index(self, output, args, **kwargs):
        output = output.replace("\n", "\r\n")
        name = self.pw.get_value_at_location(output, column=0, name=args["md_name"])
        index = self.pw.get_value_by_offset(output, name, 1)

        result = True if name == args["md_name"] and index == args["md_index"] else False
        return result, {"ret_md_name": name,
                        "ret_md_index": index}

    def check_cfm_maintenance_domain_level(self, output, args, **kwargs):
        output = output.replace("\n", "\r\n")
        name = self.pw.get_value_at_location(output, column=0, name=args["md_name"])
        level = self.pw.get_value_by_offset(output, name, 2)

        result = True if name == args["md_name"] and level == args["md_level"] else False
        return result, {"ret_md_name": name,
                        "ret_md_level": level}

    def check_cfm_maintenance_domain_type(self, output, args, **kwargs):
        md_type = self.pw.get_value_at_location(output.lower(), column=3, name=None, row=9)

        result = True if md_type == args["md_type"] else False
        return result, {"ret_md_type": md_type}

    def check_cfm_maintenance_endpoint_domain_name(self, output, args, **kwargs):
        me_domain_name = self.pw.get_value_at_location(output, column=0, name=None, row=10)

        result = True if me_domain_name == args["me_domain_name"] else False
        return result, {"ret_me_domain_name": me_domain_name}

    def check_cfm_maintenance_endpoint_association_name(self, output, args, **kwargs):
        me_association_name = self.pw.get_value_at_location(output, column=1, name=None, row=10)

        result = True if me_association_name == args["me_association_name"] else False
        return result, {"ret_me_association_name": me_association_name}

    def check_cfm_maintenance_endpoint_mepid(self, output, args, **kwargs):
        me_mepid = self.pw.get_value_at_location(output, column=2, name=None, row=10)

        result = True if me_mepid == args["me_mepid"] else False
        return result, {"ret_me_mepid": me_mepid}

    def check_cfm_maintenance_endpoint_state(self, output, args, **kwargs):
        me_state = self.pw.get_value_at_location(output, column=3, name=None, row=10)

        result = True if me_state == args["me_state"] else False
        return result, {"ret_me_state": me_state}

    def check_cfm_spbm_state_enable(self, output, args, **kwargs):
        spbm_state = self.pw.get_value_at_location(output.lower(), column=1, name=None, row=9)

        result = True if spbm_state == "enable" else False
        return result, {"ret_spbm_state": spbm_state}

    def check_cfm_maintenance_domain(self, output, args, **kwargs):
        output = output.replace("\n", "\r\n")
        name = self.pw.get_value_at_location(output, column=0, name=args["md_name"])
        index = self.pw.get_value_by_offset(output, name, 1)
        level = self.pw.get_value_by_offset(output, name, 2)

        result = True if name == args["md_name"] and index == args["md_index"] and level == args["md_level"] else False
        return result, {"ret_md_name": name,
                        "ret_md_index": index,
                        "ret_md_level": level}
