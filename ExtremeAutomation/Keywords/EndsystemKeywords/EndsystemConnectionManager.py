import time
from ExtremeAutomation.Library.Utils.NetworkElementUtils import NetworkElementUtils
from ExtremeAutomation.Library.Utils.EndsystemElementUtils import EndsystemElementUtils
from ExtremeAutomation.Library.Device.EndsystemElement.EndsystemElement import EndsystemElement
from ExtremeAutomation.Keywords.BaseClasses.EndsystemKeywordBaseClass import EndsystemKeywordBaseClass


class EndsystemConnectionManager(EndsystemKeywordBaseClass):

    def connect_to_endsystem_element(self, es_elem_name, ip, username, password, connection_method, cli_type,
                                     port=None, device_platform=None, device_version=None, device_unit=None,
                                     max_wait="60", **kwargs):
        """
        Keyword Arguments:
        [net_elem_name]     - A string name for calling the device. Example, "DUT1", "EXOS_1", or "DHCP_Server".
        [ip]                - The IP of the device.
        [username]          - The username needed to log into the device.
        [password]          - The password needed to log into the device.
        [connection_method] - The protocol used to connect to the device. Current options are
                              "telnet", "ssh" and "json".
        [cli_type]          - The type of device that will be connected to. Current options are "EOS", "EXOS",
                              "EXOS-ISW".
        [port]              - The port used to connect to the device. If no port is provided the protocols default will
                              be used.

        This keyword connects to a endsystem element. An exception is thrown if a connection cannot be established.
        """
        device = self.__base_connect_to_end_sys(es_elem_name, ip, username, password, connection_method, cli_type,
                                                port, device_platform, device_version, device_unit, **kwargs)

        self._init_keyword(es_elem_name, **kwargs)

        start_time = time.time()

        while not device.current_agent.logged_in and (time.time() - start_time) < int(max_wait):
            device.connect()

        if not device.current_agent.logged_in:
            raise AttributeError("Unable to establish a connection with end system " + es_elem_name +
                                 " within " + max_wait + " seconds.")

        self._get_platform_variables(es_elem_name)

        return device

    def connect_to_all_endsystem_elements(self, **kwargs):
        """
        This function parses the current robot variables dictionary and connects to all end
        system elements present.
        """
        variables = BuiltIn().get_variables(no_decoration=True)
        end_systems = NetworkElementUtils.get_device_names_from_variables(variables, "endsys")

        for end_system in end_systems:
            es_name = None
            es_ip = None
            es_username = None
            es_password = None
            es_con_method = None
            es_port = None
            es_os = None

            try:
                es_name = variables[end_system]["name"]
                es_ip = variables[end_system]["ip"]
                es_username = variables[end_system]["username"]
                es_password = variables[end_system]["password"]
                es_con_method = variables[end_system]["connection_method"]
                es_port = variables[end_system]["port"]
                es_os = variables[end_system]["cli_type"]
            except KeyError:
                if es_ip is None:
                    self.logger.log_error("${" + end_system + ".ip} variable not present in testbed " +
                                          "resource file.")
                if es_username is None:
                    self.logger.log_error("${" + end_system + ".username} variable not present in testbed " +
                                          "resource file.")
                if es_password is None:
                    self.logger.log_error("${" + end_system + ".password} variable not present in testbed " +
                                          "resource file.")
                if es_con_method is None:
                    self.logger.log_error("${" + end_system + ".connection_method} variable not present in testbed " +
                                          "resource file.")
                if es_os is None:
                    self.logger.log_error("${" + end_system + ".os} variable not present in testbed resource file.")

            es_platform = variables[end_system]["platform"] if "platform" in variables[end_system] else None
            es_version = variables[end_system]["version"] if "version" in variables[end_system] else None
            es_unit = variables[end_system]["unit"] if "unit" in variables[end_system] else None

            if es_name is not None:
                self.connect_to_endsystem_element(es_name, es_ip, es_username, es_password, es_con_method, es_os,
                                                  es_port, es_platform, es_version, es_unit, **kwargs)

    def close_connection_to_endsystem_element(self, es_elem_nam, **kwargs):
        """
        Keyword Arguments:
        [net_elem_name] - The name of the network element that robot should disconnect from.

        Closes the connection to a given network element.
        """
        dev, _, _ = self._init_keyword(es_elem_nam, **kwargs)
        dev.disconnect()
        self.device_collection.remove_device(es_elem_nam)

    def close_connection_to_all_endsystem_elements(self, **kwargs):
        """
        Closes the connection to all end system elements present in the extended environment file.
        """
        variables = BuiltIn().get_variables(no_decoration=True)
        end_systems = NetworkElementUtils.get_device_names_from_variables(variables, "endsys")

        for end_system in end_systems:
            es_name = variables[end_system]["name"]
            self.close_connection_to_endsystem_element(es_name, **kwargs)

    def change_connection_agent(self, es_elem_name, connection_method, connection_port=None, **kwargs):
        """
        Keyword Arguments:
        [net_elem_name]     - The network element whose connection agent should be changed.
        [connection_method] - The protocol used to connect to the device. Current options are
                              "telnet", "ssh" and "json".
        [connection_port]   - The port used to connect to the device. If no port is provided the protocols
                              default will be used.

        This keyword changes the connection_method and port to the given method.
        """
        dev, _, _ = self._init_keyword(es_elem_name, **kwargs)

        ip = dev.hostname
        os = dev.oper_sys
        unit = dev.unit
        version = dev.version
        username = dev.username
        password = dev.password
        platform = dev.platform

        self.close_connection_to_endsystem_element(es_elem_name, log_keyword=False)
        self.connect_to_endsystem_element(es_elem_name, ip, username, password, connection_method, os,
                                          connection_port, platform, version, unit, log_keyword=False)

    def __base_connect_to_end_sys(self, name, ip, user, password, connection_method, cli_type, port, platform,
                                  version, unit, **kwargs):
        device_info = EndsystemElementUtils.get_device_info(cli_type, platform, version, unit)
        connection_method, port = EndsystemElementUtils.get_connection_method(connection_method, port)

        device = EndsystemElement(device_info["device_os"], device_info["device_platform"],
                                  device_info["device_unit"], device_info["device_version"])

        EndsystemElementUtils.update_device_class(device, cli_type, platform, version, unit)
        device.hostname = ip
        device.port = port
        device.connection_method = connection_method
        device.username = user
        device.password = password
        device.login_prompt = device_info["login_prompt"]
        device.pass_prompt = device_info["pass_prompt"]
        device.main_prompt = device_info["main_prompt"]
        device.name = name
        device.eol = device_info["end_of_line"]

        self.device_collection.add_device(name, device)
        kwargs.update(device_info)
        self.set_agent_kwargs(device, **kwargs)

        return device

    @staticmethod
    def add_agent_kwarg(device, kwarg_key, kwargs):
        """
        Checks to see if <kwarg_key> is present in <kwargs>. If it is, the value will be added to the
        device's agent dict with key <kwarg_key> and the retrieved value. If no value is found it is ignored.
        """
        kwarg_val = kwargs.get(kwarg_key, None)

        if kwarg_val is not None:
            device.agent_kwargs[kwarg_key] = kwarg_val

    def set_agent_kwargs(self, device, **kwargs):
        """
        This function is used for setting kwargs on a per agent basis. It is up to the agent
        to parse this dictionary for any values it needs.
        """
        # Set slow login kwarg, only used for Windows telnet currently.
        if device.connection_method == self.agent_constants.TYPE_TELNET:
            self.add_agent_kwarg(device, "slow_login", kwargs)

        # Args for any REST or REST-like agent.
        self.add_agent_kwarg(device, "verify_cert", kwargs)
        self.add_agent_kwarg(device, "auth_mode", kwargs)
        self.add_agent_kwarg(device, "headers", kwargs)
        self.add_agent_kwarg(device, "oauth", kwargs)
