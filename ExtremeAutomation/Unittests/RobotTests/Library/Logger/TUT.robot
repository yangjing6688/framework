*** Settings ***
Library    TUTLibrary.py

*** Variables ***

*** Test Cases ***
Print all levels
    Print Step  message-level-step
    Print CLI  message-level-cli
    Print Trace  message-level-trace
    Print Info  message-level-info
    Print Debug  message-level-debug
    Print Warning  message-level-warning
    Print Critical  message-level-critical
    Print Error  message-level-error

