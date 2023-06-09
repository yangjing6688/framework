from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.hostinformation.base.\
    HostinformationBaseCustomShowTools import HostinformationBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return HostinformationCustomShowTools(device)


class HostinformationCustomShowTools(HostinformationBaseCustomShowTools):
    def __init__(self, device):
        super(HostinformationCustomShowTools, self).__init__(device)

    def check_host_contact(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "contact", 2)

        result = True if args["contact"] == parse_result else False
        return result, {"ret_host_contact": parse_result}

    def check_host_name(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "name", 2)

        result = True if args["name"] == parse_result else False
        return result, {"ret_host_name": parse_result}

    def check_host_location(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "location", 2)

        result = True if args["location"] == parse_result else False
        return result, {"ret_host_location": parse_result}

    def check_prompt(self, output, args, **kwargs):
        output = output.replace("\n", "\r\n")
        prompt_name = self.pw.get_value_by_offset(output, "SysName", 2)

        result = True if prompt_name == args["prompt_name"] else False
        return result, {"ret_prompt_name": prompt_name}

    def check_app_iqagent(self, output, args, **kwargs):
        output = output.replace("\n", "\r\n")
        parse_result = self.pw.get_value_by_offset(output, "Agent Version", 3)

        result = True if args["iqagent_version"] == parse_result else False
        return result, {"ret_iqagent_version": parse_result}

    def check_version(self, output, args, **kwargs):
        output = output.replace("\n", "\r\n")
        prompt_name = self.pw.get_value_by_offset(output, "Version : Build", 3)

        result = True if prompt_name in args["nos_version"] else False
        return result, {"ret_prompt_name": prompt_name}

    def check_state_iqagent(self, output, args, **kwargs):
        output = output.replace("\n", "\r\n")
        admin_state = self.pw.get_value_by_offset(output, "Agent Admin State", 4)
        agent_op_state = self.pw.get_value_by_offset(output, "Agent Oper State", 4)

        result = True if args["admin_state"] == admin_state and agent_op_state == args["agent_op_state"] else False
        return result, {"ret_iqagent_state": agent_op_state}
