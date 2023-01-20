class LicenseManagementWebElementsDefs:

    entitlements_no_data = \
        {
            'XPATH': '//div[@data-dojo-attach-point="gridContent"]//div[@class="dgrid-no-data"]',
            'wait_for': 5
        }

    legacy_no_data = \
        {
            'XPATH': '//div[@class="table-show-div-licenseInfoCtl"]//div[@class="ant-table-placeholder" and text()="No data"]',
            'wait_for': 5
        }

    link_xiq_to_extreme_portal_btn = \
        {
            'DESC': 'LINK MY EXTREME PORTAL ACCOUNT',
            'XPATH': '//button[text()="Link my Extreme Portal account"]',
            'wait_for': 5
        }

    xiq_not_linked_to_extreme_portal_status = \
        {
            'DESC': 'XIQ not linked to Extreme Portal',
            'XPATH': '//*[text()[contains(.,"Extreme Portal Account not linked.")]]',
            'wait_for': 3
        }

    unlink_xiq_from_extr_portal_btn = \
        {
            'XPATH': '//button[@data-dojo-attach-point="portalUnlinkBtn" and contains(text(),"Unlink from Extreme Portal")]',
            'wait_for': 3
        }

    xiq_linked_to_extreme_portal_status = \
        {
            'DESC': 'XIQ not linked to Extreme Portal',
            'XPATH': '//span[@data-dojo-attach-point="accountLinkSuccess"]/p[contains(text(),"Successfully linked to a customer account")]',
            'wait_for': 3
        }

    account_successfully_linked = \
        {
            'XPATH': '//*[@data-dojo-attach-point="accountLinkSuccess"]'
        }

    extreme_licensing_portal_btn = \
        {
            'DESC': 'LINK MY EXTREME PORTAL ACCOUNT',
            'XPATH': '//a[@data-dojo-attach-point="portalBtnLicense" and contains(text(),"Extreme Licensing Portal")]',
            'wait_for': 3
        }

    xiq_cust_partner_info = \
        {
            'DESC': 'Message to Customers and Partners when xiq not linked',
            'XPATH': '//*[text()[contains(.,"Thank you for purchasing")]]',
            'wait_for': 5
        }

    gemalto_entitlements_table_header = \
        {
            'DESC': 'LEM entitlements table header',
            'XPATH': '//h4[text()="Entitlements"]',
            'wait_for': 5
        }

    contact_sales_btn = \
        {
            'DESC': 'contact sales button',
            'XPATH': '//button[text()="Contact Sales"]',
            'wait_for': 5
        }

    legacy_entitlements_table_header = \
        {
            'DESC': 'Legacy entitlements table header',
            'XPATH': '//*[text()[contains(.,"Legacy Entitlements")]]'
        }

    unlink_confirm_yes_btn = \
        {
            'XPATH': '//div[@class="ui-cfmsg confirm"]//p[@class="cfm-btns"]//button[@class="btn btn-secondary"]',
            'wait_for': 5
        }

    unlink_confirm_no_btn = \
        {
            'XPATH': '//div[@class="ui-tipbox-con"]//button[@data-dojo-attach-point="noBtn"]',
            'wait_for': 5
        }

    unlink_confirm_msg = \
        {
            'XPATH': '//p[@data-dojo-attach-point="desEl"]',
            'wait_for': 2
        }

    license_table_iframe = \
        {
            'XPATH': '//iframe[@id="iframeIdForLicenseInfo"]',
            'wait_for': 3
        }

    license_table_iframe_attr = '@id="iframeIdForLicenseInfo"'

    legacy_ek_data = \
        {
            'XPATH': '//table//td//div[@class="entitlement-key-div-licenseInfoCtl"]',
            'wait_for': 5
        }

    upgrade_dialog_msg = \
        {
            'XPATH': '//div[@data-dojo-attach-point="mainContent"]',
            'wait_for': 3
        }

    upgrade_iagree_chkbox = \
        {
            'XPATH': '//input[@type="checkbox" and @name="agree" and @data-dojo-attach-point="iAgree"]',
            'wait_for': 3
        }

    upgrade_continue_btn = \
        {
            'XPATH': '//button[@data-dojo-attach-point="continueBtn"]',
            'wait_for': 3
        }

    upgrade_cancel_btn = \
        {
            'XPATH': '//button[@data-dojo-attach-point="closeDialog"]',
            'wait_for': 3
        }

    entitlements_rows = \
        {
            'XPATH': '//div[@data-dojo-attach-point="licenseCtn"]//div[@data-dojo-attach-point="gridContent"]//table[@class="dgrid-row-table"]/tr/td/..',
            
         }

    entitlements_table_feature_col = \
        {
            'DESC': 'Entitlements Table Feature Column',
            'CSS_SELECTOR': 'td.field-gemaltoFeature',
            'XPATH': '//td[contains(@class, "field-gemaltoFeature")]/div'

        }

    entitlements_table_total_col = \
        {
            'DESC': 'Entitlements Table Total Column',
            'CSS_SELECTOR': 'td.field-devices',
            'XPATH': '//td[contains(@class, "field-devices")]/div'

        }

    entitlements_table_available_col = \
        {
            'DESC': 'Entitlements Table Available Column',
            'CSS_SELECTOR': 'td.field-available',
            'XPATH': '//td[contains(@class, "field-available")]',
            
        }

    entitlements_table_activated_col = \
        {
            'DESC': 'Entitlements Table Activated Column',
            'CSS_SELECTOR': 'td.field-activated',
            'XPATH': '//td[contains(@class, "field-activated")]',
            
        }

    legacy_ek_checkbox = \
        {
            'XPATH': '//tr//td/div[contains(@class, "entitlement-key-div-licenseInfoCtl")and contains(text(),"-")]/ancestor::tr//td/span//input[@type="checkbox"]'
        }

    ekey_remove_deactivate_btn = \
        {
            'XPATH': '//button[contains(@class, "ant-btn table-control-key-action-antd-button-licenseInfoCtl ant-btn-primary")]'
        }

    ekey_del_confirm_btn = \
        {
            'XPATH': '//button[contains(@class, "ant-btn ant-btn-primary ant-btn-lg")]'
        }

    ekey_del_cancel_btn = \
        {
            'XPATH': '//button[contains(@class, "ant-btn ant-btn-lg")]'
        }

    ekey_del_success_msg = \
        {
            'XPATH': '//tr[contains(@class, "ant-table-row  ant-table-row-level-0")]//td//div[contains(text(), "Success")]'
        }

    ekey_del_confirm_msg_ok_btn = \
        {
            'XPATH': '//button[contains(@class, "ant-btn modal-foot-antd-button-licenseInfoCtl")]'
        }

    extreme_portal_login = \
        {
            'XPATH': '//input[@type="text"]'
        }

    extreme_portal_password = \
        {
            'XPATH': '//input[@type="password"]'
        }

    extreme_portal_login_button = \
        {
            'XPATH': '//input[@type="submit"]'
        }
