from ExtremeAutomation.Library.Device.Common.Agents.RestAgent import RestAgent


class JsonRpcAgent(RestAgent):
    def __init__(self, device):
        super(JsonRpcAgent, self).__init__(device)
        self.rpc_version = JsonRpcConstants.VERSION_2_0
        self.method = JsonRpcConstants.METHOD_CLI

    def get_request_args(self, cmd_obj):
        """
        Function Args:
            [cmd_obj] - The command object that is going to be used to create a rest request.
                        Unlike the rest agent this will likely be a CliCommandObject.

        This function creates a dictionary of arguments to pass to the request.<type> function.
        The following attributes are set.

            verify  - A boolean indicating whether or not the server's cert should be verified.
                      This is always false for JSON RPC requests.
            headers - Currently only the Content-Type header is included. If JSON RPC requires
                      additional headers in the future they should be added here.
            auth    - The authentication information for the device we are sending the
                      request to.
            json    - This contains the command ID, JSON RPC version, JSON RPC method, and
                      the command to be executed.
        """
        return {"verify": False,
                "method": "post",
                "url": self.get_full_uri(cmd_obj),
                "headers": {"Content-Type": "application/json"},
                "auth": (self.device.username, self.device.password),
                "json": {"id": 0,
                         "jsonrpc": self.rpc_version,
                         "method": self.method,
                         "params": [cmd_obj.command]}}

    def get_full_uri(self, cmd_obj):
        """
        Function Args:
            [uri] - The partial uri to convert into a full uri.

        This function returns the jsonrpc uri based on the current device's username.
        """
        return "http://" + self.device.hostname + "/jsonrpc"


class JsonRpcConstants(object):
    VERSION_2_0 = "2.0"
    METHOD_CLI = "cli"
