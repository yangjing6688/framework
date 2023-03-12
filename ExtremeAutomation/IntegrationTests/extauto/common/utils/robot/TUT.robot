*** Settings ***
Library    TUTLibrary.py

*** Variables ***

*** Test Cases ***
Robot Builtin Import
    Test Robot Builtin Import

Print all levels
    Print Debug     message-level-debug
    Print Info      message-level-info
    Print Warning   message-level-warning
    Print Error     message-level-error

