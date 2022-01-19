from extauto.common.Utils import Utils
from robot.libraries.BuiltIn import BuiltIn

list_failed_test = []

class TestFlow:
    def __init__(self):
        self.utils = Utils()
        self.robot_built_in = BuiltIn()

    def search_failed_test_case_dependency(self, prev_test_status, list_failed_test, prev_testname,  *search_test_dependency):
        if prev_test_status == 'FAIL':
            list_failed_test.append(prev_testname)
            self.utils.print_info("List of failed tests:", str(list_failed_test))
        for test in search_test_dependency:
            matching = [test_fail for test_fail in list_failed_test if test in test_fail]
            if len(matching) > 0:
                self.utils.print_info("Skip this test because of these previous tests failed:", str(list_failed_test))
                self.utils.print_info("List of failed test cases:", str(list_failed_test))
        return  list_failed_test

    def depends_on(self, *search_test_dependency):
        global list_failed_test
        prev_test_status = BuiltIn().get_variable_value('${PREV_TEST_STATUS}')
        prev_test_name = BuiltIn().get_variable_value('${PREV_TEST_NAME}')

        if prev_test_status == 'FAIL':
            list_failed_test.append(prev_test_name)
            self.utils.print_info("Adding this case to list of failed tests")

        for test in search_test_dependency:
            matching = [test_fail for test_fail in list_failed_test if test in test_fail]
            if len(matching) > 0:
                self.utils.print_info("Depending test case failed. Skipping this test case")
                self.utils.print_info("List of failed test cases:", str(list_failed_test))
                self.robot_built_in.fail('Aborting TEST CASE...')
        return list_failed_test


    def Run_Again_If_Keyword_Fails(self, cmd, *pars):
        global NTimes
        status = False
        for i in range(0, NTimes):
            status = BuiltIn().run_keyword_and_return_status(cmd, *pars)
            if status == True:
                return 1
        if status != True:
            BuiltIn().fail()




