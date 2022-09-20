class CIWebElementsDefs:
    cloud_integration = \
        {
            'XPATH': '//*[@data-automation-tag="CloudIntegration"]',
            'wait_for': 2
        }

    cloud_host_input = \
        {
            'XPATH': '//input[@type="text" and @class="ivu-input ivu-input-default" and \
             @placeholder="https://extremecloudiq.com"]',
            'wait_for': 2
        }

    cloud_admin = \
        {
            'XPATH': '//input[@type="text" and @class="ivu-input ivu-input-default" and \
             @placeholder="admin@example.com"]',
            'wait_for': 2
        }

    cloud_password = \
        {
            'XPATH': '//input[@type="password" and @class="ivu-input ivu-input-default"]',
            'wait_for': 2
        }

    cloud_link_button = \
        {
            'XPATH': '//*[@data-automation-tag="linkButton"]',
            'wait_for': 5
        }

    cloud_unlink_button = \
        {
            'XPATH': '//*[@data-automation-tag="unlinkButton"]',
            'wait_for': 5
        }