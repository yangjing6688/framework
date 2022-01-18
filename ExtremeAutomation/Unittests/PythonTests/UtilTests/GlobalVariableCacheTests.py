from ExtremeAutomation.Unittests.Utilities.RobotUnitTest import RobotUnitTest
from ExtremeAutomation.Keywords.Utils.GlobalVariableCache import GlobalVariableCache
from ExtremeAutomation.Keywords.Utils.GlobalVariableCache import GlobalVariableCacheConstants


# Test Keywords
class GlobalVariableCacheUnitTests(RobotUnitTest):
    @classmethod
    def setUpClass(cls):
        cls.value_a = "600000"
        cls.value_b = "987654321"
        cls.value_c = "12345678987654321"
        cls.storage = GlobalVariableCache()

    # Test Case 1
    def test_check_trm_file_values(self):
        value = self.storage.get_global_value(GlobalVariableCacheConstants.DEBUG_VALUE_CLI_TIME_OUT, self.value_a)
        self.assertEqual(self.value_a, value,
                         "Test Case 1 Failed: " + str(self.value_a) + " does NOT equal " + str(value) + "!")

    # Test Case 2
    def test_update_trm_file_values(self):
        self.storage.update_global_value(GlobalVariableCacheConstants.DEBUG_VALUE_CLI_TIME_OUT, self.value_b)
        value = self.storage.get_global_value(GlobalVariableCacheConstants.DEBUG_VALUE_CLI_TIME_OUT)
        self.assertEqual(self.value_b, value,
                         "Test Case 2 Failed: " + str(self.value_a) + " does NOT equal " + str(value) + "!")

    # Test Case 3
    def test_add_return(self):
        self.storage.add_global_value("test_value_A", self.value_a)
        value = self.storage.get_global_value("test_value_A")
        self.assertEqual(self.value_a, value,
                         "Test Case 3 Failed: " + str(self.value_a) + " does NOT equal " + str(value) + "!")

    # Test Case 4
    def test_add_update_return(self):
        self.storage.add_global_value("test_value_A", self.value_a)
        self.storage.update_global_value("test_value_A", self.value_b)
        value = self.storage.get_global_value("test_value_A")
        self.assertEqual(self.value_b, value,
                         "Test Case 4 Failed: " + str(self.value_b) + " does NOT equal " + str(value) + "!")

    # Test Case 5
    def test_add_update_b_return(self):
        self.storage.add_global_value("test_value_A", self.value_a)
        self.storage.update_global_value("test_value_B", self.value_b)
        value1 = self.storage.get_global_value("test_value_A")
        value2 = self.storage.get_global_value("test_value_B")
        self.assertEqual(self.value_a, value1,
                         "Test Case 5a Failed: " + str(self.value_a) + " does NOT equal " + str(value1) + "!")
        self.assertEqual(self.value_b, value2,
                         "Test Case 5b Failed: " + str(self.value_b) + " does NOT equal " + str(value2) + "!")

    # Test Case 6
    def test_update_return(self):
        self.storage.update_global_value("test_value_A", self.value_a)
        value = self.storage.get_global_value("test_value_A")
        self.assertEqual(self.value_a, value,
                         "Test Case 6 Failed: " + str(self.value_a) + " does NOT equal " + str(value) + "!")

    # Test Case 7
    def test_add_update_another_return(self):
        self.storage.add_global_value("test_value_A", self.value_a)
        self.storage.update_global_value("test_value_B", self.value_b)
        value1 = self.storage.get_global_value("test_value_A")
        value2 = self.storage.get_global_value("test_value_B")
        self.assertEqual(self.value_a, value1,
                         "Test Case 7a Failed: " + str(self.value_a) + " does NOT equal " + str(value1) + "!")
        self.assertEqual(self.value_b, value2,
                         "Test Case 7b Failed: " + str(self.value_b) + " does NOT equal " + str(value2) + "!")

    # Test Case 8
    def test_add_update_twice_return(self):
        self.storage.add_global_value("test_value_A", self.value_a)
        self.storage.update_global_value("test_value_A", self.value_b)
        self.storage.update_global_value("test_value_A", self.value_c)
        value = self.storage.get_global_value("test_value_A")
        self.assertEqual(self.value_c, value,
                         "Test Case 8 Failed: " + str(self.value_c) + " does NOT equal " + str(value) + "!")


if __name__ == '__main__':
    RobotUnitTest.main()
