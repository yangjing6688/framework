import time
import requests
import urllib3
import ssl
from urllib3.exceptions import InsecureRequestWarning
from ExtremeAutomation.Library.Utils.JsonUtils import JsonUtils
from ExtremeAutomation.Library.Device.VirtualEnvironment.CommandDataBean import CommandDataBean
from ExtremeAutomation.Library.Device.VirtualEnvironment.Virtualization import Virtualization
from ExtremeAutomation.Library.Device.VirtualEnvironment.Constants.VirtualConstants import VirtualConstants
from ExtremeAutomation.Library.Device.Common.RestCommonLib import RestCommonLib
from ExtremeAutomation.Library.Logger.Logger import Logger
from ExtremeAutomation.Keywords.Utils.KeywordUtils import KeywordUtils


def create_instance(virtual_machine):
    return VirtualBaseApi(virtual_machine.hostname, virtual_machine.port, virtual_machine.username,
                          virtual_machine.password)


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

    def __init__(self, ip_address, port, user_name, password):
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

        self.access_token = RestCommonLib.getOauthToken('testengineuser',
                                                        '@utom@tionTe$tEngineU$er',
                                                        ip_address,
                                                        9016)

        ssl._create_default_https_context = ssl._create_unverified_context
        urllib3.disable_warnings(InsecureRequestWarning)

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
        data = CommandDataBean()
        data.password = self.vbox_password
        data.username = self.vbox_user_name
        data.cmd = "VBoxManage modifyvm " + machine_name + " --nic" + nic_number + " intnet --intnet" + nic_number \
                   + " " + internal_network_name + " --macaddress" + nic_number + " " + mac_address + \
                   " --nicpromisc" + nic_number + " allow-all"
        self.logger.log_info(str(data.cmd))
        return_value = self._send_post_vm_command(data)

        return return_value

    # Never got a command for this one, they may not be using it...
    def get_internal_network_name(self, machine_name, nic_number):
        """
        Returns the Virtual Machine NIC's LAN segment.
        """
        data = CommandDataBean()
        data.password = self.vbox_password
        data.username = self.vbox_user_name
        data.cmd = "VBoxManage modifyvm " + machine_name + " --nic " + nic_number
        self.logger.log_info(str(data.cmd))
        return_value = self._send_post_vm_command(data)

        return return_value

    def turn_on_rdp_for_vm(self, machine_name):
        """
        Enables the Virtual Remote Desktop Environment for the Virtual Machine.
        """
        data = CommandDataBean()
        data.password = self.vbox_password
        data.username = self.vbox_user_name
        data.cmd = " VBoxManage modifyvm " + machine_name + " --vrde on "
        self.logger.log_info(str(data.cmd))
        return_value = self._send_post_vm_command(data)
        return return_value

    def start_vm(self, machine_name, vm_type='headless', **kwargs):
        """
        Boots-up the Virtual Machine in headless mode.
        """
        data = CommandDataBean()
        data.password = self.vbox_password
        data.username = self.vbox_user_name
        data.cmd = " VBoxManage startvm " + machine_name + " --type " + vm_type
        self.logger.log_info(str(data.cmd))
        return_value = self._send_post_vm_command(data)

        return return_value

    def power_down_vm(self, machine_name, **kwargs):
        """
        Forcefully powers off the Virtual Machine.
        """
        data = CommandDataBean()
        data.password = self.vbox_password
        data.username = self.vbox_user_name
        data.cmd = " VBoxManage controlvm " + machine_name + " poweroff"
        self.logger.log_info(str(data.cmd))
        return_value = self._send_post_vm_command(data)

        return return_value

    def power_down_vm_power_button(self, machine_name):
        """
        Attempts to gracefully shutdown the Virtual Machine.
        """
        data = CommandDataBean()
        data.password = self.vbox_password
        data.username = self.vbox_user_name
        data.cmd = " VBoxManage controlvm " + machine_name + " acpipowerbutton"
        self.logger.log_info(str(data.cmd))
        return_value = self._send_post_vm_command(data)

        return return_value

    def set_link_state(self, machine_name, link_state, adapter_id):
        """
        Sets the Virtual Machine NIC's link state.
        """
        data = CommandDataBean()
        data.password = self.vbox_password
        data.username = self.vbox_user_name
        data.cmd = " VBoxManage controlvm " + machine_name + " setlinkstate " + adapter_id + " " + link_state
        self.logger.log_info(str(data.cmd))
        return_value = self._send_post_vm_command(data)

        return return_value

    def set_nic_card_state(self, machine_name, adapter_id, state="on"):
        """
        Sets the NIC state.
        """
        if state != "on" or state != "off":
            self.logger.log_info("Invalid state " + state + ". Defaulting to \'on\'.")
            state = "on"
        data = CommandDataBean()
        data.password = self.vbox_password
        data.username = self.vbox_user_name
        #  This currently sets the nic to 'none', regardless of the given state variable.
        data.cmd = "VBoxManage modifyvm " + machine_name + " --cableconnected" + str(adapter_id) + " " + state
        self.logger.log_info(data.cmd)
        return_value = self._send_post_vm_command(data)

        return return_value

    def reset_vm(self, machine_name):
        """
        Reboots the Virtual Machine.
        """
        data = CommandDataBean()
        data.password = self.vbox_password
        data.username = self.vbox_user_name
        data.cmd = " VBoxManage controlvm " + machine_name + " reset"
        self.logger.log_info(str(data.cmd))
        return_value = self._send_post_vm_command(data)

        return return_value

    def pause_vm(self, machine_name):
        """
        Pauses the current Virtual Machine state.
        """
        data = CommandDataBean()
        data.password = self.vbox_password
        data.username = self.vbox_user_name
        data.cmd = " VBoxManage controlvm " + machine_name + " pause"
        self.logger.log_info(str(data.cmd))
        return_value = self._send_post_vm_command(data)

        return return_value

    def resume_vm(self, machine_name):
        """
        Resumes the state of a paused Virtual Machine.
        """
        data = CommandDataBean()
        data.password = self.vbox_password
        data.username = self.vbox_user_name
        data.cmd = " VBoxManage controlvm " + machine_name + " resume"
        self.logger.log_info(str(data.cmd))
        return_value = self._send_post_vm_command(data)

        return return_value

    def save_vm_state(self, machine_name):
        """
        Saves the current Virtual Machine state.
        """
        data = CommandDataBean()
        data.password = self.vbox_password
        data.username = self.vbox_user_name
        data.cmd = " VBoxManage controlvm " + machine_name + " savestate"
        self.logger.log_info(str(data.cmd))
        return_value = self._send_post_vm_command(data)

        return return_value

    def set_credentials(self, machine_name, user_name, password, domain):
        """
        Sets the login credentials and domain for the Virtual Machine.
        """
        data = CommandDataBean()
        data.password = self.vbox_password
        data.username = self.vbox_user_name
        data.cmd = " VBoxManage controlvm " + machine_name + " " + user_name + " " + password + " " + domain
        self.logger.log_info(str(data.cmd))
        return_value = self._send_post_vm_command(data)

        return return_value

    def get_all_vms(self):
        """
        Returns all Virtual Machines configured on the VirtualBox server.
        """
        data = CommandDataBean()
        data.password = self.vbox_password
        data.username = self.vbox_user_name
        data.cmd = " VBoxManage list vms"
        self.logger.log_info(str(data.cmd))
        return_value = self._send_post_vm_command(data)

        return return_value

    def get_vm_state(self, machine_name):
        """
        Returns the current state of the Virtual Machine, on or off.
        """
        data = CommandDataBean()
        data.password = self.vbox_password
        data.username = self.vbox_user_name
        data.cmd = " VBoxManage list runningvms"
        self.logger.log_info(data.cmd)
        return_value = self._send_post_vm_command(data).decode('ascii')

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
        data = CommandDataBean()
        data.password = self.vbox_password
        data.username = self.vbox_user_name
        data.cmd = " VBoxManage snapshot " + machine_name + " take " + snapshot_name
        self.logger.log_info(str(data.cmd))
        return_value = self._send_post_vm_command(data)

        return return_value

    def delete_vm_snapshot(self, machine_name, snapshot_name):
        """
        Deletes a saved Virtual Machine snapshot.
        """
        data = CommandDataBean()
        data.password = self.vbox_password
        data.username = self.vbox_user_name
        data.cmd = " VBoxManage snapshot " + machine_name + " delete " + snapshot_name
        self.logger.log_info(str(data.cmd))
        return_value = self._send_post_vm_command(data)

        return return_value

    def restore_vm_snapshot(self, machine_name, snapshot_name):
        """
        Reverts a Virtual Machine to a previously saved snapshot.
        """
        data = CommandDataBean()
        data.password = self.vbox_password
        data.username = self.vbox_user_name
        data.cmd = " VBoxManage snapshot " + machine_name + " restore " + snapshot_name
        self.logger.log_info(str(data.cmd))
        return_value = self._send_post_vm_command(data)

        return return_value

    def restore_to_current_vm_snapshot(self, machine_name, snapshot_name):
        """
        Reverts a Virtual Machine to the currently in-use snapshot.
        """
        data = CommandDataBean()
        data.password = self.vbox_password
        data.username = self.vbox_user_name
        data.cmd = " VBoxManage snapshot " + machine_name + " restorecurrent " + snapshot_name
        self.logger.log_info(str(data.cmd))
        return_value = self._send_post_vm_command(data)

        return return_value

    def delete_vm(self, machine_name):
        """
        Permanently removes the Virtual Machine from the VirtualBox server.
        """
        data = CommandDataBean()
        data.password = self.vbox_password
        data.username = self.vbox_user_name
        data.cmd = "VBoxManage unregistervm " + machine_name + " --delete "
        self.logger.log_info(str(data.cmd))
        return_value = self._send_post_vm_command(data)

        return return_value

    def shared_folder_config(self, machine_name, folder_name, host_path="", add_remove="add", automount=True):
        """
        Configures a shared folder on the VirtualBox server for the Virtual Machine.
        """
        data = CommandDataBean()
        data.password = self.vbox_password
        data.username = self.vbox_user_name
        mount = " --automount" if automount is True else ""
        if str(add_remove) == "add":
            data.cmd = "VBoxManage sharedfolder add " + machine_name + " --name " + str(folder_name) + \
                       " --hostpath " + str(host_path) + str(mount)
        else:
            data.cmd = "VBoxManage sharedfolder remove " + machine_name + " --name " + str(folder_name)
        self.logger.log_info(data.cmd)
        return_value = self._send_post_vm_command(data)

        return return_value

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
        data = CommandDataBean()
        data.password = self.vbox_password
        data.username = self.vbox_user_name
        data.cmd = "dir"
        self.logger.log_info(str(data.cmd))
        return_value = self._send_post_vm_command(data)
        return return_value

    def _send_post_vm_command(self, json):
        url = "https://" + self.vbox_server_ip_address + ":" + self.vbox_server_port + "/vm/v1/command"
        headers = {'Accept': 'application/json',
                   'Content-Type': 'application/json',
                   'Authorization': 'Bearer ' + self.access_token}
        file_content = JsonUtils.convert_to_json(json, False)

        self.logger.log_info('Send :' + url)
        result = requests.post(url, json=file_content, headers=headers, verify=False)
        if result is not None:
            return result.content
        else:
            return None
