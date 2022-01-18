from ExtremeAutomation.Keywords.BaseClasses.EndsystemKeywordBaseClass import EndsystemKeywordBaseClass
from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.CommandApis.Constants.NetsightutilitiesConstants import \
    NetsightutilitiesConstants
from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.ParseApis.Constants.NetsightutilitiesConstants import \
    NetsightutilitiesConstants as ParseConstants


class EndsystemNetsightUtilitiesKeywords(EndsystemKeywordBaseClass):
    def __init__(self):
        super(EndsystemNetsightUtilitiesKeywords, self).__init__()
        self.api_const = self.constants.API_NETSIGHT_UTILITIES
        self.command_const = NetsightutilitiesConstants()
        self.parse_const = ParseConstants()

    def install_netsight(self, element_name, netsight_version, max_attempts=360, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The name of the device this keyword should run against.
        [netsight_version] - The version of netsight that should be installed.
        [max_attempts] - The number of times the rest client should retry before failing.

        This keyword installs the provided version of netsight on the given device.
        """
        args = {"netsight_version": netsight_version}

        return self.execute_keyword(element_name, args, self.command_const.INSTALL_NETSIGHT,
                                    max_attempts=max_attempts, **kwargs)

    def restart_netsight_and_redeploy_war_file(self, element_name, max_attempts=360, **kwargs):
        """
        Keyword Arguments:
        [element_name] - THe name of the device this keyword should run against.
        [max_attempts] - The number of times the rest client should retry before failing.

        This keyword restarts the netsight server running on the given device.
        """
        return self.execute_keyword(element_name, {}, self.command_const.RESTART_NETSIGHT_AND_REDEPLOY_WAR_FILE,
                                    max_attempts=max_attempts, **kwargs)

    def netsight_script_copy(self, element_name, server_ip, script_directory, script_name, username="anonymous",
                             password="''", server_type='ftp',
                             xmc_dir=r'C:/Program Files/Extreme Networks/NetSight/appdata/scripting/overrides/',
                             max_attempts=360, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The name of the device this keyword should run against.
        [script_name] - The name of the script to copy to netsight.
        [max_attempts] - The number of times the rest client should retry before failing.

        This function copies the script with name <script_name> to the given netsight server.
        """
        args = {"script_name": script_name,
                'server_ip': server_ip,
                'script_directory': script_directory,
                'username': username,
                'password': password,
                'server_type': server_type,
                'xmc_dir': xmc_dir}

        return self.execute_keyword(element_name, args, self.command_const.NETSIGHT_SCRIPT_COPY,
                                    max_attempts=max_attempts, **kwargs)

    def netsight_log_copy(self, element_name, log_name='server.log', test_engine_ip='1.1.1.1',
                          test_engine_username="administrator", test_engine_pw='extreme', max_attempts=60, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The name of the device this keyword should run against.
        [log_name] - The name of the log file to copy.
        [test_engine_ip] - The IP of the engine the log file should be copied to.
        [test_engine_username] - The username of the engine.
        [test_engine_pw] - The password for the engine.
        [max_attempts] - The number of times the rest client should retry before failing.

        This keyword copies the log file with name <log_name> to the provided test engine.
        """
        guid = 'abcd'
        try:
            self.logger.log_info("Saving LOG to Test Engine")
        except (KeyError):
            self.logger.log_info("No GUID from Test Engine.  Saving LOG to Local XMC server")
            pass

        args = {'guid': guid,
                'test_engine_ip': test_engine_ip,
                'test_engine_username': test_engine_username,
                'test_engine_pw': test_engine_pw,
                'log_name': log_name}

        return self.execute_keyword(element_name, args, self.command_const.NETSIGHT_LOG_COPY,
                                    max_attempts=max_attempts, **kwargs)

    def test_route(self, element_name, max_attempts=360, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The name of the device this keyword should run against.
        [script_name] - The name of the script to copy to netsight.
        [max_attempts] - The number of times the rest client should retry before failing.

        This function copies the script with name <script_name> to the given netsight server.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.TEST_ROUTE,
                                    max_attempts=max_attempts, **kwargs)

    def demo_post(self, element_name, message_to_post, max_attempts=360, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The name of the device this keyword should run against.
        [script_name] - The name of the script to copy to netsight.
        [max_attempts] - The number of times the rest client should retry before failing.

        This function copies the script with name <script_name> to the given netsight server.
        """
        args = {'message_to_post': message_to_post}

        return self.execute_keyword(element_name, args, self.command_const.DEMO_POST,
                                    max_attempts=max_attempts, **kwargs)

    def demo_read_log(self, element_name, max_attempts=360, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The name of the device this keyword should run against.
        [script_name] - The name of the script to copy to netsight.
        [max_attempts] - The number of times the rest client should retry before failing.

        This function copies the script with name <script_name> to the given netsight server.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.DEMO_READ_LOG,
                                    max_attempts=max_attempts, **kwargs)

    def demo_read_log_all(self, element_name, max_attempts=360, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The name of the device this keyword should run against.
        [script_name] - The name of the script to copy to netsight.
        [max_attempts] - The number of times the rest client should retry before failing.

        This function copies the script with name <script_name> to the given netsight server.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.DEMO_READ_LOG_ALL,
                                    max_attempts=max_attempts, **kwargs)

    def demo_inspect_read_all(self, element_name, rest_inspect_data, max_attempts=360, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The name of the device this keyword should run against.
        [script_name] - The name of the script to copy to netsight.
        [max_attempts] - The number of times the rest client should retry before failing.

        This function copies the script with name <script_name> to the given netsight server.
        """
        args = {'rest_inspect_data': rest_inspect_data}

        return self.execute_verify_keyword(element_name, args, self.command_const.DEMO_READ_LOG_ALL,
                                           self.parse_const.VERIFY_REST_READ_ALL, True, "NONE", "NONE",
                                           max_attempts=max_attempts, **kwargs)

    def demo_inspect_read(self, element_name, rest_inspect_data, max_attempts=360, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The name of the device this keyword should run against.
        [script_name] - The name of the script to copy to netsight.
        [max_attempts] - The number of times the rest client should retry before failing.

        This function copies the script with name <script_name> to the given netsight server.
        """
        args = {'rest_inspect_data': rest_inspect_data}

        return self.execute_verify_keyword(element_name, args, self.command_const.DEMO_READ_LOG,
                                           self.parse_const.VERIFY_REST_READ, True, "Was properly in json output",
                                           "Was NOT in json output", max_attempts=max_attempts, **kwargs)
