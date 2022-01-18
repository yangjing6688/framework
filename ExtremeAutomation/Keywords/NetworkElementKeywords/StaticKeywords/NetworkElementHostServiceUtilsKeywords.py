from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import \
    NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.HostservicesConstants \
    import HostservicesConstants as CommandConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.HostservicesConstants \
    import HostservicesConstants as ParseConstants


class NetworkElementHostServiceUtilsKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementHostServiceUtilsKeywords, self).__init__()
        self.api_const = self.constants.API_HOSTSERVICES
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()

    # ##################################################################################################################
    #   Configuration Keywords   #######################################################################################
    # ##################################################################################################################
    def enable_sys_force_topology_ip_flag(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.

        Enables the flag that configures the CLIP ID as the topology IP.
        """
        args = {"oid_index": "0"}

        return self.execute_keyword(device_name, args, self.cmd_const.ENABLE_SYS_FORCE_TOPOLOGY_IP_FLAG,
                                    **kwargs)

    def disable_sys_force_topology_ip_flag(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.

        Disables the flag that configures the CLIP ID as the topology IP.
        """
        args = {"oid_index": "0"}

        return self.execute_keyword(device_name, args, self.cmd_const.DISABLE_SYS_FORCE_TOPOLOGY_IP_FLAG,
                                    **kwargs)

    def configure_sys_clipid_topology_ip(self, device_name, clip_id, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [clip_id]     - The CLIP interface ID.

        Configures the circuitless IP (CLIP) ID as the topology IP.
        """
        args = {"clip_id": clip_id}

        return self.execute_keyword(device_name, args, self.cmd_const.SET_SYS_CLIPID_TOPOLOGY_IP,
                                    **kwargs)

    def unconfigure_sys_clipid_topology_ip(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.

        Unconfigures the circuitless IP (CLIP) ID as the topology IP.
        """
        args = {}

        return self.execute_keyword(device_name, args, self.cmd_const.CLEAR_SYS_CLIPID_TOPOLOGY_IP,
                                    **kwargs)

    # ##################################################################################################################
    #   Inspection Keywords   ##########################################################################################
    # ##################################################################################################################
    def verify_sys_force_topology_ip_flag_is_set(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device the keyword will be run against.

        Verifies that the sys force topology ip flag is set.
        """
        args = {}

        self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SYS_SETTING,
                                    self.parse_const.VERIFY_SYS_FORCE_TOPOLOGY_IP_FLAG_IS_ENABLED, True,
                                    "The sys force-topology-ip-flag is set on {device_name}.",
                                    "The sys force-topology-ip-flag is NOT set on {device_name}.!",
                                    **kwargs)

    def verify_sys_force_topology_ip_flag_is_not_set(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device the keyword will be run against.

        Verifies that the sys force topology ip flag is not set.
        """
        args = {}

        self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SYS_SETTING,
                                    self.parse_const.VERIFY_SYS_FORCE_TOPOLOGY_IP_FLAG_IS_DISABLED, True,
                                    "The sys force-topology-ip-flag is not set on {device_name}.",
                                    "The sys force-topology-ip-flag is SET on {device_name}.!",
                                    **kwargs)

    def verify_sys_clipid_topology_ip_is_configured(self, device_name, clip_id, **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device the keyword will be run against.
        [clip_id]      - The CLIP interface ID.

        Verifies that the sys clip id topology ip is configured.
        """
        args = {"clip_id": clip_id}

        self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SYS_SETTING,
                                    self.parse_const.VERIFY_SYS_CLIPID_TOPOLOGY_IP, True,
                                    "The sys clipId topology ip is set on {device_name}.",
                                    "The sys clipId topology ip is NOT set on {device_name}.!",
                                    **kwargs)

    def verify_sys_clipid_topology_ip_is_not_configured(self, device_name, clip_id, **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device the keyword will be run against.
        [clip_id]      - The CLIP interface ID.

        Verifies that the sys clip id topology ip is not configured.
        """
        args = {"clip_id": clip_id}

        self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SYS_SETTING,
                                    self.parse_const.VERIFY_SYS_CLIPID_TOPOLOGY_IP, False,
                                    "The sys clipId topology ip is not set on {device_name}.",
                                    "The sys clipId topology ip IS set on {device_name}.!",
                                    **kwargs)
