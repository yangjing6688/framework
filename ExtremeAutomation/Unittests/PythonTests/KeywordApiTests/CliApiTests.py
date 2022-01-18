import os
from ExtremeAutomation.Unittests.Utilities.RobotUnitTest import RobotUnitTest
from ExtremeAutomation.Unittests.Utilities.NetelemApiUnitTest import CliApiUnitTest


class CliApiUnitTests(RobotUnitTest):
    @staticmethod
    def debug_tests():
        main()


def main():
    """Unit Test main definition."""
    csv_path = os.path.join("ExtremeAutomation", "Apis", "NetworkElement", "ApiDefinition", "CommandApiDefinition")
    test_gen = CliApiUnitTest(csv_path, "CLI")
    test_gen.generate_tests(CliApiUnitTests)
    RobotUnitTest.main()


if __name__ == '__main__':
    main()
