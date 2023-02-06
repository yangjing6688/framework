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
        parse_result = self.pw.get_value_by_offset(output, "Agent Version", 5)

        result = True if args["iqagent_version"] == parse_result else False
        return result, {"ret_iqagent_version": parse_result}
