import os
from ExtremeAutomation.Unittests.Utilities.RobotUnitTest import RobotUnitTest
from ExtremeAutomation.Unittests.Utilities.NetelemApiUnitTest import RestApiUnitTest


class RestApiUnitTests(RobotUnitTest):
    @staticmethod
    def debug_tests():
        main()


def main():
    """Unit Test main definition."""
    csv_path = os.path.join("ExtremeAutomation", "Apis", "NetworkElement", "ApiDefinition", "CommandApiDefinition")
    test_gen = RestApiUnitTest(csv_path, "REST")
    test_gen.generate_tests(RestApiUnitTests)
    RobotUnitTest.main()


if __name__ == '__main__':
    main()
