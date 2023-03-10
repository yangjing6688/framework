*** Settings ***
Documentation     TUT.py needs to be copied over to the following locations:
...                 /automation/tests/extreme_automation_tests/Tests/Pytest
...                 and
...                 /automation/tests/extreme_automation_tests/Tests/

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
${TUT_OUTPUT_SUBDIR_WARNING}        level_info
${TUT_OUTPUT_SUBDIR_ERROR}          level_info

${TUT_CASE_PYTHON_BUILTIN}          test_python_builtin_import

*** Test Cases ***
Run with config and check console and file at info level
    ${logging_level}                Set Variable    INFO
    ${output_dir}                   Set Variable    ${TUT_OUTPUT_DIR_WITH_CONFIG}/${TUT_OUTPUT_SUBDIR_INFO}
    ${output_file}                  Set Variable    ${output_dir}/report.html

    ${expected_stdout_line_count}   Set Variable    ${51}
    ${expected_stderr_line_count}   Set Variable    ${0}

    ${expected_info_start_code}         Set Variable    35
    ${expected_warning_start_code}      Set Variable    33
    ${expected_error_start_code}        Set Variable    31
    ${expected_reset_code}              Set Variable    39

    File Should Exist   ${TUT_WITH_PYTHON_CONFIG}

    Create Directory    ${output_dir}
    ${result} =     Run Process     pytest   --log-level   ${logging_level}     -k      not ${TUT_CASE_PYTHON_BUILTIN}   ${TUT_WITH_PYTHON_CONFIG}   cwd=${output_dir}

    @{stdout_lines} =   Split String     ${result.stdout}   \n
    @{stderr_lines} =   Split String     ${result.stderr}   \n

    Log List    ${stdout_lines}
    Log List    ${stderr_lines}

    ${stdout_line_count} =  Get Line Count  ${result.stdout}
    Should Be Equal         ${expected_stdout_line_count}   ${stdout_line_count}

    ${stderr_line_count} =  Get Line Count  ${result.stderr}
    Should Be Equal         ${expected_stderr_line_count}   ${stderr_line_count}

    ${info_line} =          Get From List   ${stdout_lines}     36
    ${warning_line} =       Get From List   ${stdout_lines}     41
    ${error_line} =         Get From List   ${stdout_lines}     46

#   Assert stdout lines

    ${level_name} =         Set Variable    info
    ${code_line_number} =   Set Variable    206
    ${regex} =              Set Variable    \\\x1b\\[${expected_info_start_code}m\\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${level_name.upper()}] \\[Utils] \\[print_${level_name}:${code_line_number}] \\[onboarding] message_print_${level_name}\\\x1b\\[${expected_reset_code}m
    Should Match Regexp     ${info_line}    ${regex}

    ${level_name} =         Set Variable    warning
    ${code_line_number} =   Set Variable    188
    ${regex} =              Set Variable    \\\x1b\\[${expected_warning_start_code}m\\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${level_name.upper()}] \\[Utils] \\[print_${level_name}:${code_line_number}] \\[onboarding] message_print_${level_name}\\\x1b\\[${expected_reset_code}m
    Should Match Regexp     ${warning_line}    ${regex}

    ${level_name} =         Set Variable    error
    ${code_line_number} =   Set Variable    170
    ${regex} =              Set Variable    \\\x1b\\[${expected_error_start_code}m\\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${level_name.upper()}] \\[Utils] \\[print_${level_name}:${code_line_number}] \\[onboarding] message_print_${level_name}\\\x1b\\[${expected_reset_code}m
    Should Match Regexp     ${error_line}    ${regex}

#   Assert log file lines

    ${log_file}             Get File            ${output_file}
    @{log_file_lines}=      Split to lines      ${log_file}

    ${info_line} =          Get From List   ${log_file_lines}     1573
    ${warning_line} =       Get From List   ${log_file_lines}     1585
    ${error_line} =         Get From List   ${log_file_lines}     1597

    ${level_name} =         Set Variable    info
    ${code_line_number} =   Set Variable    206
    ${regex} =              Set Variable    <span class="ansi${expected_info_start_code}">\\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${level_name.upper()}] \\[Utils] \\[print_${level_name}:${code_line_number}] \\[onboarding] message_print_${level_name}</span>
    Should Match Regexp     ${info_line}    ${regex}

    ${level_name} =         Set Variable    warning
    ${code_line_number} =   Set Variable    188
    ${regex} =              Set Variable    <span class="ansi${expected_warning_start_code}">\\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${level_name.upper()}] \\[Utils] \\[print_${level_name}:${code_line_number}] \\[onboarding] message_print_${level_name}</span>
    Should Match Regexp     ${warning_line}    ${regex}

    ${level_name} =         Set Variable    error
    ${code_line_number} =   Set Variable    170
    ${regex} =              Set Variable    <span class="ansi${expected_error_start_code}">\\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${level_name.upper()}] \\[Utils] \\[print_${level_name}:${code_line_number}] \\[onboarding] message_print_${level_name}</span>
    Should Match Regexp     ${error_line}    ${regex}
