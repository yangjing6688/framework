from ExtremeAutomation.Unittests.Utilities.RobotUnitTest import RobotUnitTest
from ExtremeAutomation.Library.ParsingHelper.InspectionToolkit import InspectionToolkit


class InspectionToolkitUnitTests(RobotUnitTest):
    def test_compare_port_eos(self):
        it = self.__get_toolkit(self.constants.OS_EOS.lower())

        single_port = "ge.1.5"
        port_list = "ge.1.1;ge.1.2;ge.1.3;ge.1.4-10"

        self.assertTrue(it.compare_port_values(single_port, "ge.1.5", it.constants.EQUALTO))
        self.assertTrue(it.compare_port_values(single_port, "ge.1.6", it.constants.NOTEQUALTO))
        self.assertTrue(it.compare_port_values(port_list, "ge.1.5", it.constants.CONTAINS))
        self.assertTrue(it.compare_port_values(port_list, "ge.1.10", it.constants.CONTAINS))
        self.assertTrue(it.compare_port_values(port_list, "ge.1.1", it.constants.CONTAINS))
        self.assertTrue(it.compare_port_values(port_list, "ge.1.5", it.constants.FOUNDIN))
        self.assertTrue(it.compare_port_values(port_list, "ge.1.10", it.constants.FOUNDIN))
        self.assertTrue(it.compare_port_values(port_list, "ge.1.1", it.constants.FOUNDIN))
        self.assertTrue(it.compare_port_values(port_list, "ge.2.5", it.constants.NOTCONTAIN))
        self.assertTrue(it.compare_port_values(port_list, "ge.2.10", it.constants.NOTCONTAIN))
        self.assertTrue(it.compare_port_values(port_list, "ge.2.1", it.constants.NOTCONTAIN))
        self.assertTrue(it.compare_port_values(port_list, "ge.2.5", it.constants.NOTFOUNDIN))
        self.assertTrue(it.compare_port_values(port_list, "ge.2.10", it.constants.NOTFOUNDIN))
        self.assertTrue(it.compare_port_values(port_list, "ge.2.1", it.constants.NOTFOUNDIN))
        self.assertFalse(it.compare_port_values(single_port, "ge.1.6", it.constants.EQUALTO))
        self.assertFalse(it.compare_port_values(single_port, "ge.1.5", it.constants.NOTEQUALTO))
        self.assertFalse(it.compare_port_values(port_list, "ge.2.5", it.constants.CONTAINS))
        self.assertFalse(it.compare_port_values(port_list, "ge.2.10", it.constants.CONTAINS))
        self.assertFalse(it.compare_port_values(port_list, "ge.2.1", it.constants.CONTAINS))
        self.assertFalse(it.compare_port_values(port_list, "ge.2.5", it.constants.FOUNDIN))
        self.assertFalse(it.compare_port_values(port_list, "ge.2.10", it.constants.FOUNDIN))
        self.assertFalse(it.compare_port_values(port_list, "ge.2.1", it.constants.FOUNDIN))
        self.assertFalse(it.compare_port_values(port_list, "ge.1.5", it.constants.NOTCONTAIN))
        self.assertFalse(it.compare_port_values(port_list, "ge.1.10", it.constants.NOTCONTAIN))
        self.assertFalse(it.compare_port_values(port_list, "ge.1.1", it.constants.NOTCONTAIN))
        self.assertFalse(it.compare_port_values(port_list, "ge.1.5", it.constants.NOTFOUNDIN))
        self.assertFalse(it.compare_port_values(port_list, "ge.1.10", it.constants.NOTFOUNDIN))
        self.assertFalse(it.compare_port_values(port_list, "ge.1.1", it.constants.NOTFOUNDIN))

    def test_compare_port_exos(self):
        it = self.__get_toolkit(self.constants.OS_EXOS.lower())

        single_port = "1:1"
        port_list = "1:1,1:2,1:3,1:5-10"

        self.assertTrue(it.compare_port_values(single_port, "1:1", it.constants.EQUALTO))
        self.assertTrue(it.compare_port_values(single_port, "1:2", it.constants.NOTEQUALTO))
        self.assertTrue(it.compare_port_values(port_list, "1:6", it.constants.CONTAINS))
        self.assertTrue(it.compare_port_values(port_list, "1:10", it.constants.CONTAINS))
        self.assertTrue(it.compare_port_values(port_list, "1:1", it.constants.CONTAINS))
        self.assertTrue(it.compare_port_values(port_list, "1:6", it.constants.FOUNDIN))
        self.assertTrue(it.compare_port_values(port_list, "1:10", it.constants.FOUNDIN))
        self.assertTrue(it.compare_port_values(port_list, "1:1", it.constants.FOUNDIN))
        self.assertTrue(it.compare_port_values(port_list, "2:6", it.constants.NOTCONTAIN))
        self.assertTrue(it.compare_port_values(port_list, "2:10", it.constants.NOTCONTAIN))
        self.assertTrue(it.compare_port_values(port_list, "2:1", it.constants.NOTCONTAIN))
        self.assertTrue(it.compare_port_values(port_list, "2:6", it.constants.NOTFOUNDIN))
        self.assertTrue(it.compare_port_values(port_list, "2:10", it.constants.NOTFOUNDIN))
        self.assertTrue(it.compare_port_values(port_list, "2:1", it.constants.NOTFOUNDIN))
        self.assertFalse(it.compare_port_values(single_port, "1:2", it.constants.EQUALTO))
        self.assertFalse(it.compare_port_values(single_port, "1:1", it.constants.NOTEQUALTO))
        self.assertFalse(it.compare_port_values(port_list, "2:6", it.constants.CONTAINS))
        self.assertFalse(it.compare_port_values(port_list, "2:10", it.constants.CONTAINS))
        self.assertFalse(it.compare_port_values(port_list, "2:1", it.constants.CONTAINS))
        self.assertFalse(it.compare_port_values(port_list, "2:6", it.constants.FOUNDIN))
        self.assertFalse(it.compare_port_values(port_list, "2:10", it.constants.FOUNDIN))
        self.assertFalse(it.compare_port_values(port_list, "2:1", it.constants.FOUNDIN))
        self.assertFalse(it.compare_port_values(port_list, "1:6", it.constants.NOTCONTAIN))
        self.assertFalse(it.compare_port_values(port_list, "1:10", it.constants.NOTCONTAIN))
        self.assertFalse(it.compare_port_values(port_list, "1:1", it.constants.NOTCONTAIN))
        self.assertFalse(it.compare_port_values(port_list, "1:6", it.constants.NOTFOUNDIN))
        self.assertFalse(it.compare_port_values(port_list, "1:10", it.constants.NOTFOUNDIN))
        self.assertFalse(it.compare_port_values(port_list, "1:1", it.constants.NOTFOUNDIN))

    # +------------------+
    # | Helper Functions |
    # +------------------+
    def __get_toolkit(self, dev_os):
        self.create_dummy_devices()
        return InspectionToolkit(self.dummy_devices[dev_os])


if __name__ == '__main__':
    RobotUnitTest.main()
