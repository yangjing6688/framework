*** Settings ***
Documentation     Example test cases using the keyword-driven testing approach.
...
...               All tests contain a workflow constructed from keywords in
...               ``CalculatorLibrary.py``. Creating new tests or editing
...               existing is easy even for people without programming skills.
...
...               The _keyword-driven_ appoach works well for normal test
...               automation, but the _gherkin_ style might be even better
...               if also business people need to understand tests. If the
...               same workflow needs to repeated multiple times, it is best
...               to use to the _data-driven_ approach.
Library    Process
Library    OperatingSystem

*** Variables ***
${TUT}                      ${CURDIR}/TUT.robot
${TUT_OUTPUT_DIR}           ${EXECDIR}/tut_output
${TUT_OUTPUT_LEVEL_TRACE_DIR}       ${TUT_OUTPUT_DIR}/level_trace
${TUT_OUTPUT_LEVEL_DEBUG_DIR}       ${TUT_OUTPUT_DIR}/level_debug
${TUT_OUTPUT_LEVEL_INFO_DIR}        ${TUT_OUTPUT_DIR}/level_info
${TUT_OUTPUT_LEVEL_DEFAULT_DIR}     ${TUT_OUTPUT_DIR}/level_default

*** Test Cases ***
Verify trace level
    Create Directory    ${TUT_OUTPUT_LEVEL_TRACE_DIR}
    ${result} =     Run Process     robot   --loglevel  TRACE   ${TUT}  cwd=${TUT_OUTPUT_LEVEL_TRACE_DIR}

Verify debug level
    Create Directory    ${TUT_OUTPUT_LEVEL_DEBUG_DIR}
    ${result} =     Run Process     robot   --loglevel  DEBUG   ${TUT}  cwd=${TUT_OUTPUT_LEVEL_DEBUG_DIR}

Verify info level
    Create Directory    ${TUT_OUTPUT_LEVEL_INFO_DIR}
    ${result} =     Run Process     robot   --loglevel  INFO   ${TUT}  cwd=${TUT_OUTPUT_LEVEL_INFO_DIR}

Verify default level
    Create Directory    ${TUT_OUTPUT_LEVEL_DEFAULT_DIR}
    ${result} =     Run Process     robot   ${TUT}  cwd=${TUT_OUTPUT_LEVEL_DEFAULT_DIR}
