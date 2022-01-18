from ExtremeAutomation.Library.Device.Common.Agents.RestAgent import RestAgent
from ExtremeAutomation.Library.Device.Common.Agents.RestAgent import RestAgentConstants


class NorthboundAgent(RestAgent):
    def __init__(self, device):
        super(NorthboundAgent, self).__init__(device)
        self.type = self.constants.TYPE_NORTHBOUND

    def send_command(self, command):
        """
        Calls RestAgent's send_command function with as a post plus the command passed.
        """
        return super(NorthboundAgent, self).send_command("post " + command)

    def send_command_object(self, cmd_obj, **kwargs):
        """
        Creates the query data then calls RestAgent's send_command_object with the updated data.
        """
        cmd_obj.data = {"query": cmd_obj.data}
        return super(NorthboundAgent, self).send_command_object(cmd_obj, **kwargs)

    def get_full_uri(self, cmd_obj):
        """
        URI - The string URI that should be used ot create the full URI string.

        For example uri="/debug/v1/generalinformation" would return...

        http://<hostname>:<port>/<uri>

        or

        https://<hostname>:<port>/<uri>

        if secured.
        """
        http_mode = "http://"

        if self.auth_mode in [RestAgentConstants.AUTH_SSL,
                              RestAgentConstants.AUTH_OAUTH,
                              RestAgentConstants.AUTH_BASIC_SSL]:
            http_mode = "https://"
        if cmd_obj.uri.startswith("/"):
            cmd_obj.uri = cmd_obj.uri[1::]
        return "{0}{1}:{2}/{3}".format(http_mode, self.device.hostname, str(self.device.port), cmd_obj.uri)
