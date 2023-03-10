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
Library    String
Library    Collections

*** Variables ***
${TUT}                      ${CURDIR}/TUT.robot
${TUT_OUTPUT_DIR}           ${EXECDIR}/tut_output
${TUT_OUTPUT_LEVEL_TRACE_DIR}       ${TUT_OUTPUT_DIR}/level_trace
${TUT_OUTPUT_LEVEL_DEBUG_DIR}       ${TUT_OUTPUT_DIR}/level_debug
${TUT_OUTPUT_LEVEL_INFO_DIR}        ${TUT_OUTPUT_DIR}/level_info
${TUT_OUTPUT_LEVEL_DEFAULT_DIR}     ${TUT_OUTPUT_DIR}/level_default

*** Test Cases ***
Run and check console at trace level
    ${logging_level}                Set Variable    TRACE
    ${output_dir}                   Set Variable    ${TUT_OUTPUT_LEVEL_TRACE_DIR}
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

    ${level_name} =         Set Variable    debug
    ${code_line_number} =   Set Variable    18
    ${regex} =              Set Variable    \\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${level_name.upper()}] \\[TUTLibrary] \\[print_${level_name}:${code_line_number}] \\[Print all levels] message-level-${level_name}
    Should Match Regexp     ${debug_line}   ${regex}

    ${level_name} =         Set Variable    info
    ${code_line_number} =   Set Variable    21
    ${regex} =              Set Variable    \\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${level_name.upper()}] \\[TUTLibrary] \\[print_${level_name}:${code_line_number}] \\[Print all levels] message-level-${level_name}
    Should Match Regexp     ${info_line}    ${regex}

#   Assert stderr lines

    ${level_name} =         Set Variable        warning
    ${code_line_number} =   Set Variable        24
    ${regex} =              Set Variable        \\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${level_name.upper()}] \\[TUTLibrary] \\[print_${level_name}:${code_line_number}] \\[Print all levels] message-level-${level_name}
    Should Match Regexp     ${warning_line}     ${regex}

    ${level_name} =         Set Variable        error
    ${code_line_number} =   Set Variable        30
    ${regex} =              Set Variable        \\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${level_name.upper()}] \\[TUTLibrary] \\[print_${level_name}:${code_line_number}] \\[Print all levels] message-level-${level_name}
    Should Match Regexp     ${error_line}       ${regex}


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

    ${level_name} =         Set Variable    debug
    ${code_line_number} =   Set Variable    18
    ${regex} =              Set Variable    \\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${level_name.upper()}] \\[TUTLibrary] \\[print_${level_name}:${code_line_number}] \\[Print all levels] message-level-${level_name}
    Should Match Regexp     ${debug_line}   ${regex}

    ${level_name} =         Set Variable    info
    ${code_line_number} =   Set Variable    21
    ${regex} =              Set Variable    \\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${level_name.upper()}] \\[TUTLibrary] \\[print_${level_name}:${code_line_number}] \\[Print all levels] message-level-${level_name}
    Should Match Regexp     ${info_line}    ${regex}

#   Assert stderr lines

    ${level_name} =         Set Variable        warning
    ${code_line_number} =   Set Variable        24
    ${regex} =              Set Variable        \\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${level_name.upper()}] \\[TUTLibrary] \\[print_${level_name}:${code_line_number}] \\[Print all levels] message-level-${level_name}
    Should Match Regexp     ${warning_line}     ${regex}

    ${level_name} =         Set Variable        error
    ${code_line_number} =   Set Variable        30
    ${regex} =              Set Variable        \\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${level_name.upper()}] \\[TUTLibrary] \\[print_${level_name}:${code_line_number}] \\[Print all levels] message-level-${level_name}
    Should Match Regexp     ${error_line}       ${regex}


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

    ${level_name} =         Set Variable    info
    ${code_line_number} =   Set Variable    21
    ${regex} =              Set Variable    \\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${level_name.upper()}] \\[TUTLibrary] \\[print_${level_name}:${code_line_number}] \\[Print all levels] message-level-${level_name}
    Should Match Regexp     ${info_line}    ${regex}

#   Assert stderr lines

    ${level_name} =         Set Variable        warning
    ${code_line_number} =   Set Variable        24
    ${regex} =              Set Variable        \\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${level_name.upper()}] \\[TUTLibrary] \\[print_${level_name}:${code_line_number}] \\[Print all levels] message-level-${level_name}
    Should Match Regexp     ${warning_line}     ${regex}

    ${level_name} =         Set Variable        error
    ${code_line_number} =   Set Variable        30
    ${regex} =              Set Variable        \\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${level_name.upper()}] \\[TUTLibrary] \\[print_${level_name}:${code_line_number}] \\[Print all levels] message-level-${level_name}
    Should Match Regexp     ${error_line}       ${regex}


Run and check console at default level
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

    ${level_name} =         Set Variable    info
    ${code_line_number} =   Set Variable    21
    ${regex} =              Set Variable    \\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${level_name.upper()}] \\[TUTLibrary] \\[print_${level_name}:${code_line_number}] \\[Print all levels] message-level-${level_name}
    Should Match Regexp     ${info_line}    ${regex}

#   Assert stderr lines

    ${level_name} =         Set Variable        warning
    ${code_line_number} =   Set Variable        24
    ${regex} =              Set Variable        \\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${level_name.upper()}] \\[TUTLibrary] \\[print_${level_name}:${code_line_number}] \\[Print all levels] message-level-${level_name}
    Should Match Regexp     ${warning_line}     ${regex}

    ${level_name} =         Set Variable        error
    ${code_line_number} =   Set Variable        30
    ${regex} =              Set Variable        \\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2}),(\\d{3})] \\[${level_name.upper()}] \\[TUTLibrary] \\[print_${level_name}:${code_line_number}] \\[Print all levels] message-level-${level_name}
    Should Match Regexp     ${error_line}       ${regex}
