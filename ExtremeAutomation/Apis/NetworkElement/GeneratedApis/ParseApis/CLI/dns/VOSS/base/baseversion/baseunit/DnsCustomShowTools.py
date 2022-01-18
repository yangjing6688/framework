from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.dns.base.DnsBaseCustomShowTools import \
    DnsBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.ListUtils import ListUtils
from ExtremeAutomation.Library.Utils.NumberUtils import NumberUtils


def create_instance(device):
    return DnsCustomShowTools(device)


class DnsCustomShowTools(DnsBaseCustomShowTools):
    def __init__(self, device):
        super(DnsCustomShowTools, self).__init__(device)

    def check_dns_ip_domain_name(self, output, args, **kwargs):
        domain_name = self.pw.get_value_by_offset(output.lower(), "domain name", 5)

        result = True if domain_name == args["domain_name"] else False
        return result, {"ret_domain_name": domain_name}

    def check_host_name(self, output, args, **kwargs):
        host_name = self.pw.get_value_by_offset(output.lower(), "host name", 3)

        result = True if host_name == args["host_name"] else False
        return result, {"ret_host_name": host_name}

    def check_host_ip(self, output, args, **kwargs):
        host_ip = self.pw.get_value_by_offset(output.lower(), "ip address", 4)

        result = True if host_ip == args["host_ip"] else False
        return result, {"ret_host_ip": host_ip}

    def check_dns_server_ip(self, output, args, **kwargs):
        addr_list = self.pw.get_value_by_offset(output.lower(), "address", 3).split()
        addr_list = ListUtils.convert_to_list(addr_list)

        if args["index"].isdigit():
            if len(addr_list) < int(args["index"]) + 1:
                return False, None
            elif addr_list[int(args["index"])] == "valueNotPresent":
                return False, {"ret_server_ip": addr_list[int(args["index"])]}
            else:
                result = True if addr_list[int(args["index"])] == args["ip_addr"] else False
                return result, {"ret_server_ip": addr_list[int(args["index"])]}
        else:
            return False, {"ret_server_ip": None}

    def check_dns_server_status(self, output, args, **kwargs):
        status_list = self.pw.get_value_by_offset(output.lower(), "status", 2).split()
        status_list = ListUtils.convert_to_list(status_list)

        if args["index"].isdigit():
            if len(status_list) < int(args["index"]) + 1:
                return False, None
            elif status_list[int(args["index"])] == "valueNotPresent":
                return False, {"ret_server_status": status_list[int(args["index"])]}
            else:
                result = True if status_list[int(args["index"])] == "active" else False
                return result, {"ret_server_status": status_list[int(args["index"])]}
        else:
            return False, {"ret_server_status": None}

    def check_dns_server_sent_requests(self, output, args, **kwargs):
        request_list = self.pw.get_value_by_offset(output.lower(), "total dns number", 10).split()
        request_list = ListUtils.convert_to_list(request_list)

        try:
            if len(request_list) < int(args["index"]) + 1:
                return False, None
            elif request_list[int(args["index"])] == "valueNotPresent":
                return False, {"ret_sent_requests": request_list[int(args["index"])]}
            else:
                return (NumberUtils.verify_expected_count(request_list[int(args["index"])],
                                                          args["count_operator"], args["count"]),
                        {"ret_sent_requests": request_list[int(args["index"])]})
        except ValueError as e:
            self.logger.log_error(e)
            return False, None

    def check_dns_server_successful_requests(self, output, args, **kwargs):
        success_list = self.pw.get_value_by_offset(output.lower(), "successful", 5).split()
        success_list = ListUtils.convert_to_list(success_list)

        if args["index"].isdigit():
            if len(success_list) < int(args["index"]) + 1:
                return False, {"ret_successful_requests": None}
            if success_list[int(args["index"])] == "valueNotPresent":
                return False, {"ret_successful_requests": success_list[int(args["index"])]}
            else:
                result = NumberUtils.verify_expected_count(success_list[int(args["index"])], args["count_operator"],
                                                           args["count"])
                return result, {"ret_successful_requests": success_list[int(args["index"])]}
        else:
            return False, {"ret_successful_requests": None}
