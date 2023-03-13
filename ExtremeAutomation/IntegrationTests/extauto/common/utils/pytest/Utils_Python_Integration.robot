*** Settings ***
Documentation       Test Utils integration with pytest
...                 Requirements:
...                 TUT.py needs to be copied over to the following location:
...                 /automation/tests/extreme_automation_tests/Tests/Pytest
...                 and
...                 /automation/tests/extreme_automation_tests/Tests
...                 Limitations:
...                 1. --log-level seems to not have any effect, hence:
...                 - print_debug is not tested

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

${TUT_OUTPUT_SUBDIR_DEBUG}          level_debug
${TUT_OUTPUT_SUBDIR_INFO}           level_info
${TUT_OUTPUT_SUBDIR_WARNING}        level_warning
${TUT_OUTPUT_SUBDIR_ERROR}          level_error

${TUT_CASE_PYTHON_BUILTIN}          test_python_builtin_import
${TUT_CASE_PRINT_DEBUG}             test_print_debug

${expected_info_start_code} =       35
${expected_warning_start_code} =    33
${expected_error_start_code} =      31
${expected_reset_code} =            39

${expected_info_level_name} =           info
${expected_warn_level_name} =           warning
${expected_error_level_name} =          error

${expected_info_code_line_number} =     190
${expected_warn_code_line_number} =     174
${expected_error_code_line_number} =    158

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

    ${result} =     Run Process     pytest   --log-level   ${logging_level}     -k      not ${TUT_CASE_PYTHON_BUILTIN} and not ${TUT_CASE_PRINT_DEBUG}   ${TUT_WITH_PYTHON_CONFIG}   cwd=${output_dir}

    #   Assert stdout lines

    ${expected_stdout_line_count}   Set Variable    ${39}
    ${expected_stderr_line_count}   Set Variable    ${0}

    @{stdout_lines} =   Split String     ${result.stdout}   \n
    @{stderr_lines} =   Split String     ${result.stderr}   \n

    Log List    ${stdout_lines}
    Log List    ${stderr_lines}

    ${stdout_line_count} =  Get Line Count  ${result.stdout}
    Should Be Equal         ${expected_stdout_line_count}   ${stdout_line_count}

    ${stderr_line_count} =  Get Line Count  ${result.stderr}
    Should Be Equal         ${expected_stderr_line_count}   ${stderr_line_count}

    ${regex_info_line} =        Set Variable    \\\x1b\\[${expected_info_start_code}m\\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${expected_info_level_name.upper()}] \\[Utils] \\[print_${expected_info_level_name}:${expected_info_code_line_number}] \\[${expected_test_name}] message_print_${expected_info_level_name}\\\x1b\\[${expected_reset_code}m
    ${regex_warning_line} =     Set Variable    \\\x1b\\[${expected_warning_start_code}m\\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${expected_warn_level_name.upper()}] \\[Utils] \\[print_${expected_warn_level_name}:${expected_warn_code_line_number}] \\[${expected_test_name}] message_print_${expected_warn_level_name}\\\x1b\\[${expected_reset_code}m
    ${regex_error_line} =       Set Variable    \\\x1b\\[${expected_error_start_code}m\\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${expected_error_level_name.upper()}] \\[Utils] \\[print_${expected_error_level_name}:${expected_error_code_line_number}] \\[${expected_test_name}] message_print_${expected_error_level_name}\\\x1b\\[${expected_reset_code}m

    ${info_line} =          Get From List   ${stdout_lines}     30
    ${warning_line} =       Get From List   ${stdout_lines}     33
    ${error_line} =         Get From List   ${stdout_lines}     36

    Should Match Regexp     ${info_line}        ${regex_info_line}
    Should Match Regexp     ${warning_line}     ${regex_warning_line}
    Should Match Regexp     ${error_line}       ${regex_error_line}

#   Assert log file lines

    ${log_file}             Get File            ${output_file}
    @{log_file_lines}=      Split to lines      ${log_file}

    Log List    ${log_file_lines}

    ${info_line} =          Get From List   ${log_file_lines}     1573
    ${warning_line} =       Get From List   ${log_file_lines}     1583
    ${error_line} =         Get From List   ${log_file_lines}     1593

    ${regex_info_line} =        Set Variable    <span class="ansi${expected_info_start_code}">\\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${expected_info_level_name.upper()}] \\[Utils] \\[print_${expected_info_level_name}:${expected_info_code_line_number}] \\[${expected_test_name}] message_print_${expected_info_level_name}</span>
    ${regex_warning_line} =     Set Variable    <span class="ansi${expected_warning_start_code}">\\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${expected_warn_level_name.upper()}] \\[Utils] \\[print_${expected_warn_level_name}:${expected_warn_code_line_number}] \\[${expected_test_name}] message_print_${expected_warn_level_name}</span>
    ${regex_error_line} =       Set Variable    <span class="ansi${expected_error_start_code}">\\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${expected_error_level_name.upper()}] \\[Utils] \\[print_${expected_error_level_name}:${expected_error_code_line_number}] \\[${expected_test_name}] message_print_${expected_error_level_name}</span>

    Should Match Regexp     ${info_line}        ${regex_info_line}
    Should Match Regexp     ${warning_line}     ${regex_warning_line}
    Should Match Regexp     ${error_line}       ${regex_error_line}

