*** Settings ***
Documentation       Test CommonValidation integration with robot
...                 Usage:
...                 --loglevel TRACE CommonValidation_Robot_Integration.robot

Library    Process
Library    OperatingSystem
Library    String
Library    Collections

*** Variables ***
${TUT_PATH}                         /automation/framework/extreme_automation_framework/ExtremeAutomation/IntegrationTests/extauto/common/commonvalidation/robot/TUT.robot

${TUT_OUTPUT_DIR}                   ${EXECDIR}/tut_output

${TUT_CASE_ROBOT_BUILTIN}               Robot Builtin Import
${TUT_CASE_TEST_VALIDATE_MESSAGES}      Test Validate Messages

${info_level_name}          info
${error_level_name}         error

${expected_validate_line_call_1} =       41
${expected_validate_line_call_2} =       103
${expected_validate_line_call_3} =       104
${expected_validate_line_call_4} =       105

${expected_line_1_message} =    Internal Result Verification \\[IRV\\] is: Enabled
${expected_line_2_message} =    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
${expected_line_3_message} =    \\[IRV\\] IRV is configured to expect a failure and the keyword did not fail
${expected_line_4_message} =    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

${expected_info_start_code} =             35
${expected_error_start_code} =            31
${expected_reset_code} =                  39

${regex_line_1}      \\\x1b\\[${expected_info_start_code}m\\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${info_level_name.upper()}] \\[CommonValidation] \\[validate:${expected_validate_line_call_1}] \\[Test Validate Messages] ${expected_line_1_message}\\\x1b\\[${expected_reset_code}m
${regex_line_2}      \\\x1b\\[${expected_error_start_code}m\\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${error_level_name.upper()}] \\[CommonValidation] \\[validate:${expected_validate_line_call_2}] \\[Test Validate Messages] ${expected_line_2_message}\\\x1b\\[${expected_reset_code}m
${regex_line_3}      \\\x1b\\[${expected_error_start_code}m\\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${error_level_name.upper()}] \\[CommonValidation] \\[validate:${expected_validate_line_call_3}] \\[Test Validate Messages] ${expected_line_3_message}\\\x1b\\[${expected_reset_code}m
${regex_line_4}      \\\x1b\\[${expected_error_start_code}m\\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${error_level_name.upper()}] \\[CommonValidation] \\[validate:${expected_validate_line_call_4}] \\[Test Validate Messages] ${expected_line_4_message}\\\x1b\\[${expected_reset_code}m

*** Test Cases ***
Check correct BuiltIn imported
    ${output_dir}       Set Variable    ${TUT_OUTPUT_DIR}
    Create Directory    ${output_dir}

    ${result} =     Run Process     robot   --test      ${TUT_CASE_ROBOT_BUILTIN}       ${TUT_PATH}     cwd=${output_dir}

    @{stdout_lines} =   Split String     ${result.stdout}   \n
    @{stderr_lines} =   Split String     ${result.stderr}   \n

    Log List    ${stdout_lines}
    Log List    ${stderr_lines}

    ${success_line}   Get From List   ${stdout_lines}     3

    Should Contain      ${success_line}     ${TUT_CASE_ROBOT_BUILTIN}
    Should Contain      ${success_line}     PASS


Check console at trace level
    ${logging_level}                Set Variable    TRACE
    ${output_dir}                   Set Variable    ${TUT_OUTPUT_DIR}

    ${expected_stdout_line_count}   Set Variable    ${14}
    ${expected_stderr_line_count}   Set Variable    ${3}

    Create Directory    ${output_dir}

    ${result} =     Run Process     robot   --loglevel  ${logging_level}    --test      ${TUT_CASE_TEST_VALIDATE_MESSAGES}       ${TUT_PATH}     cwd=${output_dir}

    @{stdout_lines} =   Split String     ${result.stdout}   \n
    @{stderr_lines} =   Split String     ${result.stderr}   \n

    Log List    ${stdout_lines}
    Log List    ${stderr_lines}

    ${stdout_line_count} =  Get Line Count  ${result.stdout}
    Should Be Equal         ${expected_stdout_line_count}   ${stdout_line_count}

    ${stderr_line_count} =  Get Line Count  ${result.stderr}
    Should Be Equal         ${expected_stderr_line_count}   ${stderr_line_count}

    ${line_1} =         Get From List   ${stdout_lines}     4

    ${line_2} =         Get From List   ${stderr_lines}     0
    ${line_3} =         Get From List   ${stderr_lines}     1
    ${line_4} =         Get From List   ${stderr_lines}     2

    Should Match Regexp     ${line_1}       ${regex_line_1}
    Should Match Regexp     ${line_2}       ${regex_line_2}
    Should Match Regexp     ${line_3}       ${regex_line_3}
    Should Match Regexp     ${line_4}       ${regex_line_4}

