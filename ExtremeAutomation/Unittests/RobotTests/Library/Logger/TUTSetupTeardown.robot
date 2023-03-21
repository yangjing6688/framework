*** Settings ***
Documentation       This Robot test is used by RobotLoggerTests.robot

Library    TUTLibrary.py
Suite Setup     Print Suite Setup       message-suite-setup
Suite Teardown  Print Suite Teardown    message-suite-teardown

*** Variables ***

*** Test Cases ***
Empty
    No Operation