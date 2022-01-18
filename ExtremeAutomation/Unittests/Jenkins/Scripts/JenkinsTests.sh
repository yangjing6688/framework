#!/usr/bin/env bash

TEST_DIR="$(pwd)/ExtremeAutomation/Unittests/Jenkins/Scripts"

# Execute Python Unit Tests
${TEST_DIR}/PythonTests.sh

# Execute Robot Unit Tests
${TEST_DIR}/RobotTests.sh
