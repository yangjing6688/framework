*** Settings ***
Documentation     Test RobotLogger
...
...               Limitations:
...               1. The framework lacks browser based testing for unittests, therefore HTML output
...               must be manually verified
...               2. Warning and error terminal colors are not present in output, therefore are not tested

Library    Process
Library    OperatingSystem
Library    String
Library    Collections

*** Variables ***
${TUT}                      ${CURDIR}/TUT.robot
${TUT_OUTPUT_DIR}           ${EXECDIR}/tut_output

${TUT_OUTPUT_LEVEL_TRACE_DIR}       ${TUT_OUTPUT_DIR}/level_trace
${TUT_OUTPUT_LEVEL_DEBUG_DIR}       ${TUT_OUTPUT_DIR}/level_debug
${TUT_OUTPUT_LEVEL_INFO_DIR}        ${TUT_OUTPUT_DIR}/level_info
${TUT_OUTPUT_LEVEL_WARNING_DIR}     ${TUT_OUTPUT_DIR}/level_warning
${TUT_OUTPUT_LEVEL_ERROR_DIR}       ${TUT_OUTPUT_DIR}/level_error
${TUT_OUTPUT_LEVEL_DEFAULT_DIR}     ${TUT_OUTPUT_DIR}/level_default

${trace_level_name}         trace
${debug_level_name}         debug
${info_level_name}          info
${warning_level_name}       warning
${error_level_name}         error

${trace_code_line_number}        9
${debug_code_line_number}        12
${info_code_line_number}         15
${warning_code_line_number}      18
${error_code_line_number}        21

${expected_trace_start_code} =            32
${expected_debug_start_code} =            32
${expected_info_start_code} =             35
#${expected_warning_start_code} =          33
#${expected_error_start_code} =            31
${expected_reset_code} =                  39

