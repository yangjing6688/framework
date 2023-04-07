from extauto.common.Utils import Utils
from robot.libraries.BuiltIn import BuiltIn
from ExtremeAutomation.Utilities.deprecated import deprecated

list_failed_test = []


class TestFlow:
    def __init__(self):
        self.utils = Utils()
        self.robot_built_in = BuiltIn()

    def search_failed_test_case_dependency(self, prev_test_status, list_failed_test, prev_testname,  *search_test_dependency):
        """
        - It takes list of dependent tests and previous test execution status as arguments.
        - If test fails, failed_list gets appended with test case name.
        - Keyword Usage:
         - ``Search Failed Test Case Dependency      ${test_status}    ${failed_list}   ${prev_testname}   ${tests} ``
        :param search_test_dependency: list of dependent test cases that current test depends upon
        :param prev_test_status: previous test case execution status
        :param list_failed_test: list of failed tests
        :param prev_testname: previous test case name
        :return: list of failed test cases
        """
        if prev_test_status == 'FAIL':
            list_failed_test.append(prev_testname)
            self.utils.print_info("List of failed tests:", str(list_failed_test))
        for test in search_test_dependency:
            matching = [test_fail for test_fail in list_failed_test if test in test_fail]
            if len(matching) > 0:
                self.utils.print_info("Skip this test because of these previous tests failed:", str(list_failed_test))
                self.utils.print_info("List of failed test cases:", str(list_failed_test))
        return list_failed_test

    @deprecated('Please use the \'depends_on\' keyword from DependencyLibrary. This method will be removed after 6/1/2023')
    def depends_on(self, *search_test_dependency):
        """
        - Current test execution depends on status of test[s] passed as arguments.
        - If test case in the list fails, the current test case will be skipped else continues.
        - Keyword Usage Example:
         - ``Depends On     test1       test2``
        :param search_test_dependency: list of test cases that current test depends upon
        :return: list of failed test cases
        """
        global list_failed_test
        prev_test_status = BuiltIn().get_variable_value('${PREV_TEST_STATUS}')
        prev_test_name = BuiltIn().get_variable_value('${PREV_TEST_NAME}')

        if prev_test_status == 'FAIL':
            list_failed_test.append(prev_test_name)
            self.utils.print_info("Adding this case to list of failed tests")

        for test in search_test_dependency:
            matching = [test_fail for test_fail in list_failed_test if test in test_fail]
            if len(matching) > 0:
                self.utils.print_info("Depending Test Case Failed. Skipping This Test Case")
                self.utils.print_info("List of Failed Test Cases:", str(list_failed_test))
                self.robot_built_in.skip('Skipping TEST CASE...')
        return list_failed_test

    def Run_Again_If_Keyword_Fails(self, cmd, *pars):
        """
        - Executes the failed command n times.
        - Keyword Usage:
         - ``Run Again If Keyword Fails     ${CMD}       ${PARAMETERS}``
        :param cmd: Command to be executed
        :param pars: Parameters to be passed for command
        :return: Command execution status
        """
        global NTimes
        status = False
        for i in range(0, NTimes):
            status = BuiltIn().run_keyword_and_return_status(cmd, *pars)
            if status == True:
                return 1
        if status != True:
            BuiltIn().fail()




