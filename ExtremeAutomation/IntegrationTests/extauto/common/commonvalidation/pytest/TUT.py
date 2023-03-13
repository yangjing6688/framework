from extauto.common.CommonValidation import CommonValidation
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


def test_validate_expect_to_fail_and_not_fail():
    validation = CommonValidation()
    validation.validate(1,1, expect_error="true")