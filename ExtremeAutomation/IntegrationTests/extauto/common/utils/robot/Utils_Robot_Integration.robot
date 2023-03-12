*** Settings ***
Documentation       Test Utils integration with robot

Library    Process
Library    OperatingSystem
Library    String
Library    Collections

*** Variables ***
${TUT_PATH}                         /automation/framework/extreme_automation_framework/ExtremeAutomation/IntegrationTests/extauto/common/utils/robot/TUT.robot

${TUT_OUTPUT_DIR}                   ${EXECDIR}/tut_output

${TUT_CASE_ROBOT_BUILTIN}           Robot Builtin Import
${TUT_CASE_PRINT_ALL}               Print all levels

${trace_level_name}         trace
${debug_level_name}         debug
${info_level_name}          info
${warning_level_name}       warning
${error_level_name}         error

${debug_code_line_number}        206
${info_code_line_number}         190
${warning_code_line_number}      174
${error_code_line_number}        158

${expected_debug_start_code} =            32
${expected_info_start_code} =             35
${expected_reset_code} =                  39

${debug_regex}      \\\x1b\\[${expected_debug_start_code}m\\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${debug_level_name.upper()}] \\[Utils] \\[print_${debug_level_name}:${debug_code_line_number}] \\[Print all levels] message-level-${debug_level_name}\\\x1b\\[${expected_reset_code}m
${info_regex}       \\\x1b\\[${expected_info_start_code}m\\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${info_level_name.upper()}] \\[Utils] \\[print_${info_level_name}:${info_code_line_number}] \\[Print all levels] message-level-${info_level_name}\\\x1b\\[${expected_reset_code}m
${warning_regex}    \\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${warning_level_name.upper()}] \\[Utils] \\[print_${warning_level_name}:${warning_code_line_number}] \\[Print all levels] message-level-${warning_level_name}
${error_regex}      \\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${error_level_name.upper()}] \\[Utils] \\[print_${error_level_name}:${error_code_line_number}] \\[Print all levels] message-level-${error_level_name}

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

    ${expected_stdout_line_count}   Set Variable    ${13}
    ${expected_stderr_line_count}   Set Variable    ${2}

    Create Directory    ${output_dir}

    ${result} =     Run Process     robot   --loglevel  ${logging_level}    --test      ${TUT_CASE_PRINT_ALL}       ${TUT_PATH}     cwd=${output_dir}

    @{stdout_lines} =   Split String     ${result.stdout}   \n
    @{stderr_lines} =   Split String     ${result.stderr}   \n

    Log List    ${stdout_lines}
    Log List    ${stderr_lines}

    ${stdout_line_count} =  Get Line Count  ${result.stdout}
    Should Be Equal         ${expected_stdout_line_count}   ${stdout_line_count}

    ${stderr_line_count} =  Get Line Count  ${result.stderr}
    Should Be Equal         ${expected_stderr_line_count}   ${stderr_line_count}

    ${debug_line} =     Get From List   ${stdout_lines}     3
    ${info_line} =      Get From List   ${stdout_lines}     4

    ${warning_line} =       Get From List   ${stderr_lines}     0
    ${error_line} =         Get From List   ${stderr_lines}     1

    Should Match Regexp     ${debug_line}       ${debug_regex}
    Should Match Regexp     ${info_line}        ${info_regex}
    Should Match Regexp     ${warning_line}     ${warning_regex}
    Should Match Regexp     ${error_line}       ${error_regex}

