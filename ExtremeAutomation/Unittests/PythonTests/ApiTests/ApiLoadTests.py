from ExtremeAutomation.Unittests.Utilities.RobotUnitTest import RobotUnitTest
from ExtremeAutomation.Library.Device.NetworkElement.Constants.NetworkElementConstants import NetworkElementConstants
from ExtremeAutomation.Library.Device.NetworkElement.NetworkElement import NetworkElement
from ExtremeAutomation.Library.Device.Common.Agents.AgentConstants import AgentConstants


DEVICE_OS = NetworkElementConstants.OS_EXOS
DEVICE_PLATFORM = NetworkElementConstants.PLATFORM_BASE
DEVICE_VERSION = NetworkElementConstants.VERSION_BASE
DEVICE_UNIT = NetworkElementConstants.UNIT_BASE


class UnitTestCasesApiLoad(RobotUnitTest):
    @classmethod
    def setUpClass(cls):
        cls.device = NetworkElement(DEVICE_OS, DEVICE_PLATFORM, DEVICE_UNIT, DEVICE_VERSION)
        cls.device.connection_method = AgentConstants.TYPE_TELNET

    def check_api(self, api):
        self.assertIsNotNone(api)

    def test_bonding(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_BONDING)
        self.check_api(api)

    def test_filemanagement(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_FILEMANAGEMENT)
        self.check_api(api)

    def test_hostdos(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_HOSTDOS)
        self.check_api(api)

    def test_licensing(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_LICENSING)
        self.check_api(api)

    def test_lsnat(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_LSNAT)
        self.check_api(api)

    def test_nat(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_NAT)
        self.check_api(api)

    def test_pinger(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_PINGER)
        self.check_api(api)

    def test_resetdevice(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_RESETDEVICE)
        self.check_api(api)

    def test_rmon(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_RMON)
        self.check_api(api)

    def test_setsystem(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_SETSYSTEM)
        self.check_api(api)

    def test_snmp(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_SNMP)
        self.check_api(api)

    def test_ssh(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_SSH)
        self.check_api(api)

    def test_switchstacking(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_SWITCHSTACKING)
        self.check_api(api)

    def test_ethernetoam(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_ETHERNETOAM)
        self.check_api(api)

    def test_flowlimit(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_FLOWLIMIT)
        self.check_api(api)

    def test_general(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_GENERAL)
        self.check_api(api)

    def test_lldp(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_LLDP)
        self.check_api(api)

    def test_poe(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_POE)
        self.check_api(api)

    def test_port(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_PORT)
        self.check_api(api)

    def test_cdp(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_CDP)
        self.check_api(api)

    def test_cfm(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_CFM)
        self.check_api(api)

    def test_dot1p(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_DOT1P)
        self.check_api(api)

    def test_fdb(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_FDB)
        self.check_api(api)

    def test_garp(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_GARP)
        self.check_api(api)

    def test_gvrp(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_GVRP)
        self.check_api(api)

    def test_igmp(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_IGMP)
        self.check_api(api)

    def test_lacp(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_LACP)
        self.check_api(api)

    def test_mirror(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_MIRRORING)
        self.check_api(api)

    def test_mld(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_MLD)
        self.check_api(api)

    def test_mvrp(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_MVRP)
        self.check_api(api)

    def test_netflow(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_NETFLOW)
        self.check_api(api)

    def test_portmirroring(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_PORTMIRRORING)
        self.check_api(api)

    def test_spanningtree(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_SPANNINGTREE)
        self.check_api(api)

    def test_spb(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_SPB)
        self.check_api(api)

    def test_vlan(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_VLAN)
        self.check_api(api)

    def test_addressfamily(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_ADDRESSFAMILY)
        self.check_api(api)

    def test_arp(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_ARP)
        self.check_api(api)

    def test_bgp(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_BGP)
        self.check_api(api)

    def test_dvmrp(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_DVMRP)
        self.check_api(api)

    def test_ecmforwarding(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_ECMFORWARDING)
        self.check_api(api)

    def test_interface(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_INTERFACE)
        self.check_api(api)

    def test_iprouting(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_IPROUTING)
        self.check_api(api)

    def test_isis(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_ISIS)
        self.check_api(api)

    def test_msdp(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_MSDP)
        self.check_api(api)

    def test_nd(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_ND)
        self.check_api(api)

    def test_ospf(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_OSPF)
        self.check_api(api)

    def test_pim(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_PIM)
        self.check_api(api)

    def test_probe(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_PROBE)
        self.check_api(api)

    def test_rip(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_RIP)
        self.check_api(api)

    def test_track(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_TRACK)
        self.check_api(api)

    def test_tunnel(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_TUNNEL)
        self.check_api(api)

    def test_vrf(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_VRF)
        self.check_api(api)

    def test_vrrp(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_VRRP)
        self.check_api(api)

    def test_cos(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_COS)
        self.check_api(api)

    def test_acl(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_ACL)
        self.check_api(api)

    def test_antispoof(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_ANTISPOOF)
        self.check_api(api)

    def test_autotracking(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_AUTOTRACKING)
        self.check_api(api)

    def test_cep(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_CEP)
        self.check_api(api)

    def test_dot1x(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_DOT1X)
        self.check_api(api)

    def test_macauth(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_MACAUTH)
        self.check_api(api)

    def test_maclock(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_MACLOCK)
        self.check_api(api)

    def test_macsec(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_MACSEC)
        self.check_api(api)

    def test_multiauth(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_MULTIAUTH)
        self.check_api(api)

    def test_netlogin(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_NETLOGIN)
        self.check_api(api)

    def test_policy(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_POLICY)
        self.check_api(api)

    def test_quarantineagent(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_QUARANTINEAGENT)
        self.check_api(api)

    def test_radius(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_RADIUS)
        self.check_api(api)

    def test_radiussnooping(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_RADIUSSNOOPING)
        self.check_api(api)

    def test_sysauth(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_SYSAUTH)
        self.check_api(api)

    def test_vlanauth(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_VLANAUTH)
        self.check_api(api)

    def test_chassis(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_CHASSIS)
        self.check_api(api)

    def test_prompt(self):
        api = self.device.api_factory.get_api(self.device, NetworkElementConstants.API_PROMPT)
        self.check_api(api)


if __name__ == '__main__':
    RobotUnitTest.main()
