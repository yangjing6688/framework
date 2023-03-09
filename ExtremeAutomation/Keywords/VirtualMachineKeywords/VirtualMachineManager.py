from ExtremeAutomation.Library.Device.EndsystemElement.Constants.EndsystemElementConstants import \
    EndsystemElementConstants
from ExtremeAutomation.Library.Utils.VirtualMachineUtils import VirtualMachineUtils
from ExtremeAutomation.Library.Device.Common.Agents.AgentConstants import AgentConstants
from ExtremeAutomation.Library.Device.VirtualEnvironment.VirtualMachineDevice import VirtualMachineDevice
from ExtremeAutomation.Keywords.BaseClasses.VirtualMachineKeywordBaseClass import VirtualMachineKeywordBaseClass
from ExtremeAutomation.Library.Utils.RobotUtils import RobotUtils


class VirtualMachineManager(VirtualMachineKeywordBaseClass):

    def connect_to_vm_server(self, vm_type, server_ip, port, username, password, name, connection_method="rest",
                             **kwargs):
        """
        This function adds the Virtual Machine connection info to the Device Collection and initializes it.
        """
        if vm_type == "vmware":
            virtual_machine_type = self.constants.OS_VMWARE
        elif vm_type == "vbox":
            virtual_machine_type = self.constants.OS_VIRTUAL_BOX
        else:
            virtual_machine_type = None

        vm = VirtualMachineDevice(virtual_machine_type, server_ip, port, username, password)
        vm.name = name

        # Check for non-default connection_method (default is REST, only other supported type is SSH)
        vm.connection_method, vm.port = self.__get_connection_method(connection_method, port)

        if virtual_machine_type == self.constants.OS_VIRTUAL_BOX and vm.connection_method == AgentConstants.TYPE_SSH:
            vm.oper_sys = EndsystemElementConstants.OS_LINUX
            vm.platform = EndsystemElementConstants.PLATFORM_LINUX_BASE
            vm.login_prompt = ["login as:"]
            vm.pass_prompt = ["password:"]
            vm.main_prompt = "$"
            vm.end_of_line = "\r\n"

        self.device_collection.add_device(name, vm)
        self._init_keyword(name, **kwargs)

    def connect_to_all_vm_servers(self, **kwargs):
        """
        Keyword Arguments:
        None

        Searches the testbed environment file for VM servers and connects to each.
        """
        server_dict = self.__build_dict_of_servers(**kwargs)
        for server_name in server_dict:
            server_type = server_dict[server_name]["server_type"]
            server_ip = server_dict[server_name]["server_ip"]
            server_port = server_dict[server_name]["server_port"]
            server_user = server_dict[server_name]["server_user"]
            server_pass = server_dict[server_name]["server_pass"]
            server_name = server_dict[server_name]["server_name"]
            server_connection_method = server_dict[server_name]["server_connection_method"]

            self.connect_to_vm_server(server_type, server_ip, server_port, server_user, server_pass, server_name,
                                      server_connection_method)

    def disconnect_vm_server(self, name, **kwargs):
        """
        This function removes the Virtual Machine from the Device Collection and closes any connections.
        """
        self._init_keyword(name, self.constants.BASE_VIRTUAL_API, **kwargs)
        self.device_collection.remove_device(name)
        self.vm_api.terminate()

    def disconnect_all_vm_servers(self, **kwargs):
        """
        Keyword Arguments:
        None

        Searches the currently connected VM servers and disconnects each.
        """
        devices = self.device_collection.get_device_list()
        server_list = []
        for device in devices:
            device_obj = self.device_collection.get_device(device)
            if isinstance(device_obj, VirtualMachineDevice):
                server_list.append(device)

        for server in server_list:
            self.disconnect_vm_server(server, **kwargs)

    # ##################################################################################################################
    #   Deprecated Keywords - DO NOT USE   #############################################################################
    # ##################################################################################################################
    def connect_to_vm(self, vm_type, server_ip, port, username, password, name):
        """
        *DEPRECATED!* Use "Connect to VM Server" instead.
        This function adds the Virtual Machine connection info to the Device Collection and initializes it.
        """
        if vm_type == "vmware":
            virtual_machine_type = self.constants.OS_VMWARE
        elif vm_type == "vbox":
            virtual_machine_type = self.constants.OS_VIRTUAL_BOX
        else:
            virtual_machine_type = None

        vm = VirtualMachineDevice(virtual_machine_type, server_ip, port, username, password)

        self.device_collection.add_device(name, vm)
        self._init_keyword(name)

    def disconnect_vm(self, name):
        """
        *DEPRECATED!* Use "Disconnect VM Server" instead.
        This function removes the Virtual Machine from the Device Collection and closes any connections.
        """
        self._init_keyword(name, self.constants.BASE_VIRTUAL_API)
        self.device_collection.remove_device(name)
        self.vm_api.terminate()

    # ##################################################################################################################
    #   Helper Functions   #############################################################################################
    # ##################################################################################################################
    def __build_dict_of_servers(self, **kwargs):
        try:
            variables = RobotUtils.get_variables(no_decoration=True)
        except Exception as e:
            if "yaml_dict" in kwargs:
                variables = kwargs["yaml_dict"]
            else:
                raise e

        vm_servers = VirtualMachineUtils.get_device_names_from_variables(variables, "vm_server")
        server_dict = {}
        for vm_server in vm_servers:
            server_id = vm_server
            server_ip = None
            server_user = None
            server_pass = None
            server_type = None
            server_name = None

            try:
                server_ip = variables[vm_server]["ip"]
                server_user = variables[vm_server]["username"]
                server_pass = variables[vm_server]["password"]
                server_type = variables[vm_server]["vm_type"]
                server_name = variables[vm_server]["name"]
            except KeyError:
                if server_ip is None:
                    self.logger.log_error("${" + vm_server + ".ip} variable not present in testbed " +
                                          "resource file.")
                if server_user is None:
                    self.logger.log_error("${" + vm_server + ".username} variable not present in testbed " +
                                          "resource file.")
                if server_pass is None:
                    self.logger.log_error("${" + vm_server + ".password} variable not present in testbed " +
                                          "resource file.")
                if server_type is None:
                    self.logger.log_error("${" + vm_server + ".type} variable not present in testbed resource file.")
                if server_name is None:
                    self.logger.log_error("${" + vm_server + ".name} variable not present in testbed resource file.")

            if "connection_method" in variables[vm_server]:
                server_connection_method = variables[vm_server]["connection_method"]
            else:
                server_connection_method = AgentConstants.TYPE_REST

            if "port" in variables[vm_server]:
                server_port = variables[vm_server]["port"]
            elif (server_type.lower() == "virtualbox" or server_type.lower() == "vbox") and \
                    server_connection_method.lower() == AgentConstants.TYPE_REST:
                server_port = "9016"
            elif (server_type.lower() == "virtualbox" or server_type.lower() == "vbox") and \
                    server_connection_method.lower() == AgentConstants.TYPE_SSH:
                server_port = "22"
            else:
                server_port = None

            server_dict[server_name] = {"server_ip": server_ip,
                                        "server_user": server_user,
                                        "server_pass": server_pass,
                                        "server_port": server_port,
                                        "server_type": server_type,
                                        "server_name": server_name,
                                        "server_connection_method": server_connection_method,
                                        "server_id": server_id}
        return server_dict

    @staticmethod
    def __get_connection_method(connection_method, port):
        """
        Takes a connection method string (ex. "telnet" or "ssh") and returns the connection method constant and default
        port used by the protocol.
        """
        if connection_method.lower() == AgentConstants.TYPE_SSH:
            connection_method = AgentConstants.TYPE_SSH
            port = port if port is not None else AgentConstants.SSH_PORT
        elif connection_method.lower() == AgentConstants.TYPE_REST:
            connection_method = AgentConstants.TYPE_REST
            port = port if port is not None else AgentConstants.REST_PORT
        return connection_method, port
