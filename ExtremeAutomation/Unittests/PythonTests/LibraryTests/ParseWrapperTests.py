from ExtremeAutomation.Unittests.Utilities.RobotUnitTest import RobotUnitTest
from ExtremeAutomation.Library.ParsingHelper.ParserWrapper import ParserWrapper


class ParseWrapperUnitTests(RobotUnitTest):
    def setUp(self):
        self.pw = ParserWrapper()

    def test_normalize_header(self):
        return_val = self.pw.normalize_header(self.get_test_output_2(), "-", 5)
        self.assertEqual(return_val, "\n".join(["Default         1    %%%%%% ANY    0 /0   VR-Default",
                                                "Doc             2    %%%%%% ANY    0 /0   VR-Default",
                                                "Sleepy          3    %%%%%% ANY    0 /0   VR-Default",
                                                "Dopey           4    %%%%%% ANY    0 /0   VR-Default",
                                                "Angry           5    %%%%%% ANY    0 /0   VR-Default",
                                                "Happy           6    %%%%%% ANY    0 /0   VR-Default",
                                                "Angry           7    %%%%%% ANY    0 /0   VR-Default",
                                                "Freaky          8    %%%%%% ANY    0 /0   VR-Default",
                                                "Creepy          9    %%%%%% ANY    0 /0   VR-Default"]))
        return_val = self.pw.normalize_header(self.get_test_output_1(), "-", 2, norm="$$$$$")
        self.assertEqual(return_val, "\n".join(["VLAN     : 666         Status     : Enabled",
                                                "FID      : 666         Name       : This is a test vlan",
                                                "VLAN Type: Permanent  Last Change: 2015-11-23 15:00:36",
                                                "Egress Ports:",
                                                "host.0.1;ge.1.48",
                                                "Forbidden Egress Ports:",
                                                "lag.0.1-62;tbp.0.1-62;ge.1.1-47;tg.1.1-4",
                                                "Untagged Ports:",
                                                "ge.1.48"]))
        return_val = self.pw.normalize_header(self.get_test_output_2(), "-", 5, norm="$$$$$")
        self.assertEqual(return_val, "\n".join(["Default         1    $$$$$ ANY    0 /0   VR-Default",
                                                "Doc             2    $$$$$ ANY    0 /0   VR-Default",
                                                "Sleepy          3    $$$$$ ANY    0 /0   VR-Default",
                                                "Dopey           4    $$$$$ ANY    0 /0   VR-Default",
                                                "Angry           5    $$$$$ ANY    0 /0   VR-Default",
                                                "Happy           6    $$$$$ ANY    0 /0   VR-Default",
                                                "Angry           7    $$$$$ ANY    0 /0   VR-Default",
                                                "Freaky          8    $$$$$ ANY    0 /0   VR-Default",
                                                "Creepy          9    $$$$$ ANY    0 /0   VR-Default"]))
        return_val = self.pw.normalize_header(self.get_test_output_1(), "-", 2)
        self.assertEqual(return_val, "\n".join(["VLAN     : 666         Status     : Enabled",
                                                "FID      : 666         Name       : This is a test vlan",
                                                "VLAN Type: Permanent  Last Change: 2015-11-23 15:00:36",
                                                "Egress Ports:",
                                                "host.0.1;ge.1.48",
                                                "Forbidden Egress Ports:",
                                                "lag.0.1-62;tbp.0.1-62;ge.1.1-47;tg.1.1-4",
                                                "Untagged Ports:",
                                                "ge.1.48"]))
        return_val = self.pw.normalize_header("---------- ---------- ---------- ----- ----- ----------", "-", 10)
        self.assertEqual(return_val, "%%%%%% %%%%%% %%%%%% ----- ----- %%%%%%")
        return_val = self.pw.normalize_header("---------- ---------- ---------- ----- ----- ----------", "-", 6)
        self.assertEqual(return_val, "%%%%%% %%%%%% %%%%%% ----- ----- %%%%%%")
        return_val = self.pw.normalize_header("---------- ---------- ---------- ----- ----- ----------", "-", 5)
        self.assertEqual(return_val, "%%%%%% %%%%%% %%%%%% %%%%%% %%%%%% %%%%%%")

    def test_get_value_by_index(self):
        return_val = self.pw.get_value_by_index(self.get_test_output_2(), 0)
        self.assertEqual(return_val, "Default")
        return_val = self.pw.get_value_by_index(self.get_test_output_2(), 7)
        self.assertEqual(return_val, "Doc")
        return_val = self.pw.get_value_by_index(self.get_test_output_2(), -1)
        self.assertEqual(return_val, self.constants.VALUE_NOT_PRESENT)
        return_val = self.pw.get_value_by_index(self.get_test_output_2(), 1000)
        self.assertEqual(return_val, self.constants.VALUE_NOT_PRESENT)

    def test_get_value_by_offset(self):
        return_val = self.pw.get_value_by_offset(self.get_test_output_2(), "Happy", 0)
        self.assertEqual(return_val, "Happy")
        return_val = self.pw.get_value_by_offset(self.get_test_output_2(), "Happy", 1)
        self.assertEqual(return_val, "6")
        return_val = self.pw.get_value_by_offset(self.get_test_output_2(), "Happy", 7)
        self.assertEqual(return_val, self.constants.VALUE_NOT_PRESENT)
        return_val = self.pw.get_value_by_offset(self.get_test_output_2(), "Happy", 10)
        self.assertEqual(return_val, self.constants.VALUE_NOT_PRESENT)

    def test_get_exact_value_by_offset(self):
        return_val = self.pw.get_exact_value_by_offset(self.get_test_output_2(), "Happy", 0)
        self.assertEqual(return_val, "Happy")
        return_val = self.pw.get_exact_value_by_offset(self.get_test_output_2(), "Happy ", 0)
        self.assertEqual(return_val, "Happy")
        return_val = self.pw.get_exact_value_by_offset(self.get_test_output_2(), "Happy", 1)
        self.assertEqual(return_val, "6")
        return_val = self.pw.get_exact_value_by_offset(self.get_test_output_2(), "Happy", 7)
        self.assertEqual(return_val, self.constants.VALUE_NOT_PRESENT)
        return_val = self.pw.get_exact_value_by_offset(self.get_test_output_2(), "Happy", 10)
        self.assertEqual(return_val, self.constants.VALUE_NOT_PRESENT)
        return_val = self.pw.get_exact_value_by_offset(self.get_test_output_2(), "Happ", 0)
        self.assertEqual(return_val, self.constants.VALUE_NOT_PRESENT)
        return_val = self.pw.get_exact_value_by_offset(self.get_test_output_2(), "Happ", 1)
        self.assertEqual(return_val, self.constants.VALUE_NOT_PRESENT)
        return_val = self.pw.get_exact_value_by_offset(self.get_test_output_2(), "Happ", 7)
        self.assertEqual(return_val, self.constants.VALUE_NOT_PRESENT)
        return_val = self.pw.get_exact_value_by_offset(self.get_test_output_2(), "Happ", 10)
        self.assertEqual(return_val, self.constants.VALUE_NOT_PRESENT)
        return_val = self.pw.get_exact_value_by_offset(self.get_test_output_2(), "appy", 0)
        self.assertEqual(return_val, self.constants.VALUE_NOT_PRESENT)
        return_val = self.pw.get_exact_value_by_offset(self.get_test_output_2(), "appy", 1)
        self.assertEqual(return_val, self.constants.VALUE_NOT_PRESENT)
        return_val = self.pw.get_exact_value_by_offset(self.get_test_output_2(), "appy", 10)
        self.assertEqual(return_val, self.constants.VALUE_NOT_PRESENT)
        return_val = self.pw.get_exact_value_by_offset(self.get_test_output_3(), "10.0.0.41", 0)
        self.assertEqual(return_val, "1")

    def test_get_value_by_offset_with_exclude(self):
        return_val = self.pw.get_value_by_offset_with_exclude(self.get_test_output_2(), "Happy", 0, "test")
        self.assertEqual(return_val, "Happy")
        return_val = self.pw.get_value_by_offset_with_exclude(self.get_test_output_2(), "Happy", 1, "test")
        self.assertEqual(return_val, "6")
        return_val = self.pw.get_value_by_offset_with_exclude(self.get_test_output_2(), "Happy", 7, "test")
        self.assertEqual(return_val, self.constants.VALUE_NOT_PRESENT)
        return_val = self.pw.get_value_by_offset_with_exclude(self.get_test_output_2(), "Happy", 10, "test")
        self.assertEqual(return_val, self.constants.VALUE_NOT_PRESENT)
        return_val = self.pw.get_value_by_offset_with_exclude(self.get_test_output_2(), "Happy", 0, "ANY")
        self.assertEqual(return_val, self.constants.VALUE_NOT_PRESENT)
        return_val = self.pw.get_value_by_offset_with_exclude(self.get_test_output_2(), "Happy", 1, "VR-Default")
        self.assertEqual(return_val, self.constants.VALUE_NOT_PRESENT)
        return_val = self.pw.get_value_by_offset_with_exclude(self.get_test_output_2(), "Happy", 7, "ANY")
        self.assertEqual(return_val, self.constants.VALUE_NOT_PRESENT)
        return_val = self.pw.get_value_by_offset_with_exclude(self.get_test_output_2(), "Happy", 10, "VR-Default")
        self.assertEqual(return_val, self.constants.VALUE_NOT_PRESENT)

    def test_get_value_range(self):
        return_val = self.pw.get_value_range(self.get_test_output_2(), "Default", "0")
        self.assertEqual(return_val, "1    ------------------------------------------------- ANY")
        return_val = self.pw.get_value_range(self.get_test_output_2(), "Freaky", "ANY")
        self.assertEqual(return_val, "8    -------------------------------------------------")
        return_val = self.pw.get_value_range(self.get_test_output_2(), "Default", "9")
        exp = \
            "1    ------------------------------------------------- ANY    0 /0   VR-Default\r\n" \
            "                Doc             2    ------------------------------------------------- ANY    0 /0   " \
            "VR-Default\r\n" \
            "                Sleepy          3    ------------------------------------------------- ANY    0 /0   " \
            "VR-Default\r\n" \
            "                Dopey           4    ------------------------------------------------- ANY    0 /0   " \
            "VR-Default\r\n" \
            "                Angry           5    ------------------------------------------------- ANY    0 /0   " \
            "VR-Default\r\n" \
            "                Happy           6    ------------------------------------------------- ANY    0 /0   " \
            "VR-Default\r\n" \
            "                Angry           7    ------------------------------------------------- ANY    0 /0   " \
            "VR-Default\r\n" \
            "                Freaky          8    ------------------------------------------------- ANY    0 /0   " \
            "VR-Default\r\n" \
            "                Creepy"
        self.assertEqual(return_val, exp)
        return_val = self.pw.get_value_range(self.get_test_output_2(), "NotPresent", "9")
        self.assertEqual(return_val, self.constants.VALUE_NOT_PRESENT)
        return_val = self.pw.get_value_range(self.get_test_output_2(), "Sleepy", "NotPresent")
        self.assertEqual(return_val, self.constants.VALUE_NOT_PRESENT)
        return_val = self.pw.get_value_range(self.get_test_output_2(), "NotPresent", "NotPresent")
        self.assertEqual(return_val, self.constants.VALUE_NOT_PRESENT)

    def test_get_value_from_string_to_eol(self):
        return_val = self.pw.get_value_from_string_to_eol(self.get_test_output_2(), "Sleepy")
        self.assertEqual(return_val, "3    ------------------------------------------------- ANY    0 /0   VR-Default")
        return_val = self.pw.get_value_from_string_to_eol(self.get_test_output_2(), "7")
        self.assertEqual(return_val, "------------------------------------------------- ANY    0 /0   VR-Default")
        return_val = self.pw.get_value_from_string_to_eol(self.get_test_output_2(), "VR-Default")
        self.assertEqual(return_val, "")
        return_val = self.pw.get_value_from_string_to_eol(self.get_test_output_2(), "NotPresent")
        self.assertEqual(return_val, self.constants.VALUE_NOT_PRESENT)

    def test_get_range_by_offset(self):
        return_val = self.pw.get_range_by_offset(self.get_test_output_2(), "Sleepy", 2, 5)
        self.assertEqual(return_val, ["------------------------------------------------- ANY    0 /0"])
        return_val = self.pw.get_range_by_offset(self.get_test_output_2(), "Sleepy", 0, 5)
        self.assertEqual(return_val, ["Sleepy          3    ------------------------------------------------- "
                                      "ANY    0 /0"])
        return_val = self.pw.get_range_by_offset(self.get_test_output_2(), "Sleepy", 0, 6)
        self.assertEqual(return_val, ["Sleepy          3    ------------------------------------------------- "
                                      "ANY    0 /0   VR-Default"])
        return_val = self.pw.get_range_by_offset(self.get_test_output_2(), "Sleepy", 0, -1)
        self.assertEqual(return_val, ["Sleepy          3    ------------------------------------------------- "
                                      "ANY    0 /0   VR-Default"])
        return_val = self.pw.get_range_by_offset(self.get_test_output_1(), "VLAN", 0, 3)
        self.assertEqual(return_val, ["VLAN     : 666         Status",
                                      "VLAN Type: Permanent  Last"])
        return_val = self.pw.get_range_by_offset(self.get_test_output_1(), "VLAN", 0, -1)
        self.assertEqual(return_val, ["VLAN     : 666         Status     : Enabled",
                                      "VLAN Type: Permanent  Last Change: 2015-11-23 15:00:36"])
        return_val = self.pw.get_range_by_offset(self.get_test_output_2(), "Sleepy", 0, 10)
        self.assertEqual(return_val, [self.constants.VALUE_NOT_PRESENT])
        return_val = self.pw.get_range_by_offset(self.get_test_output_2(), "Sleepy", -1, 6)
        self.assertEqual(return_val, [self.constants.VALUE_NOT_PRESENT])
        return_val = self.pw.get_range_by_offset(self.get_test_output_2(), "Sleepy", -1, -1)
        self.assertEqual(return_val, [self.constants.VALUE_NOT_PRESENT])
        return_val = self.pw.get_range_by_offset(self.get_test_output_2(), "NotPresent", 0, 5)
        self.assertEqual(return_val, [self.constants.VALUE_NOT_PRESENT])
        return_val = self.pw.get_range_by_offset(self.get_test_output_1(), "VLAN", -1, 3)
        self.assertEqual(return_val, [self.constants.VALUE_NOT_PRESENT,
                                      self.constants.VALUE_NOT_PRESENT])
        return_val = self.pw.get_range_by_offset(self.get_test_output_1(), "VLAN", -1, -1)
        self.assertEqual(return_val, [self.constants.VALUE_NOT_PRESENT,
                                      self.constants.VALUE_NOT_PRESENT])

    def test_get_eol_value(self):
        return_val = self.pw.get_eol_value(self.get_test_output_2(), "Sleepy")
        self.assertEqual(return_val, ["Sleepy          3    ------------------------------------------------- "
                                      "ANY    0 /0   VR-Default"])
        return_val = self.pw.get_eol_value(self.get_test_output_2(), "3")
        self.assertEqual(return_val, ["Sleepy          3    ------------------------------------------------- "
                                      "ANY    0 /0   VR-Default"])
        return_val = self.pw.get_eol_value(self.get_test_output_1(), "VLAN")
        self.assertEqual(return_val, ["VLAN     : 666         Status     : Enabled",
                                      "VLAN Type: Permanent  Last Change: 2015-11-23 15:00:36"])
        return_val = self.pw.get_eol_value(self.get_test_output_2(), "NotPresent")
        self.assertEqual(return_val, [self.constants.VALUE_NOT_PRESENT])

    def test_get_value_at_location(self):
        return_val = self.pw.get_value_at_location(self.get_test_output_2(), column=0, name="Sleepy")
        self.assertEqual(return_val, "Sleepy")
        return_val = self.pw.get_value_at_location(self.get_test_output_2(), column=1, name="Sleepy")
        self.assertEqual(return_val, "3")
        return_val = self.pw.get_value_at_location(self.get_test_output_2(), column=10, name="Sleepy")
        self.assertEqual(return_val, self.constants.VALUE_NOT_PRESENT)
        return_val = self.pw.get_value_at_location(self.get_test_output_2(), column=0, name="NotPresent")
        self.assertEqual(return_val, self.constants.VALUE_NOT_PRESENT)
        return_val = self.pw.get_value_at_location(self.get_test_output_2(), column=0, row=2)
        self.assertEqual(return_val, "Sleepy")
        return_val = self.pw.get_value_at_location(self.get_test_output_2(), column=10, row=2)
        self.assertEqual(return_val, self.constants.VALUE_NOT_PRESENT)
        return_val = self.pw.get_value_at_location(self.get_test_output_2(), column=0, row=10)
        self.assertEqual(return_val, self.constants.VALUE_NOT_PRESENT)
        return_val = self.pw.get_value_at_location(self.get_test_output_2(), column=0, row=2, name="Sleepy")
        self.assertEqual(return_val, "Sleepy")
        return_val = self.pw.get_value_at_location(self.get_test_output_2(), column=1, row=2, name="3")
        self.assertEqual(return_val, "3")
        return_val = self.pw.get_value_at_location(self.get_test_output_2(), column=0, row=2, name="NotPresent")
        self.assertEqual(return_val, self.constants.VALUE_NOT_PRESENT)
        return_val = self.pw.get_value_at_location(self.get_test_output_2(), column=0, row=10, name="Sleepy")
        self.assertEqual(return_val, self.constants.VALUE_NOT_PRESENT)
        return_val = self.pw.get_value_at_location(self.get_test_output_2(), column=10, row=0, name="Sleepy")
        self.assertEqual(return_val, self.constants.VALUE_NOT_PRESENT)
        return_val = self.pw.get_value_at_location(self.get_test_output_2(), column=10, row=10, name="NotPresent")
        self.assertEqual(return_val, self.constants.VALUE_NOT_PRESENT)

    def test_is_exact_string_present_in_output(self):
        self.assertTrue(self.pw.is_exact_string_present_in_output(self.get_test_output_2(), "Happy"))
        self.assertTrue(self.pw.is_exact_string_present_in_output(self.get_test_output_2(), "Happy "))
        self.assertTrue(self.pw.is_exact_string_present_in_output(self.get_test_output_2(), " Happy "))
        self.assertFalse(self.pw.is_exact_string_present_in_output(self.get_test_output_2(), " Happ"))
        self.assertFalse(self.pw.is_exact_string_present_in_output(self.get_test_output_2(), "Happ"))
        self.assertFalse(self.pw.is_exact_string_present_in_output(self.get_test_output_2(), "appy"))

    # +------------------+
    # | Helper Functions |
    # +------------------+
    @staticmethod
    def get_test_output_1():
        return "VLAN     : 666         Status     : Enabled\r\n\
                FID      : 666         Name       : This is a test vlan\r\n\
                VLAN Type: Permanent  Last Change: 2015-11-23 15:00:36\r\n\
                Egress Ports:\r\n\
                host.0.1;ge.1.48\r\n\
                Forbidden Egress Ports:\r\n\
                lag.0.1-62;tbp.0.1-62;ge.1.1-47;tg.1.1-4\r\n\
                Untagged Ports:\r\n\
                ge.1.48"

    @staticmethod
    def get_test_output_2():
        return "Default         1    ------------------------------------------------- ANY    0 /0   VR-Default\r\n\
                Doc             2    ------------------------------------------------- ANY    0 /0   VR-Default\r\n\
                Sleepy          3    ------------------------------------------------- ANY    0 /0   VR-Default\r\n\
                Dopey           4    ------------------------------------------------- ANY    0 /0   VR-Default\r\n\
                Angry           5    ------------------------------------------------- ANY    0 /0   VR-Default\r\n\
                Happy           6    ------------------------------------------------- ANY    0 /0   VR-Default\r\n\
                Angry           7    ------------------------------------------------- ANY    0 /0   VR-Default\r\n\
                Freaky          8    ------------------------------------------------- ANY    0 /0   VR-Default\r\n\
                Creepy          9    ------------------------------------------------- ANY    0 /0   VR-Default"

    @staticmethod
    def get_test_output_3():
        return "==============================================================================\r\n\
                1     10.0.0.41     255.255.255.255 disable disable 0.0.0.0\r\n\
                =============================================================================="


if __name__ == '__main__':
    RobotUnitTest.main()
