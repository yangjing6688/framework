#!/usr/bin/env bash

TEST_DIR="$(pwd)/ExtremeAutomation/Unittests"
REPORT_DIR="${TEST_DIR}/PythonTests/jenkins_reports"

python3 ${TEST_DIR}/PythonTests/AgentTests/AgentTests.py ${REPORT_DIR}
python3 ${TEST_DIR}/PythonTests/AgentTests/RestTests.py ${REPORT_DIR}
python3 ${TEST_DIR}/PythonTests/AgentTests/SnmpTests.py ${REPORT_DIR}
python3 ${TEST_DIR}/PythonTests/AgentTests/SshTests.py ${REPORT_DIR}
python3 ${TEST_DIR}/PythonTests/AgentTests/TelnetTests.py ${REPORT_DIR}

python3 ${TEST_DIR}/PythonTests/ApiTests/ApiUnitTests.py ${REPORT_DIR}
python3 ${TEST_DIR}/PythonTests/ApiTests/ApiLoadTests.py ${REPORT_DIR}

python3 ${TEST_DIR}/PythonTests/KeywordApiTests/CliApiTests.py ${REPORT_DIR}
python3 ${TEST_DIR}/PythonTests/KeywordApiTests/RestApiTests.py ${REPORT_DIR}
python3 ${TEST_DIR}/PythonTests/KeywordApiTests/SnmpApiTests.py ${REPORT_DIR}

python3 ${TEST_DIR}/PythonTests/KeywordTests/CliKeywordTests.py ${REPORT_DIR}

python3 ${TEST_DIR}/PythonTests/LibraryTests/InspectionToolkitTests.py ${REPORT_DIR}
python3 ${TEST_DIR}/PythonTests/LibraryTests/LoggerTests.py ${REPORT_DIR}
python3 ${TEST_DIR}/PythonTests/LibraryTests/ParseWrapperTests.py ${REPORT_DIR}
python3 ${TEST_DIR}/PythonTests/LibraryTests/PortParserTests.py ${REPORT_DIR}
python3 ${TEST_DIR}/PythonTests/LibraryTests/PromptHandlerTests.py ${REPORT_DIR}

python3 ${TEST_DIR}/PythonTests/TrafficGenTests/ArpResolutionTests.py ${REPORT_DIR}
python3 ${TEST_DIR}/PythonTests/TrafficGenTests/TrafficGenerationTests.py ${REPORT_DIR}

python3 ${TEST_DIR}/PythonTests/UtilTests/GlobalVariableCacheTests.py ${REPORT_DIR}
python3 ${TEST_DIR}/PythonTests/UtilTests/MultiauthSessionTests.py ${REPORT_DIR}
python3 ${TEST_DIR}/PythonTests/UtilTests/PlatVarTests.py ${REPORT_DIR}
python3 ${TEST_DIR}/PythonTests/UtilTests/ValueStorageTests.py ${REPORT_DIR}
python3 ${TEST_DIR}/PythonTests/UtilTests/CloudConnectTests.py ${REPORT_DIR}

# Remove all reports more than 3 days old.
python3 ${TEST_DIR}/Utilities/UnitTestReportCleanUp.py ${REPORT_DIR} 3
