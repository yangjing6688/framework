*** Settings ***
Documentation     Test RobotLogger
...               1. For each of robot level TRACE, DEBUG, INFO, WARN, ERROR, DEFAULT:
...               - Verify console logging
...               - Verify output.xml logging
...               2. Verify console and output.xml logging for setup and teardown phases, at DEFAULT level
...
...               Limitations:
...               1. The framework lacks browser based testing for unittests, therefore HTML output
...               must be manually verified. Pro tem assert output.xml.
...               Usage:
...               --loglevel TRACE RobotLoggerTests.robot

Library    Process
Library    OperatingSystem
Library    String
Library    Collections

*** Variables ***
${TUT}                      ${CURDIR}/TUT.robot
${TUT_SETUP_TEARDOWN}       ${CURDIR}/TUTSetupTeardown.robot
${TUT_NEW_LINE}             ${CURDIR}/TUTNewLine.robot
${TUT_OUTPUT_DIR}           ${EXECDIR}/tut_output

${TUT_OUTPUT_LEVEL_TRACE_DIR}       ${TUT_OUTPUT_DIR}/level_trace
${TUT_OUTPUT_LEVEL_DEBUG_DIR}       ${TUT_OUTPUT_DIR}/level_debug
${TUT_OUTPUT_LEVEL_INFO_DIR}        ${TUT_OUTPUT_DIR}/level_info
${TUT_OUTPUT_LEVEL_WARNING_DIR}     ${TUT_OUTPUT_DIR}/level_warning
${TUT_OUTPUT_LEVEL_ERROR_DIR}       ${TUT_OUTPUT_DIR}/level_error
${TUT_OUTPUT_LEVEL_DEFAULT_DIR}     ${TUT_OUTPUT_DIR}/level_default
${TUT_OUTPUT_SETUP_TEARDOWN_DIR}    ${TUT_OUTPUT_DIR}/setup_teardown
${TUT_OUTPUT_NEW_LINE_DIR}          ${TUT_OUTPUT_DIR}/new_line

${src_module}           TUTLibrary
${src_test_name}        Print all levels
${setup_test_name}      SETUP
${teardown_test_name}   TEARDOWN

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

${setup_code_line_number}        24
${teardown_code_line_number}     27

${expected_trace_start_code}              32
${expected_debug_start_code}              32
${expected_info_start_code}               35
${expected_warning_start_code}            33
${expected_error_start_code}              31
${expected_reset_code}                    39

${expected_trace_color}              \#aa5500
${expected_debug_color}              \#00aa00
${expected_info_color}               \#E850A8
${expected_warning_color}            \#aa5500
${expected_error_color}              \#aa0000

${regex_body_trace}         message-level-${trace_level_name}
${regex_body_debug}         message-level-${debug_level_name}
${regex_body_info}          message-level-${info_level_name}
${regex_body_warning}       message-level-${warning_level_name}
${regex_body_error}         message-level-${error_level_name}

${regex_body_setup}         message-suite-setup
${regex_body_teardown}      message-suite-teardown

