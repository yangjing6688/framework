import time
from ExtremeAutomation.Library.Logger.Logger import Logger
from ExtremeAutomation.Keywords.Utils.KeywordUtils import KeywordUtils
from ExtremeAutomation.Library.Device.VirtualEnvironment.Virtualization import Virtualization
from ExtremeAutomation.Library.Device.VirtualEnvironment.Constants.VirtualConstants import VirtualConstants
from ExtremeAutomation.Keywords.Utils.DeviceCollectionManager import DeviceCollectionManager


def create_instance(virtual_machine):
    return VirtualBaseApi(virtual_machine.hostname, virtual_machine.port, virtual_machine.username,
                          virtual_machine.password, virtual_machine.name)


class VirtualBaseApi(Virtualization):
    VBOX_STATUS_PREFIX = "VirtualBox Status: "
    vbox_server_ip_address = ""
    vbox_server_port = ""
    vbox_user_name = ""
    vbox_password = ""
    vbox_java_process = None
    vbox_mgr = None
    vbox_box = None
    vbox_initialized = False

    def __init__(self, ip_address, port, user_name, password, name):
        self.logger = Logger()
        self.gateway_active = False
        self.vbox_server_ip_address = ip_address
        self.vbox_server_port = port
        self.vbox_user_name = user_name
        self.vbox_password = password
        self.java_lib = None
        self.vbox_mgr = None
        self.vbox_box = None
        self.vbox_initialized = True
        self.server_name = name
        self.dev_collection = DeviceCollectionManager()

    def get_initialized(self):
        """
        Returns the init status of the VirtualBox instance.
        """
        return self.vbox_initialized

    # Never got a command for this one, they may not be using it, or it could be that there is no command line command
    # as this appears to just kill a process
    def terminate(self):
        """
        Stops the VirtualBox instance.
        """
        pass
        # return return_value

    def provision_vm_nic_settings(self, machine_name, nic_number, internal_network_name, mac_address):
        """
        Configures the Virtual Machine NIC's LAN segment and MAC address.
        """
        nic_number = str(nic_number)
        cmd = "VBoxManage modifyvm " + machine_name + " --nic" + nic_number + " intnet --intnet" + nic_number + \
              " " + internal_network_name + " --macaddress" + nic_number + " " + mac_address + \
              " --nicpromisc" + nic_number + " allow-all"
        self.logger.log_info(cmd)
        return self._send_vm_command(cmd)

    # Never got a command for this one, they may not be using it...
    def get_internal_network_name(self, machine_name, nic_number):
        """
        Returns the Virtual Machine NIC's LAN segment.
        """
        cmd = "VBoxManage modifyvm " + machine_name + " --nic " + nic_number
        self.logger.log_info(cmd)
        return self._send_vm_command(cmd)

    def turn_on_rdp_for_vm(self, machine_name):
        """
        Enables the Virtual Remote Desktop Environment for the Virtual Machine.
        """
        cmd = " VBoxManage modifyvm " + machine_name + " --vrde on "
        self.logger.log_info(cmd)
        return self._send_vm_command(cmd)

    def start_vm(self, machine_name, vm_type='headless', **kwargs):
        """
        Boots-up the Virtual Machine in headless mode.
        """
        cmd = " VBoxManage startvm " + machine_name + " --type " + vm_type
        self.logger.log_info(cmd)
        return self._send_vm_command(cmd)

    def power_down_vm(self, machine_name, **kwargs):
        """
        Forcefully powers off the Virtual Machine.
        """
        cmd = " VBoxManage controlvm " + machine_name + " poweroff"
        self.logger.log_info(cmd)
        return self._send_vm_command(cmd)

    def power_down_vm_power_button(self, machine_name):
        """
        Attempts to gracefully shutdown the Virtual Machine.
        """
        cmd = " VBoxManage controlvm " + machine_name + " acpipowerbutton"
        self.logger.log_info(cmd)
        return self._send_vm_command(cmd)

    def set_link_state(self, machine_name, link_state, adapter_id):
        """
        Sets the Virtual Machine NIC's link state.
        """
        cmd = " VBoxManage controlvm " + machine_name + " setlinkstate " + adapter_id + " " + link_state
        self.logger.log_info(cmd)
        return self._send_vm_command(cmd)

    def set_nic_card_state(self, machine_name, adapter_id, state="on"):
        """
        Sets the NIC state.
        """
        if state != "on" or state != "off":
            self.logger.log_info("Invalid state " + state + ". Defaulting to \'on\'.")
            state = "on"
        #  This currently sets the nic to 'none', regardless of the given state variable.
        cmd = "VBoxManage modifyvm " + machine_name + " --cableconnected" + str(adapter_id) + " " + state
        self.logger.log_info(cmd)
        return self._send_vm_command(cmd)

    def reset_vm(self, machine_name):
        """
        Reboots the Virtual Machine.
        """
        cmd = " VBoxManage controlvm " + machine_name + " reset"
        self.logger.log_info(cmd)
        return self._send_vm_command(cmd)

    def pause_vm(self, machine_name):
        """
        Pauses the current Virtual Machine state.
        """
        cmd = " VBoxManage controlvm " + machine_name + " pause"
        self.logger.log_info(cmd)
        return self._send_vm_command(cmd)

    def resume_vm(self, machine_name):
        """
        Resumes the state of a paused Virtual Machine.
        """
        cmd = " VBoxManage controlvm " + machine_name + " resume"
        self.logger.log_info(cmd)
        return self._send_vm_command(cmd)

    def save_vm_state(self, machine_name):
        """
        Saves the current Virtual Machine state.
        """
        cmd = " VBoxManage controlvm " + machine_name + " savestate"
        self.logger.log_info(cmd)
        return self._send_vm_command(cmd)

    def set_credentials(self, machine_name, user_name, password, domain):
        """
        Sets the login credentials and domain for the Virtual Machine.
        """
        cmd = " VBoxManage controlvm " + machine_name + " " + user_name + " " + password + " " + domain
        self.logger.log_info(cmd)
        return self._send_vm_command(cmd)

    def get_all_vms(self):
        """
        Returns all Virtual Machines configured on the VirtualBox server.
        """
        cmd = " VBoxManage list vms"
        self.logger.log_info(cmd)
        return self._send_vm_command(cmd)

    def get_vm_state(self, machine_name):
        """
        Returns the current state of the Virtual Machine, on or off.
        """
        cmd = " VBoxManage list runningvms"
        self.logger.log_info(cmd)
        return_value = self._send_vm_command(cmd)

        # If machine names is found in returned output then the vm is running
        # else it is poweredOff
        if return_value.find(str(machine_name)) != -1:
            vm_state = VirtualConstants.VM_STATE_POWERED_ON
        else:
            vm_state = VirtualConstants.VM_STATE_POWERED_OFF

        return vm_state

    def take_vm_snapshot(self, machine_name, snapshot_name):
        """
        Saves a snapshot of the Virtual Machine's current state.
        """
        cmd = " VBoxManage snapshot " + machine_name + " take " + snapshot_name
        self.logger.log_info(cmd)
        return self._send_vm_command(cmd)

    def delete_vm_snapshot(self, machine_name, snapshot_name):
        """
        Deletes a saved Virtual Machine snapshot.
        """
        cmd = " VBoxManage snapshot " + machine_name + " delete " + snapshot_name
        self.logger.log_info(cmd)
        return self._send_vm_command(cmd)

    def restore_vm_snapshot(self, machine_name, snapshot_name):
        """
        Reverts a Virtual Machine to a previously saved snapshot.
        """
        cmd = " VBoxManage snapshot " + machine_name + " restore " + snapshot_name
        self.logger.log_info(cmd)
        return self._send_vm_command(cmd)

    def restore_to_current_vm_snapshot(self, machine_name, snapshot_name):
        """
        Reverts a Virtual Machine to the currently in-use snapshot.
        """
        cmd = " VBoxManage snapshot " + machine_name + " restorecurrent " + snapshot_name
        self.logger.log_info(cmd)
        return self._send_vm_command(cmd)

    def delete_vm(self, machine_name):
        """
        Permanently removes the Virtual Machine from the VirtualBox server.
        """
        cmd = "VBoxManage unregistervm " + machine_name + " --delete "
        self.logger.log_info(cmd)
        return self._send_vm_command(cmd)

    def shared_folder_config(self, machine_name, folder_name, host_path="", add_remove="add", automount=True):
        """
        Configures a shared folder on the VirtualBox server for the Virtual Machine.
        """
        mount = " --automount" if automount is True else ""
        if str(add_remove) == "add":
            cmd = "VBoxManage sharedfolder add " + machine_name + " --name " + str(folder_name) + \
                  " --hostpath " + str(host_path) + str(mount)
        else:
            cmd = "VBoxManage sharedfolder remove " + machine_name + " --name " + str(folder_name)
        self.logger.log_info(cmd)
        return self._send_vm_command(cmd)

    # Never got a command for this one, they may not be using it...
    def print_all_snapshots(self, machine_name, snapshot_list=None):
        """
        Returns all snapshots saved for the Virtual Machine.
        """
        pass

    def wait_for_vm_state(self, vm_name, vm_state, timeout=60):
        """
        This command will wait for a VM to be in a given state for up to <timeout> seconds and continue on if state
        is reached before the given timeout.

        If <timeout> is exceeded this will fail and continue on.

        vm_name:  The VM name
        vm_state: The VM state that is needed
        timeout:  Number of seconds to wait for VM to be in paused state. Default set to 60s.
        """
        if vm_state == VirtualConstants.VM_STATE_POWERED_ON:
            vm_state = "PoweredOn"
        elif vm_state == VirtualConstants.VM_STATE_POWERED_OFF:
            vm_state = "PoweredOff"

        start_time = time.time()
        while True:
            if time.time() - start_time > timeout:
                self.logger.log_info("Error: Timeout before vm state [" + vm_state + "] was reached")
                break
            else:
                new_vm_state = self.get_vm_state(vm_name)
                if str(vm_state) == new_vm_state:
                    KeywordUtils.log_running_keyword(" - Machine is " + vm_state)
                    break
            time.sleep(1)
            KeywordUtils.log_running_keyword(("- Waiting for the virtual machine " + vm_name + " to be in the " +
                                              vm_state + "state. " + " Elapsed time: " +
                                              str(int(time.time() - start_time))))

    def send_test_command(self):
        """
        Returns the output from a 'dir' command on the Virtual Machine.
        """
        cmd = "dir"
        self.logger.log_info(cmd)
        return_value = self._send_vm_command(cmd)
        return return_value

    def _send_vm_command(self, cmd):
        device = self.dev_collection.get_device(self.server_name)
        device.current_agent.write(cmd + "\n")
        result = device.current_agent.wait_no_parse(1000, 1)
        self.logger.log_info(result)
        return result
