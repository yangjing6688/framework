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
    parser.addoption(
        "--magic_key",
        action="store",
        default=[],
        help="The magic key for debugging",
    )

@fixture(scope='session', autouse=True)
def loadVarabiled(request):
    global config
    try:
        uuid = request.config.option.job_suite_uuid
        config['job_suite_uuid'] = uuid
    except:
        pass
    try:
        magic_key = request.config.option.magic_key
        config['MAGIC_KEY'] = magic_key
    except:
        pass