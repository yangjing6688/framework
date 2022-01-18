#!/usr/bin/env bash

TEST_DIR="$(pwd)/ExtremeAutomation/Unittests"
REPORT_DIR="${TEST_DIR}/RobotTests/jenkins_reports"

# Clean Robot Report Dir
python3 ${TEST_DIR}/Utilities/UnitTestReportCleanUp.py ${REPORT_DIR} 0

# Device Value Storage Robot Unit Tests
pybot -L trace -T -d ${REPORT_DIR} ${TEST_DIR}/RobotTests/UtilTests/ValueStorageTests.robot
