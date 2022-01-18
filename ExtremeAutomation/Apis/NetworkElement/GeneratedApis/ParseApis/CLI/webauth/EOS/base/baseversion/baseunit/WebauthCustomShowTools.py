from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.webauth.base.WebauthBaseCustomShowTools import \
    WebauthBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return WebauthCustomShowTools(device)


class WebauthCustomShowTools(WebauthBaseCustomShowTools):
    def __init__(self, device):
        super(WebauthCustomShowTools, self).__init__(device)

    def check_webauth_enabled(self, output, args, **kwargs):
        res = self.pw.get_value_by_offset(output, 'PWA Status', 3)

        result = True if res == "enabled" else False
        return result, {"ret_state": res}

    def check_webauth_enabled_on_port(self, output, args, **kwargs):
        res = self.pw.get_value_by_offset(output, args["port"], 1)

        result = True if res == "enabled" else False
        return result, {"ret_port_state": res}

    def check_webauth_base_url_exists(self, output, args, **kwargs):
        res = self.pw.get_value_by_offset(output, 'PWA Hostname', 3)

        result = True if res == args["base_url"] else False
        return result, {"ret_url_name": res}
