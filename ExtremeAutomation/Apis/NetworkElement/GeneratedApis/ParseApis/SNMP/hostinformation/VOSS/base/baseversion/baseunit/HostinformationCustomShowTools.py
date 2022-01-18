from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.SNMP.hostinformation.base.\
    HostinformationBaseCustomShowTools import HostinformationBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Keywords.NetworkElementKeywords.Utils.NetworkElementSnmpUtils import NetworkElementSnmpUtils


def create_instance(device):
    return HostinformationCustomShowTools(device)


class HostinformationCustomShowTools(HostinformationBaseCustomShowTools):
    def __init__(self, device):
        super(HostinformationCustomShowTools, self).__init__(device)

    def check_host_location(self, output, args, **kwargs):
        """
        The following function returns True if the location value is correct.
        """
        location_value = self.pw.get_value_by_offset(output, args["location"], 2)

        return location_value == args["location"], {"ret_location": location_value}

    def check_host_contact(self, output, args, **kwargs):
        """
        The following function returns True if the contact value is correct.
        """
        contact_value = self.pw.get_value_by_offset(output, args["contact"], 2)

        return contact_value == args["contact"], {"ret_contact": contact_value}

    def check_host_name(self, output, args, **kwargs):
        """
        The following function returns True if the name value is correct.
        """
        name_value = self.pw.get_value_by_offset(output, args["name"], 2)

        return name_value == args["name"], {"ret_name": name_value}

    def check_host_system_id(self, output, args, **kwargs):
        """
        The following function returns True if the name value is correct.
        """
        parse_result = self.pw.get_value_by_offset(output, "=", 2)
        parse_result = NetworkElementSnmpUtils.systems[parse_result] if \
            parse_result in NetworkElementSnmpUtils.systems else parse_result

        return parse_result == args["system_id"], {"ret_system_id": parse_result}

    def check_prompt(self, output, args, **kwargs):
        """
        The following function returns True if the name value is correct.
        """
        name_value = self.pw.get_value_by_offset(output, args["prompt_name"], 2)

        return name_value == args["prompt_name"], {"ret_prompt": name_value}
