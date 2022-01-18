"""
Keyword class for all cfm cli commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.CfmConstants import \
    CfmConstants as ParseConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.CfmConstants import \
    CfmConstants as CommandConstants
# All imports above this line will be removed after generation.
# User imports must be added below.


class NetworkElementCfmGenKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementCfmGenKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "cfm"

    def cfm_enable_spbm(self, device_name, **kwargs):
        """
        Description: Globally Enables CFM SPBM on the device.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_SPBM,
                                    **kwargs)

    def cfm_disable_spbm(self, device_name, **kwargs):
        """
        Description: Globally Disables CFM SPBM on the device.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_SPBM,
                                    **kwargs)

    def cfm_enable_maintenance_endpoint(self, device_name, ma_name='', md_name='', mep_id='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "ma_name": ma_name,
            "md_name": md_name,
            "mep_id": mep_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_MAINTENANCE_ENDPOINT,
                                    **kwargs)

    def cfm_disable_maintenance_endpoint(self, device_name, ma_name='', md_name='', mep_id='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "ma_name": ma_name,
            "md_name": md_name,
            "mep_id": mep_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_MAINTENANCE_ENDPOINT,
                                    **kwargs)

    def cfm_set_spbm_mepid(self, device_name, mep_id='', **kwargs):
        """
        Description: Configures a mep id for cfm spbm on the device.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "mep_id": mep_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_SPBM_MEPID,
                                    **kwargs)

    def cfm_set_spbm_level(self, device_name, spbm_level='', **kwargs):
        """
        Description: Configures the CFM spbm level on the device.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "spbm_level": spbm_level
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_SPBM_LEVEL,
                                    **kwargs)

    def cfm_set_maintenance_domain(self, device_name, md_name='', md_index='', md_level='', **kwargs):
        """
        Description: Creates a cfm maintenance-domain on the device.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "md_index": md_index,
            "md_level": md_level,
            "md_name": md_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_MAINTENANCE_DOMAIN,
                                    **kwargs)

    def cfm_set_maintenance_domain_name(self, device_name, md_name='', md_index='', **kwargs):
        """
        Description: Configures the cfm maintenance-domain name on the device.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "md_index": md_index,
            "md_name": md_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_MAINTENANCE_DOMAIN_NAME,
                                    **kwargs)

    def cfm_set_maintenance_domain_index(self, device_name, md_name='', md_index='', **kwargs):
        """
        Description: Configures a cfm maintenance-domain name and index on the device.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "md_index": md_index,
            "md_name": md_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_MAINTENANCE_DOMAIN_INDEX,
                                    **kwargs)

    def cfm_set_maintenance_domain_level(self, device_name, md_name='', md_level='', md_index='', **kwargs):
        """
        Description: Configures a cfm maintenance-domain level for a given maintenance-domain name on the device.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "md_index": md_index,
            "md_level": md_level,
            "md_name": md_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_MAINTENANCE_DOMAIN_LEVEL,
                                    **kwargs)

    def cfm_set_maintenance_association(self, device_name, ma_name='', md_index='', **kwargs):
        """
        Description: Configures a cfm maintenance association for a given maintenance-domain on the device.

        Supported Agents and OS:
            SNMP: VOSS
        """
        args = {
            "ma_name": ma_name,
            "md_index": md_index
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_MAINTENANCE_ASSOCIATION,
                                    **kwargs)

    def cfm_set_maintenance_endpoint(self, device_name, **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            SNMP: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_MAINTENANCE_ENDPOINT,
                                    **kwargs)

    def cfm_clear_spbm_mepid(self, device_name, **kwargs):
        """
        Description: Sets the cfm spbm mep id back to the default setting on the device.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_SPBM_MEPID,
                                    **kwargs)

    def cfm_clear_spbm_level(self, device_name, **kwargs):
        """
        Description: Sets the cfm spbm level back to the default setting on the device.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_SPBM_LEVEL,
                                    **kwargs)

    def cfm_clear_maintenance_domain(self, device_name, md_name='', md_index='', **kwargs):
        """
        Description: Removes a cfm maintenance-domain on the device.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "md_index": md_index,
            "md_name": md_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_MAINTENANCE_DOMAIN,
                                    **kwargs)

    def cfm_clear_maintenance_association(self, device_name, **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            SNMP: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_MAINTENANCE_ASSOCIATION,
                                    **kwargs)

    def cfm_clear_maintenance_endpoint(self, device_name, **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            SNMP: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_MAINTENANCE_ENDPOINT,
                                    **kwargs)

    # ##################################################################################################################
    #   Inspection Keywords   ##########################################################################################
    # ##################################################################################################################

    def cfm_verify_spbm_enabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.

        Verifies the SPBM is globally enabled.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SPBM,
                                           self.parse_const.CHECK_CFM_SPBM_STATE_ENABLE, True,
                                           "CFM SPBM is globally enabled on {device_name}.",
                                           "CFM SPBM is not globally enabled on {device_name}!",
                                           **kwargs)

    def cfm_verify_spbm_disabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.

        Verifies the SPBM is globally disabled.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SPBM,
                                           self.parse_const.CHECK_CFM_SPBM_STATE_ENABLE, False,
                                           "CFM SPBM is globally disabled on {device_name}.",
                                           "CFM SPBM is not globally disabled {device_name}!",
                                           **kwargs)

    def cfm_verify_spbm_mepid(self, device_name, mep_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [mepid]       - The mep id value to verify.

        Verifies that the specified CFM SPBM mepid value exists on the device.
        """
        args = {"mep_id": mep_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SPBM,
                                           self.parse_const.CHECK_CFM_SPBM_MEPID, True,
                                           "The CFM SPBM MEP ID on {device_name} is set to {mep_id}.",
                                           "The CFM SPBM MEP ID on {device_name} IS NOT set to {mep_id}!",
                                           **kwargs)

    def cfm_verify_spbm_level(self, device_name, spbm_level='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [spbm_level]  - The cfm spbm level to verify.  VOSS valid range is 0-7

        Verifies the CFM spbm level on the device.
        """
        args = {"spbm_level": spbm_level}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SPBM,
                                           self.parse_const.CHECK_CFM_SPBM_LEVEL, True,
                                           "The CFM SPBM LEVEL on {device_name} is set to {spbm_level}.",
                                           "The CFM SPBM LEVEL on {device_name} IS NOT set to {spbm_level}!",
                                           **kwargs)

    def cfm_verify_spbm_mac(self, device_name, spbm_mac='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [spbm_mac]    - The cfm spbm mac address to verify.

        Verifies that a specified CFM spbm mac address is present on the device.
        """
        args = {"spbm_mac": spbm_mac}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SPBM,
                                           self.parse_const.CHECK_CFM_SPBM_MAC, True,
                                           "The CFM SPBM MAC {spbm_mac} is present on {device_name}.",
                                           "The CFM SPBM MAC {spbm_mac} IS NOT present on {device_name}!",
                                           **kwargs)

    def cfm_verify_maintenance_domain(self, device_name, md_name='', md_index='', md_level='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [md_name]     - The maintenance-domain name to verify.
        [md_index]    - The maintenance-domain index to verify.
        [md_level]    - The maintenance-domain level to verify.

        Verifies that a specified CFM maintenance-domain exists on the device.
        """
        args = {"md_name": md_name,
                "md_index": md_index,
                "md_level": md_level,
                "oid_index": md_index}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_MAINTENANCE_DOMAIN,
                                           self.parse_const.CHECK_CFM_MAINTENANCE_DOMAIN, True,
                                           "The CFM Maintenance-domain {md_name} is present on {device_name}.",
                                           "The CFM Maintenance-domain {md_name} IS NOT present on "
                                           "{device_name}!",
                                           **kwargs)

    def cfm_verify_maintenance_domain_name(self, device_name, md_name='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [md_name]     - The maintenance-domain name to verify.

        Verifies the specified CFM maintenance-domain name.
        """
        args = {"md_name": md_name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_MAINTENANCE_DOMAIN,
                                           self.parse_const.CHECK_CFM_MAINTENANCE_DOMAIN_NAME, True,
                                           "The CFM Maintenance-domain name {md_name} is present on "
                                           "{device_name}.",
                                           "The CFM Maintenance-domain name {md_name} IS NOT present on "
                                           "{device_name}!",
                                           **kwargs)

    def cfm_verify_maintenance_domain_name_and_index(self, device_name, md_name='', md_index='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [md_name]     - The maintenance-domain name to verify.
        [md_index]    - The maintenance-domain index to verify.

        Verifies the cfm maintenance-domain name and index exists on the device.
        """
        args = {"md_name": md_name,
                "md_index": md_index,
                "oid_index": md_index}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_MAINTENANCE_DOMAIN,
                                           self.parse_const.CHECK_CFM_MAINTENANCE_DOMAIN_INDEX, True,
                                           "The CFM Maintenance-domain {md_name} with index {md_index} is "
                                           "present on {device_name}.",
                                           "The CFM Maintenance-domain {md_name} with index {md_index} IS NOT "
                                           "present on {device_name}!",
                                           **kwargs)

    def cfm_verify_maintenance_domain_level(self, device_name, md_name='', md_level='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [md_name]     - The maintenance-domain name to verify.
        [md_level]    - The maintenance-domain maintenance level to verify.

        Verifies the cfm maintenance-domain level for a given maintenance-domain name on the device.
        """
        args = {"md_name": md_name,
                "md_level": md_level}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_MAINTENANCE_DOMAIN,
                                           self.parse_const.CHECK_CFM_MAINTENANCE_DOMAIN_LEVEL, True,
                                           "Level {md_level} is set for CFM Maintenance-domain {md_name} on "
                                           "{device_name}.",
                                           "Level {md_level} IS NOT set for CFM Maintenance-domain {md_name} on "
                                           "{device_name}!",
                                           **kwargs)

    def cfm_verify_maintenance_domain_does_not_exist(self, device_name, md_name='', md_index='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [md_name]     - The maintenance-domain name to verify.
        [md_index]    - The maintenance-domain index to verify.

        Verifies the cfm maintenance-domain does not exist on the device.
        """
        args = {"md_name": md_name,
                "md_index": md_index,
                "oid_index": md_index}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_MAINTENANCE_DOMAIN,
                                           self.parse_const.CHECK_CFM_MAINTENANCE_DOMAIN_INDEX, False,
                                           "The CFM Maintenance-domain {md_name} with index {md_index} is not "
                                           "present on {device_name}.",
                                           "The CFM Maintenance-domain {md_name} with index {md_index} IS "
                                           "present on {device_name}!",
                                           **kwargs)
