import atexit
import ssl
import time

from pyVim import connect
# It appears that the vmodl and vim module are lazily loaded, so pycharm will show an error here.
# noinspection PyUnresolvedReferences
from pyVmomi import vim
# noinspection PyUnresolvedReferences
from pyVmomi import vmodl
from ExtremeAutomation.Library.Logger.Logger import Logger
from ExtremeAutomation.Library.Device.VirtualEnvironment.Virtualization import Virtualization
from ExtremeAutomation.Library.Device.VirtualEnvironment.Constants.VirtualConstants import VirtualConstants


def create_instance(virtual_machine):
    return VirtualBaseApi(virtual_machine.hostname, virtual_machine.port, virtual_machine.username,
                          virtual_machine.password)


class VirtualBaseApi(Virtualization):
    vm_ware_server_ip_address = ""
    vm_ware_server_user_name = ""
    vm_ware_server_password = ""
    vm_ware_server_port = -1
    vm_ware_service_instance = None
    vm_name_uuid_map = {}
    virtual_machines = None

    def __init__(self, ip_address, port, user_name, password):
        self.vm_ware_server_ip_address = ip_address
        self.vm_ware_server_port = port
        self.vm_ware_server_user_name = user_name
        self.vm_ware_server_password = password

        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE

        self.vm_ware_service_instance = connect.SmartConnect(host=self.vm_ware_server_ip_address,
                                                             user=self.vm_ware_server_user_name,
                                                             pwd=self.vm_ware_server_password,
                                                             sslContext=context)

        atexit.register(connect.Disconnect, self.vm_ware_service_instance)
        self.retrieve_virtual_machines()
        self.initialized = True
        self.logger = Logger()

    def get_initialized(self):
        """
        Returns the init status of the VMWare instance.
        """
        return self.initialized

    def retrieve_virtual_machines(self):
        """
        Returns all Virtual Machines configured on the VMWare server.
        """
        content = self.vm_ware_service_instance.RetrieveContent()
        container = content.rootFolder
        viewType = [vim.VirtualMachine]
        recursive = True
        containerView = content.viewManager.CreateContainerView(container, viewType, recursive)
        self.virtual_machines = containerView.view

        for vm in self.virtual_machines:
            summary = vm.summary
            vm_name = summary.config.name
            vm_uuid = summary.config.instanceUuid
            # print vm_name
            self.vm_name_uuid_map[vm_name] = vm_uuid

    def get_vm_uuid_by_vm_name(self, uuid):
        """
        Returns the Virtual Machine name, from the UUID.
        """
        return self.vm_name_uuid_map.get(uuid)

    def start_vm(self, machine_name, machine_type=None, **kwargs):
        """
        Boots-up the Virtual Machine.
        """
        uuid = self.get_vm_uuid_by_vm_name(machine_name)
        virtual_machine = self.vm_ware_service_instance.content.searchIndex.FindByUuid(None, uuid, True, True)
        task = virtual_machine.PowerOnVM_Task()
        self.wait_for_tasks([task])
        self.logger.log_debug("[" + self.vm_ware_server_ip_address + "] Successfully started VM Name: " +
                              machine_name)
        return "[" + self.vm_ware_server_ip_address + "] Successfully started VM Name: " + machine_name

    def power_down_vm(self, machine_name):
        """
        Forcefully powers off the Virtual Machine.
        """
        uuid = self.get_vm_uuid_by_vm_name(machine_name)
        virtual_machine = self.vm_ware_service_instance.content.searchIndex.FindByUuid(None, uuid, True, True)
        task = virtual_machine.ShutdownGuest()
        self.wait_for_tasks([task])
        self.logger.log_debug("[" + self.vm_ware_server_ip_address + "] Successfully shut down VM Name: " +
                              machine_name)
        return "[" + self.vm_ware_server_ip_address + "] Successfully shut down VM Name: " + machine_name

    def power_down_vm_power_button(self, machine_name):
        """
        Attempts to gracefully shutdown the Virtual Machine.
        """
        uuid = self.get_vm_uuid_by_vm_name(machine_name)
        virtual_machine = self.vm_ware_service_instance.content.searchIndex.FindByUuid(None, uuid, True, True)
        task = virtual_machine.PowerOffVM_Task()
        self.wait_for_tasks([task])
        self.logger.log_debug("[" + self.vm_ware_server_ip_address + "] Successfully hard powered down VM Name: " +
                              machine_name)
        return "[" + self.vm_ware_server_ip_address + "] Successfully hard powered down VM Name: " + machine_name

    def reset_vm(self, machine_name):
        """
        Reboots the Virtual Machine.
        """
        uuid = self.get_vm_uuid_by_vm_name(machine_name)
        virtual_machine = self.vm_ware_service_instance.content.searchIndex.FindByUuid(None, uuid, True, True)
        task = virtual_machine.ResetVM_Task()
        self.wait_for_tasks([task])
        self.logger.log_debug("[" + self.vm_ware_server_ip_address + "] Successfully reset VM Name: " +
                              machine_name)
        return "[" + self.vm_ware_server_ip_address + "] Successfully reset VM Name: " + machine_name

    def pause_vm(self, machine_name):
        """
        Pauses the current Virtual Machine state.
        """
        uuid = self.get_vm_uuid_by_vm_name(machine_name)
        virtual_machine = self.vm_ware_service_instance.content.searchIndex.FindByUuid(None, uuid, True, True)
        task = virtual_machine.SuspendVM_Task()
        self.wait_for_tasks([task])
        self.logger.log_debug("[" + self.vm_ware_server_ip_address + "] Successfully paused (standby) VM Name: " +
                              machine_name)
        return "[" + self.vm_ware_server_ip_address + "] Successfully paused (standby) VM Name: " + machine_name

    def resume_vm(self, machine_name):
        """
        Resumes the state of a paused Virtual Machine.
        """
        self.start_vm(machine_name)
        self.logger.log_debug("[" + self.vm_ware_server_ip_address + "] Successfully resumed VM Name: " +
                              machine_name)
        return "[" + self.vm_ware_server_ip_address + "] Successfully resumed VM Name: " + machine_name

    def set_link_state(self, machine_name, link_state, adapter_id):
        """
        Sets the Virtual Machine NIC's link state.
        """
        return

    def save_vm_state(self, machine_name):
        """
        Saves the current Virtual Machine state.
        """
        return

    def set_credentials(self, machine_name, user_name, password, domain):
        """
        Sets the login credentials and domain for the Virtual Machine.
        """
        return

    def get_all_vms(self):
        """
        Returns all Virtual Machines configured on the VirtualBox server.
        """
        return self.virtual_machines

    def get_vm_state(self, machine_name):
        """
        Returns the current state of the Virtual Machine, on or off.
        """
        uuid = self.get_vm_uuid_by_vm_name(machine_name)
        virtual_machine = self.vm_ware_service_instance.content.searchIndex.FindByUuid(None, uuid, True, True)
        vm_state = virtual_machine.summary.runtime.powerState

        if vm_state == "poweredOn":
            vm_state = VirtualConstants.VM_STATE_POWERED_ON
        elif vm_state == "poweredOff":
            vm_state = VirtualConstants.VM_STATE_POWERED_OFF

        self.logger.log_debug("[" + self.vm_ware_server_ip_address + "] VM State: " + vm_state + " for VM Name: " +
                              machine_name)
        return vm_state

    def take_vm_snapshot(self, machine_name, snapshot_name):
        """
        Saves a snapshot of the Virtual Machine's current state.
        """
        uuid = self.get_vm_uuid_by_vm_name(machine_name)
        virtual_machine = self.vm_ware_service_instance.content.searchIndex.FindByUuid(None, uuid, True, True)
        task = virtual_machine.CreateSnapshot_Task(snapshot_name, snapshot_name, False, False)
        self.wait_for_tasks([task])
        self.logger.log_debug("[" + self.vm_ware_server_ip_address + "] Successfully created snapshot '" +
                              snapshot_name + " for VM Name: " + machine_name)
        return "[" + self.vm_ware_server_ip_address + "] Successfully created snapshot '" + snapshot_name + \
               " for VM Name: " + machine_name

    def print_all_snapshots(self, machine_name, snapshot_list=None):
        """
        Returns all snapshots saved for the Virtual Machine.
        """
        if snapshot_list is None:
            uuid = self.get_vm_uuid_by_vm_name(machine_name)
            vm = self.vm_ware_service_instance.content.searchIndex.FindByUuid(None, uuid, True, True)
            snapshot_info = vm.snapshot
            snapshot_root_tree = snapshot_info.rootSnapshotList
            snapshot_list = snapshot_root_tree[0].childSnapshotList

        if snapshot_list is not None:
            for snapshot in snapshot_list:
                self.logger.log_info(snapshot.name)
                child_snapshot_list = snapshot.childSnapshotList
                if len(child_snapshot_list) > 0:
                    self.print_all_snapshots(machine_name, child_snapshot_list)

        return

    def get_snapshot_by_vm_and_snapshot_name(self, machine_name, snapshot_name, snapshot_list=None):
        """
        Returns the snapshot name if it exists for the Virtual Machine.
        """
        return_snapshot = None

        uuid = self.get_vm_uuid_by_vm_name(machine_name)
        vm = self.vm_ware_service_instance.content.searchIndex.FindByUuid(None, uuid, True, True)

        if snapshot_list is None:
            snapshot_list = vm.snapshot.rootSnapshotList

        for snapshot in snapshot_list:
            if snapshot_name == snapshot.name:
                return_snapshot = snapshot.snapshot
                break
            else:
                child_snapshot_list = snapshot.childSnapshotList
                return_snapshot = self.get_snapshot_by_vm_and_snapshot_name(machine_name, snapshot_name,
                                                                            child_snapshot_list)

        return return_snapshot

    def delete_vm_snapshot(self, machine_name, snapshot_name):
        """
        Deletes a saved Virtual Machine snapshot.
        """
        snapshot = self.get_snapshot_by_vm_and_snapshot_name(machine_name, snapshot_name)

        if snapshot is not None:
            snapshot.RemoveSnapshot_Task(True)
            self.logger.log_debug("[" + self.vm_ware_server_ip_address + "] Successfully deleted snapshot '" +
                                  snapshot_name + "' from VM '" + machine_name + "'.")
            return "[" + self.vm_ware_server_ip_address + "] Successfully deleted snapshot '" + snapshot_name + \
                   "' from VM '" + machine_name + "'."
        else:
            self.logger.log_debug("[" + self.vm_ware_server_ip_address + "] Could not fine snapshot '" +
                                  snapshot_name + "' on VM '" + machine_name + "'.")
            return "[" + self.vm_ware_server_ip_address + "] Could not fine snapshot '" + snapshot_name + \
                   "' on VM '" + machine_name + "'."

    def restore_vm_snapshot(self, machine_name, snapshot_name):
        """
        Reverts a Virtual Machine to a previously saved snapshot.
        """
        snapshot = self.get_snapshot_by_vm_and_snapshot_name(machine_name, snapshot_name)

        if snapshot is not None:
            task = snapshot.RevertToSnapshot_Task()
            self.wait_for_tasks([task])
            self.logger.log_debug("[" + self.vm_ware_server_ip_address + "] Successfully restored the snapshot '" +
                                  snapshot_name + "' from VM '" + machine_name + "'.")
            return "[" + self.vm_ware_server_ip_address + "] Successfully restored the snapshot '" + snapshot_name + \
                   "' from VM '" + machine_name + "'."
        else:
            self.logger.log_debug("[" + self.vm_ware_server_ip_address + "] Could not fine snapshot '" +
                                  snapshot_name + "' on VM '" + machine_name + "'.")
            return "[" + self.vm_ware_server_ip_address + "] Could not fine snapshot '" + snapshot_name + \
                   "' on VM '" + machine_name + "'."

    def restore_to_current_vm_snapshot(self, machine_name, snapshot_name):
        """
        Reverts a Virtual Machine to the currently in-use snapshot.
        """
        uuid = self.get_vm_uuid_by_vm_name(machine_name)
        virtual_machine = self.vm_ware_service_instance.content.searchIndex.FindByUuid(None, uuid, True, True)
        task = virtual_machine.RevertToCurrentSnapshot_Task()
        self.wait_for_tasks([task])
        self.logger.log_debug("[" + self.vm_ware_server_ip_address +
                              "] Successfully restored to current snapshot for VM Name: " + machine_name)
        return "Successfully restored to current snapshot for VM Name: " + machine_name

    def delete_vm(self, machine_name):
        """
        Permanently removes the Virtual Machine from the VirtualBox server.
        """
        uuid = self.get_vm_uuid_by_vm_name(machine_name)
        if uuid is None:
            virtual_machine = self.vm_ware_service_instance.content.searchIndex.FindByUuid(None, uuid, True, True)
            task = virtual_machine.Destroy_Task()
            self.wait_for_tasks([task])
            self.logger.log_debug("[" + self.vm_ware_server_ip_address + "] Successfully deleted VM Name: " +
                                  machine_name)
            return "[" + self.vm_ware_server_ip_address + "] Successfully deleted VM Name: " + machine_name
        else:
            self.logger.log_debug("[" + self.vm_ware_server_ip_address + "] Could not find the VM Name: " +
                                  machine_name)
            return "[" + self.vm_ware_server_ip_address + "] Could not find the VM Name: " + machine_name

    def wait_for_tasks(self, tasks):
        """
        Given the service instance si and tasks, it returns after all the
        tasks are complete
        """
        property_collector = self.vm_ware_service_instance.content.propertyCollector
        task_list = [str(task) for task in tasks]
        # Create filter
        obj_specs = [vmodl.query.PropertyCollector.ObjectSpec(obj=task)
                     for task in tasks]
        property_spec = vmodl.query.PropertyCollector.PropertySpec(type=vim.Task,
                                                                   pathSet=[],
                                                                   all=True)
        filter_spec = vmodl.query.PropertyCollector.FilterSpec()
        filter_spec.objectSet = obj_specs
        filter_spec.propSet = [property_spec]
        pcfilter = property_collector.CreateFilter(filter_spec, True)

        try:
            version, state = None, None
            # Loop looking for updates till the state moves to a completed state.
            while len(task_list):
                update = property_collector.WaitForUpdates(version)
                for filter_set in update.filterSet:
                    for obj_set in filter_set.objectSet:
                        task = obj_set.obj
                        for change in obj_set.changeSet:
                            if change.name == 'info':
                                state = change.val.state
                            elif change.name == 'info.state':
                                state = change.val
                            else:
                                continue

                            if not str(task) in task_list:
                                continue

                            if state == vim.TaskInfo.State.success:
                                # Remove task from taskList
                                task_list.remove(str(task))
                            elif state == vim.TaskInfo.State.error:
                                raise task.info.error
                # Move to next version
                version = update.version
        finally:
            if pcfilter:
                pcfilter.Destroy()

    def terminate(self):
        """
        Stops the VirtualBox instance.
        """
        pass

    def wait_for_vm_state(self, vm_name, vm_state, timeout=60):
        """
        This command will wait for a VM to be in a given state for up to <timeout> seconds and continue on if state
        is reached before the given timeout.

        If <timeout> is exceeded this will fail and continue on.

        :param vm_name: The VM name
        :param vm_state: The VM state that is needed
        :param timeout: Number of seconds to wait for VM to be in paused state. Default set to 60s.
        :return:
        """
        if vm_state == VirtualConstants.VM_STATE_POWERED_ON:
            vm_state = "PoweredOn"
        elif vm_state == VirtualConstants.VM_STATE_POWERED_OFF:
            vm_state = "PoweredOff"

        results = "Unknown"
        sleep_time = 1
        start_time = time.time()
        while True:
            if time.time() - start_time > timeout:
                self.logger.log_info("Error: Timeout before vm state [" + vm_state + "] was reached")
                break
            else:
                results = self.get_vm_state(vm_name)
                if str(results) == vm_state:
                    self.logger.log_info("Machine is " + vm_state)
                    break
            time.sleep(1)
            time.sleep(sleep_time)
        return results
