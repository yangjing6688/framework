from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.lacp.base.LacpBaseCustomShowTools import \
    LacpBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


def create_instance(device):
    return LacpCustomShowTools(device)


class LacpCustomShowTools(LacpBaseCustomShowTools):
    def __init__(self, device):
        super(LacpCustomShowTools, self).__init__(device)

    def verify_lacp_enabled(self, output, args, **kwargs):
        lacp_output = self.pw.get_value_by_offset(output, "LACP Enabled", 3)

        result = True if lacp_output.lower() == "yes" else False
        return result, {"ret_lacp_enabled": lacp_output}

    def check_port_is_in_lag(self, output, args, **kwargs):
        output = StringUtils.format_json_output(output)
        parse_lag_ports = list()

        if isinstance(output, dict):
            for entry in output["result"]:
                try:
                    parse_master_port = str(entry["ls_ports_show"]["loadShareMaster"])
                    if parse_master_port == args["port"]:
                        parse_lag_ports.append(str(entry["ls_ports_show"]["port"]))
                except KeyError:
                    pass
        else:
            master_port_line = None
            output = output.splitlines()

            # This loop checks each line of output for long strings of "=". In the EXOS output of "show sharing detail"
            # this denotes the start of a load sharing group. Once at least 5 "=" are found we grab the master port,
            # then compare it to the master port entered by the user. If they match we know we found the correct group.
            # We save the line number we found the group on to use in the next if statement.
            for index, line in enumerate(output):
                if line.find("=====") == 0:
                    parse_master_port = self.pw.get_value_by_offset(output[index + 1], args["port"], 0)
                    if parse_master_port == args["port"]:
                        master_port_line = index + 1
                        break
                elif line.find("VLAN Configuration:") == 0:
                    break

            # If a master port line number was found we start a new loop. If the master port the user entered was not
            # found in the output the function will return False. The while loop checks each line starting from
            # master port line for the port number. If the line above a given line contains 5 "=" we know it's the
            # first line and it's parsed differently than the other lines. Each line is processed until another string
            # of 5 "=" are found, at this point we know we are at the end of the groups section.
            if master_port_line is not None:
                while output[master_port_line].find("=====") == -1:
                    if output[master_port_line - 1].find("=====") == 0:
                        # If the first line in the group is being parsed first check if "lacp", "static", or "sharing"
                        # are at index 1. If it is we know that the current master section is blank and the port is at
                        # index 5, otherwise it's at index 6.
                        if self.pw.get_value_by_offset(output[master_port_line], "", 1).lower() in \
                                ["lacp", "static", "health"]:
                            tmp_port = self.pw.get_value_by_offset(output[master_port_line], "", 5)
                        else:
                            tmp_port = self.pw.get_value_by_offset(output[master_port_line], "", 6)
                    # if it is any line other than the first the port is at index 1.
                    else:
                        tmp_port = self.pw.get_value_by_offset(output[master_port_line], "", 1)

                    parse_lag_ports.append(tmp_port)
                    master_port_line += 1

        result = args["lag_port"] in parse_lag_ports
        return result, {"ret_ports": parse_lag_ports}
