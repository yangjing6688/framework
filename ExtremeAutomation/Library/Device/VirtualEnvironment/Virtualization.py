import abc


class Virtualization(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def wait_for_vm_state(self, vm_name, vm_state, timeout=60):
        """
        This command will wait for a VM to be in a given state for up to <timeout> seconds and continue on if state
        is reached before the given timeout.

        If <timeout> is exceeded this will fail and continue on.

        vm_name:  The VM name
        vm_state: The VM state that is needed
        timeout:  Number of seconds to wait for VM to be in paused state. Default set to 60s.
        """
        pass

    @abc.abstractmethod
    def terminate(self):
        """
        Stops the VirtualBox instance.
        """
        pass

    @abc.abstractmethod
    def get_initialized(self):
        """
        Returns the init status of the VM host instance.
        """
        pass

    @abc.abstractmethod
    def start_vm(self, machine_name, machine_type, rdp):
        """
        Boots-up the Virtual Machine.
        """
        pass

    @abc.abstractmethod
    def power_down_vm(self, machine_name):
        """
        Forcefully powers off the Virtual Machine.
        """
        pass

    @abc.abstractmethod
    def power_down_vm_power_button(self, machine_name):
        """
        Attempts to gracefully shutdown the Virtual Machine.
        """
        pass

    @abc.abstractmethod
    def set_link_state(self, machine_name, link_state, adapter_id):
        """
        Sets the Virtual Machine NIC's link state.
        """
        pass

    @abc.abstractmethod
    def reset_vm(self, machine_name):
        """
        Reboots the Virtual Machine.
        """
        pass

    @abc.abstractmethod
    def pause_vm(self, machine_name):
        """
        Pauses the current Virtual Machine state.
        """
        pass

    @abc.abstractmethod
    def resume_vm(self, machine_name):
        """
        Resumes the state of a paused Virtual Machine.
        """
        pass

    @abc.abstractmethod
    def save_vm_state(self, machine_name):
        """
        Saves the current Virtual Machine state.
        """
        pass

    @abc.abstractmethod
    def set_credentials(self, machine_name, user_name, password, domain):
        """
        Sets the login credentials and domain for the Virtual Machine.
        """
        pass

    @abc.abstractmethod
    def get_all_vms(self):
        """
        Returns all Virtual Machines configured on the VirtualBox server.
        """
        pass

    @abc.abstractmethod
    def get_vm_state(self, machine_name):
        """
        Returns the current state of the Virtual Machine, on or off.
        """
        pass

    @abc.abstractmethod
    def take_vm_snapshot(self, machine_name, snapshot_name):
        """
        Saves a snapshot of the Virtual Machine's current state.
        """
        pass

    @abc.abstractmethod
    def delete_vm_snapshot(self, machine_name, snapshot_name):
        """
        Deletes a saved Virtual Machine snapshot.
        """
        pass

    @abc.abstractmethod
    def restore_vm_snapshot(self, machine_name, snapshot_name):
        """
        Reverts a Virtual Machine to a previously saved snapshot.
        """
        pass

    @abc.abstractmethod
    def restore_to_current_vm_snapshot(self, machine_name, snapshot_name):
        """
        Reverts a Virtual Machine to the currently in-use snapshot.
        """
        pass

    @abc.abstractmethod
    def print_all_snapshots(self, machine_name, snapshot_list=None):
        """
        Returns all snapshots saved for the Virtual Machine.
        """
        pass

    @abc.abstractmethod
    def delete_vm(self, machine_name):
        """
        Permanently removes the Virtual Machine from the VirtualBox server.
        """
        pass
