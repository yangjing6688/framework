from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.NetworkEmulatingEndstationApi import \
    NetworkEmulatingEndstationApi
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


class JetsEndstationApi(NetworkEmulatingEndstationApi):
    """
    meshost create local_host2 -type LOCAL_TLS -macAddr 00:00:00:ff:ff:02 -ipAddr 10.10.10.12 -vlanId 100 -intf 4
                               -isid 999 -mask 255.0.0.0

    bridge createIsidEndPoints -bridgeName edgeA -basename A_host -isidId 999 -uniBmac 00:00:00:0e:0a:0f -cVlan 100
                               -epMac 00:0a:ea:0e:0a:01 -epIp 10.10.10.55 -epMask 255.255.255.0 -numEps 1
                               -incrBmac false -incrCVlan false -bvlan 4051 -plsbInstance 1 -tuni false -cvlanPriority 0
                               -l3isid 0

    meshost create A_host1 -skip true
    """

    def __init__(self, device):
        super(JetsEndstationApi, self).__init__(device)

    # meshost create local_host2 -type LOCAL_TLS -macAddr 00:00:00:ff:ff:02 -ipAddr 10.10.10.12 -vlanId 100 -intf 4
    # -isid 999 -mask 255.0.0.0
    #
    # bridge create -bridgeName EzEdgeA -basename A_host -isidId 999 -uniBmac 00:00:00:0e:0a:0f -cVlan 100
    # -epMac 00:00:00:0c:0a:01 -epIp 10.10.10.55 -epMask 255.255.255.0 -numEps 1 -incrBmac false -incrCVlan false
    # -bvlan 4051 -plsbInstance 1 -tuni false  -cvlanPriority 0 -l3isid 0
    def create_isis_endpoint(self, bridge_name, basename, isid_id, uni_bmac, cvlan, cvlan_priority, endpoint_mac,
                             endpoint_ip, endpoint_mask, num_eps, bvlan, plsb_instance, l3isid, options=None):
        self.logger.log_debug("create_isis_endpoint() DEPRECATED, USE create_l2vsn_ipv4_endpoint OR "
                              "create_l2vsn_ip6_endpoint")
        try:
            # dev = self.get_device()
            if not isinstance(num_eps, int):
                self.logger.log_error("Number of Endpoints needs to be a number value=" + str(num_eps))
            create_isid_endpoints = " -bridgeName " + str(bridge_name) + \
                " -basename " + str(basename) + \
                " -isidId " + str(isid_id) + \
                " -uniBmac " + str(uni_bmac) + \
                " -cVlan " + str(cvlan) + \
                " -epMac " + str(endpoint_mac) + \
                " -epIp " + str(endpoint_ip) + \
                " -epMask " + str(endpoint_mask) + \
                " -numEps " + str(num_eps) + " -incrBmac false -incrCVlan false " + \
                " -bvlan " + str(bvlan) + \
                " -plsbInstance " + str(plsb_instance) + \
                " -tuni false " + \
                " -cvlanPriority " + str(cvlan_priority) + \
                " -l3isid " + str(l3isid)
            self.send_command("bridge createIsidEndPoints " + create_isid_endpoints)
            index = 1
            while index <= num_eps:
                self.send_command("meshost create " + str(basename) + str(index) + " -skip true")
                index += 1
        except Exception:
            self.logger.log_debug(StringUtils.exception_to_string())

    def create_routed_l2vsn_ipv4_endpoint(self, bridge_name, basename, isid_id, endpoint_ip, endpoint_mask,
                                          endpoint_gateway, endpoint_mac, num_eps=1, options=None):
        """
        bridge createRoutedL2VsnEndPoints -bridgeName edgeA -basename edgeA_vlan200ipv4host -isidId 200 -numEps 1
        -epMac 00:aa:c8:aa:c8:aa -epIp 200.1.1.200 -epMask 255.255.255.0 -epGw 200.1.1.1

        meshost create edgeA_vlan200ipv4host1 -skip true

        :param bridge_name:
        :param basename:
        :param isid_id:
        :param endpoint_ip:
        :param endpoint_mask:
        :param endpoint_gateway:
        :param endpoint_mac:
        :param num_eps:
        :param options:
        :return:
        """
        self.logger.log_debug("create_routed_l2vsn_ipv4_endpoint()")
        try:
            # dev = self.get_device()
            if not isinstance(num_eps, int):
                self.logger.log_error("Number of Endpoints needs to be a number value=" + str(num_eps))
            create_routed_l2_vsn_endpoints = " -bridgeName " + str(bridge_name) + \
                " -basename " + str(basename) + \
                " -isidId " + str(isid_id) + \
                " -numEps " + str(num_eps) + \
                " -epMac " + str(endpoint_mac) + \
                " -epIp " + str(endpoint_ip) + \
                " -epMask " + str(endpoint_mask) + \
                " -epGw " + str(endpoint_gateway)
            self.send_command("bridge createRoutedL2VsnEndPoints " + create_routed_l2_vsn_endpoints)
            index = 1
            while index <= num_eps:
                self.send_command("meshost create " + str(basename) + str(index) + " -skip true")
                index += 1
        except Exception:
            self.logger.log_debug(StringUtils.exception_to_string())

    def create_l2vsn_ipv4_endpoint(self, bridge_name, basename, isid_id, endpoint_ip, endpoint_mask, endpoint_mac,
                                   num_eps=1, options=None):
        """
        bridge createL2VsnEndPoints -bridgeName edgeB -basename edgeB_vlan200ipv4host -isidId 200 -numEps 1
        -epMac 00:bb:c8:bb:c8:bb -epIp 200.1.1.201 -epMask 255.255.255.0

        meshost create edgeB_vlan200ipv4host1 -skip true

        :param bridge_name:
        :param basename:
        :param isid_id:
        :param endpoint_ip:
        :param endpoint_mask:
        :param endpoint_mac:
        :param num_eps:
        :param options:
        :return:
        """
        self.logger.log_debug("create_l3vsn_ipv4_endpoint()")
        try:
            # dev = self.get_device()
            if not isinstance(num_eps, int):
                self.logger.log_error("Number of Endpoints needs to be a number value=" + str(num_eps))
            create_l2_vsn_endpoints = " -bridgeName " + str(bridge_name) + \
                " -basename " + str(basename) + \
                " -isidId " + str(isid_id) + \
                " -numEps " + str(num_eps) + \
                " -epMac " + str(endpoint_mac) + \
                " -epIp " + str(endpoint_ip) + \
                " -epMask " + str(endpoint_mask)
            self.send_command("bridge createL2VsnEndPoints " + create_l2_vsn_endpoints)
            index = 1
            while index <= num_eps:
                self.send_command("meshost create " + str(basename) + str(index) + " -skip true")
                index += 1
        except Exception:
            self.logger.log_debug(StringUtils.exception_to_string())

    def create_routed_l2vsn_ipv6_endpoint(self, bridge_name, basename, isid_id, endpoint_ip, endpoint_prefix_length,
                                          endpoint_mac, num_eps=1, options=None):
        """
        bridge createRoutedL2VsnEndPoints -bridgeName edgeB -basename edgeB_vlan201ipv6host -isidId 201 -numEps 1
        -epMac 00:bb:c9:00:c8:bb -epIp 1017::201 -preFixLen 64 -epGw NA

        meshost create edgeB_vlan201ipv6host -skip true

        :param bridge_name:
        :param basename:
        :param isid_id:
        :param endpoint_ip:
        :param endpoint_prefix_length:
        :param endpoint_mac:
        :param num_eps:
        :param options:
        :return:
        """
        self.logger.log_debug("create_routed_l2vsn_ipv4_endpoint()")
        try:
            # dev = self.get_device()
            if not isinstance(num_eps, int):
                self.logger.log_error("Number of Endpoints needs to be a number value=" + str(num_eps))
            create_routed_l2_vsn_endpoints = " -bridgeName " + str(bridge_name) + \
                " -basename " + str(basename) + \
                " -isidId " + str(isid_id) + \
                " -numEps " + str(num_eps) + \
                " -epMac " + str(endpoint_mac) + \
                " -epIp " + str(endpoint_ip) + \
                " -preFixLen " + str(endpoint_prefix_length) + \
                " -epGw NA"
            self.send_command("bridge createRoutedL2VsnEndPoints " + create_routed_l2_vsn_endpoints)
            index = 1
            while index <= num_eps:
                self.send_command("meshost create " + str(basename) + str(index) + " -skip true")
                index += 1
        except Exception:
            self.logger.log_debug(StringUtils.exception_to_string())

    def create_l2vsn_ipv6_endpoint(self, bridge_name, basename, isid_id, endpoint_ip, endpoint_prefix_length,
                                   endpoint_mac, num_eps=1, options=None):
        """
        bridge createL2VsnEndPoints -bridgeName edgeA -basename edgeA_vlan201ipv6host -isidId 201 -numEps 1
        -epMac 00:aa:c9:00:c8:aa -epIp 1017::200 -preFixLen 64

        meshost create edgeA_vlan201ipv6host -skip true

        :param bridge_name:
        :param basename:
        :param isid_id:
        :param endpoint_ip:
        :param endpoint_prefix_length:
        :param endpoint_mac:
        :param num_eps:
        :param options:
        :return:
        """
        self.logger.log_debug("create_l3vsn_ipv4_endpoint()")
        try:
            # dev = self.get_device()
            if not isinstance(num_eps, int):
                self.logger.log_error("Number of Endpoints needs to be a number value=" + str(num_eps))
            create_l2_vsn_endpoints = " -bridgeName " + str(bridge_name) + \
                " -basename " + str(basename) + \
                " -isidId " + str(isid_id) + \
                " -numEps " + str(num_eps) + \
                " -epMac " + str(endpoint_mac) + \
                " -epIp " + str(endpoint_ip) + \
                " -preFixLen " + str(endpoint_prefix_length)
            self.send_command("bridge createL2VsnEndPoints " + create_l2_vsn_endpoints)
            index = 1
            while index <= num_eps:
                self.send_command("meshost create " + str(basename) + str(index) + " -skip true")
                index += 1
        except Exception:
            self.logger.log_debug(StringUtils.exception_to_string())

    def create_l3vsn_ipv4_endpoint(self, bridge_name, basename, isid_id, starting_ip, endpoint_ip, endpoint_mask,
                                   num_eps=1, num_routes=1, cost=1, step=1, options=None):
        """
        bridge createL3VsnEndPoints -bridgeName edgeA -basename edgeA_blue -epIp 19.74.6.5 -numEps 1 -l3isid 682007
        -epMask 255.255.255.0

        meshost create edgeA_blue1 -skip true

        bridge configIpVpnReach -bridgeName edgeA -startingIp 19.74.6.0 -mask 255.255.255.0 -num_routes 15 -cost 1
        -step 1 -updown true -isid 682007

        :param bridge_name:
        :param basename:
        :param isid_id:
        :param starting_ip:
        :param endpoint_ip:
        :param endpoint_mask:
        :param num_eps:
        :param num_routes:
        :param cost:
        :param step:
        :param options:
        :return:
        """
        self.logger.log_debug("create_l3vsn_ipv4_endpoint()")
        try:
            # dev = self.get_device()
            if not isinstance(num_eps, int):
                self.logger.log_error("Number of Endpoints needs to be a number value=" + str(num_eps))
            create_l3_vsn_endpoints = " -bridgeName " + str(bridge_name) + \
                " -basename " + str(basename) + \
                " -epIp " + str(endpoint_ip) + \
                " -numEps " + str(num_eps) + \
                " -l3isid " + str(isid_id) + \
                " -epMask " + str(endpoint_mask)
            self.send_command("bridge createL3VsnEndPoints " + create_l3_vsn_endpoints)
            index = 1
            while index <= num_eps:
                self.send_command("meshost create " + str(basename) + str(index) + " -skip true")
                index += 1
            config_ip_vpn_reach = " -bridgeName " + str(bridge_name) + \
                " -startingIp " + starting_ip + \
                " -mask " + str(endpoint_mask) + \
                " -num_routes " + str(num_routes) + \
                " -cost " + str(cost) + \
                " -step " + str(step) + \
                " -updown true " \
                "-isid " + str(isid_id)
            self.send_command("bridge configIpVpnReach " + config_ip_vpn_reach)
        except Exception:
            self.logger.log_debug(StringUtils.exception_to_string())

    def create_l3vsn_ipv6_endpoint(self, bridge_name, basename, isid_id, starting_ip, endpoint_ip, prefix_length,
                                   num_eps=1, num_routes=1, cost=1, step=1, options=None):
        """
        bridge createL3VsnEndPoints -bridgeName edgeB -basename edgeB_blue -epIp 6:8:2007::10 -numEps 1 -l3isid 682007
        -preFixLen 64

        meshost create edgeB_blue1 -skip true

        bridge configIsisExtIpv6Reach -bridgeName edgeB -startingIp 6:8:2007:: -preFixLen 64 -num_routes 1 -cost 1
        -step 1 -l3isid 682007

        :param bridge_name:
        :param basename:
        :param isid_id:
        :param starting_ip:
        :param endpoint_ip:
        :param prefix_length:
        :param num_eps:
        :param num_routes:
        :param cost:
        :param step:
        :param options:
        :return:
        """
        self.logger.log_debug("create_l3vsn_ipv6_endpoint()")
        try:
            # dev = self.get_device()
            if not isinstance(num_eps, int):
                self.logger.log_error("Number of Endpoints needs to be a number value=" + str(num_eps))
            create_l3_vsn_endpoints = " -bridgeName " + str(bridge_name) + \
                " -basename " + str(basename) + \
                " -epIp " + str(endpoint_ip) + \
                " -numEps " + str(num_eps) + \
                " -l3isid " + str(isid_id) + \
                " -preFixLen " + str(prefix_length)
            self.send_command("bridge createL3VsnEndPoints " + create_l3_vsn_endpoints)
            index = 1
            while index <= num_eps:
                self.send_command("meshost create " + str(basename) + str(index) + " -skip true")
                index += 1
            config_isis_ext_ipv6_reach = " -bridgeName " + str(bridge_name) + \
                " -startingIp " + starting_ip + \
                " -preFixLen " + str(prefix_length) + \
                " -num_routes " + str(num_routes) + \
                " -cost " + str(cost) + \
                " -step " + str(step) + \
                " -updown true " \
                "-isid " + str(isid_id)
            self.send_command("bridge configIsisExtIpv6Reach " + config_isis_ext_ipv6_reach)
        except Exception:
            self.logger.log_debug(StringUtils.exception_to_string())
