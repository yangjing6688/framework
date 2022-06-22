import time
import socket
from ExtremeAutomation.Library.Utils.RobotUtils import RobotUtils
from ExtremeAutomation.Keywords.FailureException import FailureException
from ExtremeAutomation.Library.Utils.NetworkElementUtils import NetworkElementUtils
from ExtremeAutomation.Library.Device.NetworkElement.NetworkElement import NetworkElement
from ExtremeAutomation.Library.Device.NetworkElement.NetelemLearning.SystemBuilder import Builder
from ExtremeAutomation.Keywords.NetworkElementKeywords.Utils.NetworkElementSnmpUtils import NetworkElementSnmpUtils
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import \
    NetworkElementKeywordBaseClass

import inspect
import logging
import sys
import copy


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logging.basicConfig(format='[%(asctime)s] %(levelname)s: [%(filename)s %(name)s %(funcName)s (Line#%(lineno)d)]: %(message)s')

class NetworkElementConnectionManager(NetworkElementKeywordBaseClass):
    def connect_to_network_element(self, net_elem_name, ip, username, password, connection_method, device_os, port=None,
                                   device_platform=None, device_version=None, device_unit=None, debug_password=None,
                                   max_wait="60", session_key="default", **kwargs):
        """
        Keyword Arguments:
        [net_elem_name] - A string name for calling the device. Example, "DUT1", "EXOS_1", or "DHCP_Server".
        [ip] - The IP of the device.
        [username] - The username needed to log into the device.
        [password] - The password needed to log into the device.
        [connection_method] - The protocol used to connect to the device. Current options are
                              "telnet", "ssh" and "json".
        [device_os] - The OS of device that will be connected to.
        [port] - The port used to connect to the device. If no port is provided the protocols default will be used.
        [device_platform] - The platform of the device being connected to.
        [device_version] - The version of FW that the device being connected to is running.
        [device_unit] - This unit of the device being connected to.
        [session_key] - Name of session only needed for multiple connections to same netelem
        This keyword connects to a network element. An exception is thrown if a connection cannot be established.
        """
        this_function_name   = inspect.currentframe().f_code.co_name
        callingfunction_name = inspect.currentframe().f_back.f_code.co_name
        callingfile_name = inspect.currentframe().f_back.f_code.co_filename
        logger.debug("[+]Entering function     : %s()", this_function_name)
        logger.debug("[+]Called from function  : %s()", callingfunction_name)
        logger.debug("[+]Called from file      : %s()", callingfile_name)

        build_system = kwargs.get("build_system", False)
        # Alter ip/port to console_ip console_port if required
        # The default L3 connection is netelem# ip and port.  The next method only returns a value if
        #     console or slot
        cons_ip, cons_port = NetworkElementUtils.get_console_ip_port(None, net_elem_name, connection_method)
        if cons_ip:
            ip = cons_ip
            port = cons_port

        self.__base_connect_to_network_element(net_elem_name, ip, username, password, connection_method, device_os,
                                               port, device_platform, device_version, device_unit, debug_password,
                                               **kwargs)

        dev, _, _ = self._init_keyword(net_elem_name, **kwargs)
        expect_error = self.get_kwarg_bool(kwargs, "expect_error", False)
        dev.max_connection_retries = 0 if expect_error else 3
        dev.connection_method = connection_method

        start_time = time.time()

        dev.track_named_agent(session_key, connection_method, ip, port)

        i = 1
        while not dev.current_agent.logged_in and (time.time() - start_time) < int(max_wait) and not expect_error:
            try:
                dev.connect()
            except socket.error:
                self.logger.log_debug("Agent connection attempt #" + str(i) + " failed.")
            time.sleep(5)
            i += 1

        if not dev.current_agent.logged_in:
            if not expect_error:
                raise FailureException("Unable to establish a connection with network element " + net_elem_name +
                                       " within " + max_wait + " seconds.")
            else:
                self.logger.log_info("Device connection and/or login was unsuccessful. Error was expected.")
        else:
            if expect_error:
                raise FailureException("Connection was established while expecting an error.")
            self._get_platform_variables(net_elem_name)

            if build_system:
                self.build_system(net_elem_name)

        return dev

    def connect_to_all_network_elements(self, **kwargs):
        """
        Keyword Arguments:
        None

        Searches the testbed environment file for network elements and connects to each.
        """
        netelem_dict = self.build_dict_of_netelems(**kwargs)
        for netelem_name in netelem_dict:
            if not netelem_dict[netelem_name]["skip_connect"]:
                netelem_ip = netelem_dict[netelem_name]["netelem_ip"]
                netelem_user = netelem_dict[netelem_name]["netelem_user"]
                netelem_pass = netelem_dict[netelem_name]["netelem_pass"]
                netelem_con_method = netelem_dict[netelem_name]["netelem_con_method"]
                netelem_cli_type = netelem_dict[netelem_name]["netelem_cli_type"]
                netelem_port = netelem_dict[netelem_name]["netelem_port"]
                netelem_platform = netelem_dict[netelem_name]["netelem_platform"]
                netelem_version = netelem_dict[netelem_name]["netelem_version"]
                netelem_unit = netelem_dict[netelem_name]["netelem_unit"]
                netelem_console_ip = netelem_dict[netelem_name]["netelem_console_ip"]
                netelem_console_port = netelem_dict[netelem_name]["netelem_console_port"]
                snmp_info = netelem_dict[netelem_name]["snmp_info"]
                auth_mode = netelem_dict[netelem_name]["auth_mode"]
                verify_cert = netelem_dict[netelem_name]["verify_cert"]

                self.connect_to_network_element(netelem_name, netelem_ip, netelem_user, netelem_pass,
                                                netelem_con_method, netelem_cli_type, netelem_port, netelem_platform,
                                                netelem_version, netelem_unit, netelem_console_ip=netelem_console_ip,
                                                netelem_console_port=netelem_console_port, snmp_info=snmp_info,
                                                auth_mode=auth_mode, verify_cert=verify_cert, **kwargs)

    def connect_to_network_element_name(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The name of the netelem in the yaml file.

        Searches the testbed environment file for network elements and connects to each.
        """
        netelem_dict = self.build_dict_of_netelems(**kwargs)

        if device_name in netelem_dict:
            netelem_ip = netelem_dict[device_name]["netelem_ip"]
            netelem_user = netelem_dict[device_name]["netelem_user"]
            netelem_pass = netelem_dict[device_name]["netelem_pass"]
            netelem_con_method = netelem_dict[device_name]["netelem_con_method"]
            netelem_cli_type = netelem_dict[device_name]["netelem_cli_type"]
            netelem_port = netelem_dict[device_name]["netelem_port"]
            netelem_platform = netelem_dict[device_name]["netelem_platform"]
            netelem_version = netelem_dict[device_name]["netelem_version"]
            netelem_console_ip = netelem_dict[device_name]["netelem_console_ip"]
            netelem_console_port = netelem_dict[device_name]["netelem_console_port"]
            netelem_unit = netelem_dict[device_name]["netelem_unit"]
            snmp_info = netelem_dict[device_name]["snmp_info"]
            auth_mode = netelem_dict[device_name]["auth_mode"]
            verify_cert = netelem_dict[device_name]["verify_cert"]

            self.connect_to_network_element(device_name, netelem_ip, netelem_user, netelem_pass,
                                            netelem_con_method, netelem_os, netelem_port, netelem_platform,
                                            netelem_version, netelem_unit, netelem_console_ip=netelem_console_ip,
                                            netelem_console_port=netelem_console_port, snmp_info=snmp_info,
                                            auth_mode=auth_mode, verify_cert=verify_cert, **kwargs)

    def connect_to_network_element_number(self, netelem_id, **kwargs):
        """
        Keyword Arguments:
        [netelem_id] - The dictionary key for the netelem in the yaml file.
                       (Ex: netelem1)

        Searches the testbed environment file for network elements and connects to each.
        """
        netelem_dict = self.build_dict_of_netelems(**kwargs)
        for netelem_name in netelem_dict:
            if netelem_dict[netelem_name]["netelem_id"] == netelem_id:
                netelem_ip = netelem_dict[netelem_name]["netelem_ip"]
                netelem_user = netelem_dict[netelem_name]["netelem_user"]
                netelem_pass = netelem_dict[netelem_name]["netelem_pass"]
                netelem_con_method = netelem_dict[netelem_name]["netelem_con_method"]
                netelem_cli_type = netelem_dict[netelem_name]["netelem_cli_type"]
                netelem_port = netelem_dict[netelem_name]["netelem_port"]
                netelem_platform = netelem_dict[netelem_name]["netelem_platform"]
                netelem_version = netelem_dict[netelem_name]["netelem_version"]
                netelem_unit = netelem_dict[netelem_name]["netelem_unit"]
                netelem_console_ip = netelem_dict[netelem_name]["netelem_console_ip"]
                netelem_console_port = netelem_dict[netelem_name]["netelem_console_port"]
                snmp_info = netelem_dict[netelem_name]["snmp_info"]
                auth_mode = netelem_dict[netelem_name]["auth_mode"]
                verify_cert = netelem_dict[netelem_name]["verify_cert"]

                self.connect_to_network_element(netelem_name, netelem_ip, netelem_user, netelem_pass,
                                                netelem_con_method, netelem_os, netelem_port, netelem_platform,
                                                netelem_version, netelem_unit, netelem_console_ip=netelem_console_ip,
                                                netelem_console_port=netelem_console_port, snmp_info=snmp_info,
                                                auth_mode=auth_mode, verify_cert=verify_cert, **kwargs)
                break

    def close_connection_to_network_element(self, net_elem_nam, **kwargs):
        """
        Keyword Arguments:
        [net_elem_name] - The name of the network element that robot should disconnect from.

        Closes the connection to a given network element.
        """
        dev, _, _ = self._init_keyword(net_elem_nam, check_initial_prompt=False, **kwargs)
        dev.disconnect()
        if len(dev.agent_track) > 0:
            killAgentDict = {}   # temp needed because disconnect modifies the looping dictionary.
            for sess_agent in dev.agent_track.keys():
                for sess_key in dev.agent_track[sess_agent].keys():
                    dev.logger.log_debug(f"Netelem Agent Session disconnect {sess_agent} {sess_key}...")
                    if dev.agent_track[sess_agent][sess_key]['agent']:
                        killAgentDict[sess_key] = {}
                        killAgentDict[sess_key]['connection_method'] = sess_agent
                        killAgentDict[sess_key]['hostname'] = dev.agent_track[sess_agent][sess_key]['hostname']
                        killAgentDict[sess_key]['port'] = dev.agent_track[sess_agent][sess_key]['port']
                        killAgentDict[sess_key]['current_agent'] = dev.agent_track[sess_agent][sess_key]['agent']
            for skey in killAgentDict.keys():
                dev.session_key = skey
                dev.connection_method = killAgentDict[skey]['connection_method']
                dev.hostname = killAgentDict[skey]['hostname']
                dev.port = killAgentDict[skey]['port']
                dev.current_agent = killAgentDict[skey]['current_agent']
                try:
                    dev.disconnect()
                except:
                    pass
        self.device_collection.remove_device(net_elem_nam)

    def close_connection_to_all_network_elements(self, **kwargs):
        """
        Keyword Arguments:
        None

        Closes the connection all network elements present in the test bed resource file.
        """
        devices = self.device_collection.get_device_list()
        netelem_list = []
        for device in devices:
            device_obj = self.device_collection.get_device(device)
            if isinstance(device_obj, NetworkElement):
                netelem_list.append(device_obj.name)

        for netelem in netelem_list:
            self.close_connection_to_network_element(netelem, **kwargs)

    #
    # Add  or change connections to a network element
    #
    def netelem_agent_connection_modify(self, net_elem_name, connection_method, session_key=None, connection_port=None,  **kwargs):
        """
        Keyword Arguments:
        [net_elem_name] - The network element whose connection agent should be changed.
        [connection_method] - The protocol used to connect to the device. Current options are
                              "telnet", "ssh", snmp, and "json"
        [session_key]  -  "default" session_key string is used on the first connect to netelem.  When adding a new session
                          use a new session_key.  To return to an existing open session.  Calling that conn_method/string
                          pair, will return to the already open session.
        [connection_port] - The port used to connect to the device. If no port is provided the protocols
                            default will be used.
        """

        this_function_name   = inspect.currentframe().f_code.co_name
        callingfunction_name = inspect.currentframe().f_back.f_code.co_name
        callingfile_name = inspect.currentframe().f_back.f_code.co_filename
        logger.debug("[+]Entering function     : %s()", this_function_name)
        logger.debug("[+]Called from function  : %s()", callingfunction_name)
        logger.debug("[+]Called from file      : %s()", callingfile_name)

        dev, _, _ = self._init_keyword(net_elem_name, **kwargs)
        if kwargs.get("snmp_info", False):
            snmp_info = kwargs["snmp_info"]
        else:
            try:
                variables = RobotUtils.get_variables(no_decoration=True)
            except Exception as e:
                raise e

            if variables is None:
                snmp_info = None
            else:
                netelem_num = NetworkElementUtils.get_device_number(variables, net_elem_name)
                self.add_agent_kwarg(dev, "verify_cert", kwargs)
                self.add_agent_kwarg(dev, "auth_mode", kwargs)
                self.add_agent_kwarg(dev, "headers", kwargs)
                self.add_agent_kwarg(dev, "oauth", kwargs)
                snmp_info = NetworkElementUtils.get_snmp_info(variables, netelem_num)

        ip, port = NetworkElementUtils.get_console_ip_port(dev, net_elem_name, connection_method, True)
        if connection_port:
            port = connection_port
            dev.port = port
        connection_method, port = NetworkElementUtils.get_connection_method(connection_method, port)
        if session_key:
            self.session_key = session_key
            dev.set_and_connect_named_agent(self.session_key, connection_method, ip, port)
        else:
            logger.debug("[!]SessionKey should be set on initial connect")
            self.session_key = 'default'
            dev.set_and_connect_named_agent('default', connection_method, ip, port)

    def __base_connect_to_network_element(self, net_elem_name, ip, username, password, connection_method, device_os,
                                          port, device_platform, device_version, device_unit, debug_password, **kwargs):


        this_function_name   = inspect.currentframe().f_code.co_name
        callingfunction_name = inspect.currentframe().f_back.f_code.co_name
        callingfile_name = inspect.currentframe().f_back.f_code.co_filename
        logger.debug("[+]Entering function     : %s()", this_function_name)
        logger.debug("[+]Called from function  : %s()", callingfunction_name)
        logger.debug("[+]Called from file      : %s()", callingfile_name)

        # Get os, platform, and prompts based on the device type.
        device_info = NetworkElementUtils.get_device_info(device_os, device_platform, device_version, device_unit)

        # Get the connection method constant and port based on which connection method the user passed.
        # Use the port the user passed, if no port was provided use the protocol default.
        connection_method, port = NetworkElementUtils.get_connection_method(connection_method, port)

        # Set the device attributes and add the object to the DeviceCollectionManager.
        device = NetworkElement(device_info["device_os"], device_info["device_platform"],
                                device_info["device_unit"], device_info["device_version"])

        device.hostname = ip
        device.port = port
        device.connection_method = connection_method
        device.username = username
        device.password = password
        device.login_prompt = device_info["login_prompt"]
        device.pass_prompt = device_info["pass_prompt"]
        device.main_prompt = device_info["main_prompt"]
        device.name = net_elem_name
        device.debug_password = debug_password
        device.eol = device_info.get("end_of_line", None)
        device.continue_on_failure = kwargs.get('continue_on_failure', None)
        self.device_collection.add_device_with_method(net_elem_name, device, connection_method)
        self.set_agent_kwargs(device, **kwargs)

    def set_agent_kwargs(self, device, **kwargs):
        """
        Keyword Arguments:
        [device] - The Network Element for which to set agent kwargs.

        This function adds any needed kwargs to the device's agent kwarg dictionary.
        """
        # Args for the SNMP agent.
        if kwargs.get("snmp_info", None) is not None:
            snmp_info = kwargs["snmp_info"]
            self.add_agent_kwarg(device, "snmp_version", snmp_info)
            self.add_agent_kwarg(device, "snmp_community_name", snmp_info)
            self.add_agent_kwarg(device, "snmp_user_name", snmp_info)
            self.add_agent_kwarg(device, "snmp_auth_protocol", snmp_info)
            self.add_agent_kwarg(device, "snmp_auth_password", snmp_info)
            self.add_agent_kwarg(device, "snmp_privacy_protocol", snmp_info)
            self.add_agent_kwarg(device, "snmp_privacy_password", snmp_info)
            if device.connection_method == self.agent_constants.TYPE_SNMP:
                NetworkElementSnmpUtils().create_and_store_interface_index_name_dictionaries(device.name)
                NetworkElementSnmpUtils().create_and_store_interface_index_dot1d_port_dictionaries(device.name)

        # Args for any REST or REST-like agent.
        self.add_agent_kwarg(device, "verify_cert", kwargs)
        self.add_agent_kwarg(device, "auth_mode", kwargs)
        self.add_agent_kwarg(device, "headers", kwargs)
        self.add_agent_kwarg(device, "oauth", kwargs)

    @staticmethod
    def build_system(net_elem_name):
        """
        This function will create a python representation of a given network element. After
        the system is built the robot variables will be updated with the information
        provided from the system.
        """
        learned_system = Builder(net_elem_name).build()
        if learned_system is not None:
            RobotUtils.update_variables(net_elem_name, learned_system)

    def build_dict_of_netelems(self, **kwargs):
        try:
            variables = RobotUtils.get_variables(no_decoration=True)
        except Exception as e:
                raise e

        netelems = NetworkElementUtils.get_device_names_from_variables(variables, "netelem")
        # We consider AP as an netelem
        ap = NetworkElementUtils.get_device_names_from_variables(variables, "ap")
        # We consider aerohive_sw as an netelem
        aerohive_sw = NetworkElementUtils.get_device_names_from_variables(variables, "aerohive_sw")
        # We consider router as an netelem
        router = NetworkElementUtils.get_device_names_from_variables(variables, "router")

        # Add the results together
        netelems.extend(ap)
        netelems.extend(aerohive_sw)
        netelems.extend(router)
        netelem_dict = {}
        for netelem in netelems:
            netelem_id = netelem
            netelem_name = None
            netelem_ip = None
            netelem_user = None
            netelem_pass = None
            netelem_con_method = None
            netelem_port = None
            netelem_os = None
            session_keylist = []

            try:
                netelem_name = variables[netelem]["name"]
                netelem_ip = variables[netelem]["ip"]
                netelem_user = variables[netelem]["username"]
                netelem_pass = variables[netelem]["password"]
                netelem_con_method = variables[netelem]["connection_method"]
                netelem_cli_type = variables[netelem]["cli_type"]
                netelem_port = variables[netelem]["port"]
            except KeyError:
                if netelem_name is None:
                    self.logger.log_error("${" + netelem + ".name} variable not present in testbed " +
                                          "resource file.")
                if netelem_ip is None:
                    self.logger.log_error("${" + netelem + ".ip} variable not present in testbed " +
                                          "resource file.")
                if netelem_user is None:
                    self.logger.log_error("${" + netelem + ".username} variable not present in testbed " +
                                          "resource file.")
                if netelem_pass is None:
                    self.logger.log_error("${" + netelem + ".password} variable not present in testbed " +
                                          "resource file.")
                if netelem_con_method is None:
                    self.logger.log_error("${" + netelem + ".connection_method} variable not present in testbed " +
                                          "resource file.")
                if netelem_cli_type is None:
                    self.logger.log_error("${" + netelem + ".cli_type} variable not present in testbed resource file.")

            netelem_console_ip = variables[netelem]["console_ip"] if "console_ip" in variables[netelem] else None
            netelem_console_port = variables[netelem]["console_port"] if "console_port" in variables[netelem] else None
            netelem_platform = variables[netelem]["platform"] if "platform" in variables[netelem] else None
            netelem_version = variables[netelem]["version"] if "version" in variables[netelem] else None
            netelem_unit = variables[netelem]["unit"] if "unit" in variables[netelem] else None
            snmp_info = NetworkElementUtils.get_snmp_info(variables, netelem)
            if netelem_con_method.lower() == "snmp" and snmp_info is None:
                self.logger.log_error("SNMP info must be provided in the YAML environment file.")
            auth_mode = variables[netelem]["auth_mode"] if "auth_mode" in variables[netelem] else None
            if netelem_con_method.lower() == "rest" and auth_mode is None:
                self.logger.log_error("REST auth_mode was not provided. Using default AUTH_NONE.")
            verify_cert = variables[netelem]["verify_cert"] if "verify_cert" in variables[netelem] else None

            netelem_stack = 1 if "stack" in variables[netelem] else None
            slot1_console_ip = None
            slot1_console_port = None
            slot2_console_ip = None
            slot2_console_port = None
            if netelem_stack:
                for k, v in variables[netelem]["stack"].items():
                    if k == 'slot1':
                        #session_keylist.append('slot1')
                        slot1_console_ip = v["console_ip"] if "console_ip" in v else None
                        slot1_console_port = v["console_port"] if "console_port" in v else None
                    if k == 'slot2':
                        session_keylist.append('slot2')
                        slot2_console_ip = v["console_ip"] if "console_ip" in v else None
                        slot2_console_port = v["console_port"] if "console_port" in v else None

            netelem_vpex = 1 if "vpex" in variables[netelem] else None

            # Checking for 'skip_connect' key in the netelem dict
            skip_connect = variables[netelem].get("skip_connect", False)

            netelem_dict[netelem_name] = {"netelem_name": netelem_name,
                                          "netelem_ip": netelem_ip,
                                          "netelem_user": netelem_user,
                                          "netelem_pass": netelem_pass,
                                          "netelem_con_method": netelem_con_method,
                                          "netelem_port": netelem_port,
                                          "netelem_cli_type": netelem_cli_type,
                                          "netelem_platform": netelem_platform,
                                          "netelem_version": netelem_version,
                                          "netelem_unit": netelem_unit,
                                          "netelem_console_ip": netelem_console_ip,
                                          "netelem_console_port": netelem_console_port,
                                          "snmp_info": snmp_info,
                                          "auth_mode": auth_mode,
                                          "verify_cert": verify_cert,
                                          "netelem_id": netelem_id,
                                          "netelem_stack": netelem_stack,
                                          "netelem_slot1_console_ip": slot1_console_ip,
                                          "netelem_slot1_console_port": slot1_console_port,
                                          "netelem_slot2_console_ip": slot2_console_ip,
                                          "netelem_slot2_console_port": slot2_console_port,
                                          "netelem_session_keylist": session_keylist,
                                          "netelem_vpex": netelem_vpex,
                                          "skip_connect": skip_connect}

        return netelem_dict
    

