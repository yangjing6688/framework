import os
from ExtremeAutomation.Unittests.Utilities.RobotUnitTest import RobotUnitTest
from ExtremeAutomation.Unittests.Utilities.NetelemKeywordUnitTest import CliKeywordUnitTest


class CliKeywordUnitTests(RobotUnitTest):
    @staticmethod
    def debug_tests():
        main()


def main():
    """Unit Test main definition."""
    csv_path = os.path.join("ExtremeAutomation", "Apis", "NetworkElement", "ApiDefinition", "CommandApiDefinition")
    kw_path = os.path.join("ExtremeAutomation", "Keywords", "NetworkElementKeywords", "GeneratedKeywords")
    test_gen = CliKeywordUnitTest(csv_path, kw_path, "CLI")
    test_gen.generate_tests(CliKeywordUnitTests)
    RobotUnitTest.main()


if __name__ == '__main__':
    main()
