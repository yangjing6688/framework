

class CommonLoginWebElementsDefinitions:

    login_page_title = \
        {
            'DESC': 'Login Page Title',
            'XPATH': '//img[@class="logo-image" and @title="ExtremeCloud IQ Site Engine"]',
            
        }

    login_page_username_text = \
        {
            'DESC': 'Login Page Username TextField',
            'XPATH': '//input[@name="j_username"]',
            'wait_for': 20
         }

    login_page_password_text = \
        {
            'DESC': 'Login Page Password',
            'XPATH': '//input[@name="j_password"]',
            'wait_for': 5
         }

    login_page_login_button = \
        {
            'DESC': 'Login Page Submit Button',
            'XPATH': '//button[@type="submit"]',
            
        }

    login_page_error_message = \
        {
            'DESC': 'Login Page Error',
            'CSS_SELECTOR': '.login-form .errorString',
            
        }

    login_copyright_label = \
        {
            'DESC': 'Copyright Label',
            'XPATH': '//div[@class="footer"]/div[contains(text(), "Copyright")]',
            
        }

    login_support_link = \
        {
            'DESC': 'Support Link',
            'XPATH': '//div[@class="footer"]//a[text()="Support"]',
            
        }

    login_about_link = \
        {
            'DESC': 'About Link',
            'XPATH': '//div[@class="footer"]//a[text()="About"]',
            
        }
