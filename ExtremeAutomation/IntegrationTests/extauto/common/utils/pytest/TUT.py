"""
    This test module is used by Utils_Python_Integration.robot
"""
from extauto.common.Utils import Utils
import sys
import pytest

_path = '/automation/framework/extreme_automation_framework/ExtremeAutomation/IntegrationTests/extauto/common/utils/pytest/TUT.py'

@pytest.fixture(scope="module", autouse=True)
def my_fixture():
    if __file__ == _path:
        raise RuntimeError("File must be copied over")

def test_python_builtin_import():
    module = sys.modules.get("robot.libraries.BuiltIn")
    with pytest.raises(AttributeError):
        getattr(module.BuiltIn, "should_not_be_true")
    getattr(module.BuiltIn, "isRunningPytest")


def test_print_debug():
    utils = Utils()
    utils.print_debug("message_print_debug")


def test_print_info():
    utils = Utils()
    utils.print_info("message_print_info")


def test_print_warning():
    utils = Utils()
    utils.print_warning("message_print_warning")


def test_print_error():
    utils = Utils()
    utils.print_error("message_print_error")
