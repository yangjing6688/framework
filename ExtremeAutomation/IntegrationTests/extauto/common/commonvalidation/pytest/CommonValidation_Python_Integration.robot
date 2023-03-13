*** Settings ***
Documentation       Test CommonValidation integration with pytest
...                 Requirements:
...                 TUT.py needs to be copied over to the following location:
...                 /automation/tests/extreme_automation_tests/Tests/Pytest
...                 and
...                 /automation/tests/extreme_automation_tests/Tests

Library    Process
Library    OperatingSystem
Library    String
Library    Collections

*** Variables ***
${TUT_WITH_PYTHON_CONFIG}            /automation/tests/extreme_automation_tests/Tests/Pytest/TUT.py
${TUT_WITH_NO_PYTHON_CONFIG}         /automation/tests/extreme_automation_tests/Tests/TUT.py

${TUT_OUTPUT_DIR}                   ${EXECDIR}/tut_output
${TUT_OUTPUT_DIR_WITH_CONFIG}       ${TUT_OUTPUT_DIR}/with_config
${TUT_OUTPUT_DIR_WITHOUT_CONFIG}    ${TUT_OUTPUT_DIR}/without_config

${TUT_OUTPUT_SUBDIR_INFO}           level_info

${TUT_CASE_PYTHON_BUILTIN}          test_python_builtin_import

${expected_info_start_code} =       35
${expected_error_start_code} =      31
${expected_reset_code} =            39

${expected_validate_line_call_1} =       41
${expected_validate_line_call_2} =       103
${expected_validate_line_call_3} =       104
${expected_validate_line_call_4} =       105

${expected_line_1_message} =    Internal Result Verification \\[IRV\\] is: Enabled
${expected_line_2_message} =    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
${expected_line_3_message} =    \\[IRV\\] IRV is configured to expect a failure and the keyword did not fail
${expected_line_4_message} =    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

${expected_info_level_name} =           info
${expected_error_level_name} =          error

*** Test Cases ***
Check correct BuiltIn imported
    File Should Exist   ${TUT_WITH_PYTHON_CONFIG}

    ${output_dir}       Set Variable    ${TUT_OUTPUT_DIR_WITH_CONFIG}
    Create Directory    ${output_dir}

    ${result} =     Run Process     pytest   -k      ${TUT_CASE_PYTHON_BUILTIN}   ${TUT_WITH_PYTHON_CONFIG}   cwd=${output_dir}

    @{stdout_lines} =   Split String     ${result.stdout}   \n
    @{stderr_lines} =   Split String     ${result.stderr}   \n

    Log List    ${stdout_lines}
    Log List    ${stderr_lines}

    ${success_line}   Get From List   ${stdout_lines}     12

    Should Contain      ${success_line}     PASSED

