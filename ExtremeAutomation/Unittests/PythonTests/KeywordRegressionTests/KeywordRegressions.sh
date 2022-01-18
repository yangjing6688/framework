#!/usr/bin/env bash

TEST_DIR="$(pwd)/ExtremeAutomation/Unittests"
REPORT_DIR="${TEST_DIR}/PythonTests/jenkins_reports"

python3 ${TEST_DIR}/PythonTests/KeywordRegressionTests/ArpKeywordTests.py ${REPORT_DIR}
python3 ${TEST_DIR}/PythonTests/KeywordRegressionTests/FdbKeywordTests.py ${REPORT_DIR}
python3 ${TEST_DIR}/PythonTests/KeywordRegressionTests/GvrpKeywordTests.py ${REPORT_DIR}
python3 ${TEST_DIR}/PythonTests/KeywordRegressionTests/InterfaceKeywordTests.py ${REPORT_DIR}
python3 ${TEST_DIR}/PythonTests/KeywordRegressionTests/LldpKeywordTests.py ${REPORT_DIR}
python3 ${TEST_DIR}/PythonTests/KeywordRegressionTests/MirroringKeywordTests.py ${REPORT_DIR}
python3 ${TEST_DIR}/PythonTests/KeywordRegressionTests/PolicyKeywordTests.py ${REPORT_DIR}
python3 ${TEST_DIR}/PythonTests/KeywordRegressionTests/RadiusKeywordTests.py ${REPORT_DIR}
python3 ${TEST_DIR}/PythonTests/KeywordRegressionTests/SpanningTreeKeywordTests.py ${REPORT_DIR}
python3 ${TEST_DIR}/PythonTests/KeywordRegressionTests/VlanKeywordTests.py ${REPORT_DIR}

# Remove all reports more than 3 days old.
python3 ${TEST_DIR}/Utilities/UnitTestReportCleanUp.py ${REPORT_DIR} 3
