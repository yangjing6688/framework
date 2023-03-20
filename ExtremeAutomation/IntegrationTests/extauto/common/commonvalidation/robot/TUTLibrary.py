"""
    This Robot test library is used by CommonValidation_Robot_Integration.robot's TUT.robot
"""
from extauto.common.CommonValidation import CommonValidation
import sys

class TUTLibrary:

    def test_robot_builtin_import(self):
        module = sys.modules.get("robot.libraries.BuiltIn")
        try:
            getattr(module.BuiltIn, "isRunningPytest")
        except AttributeError:
            pass
        else:
            raise AssertionError()
        getattr(module.BuiltIn, "should_not_be_true")

    def test_validate_expect_to_fail_and_not_fail(self):
        validation = CommonValidation()
        validation.validate(1, 1, expect_error="true")
