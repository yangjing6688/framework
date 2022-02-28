import time
from ExtremeAutomation.Library.Utils.NetworkElementUtils import NetworkElementUtils
from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.JetsDevice import JetsDevice
from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.IxiaDevice import IxiaDevice
from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.IxLoadDevice import IxLoadDevice
from ExtremeAutomation.Library.Device.TrafficGeneration.Spirent.SpirentDevice import SpirentDevice
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.OstinatoDevice import OstinatoDevice
from ExtremeAutomation.Library.Device.TrafficGeneration.TrafficGeneratingDevice import TrafficGeneratingDevice
from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenConstants import TrafficGenConstants
from ExtremeAutomation.Keywords.BaseClasses.TrafficKeywordBaseClass import TrafficKeywordBaseClass
from ExtremeAutomation.Library.Device.Common.CommandObjects.CommandObjectConstants import CommandObjectConstants
from ExtremeAutomation.Library.Utils.RobotUtils import RobotUtils


class TrafficGeneratorConnectionManager(TrafficKeywordBaseClass):

    def connect_to_traffic_generator(self, traffic_gen_name, vendor, chassis_ip, vm_ip=None, username=None,
                                     connection_port=None, max_wait="240", password=None, **kwargs):
        """
        Keyword Arguments:
        [traffic_gen_name] - The string name of the chassis.
        [vendor] - The vendor of the chassis being connected to. Current options are "ixia", "spirent", and "ostinato".
        [chassis_ip] - The IP address of the traffic generator chassis.
        [vm_ip] - IP of the server running HLTAPI, TCL server, and TPB socket listener.
        [username] - Username to take ownership of ports under.
        [connection_port] - The port the Ixia socket listener is running on.
        [max_wait] - How long the keyword should wait for a successful connection.

        Connects to a single traffic generator.
        """
        self.__base_connect_to_traffic_generator(traffic_gen_name, vendor, chassis_ip, vm_ip, username, connection_port,
                                                 password)
        self._init_keyword(traffic_gen_name, **kwargs)
        self.__connect_and_wait(traffic_gen_name, max_wait)

    def connect_to_traffic_generators(self, traffic_gen_dicts, max_wait="30", **kwargs):
        """
        Keyword Arguments:
        [traffic_gen_dicts] - This must be a list of traffic generator dictionaries. The format of
                              the traffic generator dictionary is as follows.
        [max_wait] - How long the keyword should wait for a successful connection to each traffic generator.

        Traffic Generator Dictionary Format:
        {traffic_gen_name: <name>,
         vendor:           <vendor>,
         chassis_ip:       <ip>,
         vm_ip:            <ip>*,
         username:         <username>*,
         connection_port:  <port>*}

        * Means that the key is optional.

        Connects to each of the traffic generators present in the list.
        """
        self._init_keyword(**kwargs)

        for tgen_dict in traffic_gen_dicts:
            tgen_name = tgen_dict["traffic_gen_name"]
            vendor = tgen_dict["vendor"]
            chassis_ip = tgen_dict["chassis_ip"]

            try:
                vm_ip = tgen_dict["vm_ip"]
            except KeyError:
                vm_ip = None

            try:
                username = tgen_dict["username"]
            except KeyError:
                username = None

            try:
                port = tgen_dict["connection_port"]
            except KeyError:
                port = None

            self.__base_connect_to_traffic_generator(tgen_name, vendor, chassis_ip, vm_ip, username, port)
            self._init_keyword(tgen_name, log_keyword=False, **kwargs)
            self.__connect_and_wait(tgen_name, max_wait)

    def connect_to_traffic_generator_name(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The name of the Traffic Generator in the yaml file.

        Searches the testbed environment file for traffic generators and connects to each.
        """
        tgen_dict = self.build_dict_of_tgens(**kwargs)

        if device_name in tgen_dict:
            tgen_vendor = tgen_dict[device_name]["tgen_vendor"]
            tgen_chassis_ip = tgen_dict[device_name]["tgen_chassis_ip"]
            tgen_vm_ip = tgen_dict[device_name]["tgen_vm_ip"]
            tgen_user = tgen_dict[device_name]["tgen_user"]
            tgen_pass = tgen_dict[device_name]["tgen_pass"]
            tgen_port = tgen_dict[device_name]["tgen_port"]
            tgen_max_wait = tgen_dict[device_name]["tgen_max_wait"]
            jets_dir = tgen_dict[device_name]["jets_dir"]
            view_tag = tgen_dict[device_name]["view_tag"]

            if tgen_vendor.lower() == "jets":
                self.connect_to_traffic_generator(device_name, tgen_vendor, tgen_chassis_ip, tgen_vm_ip, tgen_user,
                                                  tgen_port, tgen_max_wait, tgen_pass, jets_dir=jets_dir,
                                                  view_tag=view_tag, **kwargs)
            else:
                self.connect_to_traffic_generator(device_name, tgen_vendor, tgen_chassis_ip, tgen_vm_ip, tgen_user,
                                                  tgen_port, tgen_max_wait, tgen_pass, **kwargs)

    def connect_to_traffic_generator_number(self, tgen_id, **kwargs):
        """
        Keyword Arguments:
        [tgen_id] - The dictionary key for the Traffic Generator in the yaml file.
                    (Ex: tgen1)

        Searches the testbed environment file for traffic generators and connects to each.
        """
        tgen_dict = self.build_dict_of_tgens(**kwargs)
        for tgen_name in tgen_dict:
            if tgen_dict[tgen_name]["tgen_id"] == tgen_id:
                tgen_vendor = tgen_dict[tgen_name]["tgen_vendor"]
                tgen_chassis_ip = tgen_dict[tgen_name]["tgen_chassis_ip"]
                tgen_vm_ip = tgen_dict[tgen_name]["tgen_vm_ip"]
                tgen_user = tgen_dict[tgen_name]["tgen_user"]
                tgen_pass = tgen_dict[tgen_name]["tgen_pass"]
                tgen_port = tgen_dict[tgen_name]["tgen_port"]
                tgen_max_wait = tgen_dict[tgen_name]["tgen_max_wait"]
                jets_dir = tgen_dict[tgen_name]["jets_dir"]
                view_tag = tgen_dict[tgen_name]["view_tag"]

                if tgen_vendor.lower() == "jets":
                    self.connect_to_traffic_generator(tgen_name, tgen_vendor, tgen_chassis_ip, tgen_vm_ip, tgen_user,
                                                      tgen_port, tgen_max_wait, tgen_pass, jets_dir=jets_dir,
                                                      view_tag=view_tag, **kwargs)
                else:
                    self.connect_to_traffic_generator(tgen_name, tgen_vendor, tgen_chassis_ip, tgen_vm_ip, tgen_user,
                                                      tgen_port, tgen_max_wait, tgen_pass, **kwargs)
                break

    def connect_to_all_traffic_generators(self, max_wait="30", **kwargs):
        """
        Keyword Arguments:
        [max_wait] - How long the keyword should wait for a successful connection to each traffic generator.

        Connects to all traffic generators present in the variables of a robot test case.
        """
        tgen_dict = self.build_dict_of_tgens(**kwargs)

        for device_name in tgen_dict:
            if not tgen_dict[device_name]["skip_connect"]:
                tgen_vendor = tgen_dict[device_name]["tgen_vendor"]
                tgen_chassis_ip = tgen_dict[device_name]["tgen_chassis_ip"]
                tgen_vm_ip = tgen_dict[device_name]["tgen_vm_ip"]
                tgen_user = tgen_dict[device_name]["tgen_user"]
                tgen_pass = tgen_dict[device_name]["tgen_pass"]
                tgen_port = tgen_dict[device_name]["tgen_port"]
                tgen_max_wait = tgen_dict[device_name]["tgen_max_wait"]
                jets_dir = tgen_dict[device_name]["jets_dir"]
                view_tag = tgen_dict[device_name]["view_tag"]

                if tgen_vendor.lower() == "jets":
                    self.connect_to_traffic_generator(device_name, tgen_vendor, tgen_chassis_ip, tgen_vm_ip, tgen_user,
                                                      tgen_port, tgen_max_wait, tgen_pass, jets_dir=jets_dir,
                                                      view_tag=view_tag, **kwargs)
                else:
                    self.connect_to_traffic_generator(device_name, tgen_vendor, tgen_chassis_ip, tgen_vm_ip, tgen_user,
                                                      tgen_port, tgen_max_wait, tgen_pass, **kwargs)

    def close_connection_to_traffic_generator(self, traffic_gen_name, **kwargs):
        """
        Keyword Arguments:
        [traffic_gen_name] - The name of the traffic generator that should be disconnected from.

        Closes the connection to a given traffic generator.
        """
        self._init_keyword(traffic_gen_name, **kwargs)

        self.traffic_gen.disconnect()
        self.device_collection.remove_device(traffic_gen_name)

    def close_connection_to_traffic_generators(self, traffic_gen_dicts, **kwargs):
        """
        Keyword Arguments:
        [traffic_gen_dicts] - This must be a list of traffic generator dictionaries. The format of
                              the traffic generator dictionary is as follows.

        Traffic Generator Dictionary Format:
        {traffic_gen_name: <name>,
         vendor:           <vendor>,
         chassis_ip:       <ip>,
         vm_ip:            <ip>*,
         username:         <username>*,
         connection_port:  <port>*}

        * Means that the key is optional.

        Disconnects to all traffic generators present in the traffic_gen_dicts list.
        """
        self._init_keyword(**kwargs)

        for tgen_dict in traffic_gen_dicts:
            self._init_keyword(tgen_dict["traffic_gen_name"], log_keyword=False, **kwargs)
            self.traffic_gen.disconnect()
            self.device_collection.remove_device(tgen_dict["traffic_gen_name"])

    def close_connection_to_all_traffic_generators(self, **kwargs):
        """
        Keyword Arguments:

        Disconnects from all traffic generators currently connected.
        """
        devices = self.device_collection.get_device_list()
        tgen_list = []
        for device in devices:
            device_obj = self.device_collection.get_device(device)
            if isinstance(device_obj, TrafficGeneratingDevice):
                tgen_list.append(device_obj.name)

        for tgen in tgen_list:
            self.close_connection_to_traffic_generator(tgen, **kwargs)

    def enable_traffic_generator_debug_output(self, traffic_gen_name, **kwargs):
        """
        Keyword Arguments:
        [traffic_gen_name] - The name of the traffic generator to enable debug output on.

        Enables debug output on a given traffic generator.
        """
        self._init_keyword(traffic_gen_name, **kwargs)

        if self.traffic_gen is not None:
            self.traffic_gen.debug_ixia = True

    def disable_traffic_generator_debug_output(self, traffic_gen_name, **kwargs):
        """
        Keyword Arguments:
        [traffic_gen_name] - The name of the traffic generator to disable debug output on.

        Disables debug output on a given traffic generator.
        """
        self._init_keyword(traffic_gen_name, **kwargs)

        if self.traffic_gen is not None:
            self.traffic_gen.debug_ixia = False

    def __base_connect_to_traffic_generator(self, traffic_gen_name, vendor, chassis_ip, vm_ip=None, username=None,
                                            connection_port=None, password=None):
        username = username if username is not None else self.traffic_gen_constants.USER_NAME
        password = password if password is not None else self.traffic_gen_constants.PASSWORD

        if vendor.lower() == TrafficGenConstants.IXIA_CHASSIS:
            traffic_device = IxiaDevice()
            traffic_device.vendor = TrafficGenConstants.IXIA_CHASSIS
            traffic_device.hostname = vm_ip if vm_ip is not None else self.traffic_gen_constants.VM_IP
            traffic_device.port = (connection_port if connection_port is not None and connection_port != ""
                                   else self.traffic_gen_constants.IXIA_PORT)
        elif vendor.lower() == TrafficGenConstants.OSTINATO_CHASSIS:
            traffic_device = OstinatoDevice()
            traffic_device.vendor = TrafficGenConstants.OSTINATO_CHASSIS
            traffic_device.hostname = chassis_ip
            traffic_device.port = (connection_port if connection_port is not None and connection_port != ""
                                   else self.traffic_gen_constants.OSTINATO_PORT)
        elif vendor.lower() == TrafficGenConstants.SPIRENT_CHASSIS:
            traffic_device = SpirentDevice()
            traffic_device.vendor = TrafficGenConstants.SPIRENT_CHASSIS
            traffic_device.hostname = vm_ip if vm_ip is not None else self.traffic_gen_constants.VM_IP
            traffic_device.port = (connection_port if connection_port is not None and connection_port != ""
                                   else self.traffic_gen_constants.SPIRENT_PORT)
        elif vendor.lower() == TrafficGenConstants.JETS_CHASSIS:
            traffic_device = JetsDevice()
            traffic_device.vendor = TrafficGenConstants.JETS_CHASSIS
            traffic_device.hostname = chassis_ip
            traffic_device.set_username(username)
            traffic_device.set_password(password)
            traffic_device.port = (connection_port if connection_port is not None and connection_port != ""
                                   else self.traffic_gen_constants.JETS_PORT)
        elif vendor.lower() == TrafficGenConstants.IXLOAD_CHASSIS:
            traffic_device = IxLoadDevice()
            traffic_device.vendor = TrafficGenConstants.IXLOAD_CHASSIS
            traffic_device.hostname = vm_ip if vm_ip is not None else self.traffic_gen_constants.VM_IP
            traffic_device.port = (connection_port if connection_port is not None and connection_port != ""
                                   else self.traffic_gen_constants.IXLOAD_PORT)
        else:
            self.logger.log_info("Vendor " + vendor + "is not supported.")
            return CommandObjectConstants.METHOD_NOT_SUPPORTED

        traffic_device.chassis_ip = chassis_ip
        traffic_device.username = username
        traffic_device.name = traffic_gen_name
        self.device_collection.add_device(traffic_gen_name, traffic_device)

        log_message = ["Connecting to traffic generator...,"
                       "Name: " + traffic_gen_name,
                       "Vendor: " + vendor,
                       "Chassis IP: " + chassis_ip,
                       "VM IP: " + traffic_device.hostname,
                       "Username: " + traffic_device.username,
                       "Connection Port: " + traffic_device.port
                       ]

        self.logger.log_debug("\n".join(log_message))

    def __connect_and_wait(self, tgen_name, max_wait):
        self.traffic_gen.connect(self.traffic_gen.hostname, self.traffic_gen.port)

        start_time = time.time()

        while not self.traffic_gen.initialized and (time.time() - start_time) < int(max_wait):
            self.logger.log_info("Unable to establish a connection with traffic generator " + tgen_name +
                                 " retrying...")

            self.traffic_gen.connect(self.traffic_gen.hostname, self.traffic_gen.port)

            time.sleep(5)

        if not self.traffic_gen.initialized:
            raise AttributeError("Unable to establish a connection with traffic generator " + tgen_name + ".")
        else:
            self.logger.log_debug("Connection to traffic generator " + tgen_name + " was successful.")

    def build_dict_of_tgens(self, **kwargs):
        try:
            variables = RobotUtils.get_variables(no_decoration=True)
        except Exception as e:
            if "yaml_dict" in kwargs:
                variables = kwargs["yaml_dict"]
            else:
                raise e

        tgens = NetworkElementUtils.get_device_names_from_variables(variables, "tgen")
        tgen_dict = {}

        for tgen in tgens:
            tgen_id = tgen
            tgen_name = None
            tgen_vendor = None
            tgen_chassis_ip = None

            try:
                tgen_name = variables[tgen]["name"]
                tgen_vendor = variables[tgen]["vendor"]
                tgen_chassis_ip = variables[tgen]["ip"]
            except KeyError:
                if tgen_vendor is None:
                    self.logger.log_error("${" + tgen + ".vendor} variable not present in testbed resource file.")
                if tgen_chassis_ip is None:
                    self.logger.log_error("${" + tgen + ".ip} variable not present in testbed " + "resource file.")

            tgen_vm_ip = variables[tgen].get("vm_ip", None)
            tgen_user = variables[tgen].get("username", None)
            tgen_pass = variables[tgen].get("password", None)
            tgen_port = variables[tgen].get("port", None)
            tgen_max_wait = variables[tgen].get("max_wait", "240")
            jets_dir = variables[tgen].get("jets_dir", None)
            view_tag = variables[tgen].get("view_tag", None)

            # Checking for 'skip_connect' key in the netelem dict
            skip_connect = variables[tgen].get("skip_connect", False)

            tgen_dict[tgen_name] = {"tgen_name": tgen_name,
                                    "tgen_vendor": tgen_vendor,
                                    "tgen_chassis_ip": tgen_chassis_ip,
                                    "tgen_vm_ip": tgen_vm_ip,
                                    "tgen_user": tgen_user,
                                    "tgen_pass": tgen_pass,
                                    "tgen_port": tgen_port,
                                    "tgen_max_wait": tgen_max_wait,
                                    "jets_dir": jets_dir,
                                    "view_tag": view_tag,
                                    "tgen_id": tgen_id,
                                    "skip_connect": skip_connect}
        return tgen_dict
