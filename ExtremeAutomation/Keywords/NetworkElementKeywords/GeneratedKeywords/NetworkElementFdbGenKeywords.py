"""
Keyword class for all fdb cli commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.FdbConstants import \
    FdbConstants as ParseConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.FdbConstants import \
    FdbConstants as CommandConstants
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Keywords.NetworkElementKeywords.Utils.NetworkElementSnmpUtils import \
    NetworkElementSnmpUtils as SnmpUtils


class NetworkElementFdbGenKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementFdbGenKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "fdb"

    def fdb_set_agetime(self, device_name, agetime='', **kwargs):
        """
        Description: Configures the given devices FDB agetime.

        Supported Agents and OS:
            CLI: EOS, EXOS, VOSS, SLX
        """
        args = {
            "agetime": agetime
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_AGETIME,
                                    **kwargs)

    def fdb_set_agetime_min(self, device_name, agetime='', **kwargs):
        """
        Description: Configures the given devices FDB agetime (in minutes).

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "agetime": agetime
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_AGETIME_MIN,
                                    **kwargs)

    def fdb_clear_agetime(self, device_name, **kwargs):
        """
        Description: Sets the FDB agetime back to it's default value.

        Supported Agents and OS:
            CLI: EOS, EXOS, VOSS, SLX
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_AGETIME,
                                    **kwargs)

    def fdb_enable_unicast_as_multicast(self, device_name, **kwargs):
        """
        Description: Enables unicast-as-multicast on a given device.

        Supported Agents and OS:
            CLI: EOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_UNICAST_AS_MULTICAST,
                                    **kwargs)

    def fdb_disable_unicast_as_multicast(self, device_name, **kwargs):
        """
        Description: Disables unicast-as-multicast on a given device.

        Supported Agents and OS:
            CLI: EOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_UNICAST_AS_MULTICAST,
                                    **kwargs)

    def fdb_clear_all(self, device_name, **kwargs):
        """
        Description: Clears all FDB entries.

        Supported Agents and OS:
            CLI: EOS, EXOS, SLX
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_ALL,
                                    **kwargs)

    def fdb_clear_all_vlan(self, device_name, vlan='', vlan_name='', **kwargs):
        """
        Description: Clears all FDB entries on the specified VID.

        Supported Agents and OS:
            CLI: EOS, EXOS, VOSS, SLX
        """
        args = {
            "vlan": vlan,
            "vlan_name": vlan_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_ALL_VLAN,
                                    **kwargs)

    def fdb_clear_all_port(self, device_name, port='', **kwargs):
        """
        Description: Clears all FDB entries on the specified port.

        Supported Agents and OS:
            CLI: EOS, EXOS, VOSS, SLX
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_ALL_PORT,
                                    **kwargs)

    def fdb_create_entry(self, device_name, mac='', port='', vlan='', vlan_name='', **kwargs):
        """
        Description: Adds the given MAC entry to the device's FDB.

        Supported Agents and OS:
            CLI: EOS, EXOS, VOSS, SLX
        """
        args = {
            "mac": mac,
            "port": port,
            "vlan": vlan,
            "vlan_name": vlan_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_ENTRY,
                                    **kwargs)

    def fdb_create_multicast_entry(self, device_name, mac='', port='', vlan='', vlan_name='', **kwargs):
        """
        Description: Adds the given multicast MAC entry to the device's FDB.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "mac": mac,
            "port": port,
            "vlan": vlan,
            "vlan_name": vlan_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_MULTICAST_ENTRY,
                                    list_value_arg=True,
                                    wait_for_prompt=False,
                                    **kwargs)

    def fdb_delete_entry(self, device_name, mac='', vlan='', vlan_name='', **kwargs):
        """
        Description: Removes the given MAC entry from the device's FDB.

        Supported Agents and OS:
            CLI: EOS, EXOS, VOSS, SLX
        """
        args = {
            "mac": mac,
            "vlan": vlan,
            "vlan_name": vlan_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DELETE_ENTRY,
                                    **kwargs)

    def fdb_create_blackhole_entry(self, device_name, mac='', vlan_name='', **kwargs):
        """
        Description: Adds a blackhole FDB entry.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "mac": mac,
            "vlan_name": vlan_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_BLACKHOLE_ENTRY,
                                    **kwargs)

    def fdb_enable_learning_vlan(self, device_name, vlan='', **kwargs):
        """
        Description: Enables learning on a given vlan and device.

        Supported Agents and OS:
            CLI: EXOS, SLX
        """
        args = {
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_LEARNING_VLAN,
                                    **kwargs)

    def fdb_enable_learning_port(self, device_name, port='', **kwargs):
        """
        Description: Enables learning on a given port and device.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_LEARNING_PORT,
                                    **kwargs)

    def fdb_disable_learning_vlan(self, device_name, vlan='', **kwargs):
        """
        Description: Disables learning on a given vlan and device.

        Supported Agents and OS:
            CLI: EXOS, SLX
        """
        args = {
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_LEARNING_VLAN,
                                    **kwargs)

    def fdb_disable_learning_port(self, device_name, port='', **kwargs):
        """
        Description: Disables learning on a given port and device.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_LEARNING_PORT,
                                    **kwargs)

    def fdb_clear_mac_port(self, device_name, mac='', port='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "mac": mac,
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_MAC_PORT,
                                    **kwargs)

    def fdb_clear_mac_port_vlan(self, device_name, mac='', port='', vlan='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "mac": mac,
            "port": port,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_MAC_PORT_VLAN,
                                    **kwargs)

    def fdb_clear_dynamic_entry(self, device_name, mac='', port='', vlan='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "mac": mac,
            "port": port,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_DYNAMIC_ENTRY,
                                    **kwargs)

    def fdb_set_agetime_conversational(self, device_name, agetime='', **kwargs):
        """
        Description: Configures the given devices FDB conversational agetime.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {
            "agetime": agetime
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_AGETIME_CONVERSATIONAL,
                                    **kwargs)

    def fdb_clear_agetime_conversational(self, device_name, **kwargs):
        """
        Description: Sets the FDB conversational agetime back to it's default value.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_AGETIME_CONVERSATIONAL,
                                    **kwargs)

    def fdb_set_fdb_learn_mode_conversational(self, device_name, **kwargs):
        """
        Description: Configures the given devices FDB learning mode to conversational.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_FDB_LEARN_MODE_CONVERSATIONAL,
                                    **kwargs)

    def fdb_clear_fdb_learn_mode(self, device_name, **kwargs):
        """
        Description: Configures the given devices FDB learning mode to default.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_FDB_LEARN_MODE,
                                    **kwargs)

    def fdb_clear_all_linecard(self, device_name, linecard='', **kwargs):
        """
        Description: Clears all FDB entries on the specified line-card.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {
            "linecard": linecard
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_ALL_LINECARD,
                                    **kwargs)

    def fdb_clear_all_linecard_rbid(self, device_name, linecard='', rbid='', **kwargs):
        """
        Description: Clears all FDB entries on the specified line-card.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {
            "linecard": linecard,
            "rbid": rbid
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_ALL_LINECARD_RBID,
                                    **kwargs)

    def fdb_enable_learning(self, device_name, **kwargs):
        """
        Description: Enables learning on a given device.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_LEARNING,
                                    **kwargs)

    def fdb_disable_learning(self, device_name, **kwargs):
        """
        Description: Disables learning on a given device.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_LEARNING,
                                    **kwargs)

    # ##################################################################################################################
    #   Inspection Keywords   ##########################################################################################
    # ##################################################################################################################

    def fdb_verify_agetime(self, device_name, agetime='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.

        Validates the FDB agetime
        """
        args = {"agetime": agetime}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_AGETIME,
                                           self.parse_const.CHECK_FDB_AGETIME, True,
                                           "FDB Agetime is properly set to {agetime} on {device_name}.",
                                           "FDB Agetime is NOT set to {agetime} on {device_name}.",
                                           **kwargs)

    def fdb_verify_entry_exists(self, device_name, mac='', vlan='', port='', **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [mac]         - The MAC address entry in the FDB table.
        [vlan]        - The expected VLAN for the MAC entry.
        [port]        - The expected port for the MAC entry.

        Verifies the specified FDB entry exists.
        """
        args = {"mac": mac,
                "vlan": vlan,
                "port": port,
                "port_if_index": SnmpUtils().get_port_index_from_name(device_name, port)}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ENTRY,
                                           self.parse_const.CHECK_FDB_ENTRY_EXISTS, True,
                                           "FDB Entry exists for {mac}, port {port}, and vlan {vlan}"
                                           " on {device_name}.",
                                           "FDB Entry for {mac}, port {port}, and vlan {vlan}"
                                           "does NOT exist on {device_name}!",
                                           **kwargs)

    def fdb_verify_entry_has_only_one_instance(self, device_name, mac='', **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [mac]         - The MAC address entry in the FDB table.

        Verifies the specified FDB entry only exists once in table.
        """
        args = {"mac": mac}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ENTRY,
                                           self.parse_const.CHECK_FDB_ENTRY_ONLY_EXISTS_ONCE, True,
                                           "FDB Entry exists for {mac} on {device_name} once.",
                                           "FDB Entry for {mac} on {device_name} does not exist or "
                                           "exists more than once.",
                                           **kwargs)

    def fdb_verify_entry_has_only_two_instances(self, device_name, mac='', **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [mac]         - The MAC address entry in the FDB table.

        Mac entry should exist in the mac address table two times in the case of 2 SPBM VLANS.
        This is VOSS specific.
        """
        args = {"mac": mac}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ENTRY,
                                           self.parse_const.CHECK_FDB_ENTRY_EXISTS_TWICE, True,
                                           "FDB Entry exists twice for {mac} on {device_name}.",
                                           "FDB Entry for {mac} on {device_name} does not exist or "
                                           "does not exist twice.",
                                           **kwargs)

    def fdb_verify_entry_does_not_exist(self, device_name, mac='', vlan='', port='', **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [mac]         - The MAC address entry in the FDB table.
        [vlan]        - The expected VLAN for the MAC entry.
        [port]        - The expected port for the MAC entry.

        Verifies the specified FDB entry exists.
        """
        args = {"mac": mac,
                "vlan": vlan,
                "port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ENTRY,
                                           self.parse_const.CHECK_FDB_ENTRY_EXISTS, False,
                                           "FDB Entry Properly does not exist for {mac} on "
                                           "{device_name}.",
                                           "FDB Entry for {mac} on {device_name} IMPROPERLY exists.",
                                           **kwargs)

    def fdb_verify_entries_all_exist(self, device_name, mac='', vlan='', port='', **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [mac]         - The MAC address entry in the FDB table.
        [vlan]        - The expected VLAN for the MAC entry.
        [port]        - The expected port for the MAC entry.

        Verifies the specified FDB entry exists.
        """
        args = {"mac": mac,
                "vlan": vlan,
                "port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL_ENTRIES,
                                           self.parse_const.CHECK_FDB_ENTRY_EXISTS, True,
                                           "FDB Entry exists for {mac} on {device_name}.",
                                           "FDB Entry for {mac} on {device_name} does not exist.",
                                           **kwargs)

    def fdb_verify_entry_exists_for_duration(self, device_name, mac='', vlan='', port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [mac]         - The mac address that is is being waited for existence.
        [vlan]        - The name of the vlan associated with the mac
        [port]        - The name of the port associated with the mac
        [max_wait]    - The maximum time that will be waited for vlan's existence.
        [interval]    - The interval between polls for the vlan's existance.

        Verifies that an FDB entry exists for at least <max_wait> seconds.
        """
        args = {"mac": mac,
                "vlan": vlan,
                "port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL_ENTRIES,
                                           self.parse_const.CHECK_FDB_ENTRY_EXISTS, False,
                                           "FDB Entry {mac} continued to exist on {device_name}.",
                                           "FDB Entry {mac} was flushed from the table on {device_name}.",
                                           wait_for=True, **kwargs)
