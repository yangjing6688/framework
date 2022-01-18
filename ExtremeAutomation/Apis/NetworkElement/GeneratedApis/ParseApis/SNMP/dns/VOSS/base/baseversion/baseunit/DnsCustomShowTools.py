from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.SNMP.dns.base.DnsBaseCustomShowTools import \
    DnsBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils
from ExtremeAutomation.Library.Utils.NumberUtils import NumberUtils


class DnsCustomShowTools(DnsBaseCustomShowTools):
    def __init__(self, device):
        super(DnsCustomShowTools, self).__init__(device)

    def check_dns_ip_domain_name(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.1.70." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if args["domain_name"] == parse_result else False
        return result, {"ret_domain_name": parse_result}

    def check_host_name(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.1.65.1.2." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if args["host_name"] == parse_result else False
        return result, {"ret_name": parse_result}

    def check_host_ip(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.1.65.1.6." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        expected_ip = StringUtils.ipaddr_to_pure_hex(args["host_ip"])

        result = True if parse_result == expected_ip else False
        return result, {"ret_ip": parse_result}

    def check_dns_server_ip(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.1.64.1.8." + args["index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        expected_ip = StringUtils.ipaddr_to_pure_hex(args["ip_addr"])

        result = True if parse_result == expected_ip else False
        return result, {"ret_ip": parse_result}

    def check_dns_server_status(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.1.64.1.3." + args["index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == "0" else False
        return result, {"ret_status": parse_result}

    def check_dns_server_sent_requests(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.1.64.1.4." + args["index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
        return result, {"ret_sent_requests": parse_result}

    def check_dns_server_successful_requests(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.1.64.1.5." + args["index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
        return result, {"ret_successful_requests": parse_result}
