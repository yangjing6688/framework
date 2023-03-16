*** Settings ***
Library    TUTLibrary.py
Suite Setup     Print Suite Setup       message-suite-setup
Suite Teardown  Print Suite Teardown    message-suite-teardown

*** Variables ***

*** Test Cases ***
Empty
    No Operation