${trace_regex}      \\\x1b\\[${expected_trace_start_code}m\\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${trace_level_name.upper()}] \\[${src_module}] \\[print_${trace_level_name}:${trace_code_line_number}] \\[${src_test_name}] ${regex_body_trace}\\\x1b\\[${expected_reset_code}m
${debug_regex}      \\\x1b\\[${expected_debug_start_code}m\\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${debug_level_name.upper()}] \\[${src_module}] \\[print_${debug_level_name}:${debug_code_line_number}] \\[${src_test_name}] ${regex_body_debug}\\\x1b\\[${expected_reset_code}m
${info_regex}       \\\x1b\\[${expected_info_start_code}m\\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${info_level_name.upper()}] \\[${src_module}] \\[print_${info_level_name}:${info_code_line_number}] \\[${src_test_name}] ${regex_body_info}\\\x1b\\[${expected_reset_code}m
${warning_regex}    \\\x1b\\[${expected_warning_start_code}m\\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${warning_level_name.upper()}] \\[${src_module}] \\[print_${warning_level_name}:${warning_code_line_number}] \\[${src_test_name}] ${regex_body_warning}\\\x1b\\[${expected_reset_code}m
${error_regex}      \\\x1b\\[${expected_error_start_code}m\\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${error_level_name.upper()}] \\[${src_module}] \\[print_${error_level_name}:${error_code_line_number}] \\[${src_test_name}] ${regex_body_error}\\\x1b\\[${expected_reset_code}m

${setup_regex}      \\\x1b\\[${expected_info_start_code}m\\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${info_level_name.upper()}] \\[${src_module}] \\[print_suite_setup:${setup_code_line_number}] \\[${setup_test_name}] ${regex_body_setup}\\\x1b\\[${expected_reset_code}m
${teardown_regex}   \\\x1b\\[${expected_info_start_code}m\\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${info_level_name.upper()}] \\[${src_module}] \\[print_suite_teardown:${teardown_code_line_number}] \\[${teardown_test_name}] ${regex_body_teardown}\\\x1b\\[${expected_reset_code}m

${regex_header_msg}     <msg timestamp="[\\d]{{8}} [\\d]{{2}}:[\\d]{{2}}:[\\d]{{2}}.[\\d]{{3}}" level="{}" html="true">&lt;div style='color: {}'&gt;
${regex_header_log}     \\[{}] \\[{}] \\[{}:{}] \\[{}]
${regex_trailer}        &lt;\\/div&gt;<\\/msg>

*** Test Cases ***
Check console and output at trace level
    ${logging_level}                Set Variable    TRACE
    ${output_dir}                   Set Variable    ${TUT_OUTPUT_LEVEL_TRACE_DIR}
    ${output_file}                  Set Variable    ${output_dir}/output.xml

    ${expected_stdout_line_count}   Set Variable    ${15}
    ${expected_stderr_line_count}   Set Variable    ${2}

    Create Directory    ${output_dir}
    ${result}       Run Process     robot   --loglevel  ${logging_level}   ${TUT}  cwd=${output_dir}

    @{stdout_lines}     Split String     ${result.stdout}   \n
    @{stderr_lines}     Split String     ${result.stderr}   \n

    Log List    ${stdout_lines}
    Log List    ${stderr_lines}

    ${stdout_line_count}    Get Line Count  ${result.stdout}
    Should Be Equal         ${expected_stdout_line_count}   ${stdout_line_count}

    ${stderr_line_count}    Get Line Count  ${result.stderr}
    Should Be Equal         ${expected_stderr_line_count}   ${stderr_line_count}

    ${trace_line}       Get From List   ${stdout_lines}     4
    ${debug_line}       Get From List   ${stdout_lines}     5
    ${info_line}        Get From List   ${stdout_lines}     6

    ${warning_line}     Get From List   ${stderr_lines}     0
    ${error_line}       Get From List   ${stderr_lines}     1

    # Assert stdout lines

    Should Match Regexp     ${trace_line}       ${trace_regex}
    Should Match Regexp     ${debug_line}       ${debug_regex}
    Should Match Regexp     ${info_line}        ${info_regex}
    Should Match Regexp     ${warning_line}     ${warning_regex}
    Should Match Regexp     ${error_line}       ${error_regex}

    # Assert output lines

    ${log_file}             Get File            ${output_file}
    @{log_file_lines}       Split to lines      ${log_file}

    Log List    ${log_file_lines}

    ${trace_line}       Get From List   ${log_file_lines}     7
    ${debug_line}       Get From List   ${log_file_lines}     14
    ${info_line}        Get From List   ${log_file_lines}     21
    ${warning_line}     Get From List   ${log_file_lines}     28
    ${error_line}       Get From List   ${log_file_lines}     35

    ${regex_header_msg_trace}           Format String   ${regex_header_msg}     TRACE   ${expected_trace_color}
    ${regex_header_log_trace}           Format String   ${regex_header_log}     ${trace_level_name.upper()}     ${src_module}    print_${trace_level_name}  ${trace_code_line_number}   ${src_test_name}
    ${regex_trace_line}                 Set Variable    ${regex_header_msg_trace}${regex_header_log_trace}

    ${regex_header_msg_debug}           Format String   ${regex_header_msg}     DEBUG   ${expected_debug_color}
    ${regex_header_log_debug}           Format String   ${regex_header_log}     ${debug_level_name.upper()}     ${src_module}    print_${debug_level_name}  ${debug_code_line_number}   ${src_test_name}
    ${regex_debug_line}                 Set Variable    ${regex_header_msg_debug}${regex_header_log_debug}

    ${regex_header_msg_info}            Format String   ${regex_header_msg}     INFO   ${expected_info_color}
    ${regex_header_log_info}            Format String   ${regex_header_log}     ${info_level_name.upper()}     ${src_module}    print_${info_level_name}  ${info_code_line_number}   ${src_test_name}
    ${regex_info_line}                  Set Variable    ${regex_header_msg_info}${regex_header_log_info}

    ${regex_header_msg_warning}         Format String   ${regex_header_msg}     WARN   ${expected_warning_color}
    ${regex_header_log_warning}         Format String   ${regex_header_log}     ${warning_level_name.upper()}     ${src_module}    print_${warning_level_name}  ${warning_code_line_number}   ${src_test_name}
    ${regex_warning_line}               Set Variable    ${regex_header_msg_warning}${regex_header_log_warning}

    ${regex_header_msg_error}           Format String   ${regex_header_msg}     ERROR   ${expected_error_color}
    ${regex_header_log_error}           Format String   ${regex_header_log}     ${error_level_name.upper()}     ${src_module}    print_${error_level_name}  ${error_code_line_number}   ${src_test_name}
    ${regex_error_line}                 Set Variable    ${regex_header_msg_error}${regex_header_log_error}

    Should Match Regexp     ${trace_line}       ${regex_trace_line}
    Should Match Regexp     ${debug_line}       ${regex_debug_line}
    Should Match Regexp     ${info_line}        ${regex_info_line}
    Should Match Regexp     ${warning_line}     ${regex_warning_line}
    Should Match Regexp     ${error_line}       ${regex_error_line}


Check console and output at debug level
    ${logging_level}                Set Variable    DEBUG
    ${output_dir}                   Set Variable    ${TUT_OUTPUT_LEVEL_DEBUG_DIR}
    ${output_file}                  Set Variable    ${output_dir}/output.xml

    ${expected_stdout_line_count}   Set Variable    ${14}
    ${expected_stderr_line_count}   Set Variable    ${2}

    Create Directory    ${output_dir}
    ${result}       Run Process     robot   --loglevel  ${logging_level}   ${TUT}  cwd=${output_dir}

    @{stdout_lines}     Split String     ${result.stdout}   \n
    @{stderr_lines}     Split String     ${result.stderr}   \n

    Log List    ${stdout_lines}
    Log List    ${stderr_lines}

    ${stdout_line_count}    Get Line Count  ${result.stdout}
    Should Be Equal         ${expected_stdout_line_count}   ${stdout_line_count}

    ${stderr_line_count}    Get Line Count  ${result.stderr}
    Should Be Equal         ${expected_stderr_line_count}   ${stderr_line_count}

    ${debug_line}       Get From List   ${stdout_lines}     4
    ${info_line}        Get From List   ${stdout_lines}     5

    ${warning_line}     Get From List   ${stderr_lines}     0
    ${error_line}       Get From List   ${stderr_lines}     1

    # Assert stdout lines

    Should Match Regexp     ${debug_line}       ${debug_regex}
    Should Match Regexp     ${info_line}        ${info_regex}
    Should Match Regexp     ${warning_line}     ${warning_regex}
    Should Match Regexp     ${error_line}       ${error_regex}

    # Assert output lines

    ${log_file}             Get File            ${output_file}
    @{log_file_lines}       Split to lines      ${log_file}

    Log List    ${log_file_lines}

    ${debug_line}       Get From List   ${log_file_lines}     10
    ${info_line}        Get From List   ${log_file_lines}     15
    ${warning_line}     Get From List   ${log_file_lines}     20
    ${error_line}       Get From List   ${log_file_lines}     25

    ${regex_header_msg_debug}           Format String   ${regex_header_msg}     DEBUG   ${expected_debug_color}
    ${regex_header_log_debug}           Format String   ${regex_header_log}     ${debug_level_name.upper()}     ${src_module}    print_${debug_level_name}  ${debug_code_line_number}   ${src_test_name}
    ${regex_debug_line}                 Set Variable    ${regex_header_msg_debug}${regex_header_log_debug}

    ${regex_header_msg_info}            Format String   ${regex_header_msg}     INFO   ${expected_info_color}
    ${regex_header_log_info}            Format String   ${regex_header_log}     ${info_level_name.upper()}     ${src_module}    print_${info_level_name}  ${info_code_line_number}   ${src_test_name}
    ${regex_info_line}                  Set Variable    ${regex_header_msg_info}${regex_header_log_info}

    ${regex_header_msg_warning}         Format String   ${regex_header_msg}     WARN   ${expected_warning_color}
    ${regex_header_log_warning}         Format String   ${regex_header_log}     ${warning_level_name.upper()}     ${src_module}    print_${warning_level_name}  ${warning_code_line_number}   ${src_test_name}
    ${regex_warning_line}               Set Variable    ${regex_header_msg_warning}${regex_header_log_warning}

    ${regex_header_msg_error}           Format String   ${regex_header_msg}     ERROR   ${expected_error_color}
    ${regex_header_log_error}           Format String   ${regex_header_log}     ${error_level_name.upper()}     ${src_module}    print_${error_level_name}  ${error_code_line_number}   ${src_test_name}
    ${regex_error_line}                 Set Variable    ${regex_header_msg_error}${regex_header_log_error}

    Should Match Regexp     ${debug_line}       ${regex_debug_line}
    Should Match Regexp     ${info_line}        ${regex_info_line}
    Should Match Regexp     ${warning_line}     ${regex_warning_line}
    Should Match Regexp     ${error_line}       ${regex_error_line}


Check console and output at info level
    ${logging_level}                Set Variable    INFO
    ${output_dir}                   Set Variable    ${TUT_OUTPUT_LEVEL_INFO_DIR}
    ${output_file}                  Set Variable    ${output_dir}/output.xml

    ${expected_stdout_line_count}   Set Variable    ${13}
    ${expected_stderr_line_count}   Set Variable    ${2}

    Create Directory    ${output_dir}
    ${result}       Run Process     robot   --loglevel  ${logging_level}   ${TUT}  cwd=${output_dir}

    @{stdout_lines}     Split String     ${result.stdout}   \n
    @{stderr_lines}     Split String     ${result.stderr}   \n

    Log List    ${stdout_lines}
    Log List    ${stderr_lines}

    ${stdout_line_count}    Get Line Count  ${result.stdout}
    Should Be Equal         ${expected_stdout_line_count}   ${stdout_line_count}

    ${stderr_line_count}    Get Line Count  ${result.stderr}
    Should Be Equal         ${expected_stderr_line_count}   ${stderr_line_count}

    ${info_line}            Get From List   ${stdout_lines}     4

    ${warning_line}         Get From List   ${stderr_lines}     0
    ${error_line}           Get From List   ${stderr_lines}     1

    # Assert stdout lines

    Should Match Regexp     ${info_line}        ${info_regex}
    Should Match Regexp     ${warning_line}     ${warning_regex}
    Should Match Regexp     ${error_line}       ${error_regex}

    # Assert output lines

    ${log_file}             Get File            ${output_file}
    @{log_file_lines}       Split to lines      ${log_file}

    Log List    ${log_file_lines}

    ${info_line}        Get From List   ${log_file_lines}     14
    ${warning_line}     Get From List   ${log_file_lines}     19
    ${error_line}       Get From List   ${log_file_lines}     24

    ${regex_header_msg_info}            Format String   ${regex_header_msg}     INFO   ${expected_info_color}
    ${regex_header_log_info}            Format String   ${regex_header_log}     ${info_level_name.upper()}     ${src_module}    print_${info_level_name}  ${info_code_line_number}   ${src_test_name}
    ${regex_info_line}                  Set Variable    ${regex_header_msg_info}${regex_header_log_info}

    ${regex_header_msg_warning}         Format String   ${regex_header_msg}     WARN   ${expected_warning_color}
    ${regex_header_log_warning}         Format String   ${regex_header_log}     ${warning_level_name.upper()}     ${src_module}    print_${warning_level_name}  ${warning_code_line_number}   ${src_test_name}
    ${regex_warning_line}               Set Variable    ${regex_header_msg_warning}${regex_header_log_warning}

    ${regex_header_msg_error}           Format String   ${regex_header_msg}     ERROR   ${expected_error_color}
    ${regex_header_log_error}           Format String   ${regex_header_log}     ${error_level_name.upper()}     ${src_module}    print_${error_level_name}  ${error_code_line_number}   ${src_test_name}
    ${regex_error_line}                 Set Variable    ${regex_header_msg_error}${regex_header_log_error}

    Should Match Regexp     ${info_line}        ${regex_info_line}
    Should Match Regexp     ${warning_line}     ${regex_warning_line}
    Should Match Regexp     ${error_line}       ${regex_error_line}


Check console and output at warning level
    ${logging_level}                Set Variable    WARN
    ${output_dir}                   Set Variable    ${TUT_OUTPUT_LEVEL_WARNING_DIR}
    ${output_file}                  Set Variable    ${output_dir}/output.xml

    ${expected_stdout_line_count}   Set Variable    ${11}
    ${expected_stderr_line_count}   Set Variable    ${2}

    Create Directory    ${output_dir}
    ${result}       Run Process     robot   --loglevel  ${logging_level}   ${TUT}  cwd=${output_dir}

    @{stdout_lines}     Split String     ${result.stdout}   \n
    @{stderr_lines}     Split String     ${result.stderr}   \n

    Log List    ${stdout_lines}
    Log List    ${stderr_lines}

    ${stdout_line_count}    Get Line Count  ${result.stdout}
    Should Be Equal         ${expected_stdout_line_count}   ${stdout_line_count}

    ${stderr_line_count}    Get Line Count  ${result.stderr}
    Should Be Equal         ${expected_stderr_line_count}   ${stderr_line_count}

    ${warning_line}         Get From List   ${stderr_lines}     0
    ${error_line}           Get From List   ${stderr_lines}     1

    # Assert stdout lines

    Should Match Regexp     ${warning_line}     ${warning_regex}
    Should Match Regexp     ${error_line}       ${error_regex}

    # Assert output lines

    ${log_file}             Get File            ${output_file}
    @{log_file_lines}       Split to lines      ${log_file}

    Log List    ${log_file_lines}

    ${warning_line}     Get From List   ${log_file_lines}     18
    ${error_line}       Get From List   ${log_file_lines}     23

    ${regex_header_msg_warning}         Format String   ${regex_header_msg}     WARN   ${expected_warning_color}
    ${regex_header_log_warning}         Format String   ${regex_header_log}     ${warning_level_name.upper()}     ${src_module}    print_${warning_level_name}  ${warning_code_line_number}   ${src_test_name}
    ${regex_warning_line}               Set Variable    ${regex_header_msg_warning}${regex_header_log_warning}

    ${regex_header_msg_error}           Format String   ${regex_header_msg}     ERROR   ${expected_error_color}
    ${regex_header_log_error}           Format String   ${regex_header_log}     ${error_level_name.upper()}     ${src_module}    print_${error_level_name}  ${error_code_line_number}   ${src_test_name}
    ${regex_error_line}                 Set Variable    ${regex_header_msg_error}${regex_header_log_error}

    Should Match Regexp     ${warning_line}     ${regex_warning_line}
    Should Match Regexp     ${error_line}       ${regex_error_line}


Check console and output at error level
    ${logging_level}                Set Variable    ERROR
    ${output_dir}                   Set Variable    ${TUT_OUTPUT_LEVEL_ERROR_DIR}
    ${output_file}                  Set Variable    ${output_dir}/output.xml

    ${expected_stdout_line_count}   Set Variable    ${11}
    ${expected_stderr_line_count}   Set Variable    ${1}

    Create Directory    ${output_dir}
    ${result}       Run Process     robot   --loglevel  ${logging_level}   ${TUT}  cwd=${output_dir}

    @{stdout_lines}     Split String     ${result.stdout}   \n
    @{stderr_lines}     Split String     ${result.stderr}   \n

    Log List    ${stdout_lines}
    Log List    ${stderr_lines}

    ${stdout_line_count}    Get Line Count  ${result.stdout}
    Should Be Equal         ${expected_stdout_line_count}   ${stdout_line_count}

    ${stderr_line_count}    Get Line Count  ${result.stderr}
    Should Be Equal         ${expected_stderr_line_count}   ${stderr_line_count}

    ${error_line}           Get From List   ${stderr_lines}     0

    # Assert stdout lines

    Should Match Regexp     ${error_line}       ${error_regex}

    # Assert output lines

    ${log_file}             Get File            ${output_file}
    @{log_file_lines}       Split to lines      ${log_file}

    Log List    ${log_file_lines}

    ${error_line}       Get From List   ${log_file_lines}     22

    ${regex_header_msg_error}           Format String   ${regex_header_msg}     ERROR   ${expected_error_color}
    ${regex_header_log_error}           Format String   ${regex_header_log}     ${error_level_name.upper()}     ${src_module}    print_${error_level_name}  ${error_code_line_number}   ${src_test_name}
    ${regex_error_line}                 Set Variable    ${regex_header_msg_error}${regex_header_log_error}

    Should Match Regexp     ${error_line}       ${regex_error_line}


Check console and output at default level
    ${output_dir}                   Set Variable    ${TUT_OUTPUT_LEVEL_DEFAULT_DIR}
    ${output_file}                  Set Variable    ${output_dir}/output.xml

    ${expected_stdout_line_count}   Set Variable    ${13}
    ${expected_stderr_line_count}   Set Variable    ${2}

    Create Directory    ${output_dir}
    ${result}       Run Process     robot   ${TUT}  cwd=${output_dir}

    @{stdout_lines}     Split String     ${result.stdout}   \n
    @{stderr_lines}     Split String     ${result.stderr}   \n

    Log List    ${stdout_lines}
    Log List    ${stderr_lines}

    ${stdout_line_count}    Get Line Count  ${result.stdout}
    Should Be Equal         ${expected_stdout_line_count}   ${stdout_line_count}

    ${stderr_line_count}    Get Line Count  ${result.stderr}
    Should Be Equal         ${expected_stderr_line_count}   ${stderr_line_count}

    ${info_line}            Get From List   ${stdout_lines}     4

    ${warning_line}         Get From List   ${stderr_lines}     0
    ${error_line}           Get From List   ${stderr_lines}     1

    # Assert stdout lines

    Should Match Regexp     ${info_line}        ${info_regex}
    Should Match Regexp     ${warning_line}     ${warning_regex}
    Should Match Regexp     ${error_line}       ${error_regex}

    # Assert output lines

    ${log_file}             Get File            ${output_file}
    @{log_file_lines}       Split to lines      ${log_file}

    Log List    ${log_file_lines}

    ${info_line}        Get From List   ${log_file_lines}     14
    ${warning_line}     Get From List   ${log_file_lines}     19
    ${error_line}       Get From List   ${log_file_lines}     24

    ${regex_header_msg_info}            Format String   ${regex_header_msg}     INFO   ${expected_info_color}
    ${regex_header_log_info}            Format String   ${regex_header_log}     ${info_level_name.upper()}     ${src_module}    print_${info_level_name}  ${info_code_line_number}   ${src_test_name}
    ${regex_info_line}                  Set Variable    ${regex_header_msg_info}${regex_header_log_info}

    ${regex_header_msg_warning}         Format String   ${regex_header_msg}     WARN   ${expected_warning_color}
    ${regex_header_log_warning}         Format String   ${regex_header_log}     ${warning_level_name.upper()}     ${src_module}    print_${warning_level_name}  ${warning_code_line_number}   ${src_test_name}
    ${regex_warning_line}               Set Variable    ${regex_header_msg_warning}${regex_header_log_warning}

    ${regex_header_msg_error}           Format String   ${regex_header_msg}     ERROR   ${expected_error_color}
    ${regex_header_log_error}           Format String   ${regex_header_log}     ${error_level_name.upper()}     ${src_module}    print_${error_level_name}  ${error_code_line_number}   ${src_test_name}
    ${regex_error_line}                 Set Variable    ${regex_header_msg_error}${regex_header_log_error}

    Should Match Regexp     ${info_line}        ${regex_info_line}
    Should Match Regexp     ${warning_line}     ${regex_warning_line}
    Should Match Regexp     ${error_line}       ${regex_error_line}

Check console and output of setup and teardown
    ${output_dir}                   Set Variable    ${TUT_OUTPUT_SETUP_TEARDOWN_DIR}
    ${output_file}                  Set Variable    ${output_dir}/output.xml

    ${expected_stdout_line_count}   Set Variable    ${13}
    ${expected_stderr_line_count}   Set Variable    ${0}

    Create Directory    ${output_dir}
    ${result}       Run Process     robot   ${TUT_SETUP_TEARDOWN}  cwd=${output_dir}

    @{stdout_lines}     Split String     ${result.stdout}   \n
    @{stderr_lines}     Split String     ${result.stderr}   \n

    Log List    ${stdout_lines}
    Log List    ${stderr_lines}

    ${stdout_line_count}    Get Line Count  ${result.stdout}
    Should Be Equal         ${expected_stdout_line_count}   ${stdout_line_count}

    ${stderr_line_count}    Get Line Count  ${result.stderr}
    Should Be Equal         ${expected_stderr_line_count}   ${stderr_line_count}

    ${setup_line}           Get From List   ${stdout_lines}     3
    ${teardown_line}        Get From List   ${stdout_lines}     6

    # Assert stdout lines

    Should Match Regexp     ${setup_line}       ${setup_regex}
    Should Match Regexp     ${teardown_line}    ${teardown_regex}

    # Assert output lines

    ${log_file}             Get File            ${output_file}
    @{log_file_lines}       Split to lines      ${log_file}

    Log List    ${log_file_lines}

    ${setup_line}        Get From List   ${log_file_lines}     5
    ${teardown_line}     Get From List   ${log_file_lines}     17

    ${regex_header_msg_info}            Format String   ${regex_header_msg}     INFO   ${expected_info_color}
    ${regex_header_log_setup}           Format String   ${regex_header_log}     ${info_level_name.upper()}     ${src_module}    print_suite_setup  ${setup_code_line_number}   ${setup_test_name}
    ${regex_info_setup}                 Set Variable    ${regex_header_msg_info}${regex_header_log_setup}

    ${regex_header_msg_info}            Format String   ${regex_header_msg}     INFO   ${expected_info_color}
    ${regex_header_log_teardown}        Format String   ${regex_header_log}     ${info_level_name.upper()}     ${src_module}    print_suite_teardown  ${teardown_code_line_number}   ${teardown_test_name}
    ${regex_info_teardown}              Set Variable    ${regex_header_msg_info}${regex_header_log_teardown}

    Should Match Regexp     ${setup_line}        ${regex_info_setup}
    Should Match Regexp     ${teardown_line}     ${regex_info_teardown}