With config check console and file at info level
    ${logging_level}                Set Variable    INFO
    ${output_dir}                   Set Variable    ${TUT_OUTPUT_DIR_WITH_CONFIG}/${TUT_OUTPUT_SUBDIR_INFO}
    ${output_file}                  Set Variable    ${output_dir}/report.html

    ${expected_test_name} =     Set Variable    onboarding

    File Should Exist   ${TUT_WITH_PYTHON_CONFIG}

    Create Directory    ${output_dir}

    ${result} =     Run Process     pytest   --log-level   ${logging_level}     -k      not ${TUT_CASE_PYTHON_BUILTIN}   ${TUT_WITH_PYTHON_CONFIG}   cwd=${output_dir}

    #   Assert stdout lines

    ${expected_stdout_line_count}   Set Variable    ${148}
    ${expected_stderr_line_count}   Set Variable    ${0}

    @{stdout_lines} =   Split String     ${result.stdout}   \n
    @{stderr_lines} =   Split String     ${result.stderr}   \n

    Log List    ${stdout_lines}
    Log List    ${stderr_lines}

    ${stdout_line_count} =  Get Line Count  ${result.stdout}
    Should Be Equal         ${expected_stdout_line_count}   ${stdout_line_count}

    ${stderr_line_count} =  Get Line Count  ${result.stderr}
    Should Be Equal         ${expected_stderr_line_count}   ${stderr_line_count}

    ${regex_line_1} =       Set Variable    \\\x1b\\[${expected_info_start_code}m\\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${expected_info_level_name.upper()}] \\[CommonValidation] \\[validate:${expected_validate_line_call_1}] \\[${expected_test_name}] ${expected_line_1_message}\\\x1b\\[${expected_reset_code}m
    ${regex_line_2} =       Set Variable    \\\x1b\\[${expected_error_start_code}m\\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${expected_error_level_name.upper()}] \\[CommonValidation] \\[validate:${expected_validate_line_call_2}] \\[${expected_test_name}] ${expected_line_2_message}\\\x1b\\[${expected_reset_code}m
    ${regex_line_3} =       Set Variable    \\\x1b\\[${expected_error_start_code}m\\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${expected_error_level_name.upper()}] \\[CommonValidation] \\[validate:${expected_validate_line_call_3}] \\[${expected_test_name}] ${expected_line_3_message}\\\x1b\\[${expected_reset_code}m
    ${regex_line_4} =       Set Variable    \\\x1b\\[${expected_error_start_code}m\\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${expected_error_level_name.upper()}] \\[CommonValidation] \\[validate:${expected_validate_line_call_4}] \\[${expected_test_name}] ${expected_line_4_message}\\\x1b\\[${expected_reset_code}m

    ${line_1} =         Get From List   ${stdout_lines}     135
    ${line_2} =         Get From List   ${stdout_lines}     136
    ${line_3} =         Get From List   ${stdout_lines}     137
    ${line_4} =         Get From List   ${stdout_lines}     138

    Should Match Regexp     ${line_1}       ${regex_line_1}
    Should Match Regexp     ${line_2}       ${regex_line_2}
    Should Match Regexp     ${line_3}       ${regex_line_3}
    Should Match Regexp     ${line_4}       ${regex_line_4}

#   Assert log file lines

    ${log_file}             Get File            ${output_file}
    @{log_file_lines}=      Split to lines      ${log_file}

    Log List    ${log_file_lines}

    ${line_1} =       Get From List   ${log_file_lines}     1573
    ${line_2} =       Get From List   ${log_file_lines}     1574
    ${line_3} =       Get From List   ${log_file_lines}     1575
    ${line_4} =       Get From List   ${log_file_lines}     1576

    ${regex_line_1} =       Set Variable    <span class="ansi${expected_info_start_code}">\\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${expected_info_level_name.upper()}] \\[CommonValidation] \\[validate:${expected_validate_line_call_1}] \\[${expected_test_name}] ${expected_line_1_message}</span>
    ${regex_line_2} =       Set Variable    <span class="ansi${expected_error_start_code}">\\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${expected_error_level_name.upper()}] \\[CommonValidation] \\[validate:${expected_validate_line_call_2}] \\[${expected_test_name}] ${expected_line_2_message}</span>
    ${regex_line_3} =       Set Variable    <span class="ansi${expected_error_start_code}">\\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${expected_error_level_name.upper()}] \\[CommonValidation] \\[validate:${expected_validate_line_call_3}] \\[${expected_test_name}] ${expected_line_3_message}</span>
    ${regex_line_4} =       Set Variable    <span class="ansi${expected_error_start_code}">\\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${expected_error_level_name.upper()}] \\[CommonValidation] \\[validate:${expected_validate_line_call_4}] \\[${expected_test_name}] ${expected_line_4_message}</span>

    Should Match Regexp     ${line_1}       ${regex_line_1}
    Should Match Regexp     ${line_2}       ${regex_line_2}
    Should Match Regexp     ${line_3}       ${regex_line_3}
    Should Match Regexp     ${line_4}       ${regex_line_4}

