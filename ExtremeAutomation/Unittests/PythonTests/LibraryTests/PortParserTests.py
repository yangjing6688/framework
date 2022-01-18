from ExtremeAutomation.Unittests.Utilities.RobotUnitTest import RobotUnitTest
from ExtremeAutomation.Library.ParsingHelper.InspectionToolkit import InspectionToolkit


class InspectionToolkitUnitTests(RobotUnitTest):
    def test_collapse_port_list_eos(self):
        it = self.__get_toolkit(self.constants.OS_EOS.lower())

        test_port_lists = {"a": "ge.1.1;ge.1.2;ge.1.3;ge.1.4-10",
                           "b": "ge.1.1-48;ge.2.2,3,4,5-48",
                           "c": "ge.1.1-2,5"}

        portparser_obj = it.get_port_parser_obj(test_port_lists["a"])
        self.assertTrue(portparser_obj.collapse_port_list() == "ge.1.1-10")

        portparser_obj = it.get_port_parser_obj(test_port_lists["b"])
        self.assertTrue(portparser_obj.collapse_port_list() == "ge.1.1-48;ge.2.2-48")

        portparser_obj = it.get_port_parser_obj(test_port_lists["c"])
        self.assertTrue(portparser_obj.collapse_port_list() == "ge.1.1-2,5")

    def test_collapse_port_list_exos(self):
        it = self.__get_toolkit(self.constants.OS_EXOS.lower())

        test_port_lists = {"a": "1:1-5,1:6-10",
                           "b": "1:1-10,1:11,1:12,2:1,2:2",
                           "c": "1:1,2:1,1:2,2:2,1:3-10"}

        portparser_obj = it.get_port_parser_obj(test_port_lists["a"])
        self.assertTrue(portparser_obj.collapse_port_list() == "1:1-10")

        portparser_obj = it.get_port_parser_obj(test_port_lists["b"])
        self.assertTrue(portparser_obj.collapse_port_list() == "1:1-12,2:1-2")

        portparser_obj = it.get_port_parser_obj(test_port_lists["c"])
        self.assertTrue(portparser_obj.collapse_port_list() == "1:1-10,2:1-2")

    def test_collapse_port_list_voss(self):
        it = self.__get_toolkit(self.constants.OS_VOSS.lower())

        test_port_lists = {"a": "1/1-1/5,1/6-1/10",
                           "b": "1/1-1/10,1/11,1/12,2/1,2/2",
                           "c": "1/1,2/1,1/2,2/2,1/3-1/10"}

        portparser_obj = it.get_port_parser_obj(test_port_lists["a"])
        self.assertTrue(portparser_obj.collapse_port_list() == "1/1-1/10")

        portparser_obj = it.get_port_parser_obj(test_port_lists["b"])
        self.assertTrue(portparser_obj.collapse_port_list() == "1/1-1/12,2/1-2/2")

        portparser_obj = it.get_port_parser_obj(test_port_lists["c"])
        print(portparser_obj.collapse_port_list())
        self.assertTrue(portparser_obj.collapse_port_list() == "1/1-1/10,2/1-2/2")

    # +------------------+
    # | Helper Functions |
    # +------------------+
    def __get_toolkit(self, dev_os):
        self.create_dummy_devices()
        return InspectionToolkit(self.dummy_devices[dev_os])


if __name__ == '__main__':
    RobotUnitTest.main()
