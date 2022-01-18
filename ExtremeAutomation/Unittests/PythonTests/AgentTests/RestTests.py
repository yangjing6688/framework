import mock
from requests import Response
from ExtremeAutomation.Unittests.Utilities.RobotUnitTest import RobotUnitTest
from ExtremeAutomation.Library.Device.Common.Agents.RestAgent import RestAgent, RestAgentConstants
from ExtremeAutomation.Library.Device.Common.CommandObjects.RestCommandObject import RestCommandObject
from ExtremeAutomation.Library.Device.NetworkElement.NetworkElement import NetworkElement
from ExtremeAutomation.Library.Device.NetworkElement.Constants.NetworkElementConstants import NetworkElementConstants


class RestTest(RobotUnitTest):
    @classmethod
    def setUpClass(cls):
        cls.dev = NetworkElement(NetworkElementConstants.OS_SNAP_ROUTE, NetworkElementConstants.PLATFORM_BASE,
                                 NetworkElementConstants.UNIT_BASE, NetworkElementConstants.VERSION_BASE)
        cls.dev.hostname = "127.0.0.1"

    # +------------------+
    # | Get Method Tests |
    # +------------------+
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.RestAgent.requests.request")
    def test_send_command_get(self, mock_requests):
        rest_agent = self.__create_rest_agent(RestAgentConstants.AUTH_NONE, True)
        mock_requests.return_value.text = "get"
        rest_agent.send_command("get get_test")
        mock_requests.assert_called_with(**self.__get_send_cmd_args(rest_agent, "get", "get_test"))

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.RestAgent.requests.request")
    def test_send_command_object_get(self, mock_requests):
        rest_agent = self.__create_rest_agent(RestAgentConstants.AUTH_NONE, True)
        cmd_obj = self.__create_cmd_obj("get_test", "get")
        mock_requests.return_value.text = "get"
        rest_agent.send_command_object(cmd_obj)
        mock_requests.assert_called_with(**self.__get_send_cmd_obj_args(rest_agent, cmd_obj))

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.RestAgent.requests.request")
    def test_send_command_object_get_ssl(self, mock_requests):
        rest_agent = self.__create_rest_agent(RestAgentConstants.AUTH_SSL, True)
        cmd_obj = self.__create_cmd_obj("get_test", "get")
        mock_requests.return_value.text = "get"
        rest_agent.send_command_object(cmd_obj)
        mock_requests.assert_called_with(**self.__get_send_cmd_obj_args(rest_agent, cmd_obj))

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.RestAgent.requests.request")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.RestAgent.HTTPBasicAuth.__new__")
    def test_send_command_object_get_basic(self, mock_auth, mock_requests):
        rest_agent = self.__create_rest_agent(RestAgentConstants.AUTH_BASIC, True)
        cmd_obj = self.__create_cmd_obj("get_test", "get")
        mock_requests.return_value.text = "get"
        mock_auth.return_value = "HTTPBasicAuth"
        rest_agent.send_command_object(cmd_obj)
        mock_requests.assert_called_with(**self.__get_send_cmd_obj_args(rest_agent, cmd_obj))

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.RestAgent.requests.request")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.RestAgent.HTTPBasicAuth.__new__")
    def test_send_command_object_get_basic_ssl(self, mock_auth, mock_requests):
        rest_agent = self.__create_rest_agent(RestAgentConstants.AUTH_BASIC_SSL, True)
        cmd_obj = self.__create_cmd_obj("get_test", "get")
        mock_requests.return_value.text = "get"
        mock_auth.return_value = "HTTPBasicAuth"
        rest_agent.send_command_object(cmd_obj)
        mock_requests.assert_called_with(**self.__get_send_cmd_obj_args(rest_agent, cmd_obj))

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.RestAgent.requests.request")
    def test_send_command_object_get_oauth(self, mock_requests):
        rest_agent = self.__create_rest_agent(RestAgentConstants.AUTH_OAUTH, True)
        cmd_obj = self.__create_cmd_obj("get_test", "get")
        mock_requests.return_value.text = "get"
        rest_agent.send_command_object(cmd_obj)
        mock_requests.assert_called_with(**self.__get_send_cmd_obj_args(rest_agent, cmd_obj))

    # +------------------+
    # | Put Method Tests |
    # +------------------+
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.RestAgent.requests.request")
    def test_send_command_put(self, mock_requests):
        rest_agent = self.__create_rest_agent(RestAgentConstants.AUTH_NONE, True)
        mock_requests.return_value.text = "put"
        rest_agent.send_command("put put_test")
        mock_requests.assert_called_with(**self.__get_send_cmd_args(rest_agent, "put", "put_test"))

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.RestAgent.requests.request")
    def test_send_command_object_put(self, mock_requests):
        rest_agent = self.__create_rest_agent(RestAgentConstants.AUTH_NONE, True)
        cmd_obj = self.__create_cmd_obj("put_test", "put")
        mock_requests.return_value.text = "put"
        rest_agent.send_command_object(cmd_obj)
        mock_requests.assert_called_with(**self.__get_send_cmd_obj_args(rest_agent, cmd_obj))

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.RestAgent.requests.request")
    def test_send_command_object_put_ssl(self, mock_requests):
        rest_agent = self.__create_rest_agent(RestAgentConstants.AUTH_SSL, True)
        cmd_obj = self.__create_cmd_obj("put_test", "put")
        mock_requests.return_value.text = "put"
        rest_agent.send_command_object(cmd_obj)
        mock_requests.assert_called_with(**self.__get_send_cmd_obj_args(rest_agent, cmd_obj))

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.RestAgent.requests.request")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.RestAgent.HTTPBasicAuth.__new__")
    def test_send_command_object_put_basic(self, mock_auth, mock_requests):
        rest_agent = self.__create_rest_agent(RestAgentConstants.AUTH_BASIC, True)
        cmd_obj = self.__create_cmd_obj("put_test", "put")
        mock_requests.return_value.text = "put"
        mock_auth.return_value = "HTTPBasicAuth"
        rest_agent.send_command_object(cmd_obj)
        mock_requests.assert_called_with(**self.__get_send_cmd_obj_args(rest_agent, cmd_obj))

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.RestAgent.requests.request")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.RestAgent.HTTPBasicAuth.__new__")
    def test_send_command_object_put_basic_ssl(self, mock_auth, mock_requests):
        rest_agent = self.__create_rest_agent(RestAgentConstants.AUTH_BASIC_SSL, True)
        cmd_obj = self.__create_cmd_obj("put_test", "put")
        mock_requests.return_value.text = "put"
        mock_auth.return_value = "HTTPBasicAuth"
        rest_agent.send_command_object(cmd_obj)
        mock_requests.assert_called_with(**self.__get_send_cmd_obj_args(rest_agent, cmd_obj))

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.RestAgent.requests.request")
    def test_send_command_object_put_oauth(self, mock_requests):
        rest_agent = self.__create_rest_agent(RestAgentConstants.AUTH_OAUTH, True)
        cmd_obj = self.__create_cmd_obj("put_test", "put")
        mock_requests.return_value.text = "put"
        rest_agent.send_command_object(cmd_obj)
        mock_requests.assert_called_with(**self.__get_send_cmd_obj_args(rest_agent, cmd_obj))

    # +-------------------+
    # | Post Method Tests |
    # +-------------------+
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.RestAgent.requests.request")
    def test_send_command_post(self, mock_requests):
        rest_agent = self.__create_rest_agent(RestAgentConstants.AUTH_NONE, True)
        mock_requests.return_value.text = "post"
        rest_agent.send_command("post post_test")
        mock_requests.assert_called_with(**self.__get_send_cmd_args(rest_agent, "post", "post_test"))

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.RestAgent.requests.request")
    def test_send_command_object_post(self, mock_requests):
        rest_agent = self.__create_rest_agent(RestAgentConstants.AUTH_NONE, True)
        cmd_obj = self.__create_cmd_obj("post_test", "post")
        mock_requests.return_value.text = "post"
        rest_agent.send_command_object(cmd_obj)
        mock_requests.assert_called_with(**self.__get_send_cmd_obj_args(rest_agent, cmd_obj))

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.RestAgent.requests.request")
    def test_send_command_object_post_ssl(self, mock_requests):
        rest_agent = self.__create_rest_agent(RestAgentConstants.AUTH_SSL, True)
        cmd_obj = self.__create_cmd_obj("post_test", "post")
        mock_requests.return_value.text = "post"
        rest_agent.send_command_object(cmd_obj)
        mock_requests.assert_called_with(**self.__get_send_cmd_obj_args(rest_agent, cmd_obj))

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.RestAgent.requests.request")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.RestAgent.HTTPBasicAuth.__new__")
    def test_send_command_object_post_basic(self, mock_auth, mock_requests):
        rest_agent = self.__create_rest_agent(RestAgentConstants.AUTH_BASIC, True)
        cmd_obj = self.__create_cmd_obj("post_test", "post")
        mock_requests.return_value.text = "post"
        mock_auth.return_value = "HTTPBasicAuth"
        rest_agent.send_command_object(cmd_obj)
        mock_requests.assert_called_with(**self.__get_send_cmd_obj_args(rest_agent, cmd_obj))

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.RestAgent.requests.request")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.RestAgent.HTTPBasicAuth.__new__")
    def test_send_command_object_post_basic_ssl(self, mock_auth, mock_requests):
        rest_agent = self.__create_rest_agent(RestAgentConstants.AUTH_BASIC_SSL, True)
        cmd_obj = self.__create_cmd_obj("post_test", "post")
        mock_requests.return_value.text = "post"
        mock_auth.return_value = "HTTPBasicAuth"
        rest_agent.send_command_object(cmd_obj)
        mock_requests.assert_called_with(**self.__get_send_cmd_obj_args(rest_agent, cmd_obj))

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.RestAgent.requests.request")
    def test_send_command_object_post_oauth(self, mock_requests):
        rest_agent = self.__create_rest_agent(RestAgentConstants.AUTH_OAUTH, True)
        cmd_obj = self.__create_cmd_obj("post_test", "post")
        mock_requests.return_value.text = "post"
        rest_agent.send_command_object(cmd_obj)
        mock_requests.assert_called_with(**self.__get_send_cmd_obj_args(rest_agent, cmd_obj))

    # +---------------------+
    # | Delete Method Tests |
    # +---------------------+
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.RestAgent.requests.request")
    def test_send_command_delete(self, mock_requests):
        rest_agent = self.__create_rest_agent(RestAgentConstants.AUTH_NONE, True)
        mock_requests.return_value.text = "delete"
        rest_agent.send_command("delete delete_test")
        mock_requests.assert_called_with(**self.__get_send_cmd_args(rest_agent, "delete", "delete_test"))

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.RestAgent.requests.request")
    def test_send_command_object_delete(self, mock_requests):
        rest_agent = self.__create_rest_agent(RestAgentConstants.AUTH_NONE, True)
        cmd_obj = self.__create_cmd_obj("delete_test", "delete")
        mock_requests.return_value.text = "delete"
        rest_agent.send_command_object(cmd_obj)
        mock_requests.assert_called_with(**self.__get_send_cmd_obj_args(rest_agent, cmd_obj))

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.RestAgent.requests.request")
    def test_send_command_object_delete_ssl(self, mock_requests):
        rest_agent = self.__create_rest_agent(RestAgentConstants.AUTH_SSL, True)
        cmd_obj = self.__create_cmd_obj("delete_test", "delete")
        mock_requests.return_value.text = "delete"
        rest_agent.send_command_object(cmd_obj)
        mock_requests.assert_called_with(**self.__get_send_cmd_obj_args(rest_agent, cmd_obj))

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.RestAgent.requests.request")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.RestAgent.HTTPBasicAuth.__new__")
    def test_send_command_object_delete_basic(self, mock_auth, mock_requests):
        rest_agent = self.__create_rest_agent(RestAgentConstants.AUTH_BASIC, True)
        cmd_obj = self.__create_cmd_obj("delete_test", "delete")
        mock_requests.return_value.text = "delete"
        mock_auth.return_value = "HTTPBasicAuth"
        rest_agent.send_command_object(cmd_obj)
        mock_requests.assert_called_with(**self.__get_send_cmd_obj_args(rest_agent, cmd_obj))

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.RestAgent.requests.request")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.RestAgent.HTTPBasicAuth.__new__")
    def test_send_command_object_delete_basic_ssl(self, mock_auth, mock_requests):
        rest_agent = self.__create_rest_agent(RestAgentConstants.AUTH_BASIC_SSL, True)
        cmd_obj = self.__create_cmd_obj("delete_test", "delete")
        mock_requests.return_value.text = "delete"
        mock_auth.return_value = "HTTPBasicAuth"
        rest_agent.send_command_object(cmd_obj)
        mock_requests.assert_called_with(**self.__get_send_cmd_obj_args(rest_agent, cmd_obj))

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.RestAgent.requests.request")
    def test_send_command_object_delete_oauth(self, mock_requests):
        rest_agent = self.__create_rest_agent(RestAgentConstants.AUTH_OAUTH, True)
        cmd_obj = self.__create_cmd_obj("delete_test", "delete")
        mock_requests.return_value.text = "delete"
        rest_agent.send_command_object(cmd_obj)
        mock_requests.assert_called_with(**self.__get_send_cmd_obj_args(rest_agent, cmd_obj))

    # +--------------------+
    # | Patch Method Tests |
    # +--------------------+
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.RestAgent.requests.request")
    def test_send_command_patch(self, mock_requests):
        rest_agent = self.__create_rest_agent(RestAgentConstants.AUTH_NONE, True)
        mock_requests.return_value.text = "patch"
        rest_agent.send_command("patch patch_test")
        mock_requests.assert_called_with(**self.__get_send_cmd_args(rest_agent, "patch", "patch_test"))

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.RestAgent.requests.request")
    def test_send_command_object_patch(self, mock_requests):
        rest_agent = self.__create_rest_agent(RestAgentConstants.AUTH_NONE, True)
        cmd_obj = self.__create_cmd_obj("patch_test", "patch")
        mock_requests.return_value.text = "patch"
        rest_agent.send_command_object(cmd_obj)
        mock_requests.assert_called_with(**self.__get_send_cmd_obj_args(rest_agent, cmd_obj))

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.RestAgent.requests.request")
    def test_send_command_object_patch_ssl(self, mock_requests):
        rest_agent = self.__create_rest_agent(RestAgentConstants.AUTH_SSL, True)
        cmd_obj = self.__create_cmd_obj("patch_test", "patch")
        mock_requests.return_value.text = "patch"
        rest_agent.send_command_object(cmd_obj)
        mock_requests.assert_called_with(**self.__get_send_cmd_obj_args(rest_agent, cmd_obj))

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.RestAgent.requests.request")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.RestAgent.HTTPBasicAuth.__new__")
    def test_send_command_object_patch_basic(self, mock_auth, mock_requests):
        rest_agent = self.__create_rest_agent(RestAgentConstants.AUTH_BASIC, True)
        cmd_obj = self.__create_cmd_obj("patch_test", "patch")
        mock_requests.return_value.text = "patch"
        mock_auth.return_value = "HTTPBasicAuth"
        rest_agent.send_command_object(cmd_obj)
        mock_requests.assert_called_with(**self.__get_send_cmd_obj_args(rest_agent, cmd_obj))

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.RestAgent.requests.request")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.RestAgent.HTTPBasicAuth.__new__")
    def test_send_command_object_patch_basic_ssl(self, mock_auth, mock_requests):
        rest_agent = self.__create_rest_agent(RestAgentConstants.AUTH_BASIC_SSL, True)
        cmd_obj = self.__create_cmd_obj("patch_test", "patch")
        mock_requests.return_value.text = "patch"
        mock_auth.return_value = "HTTPBasicAuth"
        rest_agent.send_command_object(cmd_obj)
        mock_requests.assert_called_with(**self.__get_send_cmd_obj_args(rest_agent, cmd_obj))

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.RestAgent.requests.request")
    def test_send_command_object_patch_oauth(self, mock_requests):
        rest_agent = self.__create_rest_agent(RestAgentConstants.AUTH_OAUTH, True)
        cmd_obj = self.__create_cmd_obj("patch_test", "patch")
        mock_requests.return_value.text = "patch"
        rest_agent.send_command_object(cmd_obj)
        mock_requests.assert_called_with(**self.__get_send_cmd_obj_args(rest_agent, cmd_obj))

    # +----------------------+
    # | Options Method Tests |
    # +----------------------+
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.RestAgent.requests.request")
    def test_send_command_options(self, mock_requests):
        rest_agent = self.__create_rest_agent(RestAgentConstants.AUTH_NONE, True)
        mock_requests.return_value.text = "options"
        rest_agent.send_command("options options_test")
        mock_requests.assert_called_with(**self.__get_send_cmd_args(rest_agent, "options", "options_test"))

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.RestAgent.requests.request")
    def test_send_command_object_options(self, mock_requests):
        rest_agent = self.__create_rest_agent(RestAgentConstants.AUTH_NONE, True)
        cmd_obj = self.__create_cmd_obj("options_test", "options")
        mock_requests.return_value.text = "options"
        rest_agent.send_command_object(cmd_obj)
        mock_requests.assert_called_with(**self.__get_send_cmd_obj_args(rest_agent, cmd_obj))

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.RestAgent.requests.request")
    def test_send_command_object_options_ssl(self, mock_requests):
        rest_agent = self.__create_rest_agent(RestAgentConstants.AUTH_SSL, True)
        cmd_obj = self.__create_cmd_obj("options_test", "options")
        mock_requests.return_value.text = "options"
        rest_agent.send_command_object(cmd_obj)
        mock_requests.assert_called_with(**self.__get_send_cmd_obj_args(rest_agent, cmd_obj))

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.RestAgent.requests.request")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.RestAgent.HTTPBasicAuth.__new__")
    def test_send_command_object_options_basic(self, mock_auth, mock_requests):
        rest_agent = self.__create_rest_agent(RestAgentConstants.AUTH_BASIC, True)
        cmd_obj = self.__create_cmd_obj("options_test", "options")
        mock_requests.return_value.text = "options"
        mock_auth.return_value = "HTTPBasicAuth"
        rest_agent.send_command_object(cmd_obj)
        mock_requests.assert_called_with(**self.__get_send_cmd_obj_args(rest_agent, cmd_obj))

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.RestAgent.requests.request")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.RestAgent.HTTPBasicAuth.__new__")
    def test_send_command_object_options_basic_ssl(self, mock_auth, mock_requests):
        rest_agent = self.__create_rest_agent(RestAgentConstants.AUTH_BASIC_SSL, True)
        cmd_obj = self.__create_cmd_obj("options_test", "options")
        mock_requests.return_value.text = "options"
        mock_auth.return_value = "HTTPBasicAuth"
        rest_agent.send_command_object(cmd_obj)
        mock_requests.assert_called_with(**self.__get_send_cmd_obj_args(rest_agent, cmd_obj))

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.RestAgent.requests.request")
    def test_send_command_object_options_oauth(self, mock_requests):
        rest_agent = self.__create_rest_agent(RestAgentConstants.AUTH_OAUTH, True)
        cmd_obj = self.__create_cmd_obj("options_test", "options")
        mock_requests.return_value.text = "options"
        rest_agent.send_command_object(cmd_obj)
        mock_requests.assert_called_with(**self.__get_send_cmd_obj_args(rest_agent, cmd_obj))

    # +-------------------+
    # | Head Method Tests |
    # +-------------------+
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.RestAgent.requests.request")
    def test_send_command_head(self, mock_requests):
        rest_agent = self.__create_rest_agent(RestAgentConstants.AUTH_NONE, True)
        mock_requests.return_value.text = "head"
        rest_agent.send_command("head head_test")
        mock_requests.assert_called_with(**self.__get_send_cmd_args(rest_agent, "head", "head_test"))

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.RestAgent.requests.request")
    def test_send_command_object_head(self, mock_requests):
        rest_agent = self.__create_rest_agent(RestAgentConstants.AUTH_NONE, True)
        cmd_obj = self.__create_cmd_obj("head_test", "head")
        mock_requests.return_value.text = "head"
        rest_agent.send_command_object(cmd_obj)
        mock_requests.assert_called_with(**self.__get_send_cmd_obj_args(rest_agent, cmd_obj))

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.RestAgent.requests.request")
    def test_send_command_object_head_ssl(self, mock_requests):
        rest_agent = self.__create_rest_agent(RestAgentConstants.AUTH_SSL, True)
        cmd_obj = self.__create_cmd_obj("head_test", "head")
        mock_requests.return_value.text = "head"
        rest_agent.send_command_object(cmd_obj)
        mock_requests.assert_called_with(**self.__get_send_cmd_obj_args(rest_agent, cmd_obj))

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.RestAgent.requests.request")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.RestAgent.HTTPBasicAuth.__new__")
    def test_send_command_object_head_basic(self, mock_auth, mock_requests):
        rest_agent = self.__create_rest_agent(RestAgentConstants.AUTH_BASIC, True)
        cmd_obj = self.__create_cmd_obj("head_test", "head")
        mock_requests.return_value.text = "head"
        mock_auth.return_value = "HTTPBasicAuth"
        rest_agent.send_command_object(cmd_obj)
        mock_requests.assert_called_with(**self.__get_send_cmd_obj_args(rest_agent, cmd_obj))

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.RestAgent.requests.request")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.RestAgent.HTTPBasicAuth.__new__")
    def test_send_command_object_head_basic_ssl(self, mock_auth, mock_requests):
        rest_agent = self.__create_rest_agent(RestAgentConstants.AUTH_BASIC_SSL, True)
        cmd_obj = self.__create_cmd_obj("head_test", "head")
        mock_requests.return_value.text = "head"
        mock_auth.return_value = "HTTPBasicAuth"
        rest_agent.send_command_object(cmd_obj)
        mock_requests.assert_called_with(**self.__get_send_cmd_obj_args(rest_agent, cmd_obj))

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.RestAgent.requests.request")
    def test_send_command_object_head_oauth(self, mock_requests):
        rest_agent = self.__create_rest_agent(RestAgentConstants.AUTH_OAUTH, True)
        cmd_obj = self.__create_cmd_obj("head_test", "head")
        mock_requests.return_value.text = "head"
        rest_agent.send_command_object(cmd_obj)
        mock_requests.assert_called_with(**self.__get_send_cmd_obj_args(rest_agent, cmd_obj))

    # +------------------------+
    # | Other Rest Agent Tests |
    # +------------------------+
    def test_check_response_code_good(self):
        result = True
        rest_agent = self.__create_rest_agent(RestAgentConstants.AUTH_NONE, True)
        http_codes = range(100, 400)

        for code in http_codes:
            response = Response()
            response.status_code = code
            result &= rest_agent.check_response_code(response)

        self.assertTrue(result)

    def test_check_client_error_code(self):
        result = False
        rest_agent = self.__create_rest_agent(RestAgentConstants.AUTH_NONE, True)
        http_codes = range(400, 500)

        for code in http_codes:
            response = Response()
            response.status_code = code
            result &= rest_agent.check_response_code(response)

        self.assertFalse(result)

    def test_check_server_error_code(self):
        result = False
        rest_agent = self.__create_rest_agent(RestAgentConstants.AUTH_NONE, True)
        http_codes = range(500, 600)

        for code in http_codes:
            response = Response()
            response.status_code = code
            result &= rest_agent.check_response_code(response)

        self.assertFalse(result)

    def test_generate_url(self):
        rest_agent = self.__create_rest_agent(RestAgentConstants.AUTH_NONE, True)
        cmd_obj = RestCommandObject()
        cmd_obj.uri = ""
        self.assertEqual(rest_agent.get_full_uri(cmd_obj),
                         "http://" + self.dev.hostname + ":" + str(self.dev.port) + "/")

    def test_generate_url_secure(self):
        rest_agent = self.__create_rest_agent(RestAgentConstants.AUTH_SSL, True)
        cmd_obj = RestCommandObject()
        cmd_obj.uri = ""
        self.assertEqual(rest_agent.get_full_uri(cmd_obj),
                         "https://" + self.dev.hostname + ":" + str(self.dev.port) + "/")

    # +-------------------------+
    # | Non-Test Helper Methods |
    # +-------------------------+
    @staticmethod
    def __create_cmd_obj(uri, query_type):
        cmd_obj = RestCommandObject()
        cmd_obj.uri = uri
        cmd_obj.request_type = query_type
        cmd_obj.headers = {"my_header": "test"}

        return cmd_obj

    def __create_rest_agent(self, auth_mode, verify_cert):
        rest_agent = RestAgent(self.dev)
        rest_agent.auth_mode = auth_mode
        rest_agent.verify_cert = verify_cert

        if auth_mode == RestAgentConstants.AUTH_OAUTH:
            rest_agent.oauth_token = "OAuthToken"

        return rest_agent

    def __get_send_cmd_args(self, rest_agent, method, uri):
        return {"verify": True,
                "method": method,
                "url": self.__get_full_uri(rest_agent, uri)}

    def __get_send_cmd_obj_args(self, rest_agent, cmd_obj):
        args = {"verify": True,
                "method": cmd_obj.request_type,
                "url": self.__get_full_uri(rest_agent, cmd_obj.uri)}

        if rest_agent.auth_mode in [RestAgentConstants.AUTH_NONE,
                                    RestAgentConstants.AUTH_SSL]:
            args["headers"] = {"my_header": "test"}
        elif rest_agent.auth_mode in [RestAgentConstants.AUTH_BASIC,
                                      RestAgentConstants.AUTH_BASIC_SSL]:
            args["auth"] = "HTTPBasicAuth"
            args["headers"] = {"my_header": "test"}
        elif rest_agent.auth_mode == RestAgentConstants.AUTH_OAUTH:
            args["headers"] = {'Authorization': 'Bearer OAuthToken', "my_header": "test"}

        return args

    @staticmethod
    def __get_full_uri(rest_agent, uri):
        cmd_obj = RestCommandObject()
        cmd_obj.uri = uri
        return rest_agent.get_full_uri(cmd_obj)


if __name__ == '__main__':
    RobotUnitTest.main()
