import time
from ExtremeAutomation.Library.Utils.ListUtils import ListUtils
from ExtremeAutomation.Keywords.Utils.PingKeywords import PingKeywords
from ExtremeAutomation.Keywords.FailureException import FailureException
from ExtremeAutomation.Library.Device.NetworkElement.NetworkElement import NetworkElement
from ExtremeAutomation.Library.Device.Common.Agents.AgentConstants import AgentConstants
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import \
    NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.ResetdeviceConstants \
    import ResetdeviceConstants as CommandConstants
from ExtremeAutomation.Keywords.NetworkElementKeywords.NetworkElementConnectionManager import \
    NetworkElementConnectionManager



class NetworkElementResetDeviceUtilsKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementResetDeviceUtilsKeywords, self).__init__()
        self.api_const = self.constants.API_RESETDEVICE
        self.cmd_const = CommandConstants()
        self.ping = PingKeywords()
        self.connect = NetworkElementConnectionManager()

    # ##################################################################################################################
    #   Configuration Keywords   #######################################################################################
    # ##################################################################################################################
    def reboot_network_element_now(self, device_names, **kwargs):
        """
        Keyword Arguments:
        [device_names] - The device(s) the keyword should be run against.

        Reboots the given network element.
        """
        device_names = ListUtils.convert_to_list(device_names)

        kw_results = []
        for device_name in device_names:
            dev, api, _ = self._init_keyword(device_name, self.api_const, wait_for_prompt=False, **kwargs)

            args = {"reboot_answer": "y",
                    "reboot_exos": "n"}

            cmd_obj = getattr(api, self.cmd_const.RESET_NOW)(args, **kwargs)

            if not cmd_obj.not_supported:
                cmd_obj = dev.send_command_object(cmd_obj)
                self.logger.log_info("Resetting " + device_name + " now.")

            if dev.current_agent.type != AgentConstants.TYPE_CONSOLE:
                dev.current_agent.connected = False
                dev.current_agent.logged_in = False
            else:
                dev.current_agent.logged_in = False

            kw_results.append(self._determine_result(dev, cmd_obj, **kwargs))
        return self._keyword_cleanup(kw_results)

    def reboot_network_element_with_config(self, device_names, config_name, **kwargs):
        """
        Keyword Arguments:
        [device_names] - The device(s) the keyword should run against.
        [config_name] - The name of the configuration that should be loaded.

        Loads the given configuration on the network element and then resets the device.
        """
        device_names = ListUtils.convert_to_list(device_names)

        kw_results = []
        for device_name in device_names:
            dev, api, _ = self._init_keyword(device_name, self.api_const, wait_for_prompt=False, **kwargs)

            args = {"config": config_name,
                    "reboot_answer": "y",
                    "reboot_exos": "n"}

            cmd_obj = getattr(api, self.cmd_const.RESET_SYSTEM_TO_CONFIG)(args, **kwargs)

            if not cmd_obj.not_supported:
                cmd_obj = dev.send_command_object(cmd_obj)
                self.logger.log_info("Setting " + device_name + " to load " + config_name + ".")

            if dev.current_agent.type != AgentConstants.TYPE_CONSOLE:
                dev.current_agent.connected = False
                dev.current_agent.logged_in = False
            else:
                dev.current_agent.logged_in = False

            kw_results.append(self._determine_result(dev, cmd_obj, **kwargs))
        return self._keyword_cleanup(kw_results)

    def reboot_network_element_now_and_wait(self, device_names, max_wait, wait_before="1", wait_after_success="1",
                                            **kwargs):
        """
        Keyword Arguments:
        [device_names] - The device(s) the keyword should run against.
        [max_wait] - The maximum amount of time the keyword should wait for the device to reset.
        [wait_before] - How long the keyword should wait before starting to ping the devices IP.
        [wait_after_success] - How long the keyword should wait after successfully pinging the device.

        Reboots a network element and then waits for it to become responsive again.
        """
        device_names = ListUtils.convert_to_list(device_names)

        for device_name in device_names:
            dev, api, _ = self._init_keyword(device_name, self.api_const, **kwargs)

            self.reboot_network_element_now(device_name, log_keyword=False, **kwargs)
            self.ping.wait_until_ip_is_reachable(dev.hostname, max_wait, wait_before, wait_after_success,
                                                 log_keyword=False, **kwargs)

    def reset_network_element_to_factory_defaults(self, device_names, clear_nvram="", **kwargs):
        """
        Keyword Arguments:
        [device_names] - The device(s) the keyword should be run against.
        [clear_nvram] - On EXOS switches pass "all" to clear nvram, stacking, authentication etc.

        Resets a given network element to factory defaults.
        """
        device_names = ListUtils.convert_to_list(device_names)

        kw_results = []
        for device_name in device_names:
            dev, api, _ = self._init_keyword(device_name, self.api_const, wait_for_prompt=False, **kwargs)

            args = {"reboot_answer": "y",
                    "clear_nvram_exos": str(clear_nvram)}

            if dev.oper_sys == self.constants.OS_EXOS:
                dev.wait_for_prompt = False

            cmd_obj = getattr(api, self.cmd_const.RESET_FACTORY_DEFAULT)(args, **kwargs)

            if not cmd_obj.not_supported:
                cmd_obj = dev.send_command_object(cmd_obj)
                self.logger.log_info("Resetting " + device_name + " to factory defaults now.")

            if dev.current_agent.type != AgentConstants.TYPE_CONSOLE:
                dev.current_agent.connected = False
                dev.current_agent.logged_in = False
            else:
                dev.current_agent.logged_in = False

            kw_results.append(self._determine_result(dev, cmd_obj, **kwargs))
        return self._keyword_cleanup(kw_results)

    def login_after_reset(self, device_name, username, password, **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device the keyword should be run against.
        [username]     - The network elements username.
        [password]     - The network elements password.

        This keyword will resend the login credentials for a network element to log back in after resetting.
        """
        args = {"username": username,
                "password": password}

        return self.execute_keyword(device_name, args, self.cmd_const.LOGIN_AFTER_RESET, **kwargs)

    def bypass_initial_setup(self, device_names, **kwargs):
        """
        Keyword Arguments:
        [device_names] - The device(s) the keyword should be run against.

        Bypasses the initial setup screen on EXOS devices, all options are set to default value.
        """
        device_names = ListUtils.convert_to_list(device_names)

        kw_results = []
        for device_name in device_names:
            dev, api, _ = self._init_keyword(device_name, self.constants.API_RESETDEVICE, **kwargs)

            cmd_obj = getattr(api, self.cmd_const.BYPASS_INITIAL_SETUP)(None, **kwargs)

            if not cmd_obj.not_supported:
                cmd_obj = dev.send_command_object(cmd_obj)

            kw_results.append(self._determine_result(dev, cmd_obj, **kwargs))
        return self._keyword_cleanup(kw_results)

    def baseline_testbed(self, config_name, slot="1", timeout="300", interval="10", wait_after_success="5", **kwargs):
        """
        Keyword Arguments:
        [config_name] - The name of the base config that should be loaded
        [slot] - The slot that the config file is located on.
        [timeout] - The maximum amount of time that the keyword should wait per device.
        [interval] - The amount of time to wait before each ping.

        Loads the given config file on all connected network elements.
        """
        self._init_keyword(**kwargs)

        device_list = self.device_collection.get_device_list()
        dut_list = []

        for dut in device_list:
            device = self.device_collection.get_device(dut)
            if isinstance(device, NetworkElement):
                if device.oper_sys == self.constants.OS_EOS:
                    config = "slot" + str(slot) + "/" + config_name + ".cfg"
                else:
                    config = config_name
                self.reboot_network_element_with_config(dut, config, wait_for_prompt=False, **kwargs)
                dut_list.append(dut)
        if dut_list:
            device = self.device_collection.get_device(dut_list[0])
            self.ping.wait_until_ip_is_not_reachable(device.hostname, "30", **kwargs)
            for dut in dut_list:
                device = self.device_collection.get_device(dut)
                self.ping.wait_until_ip_is_reachable(device.hostname, timeout, wait_after_success=wait_after_success,
                                                     interval=interval, **kwargs)
            self.logger.log_info("All DUTs have been reset to base config.")
        else:
            raise FailureException("There are no devices to baseline.")

    def start_network_element_failover(self, device_names, warm=False, **kwargs):
        """
        Keyword Arguments:
        [device_names] - The device(s) the keyword should be run against.

        Runs the device failover operation. (Currently EXOS-only)
        """
        device_names = ListUtils.convert_to_list(device_names)

        kw_results = []
        for device_name in device_names:
            dev, api, _ = self._init_keyword(device_name, self.api_const, wait_for_prompt=False, **kwargs)

            args = {"failover_answer": "y"}

            if warm:
                cmd_obj = getattr(api, self.cmd_const.RUN_FAILOVER_WARM)(args, **kwargs)
            else:
                cmd_obj = getattr(api, self.cmd_const.RUN_FAILOVER)(args, **kwargs)

            if not cmd_obj.not_supported:
                cmd_obj = dev.send_command_object(cmd_obj)
                self.logger.log_info("Starting failover on " + device_name + " now.")

            if dev.current_agent.type != AgentConstants.TYPE_CONSOLE:
                dev.current_agent.connected = False
                dev.current_agent.logged_in = False
            else:
                dev.current_agent.logged_in = False

            kw_results.append(self._determine_result(dev, cmd_obj, **kwargs))
        return self._keyword_cleanup(kw_results)

    def start_network_element_failover_and_wait(self, device_names, max_wait, wait_before="1", wait_after_success="1",
                                                warm=False, reconnect_on_failure=False, reconnect_delay="120",
                                                reconnect_max_wait="", **kwargs):
        """
        Keyword Arguments:
        [device_names] - The device(s) the keyword should run against.
        [max_wait] - The maximum amount of time the keyword should wait for the device to reset.
        [wait_before] - How long the keyword should wait before starting to ping the devices IP.
        [wait_after_success] - How long the keyword should wait after successfully pinging the device.
        [warm] - Toggles the warm failover option, instead of cold.
        [reconnect_on_failure] - Allows closing connection to the device and re-opening when the ping fails.
        [reconnect_delay] - The time to delay before attempting to reconnect after ping failure.
        [reconnect_max_wait] - The max_wait argument for the reconnect keyword call.

        Runs a network element failover and then waits for it to become responsive again.
        """
        device_names = ListUtils.convert_to_list(device_names)

        for device_name in device_names:
            dev, api, _ = self._init_keyword(device_name, self.api_const, **kwargs)

            self.start_network_element_failover(device_name, warm, log_keyword=False, **kwargs)

            if "continue_on_failure" not in kwargs:
                kwargs["continue_on_failure"] = dev.continue_on_failure
            kw_results = self.ping.wait_until_ip_is_reachable(dev.hostname, max_wait, wait_before, wait_after_success,
                                                              log_keyword=False, **kwargs)
            reconnect = False
            for result in kw_results:
                if not result.test_result and reconnect_on_failure:
                    reconnect = True
                    break

            if reconnect:
                self.connect.close_connection_to_network_element(device_name)
                time.sleep(int(reconnect_delay))
                max_connect_wait = "60" if not reconnect_max_wait else reconnect_max_wait
                self.connect.connect_to_network_element(device_name, dev.hostname, dev.username, dev.password,
                                                        dev.connection_method, dev.oper_sys, dev.port, dev.platform,
                                                        dev.version, dev.unit, dev.debug_password, max_connect_wait,
                                                        **kwargs)