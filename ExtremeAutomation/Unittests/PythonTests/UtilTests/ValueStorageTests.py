from ExtremeAutomation.Unittests.Utilities.RobotUnitTest import RobotUnitTest
from ExtremeAutomation.Keywords.Utils.DeviceCollectionManager import DeviceCollectionManager
from ExtremeAutomation.Library.Device.NetworkElement.NetworkElement import NetworkElement
from ExtremeAutomation.Library.Device.NetworkElement.Constants.NetworkElementConstants import NetworkElementConstants
# Test Keywords
from ExtremeAutomation.Keywords.Utils.DeviceValueStorage import DeviceValueStorage


class ValueStorageUnitTests(RobotUnitTest):
    @classmethod
    def setUpClass(cls):
        cls.netelem1 = "netelem1"
        cls.netelem2 = "netelem2"
        cls.value_a = "123456789"
        cls.value_b = "987654321"
        cls.value_c = "12345678987654321"
        cls.storage = DeviceValueStorage()
        cls.constants = NetworkElementConstants
        cls.device_collection = DeviceCollectionManager()

        cls.device_collection.add_device(cls.netelem1, NetworkElement(cls.constants.OS_EOS,
                                                                      cls.constants.PLATFORM_EOS_BASE,
                                                                      cls.constants.UNIT_BASE,
                                                                      cls.constants.VERSION_BASE))
        cls.device_collection.add_device(cls.netelem2, NetworkElement(cls.constants.OS_EOS,
                                                                      cls.constants.PLATFORM_EOS_BASE,
                                                                      cls.constants.UNIT_BASE,
                                                                      cls.constants.VERSION_BASE))

    # Test Case 1
    def test_add_return(self):
        self.storage.add_value(self.netelem1, "test_value_A", self.value_a)
        value = self.storage.get_value(self.netelem1, "test_value_A")
        self.assertEqual(self.value_a, value,
                         "Test Case 1 Failed: " + str(self.value_a) + " does NOT equal " + str(value) + "!")

    # Test Case 2
    def test_add_update_return(self):
        self.storage.add_value(self.netelem1, "test_value_A", self.value_a)
        self.storage.update_value(self.netelem1, "test_value_A", self.value_b)
        value = self.storage.get_value(self.netelem1, "test_value_A")
        self.assertEqual(self.value_b, value,
                         "Test Case 2 Failed: " + str(self.value_b) + " does NOT equal " + str(value) + "!")

    # Test Case 3
    def test_add_update_b_return(self):
        self.storage.add_value(self.netelem1, "test_value_A", self.value_a)
        self.storage.update_value(self.netelem1, "test_value_B", self.value_b)
        value1 = self.storage.get_value(self.netelem1, "test_value_A")
        value2 = self.storage.get_value(self.netelem1, "test_value_B")
        self.assertEqual(self.value_a, value1,
                         "Test Case 3a Failed: " + str(self.value_a) + " does NOT equal " + str(value1) + "!")
        self.assertEqual(self.value_b, value2,
                         "Test Case 3b Failed: " + str(self.value_b) + " does NOT equal " + str(value2) + "!")

    # Test Case 4
    def test_update_return(self):
        self.storage.update_value(self.netelem1, "test_value_A", self.value_a)
        value = self.storage.get_value(self.netelem1, "test_value_A")
        self.assertEqual(self.value_a, value,
                         "Test Case 4 Failed: " + str(self.value_a) + " does NOT equal " + str(value) + "!")

    # Test Case 5
    def test_add_two_devices_return(self):
        self.storage.add_value(self.netelem1, "test_value_A", self.value_a)
        self.storage.add_value(self.netelem2, "test_value_A", self.value_b)
        value1 = self.storage.get_value(self.netelem1, "test_value_A")
        value2 = self.storage.get_value(self.netelem2, "test_value_A")
        self.assertEqual(self.value_a, value1,
                         "Test Case 5a Failed: " + str(self.value_a) + " does NOT equal " + str(value1) + "!")
        self.assertEqual(self.value_b, value2,
                         "Test Case 5b Failed: " + str(self.value_b) + " does NOT equal " + str(value2) + "!")

    # Test Case 6
    def test_add_update_different_return(self):
        self.storage.add_value(self.netelem1, "test_value_A", self.value_a)
        self.storage.update_value(self.netelem2, "test_value_A", self.value_b)
        value1 = self.storage.get_value(self.netelem1, "test_value_A")
        value2 = self.storage.get_value(self.netelem2, "test_value_A")
        self.assertEqual(self.value_a, value1,
                         "Test Case 6a Failed: " + str(self.value_a) + " does NOT equal " + str(value1) + "!")
        self.assertEqual(self.value_b, value2,
                         "Test Case 6b Failed: " + str(self.value_b) + " does NOT equal " + str(value2) + "!")

    # Test Case 7
    def test_update_two_devices_return(self):
        self.storage.update_value(self.netelem1, "test_value_A", self.value_a)
        self.storage.update_value(self.netelem2, "test_value_A", self.value_b)
        value1 = self.storage.get_value(self.netelem1, "test_value_A")
        value2 = self.storage.get_value(self.netelem2, "test_value_A")
        self.assertEqual(self.value_a, value1,
                         "Test Case 7a Failed: " + str(self.value_a) + " does NOT equal " + str(value1) + "!")
        self.assertEqual(self.value_b, value2,
                         "Test Case 7b Failed: " + str(self.value_b) + " does NOT equal " + str(value2) + "!")

    # Test Case 8
    def test_add_update_another_return(self):
        self.storage.add_value(self.netelem1, "test_value_A", self.value_a)
        self.storage.update_value(self.netelem1, "test_value_B", self.value_b)
        value1 = self.storage.get_value(self.netelem1, "test_value_A")
        value2 = self.storage.get_value(self.netelem1, "test_value_B")
        self.assertEqual(self.value_a, value1,
                         "Test Case 8a Failed: " + str(self.value_a) + " does NOT equal " + str(value1) + "!")
        self.assertEqual(self.value_b, value2,
                         "Test Case 8b Failed: " + str(self.value_b) + " does NOT equal " + str(value2) + "!")

    # Test Case 9
    def test_add_update_twice_return(self):
        self.storage.add_value(self.netelem1, "test_value_A", self.value_a)
        self.storage.update_value(self.netelem1, "test_value_A", self.value_b)
        self.storage.update_value(self.netelem1, "test_value_A", self.value_c)
        value = self.storage.get_value(self.netelem1, "test_value_A")
        self.assertEqual(self.value_c, value,
                         "Test Case 9 Failed: " + str(self.value_c) + " does NOT equal " + str(value) + "!")


if __name__ == '__main__':
    RobotUnitTest.main()
