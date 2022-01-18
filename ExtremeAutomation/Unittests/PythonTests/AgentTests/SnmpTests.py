import pysnmp.hlapi as api
from ExtremeAutomation.Unittests.Utilities.RobotUnitTest import RobotUnitTest
from ExtremeAutomation.Library.Device.NetworkElement.NetworkElement import NetworkElement
from ExtremeAutomation.Library.Device.Common.Agents.SnmpAgent import SnmpAgent, SnmpConstants
from ExtremeAutomation.Library.Device.Common.CommandObjects.SnmpCommandObject import SnmpCommandObject
from ExtremeAutomation.Library.Device.NetworkElement.Constants.NetworkElementConstants import NetworkElementConstants
from ExtremeAutomation.Keywords.Utils.DeviceCollectionManager import DeviceCollectionManager


class SnmpTests(RobotUnitTest):
    @classmethod
    def setUpClass(cls):
        cls.dev = NetworkElement(NetworkElementConstants.OS_EXOS, NetworkElementConstants.PLATFORM_BASE,
                                 NetworkElementConstants.UNIT_BASE, NetworkElementConstants.VERSION_BASE)
        cls.dev.hostname = "10.52.15.22"
        cls.dev.name = "DUT"
        cls.dcm = DeviceCollectionManager()
        cls.dcm.add_device(cls.dev.name, cls.dev)

    def test_get_command_type_get(self):
        snmp_agent = self.__get_snmp_agent()
        self.assertEqual(snmp_agent.get_command_type(SnmpConstants.SNMP_GET_CMD), api.getCmd)

    def test_get_command_type_set(self):
        snmp_agent = self.__get_snmp_agent()
        self.assertEqual(snmp_agent.get_command_type(SnmpConstants.SNMP_SET_CMD), api.setCmd)

    def test_get_command_type_get_next(self):
        snmp_agent = self.__get_snmp_agent()
        self.assertEqual(snmp_agent.get_command_type(SnmpConstants.SNMP_GET_NEXT_CMD), api.nextCmd)

    def test_get_command_type_walk(self):
        snmp_agent = self.__get_snmp_agent()
        self.assertEqual(snmp_agent.get_command_type(SnmpConstants.SNMP_WALK_CMD), api.nextCmd)

    def test_get_command_type_bulk_walk(self):
        snmp_agent = self.__get_snmp_agent()
        self.assertEqual(snmp_agent.get_command_type(SnmpConstants.SNMP_BULK_WALK_CMD), api.bulkCmd)

    def test_get_command_type_bad_command_type(self):
        snmp_agent = self.__get_snmp_agent()
        self.assertRaises(ValueError, snmp_agent.get_command_type, "bad_command_type")

    def test_get_data_type_none(self):
        snmp_agent = self.__get_snmp_agent()
        self.assertEqual(snmp_agent.get_data_type(None), api.Integer)

    def test_get_data_type_integer(self):
        snmp_agent = self.__get_snmp_agent()
        self.assertEqual(snmp_agent.get_data_type(SnmpConstants.DATA_TYPE_INTEGER), api.Integer)

    def test_get_data_type_unsigned_32(self):
        snmp_agent = self.__get_snmp_agent()
        self.assertEqual(snmp_agent.get_data_type(SnmpConstants.DATA_TYPE_UNSIGNED_32), api.Unsigned32)

    def test_get_data_type_time_ticks(self):
        snmp_agent = self.__get_snmp_agent()
        self.assertEqual(snmp_agent.get_data_type(SnmpConstants.DATA_TYPE_TIME_TICKS), api.TimeTicks)

    def test_get_data_type_ip_addr(self):
        snmp_agent = self.__get_snmp_agent()
        self.assertEqual(snmp_agent.get_data_type(SnmpConstants.DATA_TYPE_IP_ADDR), api.IpAddress)

    def test_get_data_type_bits(self):
        snmp_agent = self.__get_snmp_agent()
        self.assertEqual(snmp_agent.get_data_type(SnmpConstants.DATA_TYPE_BITS), api.Bits)

    def test_get_data_type_obj_id(self):
        snmp_agent = self.__get_snmp_agent()
        self.assertEqual(snmp_agent.get_data_type(SnmpConstants.DATA_TYPE_OBJ_ID), api.ObjectIdentifier)

    def test_get_data_type_oct_str(self):
        snmp_agent = self.__get_snmp_agent()
        self.assertEqual(snmp_agent.get_data_type(SnmpConstants.DATA_TYPE_OCT_STR), api.OctetString)

    def test_get_data_type_bad_data_type(self):
        snmp_agent = self.__get_snmp_agent()
        self.assertRaises(ValueError, snmp_agent.get_data_type, "bad_data_type")

    def test_send_command_object_v1(self):
        snmp_agent = self.__get_snmp_agent_v1()
        snmp_cmd_obj_1 = self.__create_command_object(SnmpConstants.SNMP_GET_CMD, "1.3.6.1.2.1.1.5.0", None, None)
        snmp_cmd_obj_2 = self.__create_command_object(SnmpConstants.SNMP_SET_CMD, "1.3.6.1.2.1.1.5.0",
                                                      SnmpConstants.DATA_TYPE_OCT_STR, "test_value")

        def_val = snmp_agent.send_command_object(snmp_cmd_obj_1).return_text.split(" = ")[1]
        snmp_agent.send_command_object(snmp_cmd_obj_2)
        self.assertIn("test_value", snmp_agent.send_command_object(snmp_cmd_obj_1).return_text)

        snmp_cmd_obj_3 = self.__create_command_object(SnmpConstants.SNMP_SET_CMD, "1.3.6.1.2.1.1.5.0",
                                                      SnmpConstants.DATA_TYPE_OCT_STR, def_val)
        snmp_agent.send_command_object(snmp_cmd_obj_3)

    def test_send_command_object_v2(self):
        snmp_agent = self.__get_snmp_agent_v2()
        snmp_cmd_obj_1 = self.__create_command_object(SnmpConstants.SNMP_GET_CMD, "1.3.6.1.2.1.1.5.0", None, None)
        snmp_cmd_obj_2 = self.__create_command_object(SnmpConstants.SNMP_SET_CMD, "1.3.6.1.2.1.1.5.0",
                                                      SnmpConstants.DATA_TYPE_OCT_STR, "test_value")

        def_val = snmp_agent.send_command_object(snmp_cmd_obj_1).return_text.split(" = ")[1]
        snmp_agent.send_command_object(snmp_cmd_obj_2)
        self.assertIn("test_value", snmp_agent.send_command_object(snmp_cmd_obj_1).return_text)

        snmp_cmd_obj_3 = self.__create_command_object(SnmpConstants.SNMP_SET_CMD, "1.3.6.1.2.1.1.5.0",
                                                      SnmpConstants.DATA_TYPE_OCT_STR, def_val)
        snmp_agent.send_command_object(snmp_cmd_obj_3)

    def test_send_command_object_v3(self):
        snmp_agent = self.__get_snmp_agent_v3()
        snmp_cmd_obj_1 = self.__create_command_object(SnmpConstants.SNMP_GET_CMD, "1.3.6.1.2.1.1.5.0", None, None)
        snmp_cmd_obj_2 = self.__create_command_object(SnmpConstants.SNMP_SET_CMD, "1.3.6.1.2.1.1.5.0",
                                                      SnmpConstants.DATA_TYPE_OCT_STR, "test_value")

        def_val = snmp_agent.send_command_object(snmp_cmd_obj_1).return_text.split(" = ")[1]
        snmp_agent.send_command_object(snmp_cmd_obj_2)
        self.assertIn("test_value", snmp_agent.send_command_object(snmp_cmd_obj_1).return_text)

        snmp_cmd_obj_3 = self.__create_command_object(SnmpConstants.SNMP_SET_CMD, "1.3.6.1.2.1.1.5.0",
                                                      SnmpConstants.DATA_TYPE_OCT_STR, def_val)
        snmp_agent.send_command_object(snmp_cmd_obj_3)

    def __get_snmp_agent(self):
        snmp_agent = SnmpAgent(self.dev)
        return snmp_agent

    def __get_snmp_agent_v1(self):
        snmp_agent = self.__get_snmp_agent()
        snmp_agent.snmp_version = SnmpConstants.SNMP_VER_1
        snmp_agent.community_name = "extreme123"
        return snmp_agent

    def __get_snmp_agent_v2(self):
        snmp_agent = self.__get_snmp_agent()
        snmp_agent.snmp_version = SnmpConstants.SNMP_VER_2
        snmp_agent.community_name = "extreme123"
        return snmp_agent

    def __get_snmp_agent_v3(self):
        snmp_agent = self.__get_snmp_agent()
        snmp_agent.snmp_version = SnmpConstants.SNMP_VER_3
        snmp_agent.user_name = "user_md5_des"
        snmp_agent.auth_protocol = SnmpConstants.SNMP_AUTH_MD5
        snmp_agent.auth_password = "extreme123"
        snmp_agent.privacy_protocol = SnmpConstants.SNMP_PRIV_DES
        snmp_agent.privacy_password = "extreme123"
        return snmp_agent

    @staticmethod
    def __create_command_object(cmd_type, oid, data_type, value):
        cmd_obj = SnmpCommandObject()
        cmd_obj.command_type = cmd_type
        cmd_obj.oid = oid
        cmd_obj.data_type = data_type
        cmd_obj.value = value
        return cmd_obj


if __name__ == '__main__':
    RobotUnitTest.main()