Without config check console and file at info level
    ${logging_level}                Set Variable    INFO
    ${output_dir}                   Set Variable    ${TUT_OUTPUT_DIR_WITHOUT_CONFIG}/${TUT_OUTPUT_SUBDIR_INFO}
    ${output_file}                  Set Variable    ${output_dir}/report.html

    ${expected_test_name} =     Set Variable    SETUP

    File Should Exist   ${TUT_WITH_NO_PYTHON_CONFIG}

    Create Directory    ${output_dir}

    ${result} =     Run Process     pytest   --log-level   ${logging_level}     -k      not ${TUT_CASE_PYTHON_BUILTIN} and not ${TUT_CASE_PRINT_DEBUG}   ${TUT_WITH_NO_PYTHON_CONFIG}   cwd=${output_dir}

    #   Assert stdout lines

    ${expected_stdout_line_count}   Set Variable    ${39}
    ${expected_stderr_line_count}   Set Variable    ${0}

    @{stdout_lines} =   Split String     ${result.stdout}   \n
    @{stderr_lines} =   Split String     ${result.stderr}   \n

    Log List    ${stdout_lines}
    Log List    ${stderr_lines}

    ${stdout_line_count} =  Get Line Count  ${result.stdout}
    Should Be Equal         ${expected_stdout_line_count}   ${stdout_line_count}

    ${stderr_line_count} =  Get Line Count  ${result.stderr}
    Should Be Equal         ${expected_stderr_line_count}   ${stderr_line_count}

    ${regex_info_line} =        Set Variable    \\\x1b\\[${expected_info_start_code}m\\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${expected_info_level_name.upper()}] \\[Utils] \\[print_${expected_info_level_name}:${expected_info_code_line_number}] \\[${expected_test_name}] message_print_${expected_info_level_name}\\\x1b\\[${expected_reset_code}m
    ${regex_warning_line} =     Set Variable    \\\x1b\\[${expected_warning_start_code}m\\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${expected_warn_level_name.upper()}] \\[Utils] \\[print_${expected_warn_level_name}:${expected_warn_code_line_number}] \\[${expected_test_name}] message_print_${expected_warn_level_name}\\\x1b\\[${expected_reset_code}m
    ${regex_error_line} =       Set Variable    \\\x1b\\[${expected_error_start_code}m\\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${expected_error_level_name.upper()}] \\[Utils] \\[print_${expected_error_level_name}:${expected_error_code_line_number}] \\[${expected_test_name}] message_print_${expected_error_level_name}\\\x1b\\[${expected_reset_code}m

    ${info_line} =          Get From List   ${stdout_lines}     30
    ${warning_line} =       Get From List   ${stdout_lines}     33
    ${error_line} =         Get From List   ${stdout_lines}     36

    Should Match Regexp     ${info_line}        ${regex_info_line}
    Should Match Regexp     ${warning_line}     ${regex_warning_line}
    Should Match Regexp     ${error_line}       ${regex_error_line}

#   Assert log file lines

    ${log_file}             Get File            ${output_file}
    @{log_file_lines}=      Split to lines      ${log_file}

    Log List    ${log_file_lines}

    ${info_line} =          Get From List   ${log_file_lines}     1573
    ${warning_line} =       Get From List   ${log_file_lines}     1583
    ${error_line} =         Get From List   ${log_file_lines}     1593

    ${regex_info_line} =        Set Variable    <span class="ansi${expected_info_start_code}">\\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${expected_info_level_name.upper()}] \\[Utils] \\[print_${expected_info_level_name}:${expected_info_code_line_number}] \\[${expected_test_name}] message_print_${expected_info_level_name}</span>
    ${regex_warning_line} =     Set Variable    <span class="ansi${expected_warning_start_code}">\\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${expected_warn_level_name.upper()}] \\[Utils] \\[print_${expected_warn_level_name}:${expected_warn_code_line_number}] \\[${expected_test_name}] message_print_${expected_warn_level_name}</span>
    ${regex_error_line} =       Set Variable    <span class="ansi${expected_error_start_code}">\\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${expected_error_level_name.upper()}] \\[Utils] \\[print_${expected_error_level_name}:${expected_error_code_line_number}] \\[${expected_test_name}] message_print_${expected_error_level_name}</span>

    Should Match Regexp     ${info_line}        ${regex_info_line}
    Should Match Regexp     ${warning_line}     ${regex_warning_line}
    Should Match Regexp     ${error_line}       ${regex_error_line}