${trace_regex}      \\\x1b\\[${expected_trace_start_code}m\\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${trace_level_name.upper()}] \\[TUTLibrary] \\[print_${trace_level_name}:${trace_code_line_number}] \\[Print all levels] message-level-${trace_level_name}\\\x1b\\[${expected_reset_code}m
${debug_regex}      \\\x1b\\[${expected_debug_start_code}m\\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${debug_level_name.upper()}] \\[TUTLibrary] \\[print_${debug_level_name}:${debug_code_line_number}] \\[Print all levels] message-level-${debug_level_name}\\\x1b\\[${expected_reset_code}m
${info_regex}       \\\x1b\\[${expected_info_start_code}m\\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${info_level_name.upper()}] \\[TUTLibrary] \\[print_${info_level_name}:${info_code_line_number}] \\[Print all levels] message-level-${info_level_name}\\\x1b\\[${expected_reset_code}m
${warning_regex}    \\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${warning_level_name.upper()}] \\[TUTLibrary] \\[print_${warning_level_name}:${warning_code_line_number}] \\[Print all levels] message-level-${warning_level_name}
${error_regex}      \\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${error_level_name.upper()}] \\[TUTLibrary] \\[print_${error_level_name}:${error_code_line_number}] \\[Print all levels] message-level-${error_level_name}

*** Test Cases ***
Run and check console at trace level
    ${logging_level}                Set Variable    TRACE
    ${output_dir}                   Set Variable    ${TUT_OUTPUT_LEVEL_TRACE_DIR}
    ${expected_stdout_line_count}   Set Variable    ${14}
    ${expected_stderr_line_count}   Set Variable    ${2}

    Create Directory    ${output_dir}
    ${result} =     Run Process     robot   --loglevel  ${logging_level}   ${TUT}  cwd=${output_dir}

    @{stdout_lines} =   Split String     ${result.stdout}   \n
    @{stderr_lines} =   Split String     ${result.stderr}   \n

    Log List    ${stdout_lines}
    Log List    ${stderr_lines}

    ${stdout_line_count} =  Get Line Count  ${result.stdout}
    Should Be Equal         ${expected_stdout_line_count}   ${stdout_line_count}

    ${stderr_line_count} =  Get Line Count  ${result.stderr}
    Should Be Equal         ${expected_stderr_line_count}   ${stderr_line_count}

    ${trace_line} =     Get From List   ${stdout_lines}     3
    ${debug_line} =     Get From List   ${stdout_lines}     4
    ${info_line} =      Get From List   ${stdout_lines}     5

    ${warning_line} =       Get From List   ${stderr_lines}     0
    ${error_line} =         Get From List   ${stderr_lines}     1

    #   Assert stdout lines

    Should Match Regexp     ${trace_line}       ${trace_regex}
    Should Match Regexp     ${debug_line}       ${debug_regex}
    Should Match Regexp     ${info_line}        ${info_regex}
    Should Match Regexp     ${warning_line}     ${warning_regex}
    Should Match Regexp     ${error_line}       ${error_regex}


Run and check console at debug level
    ${logging_level}                Set Variable    DEBUG
    ${output_dir}                   Set Variable    ${TUT_OUTPUT_LEVEL_DEBUG_DIR}
    ${expected_stdout_line_count}   Set Variable    ${13}
    ${expected_stderr_line_count}   Set Variable    ${2}

    Create Directory    ${output_dir}
    ${result} =     Run Process     robot   --loglevel  ${logging_level}   ${TUT}  cwd=${output_dir}

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

    #   Assert stdout lines

    Should Match Regexp     ${debug_line}       ${debug_regex}
    Should Match Regexp     ${info_line}        ${info_regex}
    Should Match Regexp     ${warning_line}     ${warning_regex}
    Should Match Regexp     ${error_line}       ${error_regex}


Run and check console at info level
    ${logging_level}                Set Variable    INFO
    ${output_dir}                   Set Variable    ${TUT_OUTPUT_LEVEL_INFO_DIR}
    ${expected_stdout_line_count}   Set Variable    ${12}
    ${expected_stderr_line_count}   Set Variable    ${2}

    Create Directory    ${output_dir}
    ${result} =     Run Process     robot   --loglevel  ${logging_level}   ${TUT}  cwd=${output_dir}

    @{stdout_lines} =   Split String     ${result.stdout}   \n
    @{stderr_lines} =   Split String     ${result.stderr}   \n

    Log List    ${stdout_lines}
    Log List    ${stderr_lines}

    ${stdout_line_count} =  Get Line Count  ${result.stdout}
    Should Be Equal         ${expected_stdout_line_count}   ${stdout_line_count}

    ${stderr_line_count} =  Get Line Count  ${result.stderr}
    Should Be Equal         ${expected_stderr_line_count}   ${stderr_line_count}

    ${info_line} =      Get From List   ${stdout_lines}     3

    ${warning_line} =       Get From List   ${stderr_lines}     0
    ${error_line} =         Get From List   ${stderr_lines}     1

    #   Assert stdout lines

    Should Match Regexp     ${info_line}        ${info_regex}
    Should Match Regexp     ${warning_line}     ${warning_regex}
    Should Match Regexp     ${error_line}       ${error_regex}


Run and check console at warning level
    ${logging_level}                Set Variable    WARN
    ${output_dir}                   Set Variable    ${TUT_OUTPUT_LEVEL_WARNING_DIR}
    ${expected_stdout_line_count}   Set Variable    ${11}
    ${expected_stderr_line_count}   Set Variable    ${2}

    Create Directory    ${output_dir}
    ${result} =     Run Process     robot   --loglevel  ${logging_level}   ${TUT}  cwd=${output_dir}

    @{stdout_lines} =   Split String     ${result.stdout}   \n
    @{stderr_lines} =   Split String     ${result.stderr}   \n

    Log List    ${stdout_lines}
    Log List    ${stderr_lines}

    ${stdout_line_count} =  Get Line Count  ${result.stdout}
    Should Be Equal         ${expected_stdout_line_count}   ${stdout_line_count}

    ${stderr_line_count} =  Get Line Count  ${result.stderr}
    Should Be Equal         ${expected_stderr_line_count}   ${stderr_line_count}

    ${warning_line} =       Get From List   ${stderr_lines}     0
    ${error_line} =         Get From List   ${stderr_lines}     1

    #   Assert stdout lines

    Should Match Regexp     ${warning_line}     ${warning_regex}
    Should Match Regexp     ${error_line}       ${error_regex}


Run and check console at error level
    ${logging_level}                Set Variable    ERROR
    ${output_dir}                   Set Variable    ${TUT_OUTPUT_LEVEL_ERROR_DIR}
    ${expected_stdout_line_count}   Set Variable    ${11}
    ${expected_stderr_line_count}   Set Variable    ${1}

    Create Directory    ${output_dir}
    ${result} =     Run Process     robot   --loglevel  ${logging_level}   ${TUT}  cwd=${output_dir}

    @{stdout_lines} =   Split String     ${result.stdout}   \n
    @{stderr_lines} =   Split String     ${result.stderr}   \n

    Log List    ${stdout_lines}
    Log List    ${stderr_lines}

    ${stdout_line_count} =  Get Line Count  ${result.stdout}
    Should Be Equal         ${expected_stdout_line_count}   ${stdout_line_count}

    ${stderr_line_count} =  Get Line Count  ${result.stderr}
    Should Be Equal         ${expected_stderr_line_count}   ${stderr_line_count}

    ${error_line} =         Get From List   ${stderr_lines}     0

    #   Assert stdout lines

    Should Match Regexp     ${error_line}       ${error_regex}


Run and check console at default level
    ${output_dir}                   Set Variable    ${TUT_OUTPUT_LEVEL_DEFAULT_DIR}
    ${expected_stdout_line_count}   Set Variable    ${12}
    ${expected_stderr_line_count}   Set Variable    ${2}

    Create Directory    ${output_dir}
    ${result} =     Run Process     robot   ${TUT}  cwd=${output_dir}

    @{stdout_lines} =   Split String     ${result.stdout}   \n
    @{stderr_lines} =   Split String     ${result.stderr}   \n

    Log List    ${stdout_lines}
    Log List    ${stderr_lines}

    ${stdout_line_count} =  Get Line Count  ${result.stdout}
    Should Be Equal         ${expected_stdout_line_count}   ${stdout_line_count}

    ${stderr_line_count} =  Get Line Count  ${result.stderr}
    Should Be Equal         ${expected_stderr_line_count}   ${stderr_line_count}

    ${info_line} =      Get From List   ${stdout_lines}     3

    ${warning_line} =       Get From List   ${stderr_lines}     0
    ${error_line} =         Get From List   ${stderr_lines}     1

    #   Assert stdout lines

    Should Match Regexp     ${info_line}        ${info_regex}
    Should Match Regexp     ${warning_line}     ${warning_regex}
    Should Match Regexp     ${error_line}       ${error_regex}
