import time
from ExtremeAutomation.Library.Utils.ListUtils import ListUtils
from ExtremeAutomation.Keywords.FailureException import FailureException
from ExtremeAutomation.Library.Utils.VirtualMachineUtils import VirtualMachineUtils
from ExtremeAutomation.Keywords.BaseClasses.VirtualMachineKeywordBaseClass import VirtualMachineKeywordBaseClass
from ExtremeAutomation.Library.Device.VirtualEnvironment.Constants.VirtualConstants import VirtualConstants
from ExtremeAutomation.Library.Utils.RobotUtils import RobotUtils


class VirtualMachineControl(VirtualMachineKeywordBaseClass):
    """
    This library is designed to control Virtual Machines (VM's) throughout your testing. Currently it should work with
    virtualbox and VMware.

    In order to use this class you need a server connection element and the name of a Virtual machine to work with.

    vm_server = VmManager.connect_to_vm(SERVER_TYPE, SERVER_IP, SERVER_PORT, SERVER_USERNAME, SERVER_PASSWORD,
                                        SERVER_ALIAS)

    SERVER_TYPE:     This is the type of server you will connect to current options are "vbox" or "vmware".
    SERVER_IP:       This is the IP address of the server.
    SERVER_PORT:     This is the port the server is listening on. Vbox is 18083.
    SERVER_USERNAME: Name to authenticate to the server with.
    SERVER_PASSWORD: Password to authenticate to the server with.
    SERVER_ALIAS:    Alias name to give the server in order to easily work with throughout your testing.

    Here is an example use case to turn on a VM:

        #This only needs to be issued once at the beginning of a testplan
        vm_server = VmManager.connect_to_vm("vbox", "10.52.1.43", "18083", "administrator", "password!", "server1")

        VMControl.turn_on_vm("server1", "My_Windows_VM")

    """

    def turn_on_vm(self, server, vm_names, wait_after_startup=0, vm_type='headless', **kwargs):
        """
        Keyword Arguments:
        [server]             - The host server for the Virtual Machine
        [vm_names]           - The name of the Virtual Machine(s)
        [wait_after_startup] - The time to delay after starting the Virtual Machine
        [vm_type]            - The Virtual Machine type, headless or GUI
                               (This is dependant on the server type)

        This function will turn on a VM.
        If the VM is already running this command will not be run.
        """
        self._init_keyword(server, self.constants.BASE_VIRTUAL_API, **kwargs)
        vm_names = ListUtils.convert_to_list(vm_names)
        for vm_name in vm_names:
            if self.vm_api.get_initialized():
                current_state = self.vm_api.get_vm_state(vm_name)
                self.logger.log_info("Current State" + str(current_state))
                if current_state == VirtualConstants.VM_STATE_POWERED_ON:
                    self.logger.log_info("VM is already Running")
                else:
                    self.vm_api.start_vm(vm_name, vm_type, **kwargs)
                    self.vm_api.wait_for_vm_state(vm_name, VirtualConstants.VM_STATE_POWERED_ON, timeout=60)
                    time.sleep(int(wait_after_startup))
            else:
                raise FailureException("Something went wrong with vm get_initialized")

    def turn_on_all_network_element_vms(self, **kwargs):
        """
        Keyword Arguments:
        None

        Searches the testbed environment file for VMs that start with 'netelem' and turns them on.
        """
        netelem_vm_dict = self.__build_dict_of_netelem_vms(**kwargs)
        for vm in netelem_vm_dict:
            vm_server = netelem_vm_dict[vm]["vm_server"]
            vm_name = netelem_vm_dict[vm]["vm_name"]
            vm_wait = netelem_vm_dict[vm]["vm_wait"]
            vm_type = netelem_vm_dict[vm]["vm_type"]

            self.turn_on_vm(vm_server, vm_name, vm_wait, vm_type)

    def turn_off_all_network_element_vms(self, **kwargs):
        """
        Keyword Arguments:
        None

        Searches the testbed environment file for VMs that start with 'netelem' and turns them off.
        """
        netelem_vm_dict = self.__build_dict_of_netelem_vms(**kwargs)
        for vm in netelem_vm_dict:
            vm_server = netelem_vm_dict[vm]["vm_server"]
            vm_name = netelem_vm_dict[vm]["vm_name"]
            vm_wait = netelem_vm_dict[vm]["vm_wait"]

            self.turn_off_vm_forceful(vm_server, vm_name, vm_wait)

    def get_internal_network_name(self, server, vm_name, nic_number):
        """
        Keyword Arguments:
        [server]     - The host server for the Virtual Machine
        [vm_name]    - The Virtual Machine's device name
        [nic_number] - The Virtual Machine interface number

        This function returns the Virtual Machine NIC's internal network name.
        """
        self._init_keyword(server, self.constants.BASE_VIRTUAL_API)
        network = self.vm_api.get_internal_network_name(vm_name, nic_number)
        return network

    def provision_vm_nic_settings(self, server, vm_names, nic_number, internal_nic_name, mac_address):
        """
        Keyword Arguments:
        [server]            - The host server for the Virtual Machine(s)
        [vm_names]          - The name of the Virtual Machine(s)
        [nic_number]        - The Virtual Machine(s) interface number
        [internal_nic_name] - The Internal Network to assign to the NIC
        [mac_address]       - The MAC address to use for the NIC

        This function configures the Virtual Machine NIC with the given internal network.
        """
        self._init_keyword(server, self.constants.BASE_VIRTUAL_API)
        vm_names = ListUtils.convert_to_list(vm_names)
        for vm_name in vm_names:
            if self.vm_api.get_initialized():
                current_state = self.vm_api.get_vm_state(vm_name)
                if current_state == VirtualConstants.VM_STATE_POWERED_ON:
                    self.logger.log_info("VM is already Running... Will not configure NIC settings")
                else:
                    self.vm_api.provision_vm_nic_settings(vm_name, int(nic_number), str(internal_nic_name),
                                                          str(mac_address))
            else:
                raise FailureException("Something went wrong with vm get_initialized")

    def turn_on_rdp_for_vm(self, server, vm_names):
        """
        Keyword Arguments:
        [server]   - The host server for the Virtual Machine(s)
        [vm_names] - The name of the Virtual Machine(s)

        This function enables the Virtual Remote Desktop service for the Virtual Machine(s).
        """
        self._init_keyword(server, self.constants.BASE_VIRTUAL_API)
        vm_names = ListUtils.convert_to_list(vm_names)
        for vm_name in vm_names:
            if self.vm_api.get_initialized():
                current_state = self.vm_api.get_vm_state(vm_name)

                if current_state == VirtualConstants.VM_STATE_POWERED_ON:
                    self.logger.log_info("VM is already Running")
                else:
                    self.vm_api.turn_on_rdp_for_vm(vm_name)

            else:
                raise FailureException("Something went wrong with vm get_initialized")

    def turn_on_cloud_vm(self, vm_name):
        """
        Keyword Agruments:
        [vm_name] - Name of VM to be working with. This IS case sensitive.

        This function will turn on a VM. If the Vm is already running this command will not be run.
        """
        device = self._init_keyword(vm_name, self.constants.BASE_VIRTUAL_API)

        if self.vm_api.get_initialized():
            current_state = self.vm_api.get_vm_state(vm_name)

            if current_state == VirtualConstants.VM_STATE_POWERED_ON:
                self.logger.log_info("VM is already Running")
            else:
                instance = self.vm_api.start_vm(vm_name)
                device.instance_id = instance.id
        else:
            raise FailureException("Something went wrong with vm get_initialized")

    def turn_off_vm_graceful(self, server, vm_names, wait_after_shutdown=0):
        """
        Keyword Arguments:
        [server]              - The host server for the Virtual Machine(s)
        [vm_names]            - The name of the Virtual Machine(s)
        [wait_after_shutdown] - The time to delay after shutting down the Virtual Machine

        This function will gracefully power down a VM. To prevent VM lockups, this command will not be
        run if the VM is already powered off.
        """
        self._init_keyword(server, self.constants.BASE_VIRTUAL_API)
        vm_names = ListUtils.convert_to_list(vm_names)
        for vm_name in vm_names:
            if self.vm_api.get_initialized():
                current_state = self.vm_api.get_vm_state(vm_name)

                if current_state == VirtualConstants.VM_STATE_POWERED_OFF:
                    self.logger.log_info("VM is already off")
                else:
                    self.vm_api.power_down_vm_power_button(vm_name)
                    time.sleep(int(wait_after_shutdown))

            else:
                # KeywordUtils.log_running_keyword("Something went wrong with vm get_initialized")
                raise FailureException("Something went wrong with vm get_initialized")

    def turn_off_vm_forceful(self, server, vm_names, wait_after_shutdown=0):
        """
        Keyword Arguments:
        [server]              - The host server for the Virtual Machine(s)
        [vm_names]            - The name of the Virtual Machine(s)
        [wait_after_shutdown] - The time to delay after shutting down the Virtual Machine

        This function will gracefully power down a VM. To prevent VM lockups, this command will not be
        run if the VM is already powered off.
        """
        self._init_keyword(server, self.constants.BASE_VIRTUAL_API)
        vm_names = ListUtils.convert_to_list(vm_names)
        for vm_name in vm_names:
            if self.vm_api.get_initialized():
                current_state = self.vm_api.get_vm_state(vm_name)

                if current_state == VirtualConstants.VM_STATE_POWERED_OFF:
                    self.logger.log_info("VM is already off")
                else:
                    self.vm_api.power_down_vm(vm_name)
                    self.vm_api.wait_for_vm_state(vm_name, VirtualConstants.VM_STATE_POWERED_OFF, timeout=60)
                    time.sleep(int(wait_after_shutdown))
            else:
                raise FailureException("Something went wrong with vm get_initialized")

    def turn_off_cloud_vm(self, vm_name):
        """
        Keyword Arguments:
        [vm_name] - The name of the Virtual Machine

        This function will gracefully power down a VM. To prevent VM lockups, this command will not be
        run if the VM is already powered off.
        """
        self._init_keyword(vm_name, self.constants.BASE_VIRTUAL_API)

        if self.vm_api.get_initialized():
            current_state = self.vm_api.get_vm_state(vm_name)
            if current_state == VirtualConstants.VM_STATE_POWERED_OFF:
                self.logger.log_info("VM is already off")
            else:
                self.vm_api.terminate_vm(vm_name)
        else:
            raise FailureException("Something went wrong with vm get_initialized")

    def get_current_vm_state(self, server, vm_names):
        """
        Keyword Arguments:
        [server]   - The host server for the Virtual Machine(s)
        [vm_names] - The name of the Virtual Machine(s)

        This function returns the current operational state of the Virtual Machine.
        """
        self._init_keyword(server, self.constants.BASE_VIRTUAL_API)
        vm_names = ListUtils.convert_to_list(vm_names)
        for vm_name in vm_names:
            current_state = self.vm_api.get_vm_state(vm_name)
            return current_state

    def is_vm_running(self, server, vm_names):
        """
        Keyword Arguments:
        [server]   - The host server for the Virtual Machine(s)
        [vm_names] - The name of the Virtual Machine(s)

        This function returns 'True' if the Virtual Machine is powered on.
        """
        self._init_keyword(server, self.constants.BASE_VIRTUAL_API)
        vm_names = ListUtils.convert_to_list(vm_names)
        for vm_name in vm_names:
            current_state = self.vm_api.get_vm_state(vm_name)
            if current_state == 'PoweredOn':
                return True
            else:
                return False

    def log_into_vm(self, server, vm_name, domain, username, password):
        """
        Keyword Arguments:
        [server]   - Dictionary list of Server elements
        [vm_name]  - Name of VM to be working with. This IS case sensitive.
        [domain]   - Domain for user to log into
        [username] - Username for user to log into the VM
        [password] - Password for user to log into the VM

        This function will log a user into the given VM.
        """
        self._init_keyword(server, self.constants.BASE_VIRTUAL_API)

        if self.vm_api.get_initialized():
            current_state = self.vm_api.get_vm_state(vm_name)
            if current_state != VirtualConstants.VM_STATE_POWERED_ON:
                raise FailureException("VM is not running, log in will not be attempted!")
            else:
                self.vm_api.set_credentials(vm_name, username, password, domain)
                self.vm_api.wait_for_vm_state(vm_name, VirtualConstants.VM_STATE_POWERED_ON, timeout=60)
        else:
            raise FailureException("Something went wrong with vm get_initialized")

    def load_snapshot(self, server, vm_names, snapshot):
        """
        Keyword Arguments:
        [server]   - Dictionary list of Server elements
        [vm_name]  - Name of VM to be working with. This IS case sensitive.
        [snapshot] - Name of the snapshot. Case sensitive

        This function will load a snapshot on a VM. The function checks to verify VM
        is powered off before attempting to load the snapshot.
        """
        self._init_keyword(server, self.constants.BASE_VIRTUAL_API)
        vm_names = ListUtils.convert_to_list(vm_names)
        for vm_name in vm_names:
            if self.vm_api.get_initialized():
                current_state = self.vm_api.get_vm_state(vm_name)

                if current_state != VirtualConstants.VM_STATE_POWERED_OFF:
                    self.logger.log_info("VM is already Running... Will NOT load snapshot")
                else:
                    self.vm_api.restore_vm_snapshot(vm_name, snapshot)
            else:
                raise FailureException("Something went wrong with vm get_initialized")

    def take_snapshot(self, server, vm_name, snapshot):
        """
        Keyword Arguments:
        [server]   - Dictionary list of Server elements
        [vm_name]  - Name of VM to be working with. This IS case sensitive.
        [snapshot] - Name to save the snapshot as

        This function will take a snapshot of the current system. This defined function will verify system is
        in the powered off state before the snapshot is taken.
        """
        self._init_keyword(server, self.constants.BASE_VIRTUAL_API)

        if self.vm_api.get_initialized():
            current_state = self.vm_api.get_vm_state(vm_name)
            if current_state != VirtualConstants.VM_STATE_POWERED_OFF:
                self.logger.log_info("VM is already Running... Will not configure NIC settings")
            else:
                self.vm_api.take_vm_snapshot(vm_name, snapshot)
                self.vm_api.wait_for_vm_state(vm_name, VirtualConstants.VM_STATE_POWERED_OFF, timeout=60)
        else:
            raise FailureException("Something went wrong with vm get_initialized")

    def delete_snapshot(self, server, vm_name, snapshot):
        """
        Keyword Arguments:
        [server]   - Dictionary list of Server elements
        [vm_name]  - Name of VM to be working with. This IS case sensitive.
        [snapshot] - Name of snapshot. Case sensitive

        This function will delete a snapshot. This will also check to verify system is powerd off before
        attempting to delete the snapshot.
        """
        self._init_keyword(server, self.constants.BASE_VIRTUAL_API)

        if self.vm_api.get_initialized():
            current_state = self.vm_api.get_vm_state(vm_name)
            if current_state != VirtualConstants.VM_STATE_POWERED_OFF:
                raise FailureException("VM is running, restore snapshot will not be attempted unless vm is PoweredOff!")
            else:
                self.vm_api.delete_vm_snapshot(vm_name, snapshot)
                self.vm_api.wait_for_vm_state(vm_name, VirtualConstants.VM_STATE_POWERED_OFF, timeout=60)
        else:
            raise FailureException("Something went wrong with vm get_initialized")

    def pause_vm(self, server, vm_name):
        """
        Keyword Arguments:
        [server]  - Dictionary list of Server elements
        [vm_name] - Name of VM to be working with. This IS case sensitive.

        This function will pause a VM.
        """
        self._init_keyword(server, self.constants.BASE_VIRTUAL_API)

        if self.vm_api.get_initialized():
            current_state = self.vm_api.get_vm_state(vm_name)
            if current_state == "Paused":
                raise FailureException("VM is already paused!")
            else:
                self.vm_api.pause_vm(vm_name)
                self.vm_api.wait_for_vm_state(vm_name, "Paused", timeout=60)
        else:
            raise FailureException("Something went wrong with vm get_initialized")

    def resume_vm(self, server, vm_name):
        """
        Keyword Arguments:
        [server]  - Dictionary list of Server elements
        [vm_name] - Name of VM to be working with. This IS case sensitive.

        This function will resume a paused VM.
        """
        self._init_keyword(server, self.constants.BASE_VIRTUAL_API)

        if self.vm_api.get_initialized():
            current_state = self.vm_api.get_vm_state(vm_name)
            if current_state == VirtualConstants.VM_STATE_POWERED_ON:
                raise FailureException("VM is already running!")
            else:
                self.vm_api.resume_vm(vm_name)
                self.vm_api.wait_for_vm_state(vm_name, VirtualConstants.VM_STATE_POWERED_ON, timeout=60)
        else:
            raise FailureException("Something went wrong with vm get_initialized")

    def simulate_cable_disconnect(self, server, vm_name, interface):
        """
        Keyword Arguments:
        [server]    - Dictionary list of Server elements
        [vm_name]   - Name of VM to be working with. This IS case sensitive.
        [interface] - Interface number on VM e.g. 1 Current valid range for Vbox is 1-8

        This function will simulate a cable disconnect between the VM and connected device. Link will show down on the
        VM however it may still show link up on the DUT end of the connection.
        """
        self._init_keyword(server, self.constants.BASE_VIRTUAL_API)

        if self.vm_api.get_initialized():
            self.vm_api.set_link_state(vm_name, "Off", int(interface))
        else:
            raise FailureException("Something went wrong with vm get_initialized")

    def simulate_cable_reconnect(self, server, vm_name, interface):
        """
        Keyword Arguments:
        [server]    - Dictionary list of Server elements
        [vm_name]   - Name of VM to be working with. This IS case sensitive.
        [interface] - Interface number on VM e.g. 1 Current valid range for Vbox is 1-8

        This function will simulate a cable reconnect between the VM and connected device. This will brink link up on
        both the VM and the connected device.
        """
        self._init_keyword(server, self.constants.BASE_VIRTUAL_API)

        if self.vm_api.get_initialized():
            self.vm_api.set_link_state(vm_name, "On", int(interface))
        else:
            raise FailureException("Something went wrong with vm get_initialized")

    def enable_nic_card(self, server, vm_names, interface):
        """
        Keyword Arguments:
        [server]    - The host server for the Virtual Machine(s)
        [vm_names]  - The name of the Virtual Machine(s)
        [interface] - The Virtual Machine's NIC number.

        This function enables the NIC's connection for the Virtual Machine.
        """
        self._init_keyword(server, self.constants.BASE_VIRTUAL_API)
        vm_names = ListUtils.convert_to_list(vm_names)
        for vm_name in vm_names:
            if self.vm_api.get_initialized():
                current_state = self.vm_api.get_vm_state(vm_name)
                if current_state == VirtualConstants.VM_STATE_POWERED_ON:
                    self.logger.log_info("VM is already Running... Will not configure NIC settings")
                else:
                    self.vm_api.set_nic_card_state(vm_name, int(interface), "on")
            else:
                raise FailureException("Something went wrong with vm get_initialized")

    def disable_nic_card(self, server, vm_names, interface):
        """
        Keyword Arguments:
        [server]    - The host server for the Virtual Machine(s)
        [vm_names]  - The name of the Virtual Machine(s)
        [interface] - The Virtual Machine's NIC number.

        This function disables the NIC's connection for the Virtual Machine.
        """
        self._init_keyword(server, self.constants.BASE_VIRTUAL_API)
        vm_names = ListUtils.convert_to_list(vm_names)
        for vm_name in vm_names:
            if self.vm_api.get_initialized():
                current_state = self.vm_api.get_vm_state(vm_name)
                if current_state == VirtualConstants.VM_STATE_POWERED_ON:
                    self.logger.log_info("VM is already Running... Will not configure NIC settings")
                else:
                    self.vm_api.set_nic_card_state(vm_name, int(interface), 'off')
            else:
                raise FailureException("Something went wrong with vm get_initialized")

    def set_instance_image_id(self, vm_name, image_id):
        """
        Keyword Arguments:
        [vm_name]  - Name of VM to be working with. This IS case sensitive.
        [image_id] - The AMI image ID.

        This function will set the AMI image ID used to create the VM.
        """
        self._init_keyword(vm_name, self.constants.BASE_VIRTUAL_API)

        if self.vm_api.get_initialized():
            self.vm_api.set_image_id(vm_name, image_id)
        else:
            raise FailureException("Something went wrong with vm get_initialized")

    def get_instance_image_id(self, vm_name):
        """
        Keyword Arguments:
        [vm_name] - Name of VM to be working with. This IS case sensitive.

        This function will return the current AMI image_id.
        """
        self._init_keyword(vm_name, self.constants.BASE_VIRTUAL_API)

        if self.vm_api.get_initialized():
            self.vm_api.get_image_id()
        else:
            raise FailureException("Something went wrong with vm get_initialized")

    def set_vm_type(self, vm_name, vm_type):
        """
        Keyword Arguments:
        [vm_name]  - Name of VM to be working with. This IS case sensitive.
        [image_id] - The AMI image ID.

        This function will set the AMI image ID used to create the VM.
        """
        self._init_keyword(vm_name, self.constants.BASE_VIRTUAL_API)

        if self.vm_api.get_initialized():
            self.vm_api.set_instance_type(vm_name, vm_type)
        else:
            raise FailureException("Something went wrong with vm get_initialized")

    def get_vm_type(self, vm_name):
        """
        Keyword Arguments:
        [vm_name]  - Name of VM to be working with. This IS case sensitive.
        [image_id] - The AMI image ID.

        This function will set the AMI image ID used to create the VM.
        """
        self._init_keyword(vm_name, self.constants.BASE_VIRTUAL_API)

        if self.vm_api.get_initialized():
            self.vm_api.get_instance_type()
        else:
            raise FailureException("Something went wrong with vm get_initialized")

    def set_min_count(self, vm_name, min_count):
        """
        Keyword Arguments:
        [vm_name]   - Name of VM to be working with. This IS case sensitive.
        [min_count] - The minimum count.

        This function will set the minimum VM count to spin up.
        """
        self._init_keyword(vm_name, self.constants.BASE_VIRTUAL_API)

        if self.vm_api.get_initialized():
            self.vm_api.set_min_count(vm_name, min_count)
        else:
            raise FailureException("Something went wrong with vm get_initialized")

    def get_min_count(self, vm_name):
        """
        Keyword Arguments:
        [vm_name] - Name of VM to be working with. This IS case sensitive.

        This function will return the current min_count value.
        """
        self._init_keyword(vm_name, self.constants.BASE_VIRTUAL_API)

        if self.vm_api.get_initialized():
            self.vm_api.get_min_count(vm_name)
        else:
            raise FailureException("Something went wrong with vm get_initialized")

    def get_vm_management_ip(self, vm_name):
        """
        Keyword Arguments:
        [vm_name] - Name of VM to be working with. This IS case sensitive.

        This function will return the current Public IP Address of the VM.
        """
        device = self._init_keyword(vm_name, self.constants.BASE_VIRTUAL_API)

        instance = device.instance_id
        result = self.vm_api.get_public_ip(instance)
        return result

    def get_vm_interface_external_ip(self, vm_name, int_name):
        """
        Keyword Arguments:
        [vm_name]  - Name of VM to be working with. This IS case sensitive.
        [int_name] - Name of Interface to be working with. This IS case sensitive.

        This function will return the current Public IP Address of a specific interface.
        """
        device = self._init_keyword(vm_name, self.constants.BASE_VIRTUAL_API)

        instance = device.instance_id
        result = self.vm_api.get_public_ip(instance)
        return result

    def get_vm_connection_type(self, vm_name):
        """
        Keyword Arguments:
        [vm_name] - Name of VM to be working with. This IS case sensitive.

        This function will return the connection agent type for the VM.
        """
        self._init_keyword(vm_name, self.constants.BASE_VIRTUAL_API)

        result = self.vm_api.get_connection_agent_type()
        return result

    def get_vm_connection_key(self, vm_name):
        """
        Keyword Arguments:
        [vm_name] - Name of VM to be working with. This IS case sensitive.

        This function will return the connection agent's key for the Virtual Machine.
        """
        device = self._init_keyword(vm_name, self.constants.BASE_VIRTUAL_API)

        instance = device.instance_id
        result = self.vm_api.get_connection_agent_key(instance)
        return result

    def create_cloud_interface(self, vm_name, ipaddr, int_name):
        """
        Keyword Arguments:
        [vm_name]  - The name of the Virtual Machine
        [ipaddr]   - The IP Address to assign to the interface
        [int_name] - The name to give the interface

        This function adds an new interface to the cloud VM with the given information.
        """
        self._init_keyword(vm_name, self.constants.BASE_VIRTUAL_API)

        self.vm_api.create_network_interface(ipaddr, int_name)

    def delete_cloud_interface(self, vm_name, int_name):
        """
        Keyword Arguments:
        [vm_name]  - The name of the Virtual Machine
        [int_name] - The name of the interface to delete

        This function removes the specified interface from the cloud VM.
        """
        self._init_keyword(vm_name, self.constants.BASE_VIRTUAL_API)

        self.vm_api.delete_network_interface(int_name)

    def connect_cloud_interface(self, vm_name, int_name):
        """
        Keyword Arguments:
        [vm_names]  - The name of the Virtual Machine(s)
        [interface] - The Virtual Machine's interface name.

        This function enables the NIC's connection for the Virtual Machine.
        """
        self._init_keyword(vm_name, self.constants.BASE_VIRTUAL_API)

        self.vm_api.connect_network_interfaces(int_name)

    def disconnect_cloud_interface(self, vm_name, int_name):
        """
        Keyword Arguments:
        [vm_names]  - The name of the Virtual Machine(s)
        [interface] - The Virtual Machine's interface name.

        This function disables the NIC's connection for the Virtual Machine.
        """
        self._init_keyword(vm_name, self.constants.BASE_VIRTUAL_API)

        self.vm_api.disconnect_network_interfaces(int_name)

    def _get_cloud_interface_state(self, vm_name, int_name):
        self._init_keyword(vm_name, self.constants.BASE_VIRTUAL_API)

        result = self.vm_api.get_network_interface_state(int_name)
        return result

    def wait_for_interface_state(self, vm_name, int_name, state):
        """
        Keyword Arguments:
        [vm_name]  - The name of the Virtual Machine
        [int_name] - The name of the Virtual Machine's interface
        [state]    - The interface state to wait for

        This function waits for the specified interface to reach the given state.
        """
        self._wait_for('120', '10', "Waiting for " + int_name + " to enter state " + state + ".",
                       self._get_cloud_interface_state, state, vm_name, int_name)

    def display_cloud_testbed_info(self, vm_name, int_name):
        """
        Keyword Arguments:
        [vm_name]  - The name of the Virtual Machine
        [int_name] - The name of the Virtual Machine's interface

        This function displays the connection information for the Virtual Machine from the specified interface.
        """
        self._init_keyword(vm_name, self.constants.BASE_VIRTUAL_API)

        self.logger.log_info("  - " + vm_name + " -" + "\n" +
                             "External IP Address: " + str(self.get_vm_interface_external_ip(vm_name,
                                                                                             int_name)) + "\n" +
                             "Connection Agent Type: " + str(self.get_vm_connection_type(vm_name)) + "\n" +
                             "Connection Agent Key: " + str(self.get_vm_connection_key(vm_name))
                             )

    def display_cloud_engine_info(self, vm_name):
        """
        Keyword Arguments:
        [vm_name]  - The name of the Virtual Machine

        This function displays the connection information for the Virtual Machine Test Engine.
        """
        self._init_keyword(vm_name, self.constants.BASE_VIRTUAL_API)

        self.logger.log_info("  - " + vm_name + " -" + "\n" +
                             "External IP Address: " + str(self.get_vm_management_ip(vm_name)) + "\n" +
                             "Connection Agent Type: " + str(self.get_vm_connection_type(vm_name)) + "\n" +
                             "Connection Agent Key: " + str(self.get_vm_connection_key(vm_name))
                             )

    def allocate_public_ip_address(self, vm_name):
        """
        Keyword Arguments:
        [vm_name]  - The name of the Virtual Machine

        This function requests a public IP address for the Virtual Machine.
        """
        self._init_keyword(vm_name, self.constants.BASE_VIRTUAL_API)

        self.vm_api.allocate_ip_address()

    def assign_public_ip_address(self, vm_name, int_name):
        """
        Keyword Arguments:
        [vm_name]  - The name of the Virtual Machine
        [int_name] - The name of the Virtual Machine's interface

        This function assigns the public IP address to the specified Virtual Machine interface.
        """
        self._init_keyword(vm_name, self.constants.BASE_VIRTUAL_API)

        self.vm_api.wait_for_vm_state(vm_name, "Running", timeout=120)
        self.vm_api.assign_ip_address(int_name)

    def add_cloud_vm_interface(self, vm_name, int_name, dev_index, subnet_id, ip_address=None):
        """
        Keyword Arguments:
        [vm_name]    - The name of the Virtual Machine
        [int_name]   - The name to give the interface
        [dev_index]  - The interface index number
        [subnet_id]  - The subnet ID for the IP address
        [ip_address] - The IP Address to assign to the interface

        This function adds an new interface to the cloud VM with the given information.
        """
        self._init_keyword(vm_name, self.constants.BASE_VIRTUAL_API)

        self.vm_api.add_network_interface(int_name, dev_index, subnet_id, ip_address)

    def add_shared_folder(self, server, vm_names, folder_name, host_path, automount=True, **kwargs):
        """
        Keyword Arguemnts:
        [server]      - The host server for the Virtual Machine(s)
        [vm_names]    - The name of the Virtual Machine(s)
        [folder_name] - The name to assign to the shared folder config
        [host_path]   - The path to the shared folder on the host server
        [automount]   - Toggle for allowing auto-mount of the shared folder

        This function will add a shared folder from the Host server to the specified VM.
        """
        self._init_keyword(server, self.constants.BASE_VIRTUAL_API, **kwargs)
        vm_names = ListUtils.convert_to_list(vm_names)
        for vm_name in vm_names:
            if self.vm_api.get_initialized():
                current_state = self.vm_api.get_vm_state(vm_name)
                if current_state == VirtualConstants.VM_STATE_POWERED_ON:
                    self.logger.log_info("VM is already Running... Will not configure shared folders")
                else:
                    self.vm_api.shared_folder_config(vm_name, folder_name, host_path, "add", automount)
            else:
                raise FailureException("Something went wrong with vm get_initialized")

    def remove_shared_folder(self, server, vm_names, folder_name, **kwargs):
        """
        Keyword Arguemnts:
        [server]      - The host server for the Virtual Machine(s)
        [vm_names]    - The name of the Virtual Machine(s)
        [folder_name] - The name assigned to the shared folder config

        This function will remove a shared folder from the Host server on the specified VM.
        """
        self._init_keyword(server, self.constants.BASE_VIRTUAL_API, **kwargs)
        vm_names = ListUtils.convert_to_list(vm_names)
        for vm_name in vm_names:
            if self.vm_api.get_initialized():
                current_state = self.vm_api.get_vm_state(vm_name)
                if current_state == VirtualConstants.VM_STATE_POWERED_ON:
                    self.logger.log_info("VM is already Running... Will not configure shared folders")
                else:
                    self.vm_api.shared_folder_config(vm_name, folder_name, add_remove="remove")
            else:
                raise FailureException("Something went wrong with vm get_initialized")

    def delete_vm(self, server, vm_name):
        """
        Keyword Arguments:
        [vm_name] - Name of VM to be working with. This IS case sensitive.

        This function will delete the VM
        """
        self._init_keyword(server, self.constants.BASE_VIRTUAL_API)
        self.vm_api.delete_vm(vm_name)

    def __build_dict_of_netelem_vms(self, **kwargs):
        try:
            variables = RobotUtils.get_variables(no_decoration=True)
        except Exception as e:
            if "yaml_dict" in kwargs:
                variables = kwargs["yaml_dict"]
            else:
                raise e

        netelem_vms = VirtualMachineUtils.get_device_names_from_variables(variables, "netelem")
        netelem_vm_dict = {}
        for netelem in netelem_vms:
            vm_id = netelem
            vm_server = None
            vm_name = None
            vm_wait = None
            vm_type = None

            try:
                vm_server = variables["vms"][netelem]["server"]
                vm_name = variables["vms"][netelem]["name"]
                vm_wait = variables["vms"][netelem]["wait_after_startup"]
                vm_type = variables["vms"][netelem]["vm_type"]
            except KeyError:
                if vm_server is None:
                    self.logger.log_error("${vms." + netelem + ".server} variable not present in testbed " +
                                          "resource file.")
                if vm_name is None:
                    self.logger.log_error("${vms." + netelem + ".name} variable not present in testbed " +
                                          "resource file.")
                if vm_wait is None:
                    self.logger.log_error("${vms." + netelem + ".wait_after_startup} variable not present in testbed " +
                                          "resource file.")
                if vm_type is None:
                    self.logger.log_error("${vms." + netelem +
                                          ".vm_type} variable not present in testbed resource file.")

            netelem_vm_dict[vm_name] = {"vm_server": vm_server,
                                        "vm_name": vm_name,
                                        "vm_wait": vm_wait,
                                        "vm_type": vm_type,
                                        "vm_id": vm_id}
        return netelem_vm_dict
