from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.NetworkEmulatingDvrApi import \
    NetworkEmulatingDvrApi, DvrHost
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils
from collections import OrderedDict


class JetsDvrApi(NetworkEmulatingDvrApi):
    def __init__(self, device):
        super(JetsDvrApi, self).__init__(device)

    def get_all_dvr_enties(self, bridge_name):
        self.logger.log_debug("get_all_dvr_enties()")
        try:
            # dev = self.get_device()
            order_dict = OrderedDict()
            order_dict["bridgeName"] = bridge_name
            order_dict["l3isid"] = str(0)
            order_dict["l2isid"] = str(0)
            order_dict["bmac"] = str("0:0:0:0:0:0")
            order_dict["maskLen"] = str(24)
            order_dict["network"] = str("1.1.1.1")
            order_dict["domainId"] = str(25)
            create_core_plsb_interface = " ".join('-{} {}'.format(key, value) for key, value in order_dict.items())
            cmd_obj = self.send_command_no_parse("bridge verifyLearnedDvrRoute " + create_core_plsb_interface)
            if len(cmd_obj.return_text) < 0:
                return []
            index = 0
            while len(cmd_obj.return_text) < 0 > index and " in " not in str(cmd_obj.return_text[index]):
                index += 1
            ptext = "".join(cmd_obj.return_text[index:])
            ptext = ptext.split(" in ")
            ptext = "".join(ptext[1:])
            if ptext.startswith("{"):
                ptext = ", " + ptext[1:]
            if ptext.endswith("]"):
                ptext = ptext[:-1]
            dbp_id_blocks = ptext.split(', DbpId srcId')
            index = 0
            while len(dbp_id_blocks) > index:
                if len(dbp_id_blocks[index]) > 0:
                    dbp_id_blocks[index] = "DbpId srcId" + dbp_id_blocks[index]
                index += 1
            dvr_hosts = []
            for block in dbp_id_blocks:
                if block != "":
                    host = DvrHost()
                    host.process_jets_info(block)
                    self.logger.log_info(block)
                    dvr_hosts.append(host)
            return dvr_hosts

        except Exception:
            self.logger.log_debug(StringUtils.exception_to_string())

    # JETS_SIM>bridge addDvrGw -bridgeName edgeA -l3isid 0 -l2isid 999 -cmac 0:0:0:0:0:0 -maskLen 24 -gateway 10.10.10.1
    # -vrfId 0 -vlan_ip_interface 10.10.10.2
    # Created DvrIpv4GatewayTlv:0:999:10.10.10.1:24:0:0:0:e:a:f:0:0:0:e:a:62:0:0:0:e:a:f and 10.10.10.1
    def add_dvr_gateway(self, bridge_name, l3_isid, l2_isid, cmac, mask_length, gateway, vlan_ip_interface):
        self.logger.log_debug("add_dvr_gateway()")
        try:
            # dev = self.get_device()
            create_isid_endpoints = " -bridgeName " + str(bridge_name) + \
                " -l3isid " + str(l3_isid) + \
                " -l2isid " + str(l2_isid) + \
                " -cmac " + str(cmac) + \
                " -maskLen " + str(mask_length) + \
                " -gateway " + str(gateway) + \
                " -vrfId 0" + \
                " -vlan_ip_interface " + str(vlan_ip_interface)
            self.send_command("bridge addDvrGw " + create_isid_endpoints)
        except Exception:
            self.logger.log_debug(StringUtils.exception_to_string())

    # JETS_SIM>bridge deleteDvrGw -bridgeName edgeA -l3isid 0 -l2isid 999  -gateway 10.10.10.1
    def delete_dvr_gateway(self, bridge_name, l3_isid, l2_isid, gateway):
        self.logger.log_debug("delete_dvr_gateway()")
        try:
            # dev = self.get_device()
            create_isid_endpoints = " -bridgeName " + str(bridge_name) + \
                " -l3isid " + str(l3_isid) + \
                " -l2isid " + str(l2_isid) + \
                " -gateway " + str(gateway)
            self.send_command("bridge deleteDvrGw " + create_isid_endpoints)
        except Exception:
            self.logger.log_debug(StringUtils.exception_to_string())

    def verify_dvr_gateway(self, bridge_name, l3_isid, l2_isid, cmac, bmac, mask_length, gateway, options=None):
        self.logger.log_debug("verify_dvr_gateway()")
        try:
            if not options:
                options = {}
            # dev = self.get_device()
            order_dict = OrderedDict()
        # JETS_SIM>bridge verifyLearnedDvrGw -bridgeName edgeA -l3isid 0 -l2isid 999 -cmac 0:0:0:0:0:0 -maskLen 24
        # -gateway 10.10.10.1 -vrfId 0 -vlan_ip_interface 10.10.10.2
        # http://avaya-svn.extremenetworks.com/svn/nes/Jets/trunk/src/com/nortel/jets/jetsTcl/bridging/VerifyDvrGw.java
            order_dict["bridgeName"] = bridge_name
            order_dict["l3isid"] = str(l3_isid)
            order_dict["l2isid"] = str(l2_isid)
            order_dict["bmac"] = str(bmac)
            order_dict["cmac"] = str(cmac)
            order_dict["maskLen"] = str(mask_length)
            order_dict["gatewayIp"] = str(gateway)

            for key in options:
                order_dict[key] = options[key]
            create_core_plsb_interface = " ".join('-{} {}'.format(key, value) for key, value in order_dict.items())
            self.send_command("bridge verifyLearnedDvrGw " + create_core_plsb_interface)
        except Exception:
            self.logger.log_debug(StringUtils.exception_to_string())

    # JETS_SIM>bridge addDvrRoute -bridgeName edgeA -l3isid 0 -l2isid 999 -cmac 0:0:0:0:0:0 -maskLen 24
    # -network 10.10.10.0 -nexthop 10.10.10.1 -vrfId 0 -domainId 3
    # Created DvrIpv4RouteTlv:0:999:10.10.10.0:24:0:0:0:e:a:f:0:0:0:e:a:62:3
    def add_dvr_route(self, bridge_name, l3_isid, l2_isid, cmac, mask_length, network_address, next_hop, domain_id):
        self.logger.log_debug("add_dev_route()")
        try:
            # dev = self.get_device()
            create_isid_endpoints = " -bridgeName " + str(bridge_name) + \
                " -l3isid " + str(l3_isid) + \
                " -l2isid " + str(l2_isid) + \
                " -cmac " + str(cmac) + \
                " -maskLen " + str(mask_length) + \
                " -network " + str(network_address) + \
                " -nexthop " + str(next_hop) + \
                " -vrfId 0" + \
                " -domainId " + str(domain_id)
            self.send_command("bridge addDvrRoute " + create_isid_endpoints)
        except Exception:
            self.logger.log_debug(StringUtils.exception_to_string())

    # JETS_SIM>bridge deleteDvrRoute -bridgeName edgeA -l3isid 0 -l2isid 999 -cmac 0:0:0:0:0:0 -maskLen 24
    # -network 10.10.10.0
    def delete_dvr_route(self, bridge_name, l3_isid, l2_isid, cmac, mask_length, network_address):
        self.logger.log_debug("delete_dev_route()")
        try:
            # dev = self.get_device()
            create_isid_endpoints = " -bridgeName " + str(bridge_name) + \
                " -l3isid " + str(l3_isid) + \
                " -l2isid " + str(l2_isid) + \
                " -cmac " + str(cmac) + \
                " -maskLen " + str(mask_length) + \
                " -network " + str(network_address)
            self.send_command("bridge deleteDvrRoute " + create_isid_endpoints)
        except Exception:
            self.logger.log_debug(StringUtils.exception_to_string())

    # JETS_SIM>bridge verifyLearnedDvrRoute -bridgeName edgeA -l3isid 0 -l2isid 999 -cmac 0:0:0:0:0:0 -maskLen 24
    # -network 10.10.10.0 -nexthop 10.10.10.1 -vrfId 0 -domainId 3
    # http://avaya-svn.extremenetworks.com/svn/nes/Jets/trunk/src/com/nortel/jets/jetsTcl/bridging/VerifyDvrRoute.java
    def verify_dvr_route(self, bridge_name, l3_isid, l2_isid, cmac, bmac, mask_length, network_address, domain_id,
                         ctrl=1, cost=1, options=None):
        self.logger.log_debug("verify_dvr_route()")
        try:
            if not options:
                options = {}
            # dev = self.get_device()
            order_dict = OrderedDict()
            order_dict["bridgeName"] = bridge_name
            order_dict["l3isid"] = str(l3_isid)
            order_dict["l2isid"] = str(l2_isid)
            order_dict["cmac"] = str(cmac)
            order_dict["bmac"] = str(bmac)
            order_dict["maskLen"] = str(mask_length)
            order_dict["network"] = str(network_address)
            order_dict["domainId"] = str(domain_id)
            order_dict["ctrl"] = str(ctrl)
            order_dict["cost"] = str(cost)

            for key in options:
                order_dict[key] = options[key]

            create_core_plsb_interface = " ".join('-{} {}'.format(key, value) for key, value in order_dict.items())

            self.send_command("bridge verifyLearnedDvrRoute " + create_core_plsb_interface)
        except Exception:
            self.logger.log_debug(StringUtils.exception_to_string())

    # JETS_SIM>bridge addDvrMcast -bridgeName edgeA -l3isid 0 -l2isid 999 -mcastCfg 1 -igmpVersion 2
    # Created key=0:999 and tlv=DvrMulticastConfigTlv:0:999:1:2:125:100:2:10:1
    def add_dvr_multicast(self, bridge_name, l3_isid, l2_isid, multicast_config, igmp_version):
        self.logger.log_debug("add_dev_multicast()")
        try:
            # dev = self.get_device()
            create_isid_endpoints = " -bridgeName " + str(bridge_name) + \
                " -l3isid " + str(l3_isid) + \
                " -l2isid " + str(l2_isid) + \
                " -mcastCfg " + str(multicast_config) + \
                " -igmpVersion " + str(igmp_version)
            self.send_command("bridge addDvrMcast " + create_isid_endpoints)
        except Exception:
            self.logger.log_debug(StringUtils.exception_to_string())

    # JETS_SIM>bridge deleteDvrMcast -bridgeName edgeA -l3isid 0 -l2isid 999
    def delete_dvr_multicast(self, bridge_name, l3_isid, l2_isid):
        self.logger.log_debug("delete_dev_multicast()")
        try:
            # dev = self.get_device()
            create_isid_endpoints = " -bridgeName " + str(bridge_name) + \
                " -l3isid " + str(l3_isid) + \
                " -l2isid " + str(l2_isid)
            self.send_command("bridge deleteDvrMcast " + create_isid_endpoints)
        except Exception:
            self.logger.log_debug(StringUtils.exception_to_string())

    # JETS_SIM>bridge verifyLearnedDvrMcast -bridgeName edgeA -l3isid 0 -l2isid 999 -mcastCfg 1 -igmpVersion 2
    def verify_dvr_multicast(self, bridge_name, l3_isid, l2_isid, multicast_config, igmp_version=2,
                             igmp_query_interval=0, igmp_query_max_response=0, igmp_robust_value=0,
                             igmp_member_query_interval=0, igmp_ext_compatibility_mode_enable=16777215):
        self.logger.log_debug("verify_dvr_multicast()")
        try:
            # dev = self.get_device()
            order_dict = OrderedDict()
        # JETS_SIM>bridge verifyLearnedDvrMcast -bridgeName edgeA -l3isid 0 -l2isid 999 -cmac 0:0:0:0:0:0 -maskLen 24
        # -network 10.10.10.0 -nexthop 10.10.10.1 -vrfId 0 -domainId 3
        # http://avaya-svn.extremenetworks.com/svn/nes/Jets/trunk/src/com/nortel/jets/jetsTcl/bridging/
        #                                                                                   VerifyDvrMulticastTlv.java
            order_dict["bridgeName"] = bridge_name
            order_dict["l3isid"] = str(l3_isid)
            order_dict["l2isid"] = str(l2_isid)
            order_dict["spb_mcast_config"] = str(multicast_config)
            order_dict["igmp_version_config"] = str(igmp_version)
            order_dict["igmp_query_interval"] = str(igmp_query_interval)
            order_dict["igmp_query_max_response"] = str(igmp_query_max_response)
            order_dict["igmp_robust_value"] = str(igmp_robust_value)
            order_dict["igmp_member_query_interval"] = str(igmp_member_query_interval)
            order_dict["igmp_ext_compatibility_mode_enable"] = str(igmp_ext_compatibility_mode_enable)

            create_core_plsb_interface = " ".join('-{} {}'.format(key, value) for key, value in order_dict.items())

            self.send_command("bridge verifyLearnedDvrRoute " + create_core_plsb_interface)
        except Exception:
            self.logger.log_debug(StringUtils.exception_to_string())

    # JETS_SIM>bridge addHostBehindDvrGw -bridgeName edgeA -l3isid 0 -ipAddr 10.10.10.53 -macAddr 00:00:00:aa:aa:01
    #   -gwAddr 10.10.10.1
    # Created DvrEp:10.10.10.53:Behind:10.10.10.1
    def create_dvr_gw_endpoint(self, bridge_name, l3_sid, starting_ip, mac_address, gateway):
        self.logger.log_debug("create_dvr_gw_endpoint()")
        try:
            # dev = self.get_device()
            create_isid_endpoints = " -bridgeName " + str(bridge_name) + \
                " -l3isid " + str(l3_sid) + \
                " -ipAddr " + str(starting_ip) + \
                " -macAddr " + str(mac_address) + \
                " -gwAddr " + str(gateway)
            self.send_command("bridge addHostBehindDvrGw " + create_isid_endpoints)
        except Exception:
            self.logger.log_debug(StringUtils.exception_to_string())

    # JETS_SIM>bridge verifyLearnedDvrMember -bridgeName edgeA -l3isid 0 -ipAddr 10.10.10.53 -macAddr 00:00:00:aa:aa:01
    # -gwAddr 10.10.10.1
    # http://avaya-svn.extremenetworks.com/svn/nes/Jets/trunk/src/com/nortel/jets/jetsTcl/bridging/VerifyDvrMember.java
    def verify_dvr_member(self, bridge_name, bmac, domain_id, role, domain_isid, code):
        self.logger.log_debug("verify_dvr_member()")
        try:
            # dev = self.get_device()
            order_dict = OrderedDict()
            order_dict["bridgeName"] = bridge_name
            order_dict["bmac"] = str(bmac)
            order_dict["domainId"] = str(domain_id)
            order_dict["role"] = str(role)
            order_dict["domainIsid"] = str(domain_isid)
            order_dict["code"] = str(code)
            create_core_plsb_interface = " ".join('-{} {}'.format(key, value) for key, value in order_dict.items())
            self.send_command("bridge verifyLearnedDvrMember " + create_core_plsb_interface)
        except Exception:
            self.logger.log_debug(StringUtils.exception_to_string())
