"""
Keyword class for all dvr cli commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.DvrConstants import \
    DvrConstants as ParseConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.DvrConstants import \
    DvrConstants as CommandConstants
# All imports above this line will be removed after generation.
# User imports must be added below.


class NetworkElementDvrGenKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementDvrGenKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "dvr"

    def dvr_set_domain_controller(self, device_name, domain_id='', **kwargs):
        """
        Description: Configures a DVR domain controller domain-id.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "domain_id": domain_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_DOMAIN_CONTROLLER,
                                    **kwargs)

    def dvr_clear_domain_controller(self, device_name, **kwargs):
        """
        Description: Removes a DVR domain controller on the device.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_DOMAIN_CONTROLLER,
                                    **kwargs)

    def dvr_disable_domain_controller_inject_default_route_all(self, device_name, **kwargs):
        """
        Description: Disables the injection of default routes for all DVR domain controllers.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_DOMAIN_CONTROLLER_INJECT_DEFAULT_ROUTE_ALL,
                                    **kwargs)

    def dvr_disable_domain_controller_inject_default_route(self, device_name, domain_id='', **kwargs):
        """
        Description: Disables injecting of default routes for the specified DVR domain controller id.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "domain_id": domain_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_DOMAIN_CONTROLLER_INJECT_DEFAULT_ROUTE,
                                    **kwargs)

    def dvr_set_leaf_id(self, device_name, domain_id='', **kwargs):
        """
        Description: Sets the domain id for the DVR leaf.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "domain_id": domain_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_LEAF_ID,
                                    **kwargs)

    def dvr_set_leaf_virtual_ist(self, device_name, interface='', local_ip='', mask='', peer_ip='', cluster_id='',
                                 **kwargs):
        """
        Description: Sets the virtual-ist IP address for the DVR leaf on the specified interface.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "cluster_id": cluster_id,
            "interface": interface,
            "local_ip": local_ip,
            "mask": mask,
            "peer_ip": peer_ip
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_LEAF_VIRTUAL_IST,
                                    **kwargs)

    def dvr_clear_leaf_virtual_ist(self, device_name, interface='', **kwargs):
        """
        Description: Removes the virtual-ist for the DVR leaf on the specified interface.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "interface": interface
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_LEAF_VIRTUAL_IST,
                                    **kwargs)

    def dvr_set_interface_gateway_ipv4(self, device_name, interface='', ip='', **kwargs):
        """
        Description: Configures a DVR IPv4 gateway on an interface.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "interface": interface,
            "ip": ip
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_INTERFACE_GATEWAY_IPV4,
                                    **kwargs)

    def dvr_clear_interface_gateway_ipv4(self, device_name, interface='', **kwargs):
        """
        Description: Removes a DVR IPv4 gateway on the specified interface.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "interface": interface
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_INTERFACE_GATEWAY_IPV4,
                                    **kwargs)

    def dvr_enable_interface(self, device_name, interface='', **kwargs):
        """
        Description: Enables DVR on an interface.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "interface": interface
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_INTERFACE,
                                    **kwargs)

    def dvr_disable_interface(self, device_name, interface='', **kwargs):
        """
        Description: Disables DVR on an interface.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "interface": interface
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_INTERFACE,
                                    **kwargs)

    def dvr_set_redistribute(self, device_name, **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_REDISTRIBUTE,
                                    **kwargs)

    def dvr_set_redistribute_direct(self, device_name, **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_REDISTRIBUTE_DIRECT,
                                    **kwargs)

    def dvr_set_redistribute_direct_metric(self, device_name, metric='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "metric": metric
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_REDISTRIBUTE_DIRECT_METRIC,
                                    **kwargs)

    def dvr_set_redistribute_vrf(self, device_name, vrf='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "vrf": vrf
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_REDISTRIBUTE_VRF,
                                    **kwargs)

    def dvr_clear_redistribute_direct(self, device_name, **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_REDISTRIBUTE_DIRECT,
                                    **kwargs)

    def dvr_enable_redistribute_direct(self, device_name, **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_REDISTRIBUTE_DIRECT,
                                    **kwargs)

    def dvr_disable_redistribute_direct(self, device_name, **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_REDISTRIBUTE_DIRECT,
                                    **kwargs)

    def dvr_set_redistribute_static(self, device_name, **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_REDISTRIBUTE_STATIC,
                                    **kwargs)

    def dvr_set_redistribute_static_metric(self, device_name, metric='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "metric": metric
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_REDISTRIBUTE_STATIC_METRIC,
                                    **kwargs)

    def dvr_clear_redistribute_static(self, device_name, **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_REDISTRIBUTE_STATIC,
                                    **kwargs)

    def dvr_enable_redistribute_static(self, device_name, **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_REDISTRIBUTE_STATIC,
                                    **kwargs)

    def dvr_disable_redistribute_static(self, device_name, **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_REDISTRIBUTE_STATIC,
                                    **kwargs)

    def dvr_clear_host_entries(self, device_name, **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_HOST_ENTRIES,
                                    **kwargs)

    def dvr_clear_host_entries_ipv4(self, device_name, ip='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "ip": ip
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_HOST_ENTRIES_IPV4,
                                    **kwargs)

    def dvr_clear_host_entries_ipv4_l3isid(self, device_name, ip='', isid='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "ip": ip,
            "isid": isid
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_HOST_ENTRIES_IPV4_L3ISID,
                                    **kwargs)

    def dvr_clear_host_entries_l2isid(self, device_name, isid='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "isid": isid
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_HOST_ENTRIES_L2ISID,
                                    **kwargs)

    def dvr_clear_host_entries_l3isid(self, device_name, isid='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "isid": isid
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_HOST_ENTRIES_L3ISID,
                                    **kwargs)

    # ##################################################################################################################
    #   Inspection Keywords   ##########################################################################################
    # ##################################################################################################################

    def dvr_verify_interface_enabled(self, device_name, interface='', **kwargs):
        """
        Keyword Arguments:
        [device_name]   - The device the keyword will be run against.
        [interface]     - The interface to verify DVR is enabled on.

        Verifies DVR is enabled on the specified interface.
        """
        args = {"interface": interface,
                "intf": "vlan"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACES,
                                           self.parse_const.VERIFY_DVR_ON_INTERFACE_IS_ENABLED, True,
                                           "DVR is enabled on interface {interface} on {device_name}.",
                                           "DVR is NOT enabled on interface {interface} on {device_name}!",
                                           **kwargs)

    def dvr_verify_interface_disabled(self, device_name, interface='', **kwargs):
        """
        Keyword Arguments:
        [device_name]   - The device the keyword will be run against.
        [interface]     - The interface to verify DVR is disabled on.

        Verifies DVR is disabled on the specified interface.
        """
        args = {"interface": interface,
                "intf": "vlan"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACES,
                                           self.parse_const.VERIFY_DVR_ON_INTERFACE_IS_ENABLED, False,
                                           "DVR is disabled on interface {interface} on {device_name}.",
                                           "DVR is NOT disabled on interface {interface} on {device_name}!",
                                           **kwargs)

    def dvr_verify_domain_controller_id_exists(self, device_name, domain_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name]   - The device the keyword will be run against.
        [domain_id]     - The DVR domain controller id to verify.

        Verifies the specified DVR domain controller id exists on the device.
        """
        args = {"domain_id": domain_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.VERIFY_DVR_DOMAIN_CONTROLLER_EXISTS, True,
                                           "The DVR Domain Controller ID {domain_id} is present on {device_name}.",
                                           "The DVR Domain Controller ID {domain_id} is NOT present on {device_name}!",
                                           **kwargs)

    def dvr_verify_leaf_domain_id(self, device_name, interface='', domain_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name]   - The device the keyword will be run against.
        [interface]     - The interface to verify the domain id on.
        [domain_id]     - The domain id to verify for the DVR leaf.  (Acceptable value: 1-255)

        Verifies the domain id is set for the DVR leaf on the specified interface.
        """
        args = {"interface": interface,
                "domain_id": domain_id,
                "intf": "vlan"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACES,
                                           self.parse_const.VERIFY_DVR_LEAF_ID_IS_SET, True,
                                           "The DVR Domain ID {domain_id} is set on interface {interface} on "
                                           "{device_name}.",
                                           "The DVR Domain ID {domain_id} is NOT set on interface {interface} on "
                                           "{device_name}!",
                                           **kwargs)
