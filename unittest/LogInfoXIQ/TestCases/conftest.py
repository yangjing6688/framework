import pytest
from pytest import fixture
from pytest_testconfig import config

def pytest_addoption(parser):
    parser.addoption(
        "--job_suite_uuid",
        action="store",
        default=[],
        help="The job Suite UUID",
    )

@fixture(scope='session', autouse=True)
def loadVarabiled(request):
    global config
    try:
        uuid = request.config.option.job_suite_uuid
        config['job_suite_uuid'] = uuid
    except:
        pass