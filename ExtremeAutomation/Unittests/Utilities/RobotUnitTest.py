import sys
import unittest
import xmlrunner
from ExtremeAutomation.Library.Logger.Logger import Logger
from ExtremeAutomation.Library.Utils.CollectionUtils import CollectionUtils
from ExtremeAutomation.Library.Device.NetworkElement.NetworkElement import NetworkElement
from ExtremeAutomation.Library.Device.UiElement.UiElement import UiElement
from ExtremeAutomation.Library.Device.NetworkElement.Constants.NetworkElementConstants import NetworkElementConstants
from ExtremeAutomation.Library.Device.UiElement.Constants.UiElementConstants import UiElementConstants
from ExtremeAutomation.Keywords.NetworkElementKeywords.NetworkElementConnectionManager import \
    NetworkElementConnectionManager
from ExtremeAutomation.Keywords.TrafficKeywords.TrafficGeneratorConnectionManager import \
    TrafficGeneratorConnectionManager


class RobotUnitTest(unittest.TestCase):
    Logger().console_level = Logger.ALL
    constants = NetworkElementConstants()
    ui_constants = UiElementConstants()
    boss_dev = None
    eos_dev = None
    exos_dev = None
    ecos_dev = None
    linux_dev = None
    extr_wireless_dev = None
    zebra_wireless_dev = None
    snap_route_dev = None
    voss_dev = None
    jets_dev = None
    alpha_dev = None
    eos_stacks_dev = None
    slx_dev = None
    env = None
    dummy_devices = {}

    @classmethod
    def create_devices(cls):
        cls.eos_dev = NetworkElement(cls.constants.OS_EOS, cls.constants.PLATFORM_BASE,
                                     cls.constants.UNIT_BASE, cls.constants.VERSION_BASE)
        cls.exos_dev = NetworkElement(cls.constants.OS_EXOS, cls.constants.PLATFORM_BASE,
                                      cls.constants.UNIT_BASE, cls.constants.VERSION_BASE)
        cls.xmc_dev = UiElement(cls.ui_constants.APP_EMC, cls.ui_constants.APP_VER_BASE)

        # Configure EOS device values.
        cls.eos_dev.hostname = "10.52.15.21"
        cls.eos_dev.username = "admin"
        cls.eos_dev.password = "extremeROBOT"
        cls.eos_dev.login_prompt = "Username:"
        cls.eos_dev.pass_prompt = "Password:"
        cls.eos_dev.main_prompt = "->"
        cls.eos_dev.console_ip = "10.52.15.4"
        cls.eos_dev.console_port = "10031"

        cls.eos_env = CollectionUtils.parse_yaml("ExtremeAutomation/Unittests/Resources/tor_1node_1.yaml")
        cls.netelem1 = cls.eos_env["netelem1"]["name"]
        cls.eos_netelem_port = cls.eos_env["netelem1"]["tgen"]["port_a"]["ifname"]
        cls.eos_netelem_port_b = cls.eos_env["netelem1"]["tgen"]["port_b"]["ifname"]
        cls.eos_tgen_port = cls.eos_env["tgen_ports"]["netelem1"]["port_a"]
        cls.eos_snmp_info = {
            "snmp_version": cls.eos_env["netelem1"]["snmp_version"],
            "snmp_community_name": cls.eos_env["netelem1"]["snmp_community_name"],
            "snmp_user_name": cls.eos_env["netelem1"]["snmp_user_name"],
            "snmp_auth_protocol": cls.eos_env["netelem1"]["snmp_auth_protocol"],
            "snmp_auth_password": cls.eos_env["netelem1"]["snmp_auth_password"],
            "snmp_privacy_protocol": cls.eos_env["netelem1"]["snmp_privacy_protocol"],
            "snmp_privacy_password": cls.eos_env["netelem1"]["snmp_privacy_password"]
            }

        # Configure EXOS device values.
        cls.exos_dev.hostname = "10.52.15.22"
        cls.exos_dev.username = "admin"
        cls.exos_dev.password = "extremeROBOT"
        cls.exos_dev.login_prompt = "login:"
        cls.exos_dev.pass_prompt = "password:"
        cls.exos_dev.main_prompt = "# "
        cls.exos_dev.console_ip = "10.52.15.4"
        cls.exos_dev.console_port = "10032"

        cls.exos_env = CollectionUtils.parse_yaml("ExtremeAutomation/Unittests/Resources/x450g2_1node_1.yaml")
        cls.netelem2 = cls.exos_env["netelem1"]["name"]
        cls.exos_netelem_port = cls.exos_env["netelem1"]["tgen"]["port_a"]["ifname"]
        cls.exos_netelem_port_b = cls.exos_env["netelem1"]["tgen"]["port_b"]["ifname"]
        cls.exos_tgen_port = cls.exos_env["tgen_ports"]["netelem1"]["port_a"]
        cls.exos_snmp_info = {
            "snmp_version": cls.exos_env["netelem1"]["snmp_version"],
            "snmp_community_name": cls.exos_env["netelem1"]["snmp_community_name"],
            "snmp_user_name": cls.exos_env["netelem1"]["snmp_user_name"],
            "snmp_auth_protocol": cls.exos_env["netelem1"]["snmp_auth_protocol"],
            "snmp_auth_password": cls.exos_env["netelem1"]["snmp_auth_password"],
            "snmp_privacy_protocol": cls.exos_env["netelem1"]["snmp_privacy_protocol"],
            "snmp_privacy_password": cls.exos_env["netelem1"]["snmp_privacy_password"]
        }

        # Configure XMC device values.
        cls.xmc_env = CollectionUtils.parse_yaml("ExtremeAutomation/Unittests/Resources/2node_1.yaml")
        cls.uielem1 = cls.xmc_env["uielem1"]["name"]
        cls.xmc_dev.hostname = cls.xmc_env["uielem1"]["ip"]
        cls.xmc_dev.url = cls.xmc_env["uielem1"]["url"]
        cls.xmc_dev.username = cls.xmc_env["uielem1"]["username"]
        cls.xmc_dev.password = cls.xmc_env["uielem1"]["password"]
        cls.xmc_dev.connection_method = cls.xmc_env["uielem1"]["agent"]
        cls.xmc_dev.application = cls.xmc_env["uielem1"]["application"]
        cls.xmc_dev.port = cls.xmc_env["uielem1"]["port"]
        cls.xmc_dev.app_version = cls.xmc_env["uielem1"]["app_version"]

    @classmethod
    def create_dummy_devices(cls):
        """
        This function creates a dummy device object for each OS_x value found in NetworkElementConstants.
        These should only be used as mock devices, they do not exist and cannot be connected to.
        """
        dev_os = [i for i in dir(cls.constants) if i.startswith("OS_")]

        for index, oper_sys in enumerate(dev_os):
            obj_name = oper_sys[3::].lower() + "_dev"
            netelem = NetworkElement(getattr(cls.constants, oper_sys), cls.constants.PLATFORM_BASE,
                                     cls.constants.UNIT_BASE, cls.constants.VERSION_BASE)
            netelem.hostname = str(index) + "." + str(index) + "." + str(index) + "." + str(index)
            netelem.username = "username"
            netelem.password = "password"
            netelem.login_prompt = "login_prompt"
            netelem.pass_prompt = "pass_prompt"
            netelem.main_prompt = "main_prompt"
            cls.dummy_devices[oper_sys[3::].lower()] = netelem
            setattr(cls, obj_name, netelem)

    @classmethod
    def connect_to_devices(cls):
        cls.eos_dev.connect()
        cls.exos_dev.connect()

    @classmethod
    def disconnect_from_devices(cls):
        cls.eos_dev.disconnect()
        cls.exos_dev.disconnect()

    @classmethod
    def keyword_connect_devices(cls):
        cls.create_devices()
        connect = NetworkElementConnectionManager()
        cls.env = CollectionUtils.parse_yaml("ExtremeAutomation/Unittests/Resources/2node_1.yaml")

        connect.connect_to_all_network_elements(yaml_dict=cls.env)

    @classmethod
    def keyword_disconnect_devices(cls):
        connect = NetworkElementConnectionManager()
        if cls.env is not None:
            connect.close_connection_to_all_network_elements(yaml_dict=cls.env)

    @classmethod
    def keyword_connect_tgens(cls):
        connect = TrafficGeneratorConnectionManager()
        connect.connect_to_all_traffic_generators(yaml_dict=cls.env)

    @classmethod
    def keyword_disconnect_tgens(cls):
        connect = TrafficGeneratorConnectionManager()
        if cls.env is not None:
            connect.close_connection_to_all_traffic_generators(yaml_dict=cls.env)

    @staticmethod
    def main():
        try:
            report_dir = sys.argv[1:][0]
            del sys.argv[1:]
            unittest.main(testRunner=xmlrunner.XMLTestRunner(output=report_dir))
        except IndexError:
            unittest.main()
