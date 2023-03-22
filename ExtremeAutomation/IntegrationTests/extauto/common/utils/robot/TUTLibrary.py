"""
    This Robot test library is used by Utils_Robot_Integration.robot's TUT.robot
"""
from extauto.common.Utils import Utils
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

    def print_debug(self, message):
        Utils().print_debug(message)

    def print_info(self, message):
        Utils().print_info(message)

    def print_warning(self, message):
        Utils().print_warning(message)

    def print_error(self, message):
        Utils().print_error(message)
