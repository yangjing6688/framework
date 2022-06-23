*** Settings ***
Resource        ../../../ExtremeAutomation/Resources/Libraries/DefaultLibraries.robot
Variables    ../Resources/specialYamlOfDevices.yaml
Library     ../../../extauto/common/Cli.py
Force Tags      testbed_1_node

*** Test Cases ***
test_01_log_all_generic_devices
    [Documentation]     Log into All Device Types
    Base Test Suite Setup
    Base Test Suite Cleanup

test_02_log_into_exos
    [Documentation]     Log into EXOS

    ${SPAWN}=        Open Spawn          ${netelem1.ip}   ${netelem1.port}      ${netelem1.username}       ${netelem1.password}        ${netelem1.cli_type}
    send   ${SPAWN}   show version
    send   ${SPAWN}   error commmand isssued   expect_error=true
    Close Spawn     ${SPAWN}

test_03_log_into_voss
    [Documentation]     Log into VOSS

    ${SPAWN}=        Open Spawn          ${netelem2.ip}   ${netelem2.port}      ${netelem2.username}       ${netelem2.password}        ${netelem2.cli_type}
    send   ${SPAWN}   show sys-info uboot
    send   ${SPAWN}   error commmand isssued   expect_error=true
    Close Spawn     ${SPAWN}

test_04_log_into_wing_ap
    [Documentation]     Log into Wing

    ${SPAWN}=        Open Spawn          ${wing1.ip}   ${wing1.port}      ${wing1.username}       ${wing1.password}        ${wing1.cli_type}
    send   ${SPAWN}   show boot
    send   ${SPAWN}   error commmand isssued   expect_error=true
    Close Spawn     ${SPAWN}

test_05_log_into_sr_router_ap
    [Documentation]     Log into SR router

    ${SPAWN}=        Open Spawn          ${aerohive_sw1.ip}   ${aerohive_sw1.port}      ${aerohive_sw1.username}       ${aerohive_sw1.password}        ${aerohive_sw1.cli_type}
    send   ${SPAWN}   show sysinfo
    send   ${SPAWN}   error commmand isssued   expect_error=true
    Close Spawn     ${SPAWN}

test_06_log_into_xr_router_ap
    [Documentation]     Log into XR Router

    ${SPAWN}=        Open Spawn          ${router1.ip}   ${router1.port}      ${router1.username}       ${router1.password}        ${router1.cli_type}      connection_method=console
    send   ${SPAWN}   show system disk-info
    send   ${SPAWN}   error commmand isssued   expect_error=true
    Close Spawn     ${SPAWN}

test_07_log_into_ap
    [Documentation]     Log into AP

    ${SPAWN}=        Open Spawn          ${ap1.ip}   ${ap1.port}      ${ap1.username}       ${ap1.password}        ${ap1.cli_type}
    send   ${SPAWN}   show version
    send   ${SPAWN}   error commmand isssued   expect_error=true
    Close Spawn     ${SPAWN}

test_08_log_into_win_mu
    [Documentation]     Log into Windows MU

    ${SPAWN}=        Open Spawn          ${mu1.ip}   ${mu1.port}      ${mu1.username}       ${mu1.password}        ${mu1.cli_type}
    send   ${SPAWN}   dir
    send   ${SPAWN}   error commmand isssued   expect_error=true
    Close Spawn     ${SPAWN}

test_09_log_into_mac_mu
    [Documentation]     Log into Mac MU

    ${SPAWN}=        Open Spawn          ${mu2.ip}   ${mu2.port}      ${mu2.username}       ${mu2.password}        ${mu2.cli_type}
    send   ${SPAWN}   ls -al
    send   ${SPAWN}   error commmand isssued   expect_error=true
    Close Spawn     ${SPAWN}

test_10_log_into_a3
    [Documentation]     Log into A3

    ${SPAWN}=        Open Spawn          ${a3.node1_ip}   ${a3.console_port}      ${a3.console_username}       ${a3.console_password}        ${a3.cli_type}
    send   ${SPAWN}   ls -al
    send   ${SPAWN}   error commmand isssued   expect_error=true
    Close Spawn     ${SPAWN}

test_11_log_into_linux
    [Documentation]     Log into Linux MU

    ${SPAWN}=        Open Spawn          ${mu3.ip}   ${mu3.port}      ${mu3.username}       ${mu3.password}        ${mu3.cli_type}
    send   ${SPAWN}   ls -al
    send   ${SPAWN}   error commmand isssued   expect_error=true
    Close Spawn     ${SPAWN}