Without config check console and file at info level
    ${logging_level}                Set Variable    INFO
    ${output_dir}                   Set Variable    ${TUT_OUTPUT_DIR_WITHOUT_CONFIG}/${TUT_OUTPUT_SUBDIR_INFO}
    ${output_file}                  Set Variable    ${output_dir}/report.html

    ${expected_test_name} =     Set Variable    SETUP

    File Should Exist   ${TUT_WITH_NO_PYTHON_CONFIG}

    Create Directory    ${output_dir}

    ${result} =     Run Process     pytest   --log-level   ${logging_level}     -k      not ${TUT_CASE_PYTHON_BUILTIN}   ${TUT_WITH_NO_PYTHON_CONFIG}   cwd=${output_dir}

    #   Assert stdout lines

    ${expected_stdout_line_count}   Set Variable    ${150}
    ${expected_stderr_line_count}   Set Variable    ${0}

    @{stdout_lines} =   Split String     ${result.stdout}   \n
    @{stderr_lines} =   Split String     ${result.stderr}   \n

    Log List    ${stdout_lines}
    Log List    ${stderr_lines}

    ${stdout_line_count} =  Get Line Count  ${result.stdout}
    Should Be Equal         ${expected_stdout_line_count}   ${stdout_line_count}

    ${stderr_line_count} =  Get Line Count  ${result.stderr}
    Should Be Equal         ${expected_stderr_line_count}   ${stderr_line_count}

    ${regex_line_1} =       Set Variable    \\\x1b\\[${expected_info_start_code}m\\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${expected_info_level_name.upper()}] \\[CommonValidation] \\[validate:${expected_validate_line_call_1}] \\[${expected_test_name}] ${expected_line_1_message}\\\x1b\\[${expected_reset_code}m
    ${regex_line_2} =       Set Variable    \\\x1b\\[${expected_error_start_code}m\\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${expected_error_level_name.upper()}] \\[CommonValidation] \\[validate:${expected_validate_line_call_2}] \\[${expected_test_name}] ${expected_line_2_message}\\\x1b\\[${expected_reset_code}m
    ${regex_line_3} =       Set Variable    \\\x1b\\[${expected_error_start_code}m\\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${expected_error_level_name.upper()}] \\[CommonValidation] \\[validate:${expected_validate_line_call_3}] \\[${expected_test_name}] ${expected_line_3_message}\\\x1b\\[${expected_reset_code}m
    ${regex_line_4} =       Set Variable    \\\x1b\\[${expected_error_start_code}m\\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${expected_error_level_name.upper()}] \\[CommonValidation] \\[validate:${expected_validate_line_call_4}] \\[${expected_test_name}] ${expected_line_4_message}\\\x1b\\[${expected_reset_code}m

    ${line_1} =         Get From List   ${stdout_lines}     136
    ${line_2} =         Get From List   ${stdout_lines}     137
    ${line_3} =         Get From List   ${stdout_lines}     138
    ${line_4} =         Get From List   ${stdout_lines}     139

    Should Match Regexp     ${line_1}       ${regex_line_1}
    Should Match Regexp     ${line_2}       ${regex_line_2}
    Should Match Regexp     ${line_3}       ${regex_line_3}
    Should Match Regexp     ${line_4}       ${regex_line_4}

#   Assert log file lines

    ${log_file}             Get File            ${output_file}
    @{log_file_lines}=      Split to lines      ${log_file}

    Log List    ${log_file_lines}

    ${line_1} =       Get From List   ${log_file_lines}     1573
    ${line_2} =       Get From List   ${log_file_lines}     1574
    ${line_3} =       Get From List   ${log_file_lines}     1575
    ${line_4} =       Get From List   ${log_file_lines}     1576

    ${regex_line_1} =       Set Variable    <span class="ansi${expected_info_start_code}">\\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${expected_info_level_name.upper()}] \\[CommonValidation] \\[validate:${expected_validate_line_call_1}] \\[${expected_test_name}] ${expected_line_1_message}</span>
    ${regex_line_2} =       Set Variable    <span class="ansi${expected_error_start_code}">\\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${expected_error_level_name.upper()}] \\[CommonValidation] \\[validate:${expected_validate_line_call_2}] \\[${expected_test_name}] ${expected_line_2_message}</span>
    ${regex_line_3} =       Set Variable    <span class="ansi${expected_error_start_code}">\\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${expected_error_level_name.upper()}] \\[CommonValidation] \\[validate:${expected_validate_line_call_3}] \\[${expected_test_name}] ${expected_line_3_message}</span>
    ${regex_line_4} =       Set Variable    <span class="ansi${expected_error_start_code}">\\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${expected_error_level_name.upper()}] \\[CommonValidation] \\[validate:${expected_validate_line_call_4}] \\[${expected_test_name}] ${expected_line_4_message}</span>

    Should Match Regexp     ${line_1}       ${regex_line_1}
    Should Match Regexp     ${line_2}       ${regex_line_2}
    Should Match Regexp     ${line_3}       ${regex_line_3}
    Should Match Regexp     ${line_4}       ${regex_line_4}
