from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.site.base.SiteBaseCustomShowTools import \
    SiteBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return SiteCustomShowTools(device)


class SiteCustomShowTools(SiteBaseCustomShowTools):
    def __init__(self, device):
        super(SiteCustomShowTools, self).__init__(device)

    # #################################################################################################################
    #   Current Parser Functions   ####################################################################################
    # #################################################################################################################
    def check_site_exists(self, output, args, **kwargs):
        site_offset = 0
        site_word = ""
        site_name_in_table = list()
        for site_word in args['site_name'].split():
            site_name_in_table.append(self.pw.get_value_by_offset(output, site_word, site_offset))
            site_offset += 1

        result = True if site_word in site_name_in_table else False

        return result, {"ret_site": ', '.join(site_name_in_table)}

    def check_site_ap_exists(self, output, args, **kwargs):
        output = output.splitlines()

        for line in output:
            if "(" in line and ")" in line:
                current_ap_name = line[line.find("(") + 1:line.find(")")]
                result = True if current_ap_name == args['ap_name'] else False
                return result, {"ret_ap": current_ap_name}
        return False, False

    def check_site_dns_server_exists(self, output, args, **kwargs):
        dns_server_in_table = self.pw.get_value_by_offset(output, args['dns_server'], 2)

        result = True if args['dns_server'] in dns_server_in_table.split() else False

        return result, {"ret_dns_server": dns_server_in_table}

    def check_site_wlan_radio_mode_exists(self, output, args, **kwargs):
        wlan_offset = 0
        wlan_word = ""
        wlan_name_in_table = list()
        for wlan_word in args['wlan_name'].split():
            wlan_name_in_table.append(self.pw.get_value_by_offset(output, wlan_word, wlan_offset))
            wlan_offset += 1

        radio_mode_in_table = self.pw.get_value_by_offset(output, args['radio_mode'], wlan_offset)

        if wlan_word in wlan_name_in_table:
            result = True if args['radio_mode'] in radio_mode_in_table else False
            return result, {"ret_radio_mode": radio_mode_in_table}
        return False, {"ret_radio_mode": radio_mode_in_table}
