*** Settings ***
Library    KeywordsUserGroups.py
Library    xiq/flows/common/Login.py
Library    xiq/flows/configure/UserGroups.py
Library    Collections
Variables    Environments/${TOPO}
Variables    Environments/${ENV}
Variables    TestBeds/${TESTBED}
Suite Setup     Test Suite Setup
Suite Teardown  Test Suite Cleanup

*** Keywords ***
Test Suite Setup
    Login User          ${tenant_username}    ${tenant_password}

Test Suite Cleanup
    Logout User
    Quit Browser

Cleanup Usergroup
    [Arguments]    ${usergroup_name}

    ${STATUS}=  delete user group    ${usergroup_name}
    should be equal as strings     '${STATUS}'        '1'

Cleanup Usergroups
    [Arguments]    @{usergroup_names}
    FOR    ${item}    IN    @{usergroup_names}
        ${STATUS}=  delete user group    ${item}
        should be equal as strings     '${STATUS}'        '1'
    END

*** Test Cases ***
Test Create User Group
    [Documentation]     Test Objective: Test Create User Group
    ...                 Variation A: DB Location = "LOCAL", Password Type = "PPSK"
    ...                 Variation B: DB Location = "LOCAL", Password Type = "RADIUS"
    ...                 Variation C: DB Location = "CLOUD", Password Type = "PPSK"
    ...                 Variation D: DB Location = "CLOUD", Password Type = "RADIUS"
    ...                 Variation E: Password Type = "PPSK"
    ...                 Variation F: Password Type = "RADIUS"
    ...                 Variation G: DB Location = "LOCAL"
    ...                 Variation H: DB Location = "CLOUD"

    ${Variation_A}=   create dictionary    pass_db_loc=LOCAL     pass_type=ppsk     client_per_ppsk=${None}     pcg_use=${None}     ppsk_classification=${None}
    ${Variation_B}=   create dictionary    pass_db_loc=LOCAL     pass_type=radius   client_per_ppsk=${None}     pcg_use=${None}     ppsk_classification=${None}
    ${Variation_C}=   create dictionary    pass_db_loc=CLOUD     pass_type=ppsk     client_per_ppsk=${None}     pcg_use=${None}     ppsk_classification=${None}     cwp_register=${None}
    ${Variation_D}=   create dictionary    pass_db_loc=CLOUD     pass_type=radius   client_per_ppsk=${None}     pcg_use=${None}     ppsk_classification=${None}
    ${Variation_E}=   create dictionary    pass_type=ppsk       client_per_ppsk=${None}     pcg_use=${None}     ppsk_classification=${None}     cwp_register=${None}
    ${Variation_F}=   create dictionary    pass_type=radius     client_per_ppsk=${None}     pcg_use=${None}     ppsk_classification=${None}
    ${Variation_G}=   create dictionary    pass_db_loc=LOCAL    client_per_ppsk=${None}     pcg_use=${None}     ppsk_classification=${None}
    ${Variation_H}=   create dictionary    pass_db_loc=CLOUD    client_per_ppsk=${None}     pcg_use=${None}     ppsk_classification=${None}     cwp_register=${None}

    ${USER_GROUP_VARIATION_A}=   create dictionary    user_group_config=${Variation_A}  users_config=None
    ${USER_GROUP_VARIATION_B}=   create dictionary    user_group_config=${Variation_B}  users_config=None
    ${USER_GROUP_VARIATION_C}=   create dictionary    user_group_config=${Variation_C}  users_config=None
    ${USER_GROUP_VARIATION_D}=   create dictionary    user_group_config=${Variation_D}  users_config=None
    ${USER_GROUP_VARIATION_E}=   create dictionary    user_group_config=${Variation_E}  users_config=None
    ${USER_GROUP_VARIATION_F}=   create dictionary    user_group_config=${Variation_F}  users_config=None
    ${USER_GROUP_VARIATION_G}=   create dictionary    user_group_config=${Variation_G}  users_config=None
    ${USER_GROUP_VARIATION_H}=   create dictionary    user_group_config=${Variation_H}  users_config=None

    ${STATUS}=  KeywordsUserGroups.create user group   Group_A     user_group_profile=&{USER_GROUP_VARIATION_A}
    should be equal as strings     '${STATUS}'        '1'
    ${STATUS}=  KeywordsUserGroups.create user group   Group_B     user_group_profile=&{USER_GROUP_VARIATION_B}
    should be equal as strings     '${STATUS}'        '1'
    ${STATUS}=  KeywordsUserGroups.create user group   Group_C     user_group_profile=&{USER_GROUP_VARIATION_C}
    should be equal as strings     '${STATUS}'        '1'
    ${STATUS}=  KeywordsUserGroups.create user group   Group_D     user_group_profile=&{USER_GROUP_VARIATION_D}
    should be equal as strings     '${STATUS}'        '1'
    ${STATUS}=  KeywordsUserGroups.create user group   Group_E     user_group_profile=&{USER_GROUP_VARIATION_E}
    should be equal as strings     '${STATUS}'        '1'
    ${STATUS}=  KeywordsUserGroups.create user group   Group_F     user_group_profile=&{USER_GROUP_VARIATION_F}
    should be equal as strings     '${STATUS}'        '1'
    ${STATUS}=  KeywordsUserGroups.create user group   Group_G     user_group_profile=&{USER_GROUP_VARIATION_G}
    should be equal as strings     '${STATUS}'        '1'
    ${STATUS}=  KeywordsUserGroups.create user group   Group_H     user_group_profile=&{USER_GROUP_VARIATION_H}
    should be equal as strings     '${STATUS}'        '1'

    [Teardown]    Cleanup Usergroups     Group_A     Group_B     Group_C     Group_D     Group_E     Group_F     Group_G     Group_H