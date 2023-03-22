*** Settings ***
Documentation       This Robot test is used by RobotLoggerTests.robot

Library    TUTLibrary.py

*** Variables ***

*** Test Cases ***
Print all levels
    Print Trace     message-level-trace
    Print Debug     message-level-debug
    Print Info      message-level-info
    Print Warning   message-level-warning
    Print Error     message-level-error

