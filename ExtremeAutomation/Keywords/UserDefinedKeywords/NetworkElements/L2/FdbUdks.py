from ExtremeAutomation.Keywords.NetworkElementKeywords.GeneratedKeywords.NetworkElementFdbGenKeywords import NetworkElementFdbGenKeywords
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils
import time


class FdbUdks():
    def __init__(self) -> None:
        self.NetworkElementFdbGenKeywords = NetworkElementFdbGenKeywords()
        self.stringUtils = StringUtils()

    def Add_Static_FDB_Entry_and_Validate_It_Exists(self, netelem_name,  mac,  vlan,  port,  vlan_name=None, **kwargs):
        default_vlan_name = self.stringUtils.exos_vlan_string(vlan, **kwargs)
        if vlan_name is None:
            self.NetworkElementFdbGenKeywords.fdb_create_entry(netelem_name,  mac,  port,  vlan,  default_vlan_name, **kwargs)
        else:
            self.NetworkElementFdbGenKeywords.fdb_create_entry(netelem_name,  mac,  port,  vlan,  vlan_name, **kwargs)
        self.NetworkElementFdbGenKeywords.fdb_verify_entry_exists(netelem_name,  mac,  vlan,  port, **kwargs)

    def Add_Static_Multicast_FDB_Entry_and_Validate_It_Exists(self, netelem_name,  mac,  vlan,  port,  vlan_name=None, **kwargs):
        default_vlan_name = self.stringUtils.exos_vlan_string(vlan)
        if vlan_name is None:
            self.NetworkElementFdbGenKeywords.fdb_create_multicast_entry(netelem_name,  mac,  port,  vlan,  default_vlan_name, **kwargs)
        else:
            self.NetworkElementFdbGenKeywords.fdb_create_multicast_entry(netelem_name,  mac,  port,  vlan,  vlan_name, **kwargs)
        self.NetworkElementFdbGenKeywords.fdb_verify_entry_exists(netelem_name,  mac,  vlan,  port, **kwargs)

    def Remove_Static_FDB_Entry_and_Validate_It_Does_Not_Exist(self, netelem_name,  mac,  vlan,  netelem_port,  vlan_name=None, **kwargs):
        default_vlan_name = self.stringUtils.exos_vlan_string(vlan, **kwargs)
        if vlan_name is None:
            self.NetworkElementFdbGenKeywords.fdb_delete_entry(netelem_name,  mac,  vlan,  default_vlan_name,  ignore_cli_feedback=True)
        else:
            self.NetworkElementFdbGenKeywords.fdb_delete_entry(netelem_name,  mac,  vlan,  vlan_name, ignore_cli_feedback=True)
        self.NetworkElementFdbGenKeywords.fdb_verify_entry_does_not_exist(netelem_name,  mac,  vlan,  netelem_port, ignore_cli_feedback=True)

    def Delay_X_Seconds_and_then_Validate_Fdb_Entry_Still_Exists(self, delay_time,  netelem_name,  mac,  vlan,  netelem_port, **kwargs):
        time.sleep(int(delay_time))
        self.NetworkElementFdbGenKeywords.fdb_verify_entry_exists(netelem_name,  mac,  vlan,  netelem_port, **kwargs)

    def Set_FDB_Agetime_and_Verify_it_is_Correctly_Set(self, netelem_name, agetime, **kwargs):
        age_integer = int(agetime)
        if age_integer <= 15:
            self.NetworkElementFdbGenKeywords.fdb_set_agetime_min(netelem_name, agetime, **kwargs)
        else:
            self.NetworkElementFdbGenKeywords.fdb_set_agetime(netelem_name, agetime, **kwargs)
        self.NetworkElementFdbGenKeywords.fdb_verify_agetime(netelem_name, agetime, **kwargs)

    def Clear_FDB_Agetime_and_Verify_it_is_Correctly_Set(self, netelem_name,  agetime, **kwargs):
        self.NetworkElementFdbGenKeywords.fdb_clear_agetime(netelem_name)
        self.NetworkElementFdbGenKeywords.fdb_verify_agetime(netelem_name,  agetime, **kwargs)

