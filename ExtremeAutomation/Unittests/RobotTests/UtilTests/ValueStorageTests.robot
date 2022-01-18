# *** Settings ***
# Resource         ExtremeAutomation/Resources/Libraries/DefaultLibraries.robot
# Library          ExtremeAutomation/Keywords/Utils/DeviceValueStorage.py
# Variables        ExtremeAutomation/Unittests/Resources/2node_1.yaml

# Documentation    Regression unit cases for Device Value Storage

# Suite Setup      Test Suite Setup
# Suite Teardown   Test Suite Cleanup

# *** Variables ***
# ${value_a}   123456789
# ${value_b}   987654321
# ${value_c}   12345678987654321

# *** Test Cases ***
# Basic Storage and Retrieval
    # [Tags]    REGRESSION
    # Add Value         ${netelem1.name}   test_value_A         ${value_a}
    # Should be Equal   ${netelem1.value_storage.test_value_A}  ${value_a}

# Storage, Update and Retrieval
    # [Tags]    REGRESSION
    # Add Value         ${netelem1.name}   test_value_A         ${value_a}
    # Update Value      ${netelem1.name}   test_value_A         ${value_b}
    # Should be Equal   ${netelem1.value_storage.test_value_A}  ${value_b}

# Multiple Storage and Retrieval - Single DUT
    # [Tags]    REGRESSION
    # Add Value         ${netelem1.name}   test_value_A         ${value_a}
    # Add Value         ${netelem1.name}   test_value_B         ${value_b}
    # Should be Equal   ${netelem1.value_storage.test_value_A}  ${value_a}
    # Should be Equal   ${netelem1.value_storage.test_value_B}  ${value_b}

# Multiple Storage and Retrieval - Two DUT
    # [Tags]    REGRESSION
    # Add Value         ${netelem1.name}   test_value_A         ${value_a}
    # Add Value         ${netelem2.name}   test_value_A         ${value_b}
    # Should be Equal   ${netelem1.value_storage.test_value_A}  ${value_a}
    # Should be Equal   ${netelem2.value_storage.test_value_A}  ${value_b}

# Multiple Storage, Update and Retrieval - Two DUT
    # [Tags]    REGRESSION
    # Add Value         ${netelem1.name}   test_value_A         ${value_a}
    # Add Value         ${netelem2.name}   test_value_A         ${value_b}
    # Update Value      ${netelem2.name}   test_value_A         ${value_c}
    # Should be Equal   ${netelem1.value_storage.test_value_A}  ${value_a}
    # Should be Equal   ${netelem2.value_storage.test_value_A}  ${value_c}

# Storage, Overwrite and Retrieval
    # [Tags]    REGRESSION
    # Add Value         ${netelem1.name}   test_value_A         ${value_a}
    # Add Value         ${netelem1.name}   test_value_A         ${value_b}
    # Add Value         ${netelem1.name}   test_value_B         ${value_b}
    # Update Value      ${netelem1.name}   test_value_C         ${value_c}
    # Should be Equal   ${netelem1.value_storage.test_value_A}  ${value_b}
    # Should be Equal   ${netelem1.value_storage.test_value_B}  ${value_b}
    # Should be Equal   ${netelem1.value_storage.test_value_C}  ${value_c}

# *** Keywords ***
# Test Suite Setup
    # Connect to All Network Elements

# Test Suite Cleanup
    # Close Connection to All Network Elements