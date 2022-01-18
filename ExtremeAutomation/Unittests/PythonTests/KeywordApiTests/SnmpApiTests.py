import os
from ExtremeAutomation.Unittests.Utilities.RobotUnitTest import RobotUnitTest
from ExtremeAutomation.Unittests.Utilities.NetelemApiUnitTest import SnmpApiUnitTest


class SnmpApiUnitTests(RobotUnitTest):
    @staticmethod
    def debug_tests():
        main()


def main():
    """Unit Test main definition."""
    csv_path = os.path.join("ExtremeAutomation", "Apis", "NetworkElement", "ApiDefinition", "CommandApiDefinition")
    test_gen = SnmpApiUnitTest(csv_path, "SNMP")
    test_gen.generate_tests(SnmpApiUnitTests)
    RobotUnitTest.main()


if __name__ == '__main__':
    main()
